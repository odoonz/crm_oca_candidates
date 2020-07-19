# Copyright 2020 Graeme Gellatly
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Crm Lead Influencer",
    "description": """
        Allows to specify other involved contacts and their role in lead""",
    "version": "12.0.1.0.0",
    "license": "AGPL-3",
    "author": "Graeme Gellatly",
    "website": "https://o4sb.com",
    "depends": ["crm"],
    "data": [
        "security/ir.model.access.csv",
        "views/crm_lead_influencer_role.xml",
        "views/crm_lead.xml",
    ],
    "demo": [],
}
