from app import app
from model.user_model import user_model #import folder first user_model is class and second is variable
from flask import request
obj = user_model() #created an object
@app.route("/user/getall")
def user_getall_controller():
    return obj.user_getall_model() #call user_model


#create operation
@app.route("/user/addone")
def user_addone_controller():
    return obj.user_addone_model(request.form)

#update operation
@app.route("/user/update")
def user_update_controller():
    return obj.user_update_model(request.form)




#delete operation
@app.route("/user/delete/<id>",methods=["DELETE"])
def user_delete_controller(id):
    return obj.user_delete_model(id)