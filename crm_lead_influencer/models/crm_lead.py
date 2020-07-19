# Copyright 2020 Graeme Gellatly
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _


class CrmLead(models.Model):

    _inherit = "crm.lead"

    influencer_ids = fields.One2many(
        comodel_name="crm.lead.influencer",
        inverse_name="lead_id",
        string="Influencers",
    )
