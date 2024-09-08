from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta_aqui'

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form.get('nome')
        if not name:
            flash('Por favor, preencha o campo nome.')
        else:
            flash(f'Hello, {name}! Seu formulário foi enviado com sucesso.')
        return redirect(url_for('home'))
    return render_template('Form.html')

if __name__ == '__main__':
    app.run(debug=True)
