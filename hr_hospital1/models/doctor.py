from odoo import api, fields, models, _


class HospitalDoctor(models.Model):
    _name = "hospital.doctor"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Hospital Doctor"
    _rec_name = 'doctor_name'

    doctor_name = fields.Char(string='Name', required=True, tracking=True)
    age = fields.Integer(string="Age", tracking=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')],
                              required=True, string="Gender", default='male', tracking=True)
    # ref = fields.Char(string="Reference", required=True)
    specialty = fields.Char()
    doctor_role = fields.Selection([
        ('intern', 'Intern'),
        ('mentor', 'Doctor Mentor')
    ])
    notes = fields.Text(string="Notes", copy=False)
    image = fields.Binary(string="Patient Image")

    def copy(self, default=None):
        if default is None:
            default = {}
        if not default.get('doctor_name'):
            default['doctor_name'] = _("%s (copy)", self.doctor_name)
        return super(HospitalDoctor, self).copy(default)


