#!/usr/bin/env python

import json, sys

from pprint import pprint

from ws4py.client.threadedclient import WebSocketClient


class MopidyClient(WebSocketClient):
    def opened(self):
        data = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "core.describe"
        }

        self.send(json.dumps(data))

    def closed(self, code, reason=None):
        print "Closed down", code, reason

    def received_message(self, m):
        pprint(json.loads(m.data))
        return m

if __name__ == '__main__':
    try:
        ws = MopidyClient("ws://localhost:6680/mopidy/ws/")
        ws.connect()
        #ws.join()
        #ws.send(json.dumps({"jsonrpc": "2.0", "id": 1, "method": sys.argv[1]}))
    except KeyboardInterrupt:
        ws.close()
