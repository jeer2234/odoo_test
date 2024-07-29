# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo.addons.survey.tests.common import TestSurveyCommon
from odoo.addons.project.tests.test_project_base import TestProjectCommon


class SurveyCase(TestSurveyCommon, TestProjectCommon):

    @classmethod
    def setUpClass(cls):
        super(SurveyCase, cls).setUpClass()
        cls.survey_2 = cls.env['survey.survey'].with_user(cls.survey_manager).create({
            'title': 'Public Survey for Tarte Al Djotte',
            'access_mode': 'public',
            'users_login_required': False,
            'questions_layout': 'page_per_section',
        })

        # First page is about customer data
        page_0 = cls.env['survey.question'].create({
            'is_page': True,
            'question_type': False,
            'sequence': 1,
            'title': 'Page1: Your Data',
            'survey_id': cls.survey_2.id,
        })
        cls._add_question(
            cls, page_0, 'What is your name', 'text_box',
            comments_allowed=False,
            constr_mandatory=True, constr_error_msg='Please enter your name', survey_id=cls.survey_2.id)
        cls._add_question(
            cls, page_0, 'What is your age', 'numerical_box',
            comments_allowed=False,
            constr_mandatory=True, constr_error_msg='Please enter your name', survey_id=cls.survey_2.id)

        # Second page is about tarte al djotte
        page_1 = cls.env['survey.question'].create({
            'is_page': True,
            'question_type': False,
            'sequence': 4,
            'title': 'Page2: Tarte Al Djotte',
            'survey_id': cls.survey_2.id,
        })
        cls._add_question(
            cls, page_1, 'What do you like most in our tarte al djotte', 'multiple_choice',
            labels=[{'value': 'The gras'},
                    {'value': 'The bette'},
                    {'value': 'The tout'},
                    {'value': 'The regime is fucked up'}], survey_id=cls.survey_2.id)

        cls.customer_2 = cls.env['res.partner'].create({
            'name': 'cudio client',
            'email': 'customer_2@example.com',
        })
        cls.task_2.partner_id = cls.customer_2.id
        cls.task_1.survey_id = cls.survey
