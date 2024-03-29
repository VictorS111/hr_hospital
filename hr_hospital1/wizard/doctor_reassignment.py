from datetime import date
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class DoctorReassignment(models.TransientModel):
    _name = "doctor.reassignment.wizard"
    _description = "Doctor Reassignment Wizard"

    doctor_id = fields.Many2one('hospital.doctor', string="Doctor", required=True)

    def action_doctor_reassignment(self):
        action = self.env.ref('hr_hospital1.action_hospital_appointment').read()[0]
        action['domain'] = [('doctor_id', '=', self.doctor_id.id)]
        return action

