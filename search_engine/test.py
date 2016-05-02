#encoding=utf8
from core import *

test = search_core('./index.sum','./index.sum.brief')
print len(test.indexdict)
id_hash = test.query_recall('性能')
id_list = test.query_topn(id_hash,1)
print id_hash
print id_list
print test.output_brief(id_list)
id_hash = test.query_recall('上山打老虎')
id_list = test.query_topn(id_hash,10)
print id_hash
print id_list
print test.output_brief(id_list)
