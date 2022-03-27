# -*- coding: utf-8 -*-
# Part of Odoo Module Developed by Cloudia Solutions S.A.C. | http://cloudia.pe | <info@cloudia.pe>
# Copyright (c) 2021 Cloudia Solutions S.A.C.
# See LICENSE and COPYRIGHT files for full copyright and licensing details.

import json
from odoo import http
from odoo.http import request


class CompanyLogo(http.Controller):

    @http.route(['/check_company_logo'], type='http', auth="public", methods=['GET'], website=True, sitemap=False)
    def check_company_logo(self, company_id=0):
        has_logo = bool(request.env['res.company'].browse(int(company_id)).logo)

        return json.dumps({
            'has_logo': has_logo,
        }, ensure_ascii=False)
