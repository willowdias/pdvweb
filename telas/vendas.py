from flask import Flask, render_template, request, redirect, url_for,flash
from telas.database import*
from flask import Blueprint
from flask import request
app2  = Blueprint('app2',__name__)

informacoes = []
lista_opcoes = ['willow', 'albert', 'lucas', 'matheus']
PlanoPAgamento=['Avista','1x','2x']
tipodocumento=['Dinheiro','Cartao Credito','Cartao Debito','Pix']
@app2.route('/pdv')
def pdv():
    try:
        
        return render_template('pdv.html',Quant='1',caixa="Caixa Aberto",lista_opcoes=lista_opcoes,
                               PlanoPAgamento=PlanoPAgamento,tipodocumento=tipodocumento)
    except Exception as e:
        return e
@app2.route('/venda', methods=['POST'])
def venda():
    try:
        if len(informacoes)<1:#verfica se a produto lista e cria tabela temporaria
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
        subtotal = sum(item["preco"] for item in final)#essa opçao pega soma iten preco
        valototal = sum(item["valor"] for item in final)
        informacoes.append(final)
        if len(final)>0:
            caixa="Caixa Ocupado"
        else:
            caixa="Caixa Aberto"
        return render_template('pdv.html',informacoes=final,Quant='1',
                               subtotal=subtotal,valortotal=valototal,caixa=caixa,
                               lista_opcoes=lista_opcoes,QuantidadeItens=len(final),
                               PlanoPAgamento=PlanoPAgamento,tipodocumento=tipodocumento)
    except  ValueError as e:
        print (e)        
@app2.route('/FinalizarVenda', methods=['POST'])
def FinalizarVenda():
    
    banco=select("SELECT * FROM temp_table")
    if len(banco)>0:
        cliente = request.form['cliente']
        plano = request.form['planopg']
        tipodoc = request.form['tipodc']
        
        Name=None
        if cliente=="":
            Name="Consumidor final"
        else:
            Name=cliente

        valototal = sum(item["valor"] for item in banco)
        insert(f""" insert into orca_cb (cod_cliente,nome_cli,valor) 
            VALUES (0,'{Name}','{valototal}'); """)
        
    
        #essa funçao apaga tabela criada e cria outra
        dell("DROP TABLE IF EXISTS temp_table")
        tabelaVendaTemporaria()
        flash(f" Venda Numero #{45} Finalizada ")
        return render_template('pdv.html',Quant='1',caixa="Caixa Aberto",lista_opcoes=lista_opcoes)
    else:
        flash(f" Tabela Venda Vazia ")
    
@app2.route('/deletar/<int:produto_id>', methods=['GET'])
def deletar(produto_id):
    
    
    dell(f"""delete from temp_table where id='{produto_id}' """)
    final=select("SELECT * FROM temp_table")
    subtotal = sum(item["preco"] for item in final)
    valototal = sum(item["valor"] for item in final)
    if len(final)>0:
        caixa="Caixa Ocupado"
    else:
        caixa="Caixa Aberto"
    return render_template('pdv.html',informacoes=final,Quant='1',
                            subtotal=subtotal,valortotal=valototal,
                            caixa=caixa,lista_opcoes=lista_opcoes,QuantidadeItens=len(final))

