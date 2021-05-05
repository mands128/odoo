import sys
from odoo import models, fields, api, _
import datetime
from dateutil.relativedelta import relativedelta
# sys.setrecursionlimit(4000)
# import odoo.exceptions


# from exceptions import UserError
from odoo import exceptions


class Student(models.Model):
    _name = 'school_student'
    # _order =

    name = fields.Char(string="Student name")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], default="male")
    dob = fields.Date()
    email = fields.Char(copy=False)
    phone = fields.Integer()
    photo = fields.Image(max_width=30, max_height=50)
    address = fields.Text()
    state = fields.Selection([('draft', 'Draft'), ('confirm', 'Confirm')])
    course_id=fields.Many2many('school_course',string="Course")
    # course_id = fields.One2many('school_course', 'student_id')
    # course_name = fields.Many2one('school_course')
    # desc = fields.Text(related='course_name.desc')
    # fee = fields.Integer(related='course_name.fee')
    # age = fields.Integer(compute="compute_age_calculate", store=True)
    age = fields.Integer()

    #
    # date = fields.Date(string="Date", default=datetime.today())

    # @api.depends('dob')
    # def compute_age_calculate(self):
    #     for rec in self:
    #         if rec.dob:
    #             rec.age = abs(relativedelta(rec.dob, datetime.date.today()).years)
    #             print(rec.age)
    #             print(rec.age)
    #             print(rec.age)
    #             print(rec.age)
    #             print(rec.age)

    @api.onchange('dob')
    def age_calculate(self):
        for rec in self:
            if rec.dob:
                rec.age = abs(relativedelta(rec.dob, datetime.date.today()).years)

    # @api.onchange('age')
    # def age_fun(self):
    #     for rec in self:
    #         if rec.age > 18:
    #             raise UserError

    # def create_name(self):
    #     for rec in self:
    #         rtn=rec.write({
    #             'name':
    #         })

    def action_abc(self):
        # partner = self.env['res.partner']
        # print("kem cho majama", self.id)
        # vals = {
        #     'name': self.name,
        #     'email': self.email,
        #     'phone': self.phone,
        # }
        # rtn = partner.search([('name', '=', vals['name'])])
        # if not rtn:
        #     partner.create(vals)
        # else:
        #     partner.write(vals)
        # self.env['res.partner'].create({'name': 'aaaaa', 'phone': 5564798})
        # self.env['res.partner'].search([('name','=','chasham')]).write({'phone': 5564798,'website':'www.youtube.com'})
        # self.env['res.partner'].browse(84).unlink()
        self.env['res.partner'].browse(16).copy()

    # @api.model
    # def create(self, vals):
    #     student_create = super(Student, self).create(vals)
    #     print("Hathi mera sathi......", vals)
    #     print("Dhooom machale....", student_create)
    #     return student_create

    # def write(self,vals):
    #     # self.name=vals['name']
    #     student_write = super(Student, self).write(vals)
    #     print("Hathi mera sathi......", vals)
    #     print("Dhooom machale write....", student_write)
    #     return student_write

    # def unlink(self):
    #     # self.name=vals['name']
    #     student_unlink = super(Student, self).unlink()
    #     print("its done",self.id)
    #     print("Dhooom machale unlink....", student_unlink)
    #     return student_unlink

    # def copy(self):
    #     # self.name=vals['name']
    #     student_copy = super(Student, self).copy()
    #     print("its done",self.id)
    #     print("Dhooom machale copy....", student_copy)
    #     return student_copy

    # api constrain
    # @api.constrains('age')
    # def _check(self):
    #     if self.age <= 20 or self.age >= 35:
    #         raise exceptions.ValidationError(_("age should be between 20 and 35"))

    # @api.constrains('name')
    # def _check_name(self):
    #     for rec in self:
    #         if len(rec.name) < 6:
    #             raise exceptions.ValidationError(_("Your name should atleast 6 characters"))
    #         print(rec.name)

    # @api.constrains('dob')
    # def _check_dob(self):
    #     current=datetime.date.today()
    #     print(current)
    #     print(type(current))
    #
    #     for rec in self:
    #         print("date........",rec.dob)
    #         print("datetype........",type(rec.dob))
    #             if current <= rec.dob:
    #             raise exceptions.ValidationError(_("Current date should be greater than equal to student dob"))

    # _sql_constraints = [
    #     ('check_dob', 'CHECK(len(name) < 6)', 'Your name should atleast 6 characters')
    # ]
    @api.constrains('name')
    def _check_name(self):
        for val in self:
            if len(val.name) < 6:
                raise exceptions.UserError(_('Your name should atleast 6 characters'))
