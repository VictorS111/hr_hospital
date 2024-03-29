import logging
from odoo import api, fields, models, _

_logger = logging.getLogger(__name__)

class Person(models.AbstractModel):
    _name = "person"
    _description = "Person"

    name = fields.Char(string='Name', required=True, tracking=True)
    second_name = fields.Char(string='Second Name', required=True, tracking=True)
    phonenumber = fields.Char(string='Phone')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')],
                              required=True, string="Gender", default='male', tracking=True)
    image = fields.Binary(string="Patient Image")

