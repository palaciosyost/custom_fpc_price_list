from odoo import models, api, fields, _


class ListaPrecio(models.Model):
    _name = "price.product.list"
    _description = "Lista de precio para productos"
    _order = "fecha_registro desc"

    fecha_registro = fields.Date(
        string="Fecha de Registro", default=fields.Date.today, required=True
    )

    moneda_id = fields.Many2one(
        "res.currency", string="Moneda"
    )
    cliente = fields.Many2one("res.partner", string="Competencia")
    product_id = fields.Many2one(
        "product.template", string="Producto", default=lambda self: self.env.context.get('default_product_id')
    )

    precio_unitario = fields.Float(
        string="Precio Unitario",
    )

