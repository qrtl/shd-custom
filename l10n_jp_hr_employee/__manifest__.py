# Copyright 2019 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Extension to Employees for Japan",
    "description": """
    """,
    "version": "13.0.1.0.0",
    "category": "Localization",
    "website": "https://www.quartile.co/",
    "author": "Quartile Limited",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "hr",
        "hr_contract",
    ],
    'external_dependencies': {
        'python': [
            'jaconv>=0.2.4'
        ]
    },
    "data": [
        'security/res_groups.xml',
        'security/ir.model.access.csv',
        'security/hr_security.xml',
        'data/hr_employment_type_data.xml',
        'data/mail_template_data.xml',
        'views/hr_employee_views.xml',
        'views/hr_qualification_views.xml',
        'views/hr_dependant_views.xml',
    ],
}
