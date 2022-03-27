# -*- coding: utf-8 -*-
# Part of Odoo Module Developed by Cloudia Solutions S.A.C. | http://cloudia.pe | <info@cloudia.pe>
# Copyright (c) 2021 Cloudia Solutions S.A.C.
# See LICENSE and COPYRIGHT files for full copyright and licensing details.

{
    'name': 'ZCS Data - Base (Xmarts Peru)',
    'summary': 'Base: Data configuration',
    'author': 'Xmarts Peru',
    'category': 'Xmarts',
    'version': '14.0.0.1',
    'license': 'OPL-1',
    'description': """
    """,
    'depends': [
        'product', 'attachment_indexation', 'im_livechat_enterprise', 'data_merge_utm', 'hr_contract_reports',
        'hr_work_entry', 'contacts_enterprise', 'google_calendar', 'google_spreadsheet', 'hr_gamification', 'hr_skills',
        'barcodes_mobile', 'base_automation_hr_contract', 'link_tracker', 'note', 'timer', 'base_import_module',
        'base_sparse_field',
    ],

    'data': [
        'data/ir_ui_menu_data.xml',
        'data/res_lang_data.xml',
        'data/res_country_data.xml',
        'data/res_country_group_data.xml',
        'data/res_currency_data.xml',
        'data/res_company_data.xml',
        'data/res_users_data.xml',
        'data/res_partner_industry_data.xml',
        'data/res_partner_data.xml',
        'data/res_bank_data.xml',
        'data/res_config_data.xml',
        'data/ir_default.xml',
        'data/ir_module_category_data.xml',
        # 'views/list_view_sticky_header.xml',
        # 'views/resources.xml',
    ],

    'support': 'soporte@cloudia.pe',
}
