from odoo import models, fields, api


class TrpModuleOtherAllowanceExpensesTable(models.Model):
    _name = 'trpmodule.otherallowanceexpensestable'

    requisitionss_ids = fields.Many2one('trpmodule.travelrequisitiontable', readonly=True)
    name = fields.Char('Allowance')
    currency = fields.Selection([('Rs.', 'INR'), ('$', 'USD')], string='Currency Symbol', default='Rs.')
    est_price = fields.Float('Est.Price')
    remarks = fields.Char('Remarks')
    sub_total_inr = fields.Float('Sub Total (INR)')
