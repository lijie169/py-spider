import re
import os,sys

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
				