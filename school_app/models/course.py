from odoo import models, fields



class Course(models.Model):
    _name = "school_course"
    _description = "course desc"
    # _rec_name = ''

    course_name = fields.Char(string="Course name")
    # course_id = fields.Many2one('course')
    desc = fields.Text(size=40, string="Course Description")
    fee = fields.Integer(string="Course fee")
    website = fields.Char(string="Course website")
    student_id = fields.Many2one('school_student')