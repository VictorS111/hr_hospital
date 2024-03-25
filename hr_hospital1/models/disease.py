from odoo import api, fields, models, _
class Disease(models.Model):
    _name = "disease"
    _description = "Disease"

    name = fields.Char(string='Name', required=True, tracking=True)
    description = fields.Text()
    parent_id = fields.Many2one('disease')