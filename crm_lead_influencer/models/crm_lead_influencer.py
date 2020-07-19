# Copyright 2020 Graeme Gellatly
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _


class CrmLeadInfluencer(models.Model):

    _name = "crm.lead.influencer"
    _description = "Influencer"

    lead_id = fields.Many2one("crm.lead", string="Lead")
    role_id = fields.Many2one("crm.lead.influencer.role", string="Role")
    partner_id = fields.Many2one("res.partner", string="Partner")
    phone = fields.Char("Phone")
    mobile = fields.Char("Mobile")
    name = fields.Char()
    email = fields.Char()
    note = fields.Text()

    @api.onchange("partner_id")
    def onchange_partner(self):
        if self.partner_id:
            self.phone = self.partner_id.phone
            self.mobile = self.partner_id.mobile
            self.name = self.partner_id.name
            self.email = self.partner_id.email
