from odoo import models, fields, api


class PtdSTechnicalCharacteristics(models.Model):
    _name = "ptd.technical.characteristics"
    _description = "Thông tin đặc điểm kĩ thuật"


    parameters = fields.Char(string="Tham số")
    val_maintain = fields.Char(string="Giá trị")
    display_resolution = fields.Char(string="Đặc điểm")
    exact_level = fields.Char(string="Sai số")
    technical_characteristics_id= fields.Many2one('ptd.ptd')