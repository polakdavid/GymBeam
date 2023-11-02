# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Employees Case Study',
    'version': '1.0',
    'summary': 'Centralize employee information',
    'description': "",

    'depends': [
        'base_setup',
        'mail',
        'resource',
        'web',
        'mail_bot',
    ],

    'data': [
        'views/hr_employee_views.xml',
        'views/res_users.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
