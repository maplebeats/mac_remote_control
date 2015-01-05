#!/usr/bin/env python
# -*- coding: utf-8 -*-  
import web
import apple
import urllib

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

urls = (
        "/","index",
        "/favicon.ico","favicon",
        "/click","click",
        "/active","active"
        )

class click:
    def GET(self):
        i = web.input()
        key = i.get('key')
        print("click %s" % key)
        ret = apple.keystroke(key)
        return ret

class active:
    def GET(self):
        i = web.input()
        #app = "搜狐影音"
        app=i.app
        print(app)
        ret = apple.active(app)
        return ret

class favicon:
    def GET(self):
        return 0x11111111111

class index:
    def GET(self):
        web.redirect("/static/main.html")

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
