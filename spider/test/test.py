#coding = utf-8
import urllib
import re

def getHtml(url):
	page = urllib.urlopen(url)
	html = page.read()
	return html

def getImg(html):
	reg = '<div .*? class=\"d_post_content j_d_post_content \">(.*?)</div>'
	imgre = re.compile(reg)
	imglist = re.findall(imgre,html)
	x = 0
	return re.sub('<br>','\n',imglist[0])
	

html = getHtml(r"http://tieba.baidu.com/p/3779823764")
print getImg(html)