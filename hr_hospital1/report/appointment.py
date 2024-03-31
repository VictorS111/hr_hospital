from odoo import api, models, _


class AppointmentReport(models.AbstractModel):
    _name = 'report.hr_hospital1.appointment_report'
    _description = 'Appointment Report'

    @api.model
    def _get_report_values(self, docids, data=None):
        if data['form']['patient_id']:
            appointments = self.env['hospital.appointment'].search([('patient_id', '=', data['form']['patient_id'][0])])
        else:
            appointments = self.env['hospital.appointment'].search([])
        # appointment_list = []
        # for app in appointments:
        #     vals = {
        #         'name': app.patient_id,
        #         'notes': app.notes,
        #         'booking_date': app.booking_date
        #     }
        #     appointment_list.append(vals)
        return {
            'doc_model': 'hospital.appointment',
            'appointments': appointments,
        }
