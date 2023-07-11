# -*- coding: utf-8 -*-
# See LICENSE file for full copyright and licensing details.
{
    'name': 'TH: Factura',
    'version': '1.0.',
    'category': 'Other',
    'license': '',
    'author': 'Tecnihand',
    'website': 'https://www.tecnihand.com',
    'maintainer': 'Joel Estrada',
    'summary': """Módulo Factura""",
    'depends': ["sale"],
    'data': [
        'security/ir.model.access.csv',
        'report/report_stock_picking_price.xml',
    ],
    'installable': True,
}
