# Copyright 2020 Graeme Gellatly
# License LGPL-3 or later (http://www.gnu.org/licenses/lgpl).

from odoo import api, fields, models, _


class CrmLeadInfluencerRole(models.Model):

    _name = "crm.lead.influencer.role"
    _description = "Influencer Role"

    name = fields.Char(required=True)
