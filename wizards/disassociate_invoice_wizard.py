# -*- coding: utf-8 -*-
from odoo import models, fields, api


class DisassociateInvoiceWizard(models.TransientModel):
    _name = 'disassociate.invoice.wizard'
    _description = 'Wizard para Desasociar Facturas del Embarque'

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
        string='Facturas a Desasociar',
        domain="[('mrdc_shipment_id', '=', shipment_id)]",
    )

    @api.onchange('shipment_id')
    def _onchange_shipment_id(self):
        """Cargar las facturas asociadas al embarque"""
        if self.shipment_id:
            return {'domain': {'invoice_ids': [('mrdc_shipment_id', '=', self.shipment_id.id)]}}

    def action_disassociate(self):
        """Desasociar las facturas seleccionadas del embarque"""
        self.ensure_one()
        if self.invoice_ids:
            self.invoice_ids.write({
                'mrdc_shipment_id': False,
            })
        return {'type': 'ir.actions.act_window_close'}

