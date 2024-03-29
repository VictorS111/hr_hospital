import logging
from odoo import api, fields, models, _

_logger = logging.getLogger(__name__)

class Diagnosis(models.Model):
    _name = "diagnosis"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Patients Diagnosis"

    # visit_id = fields.Many2one('patient.visits', required=True)
    doctor_id = fields.Many2one('hospital.doctor', required=True)
    patient_id = fields.Many2one('hospital.patient', required=False)
    disease_id = fields.Many2one('disease', required=True)
    description = fields.Text(string='Description For Treatment')