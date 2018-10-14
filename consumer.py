import gevent
from gevent.pywsgi import WSGIServer

from consumer_api import api

if __name__ == '__main__':
    api_server = WSGIServer(("0.0.0.0", 9001), api)
    api_server.start()

    while True:
        gevent.sleep(60)
