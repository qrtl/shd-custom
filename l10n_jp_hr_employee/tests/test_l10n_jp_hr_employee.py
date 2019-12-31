# Copyright 2019 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo.tests import common


class L10nJpHrEmployee(common.TransactionCase):

    def setUp(self):
        super(L10nJpHrEmployee, self).setUp()
        # Demo user
        self.test_user = self.env.ref('base.user_demo')
        # Employee record that linked to Demo user
        self.test_employee = self.env.ref('hr.employee_qdp')

    def test_00_create_dependant_information(self):
        self.env['hr.dependant'].with_user(self.test_user.id).create({
            'employee_id': self.test_employee.id,
            'dependant_categ': '01_spouse',
            'gender': 'male',
            'residence_categ': 'together',
            'income': 0,
            'birthday': '2000-01-01',
            'furi_name': 'ﾔﾏﾀﾞ ﾀﾛｳ',
            'name': '山田 太郎',
        })

    def test_01_create_hr_qualification(self):
        self.env['hr.qualification'].with_user(self.test_user.id).create({
            'employee_id': self.test_employee.id,
            'name': 'CISA',
            'date_obtained': '2000-01-01',
        })
