import pymysql


db = pymysql.connect(host='127.0.0.1',
                     user='root',
                     password='',
                     database='bancojs',
                     cursorclass=pymysql.cursors.DictCursor)

def select(query):
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()

def tabelaVendaTemporaria():
    cursor = db.cursor()
    cursor.execute("""CREATE TEMPORARY TABLE temp_table(
    id INT AUTO_INCREMENT PRIMARY KEY,
    codigo_br varchar(200),
    descricao varchar(200),
    quant numeric(18,5),
    preco numeric(18,5),
    valor numeric(18,5)
    
    ); """)  

    
def insert(query):#acicionar item
    cursor = db.cursor()
    cursor.execute(query)
    return db.commit()
def dell(query):
    cursor = db.cursor()
    cursor.execute(query)
    return db.commit()
def createtabela():
    cursor = db.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS estoque(
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    codigo int,
    descricao varchar(200) NOT NULL,
    quantidade varchar(200),
    preco numeric(18,5),
    valor numeric(18,5)
    ); """)
    cursor.execute("""CREATE TABLE IF NOT EXISTS orca_cb(
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    nota int,
    cod_cliente int,
    nome_cli varchar(200),
    valor numeric(18,5)               
    ); """)

    cursor.execute("""CREATE TABLE IF NOT EXISTS orca_item(
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    nota int,
    descricao varchar(200) NOT NULL,
    quantidade varchar(200),
    preco numeric(18,5),
    valor numeric(18,5)
                   
    ); """)
    

   


    db.commit()
    cursor.close()
#tabelaVendaTemporaria()    
#insert(f"""INSERT INTO temp_table (codigo_br) VALUES ('1')""")