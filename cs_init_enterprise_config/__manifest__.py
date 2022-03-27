# -*- coding: utf-8 -*-
# Part of Odoo Module Developed by Cloudia Solutions S.A.C. | http://cloudia.pe | <info@cloudia.pe>
# Copyright (c) 2021 Cloudia Solutions S.A.C.
# See LICENSE and COPYRIGHT files for full copyright and licensing details.

{
    'name': 'Initial configuration - Base (Xmarts Peru)',
    'summary': 'Base: Initial configuration',
    'author': 'Xmarts Peru',
    'category': 'Xmarts',
    'version': '14.0.0.1',
    'license': 'OPL-1',
    'description': """
    """,

    'depends': [
        'web_enterprise',
    ],

    "qweb": [
        'static/src/xml/templates.xml',
    ],

    'support': 'soporte@cloudia.pe',
    'application': False,
    'installable': True,
    'auto_install': True,
    'pre_init_hook': 'pre_init_hook',
    'post_init_hook': 'post_init_hook',
}
