#encoding=utf-8
import jieba
import sys
import heapq
import cPickle as p

class search_core:
	def __init__(self,indexfile,indexbreiffile):
		self.indexfile = indexfile
		self.indexbreiffile = indexbreiffile
#load index -> dict[dict]
		f2 = file(self.indexfile)
		sum_dictlist = p.load(f2)
		f2.close()
		self.indexdict = {}
# word 1,23, list
		for word,id_list in sum_dictlist.items():
			tmp_hash = {}
			for i in range(0,len(id_list)):
				tmp_hash[id_list[i]] = ""
			self.indexdict[word] = tmp_hash
#load index breif -> dict[list]
		f3 = file(self.indexbreiffile)
		self.briefdict = p.load(f3)
        	f3.close()
	def reload(self,indexfile = "",indexbreiffile = ""):
#load index -> dict[dict]
		f2 = file(indexfile)
		sum_dictlist = p.load(f2)
		f2.close()
		tmp_indexdict = {}
# word 1,23, list
		for word,id_list in sum_dictlist.items():
			tmp_hash = {}
			for i in range(0,len(id_list)):
				tmp_hash[id_list[i]] = ""
			tmp_indexdict[word] = tmp_hash
#load index breif -> dict[list]
		f3 = file(indexbreiffile)
		tmp_briefdict = p.load(f3)
        	f3.close()
#reload index
		if (len(tmp_indexdict) > 0 and len(tmp_briefdict) > 0):
			self.indexfile = indexfile
			self.indexbreiffile = indexbreiffile
			self.indexdict.clear()
			self.briefdict.clear()
			self.indexdict = tmp_indexdict
			self.briefdict = tmp_briefdict

	def core_getbrief(self,id):
		if id in self.briefdict:
			return self.briefdict[id]
		else:
			return None
	def core_getids(self,word):
		if word in self.indexdict:
			return self.indexdict[word]
		else:
			return None
	def core_getscore(self,id):
		return int(id)
	def query_recall(self,query):
#cut words
		seg_list = jieba.cut(query)
		min_w = ""
		min_hash = {}
		min_count,i = 0,0
#get min count word->list
		for w in seg_list:
			i=i+1
			if self.core_getids(w) is None:
				return {}
			if i==1:
				min_w = w
				min_hash = self.core_getids(w)
				min_count = len(self.core_getids(w))
			else:
				if (len(self.core_getids(w)) < min_count):
					min_w = w
					min_hash = self.core_getids(w)
					min_count = len(self.core_getids(w))
#action and
		for w in seg_list:
			if self.core_getids(w) is None:
				return {}
			if min_w==w:
				continue
			else:
				cur_hash = self.core_getids(w)
				if len(cur_hash)>0:
					min_hash = dict.fromkeys(x for x in min_hash if x in cur_hash)
		return min_hash
	def query_topn(self,id_hash,startid):
		topn=startid+10
		sorted_list = []
#get all score
		for k in id_hash.keys():
#			if self.core_getids(k) is None:
#				del id_hash[k]
#				continue
			id_hash[k] = self.core_getscore(k)
#get max score topn(if list is large,may OOM,so best is top k sort in get_scoring,dodng todo)
		nlargestList = heapq.nlargest(topn,id_hash.values()) 
		for value in nlargestList:                                #输出结果  
			for key in id_hash.keys():  
        			if id_hash[key] == value:
					sorted_list.append(key)
				if (len(sorted_list) >= topn):
					return sorted_list[startid:]
		return sorted_list[startid:]
	def output_brief(self,id_list):
		brief_list = []
		for i in range(0,len(id_list)):
			tmp_list = self.core_getbrief(id_list[i])
			if tmp_list is not None:
				brief_list.append(tmp_list)
		return brief_list
            		  
			
