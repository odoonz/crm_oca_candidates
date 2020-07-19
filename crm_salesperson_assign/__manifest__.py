# Copyright 2020 Graeme Gellatly
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

{
    "name": "Crm Salesperson Assign",
    "summary": """
        Rules to assign salepeople to leads and opportunities""",
    "version": "12.0.1.0.0",
    "license": "LGPL-3",
    "author": "Graeme Gellatly",
    "website": "https://o4sb.com",
    "depends": ["crm", "sales_team",],
    "data": ["security/ir.model.access.csv", "views/crm_team.xml",],
}
