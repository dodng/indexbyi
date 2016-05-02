#encoding=utf-8
import cPickle as p 
import os 

f = file('index_one_url')  
storedlist = p.load(f) 

if os.path.exists('index.sum') and os.path.getsize('index.sum') > 0:
	f2 = file('index.sum')  
	sum_dict2 = p.load(f2)
	f2.close()
	f2 = file('index.sum','w')  
else:
	f2 = file('index.sum','w')  
	sum_dict2 = {}

#word,url_id pair
for i in range(0,len(storedlist)):
	if storedlist[i][0] in sum_dict2:
		tmp_list = sum_dict2[storedlist[i][0]]
		for j in range(0,len(tmp_list)):
			if tmp_list[j] == storedlist[i][1]:
				break;
			elif (j == len(tmp_list) -1):
				tmp_list.append(storedlist[i][1])
				sum_dict2[storedlist[i][0]] = tmp_list
				break;
			else:
				continue;
	else:
		tmp_list = []
		tmp_list.append(storedlist[i][1])
		sum_dict2[storedlist[i][0]] = tmp_list

p.dump(sum_dict2, f2) # dump the object to a file
#for i in range(0,len(storedlist)):
#	print storedlist[i][0].encode('utf-8')
