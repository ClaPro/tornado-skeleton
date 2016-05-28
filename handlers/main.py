# -*- coding: utf-8 -*-
"""Resolve the basic html templates."""

import tornado.web


class MainHandler(tornado.web.RequestHandler):
    """Resolve the basic html templates."""

    # @tornado.web.authenticated
    def get(self):
        """Response to "GET /" with index.html."""
        self.render('index.html')
