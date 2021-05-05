from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'


    # sale_tax_id = fields.Many2one('account.tax', string="Default Sale Tax", related='company_id.account_sale_tax_id', readonly=False)
    api_key= fields.Char(string="api_key")
    alt=fields.Char(string="alt")



    @api.model
    def set_values(self):
        self.env['ir.config_parameter'].set_param(
            "school_app.api_key", self.api_key)
        self.env['ir.config_parameter'].set_param(
            "school_app.alt", self.alt)  
        res = super(ResConfigSettings, self).set_values()
        print("Set suceesfully")

    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        res['api_key'] = self.env['ir.config_parameter'].sudo().get_param('school_app.api_key')
        res['alt'] = self.env['ir.config_parameter'].sudo().get_param('school_app.alt')
        print("running succesfully")
        return res
