# Copyright 2020 O4SB Ltd
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _


class CrmLead(models.Model):

    _inherit = 'crm.lead'

    @api.model_create_multi
    def create(self, vals_list):
        for record in vals_list:
            partner = record.get("partner_id")
            if partner:
                continue
            if record.get("email_from"):
                partner = self.env["res.partner"].search(
                    [("email", "=", record["email_from"])], limit=1
                )
            if (
                not partner
                and record.get("contact_lastname")
                and record.get("contact_name")
            ):
                partner = self.env["res.partner"].search(
                    [
                        ("lastname", "=", record["contact_lastname"]),
                        ("firstname", "=", record["contact_name"]),
                    ],
                    limit=1,
                )
            if partner:
                record.update(partner_id=partner.id)
        return super().create(vals_list)
