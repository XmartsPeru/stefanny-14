# -*- coding: utf-8 -*-
# Part of Odoo Module Developed by Cloudia Solutions S.A.C. | http://cloudia.pe | <info@cloudia.pe>
# Copyright (c) 2021 Cloudia Solutions S.A.C.
# See LICENSE and COPYRIGHT files for full copyright and licensing details.


from reactivex import create, of, operators as op
import asyncio
from PIL import Image
import urllib.request as urllib2

import logging

from odoo.tools import convert_file
from odoo import api, registry, SUPERUSER_ID

_logger = logging.getLogger(__name__)

DATA_MODULE = 'cs_init_enterprise_load_data'

UNISTALL_MODULE = [
    'partner_autocomplete', 'sms', 'snailmail'
]


def pre_init_hook(cr):
    _logger.info('CS Init Enterprise Config: pre_init_hook')
    env = api.Environment(cr, SUPERUSER_ID, {})

    Module = env['ir.module.module']
    # Install the last data
    data_module = Module.search([('name', '=', DATA_MODULE), ('state', '=', 'uninstalled')], limit=1)
    if data_module:
        data_module.button_install()

    Module.invalidate_cache(['state'])
    Module.flush()


def post_init_hook(cr, registry):
    _logger.info('CS Init Enterprise Config: post_init_hook')
    env = api.Environment(cr, SUPERUSER_ID, {})

    Module = env['ir.module.module']
    modules = Module.search([('name', 'in', UNISTALL_MODULE), ('state', '=', 'installed')])
    if modules:
        modules.button_uninstall()

    Module.invalidate_cache(['state'])
    Module.flush()
