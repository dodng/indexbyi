#encoding=utf-8
import cPickle as p 
import os
import sys 

#py id id.html url_ori date

if os.path.exists('index.sum.brief') and os.path.getsize('index.sum.brief') > 0:
	f2 = file('index.sum.brief')  
	sum_dict2 = p.load(f2)
	f2.close()
else:
	sum_dict2 = {}

url_id = sys.argv[1]
url_html = sys.argv[2]
url = sys.argv[3]
date = sys.argv[4]

if url_id in sum_dict2:
	pass
else:
	tmp_list = []
	url_title = open(url_html+'.title').read().strip(' \n')
	url_head = open(url_html+'.header').read().strip(' \n')
	tmp_list.append(url_title)
	tmp_list.append(url_head)
	tmp_list.append(url)
	tmp_list.append(date)
	sum_dict2[url_id] = tmp_list
	f2 = file('index.sum.brief','w')  
	p.dump(sum_dict2, f2) # dump the object to a file
	f2.close()
#for i in range(0,len(storedlist)):
#	print storedlist[i][0].encode('utf-8')
