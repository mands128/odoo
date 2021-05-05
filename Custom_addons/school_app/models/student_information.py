from odoo import models, fields,api
from datetime import datetime,timedelta
from dateutil.relativedelta import relativedelta

class StudentInformation(models.Model):
    _name = "student.information"
    _description = "Studetn informaation"
    # _rec_name = ''
	    

    student_name = fields.Char(string="Name")
    student_email = fields.Char(string="email")
    mobile_no = fields.Integer(string="Mobile Number")
    state = fields.Char(string="state")
    country=fields.Char(string="country")
    education_qualification = fields.One2many("education.qualification","student_id")

    
    # current_year=fields.Integer(string="Current Year", default=datetime.now().year)
    # degree=fields.Char(string="Degree")
    states = fields.Selection([
        ('draft', 'Draft'),
        ('approved', 'Approved'),
        ('cancel','Cancel'),
        ], string='Status', readonly=True, copy=False, index=True, tracking=3, default='draft')

    # education_qualification = fields.One2many("student.information","student_id")


    
    def act_cancel(self):
        for rec in self:
            rec.states='cancel'

    #button reset
    def act_draft(self):
        for rec in self:
            rec.states='draft'

    def act_approve(self):
    	for rec in self:
    		rec.states='approved'



class EducationQualification(models.Model):
    _name = "education.qualification"
    _description = "education qualification"

    student_id = fields.Many2one("student.information")
    degree=fields.Char(string="Degree")
    institute_name=fields.Char(string="Institute name")
    # passout_year=fields.Date(default="datetime.date.y")
    passout_year=fields.Selection([(str(num),str(num)) for num in range(1900, (datetime.now().year)+15 )])
    difference_year=fields.Integer(string="Difference Year") 
    @api.onchange("passout_year")
    def compute_year(self):
    	for rec in self:
    		if rec.passout_year:
    			print(rec.passout_year)
    			print("diofddvdsdd")
    			print(datetime.today().year)
    			print(type(datetime.today().year))
    			differenceyear=abs(datetime.today().year - int(rec.passout_year))
    			print(type(differenceyear))
    			print("done.......",differenceyear)
    			rec.difference_year=differenceyear





