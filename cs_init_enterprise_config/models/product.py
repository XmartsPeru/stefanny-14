# -*- coding: utf-8 -*-
# Part of Odoo Module Developed by Cloudia Solutions S.A.C. | http://cloudia.pe | <info@cloudia.pe>
# Copyright (c) 2021 Cloudia Solutions S.A.C.
# See LICENSE and COPYRIGHT files for full copyright and licensing details.

from odoo import fields, models


class ProductProduct(models.Model):
    _inherit = "product.product"
    _order = "default_code, id"


class ProductTemplate(models.Model):
    _inherit = "product.template"
    _order = "default_code, id"

    default_code = fields.Char(index=True)
