# -*- coding: utf-8 -*-
from odoo import models, fields, api


class AccountMove(models.Model):
    _inherit = 'account.move'

    # El campo mrdc_shipment_id ya existe en mrdc_shipment_base
    # Solo agregamos el conteo de embarques para el botón estadístico
    
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
