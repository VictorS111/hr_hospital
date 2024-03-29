from datetime import date
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class CreateReportWizard(models.TransientModel):
    _name = "create.report.wizard"
    _description = "Create Report Wizard"

    doctor_id = fields.Many2one('hospital.doctor', string="Doctor", required=True)
    disease_id = fields.Many2one('disease', required=True)
    date_begin = fields.Date(string='Start Date', required=False)
    date_end = fields.Date(string='End Date', required=False)

    def action_create_report(self):
        vals = {
            'doctor_id': self.doctor_id.id,
            'disease_id': self.disease_id.id,
        }
        diagnosis_rec = self.env['diagnosis'].create(vals)
        return {
            'name': _('diagnosis'),
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'diagnosis',
            'res_id': diagnosis_rec.id,
            'target': 'new',
        }


