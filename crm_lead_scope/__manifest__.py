# Copyright 2020 O4SB Ltd
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Crm Lead Scope Category',
    'description': """
        Adds a category to leads to define scope.""",
    'version': '12.0.1.0.0',
    'license': 'AGPL-3',
    'author': 'O4SB Ltd',
    'website': 'https://o4sb.com',
    'depends': [
        "crm"
    ],
    'data': [
        'views/crm_lead.xml',
        'security/ir.model.access.csv',
        'views/crm_lead_scope.xml',
    ],
    'demo': [
    ],
}
