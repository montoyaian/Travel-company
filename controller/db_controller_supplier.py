import mysql.connector
from Classes.supplier import Supplier

DELETE_SUCCESS = {"message": "eliminacion completa"}

class DatabaseControllerSupplier():
    """
    This class is used to connect to the database and execute queries
    """

    def insert_supplier(self, supplier:Supplier ):
        connection = mysql.connector.connect(user='root',password='chDh466Ec1f4aFg31b1Fd-3f1H4FG3gF',host='viaduct.proxy.rlwy.net',database='railway',port='40559')
        cursor = connection.cursor()
        cursor.execute("""INSERT INTO  railway.supplier(
        Name,
        Contact,
        Description
        ) VALUES (%s,%s, %s)""",
        (
        supplier.name,
        supplier.contact,
        supplier.description,
        ))
        connection.commit()
        supplierj = {
        "name": supplier.name,
        "contact": supplier.contact,
        "Description": supplier.description,
        }

        return supplierj      


     
    def edit_supplier(self,supplier:Supplier ):
        connection = mysql.connector.connect(user='root',password='chDh466Ec1f4aFg31b1Fd-3f1H4FG3gF',host='viaduct.proxy.rlwy.net',database='railway',port='40559')
        cursor = connection.cursor()
        cursor.execute("""SELECT * FROM railway.supplier WHERE ID = %s""", (supplier.id,))
        result = cursor.fetchone()

        if not result :
            return {"error":"proveedor no encontrado"}

        cursor.execute("""UPDATE railway.supplier SET 
        Name = %s,
        Contact = %s,
        Description = %s
        WHERE ID = %s""",
        (
        supplier.name,
        supplier.contact,
        supplier.description,
        supplier.id,
        ))
        connection.commit()
        supplierj = {
        "id": supplier.id,
        "name": supplier.name,
        "contact": supplier.contact,
        "Description": supplier.description,
        }
        return supplierj

    def delete_supplier(self, id:int):
        connection = mysql.connector.connect(user='root',password='chDh466Ec1f4aFg31b1Fd-3f1H4FG3gF',host='viaduct.proxy.rlwy.net',database='railway',port='40559')
        """
        Delete a supplier from database
        """
        cursor = connection.cursor()
        
        cursor.execute(
        """SELECT * FROM railway.supplier WHERE id = %s""",
        (id,),
        )
        result = cursor.fetchone()
        if result:
            cursor.execute("""DELETE FROM railway.supplier  WHERE id = %s""", (id,))      
            cursor.execute("""DELETE FROM railway.first_class  WHERE ID_agency = %s""", (id,))
            cursor.execute("""DELETE FROM railway.standard_class  WHERE ID_agency = %s""", (id,))
            connection.commit()
                      
            return DELETE_SUCCESS
        else:
            return {"error":"proveedor no encontrado"}        

    def show_supplier(self,id:str):
        connection = mysql.connector.connect(user='root',password='chDh466Ec1f4aFg31b1Fd-3f1H4FG3gF',host='viaduct.proxy.rlwy.net',database='railway',port='40559')
        cursor = connection.cursor()
        if id == "all":
            cursor.execute(
            '''SELECT * FROM railway.supplier''')
            rows = cursor.fetchall()
            rowsj=[]
            for i in rows:
                rowj ={
                "id" : i[0],
                "name": i[1],
                "contact": i[2],
                "Description": i[3],
                }
                rowsj.append(rowj)
  
            return rowsj
        else:
            try:
                id = int(id)
                cursor.execute(
                '''SELECT * FROM railway.supplier WHERE id = %s''',(id,))
                rows = cursor.fetchall()
                rowj = {
                    "id": rows[0][0],
                    "name": rows[0][1],
                    "contact": rows[0][2],
                    "Description": rows[0][3]
                }
                return rowj
            except:
                {"message" : "datos no validos"}   
    def show_supplier_name(self):
        connection = mysql.connector.connect(user='root',password='chDh466Ec1f4aFg31b1Fd-3f1H4FG3gF',host='viaduct.proxy.rlwy.net',database='railway',port='40559')
        cursor = connection.cursor()
        cursor.execute(
            '''SELECT * FROM railway.supplier''')
        rows = cursor.fetchall()
        return rows
        
