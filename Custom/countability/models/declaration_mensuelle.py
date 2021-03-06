from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class DeclarationMensuelle(models.Model):
    _name = 'declaration.mensuelle'
    _description = 'declaration mensuelle'

    @api.constrains('month')
    def check_month(self):
        for rec in self:
            if rec.month >= 13 or rec.month <= 0:
                raise ValidationError(_('mois incorrect.'))

    @api.constrains('year')
    def check_year(self):
        for rec in self:
            if rec.year >= 12 or rec.year <= 0:
                raise ValidationError(_('année incorrect.'))

    pay = fields.Integer(string='valeur a payé')
    client_id = fields.Many2one('acc.client', 'client_name')
    month = fields.Integer(string='mois')
    year = fields.Integer(string='année')
