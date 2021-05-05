# -*- coding: utf-8 -*-
# from odoo import http


# class SchoolApp(http.Controller):
#     @http.route('/school_app/school_app/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/school_app/school_app/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('school_app.listing', {
#             'root': '/school_app/school_app',
#             'objects': http.request.env['school_app.school_app'].search([]),
#         })

#     @http.route('/school_app/school_app/objects/<model("school_app.school_app"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('school_app.object', {
#             'object': obj
#         })
