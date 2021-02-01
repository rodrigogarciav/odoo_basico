# -*- coding: utf-8 -*-

from odoo import models, fields, api


class suceso(models.Model):
     _name = 'odoo_basico.suceso' # Será o nome da táboa
     _description = ' Proba de vista tree en modo edición'

     name = fields.Char(string="Suceso",required=True,size=20)
     descripcion = fields.Text(string="A Descripción do Suceso")
     nivel = fields.Selection([('Alto','Alto'),('Medio','Medio'),('Baixo','Baixo')],string="Nivel")
     data_hora = fields.Datetime(string="Data e Hora")