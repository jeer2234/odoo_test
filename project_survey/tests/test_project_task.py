# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo.addons.project_survey.tests import common
from odoo.tests import Form


class TestSurveyInvite(common.SurveyCase):

    def test_flow_public_beta(self):

        self.task_2.survey_id = self.survey_2
        action_1 = self.task_1.action_send_survey_from_task()
        action_2 = self.task_2.action_send_survey_from_task()
        invite_form_1 = Form(self.env[action_1['res_model']].with_context(action_1['context']))
        invite_form_2 = Form(self.env[action_2['res_model']].with_context(action_2['context']))
        invite_1 = invite_form_1.save()
        invite_1.action_invite()
        invite_2 = invite_form_2.save()
        invite_2.action_invite()

        answers_1 = self.env['survey.user_input'].search([('survey_id', '=', self.survey.id), ('partner_id', '=', self.task_1.partner_id.id)])
        answers_2 = self.env['survey.user_input'].search([('survey_id', '=', self.survey_2.id),('partner_id', '=', self.task_2.partner_id.id)])
        self.assertEqual(answers_1, self.task_1.user_input_ids)
        self.assertEqual(answers_2, self.task_2.user_input_ids)
