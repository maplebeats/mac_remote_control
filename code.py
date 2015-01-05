#!/usr/bin/env python

import web

urls = (
        "/","index"
        )

class index:
    def GET(self):
        return "hello world"

app = web.application(urls, globals())
app.run()

