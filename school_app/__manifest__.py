# -*- coding: utf-8 -*-
{
    'name': "school_app",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','product','contacts'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/student.xml',
        'views/course.xml',
        'views/professor.xml',
        'views/update_contacts_views.xml',
        'views/replace_class_values.xml',
	   'reports/professor_template.xml',
        'reports/reports.xml',
        'reports/sale_order_report_inherit.xml',
        'reports/delievery_slip_inherit_report.xml',
        'wizard/professor_wizard_view.xml'
        
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable':True,
    'application':False,
    'auto-install':False
}
