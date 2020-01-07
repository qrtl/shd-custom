# Copyright 2019 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import jaconv

from odoo import models, fields, api


class HrEmployeePublic(models.Model):
    _inherit = 'hr.employee.public'

    family_name = fields.Char(
        'Family Name',
    )
    given_name = fields.Char(
        'Given Name',
    )
    furi_family_name = fields.Char(
        'Family Name Furigana',
    )
    furi_given_name = fields.Char(
        'Given Name Furigana',
    )
    employment_type_id = fields.Many2one(
        'hr.employment.type',
        string='Employment Type',
    )

    @api.onchange('family_name')
    def _onchange_family_name(self):
        if self.family_name:
            self.family_name = jaconv.h2z(
                self.family_name, ascii=True, digit=True)

    @api.onchange('given_name')
    def _onchange_given_name(self):
        if self.given_name:
            self.given_name = jaconv.h2z(
                self.given_name, ascii=True, digit=True)

    @api.onchange('furi_family_name')
    def _onchange_furi_family_name(self):
        if self.furi_family_name:
            self.furi_family_name = jaconv.z2h(
                jaconv.hira2kata(self.furi_family_name))

    @api.onchange('furi_given_name')
    def _onchange_furi_given_name(self):
        if self.furi_given_name:
            self.furi_given_name = jaconv.z2h(
                jaconv.hira2kata(self.furi_given_name))
