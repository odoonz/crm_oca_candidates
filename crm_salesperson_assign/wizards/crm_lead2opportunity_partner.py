# Copyright 2020 Graeme Gellatly
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import api, fields, models, _


class CrmLead2opportunityPartner(models.TransientModel):

    _inherit = "crm.lead2opportunity.partner"

    @api.model
    def default_get(self, fields_list):
        """ Default get for name, opportunity_ids.
            In the transition for lead generation to
            opportunity we want to reassign the salesperson
        """
        result = super().default_get(fields_list)
        if self._context.get("active_id"):
            lead = self.env["crm.lead"].browse(self._context["active_id"])
            if lead.team_id or result.get("team_id"):
                team = lead.team_id or self.env["crm.team"].browse(result["team_id"])
                stage = lead._stage_find(
                    team_id=team.id,
                    domain=[("lead_type", "in", ["opportunity", "both"])],
                )
                salesperson = team.get_salesperson(lead, stage, self.env.user.id)
                if salesperson:
                    result["user_id"] = salesperson.id
        return result

    @api.onchange("team_id")
    def onchange_team_id(self):
        for lead_conversion in self:
            if lead_conversion.team_id:
                lead = self.env["crm.lead"].browse(self._context["active_id"])
                stage = lead._stage_find(
                    team_id=lead_conversion.team_id.id,
                    domain=[("lead_type", "in", ["opportunity", "both"])],
                )
                salesperson = lead_conversion.team_id.get_salesperson(
                    lead, stage, self.env.user.id
                )
                if salesperson:
                    lead_conversion.user_id = salesperson.id
