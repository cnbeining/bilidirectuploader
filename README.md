bilidirectuploader
==================

Upload to Bilibili via Bilibili's internal uploading method.

二压等待别人研究了。


Usage
--------
需要Python3和requests。没这货自己手打一个POST包太闹心，更别提OPTIONS了。

查阅https://pypi.python.org/pypi/requests/  。

cookie文件名是./bilicookies  .

格式：`DedeUserID=******;DedeUserID__ckMd5=*******;SESSDATA=*******`

运行 `python3 bilidirectuploader.py [FILENAME1] [FILENAME2]` 开始上传. 

写死了，只能传1.4GiB文件。

写了个最简略的进度。

如果网络特别差，手工改一下分片大小。懒得再写命令行解析了。


Misc
----
* 还是晚上写的，有问题谅解，也没做PEP-8，随便看看吧。
* 禁止转载到**墙内**各种电子公告服务（包括但不限于百毒贴吧、AC 丧尸岛、各种论坛、微博等）。发现腿打折。之前不是没有过先例。
* GNU v2开源。吃我大传染性吧。顺便治治大陆不尊重开源协议的货。


作者
----
Beining http://www.cnbeining.com https://github.com/cnbeining

有问题开issue最快，因为直接邮件通知。去Blog留言也可以。

私人联系方式...有的人自然有。

#### 小提示
* 完成后程序自动输出投稿代码，格式 [vupload]114fc72082dee72ec81c041e5191f1b0;t.flv;2;[/vupload]
* 代码投稿后，立即编辑，会看见代码变成 [vupload]vupload_2393890[/vupload]
* 后面的数字就是cid，用两个interface的API可以查转码进度。
* 这些服务器速度不怎么样，自便吧。