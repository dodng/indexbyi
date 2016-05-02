# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import sys
import jieba

soup = BeautifulSoup(file(sys.argv[1]),"html.parser")

try:
	f1 = file(sys.argv[1]+".title",'w')
	f1.write(soup.title.string.encode('utf-8'))
	f1.close()
except:
	pass

try:
	f3 = file(sys.argv[1]+".header",'w')
	f3.write(soup.p.string[:190].encode('utf-8'))
	f3.close()
except:
	pass

try:
	f2 = file(sys.argv[1]+".content",'w')
	f2.write(soup.get_text().encode('utf-8'))
	f2.close()
except:
	pass
