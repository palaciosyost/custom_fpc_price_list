from odoo import models, api, fields, _

class WizardEditarPrecio(models.TransientModel):
    _name = 'wizard.editar.precio'
    _description = 'Wizard para editar precio unitario'

    sale_line_id = fields.Many2one('sale.order.line', string='Línea de Venta')
    price_unit = fields.Float(string='Nuevo Precio')

    def apply_new_price(self):
        self.sale_line_id.price_unit = self.price_unit
        return {'type': 'ir.actions.act_window_close'}
