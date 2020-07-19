# Copyright 2020 Graeme Gellatly
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _


class CrmLeadInfluencerRole(models.Model):

    _name = "crm.lead.influencer.role"
    _description = "Influencer Role"

    name = fields.Char(required=True)
