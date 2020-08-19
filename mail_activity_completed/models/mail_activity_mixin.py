# Copyright 2020 Civiq Pty Ltd
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _

class MailActivityMixin(models.AbstractModel):

    _inherit = 'mail.activity.mixin'

    activity_date_done = fields.Date(
        'Last Activity Completed',
        compute='_compute_activity_date_done', search='_search_activity_date_done',
        readonly=True, store=False,
        groups="base.group_user")
    completed_activity_ids = fields.One2many(
        'mail.activity', 'res_id', 'Completed Activities',
        auto_join=True,
        groups="base.group_user",
        domain=lambda self: [('res_model', '=', self._name),
                             ('active', '=', False)])

    @api.depends('completed_activity_ids.date_done')
    def _compute_activity_date_done(self):
        for record in self:
            record.activity_date_done = max(record.completed_activity_ids.mapped('date_done')+[False])

    def _search_activity_date_done(self, operator, operand):
        if operator == '=' and not operand:
            return [('completed_activity_ids', '=', False)]
        return [('completed_activity_ids.date_done', operator, operand)]

