# Copyright 2020 Graeme Gellatly
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import api, fields, models, _


class CrmLead(models.Model):

    _inherit = "crm.lead"

    def _update_salesperson(self):
        for lead in self:
            salesperson = lead.team_id.get_salesperson(lead, lead.stage_id)
            if salesperson:
                lead.user_id = salesperson

    def write(self, vals):
        res = super().write(vals)
        if vals.get("stage_id"):
            self._update_salesperson()
        return res

    @api.model_create_multi
    def create(self, vals_list):
        leads = super().create(vals_list)
        leads._update_salesperson()
        return leads

    def allocate_salesman(self, user_ids=None, team_id=False):
        if team_id and len(user_ids) != 1:
            team = self.env["crm.lead"].browse(team_id)
            for lead in self.env["crm.lead"].browse(self.ids):
                # Note we deliberately rebrowse to modify self
                salesperson = team.get_salesperson(lead, lead.stage_id)
                if salesperson:
                    lead.user_id = salesperson.id
                    self -= lead
        if self:
            return super(CrmLead, self).allocate_salesman(
                user_ids=user_ids, team_id=team_id
            )
