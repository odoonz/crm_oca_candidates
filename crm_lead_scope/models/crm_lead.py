# Copyright 2020 Graeme Gellatly
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _


class CrmLead(models.Model):

    _inherit = 'crm.lead'

    scope_id = fields.Many2one(comodel_name='crm.lead.scope', string='Scope')
