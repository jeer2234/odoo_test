# -*- coding: utf-8 -*-

from odoo import models, fields, api


class project_survey(models.Model):
    _inherit = 'project.task'
    _description = 'class for cudio development'

    survey_ids = fields.Many2many("survey.survey", string="surveys")
    user_survey_input_ids = fields.Many2many("survey.user_input", string='Users responses', compute='_compute_user_survey_input_ids')

    def _compute_user_survey_input_ids(self):
        for record in self:
            record.user_survey_input_ids = record.survey_ids.user_input_ids

    def action_send_survey_from_task(self):
        self.ensure_one()

        # # if an applicant does not already has associated partner_id create it
        # if not self.partner_id:
        #     if not self.partner_name:
        #         raise UserError(_('Please provide an applicant name.'))
        #     self.partner_id = self.env['res.partner'].sudo().create({
        #         'is_company': False,
        #         'name': self.partner_name,
        #         'email': self.email_from,
        #         'phone': self.partner_phone,
        #         'mobile': self.partner_mobile
        #     })

        self.survey_ids.check_validity()
        template = self.env.ref('hr_recruitment_survey.mail_template_applicant_interview_invite', raise_if_not_found=False)


        return {
            'type': 'ir.actions.act_window',
            'name': _("Send an interview"),
            'view_mode': 'form',
            'res_model': 'survey.invite',
            'target': 'new',
            'context': local_context,
        }