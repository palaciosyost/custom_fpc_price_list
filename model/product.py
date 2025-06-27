from odoo import models, fields, api, _


class ProductPrice(models.Model):
    _inherit = "product.template"
    _description = "Precios producto"

    precio_lista = fields.One2many(
        "price.product.list", "product_id", string="Historail de precios"
    )




class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    def action_open_precio_wizard(self):
        return {
            'name': 'Historial de Precios',
            'type': 'ir.actions.act_window',
            'res_model': 'price.product.list',
            'view_mode': 'tree',
            'target': 'new',
            'domain': [('product_id', '=', self.product_template_id.id)],
        }
