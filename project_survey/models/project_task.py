# -*- coding: utf-8 -*-

from odoo import models, fields, api


class project_survey(models.Model):
    _inherit = 'project.task'
    _description = 'class for cudio development'
    survey_id = fields.Many2one("survey.survey", string="survey")
    user_input_ids = fields.One2many('survey.user_input', compute='_compute_user_input_ids')

    def _compute_user_input_ids(self):
        for record in self:
            record.user_input_ids = record.survey_id.user_input_ids.filtered(
                lambda input: input.partner_id == record.partner_id)

    def action_send_survey_from_task(self):
        """ Open a window to compose an email, pre-filled with the survey message plus task customer nad defaul """
        res = self.survey_id.action_send_survey()
        local_context = dict(
            default_partner_ids=self.partner_id.ids,
            default_send_email=True,
        )
        res['context'].update(local_context)

        return res
