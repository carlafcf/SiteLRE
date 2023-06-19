from django import forms

from django.core.mail import EmailMessage

class ContatoForm(forms.Form):
    nome = forms.CharField(label="Nome", max_length=200)
    email = forms.EmailField(label="E-mail", max_length=200)
    assunto = forms.CharField(label="Assunto", max_length=200)
    mensagem = forms.CharField(label="Mensagem", widget=forms.Textarea())

    def send_email(self):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        assunto = self.cleaned_data['assunto']
        mensagem = self.cleaned_data['mensagem']

        header_email = "Mensagem enviada pelo site do LRE"
        corpo_email = f"{assunto}\n\nNome: {nome}\nE-mail: {email}\nMensagem: {mensagem}"
        footer_email = "Entraremos em contato assim que possível. Qualquer coisa pode entrar em contato através do nosso e-mail: contato.lre.ufrn@gmail.com"

        corpo = header_email+"\n\n"+corpo_email+"\n\n"+footer_email

        mail = EmailMessage(
            subject="Contato via site: "+assunto,
            from_email=email,
            to=[email,'contato.lre.ufrn@gmail.com'],
            body=corpo,
            headers={
                'Replay-To': 'contato.lre.ufrn@gmail.com'
            }
        )

        mail.send()