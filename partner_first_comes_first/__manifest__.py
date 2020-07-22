# Copyright 2020 Graeme Gellatly
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

{
    'name': 'First Comes First',
    'summary': """
        Puts first name first on partner_firstname modules""",
    'version': '12.0.1.0.0',
    'license': 'LGPL-3',
    'author': 'Graeme Gellatly',
    'website': 'https://o4sb.com',
    'depends': [
        "partner_firstname",
    ],
    'data': [
        "views/res_partner.xml",
    ],

}
