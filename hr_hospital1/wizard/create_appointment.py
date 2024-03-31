from datetime import date
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class CreateAppointmentWizard(models.TransientModel):
    _name = "create.appointment.wizard"
    _description = "Create Appointment Wizard"

    booking_date = fields.Date(string='Booking Date', required=False)
    patient_id = fields.Many2one('hospital.patient', string="Patient", required=False)

    def action_create_appointment(self):
        print('Button Is Clicked')
        vals = {
            'patient_id': self.patient_id.id,
            'booking_date': self.booking_date,
        }
        appointment_rec = self.env['hospital.appointment'].create(vals)
        print("appointment_id", appointment_rec)

        return {
            'name': _('Appointment'),
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'hospital.appointment',
            'res_id': appointment_rec.id,
            'target': 'new',
        }

    def print_report(self):
        data = {
            'model': 'create.appointment.wizard',
            'form': self.read()[0]
        }
        return (
            self.env.ref('hr_hospital1.report_appointment').with_context(landscape=True).report_action(self, data=data))




    # def action_view_appointment(self):
    #     action = self.env.ref('hr_hospital1.action_hospital_appointment').read()[0]
    #     action['domain'] = [('patient_id', '=', self.patient_id.id)]
    #     # action = self.env['ir.actions.actions']._for_xml_id("hr_hospital1.action_hospital_appointment")
    #     # action['domain'] = [('patient_id', '=', self.patient_id.id)
    #     return action
