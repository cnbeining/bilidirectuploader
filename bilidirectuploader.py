#!/usr/bin/env python3
#coding:utf-8
# Author:  Beining --<ACICFG>
# Purpose:  Upload to Bilibili via Bilibili's internal uploading method
# Created: 10/01/2014

#python3 bilidirectuploader.py 0.flv 1.flv

import urllib.request
import sys
import os
import json
import subprocess
import hashlib
import requests

global cookiepath
cookiepath = './bilicookies'
global video_list
video_list = ''


#----------------------------------------------------------------------
def upload(file2Upload):
    """"""
    #Read Cookie.....Damn it I didn't have my supper!
    try:
        cookies = open(cookiepath, 'r').readline()
        #print(cookies)
    except:
        print('I am hungry, please give me your Cookie!')
        exit()
    #Get filename
    if not os.path.isfile(file2Upload):
        print('Not file!')
        pass    
    if os.path.splitext(file2Upload)[1] != '.flv':
        print('ERROR: You can only upload .flv file(s)!')
        exit()
    filename = os.path.basename(file2Upload)
    #print(filename)
    #Calculate Filesize, since there s 1.4GiB limit
    filesize = os.path.getsize(file2Upload)
    print('Size of file: ' + str(filesize))
    if filesize > (1.4 * 1024 * 1024 * 1024):
        print('File larger than 1.4 GiB, unable to upload!')
        exit()
    #Fetch UploadUrl
    request_full = urllib.request.Request('http://member.bilibili.com/get_vupload_url', headers={ 'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36', 'Cache-Control': 'no-cache', 'Pragma': 'no-cache' , 'Cookie': cookies,})
    try:
        response = urllib.request.urlopen(request_full)
    except Exception:
        print('Cannot get response from server!')
        pass
    data = response.read()
    uploadresponse = json.loads(data.decode('utf-8'))
    try:        # if error happens...
        uploadresponse["error_code"]
    except KeyError:
        pass
    except:
        print('ERROR: '+ uploadresponse['error_msg'] + ', ' + str(uploadresponse["error_code"]))
        sys.exit() # exit the program
    #print(uploadresponse['url'])
    #make filename
    server_ip = str(uploadresponse['server_ip'])
    remote_file_name = str(uploadresponse['file_name'])
    #start upload
    upload_url = str(uploadresponse['url'])
    #print(upload_url)
    f = open(file2Upload, 'rb')
    c = 0
    for piece in read_in_chunks(f):
        headers_post = {'content-type': 'multipart/form-data', 'Content-Length': '524288', 'Content-Range': 'bytes ' + str(c * 524288) + '-' + str((c + 1) * 524288) + '/' + str(filesize),}
        requests.options(upload_url)  #dont really know why
        files = {'file': piece}
        r = requests.post(upload_url, files=files, headers = headers_post)
        c = c + 1
        
        print(str(c * 524288) + '/' + str(filesize) + ' done...')
    #video_list = video_list + (str('[vupload]' + remote_file_name + ';' + filename + ';' + server_ip + ';[/vupload]\n'))
    print('\n'+'Hope everything is fine. '+ '\n' + '[vupload]' + remote_file_name + ';' + filename + ';' + server_ip + ';[/vupload]')

#----------------------------------------------------------------------

def read_in_chunks(file_object, chunk_size=524288):
    """Lazy function (generator) to read a file piece by piece.
    Default chunk size: 524288."""
    while True:
        data = file_object.read(chunk_size)
        if not data:
            break
        yield data

#----------------------------------------------------------------------
if __name__=='__main__':
    #Test sys encoding
    if not sys.getdefaultencoding() is 'utf-8':
        os.system('export LC_ALL="en_US.UTF-8"')
    total_file_num = len(sys.argv[1:])
    i = 0
    if len(sys.argv[1:]) == 0:
        print('''
        Author: Beining http://www.cnbeining.com https://github.com/cnbeining
        
        Require: requests
        
        Usage:
        python3 bilidirectuploader.py [file1]  [file2]  [file3]...
        You can only upload .flv file(s) under 1.4 GiB.
        
        If network is bad, change chunk size at L85, and display at L78.
        ''')
    for name in sys.argv[1:]:
        #print(name)
        i = i + 1
        print('Uploading '+ str(i)+' in '+str(total_file_num)+' files...')
        upload(name)
    if len(video_list) != 0:
        print(video_list)
