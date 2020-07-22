# Copyright 2020 Graeme Gellatly
# License LGPL-3 or later (http://www.gnu.org/licenses/lgpl).

from odoo import api, models, _
from odoo.exceptions import ValidationError


class CrmLead(models.Model):
    _inherit = "crm.lead"

    @api.constrains("stage_id")
    def required_field_check(self):
        for record in self:
            required_fields = record.stage_id.required_fields
            for field in required_fields:
                if not record[field.name]:
                    raise ValidationError(
                        _(
                            "Lead %s (%d) is missing required fields to transition "
                            "to %s stage.\n\nThe required fields are:\n"
                        )
                        % (record.name, record.id, record.stage_id.name)
                        + "\n".join(
                            [_(" - %s") % f.field_description for f in required_fields]
                        )
                    )
