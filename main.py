from flask import Flask, render_template, request, redirect, url_for
import pymysql
from database import*
from flask import Flask, render_template, flash, redirect, url_for
from flask import request
app = Flask(__name__)

informacoes = []
app.secret_key = '123'
@app.route('/')
def index():
    try:
        
        return render_template('index.html',Quant='1',caixa="Caixa Aberto")
    except Exception as e:
        return e
@app.route('/venda', methods=['POST'])
def venda():
    try:
        if len(informacoes)<1:
            tabelaVendaTemporaria()
       
    except ValueError as e:
        print(e)
    try:
        descricaocodigo = request.form['descricao']
        banco=select(f"SELECT * FROM estoque where descricao='{descricaocodigo}'")
        quant = request.form['quantidade']
        if not banco:
            flash('Produto Nao Cadastrado')
            
        elif not quant:
            flash('Produto Nao Cadastrado')
        
            
        else:
            valorfinal=(float(banco[0]['preco'])*float(quant))
            insert(f"""INSERT INTO temp_table (codigo_br,descricao,quant,preco,valor) VALUES
                
                ({banco[0]['codigo']},'{banco[0]['descricao']}',
                {quant},'{banco[0]['preco']}',
                '{valorfinal}'); """)
            
        final=select("SELECT * FROM temp_table")
        subtotal = sum(item["preco"] for item in final)
        valototal = sum(item["valor"] for item in final)
        informacoes.append(final)
        if len(final)>0:
            caixa="Caixa Ocupado"
        else:
            caixa="Caixa Aberto"
        return render_template('index.html',informacoes=final,Quant='1',
                               subtotal=subtotal,valortotal=valototal,caixa=caixa)
    except  ValueError as e:
        print (e)        
@app.route('/FinalizarVenda', methods=['POST'])
def FinalizarVenda():
    flash(f" Venda Numero #45 Finalizada ")
    return redirect(url_for('index'))
@app.route('/deletar/<int:produto_id>', methods=['GET'])
def deletar(produto_id):
    
    
    dell(f"""delete from temp_table where id='{produto_id}' """)
    final=select("SELECT * FROM temp_table")
    subtotal = sum(item["preco"] for item in final)
    valototal = sum(item["valor"] for item in final)
    if len(final)>0:
        caixa="Caixa Ocupado"
    else:
        caixa="Caixa Aberto"
    return render_template('index.html',informacoes=final,Quant='1',
                            subtotal=subtotal,valortotal=valototal,caixa=caixa)

if __name__ == '__main__':
    app.run(debug=True)
