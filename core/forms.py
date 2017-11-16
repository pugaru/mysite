# -*- coding: utf-8 -*-
from django import forms

class ContactForm(forms.Form):
    nome = forms.CharField
    email = forms.EmailField
    mensagem = forms.CharField

    def envia_email(self):
        print(
            "Email para você:\n"+
            "Aluno: "+self.nome+"\n"+
            "Email: "+self.email+"\n"+
            "Mensagem: "+self.mensagem
            )
        
