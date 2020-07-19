# Copyright 2020 Graeme Gellatly
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import fields, models
from odoo.tools import safe_eval


class CrmTeam(models.Model):

    _inherit = "crm.team"

    team_assign_rule_ids = fields.One2many(
        comodel_name="crm.team.assign.rule", inverse_name="team_id"
    )

    def get_salesperson(self, lead, stage, user_id=None):
        if not user_id:
            user_id = lead.user_id.id if lead.user_id else self.env.user.id
        rule = self._find_assign_rule(lead, stage)
        if rule:
            return rule.get_salesperson(lead, user_id)

    def _find_assign_rule(self, lead, stage):
        search_domain = [("id", "=", lead.id)]
        for rule in self.team_assign_rule_ids.filtered(
            lambda s: not s.stage_to or s.stage_to == stage
        ):
            domain = safe_eval(rule.filter_domain or "[]") + search_domain
            applies = self.env["crm.lead"].search(domain, limit=1)
            if applies:
                return rule
        return None
