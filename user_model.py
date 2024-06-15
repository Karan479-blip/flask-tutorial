import mysql.connector
import json
class user_model:  #class
    def __init__(self):
        try:
            self.con=mysql.connector.connect(host="localhost",user="root",password="W7301@jqir#",database="flask_tutuorial")#connect sql and python connector take 4 parameter host,user,password,database
            self.con.autocommit=True 
            self.cur=self.con.cursor(dictionary=True)
            print("Connection Successful")
        except:
            print("Some error")    

    
    def user_getall_model(self):
        self.cur.execute("SELECT * FROM user")
        result = self.cur.fetchall()
        if len(result)>0:
            return json.dumps(result)
        else:
            return "No Data Found"
        

#create operation model pair
    def user_addone_model(self,data):
        self.cur.execute(f"INSERT INTO user(name, email, phone, role, password) VALUES('{data['name']}', '{data['email']}', '{data['phone']}', '{data['role']}', '{data['password']}')")
        return "User Created Successfully"
   
     
#update operation model pair
    def user_update_model(self,data):
        self.cur.execute(f"UPDATE user SET name='{data['name']}', email='{data['email']}', phone='{data['phone']}', role='{data['role']}', password='{data['password']}' WHERE id={data['id']}")

        if self.cur.rowcount>0:
            return "User updated Successfully"
        else:
            return "Nothing to Update"

         

#delete operation model pair
    def user_delete_model(self,id):
        self.cur.execute(f"DELETE FROM user WHERE id={id}")

        if self.cur.rowcount>0:
            return "User deleted Successfully"
        else:
             return "Nothing to delete"