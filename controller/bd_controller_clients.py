from Classes.standard_client import Standardclient
from Classes.premium_client import PremiumClient
from Classes.offers import Offer
from Classes.Admins import Admins
import mysql.connector
from mysql.connector import Error
from fastapi.encoders import jsonable_encoder
import jwt

from models.client_model import *

connection = mysql.connector.connect(user='root',password='@73tubgixjy4e0qo1uqaw@9k7rvvm_nt',host='monorail.proxy.rlwy.net',database='railway',port='42203')
cursor = connection.cursor()

DELETE_SUCCESS = {"message": "eliminacion completa"}
class DatabaseControllerClient():
    """
    This class is used to connect to the database and execute queries
    """
    def login(self, login_item:loginModel ):

        connection = mysql.connector.connect(user='root',password='@73tubgixjy4e0qo1uqaw@9k7rvvm_nt',host='monorail.proxy.rlwy.net',database='railway',port='42203')
        cursor = connection.cursor()
        SECRET_KEY = "travelcompany123456789"
        ALGORITHM = "HS256"
        ACCESS_TOKEN_EXPIRE_MINUTES = 800 
        cursor.execute('SELECT * FROM railway.standard_client')
        rows = cursor.fetchall()
        data = jsonable_encoder(login_item)
        for i in rows:
            if (i[1] == data['name']  ) and (i[5] == data['password']):
                encoded_jwt = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)
                return {'token': encoded_jwt ,
                        'user_role': "user"}
        cursor.execute('SELECT * FROM railway.premium_client')
        rows = cursor.fetchall()
        for i in rows:
            if (i[1] == data['name']  ) and (i[5] == data['password']):
                encoded_jwt = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)
                return {'token': encoded_jwt  ,
                        'user_role': "user"}        
        for i in Admins:
            if (i["name"] == data['name']  ) and (i["password"] == data['password']):
                encoded_jwt = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)
                return {'token': encoded_jwt ,
                        'user_role': "admin" }   

        return {"error" : "inicio de sesion fallido"}
        
        
    def insert_client(self, client: Standardclient or PremiumClient):
        connection = mysql.connector.connect(user='root',password='@73tubgixjy4e0qo1uqaw@9k7rvvm_nt',host='monorail.proxy.rlwy.net',database='railway',port='42203')
        cursor = connection.cursor()
       
        if isinstance(client,Standardclient):
            cursor.execute('''INSERT INTO railway.standard_client(
            Name,
            Contact,
            Bookings,
            Email,
            Password
            ) VALUES (%s, %s, %s, %s, %s )''',
            (   
            client.name,
            client.contact,
            0,
            client.email,
            client.password
            ))
            connection.commit()
            clientj = {
            "name": client.name,
            "contact": client.contact,
            "bookings": 0,
            "email": client.email,
            }
            return clientj

        elif isinstance(client,PremiumClient):
            cursor.execute('''INSERT INTO railway.premium_client(
            Name,
            Contact,
            Bookings,
            Email,
            Password
            ) VALUES (%s, %s, %s, %s, %s )''',
            (   
            client.name,
            client.contact,
            0,
            client.email,
            client.password
            ))
            connection.commit()
            
            clientj = {
            "name": client.name,
            "contact": client.contact,
            "bookings": client.bookings,
            "email": client.email,
            }
            return clientj

    def insert_offer(self, offer:Offer):
        connection = mysql.connector.connect(user='root',password='@73tubgixjy4e0qo1uqaw@9k7rvvm_nt',host='monorail.proxy.rlwy.net',database='railway',port='42203')
        cursor = connection.cursor()
        if offer.flight_type == "standard class":
            cursor.execute(
            """SELECT * FROM railway.standard_class WHERE id = %s""",
            (offer.id_flight,),
            )
            result = cursor.fetchone()
            if result:
                cursor.execute("""INSERT INTO railway.Offers(
                Id_flight,
                Discount,
                Customer_type,
                Flight_type
                ) VALUES (%s, %s, %s, %s)""",
                (
                offer.id_flight,
                offer.discount,
                offer.customer_type,
                offer.flight_type
                ))
                connection.commit()
                
                offerj = {
                    "Id_flight":offer.id_flight,
                    "Discount":offer.discount,
                    "Customer_type":offer.customer_type,
                    "Flight_type":offer.flight_type
                    }
                return offerj
            else:
                return{"error": "id de vuelo no encotrado"}
            
        elif offer.flight_type == "first class":
            cursor = connection.cursor()
            cursor.execute(
            """SELECT * FROM railway.first_class WHERE id = %s""",
            (offer.id_flight,),
            )
            result = cursor.fetchone()
            if result:
                cursor.execute(      """INSERT INTO  railway.Offers(
                Id_flight,
                Discount,
                Customer_type,
                Flight_type
                ) VALUES (%s, %s, %s, %s)""",
                (
                offer.id_flight,
                offer.discount,
                offer.customer_type,
                offer.flight_type
                ))
                connection.commit()
                
                offerj = {
                    "Id_flight":offer.id_flight,
                    "Discount":offer.discount,
                    "Customer_type":offer.customer_type,
                    "Flight_type":offer.flight_type
                    }
                return offerj
            else:
                return{"error": "id de vuelo no encotrado"} 
        else:
            return{"error": "tipo de vuelo no encotrado"}       
        
    def edit_client(self, client):
        connection = mysql.connector.connect(user='root',password='@73tubgixjy4e0qo1uqaw@9k7rvvm_nt',host='monorail.proxy.rlwy.net',database='railway',port='42203')
        cursor = connection.cursor()
        if isinstance(client, Standardclient):
            cursor.execute(
            """SELECT * FROM railway.standard_client WHERE id = %s""",
            (client.id,),
        )
            result = cursor.fetchone()
            if result:
                cursor.execute("""UPDATE railway.premium_client SET 
                Name = %s,
                Contact = %s,
                Email = %s,
                Password = %s
                WHERE ID = %s""",
                (
                client.name,
                client.contact,
                client.email,
                client.password,
                client.id
                ))
                connection.commit()
                
                clientj = {
                "name": client.name,
                "contact": client.contact,

                "email": client.email,
                }
                return clientj
            else:
                return{"error": "cliente no encontrado"}
        elif isinstance(client, PremiumClient):
            cursor.execute(
            """SELECT * FROM railway.premium_client WHERE id = %s""",
            (client.id,),
        )
            result = cursor.fetchone()
            if result:
                cursor.execute("""UPDATE railway.premium_client SET 
                Name = %s,
                Contact = %s,
                Email = %s,
                Password = %s
                WHERE ID = %s""",
                (
                client.name,
                client.contact,
                client.email,
                client.password,
                client.id
                ))
                connection.commit()
                
                clientj = {
                "name": client.name,
                "contact": client.contact,
                "email": client.email,
                }
                return clientj
            else:
                return{"error": "cliente no encontrado"}

    def edit_offer(self,offer:Offer):
        connection = mysql.connector.connect(user='root',password='@73tubgixjy4e0qo1uqaw@9k7rvvm_nt',host='monorail.proxy.rlwy.net',database='railway',port='42203')
        cursor = connection.cursor()
        cursor.execute(
        """SELECT * FROM railway.Offers WHERE id = %s""",
        (offer.id,),
        )
        result = cursor.fetchone()
        if result:
            if offer.flight_type == "standard class":
                cursor.execute(
                """SELECT * FROM railway.standard_class WHERE id = %s""",
                (offer.id_flight,),
                )
                result = cursor.fetchone()
                if result:
                    cursor.execute("""UPDATE railway.Offers SET
                    Id_flight = %s,
                    Discount = %s,
                    Customer_type = %s,
                    Flight_type = %s
                    WHERE id = %s""",
                    (
                    offer.id_flight,
                    offer.discount,
                    offer.customer_type,
                    offer.flight_type,
                    offer.id
                    ))
                    connection.commit()
                    
                    offerj = {
                        "ID":offer.id,
                        "Id_flight":offer.id_flight,
                        "Discount":offer.discount,
                        "Customer_type":offer.customer_type,
                        "Flight_type":offer.flight_type
                        }
                    return offerj
                else:
                    return{"error": "id de vuelo no encotrado"}            
            elif offer.flight_type == "first class":
                cursor.execute(
                """SELECT * FROM railway.first_class WHERE id = %s""",
                (offer.id_flight,),
                )
                result = cursor.fetchone()
                if result:
                    cursor.execute(      """UPDATE railway.Offers SET
                    Id_flight = %s,
                    Discount = %s,
                    Customer_type = %s,
                    Flight_type = %s
                    WHERE id = %s""",
                    (
                    offer.id_flight,
                    offer.discount,
                    offer.customer_type,
                    offer.flight_type,
                    offer.id
                    ))
                    connection.commit()
                    
                    offerj = {
                        "ID":offer.id,
                        "Id_flight":offer.id_flight,
                        "Discount":offer.discount,
                        "Customer_type":offer.customer_type,
                        "Flight_type":offer.flight_type
                        }
                    return offerj
                else:
                    return{"error": "id de vuelo no encotrado"} 
            else:
                return{"error": "tipo de vuelo no encotrado"}            
        else:
            return{"error": "reserva no encontrada"}  
                   
    def delete_client(self, id: int, client_type: str):
        connection = mysql.connector.connect(user='root',password='@73tubgixjy4e0qo1uqaw@9k7rvvm_nt',host='monorail.proxy.rlwy.net',database='railway',port='42203')
        """
        Delete a client from database
        """
        cursor = connection.cursor()
        client_type.lower()
        if (client_type == "premium client"):
            cursor.execute("""SELECT * FROM railway.premium_client WHERE ID = %s """,(id,))
            result = cursor.fetchone()
            if result:
                cursor.execute("""DELETE FROM railway.premium_client  WHERE id = %s""", (id,))
                connection.commit()
                cursor.execute("""SELECT * FROM railway.bookings WHERE Id_client = %s AND Type_client = 'premium client' """,(id,))
                rows = cursor.fetchall()
                for  booking in rows:  
                    if booking[4] == "standard class":
                        cursor.execute("""SELECT * FROM railway.standard_class WHERE ID= %s""", (booking[2],))
                        flight = cursor.fetchone()
                        flight_new_position = flight[4] + booking[1]

                        cursor.execute(
                        """UPDATE railway.standard_class SET
                        Positions=%s
                        WHERE id = %s""",
                        (
                        flight_new_position,
                        flight[0],
                        ),
                        )
                        connection.commit()   
                    else:
                        cursor.execute("""SELECT * FROM railway.first_class WHERE ID= %s""", (booking[2],))
                        flight = cursor.fetchone()
                        flight_new_position = flight[4] + booking[1]
                        cursor.execute(
                        """UPDATE railway.first_class SET
                        Positions=%s
                        WHERE id = %s""",
                        (
                        flight_new_position,
                        flight[0],
                        ),
                        )
                        connection.commit()
                cursor.execute("""DELETE FROM railway.bookings  WHERE id_client = %s AND Type_client = 'premium client'""", (id,))
                connection.commit()
                
                return DELETE_SUCCESS
            else:
                return{"error":"cliente no encontrado"}
                            
        elif (client_type == "standard client"):
            cursor.execute("""SELECT * FROM railway.standard_client WHERE ID = %s """,(id,))
            result = cursor.fetchone()
            if result:
                cursor.execute("""DELETE FROM railway.standard_client WHERE id = %s""", (id,))
                connection.commit()
                cursor.execute("""SELECT * FROM railway.bookings WHERE Id_client = %s AND Type_client = 'standard client' """,(id,))
                rows = cursor.fetchall()
                for  booking in rows:  
                    if booking[4] == "standard class":
                        cursor.execute("""SELECT * FROM railway.standard_class WHERE ID= %s""", (booking[2],))
                        flight = cursor.fetchone()
                        flight_new_position = flight[4] + booking[1]
                        cursor.execute(
                        """UPDATE railway.standard_class SET
                        Positions=%s
                        WHERE id = %s""",
                        (
                        flight_new_position,
                        flight[0],
                        ),
                        )
                        connection.commit()   
                    else:
                        cursor.execute("""SELECT * FROM railway.first_class WHERE ID= %s""", (booking[2],))
                        flight = cursor.fetchone()
                        flight_new_position = flight[4] + booking[1]
                        cursor.execute(
                        """UPDATE railway.first_class SET
                        Positions=%s
                        WHERE id = %s""",
                        (
                        flight_new_position,
                        flight[0],
                        ),
                        )
                        connection.commit()
                cursor.execute("""DELETE FROM railway.bookings  WHERE Id_client = %s AND Type_client = 'standard client'""", (id,))
                connection.commit()
                
                return DELETE_SUCCESS
            else:
                return{"error":"cliente no encontrado"}
        else:
            return {"error":"cliente no encontrado"}
        
    def delete_offer(self, id:int):
        connection = mysql.connector.connect(user='root',password='@73tubgixjy4e0qo1uqaw@9k7rvvm_nt',host='monorail.proxy.rlwy.net',database='railway',port='42203')
        cursor = connection.cursor()
        """
        Delete a offer from database
        """
        cursor.execute(
        """SELECT * FROM railway.Offers WHERE id = %s""",
        (id,),
        )
        result = cursor.fetchone()
        if result:
            cursor.execute("""DELETE FROM railway.Offers  WHERE id = %s""", (id,))
            connection.commit()
            
            return DELETE_SUCCESS   
        else:
            return {"error":"oferta no encontrada"} 

    def show_client(self, table_name:str, id: str):
        connection = mysql.connector.connect(user='root',password='@73tubgixjy4e0qo1uqaw@9k7rvvm_nt',host='monorail.proxy.rlwy.net',database='railway',port='42203')
        cursor = connection.cursor()
        try:
            if table_name == "all":
                cursor.execute('SELECT * FROM railway.standard_client')
                rows = cursor.fetchall()
                cursor.execute('SELECT * FROM railway.premium_client')
                rows += cursor.fetchall()
                rowsj=[]
                for i in rows:
                    rowj = {
                    "id":i[0],
                    "name": i[1],
                    "contact": i[2],
                    "bookings": i[3],
                    "email": i[4],
                    }
                    rowsj.append(rowj)
    
                return rowsj
            else:
                if id == "all":
                    cursor.execute(
                        '''SELECT * FROM railway.{}'''.format(table_name))
                    rows = cursor.fetchall()
                    rowsj=[]
                    for i in rows:
                        rowj ={
                        "id":i[0],
                        "name": i[1],
                        "contact": i[2],
                        "bookings": i[3],
                        "email": i[4],
                        }
                        rowsj.append(rowj)
    
                    return rowsj

                else:
                    cursor.execute(
                        '''SELECT * FROM railway.{} WHERE id = {}'''.format(table_name, id))
                    rows = cursor.fetchall()
                    rowj = {
                    "id":rows[0][0],
                    "name": rows[0][1],
                    "contact": rows[0][2],
                    "bookings": rows[0][3],
                    "email": rows[0][4],
                    }
                    return rowj           
        except:
            return {"error": "datos no encontrados"}     

    def show_offer(self, id:str):
        connection = mysql.connector.connect(user='root',password='@73tubgixjy4e0qo1uqaw@9k7rvvm_nt',host='monorail.proxy.rlwy.net',database='railway',port='42203')
        cursor = connection.cursor()
        if id == "all":
            cursor.execute(
                '''SELECT * FROM railway.Offers''')
            rows = cursor.fetchall()
            rowsj=[]
            for i in rows:
                rowj ={
                "id":i[0],
                "Id_flight":i[1],
                "Discount":i[2],
                "Customer_type":i[3],
                "Flight_type":i[4]
                }
                rowsj.append(rowj)
    
            return rowsj
        else:
            try:
                cursor.execute(
                '''SELECT * FROM railway.Offers WHERE ID = %s''',(id,))
                rows = cursor.fetchone()
                rowj = {
                "id":rows[0],
                "Id_flight":rows[1],
                "Discount":rows[2],
                "Customer_type":rows[3],
                "Flight_type":rows[4]
                }
 
                return rowj
            except:
                {"message" : "datos no validos"}
        
        
        
        
    def premium_clients(self):
        connection = mysql.connector.connect(user='root',password='@73tubgixjy4e0qo1uqaw@9k7rvvm_nt',host='monorail.proxy.rlwy.net',database='railway',port='42203')
        cursor = connection.cursor()
        cursor.execute(
        """SELECT * FROM railway.standard_client WHERE Bookings >= %s""",
        (4,),
        )
        for row in cursor.fetchall():
            cursor.execute(
            """INSERT INTO  railway.premium_client(
            Name,
            Contact,
            Bookings,
            Email,
            Password
            ) VALUES (%s, %s, %s, %s, %s )""",
            (
            row[1], 
            row[2], 
            row[3], 
            row[4], 
            row[5]
            ))
            cursor.execute("""DELETE FROM railway.standard_client WHERE id = %s""", (row[0],))
            connection.commit()
        cursor.execute(
        """SELECT * FROM railway.premium_client WHERE Bookings  < %s""",
        (4,),
        )
        for row in cursor.fetchall():
            cursor.execute(
            """INSERT INTO  railway.standard_client(
            Name,
            Contact,
            Bookings,
            Email,
            Password
            ) VALUES (%s, %s, %s, %s, %s )""",
            (
            row[1], 
            row[2], 
            row[3], 
            row[4], 
            row[5]
            ))
            cursor.execute("""DELETE FROM railway.premium_client WHERE id = %s""", (row[0],))
            connection.commit()
        cursor.execute('SELECT * FROM railway.premium_client')
        rows = cursor.fetchall()
        rowsj=[]
        for i in rows:
            rowj ={
            "id" : i[0],
            "name": i[1],
            "contact": i[2],
            "Bookings": i[3],
            "Email" : i[4]
            }
            rowsj.append(rowj)
    
        return rowsj                   

 
        