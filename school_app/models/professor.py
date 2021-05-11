import datetime
from dateutil.relativedelta import relativedelta

from odoo import models, fields, api, exceptions


class Professor(models.Model):
    _name = "school.professor"
    # _inherit = "res.partner"

    # name = fields.Char(string="Professor name")
    # gender = fields.Selection([('male', 'Male'), ('female', 'Female')], default="male")
    # dob = fields.Date()
    # email = fields.Char()
    # phone = fields.Integer()
    # photo = fields.Image(max_width=30, max_height=50)
    # address = fields.Text()
    order_lines = fields.One2many('school.product', 'order_id')
    name = fields.Many2one('res.partner', domain="[('professor','=',True)]")
    email = fields.Char(related='name.email')
    phone = fields.Char(related='name.phone')
    street = fields.Char(related='name.street')
    street2 = fields.Char(related='name.street2')
    city = fields.Char(related='name.city')
    state = fields.Many2one('res.country.state', related='name.state_id')
    country = fields.Many2one('res.country', related='name.country_id')
    # age = fields.Integer(compute="compute_abc", store=True)
    age = fields.Integer()
    description=fields.Text(string="Description")
    states = fields.Selection([
        ('draft', 'Draft'),
        ('confirm', 'Confirm'),
        ('order', 'Sales Order'),
        ('cancel', 'Cancelled'),
        ], string='Status', readonly=True, copy=False, index=True, tracking=3, default='draft')
    # professor = fields.Boolean(string="professor")
    login_user=fields.Many2one("res.users",default=lambda self:self.env.user)
    _sql_constraints = [
        ('age_uniq', 'UNIQUE (age)', 'You can not have two users with the same age !'),
        ('check_age', 'CHECK(age > 20 and age < 35)', 'age should be between 20 and 35')
    ]

    # @api.constrains('age')
    # def check_age(self):
    #     if self.age <= 20 or self.age >= 35:
#         raise exceptions.ValidationError(_("age should be between 20 and 35"))

    # @api.depends('name.dob')
    # def compute_abc(self):
    #     for prof in self:
    #         if prof.name.dob:
    #             prof.age = abs(relativedelta(prof.name.dob, datetime.date.today()).years)

    # @api.onchange('name.dob')
    # def compute_abc(self):
    #     for prof in self:
    #         if prof.name.dob:
    #             prof.age = abs(relativedelta(prof.name.dob, datetime.date.today()).years)

    # @api.onchange('order_lines')
    # def write_quantity(self):
    #     for rec in self.order_lines:
    #         if not rec.product_uom_qty:
    #             rec.write({
    #                 'product_uom_qty': 100.00
    #             })

    # def name_get(self):
    #     result = []
    #     for pro in self:
    #         result.append((pro.id, "{}{}".format(pro.name.name, pro.email)))
    #         return result

    # def act_confirm(self):
        
        # for rec in self:
        #     # search
        #     professors_search = self.env['res.partner'].search([('professor', '=', True)])
        #     print("professors_search...", professors_search)

        # search_count
        # professors_search_count = self.env['res.partner'].search_count([('professor', '=', True)])
        # print("professors_search_count...", professors_search_count)

        # ref
        # professors_ref = self.env.ref('base.res_partner_address_15')
        # print("professors_ref...", professors_ref)

        # browse
        # professors_browse = self.env['res.partner'].browse([26, 14])
        # print("professors_browse...", professors_browse)

        # browse and exists
        # professors_browse = self.env['res.partner'].browse(1000)
        # print("professors_browse...", professors_browse)
        # if professors_browse.exists():
        #     print("Existing record.....")
        # else:
        #     print("record does not exist")

        # create
        # vals = {
        #     'name': 'dhruvi',
        #     'phone': 4589623,
        #     'professor': True,
        # }
        # a= self.env['res.partner'].create(vals)
        # print("Kem cho ne majama", professor)


        # write method
        # professor = self.env['res.partner']
        # partner_write = professor.browse(26)
        # if partner_write.exists():
        #     vals = {
        #         'name': 'kinal17',
        #         'phone': 8141303040,
        #         'professor': True,
        #         'email': 'kinal1711@gmail.com',
        #         'website':"www.youtube.com"
        #     }
        #     partner_write.write(vals)

        # copy
        # professor_copy = self.env['res.partner'].browse(35)
        # professor_copy.copy()

        # unlink
        # professor_unlink=self.env['res.partner'].browse([27,33,45])
        # professor_unlink.unlink()

        # search_read
        # professor_seach_read = self.env['res.partner'].search_read([('name', '=', 'MANTHANHUB')])
        # print("kem cho majama.........",professor_seach_read)

        # read
        # professor_read=self.env['res.partner'].search([('professor', '=', False)]).read(['name'])
        # print("Hiii........",professor_read)
        # vals={
        #         'name': 'shant',
        #         'phone': 8141303040,
        # professor       'professor': True,
        #         'email': 'shant1711@gmail.com',
        #         'website':"www.youtube.com"
        #     }
        # self.env['res.partner'].create(vals)


    # def create(self, vals):
    #     professor_create = super(Professor, self).create(vals)
    #     return professor_create


    def preview_professor_order(self):
        return{
            'name': ('Contacts'),
            'domain':[('email','=',self.email)],
            'view_mode':'tree,form',
            'res_model': 'res.partner',
            'type':'ir.actions.act_window'
        }

    #print report usinf button    
    def print_report(self):
        print("report")
        return self.env.ref('school_app.action_report_professor').report_action(self)

    # def create_professor(self):
    #     print("fill_report")
    #     vals={
    #             'name': 'shant',
    #             'phone': 8141303040,
    #             'professor': True,
    #             'email': 'shant1711@gmail.com',
    #             'website':"www.youtube.com"
    #         }
    #     return self.env['res.partner'].create(vals)
  
    #button confirm
    def act_confirm(self):
        for rec in self:
            rec.states='confirm'

    #button order
    def act_order(self):
        for rec in self:
            rec.states='order'        


    #button cancel
    def act_cancel(self):
        for rec in self:
            rec.states='cancel'

    #button reset
    def act_draft(self):
        for rec in self:
            rec.states='draft'

    # button wizard
    def act_desc(self):
        return {'type': 'ir.actions.act_window',
            'name': ('Professor'),
            'res_model': 'professor.wizard',
            'target': 'new',
            'view_id': self.env.ref('school_app.professor_wizard_form_view').id,
            'view_mode': 'form',
            }

            
    class Product(models.Model):
        _name = 'school.product'

        order_id = fields.Many2one('school.professor')
        product_id = fields.Many2one('product.product', domain="[('type','=','service')]", ondelete='cascade')
        product_temp_id = fields.Many2one('product.template', related='product_id.product_tmpl_id')
            # product_temp_id = fields.Many2one('sale.order.line')
        desc = fields.Text(string="Description", related='product_temp_id.description_sale', readonly=False)
        sequence = fields.Integer(string='Sequence', default=10)
        product_uom_qty = fields.Float(string='Quantity')
        price_unit = fields.Float('Unit Price', related="product_temp_id.list_price", readonly=False)
            # subtotal_price = fields.Float(compute="compute_total_price", store=True, string="Total_price")
        subtotal_price = fields.Float(string="Total_price")

        # @api.depends('product_uom_qty', 'price_unit')
        # def compute_total_price(self):
        #     for rec in self:
        #         rec.subtotal_price = rec.product_uom_qty * rec.price_unit

        @api.onchange('product_uom_qty', 'price_unit')
        def total_price(self):
            for rec in self:
                rec.subtotal_price = rec.product_uom_qty * rec.price_unit

        # @api.onchange('price_unit')
        # def update(self):
        # for rec in self:

        # @api.onchange('order_id')
        # def test_orm(self):
        #     quantity = self.create({
        #         'product_id': Manan,
        #     })
        #     return quantity

    class ContactsInherit(models.Model):
        # _name = 'school.contacts'
        _inherit = "res.partner"

        professor = fields.Boolean(string="Professor")
        dob = fields.Date()
        student_id = fields.Many2one(readonly=True)
