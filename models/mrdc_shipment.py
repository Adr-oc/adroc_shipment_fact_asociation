# -*- coding: utf-8 -*-
from odoo import models, fields, api


class MrdcShipment(models.Model):
    _inherit = 'mrdc.shipment'

    # Campo One2many inverso del mrdc_shipment_id en account.move
    associated_move_ids = fields.One2many(
        comodel_name='account.move',
        inverse_name='mrdc_shipment_id',
        string='Facturas Asociadas',
        domain="[('move_type', 'in', ['out_invoice', 'in_invoice', 'out_refund', 'in_refund']), ('company_id', '=', company_id)]",
        help='Facturas asociadas a este embarque.',
    )

    associated_move_count = fields.Integer(
        string='Cantidad de Facturas Asociadas',
        compute='_compute_associated_move_count',
    )

    @api.depends('associated_move_ids')
    def _compute_associated_move_count(self):
        for record in self:
            record.associated_move_count = len(record.associated_move_ids)

    def action_view_associated_moves(self):
        """Abrir vista de todas las facturas asociadas"""
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Facturas Asociadas',
            'res_model': 'account.move',
            'view_mode': 'list,form',
            'domain': [('mrdc_shipment_id', '=', self.id)],
            'context': {
                'default_mrdc_shipment_id': self.id,
                'default_company_id': self.company_id.id,
            },
        }

    def action_open_associate_wizard(self):
        """Abrir wizard para asociar facturas"""
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Asociar Facturas',
            'res_model': 'associate.invoice.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {
                'default_shipment_id': self.id,
            },
        }
