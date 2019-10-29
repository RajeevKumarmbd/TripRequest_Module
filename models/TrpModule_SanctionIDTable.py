from odoo import models, fields, api


class TrpModuleSanctionIDTable(models.Model):
    _name = 'trpmodule.sanctionidtable'

    name = fields.Char('Sanction ID', required=True)
    agenda_ref_no = fields.Char('Agenda Ref. No')
    project_name = fields.Char('Project Name')
    description_justification = fields.Char('Description / Justifications')
    submitted_by = fields.Char('Submitted By')
    submitted_on = fields.Date('Submitted On')
    status = fields.Boolean('Status')
    file_name = fields.Char('File Name')
    md_approve_by = fields.Char('MD Approved By')
    md_approve_on = fields.Date('MD Approved On')
    md_remarks = fields.Char('MD Remarks')
    audited_by = fields.Char('Audited By')
    audited_on = fields.Char('Audited On')
    auditor_remark = fields.Char('Auditor Remarks')
