# coding=gbk
import re
import os,sys
import urllib2
def get_buffer(filename):
	fd = open(filename)
	all_text = None
	try:
		all_text = fd.read()
	finally:
		fd.close()
	return all_text

def and_rules(rule_list,astr):
	str_list = [astr]
	for rule in rule_list:
		tmp_list = []
		patt = re.compile(rule[0],rule[1])
		for sstr in str_list:
			tmp_list.extend(re.findall(patt,sstr))
		str_list = tmp_list
	
	return str_list

def or_rules(rule_list,astr):
	ret = []
	for rule in rule_list:
		patt = re.compile(rule[0],rule[1])
		tmp_list = re.findall(patt,astr)
		ret.extend(tmp_list)
	return ret
	
def getHtml(url):
	page = urllib2.urlopen(url)
	html = page.read()
	return html
def get_content():
	url = get_buffer('url.txt')
	if url :
		return getHtml(url)
def display_all(list_list):
	print ' 排名  代码        名称         净值     波动   评价  晨星风险系数  评价  最近三年(夏普比率) 评价  总回报  3年 变化  5年 变化'
	for list in list_list:
		print '%3s%8s%24s%8s%8s%4s%10s%10s%6s%16s%8s%4s%4s%4s%4s'%(list[0],list[1],list[2],list[3],list[4],list[5],list[6],list[7],list[8],\
	list[9],list[10],list[11],list[12],list[13],list[14])
def get_data():
	content = get_content()
	if not content:
		print 'url is not available'
	and_ = [
			['<table class="fr_tablecontent">(.*?)</table.*?>',re.S],
			['<tr>(.*?)</tr>',re.S],
		]
	table_content= and_rules(and_,content)
	or_ = [['>([^<\n\t-].*?)<',0] ,
			['(\d).gif',0] 
			]
	core_data = []
	for row_data in table_content:
		core_data.append(or_rules(or_,row_data))
	display_all(core_data[:-1])
	print ''
	