#!/usr/bin/python  
# -*- coding:utf-8 -*-  
import urllib
import urllib2

def getRemoteFileSize(url):
    #content-length头即为远程文件大小
    opener = urllib2.build_opener()
    try:
        request = urllib2.Request(url)
        response = opener.open(request)
        response.read()
    except:
        return 0;
    
    fileSize = dict(response.headers).get('content-length',0)
    return int(fileSize)

fuli = open('fuli.txt')
count = 80
for url in fuli:
   print url
   if url[:4] == 'http': 
       try:
           if(getRemoteFileSize(url) != 0):
               urllib.urlretrieve(url,"%d.mov"%count)
               count +=1
       except:
           print 'error'
           continue

    