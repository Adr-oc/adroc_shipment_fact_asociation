# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import UserError


class AssociateInvoiceWizard(models.TransientModel):
    _name = 'associate.invoice.wizard'
    _description = 'Wizard para Asociar Facturas de Compra al Embarque'

    shipment_id = fields.Many2one(
        comodel_name='mrdc.shipment',
        string='Embarque',
        required=True,
        readonly=True,
    )

    company_id = fields.Many2one(
        comodel_name='res.company',
        string='Compañía',
        related='shipment_id.company_id',
        readonly=True,
    )

    invoice_ids = fields.Many2many(
        comodel_name='account.move',
        relation='associate_invoice_wizard_move_rel',
        column1='wizard_id',
        column2='move_id',
        string='Facturas de Compra a Asociar',
        domain="[('move_type', 'in', ['in_invoice', 'in_refund']), ('company_id', '=', company_id), ('mrdc_shipment_id', '=', False)]",
    )

    def action_associate(self):
        """Asociar las facturas de compra seleccionadas al embarque"""
        self.ensure_one()
        if self.shipment_id.state == 'delivered':
            raise UserError('No se pueden asociar facturas a un embarque cerrado.')
        if self.invoice_ids:
            self.invoice_ids.write({
                'mrdc_shipment_id': self.shipment_id.id,
            })
        return {'type': 'ir.actions.act_window_close'}

