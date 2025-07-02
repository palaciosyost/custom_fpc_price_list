from odoo import http
from odoo.http import request

class CustomStockInfoController(http.Controller):

    @http.route('/stock_info_from_line', type='json', auth='user')
    def stock_info_from_line(self, line_id):
        line = request.env['sale.order.line'].browse(int(line_id))
        product = line.product_id
        return {
            'forecasted_qty': product.virtual_available,
            'qty_available': product.qty_available,
            'date': fields.Date.today().strftime('%Y-%m-%d'),
        }

