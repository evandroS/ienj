from flask import Flask, render_template, redirect, request, flash
from flask_mail import Mail, Message
from config import email, senha


app = Flask(__name__)
app.secret_key = 'senhateste'


mail_settings = {
    "MAIL_SERVER": 'smtp.office365.com',
    "MAIL_PORT": 587,
    "MAIL_USE_TLS": True,
    "MAIL_USE_SSL": False,
    "MAIL_USERNAME": email,
    "MAIL_PASSWORD": senha

    #smtp-mail.outlook.com

}
app.config.update(mail_settings)
mail = Mail(app)

class Contato:
    def __init__(self, nome, email,assunto,telefone,celular, mensagem):
        self.nome = nome
        self.email = email
        self.assunto = assunto
        self.telefone = telefone
        self.celular = celular
        self.mensagem = mensagem

#cria as funções para abrir a pagina
@app.route("/")
def homepage():
    return render_template('home.html')

@app.route('/send',methods=['GET','POST'])
def send():
    if request.method == 'POST':
        formContato = Contato(
            request.form["nome"],
            request.form["email"],
            request.form["assunto"],
            request.form["telefone"],
            request.form["celular"],
            request.form["mensagem"]
        )
        msg = Message(
            subject = formContato.assunto +' - CONTATO IENJ',#assunto
            sender = app.config.get("MAIL_USERNAME"),
            recipients = ['evandro@incsoft.com.br', app.config.get("MAIL_USERNAME")],
            body = f'''
            Contato:  {formContato.nome} 
            Assunto:  {formContato.assunto}
            E-mail:   {formContato.email}
            Telefone: {formContato.telefone}
            Celular:  {formContato.celular}
            ________________________________________________________________________________
            Mensagens:'<p>' {formContato.mensagem} '</p>'
            '''



        )
        mail.send(msg)
        flash("Mensagem enviada com sucesso")
    return redirect("/")


#coloca o site no Ar
if __name__ == "__main__":
    app.run(debug=True)

