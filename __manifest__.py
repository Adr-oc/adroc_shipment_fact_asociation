# -*- coding: utf-8 -*-
{
    'name': "Adroc - Shipment Factura Asociación",

    'summary': """
        Asociación de facturas con embarques (shipments).
        """,

    'description': """
        Módulo para gestionar la asociación entre facturas y embarques.
        
        Funcionalidades:
        - Wizard para asociar facturas (venta y compra) a un embarque
        - Las facturas de venta aparecen automáticamente en "Facturas de Venta"
        - Las facturas de compra aparecen automáticamente en "Facturas de Proveedor"
        - Usa el campo existente mrdc_shipment_id de account.move
        - Disponible en TODAS las vistas del embarque
        
        Compatible con Odoo 19 Community Edition.
        """,

    'author': "Adroc",
    'category': 'Operations',
    'version': '19.0.1.0.0',

    'depends': [
        'account',
        'mrdc_shipment_base',
        'mrdc_shipment_importer_exporter',
        'mrdc_shipment_carrier',
        'mrdc_shipment_customs_agency',
        'mrdc_shipment_customs_broker_person',
        'mrdc_shipment_freight_agency',
        'mrdc_shipment_good_carrier',
    ],

    "data": [
        "security/ir.model.access.csv",
        "wizards/associate_invoice_wizard_views.xml",
        "views/mrdc_shipment_views.xml",
        "views/account_move_views.xml",
    ],

    'license': 'OPL-1',
}
