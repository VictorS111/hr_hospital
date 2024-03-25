from datetime import date
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Hospital Patient"
    _order = "id desc"

    @api.model
    def default_get(self, fields):
        res = super(HospitalPatient, self).default_get(fields)
        res['notes'] = 'Test Default Get Method'
        return res

    name = fields.Char(string='Name', required=True, tracking=True)
    date_of_birth = fields.Date(string='Date Of Birth')
    age = fields.Integer(string="Age", compute='_compute_age', tracking=True)
    is_child = fields.Boolean(string="Is Child ?", tracking=True)
    notes = fields.Text(string="Notes")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string="Gender", tracking=True, default='male')
    capitalized_name = fields.Char(string='Capitalized Name', compute='_compute_capitalized_name', store=True)
    ref = fields.Char(string="Reference", default=lambda self: _('New'))
    active = fields.Boolean(string="Active", default=True)
    appointment_id = fields.Many2one(comodel_name='hospital.appointment', string="Appointments")
    appointment_count = fields.Integer(string='Appointment Count', compute='_compute_appointment_count')
    image = fields.Binary(string="Patient Image")

    doctor2_id = fields.Many2one('hospital.doctor', string='Doctors',
                                 domain="[('doctor_role', '!=', 'intern')]")
    # doctor_id = fields.Char(related='hospital.doctor', string='Doctors')
    appointment_ids = fields.One2many('hospital.appointment', 'patient_id',
                                      string="Appointments")

    def _compute_appointment_count(self):
        appointment_count = self.env['hospital.appointment'].search_count([('patient_id', '=', self.id)])
        self.appointment_count = appointment_count

    @api.depends('date_of_birth')
    def _compute_age(self):
        for rec in self:
            today = date.today()
            if rec.date_of_birth:
                rec.age = today.year - rec.date_of_birth.year
            else:
                rec.age = 0

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            vals['ref'] = self.env['ir.sequence'].next_by_code('hospital.patient')
        return super(HospitalPatient, self).create(vals_list)

    @api.constrains('is_child', 'age')
    def _check_child_age(self):
        for rec in self:
            if rec.is_child and rec.age == 0:
                raise ValidationError(_("Age Cannot Be Zero!"))

    @api.constrains('name')
    def check_name(self):
        for rec in self:
            patients = self.env['hospital.patient'].search([('name', '=', rec.name), ('id', '!=', rec.id)])
            if patients:
                raise ValidationError("Name %s Already Exists" % rec.name)

    @api.depends('name')
    def _compute_capitalized_name(self):
        for rec in self:
            if rec.name:
                rec.capitalized_name = rec.name.upper()
            else:
                rec.capitalized_name = ''

    @api.onchange('age')
    def _onchange_age(self):
        if self.age <= 10:
            self.is_child = True
        else:
            self.is_child = False

    @api.onchange('doctor_id')
    def doctor_gender(self):
        for rec in self:
            if rec.doctor_id:
                rec.gender_id = rec.doctor_id.gender

    # def name_get(self):
    #     result = []
    #     for rec in self:
    #         name = '[' + rec.gender + ']' + rec.name
    #         result.append((rec.id, name))
    #     return result


