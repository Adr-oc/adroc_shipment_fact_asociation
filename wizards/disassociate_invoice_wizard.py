# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import UserError


class DisassociateInvoiceWizard(models.TransientModel):
    _name = 'disassociate.invoice.wizard'
    _description = 'Wizard para Desasociar Facturas de Compra del Embarque'

    shipment_id = fields.Many2one(
        comodel_name='mrdc.shipment',
        string='Embarque',
        required=True,
        readonly=True,
    )

    invoice_ids = fields.Many2many(
        comodel_name='account.move',
        relation='disassociate_invoice_wizard_move_rel',
        column1='wizard_id',
        column2='move_id',
        string='Facturas de Compra a Desasociar',
        domain="[('mrdc_shipment_id', '=', shipment_id), ('move_type', 'in', ['in_invoice', 'in_refund'])]",
    )

    @api.onchange('shipment_id')
    def _onchange_shipment_id(self):
        """Cargar las facturas de compra asociadas al embarque"""
        if self.shipment_id:
            return {'domain': {'invoice_ids': [
                ('mrdc_shipment_id', '=', self.shipment_id.id),
                ('move_type', 'in', ['in_invoice', 'in_refund'])
            ]}}

    def action_disassociate(self):
        """Desasociar las facturas de compra seleccionadas del embarque"""
        self.ensure_one()
        if self.shipment_id.state == 'delivered':
            raise UserError('No se pueden desasociar facturas de un embarque cerrado.')
        if self.invoice_ids:
            self.invoice_ids.write({
                'mrdc_shipment_id': False,
            })
        return {'type': 'ir.actions.act_window_close'}

