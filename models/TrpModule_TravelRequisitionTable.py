from odoo import api, fields, models, SUPERUSER_ID, _
from odoo.exceptions import UserError, ValidationError


class TrpModuleTravelRequisitionTable(models.Model):
    _name = 'trpmodule.travelrequisitiontable'

    name = fields.Char('Trip Purpose')
    estimateexpensedetails_id = fields.One2many('trpmodule.estimateexpensedetailstable', 'requisition_id')
    otherallowance_id = fields.One2many('trpmodule.otherallowanceexpensestable', 'requisitionss_ids')
    groupdetails_id = fields.One2many('trpmodule.groupsdetailstable', 'requisitionss_ids')
    FCM_Booking_id = fields.One2many('trpmodule.fcmbookeddetailstable', 'requisitionss_ids')
    sanction_id = fields.Many2one('trpmodule.sanctionidtable', 'Sanction ID', required=True)
    trip_request_id = fields.Char('Trip Request ID', store=True)
    trip_start_date = fields.Date('Trip Start Date')
    trip_end_date = fields.Date('Trip End Date')
    date_created = fields.Date('Requesting Date')
    number_of_days = fields.Integer('Number of Days', required=True)
    are_date_fixed = fields.Selection([('yes', 'Yes'), ('no', 'No')], string='Are Date Fixed')
    total_cost = fields.Float('Total Cost')
    cost_borne_by_company = fields.Float('Cost Borne By Company')
    cost_borne_by_third_party = fields.Float('Cost Borne By 3rd Party')
    tour_type = fields.Selection([('domestic', 'Domestic'), ('international', 'International')], string='Tour Type')
    trip_request_for = fields.Char('Trip Request For')
    no_of_pax = fields.Integer('No of Pax', required=True)
    cost_center = fields.Char('Cost Center')
    card_no = fields.Char('Card No.', compute='default_cardno', store=True)
    emp_name = fields.Char('Employee Name', compute='default_cardno', store=True)
    dep_name = fields.Char('Department', compute='default_cardno', store=True)
    designation = fields.Char('Designation', compute='default_cardno', store=True)
    email_id = fields.Char('Email ID', compute='default_cardno', store=True)
    contact_no = fields.Char('Contact Number', compute='default_cardno', store=True)
    ta_category = fields.Char('TA Category')
    status_approver = fields.Selection([('Free', 'Free'), ('For Approval', 'For Approval'),
                                        ('Approved', 'Approved'), ('Reject', 'Reject')],
                                       'Status')

    sanction_agenda_ref_no = fields.Char('Agenda Ref. No', related='sanction_id.agenda_ref_no')
    user_id = fields.Many2one('res.users', ondelete='set null', string='Assign To', required=True)
    assign_remarks = fields.Text('Remark')

    # assign_to = fields.Char('Assign To', related='user_id.login', store=True)
    # assign_to = fields.Many2one('hrmodule.employeetable', 'Assign To', required=True)

    @api.multi
    def send_for_approval(self):
        if self.trip_request_id == '':
            raise ValidationError(_("Firstly Save All Details"))

    @api.model
    def create(self, vals):
        seq = self.env['ir.sequence'].next_by_code('trpmodule.travelrequisitiontable')
        vals.update({'trip_request_id': seq})
        res = super(TrpModuleTravelRequisitionTable, self).create(vals)
        return res

    @api.depends('number_of_days')
    def default_cardno(self):
        employee_pool = self.env['hrmodule.employeetable']
        defemployee = employee_pool.search([('login', '=', self.env.user.login)])
        if not defemployee:
            for record in self:
                record.card_no = "Card No. not found"

        else:
            for record in self:
                record.card_no = defemployee.cardno
                record.emp_name = defemployee.name
                record.dep_name = defemployee.department
                record.designation = defemployee.designation
                record.email_id = defemployee.login
                record.status_approver = 'Free'

    def send_for_approval(self):
        self.write({'status_approver': 'For Approval'})

    def reject_trip(self):
        self.write({'status_approver': 'Reject'})

    def approved_trip(self):
        self.write({'status_approver': 'Approved'})
