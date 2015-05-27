#coding = utf-8
import urllib
import re
import code.rules
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
	
def test_getHtml():
	html = getHtml(r"htp://tieba.baidu.com/p/3779823764")	
	print getImg(html)

def test_andrules():
	l = [
		['<table class="fr_tablecontent">(.*?)</table.*?>',re.S],
		['<tr>(.*?)</tr>',re.S]
		]
	content = code.rules.get_buffer(r'test\test.txt')
	list1= code.rules.and_rules(l,content)
	print list1[0]
	print list1[1]
