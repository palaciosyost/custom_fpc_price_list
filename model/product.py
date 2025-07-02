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
            'context': {
                'default_product_id': self.product_template_id.id,
            },
        }
    def action_open_stock_wizard(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Stock del Producto',
            'res_model': 'wizard.stock.info',
            'view_mode': 'form',
            'target': 'new',
            'context': {
                'product_id': self.product_id.id
            }
        }


class WizardStockInfo(models.TransientModel):
    _name = 'wizard.stock.info'
    _description = 'Información de Ubicaciones de Stock'

    stock_html = fields.Html(string="Detalle de Ubicaciones", sanitize=False)

    @api.model
    def default_get(self, fields_list):
        res = super().default_get(fields_list)
        product_id = self.env.context.get('product_id')
        if product_id:
            product = self.env['product.product'].browse(product_id)
            quants = self.env['stock.quant'].search([
                ('product_id', '=', product.id),
                ('quantity', '>', 0)
            ])
            html = "<div><h5>Stock del producto</h5><ul>"
            total = 0
            for q in quants:
                html += f"<li>{q.location_id.display_name}: {q.quantity}</li>"
                total += q.quantity
            html += f"</ul><strong>Total: {total}</strong></div>"
            html += f"<br/><div><h5>Ubicación del producto</h5><ul>" if product.tab_localizacion else ''
            for tab in product.tab_localizacion:                    
                html += f"<li><strong>Estante:</strong> {tab.estante.name} / <strong>Fila:</strong> {tab.fila.name}</li>"
                html += "</ul></div>"
            res['stock_html'] = html
        return res
