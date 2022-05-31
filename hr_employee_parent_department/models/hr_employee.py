# Copyright 2022 Quartile Limited
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import _, api, fields, models


class HrEmployee(models.Model):
    _inherit = ["hr.employee"]

    top_dept_id = fields.Many2one(
        'hr.department',
        string="Top Dept",
        compute='_compute_parent_department',
        help="Company",
        )

    @api.depends('department_id')
    def _compute_parent_department(self):
        for employee in self:
            employee.top_dept_id = False  # たしか14.0だとFalseの場合でも明示的に指定が必要なのではじめにこの行を設けておく
            top_dept = employee.department_id
            if not top_dept:
                continue
            parent = top_dept.parent_id
            while parent:
                top_dept = parent
                parent = top_dept.parent_id
            employee.top_dept_id = top_dept
