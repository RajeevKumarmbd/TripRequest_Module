from odoo import models, fields, api


class TrpModuleGroupsDetailsTable(models.Model):
    _name = 'trpmodule.groupsdetailstable'

    requisitionss_ids = fields.Many2one('trpmodule.travelrequisitiontable','groupdetails_id', readonly=True)
    name = fields.Char('Company')
    user_name = fields.Char('Name')
    age = fields.Integer('Age')
    phone = fields.Integer('Phone')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('others', 'Others')], string='Gender')
    email_id = fields.Char('Email ID')
    expense_born_by = fields.Char('Expense Born By')
