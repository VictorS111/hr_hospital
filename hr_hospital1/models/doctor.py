from odoo import api, fields, models, _


class HospitalDoctor(models.Model):
    _name = "hospital.doctor"
    _inherit = "mail.thread"
    _description = "Doctor Records"

    _rec_name = 'ref'

    name = fields.Char(string='Name', required=True, tracking=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')],
                              string="Gender", tracking=True)
    ref = fields.Char(string="Reference", required=True)

    # user_id = fields.Many2one('res.users', string='Related User')
    # patient_id = fields.One2many('hospital.patient', string='Related Patient')
    # related_patient_id = fields.Many2one('hospital.patient', string='Related Patient ID')
    # @api.model
    # def create(self, vals):
    #     vals['name'] = self.env['ir.sequence'].next_by_code('doctors.sequence')
    #     result = super(HospitalDoctor, self).create(vals)
    #     return result
