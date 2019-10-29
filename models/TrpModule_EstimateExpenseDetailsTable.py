from odoo import models, fields, api


class TrpModuleEstimateExpenseDetailsTable(models.Model):
    _name = 'trpmodule.estimateexpensedetailstable'

    requisition_id = fields.Many2one('trpmodule.travelrequisitiontable', readonly=True)
    name = fields.Char('Item')
    description_route = fields.Char('Description / Route')
    number_of_pax = fields.Integer('No. Of Pax')
    qty = fields.Integer('Qty')
    est_price = fields.Float('Est.Price')
    currency = fields.Selection([('Rs.', 'INR'), ('$', 'USD')], string='Currency Symbol', default='Rs.')
    sub_total = fields.Float('Sub Total')
    sub_total_inr = fields.Float('Sub Total (INR)')
