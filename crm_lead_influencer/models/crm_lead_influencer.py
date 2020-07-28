# Copyright 2020 Graeme Gellatly
# License LGPL-3 or later (http://www.gnu.org/licenses/lgpl).

from odoo import api, fields, models, _


class CrmLeadInfluencer(models.Model):

    _name = "crm.lead.influencer"
    _description = "Influencer"
    _order = "sequence, id"

    lead_id = fields.Many2one("crm.lead", string="Lead")
    role_id = fields.Many2one("crm.lead.influencer.role", string="Role")
    partner_id = fields.Many2one("res.partner", string="Partner")
    phone = fields.Char("Phone")
    mobile = fields.Char("Mobile")
    name = fields.Char(string="Company Name")
    contact_name = fields.Char()
    email = fields.Char()
    note = fields.Text()
    sequence = fields.Integer(default=10)

    @api.onchange("partner_id")
    def onchange_partner(self):
        if self.partner_id:
            self.phone = self.partner_id.phone
            self.mobile = self.partner_id.mobile
            self.contact_name = self.partner_id.name
            self.name = self.partner_id.parent_id.name
            self.email = self.partner_id.email
