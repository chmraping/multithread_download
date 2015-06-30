# coding=utf-8
import urllib
import urllib2
import threading


def getRemoteFileSize(url):
	#content-length头即为远程文件大小
	opener = urllib2.build_opener()
	try:
		request = urllib2.Request(url)
		response = opener.open(request)
		response.read()
	except:
		return 0;

	fileSize = dict(response.headers).get('content-length', 0)
	return int(fileSize)


def downloadFile(url):
	global count
	sz = getRemoteFileSize(url)
	if (sz != 0):
		print sz
		lock.acquire()
		try:
			tmp_count = count
			count += 1
		finally:
			lock.release()
		try:
			print "download %d.mov" % tmp_count
			urllib.urlretrieve(url, "%d.mov" % tmp_count)
			print "download %d.mov success" % tmp_count
		except Exception,e:
			print "error %d.mov success" %tmp_count
			print e



count = 0
lock = threading.Lock()
fuli = open('fuli.txt')
for url in fuli:
	print url
	if url[:4] == 'http':
		threading.Thread(target=downloadFile, args=(url,)).start()


