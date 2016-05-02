__Indexbyi a http server which providing full-text search__

It is a tiny but complete full-text search http server (include make index,search engine,http server)

##0.What to do 

a:Quick and convenient to build a http server (which Only belong to you ) 

b:Help you to understand the required modules of a full-text search system (like www.google.com)
Small as the sparrow is, it possesses all its internal organs -- small but complete

c:an exmple:http://www.indexbyi.com:8199/

![an exmple](https://github.com/dodng/indexbyi/blob/master/doc/indexbyi_example1.png)

##1 Technical Architecture

![major modules architecture](https://github.com/dodng/indexbyi/blob/master/doc/indexbyi.png)

##2 code Architecture

make_index

	|_url.seed (url list which will be added into index)
	
	|_url.seed.here(url list which already being added into index)
	
	|_make_index.sh(make_index contronl shell bash)
	
	|_parse_html.py(use python third lib beautifulsoup to change html to text content)
	
	|_seg_word.py(use python third lib jieba to cut a text to many words)
	
	|_merge_index.py(merge already exist index and the just generated to the index)
	
	|_dump_brief.py(dump the url breif to display info)
	
search_engine

	|_core.py(use the index file and search policy to provide full-text search funtion)
	
	|_test.py(a example to just use the search_engine to test)
	
http_server

	|_index.html(Front-end use AJAX to get json from ui.py and display info)
	
	|_ui.py(use python third lib tornado to provide http server (include search_engine))
	
	
##3.how to work

a:add and edit the url.feed

b:use linux bash to start make_index.sh to gen index files

c:move index files to the right path(core.py have the path)

d:start the ui.py(You have to install tornado first)

-----------------------------------------------------------

author email:dodng12@163.com

welcome to any problems.

If it can help you,I will be very happy.
