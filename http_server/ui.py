import tornado.ioloop
import tornado.web
import search_engine.core

search_eng = search_engine.core.search_core('./index_byi/index.sum','./index_byi/index.sum.brief')

class SearchHandler(tornado.web.RequestHandler):
	def get(self):
		json_ct = {}
		query = self.get_argument("query")
		startid_ori = self.get_argument("startid")
		if startid_ori.isdigit():
			startid = int(startid_ori)
			if startid <= 0:
				startid = 0
		else:
			startid = 0
#start id is no num,and num
		id_hash = search_eng.query_recall(query)
		id_list = search_eng.query_topn(id_hash,startid)
		json_ct["content_sum"] = len(id_hash)
		json_ct["content_num"] = len(id_list)
		json_ct["content_startid"] = startid
		json_ct["content"] = search_eng.output_brief(id_list)
		self.write(json_ct)


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")



def make_app():
		return tornado.web.Application([
(r"/s", SearchHandler), 
(r"/", MainHandler)])

if __name__ == "__main__":
	app = make_app()
	app.listen(8199)
	tornado.ioloop.IOLoop.current().start()
