#coding = gbk
import urllib
import re
import code
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

def test_and_rules():
	l = [
		['<table class="fr_tablecontent">(.*?)</table.*?>',re.S],
		['<tr>(.*?)</tr>',re.S]
		]
	content = code.rules.get_buffer(r'test\test.txt')
	list1= code.rules.and_rules(l,content)
	return list1
	
def test_or_rules():
	l = [
			['<td .*?>([^<].*?)</.*?>',0]
		]
	al =[
		['>([^<\n\t].*?)<',0]
	]
	test_str=				'<td style="width:30px; text-align:center;">1</td>\
							<td sort="Symbol" style="width:65px; text-align:left;"><input type="checkbox" fid="F00000044F"\ onchange="$msfr.OnCheckboxChange("F00000044F",this.checked);"/>110029</td>\
                            <td sort="Default" style="width:200px;text-align:left;"><a href="/quicktake/F00000044F" target="_blank">yyyy</a></td>\
                            <td sort="NAV" style="width:60px; text-align:center;">2.4754</td>\
                            <td sort="StarRating3" style="width:70px; text-align:left;"><img src="/common/images/smallstar5.gif" /><img\ src="/common/images/change2.gif" /></td>'
	print code.rules.or_rules(l,test_str)
	print code.rules.or_rules(al,test_str)
	