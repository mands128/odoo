from odoo import models, fields, api, _


class ProfessorWizard(models.TransientModel):
    _name = "professor.wizard"
    _description = "this is professor wizard model"

    professor_desc=fields.Text()


    def act_submit(self):
        print(f"\n\n\n _description successfully...  \n\n\n")
        print(self.env['school.professor'].browse(
            self._context.get("active_id")))
        self.env['school.professor'].browse(
            self._context.get("active_id")).write({'description': self.professor_desc})
        return True



            