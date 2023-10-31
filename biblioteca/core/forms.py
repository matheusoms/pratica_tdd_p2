from django import forms
from django.core.exceptions import ValidationError
from core.models import LivroModel

def validate_title(titulo):
    if len(titulo) < 3:
        raise ValidationError('O título deve ter pelo menos três caracteres')
    
def validate_title(editora):
    if len(editora) < 3:
        raise ValidationError('A editora deve ter pelo menos três caracteres')
    
def validate_title(isbn):
    if len(isbn) != 13 or not isbn.isdigit():
        raise ValidationError('O ISBN deve conter exatamente 13 caracteres numéricos')

def validate_title(num_pagina):
    if not (1 <= len(num_pagina) <= 3) or not num_pagina.isdigit():
        raise ValidationError('Deve conter entre 1 e 3 caracteres numéricos')
    
def validate_title(edicao):
    if len(edicao) != 4 or not edicao.isdigit():
        raise ValidationError('A edição deve conter exatamente 4 caracteres numéricos')

class LivroForm(forms.ModelForm):

    class Meta:
        model = LivroModel
        fields = ['titulo', 'editora', 'autor', 'isbn', 'num_pagina', 'edicao']
        error_messages = {
            'titulo': {
                'required': ("Informe o título do livro."),
            },
            'editora': {
                'required': ("Informe a editora do livro."),
            },
            'autor': {
                'required': ("Informe o autor do livro."),
            },
            'isbn': {
                'required': ("Informe o isbn do livro."),
            },
            'num_pagina': {
                'required': ("Informe o número de paginas do livro."),
            },
            'edicao': {
                'required': ("Informe a edição do livro."),
            },
        }

    def clean_titulo(self):
        titulo = self.cleaned_data['titulo']
        validate_title(titulo)
        return titulo

    def clean_editora(self):
        editora = self.cleaned_data['editora']
        validate_title(editora)
        return editora
    
    def clean_autor(self):
        autor = self.cleaned_data['autor']
        validate_title(autor)
        return autor
    
    def clean_isbn(self):
        isbn = self.cleaned_data['isbn']
        validate_title(isbn)
        return isbn
    
    def clean_num_pagina(self):
        num_pagina = self.cleaned_data['num_pagina']
        validate_title(num_pagina)
        return num_pagina
    
    def clean_edicao(self):
        edicao = self.cleaned_data['edicao']
        validate_title(edicao)
        return edicao

    def clean(self):
        self.cleaned_data = super().clean()
        return self.cleaned_data
    
    