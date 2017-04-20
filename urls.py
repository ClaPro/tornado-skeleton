# -*- coding: utf-8 -*-

from handlers import main


url_patterns = [
    (r"/", main.MainHandler),
]
