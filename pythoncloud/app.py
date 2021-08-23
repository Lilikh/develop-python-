from flask import Flask, request, jsonify
import pyodbc

#init
app = Flask(__name__)
conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};Server=tcp:pyt21-sqlserver21.database.windows.net,1433;Database=sqldb;Uid=nilisha;Pwd={Kash@2016edu};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')
cursor = conn.cursor()

#routes
@app.route('/api/products', methods =['GET'])
def get_all():
    products = []

    for row in cursor.execute('SELECT p.Id, p.Name, p.Description,c.Name Category from PRODUCTS p join Categories c on p.CategoryId = c.Id'):
        products.append({'id':row.Id, 'name': row.Name, 'description':row.Description, 'category':row.Category})

    return jsonify(products)

@app.route('/api/products/<id>', methods =['GET'])
def get_by_id(id):
    products = []

    result = cursor.execute('SELECT p.Id, p.Name, p.Description,c.Name Category from PRODUCTS p join Categories c on p.CategoryId = c.Id where p.Id = ?',[id]).fetchone()
    product = {
        'id': result.Id,
        'name': result.Name,
        'description': result.Description,
        'category': result.Category
    }
    return jsonify(product)
    

@app.route('/api/products', methods=['POST'])
def post():
    name = request.json['name']
    description =request.json['description']
    category_id = request.json['categoryId']

    cursor.execute('Insert into Products(Name,Description,CategoryId) Values(?,?,?)', name, description,category_id)
    result = cursor.execute('SELECT p.Id, p.Name, p.Description,c.Name Category from PRODUCTS p join Categories c on p.CategoryId = c.Id where p.Id = @@IDENTITY').fetchone()
    cursor.commit()

    product = {
        'id': result.Id,
        'name': result.Name,
        'description': result.Description,
        'category': result.Category
    }
    return jsonify(product)

if __name__ == '__main__':
    app.run()