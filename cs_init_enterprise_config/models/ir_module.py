# -*- coding: utf-8 -*-
# Part of Odoo Module Developed by Cloudia Solutions S.A.C. | http://cloudia.pe | <info@cloudia.pe>
# Copyright (c) 2021 Cloudia Solutions S.A.C.
# See LICENSE and COPYRIGHT files for full copyright and licensing details.

from odoo import api, fields, models, _


env['ir.module.module'].search([('name', '=', 'board'), ('state', '=', 'uninstalled')]).button_install()
env['ir.module.module'].search([('name', '=', 'im_livechat_enterprise'), ('state', '=', 'uninstalled')]).button_install()
env['ir.module.module'].search([('name', '=', 'data_merge_utm'), ('state', '=', 'uninstalled')]).button_install()
env['ir.module.module'].search([('name', '=', 'hr_contract_reports'), ('state', '=', 'uninstalled')]).button_install()
env['ir.module.module'].search([('name', '=', 'hr_work_entry'), ('state', '=', 'uninstalled')]).button_install()
env['ir.module.module'].search([('name', '=', 'contacts_enterprise'), ('state', '=', 'uninstalled')]).button_install()
env['ir.module.module'].search([('name', '=', 'google_calendar'), ('state', '=', 'uninstalled')]).button_install()
env['ir.module.module'].search([('name', '=', 'google_spreadsheet'), ('state', '=', 'uninstalled')]).button_install()
env['ir.module.module'].search([('name', '=', 'hr_gamification'), ('state', '=', 'uninstalled')]).button_install()
env['ir.module.module'].search([('name', '=', 'hr_skills'), ('state', '=', 'uninstalled')]).button_install()
env['ir.module.module'].search([('name', '=', 'product'), ('state', '=', 'uninstalled')]).button_install()
env['ir.module.module'].search([('name', '=', 'barcodes_mobile'), ('state', '=', 'uninstalled')]).button_install()
env['ir.module.module'].search([('name', '=', 'base_automation_hr_contract'), ('state', '=', 'uninstalled')]).button_install()
env['ir.module.module'].search([('name', '=', 'link_tracker'), ('state', '=', 'uninstalled')]).button_install()
env['ir.module.module'].search([('name', '=', 'note'), ('state', '=', 'uninstalled')]).button_install()
env['ir.module.module'].search([('name', '=', 'timer'), ('state', '=', 'uninstalled')]).button_install()
env['ir.module.module'].search([('name', '=', 'base_import_module'), ('state', '=', 'uninstalled')]).button_install()
env['ir.module.module'].search([('name', '=', 'base_sparse_field'), ('state', '=', 'uninstalled')]).button_install()
env['ir.module.module'].search([('name', '=', 'attachment_indexation'), ('state', '=', 'uninstalled')]).button_install()
