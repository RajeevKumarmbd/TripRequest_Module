from odoo import models, fields, api
from odoo.service import model


class TrpModuleFcmBookedDetailsTable(models.Model):
    _name = 'trpmodule.fcmbookeddetailstable'

    requisitionss_ids = fields.Many2one('trpmodule.travelrequisitiontable', 'FCM_Booking_id', ondelete='cascade',
                                        readonly=True)
    name = fields.Char('Ticket No.', required=True)
    travel_date = fields.Date('Travel Date', required=True)
    sector = fields.Char('Sector')
    pax_name = fields.Char('PAX Name')
    invoice_no = fields.Char('Invoice No', required=True)
    trip_id = fields.Char('Trip ID')
    invoice_date = fields.Date('Invoice Date')
    fcm_status = fields.Boolean(string="Cancellation", Defaul=False)
    booking_status = fields.Selection([('Reserve', 'Reserve'), ('Booking Cancel', 'Booking Cancel'), ('Cancel Against Booking', 'Cancel Against Booking')], 'Booking Status')

    @api.onchange('travel_date')
    def default_trip_id(self):
        for thisrequisitionid in self.requisitionss_ids:
            self.trip_id = thisrequisitionid.trip_request_id

    @api.onchange('fcm_status')
    def set_status(self):
        if self.fcm_status is True:
            self.booking_status = "Booking Cancel"
            b = self.env['trpmodule.travelrequisitiontable'].search([('trip_request_id', '=', self.trip_id)])
            a = self.env['trpmodule.fcmbookeddetailstable'].search([('trip_id', '=', b.trip_request_id), ('requisitionss_ids', '=', b.id), ('invoice_no', '=', self.invoice_no)])
            self.env['trpmodule.fcmbookeddetailstable'].create({'requisitionss_ids': b.id,
                                                                'name': a.name,
                                                                'travel_date': a.travel_date,
                                                                'sector': a.sector,
                                                                'pax_name': a.pax_name,
                                                                'invoice_no': a.invoice_no,
                                                                'invoice_date': a.invoice_date,
                                                                'fcm_status': False,
                                                                'trip_id': a.trip_id,
                                                                'booking_status': 'Cancel Against Booking'})
