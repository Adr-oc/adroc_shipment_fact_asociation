# -*- coding: utf-8 -*-
from odoo import models, fields, api


class AccountMove(models.Model):
    _inherit = 'account.move'

    def action_view_shipment(self):
        """Abrir vista del embarque asociado"""
        self.ensure_one()
        if self.mrdc_shipment_id:
            return {
                'type': 'ir.actions.act_window',
                'name': 'Embarque',
                'res_model': 'mrdc.shipment',
                'view_mode': 'form',
                'res_id': self.mrdc_shipment_id.id,
            }

    def action_disassociate_shipment(self):
        """Desasociar la factura del embarque"""
        self.write({'mrdc_shipment_id': False})
        return True
