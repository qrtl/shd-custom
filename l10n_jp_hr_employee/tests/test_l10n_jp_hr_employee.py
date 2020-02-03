# Copyright 2019-2020 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo.tests import common
from odoo.exceptions import AccessError


class L10nJpHrEmployee(common.TransactionCase):

    def setUp(self):
        super(L10nJpHrEmployee, self).setUp()
        # Demo user
        self.test_user = self.env.ref('base.user_demo')
        # Employee record that linked to Demo user
        self.test_employee = self.env.ref('hr.employee_qdp')

    def test_00_update_own_private_info_without_self_edit(self):
         # User should not be able to update SELF_READABLE_FIELDS when
         # hr_employee_self_edit is not True
        self.env['ir.config_parameter'].sudo().set_param(
            'hr.hr_employee_self_edit', False)
        with self.assertRaises(AccessError):
            self.test_user.with_user(self.test_user).write({
                'private_phone': '1133334444',
                'private_email': 'test@odoo.com',
                'roman_family_name': 'YAMADA',
                'roman_given_name': 'TAROU',
            })

    def test_01_update_own_private_info_with_self_edit(self):
         # User should be able to update SELF_READABLE_FIELDS when
         # hr_employee_self_edit is True
        self.env['ir.config_parameter'].sudo().set_param(
            'hr.hr_employee_self_edit', True)
        self.test_user.with_user(self.test_user).write({
            'private_phone': '1133334444',
            'private_email': 'test@odoo.com',
            'roman_family_name': 'YAMADA',
            'roman_given_name': 'TAROU',
        })

    def test_02_create_dependant_information(self):
        self.env['hr.dependant'].with_user(self.test_user).create({
            'employee_id': self.test_employee.id,
            'dependant_categ': '01_spouse',
            'gender': 'male',
            'residence_categ': 'together',
            'income': 0,
            'birthday': '2000-01-01',
            'furi_name': 'ﾔﾏﾀﾞ ﾀﾛｳ',
            'name': '山田 太郎',
        })

    def test_03_create_hr_qualification(self):
        self.env['hr.qualification'].with_user(self.test_user).create({
            'employee_id': self.test_employee.id,
            'name': 'CISA',
            'date_obtained': '2000-01-01',
        })
