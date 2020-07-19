# Copyright 2020 Graeme Gellatly
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import fields, models
from random import choice


class CrmTeamAssignRule(models.Model):

    _name = "crm.team.assign.rule"
    _rec_name = "filter_domain"
    _description = "CRM Team Assignation Rule"
    _order = "sequence asc"

    sequence = fields.Integer(default=10)
    team_id = fields.Many2one(comodel_name="crm.team")
    filter_domain = fields.Char(
        string="Apply on",
        help="If present, this condition must be satisfied before executing the action rule.",
    )
    user_ids = fields.Many2many(
        comodel_name="res.users", string="Assign To", required=True
    )
    no_force = fields.Boolean(
        string="Do not Force Reassign",
        help="If the currently assigned user is a valid choice, do not reassign",
    )
    stage_to = fields.Many2one(comodel_name="crm.stage", string="Next Stage")
    assign_method = fields.Selection(
        selection=[("random", "Random")], required=True, default="random"
    )

    def _get_salesperson_random(self):
        return choice(self.user_ids)

    def get_salesperson(self, lead=False, user_id=False):
        self.ensure_one()
        if len(self.user_ids) == 1:
            return self.user_ids
        if user_id and self.no_force and user_id in self.user_ids.ids:
            return self.env["res.users"].browse(user_id)
        if lead and self.no_force and lead.user_id in self.user_ids:
            return lead.user_id
        # We implement a dispatcher here to allow for easy
        # future extension of other assigning methods such as
        # round-robin or equal weighting
        return getattr(
            self,
            "_get_salesperson_{}".format(self.assign_method),
            self._get_salesperson_random,
        )()
