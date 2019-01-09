import json
import os 
he_data = json.load(open('he_data.json'))

data = []
geoCoordMap = {}
for idx, item in enumerate(he_data):
    data.append({"name":item['_id'], "value": item['room_price']})
    geoCoordMap[item['_id']] = [item['lng'],item['lat']]

# json.dump(data,open('data.json',mode='w'))
# json.dump(geoCoordMap,open('geoCoordMap.json',mode='w'))


import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
         self.render("index.html",  data=json.dumps(data) , geoCoordMap=json.dumps(geoCoordMap))

def make_app():
    print(os.path.join(os.path.dirname(__file__), "static"))

    return tornado.web.Application([
        (r"/", MainHandler),
    ],
    static_path=os.path.join(os.path.dirname(__file__), "static"),
    )

if __name__ == "__main__":
    app = make_app()
    app.listen(8889)
    tornado.ioloop.IOLoop.current().start()
