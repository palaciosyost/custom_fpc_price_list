{
    "name": "Historial de precios de productos (competencia)",
    "version": "1.0",
    "summary": "Control manual de precios de la competencia por producto",
    "description": """
Módulo para registrar manualmente precios que ofrece la competencia en productos, con el fin de monitorear y tomar mejores decisiones de venta:

    - Registro de precios ofrecidos por otros proveedores
    - Moneda y fecha de los precios
    - Asociación directa con productos
    - Acceso rápido mediante wizard
    """,
    "author": "FPC Technology",
    "website": "https://fpc-technology.com/",
    "license": "LGPL-3",
    "depends": ["base", "stock", "sale", "product", "custom_fpc_stock_ubicacion"],
    "data": [
        "security/security.xml",
        "security/ir.model.access.csv",
        "view/view_inherit_product.xml",
        "view/view_sale_order.xml",
        "view/view_historial_precio.xml",
    ],
    "assets": {
        "web.assets_backend": [
            "custom_fpc_price_list/static/src/js/stock_info_button.js",
            # "custom_fpc_price_list/static/src/xml/stock_info_button.xml",
        ],
    },
    "installable": True,
    "auto_install": False,
    "application": True,
}
