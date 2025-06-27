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

    product_id = fields.Many2one(
        "product.template", string="Producto"
    )

    precio_unitario = fields.Float(
        string="Precio Unitario",
    )

