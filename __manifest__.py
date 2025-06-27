{
    'name': 'Historial de precios de productos (competencia)',
    'version': '1.0',
    'summary': 'Control manual de precios de la competencia por producto',
    'description': """
Módulo para registrar manualmente precios que ofrece la competencia en productos, con el fin de monitorear y tomar mejores decisiones de venta:

    - Registro de precios ofrecidos por otros proveedores
    - Moneda y fecha de los precios
    - Asociación directa con productos
    - Acceso rápido mediante wizard
    """,
    'author': 'FPC Technology',
    'website': 'https://fpc-technology.com/',
    'license': 'LGPL-3',
    'depends': [
        'base', 'stock', 'sale', 'product'
    ],
    'data': [
        'security/ir.model.access.csv',
        'view/view_inherit_product.xml',
        'view/view_sale_order.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
