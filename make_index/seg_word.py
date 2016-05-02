#encoding=utf-8
import jieba
import sys
import cPickle as p

file_object = open(sys.argv[1])
dict_id = []
url_id = sys.argv[2]
try:
	all_the_text = file_object.read()
	seg_list = jieba.cut(all_the_text)
	for w in seg_list:
		dict_id.append((w,url_id))
	f = file('index_one_url', 'w')  
	p.dump(dict_id, f) # dump the object to a file  
finally:
	f.close()  
	file_object.close()
