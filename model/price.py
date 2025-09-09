from odoo import models, fields, api

class PriceProductListWizard(models.TransientModel):
    _name = "price.product.list.wizard"
    _description = "Wizard - Historial de Precios"

    product_id = fields.Many2one(
        "product.template", string="Producto", required=True
    )
    line_ids = fields.One2many(
        "price.product.list", "wizard_id", string="Historial"
    )

    @api.model
    def default_get(self, fields_list):
        """Cargar historial existente en el wizard"""
        res = super().default_get(fields_list)
        product_id = self.env.context.get("default_product_id")
        if product_id:
            historial = self.env["price.product.list"].search([("product_id", "=", product_id)])
            lines = []
            for h in historial:
                lines.append((0, 0, {
                    "fecha_registro": h.fecha_registro,
                    "moneda_id": h.moneda_id.id,
                    "cliente": h.cliente.id,
                    "product_id": h.product_id.id,
                    "precio_unitario": h.precio_unitario,
                    "is_existing": True,
                }))
            res["line_ids"] = lines
            res["product_id"] = product_id
        return res

    def action_save(self):
        """Crear en el modelo real solo las nuevas líneas"""
        for line in self.line_ids:
            if not line.is_existing:
                self.env["price.product.list"].create({
                    "fecha_registro": line.fecha_registro,
                    "moneda_id": line.moneda_id.id,
                    "cliente": line.cliente.id,
                    "product_id": self.product_id.id,
                    "precio_unitario": line.precio_unitario,
                })
        return {"type": "ir.actions.act_window_close"}


class PriceProductListWizardLine(models.TransientModel):
    _name = "price.product.list"
    _description = "Líneas del Wizard de Precios"

    wizard_id = fields.Many2one("price.product.list.wizard", ondelete="cascade")
    fecha_registro = fields.Date(
        string="Fecha de Registro", default=fields.Date.today, required=True
    )
    moneda_id = fields.Many2one("res.currency", string="Moneda")
    cliente = fields.Many2one("res.partner", string="Competencia")
    product_id = fields.Many2one("product.template", string="Producto")
    precio_unitario = fields.Float(string="Precio Unitario")
    is_existing = fields.Boolean("Ya existe", default=False, readonly=True)
