# Copyright 2022 Quartile Limited
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import fields, models


class HrEmployee(models.Model):
    _inherit = "hr.employee"

    parent_department = fields.Many2one('hr.department')

    # @api.depend('hr.department')
