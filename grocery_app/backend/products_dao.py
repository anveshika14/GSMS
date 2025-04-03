import mysql.connector
from sql_connection import get_sql_connection
def get_all_products(connection):
    cursor = connection.cursor()
    query = ("SELECT products.product_id,products.name,products.uom_id, products.price_per_unit,uom.uom_name FROM products INNER JOIN uom on uom.uom_id=products.uom_id;")
    cursor.execute(query)
    response = []
    for (product_id,name,uom_id,price_per_unit,uom_name) in cursor:
       response.append({                
           'product_id': product_id,
           'name': name,
           'uom_id': uom_id,
           'price_per_unit': price_per_unit,    
           'uom_name': uom_name
       })
    # connection.close()
    return response
def insert_new_product(connection,product):
    cursor = connection.cursor()
    query = ("insert  into products(name,uom_id,price_per_unit)values(%s,%s,%s)")
    data=(product['product_name'],product['uom_id'],product['price_per_unit'])
    cursor.execute(query,data)
    connection.commit()
    return cursor.lastrowid
    pass
def delete_product(connection,product_id):
    cursor = connection.cursor()
    query = ("delete from products where product_id=" +str(product_id))
    cursor.execute(query)
    connection.commit()
    return cursor.lastrowid

if __name__=='__main__':
    connection = get_sql_connection()
    # print(get_all_products(connection))
    # print(insert_new_product(connection,{
    #     'product_name':'okra',
    #     'uom_id':'1',
    #     'price_per_unit':'20'
    # }))
    print(delete_product(connection,9))