from model import app, request, jsonify,db
from controller import *
import os
import json


@app.before_first_request
def create_table():
    db.create_all()

#This Api will be called when we need to create a new form 
@app.route("/Submit/form/data",methods=['POST'])
def form_data_submission():
    if request.method== 'POST':
        fd=post_data_form(request.json)
        if fd:
            return jsonify({"Status": "Succesfully added",
                            "Status_code": "200",
                           })
        else:
            return jsonify({"Status": "Failed",
                            "Status_code": "400",
                            })

#This API will be called when we need to show data to the user on the Frontend
@app.route("/fetch/form/data/<form_id>",methods=['GET'])
def fetch_form_data(form_id):
    if request.method=='GET':
        var=fetch_data(form_id)
        #json_string = json.dumps(var)
        if var:
            return jsonify({"Status": "Succesfully added",
                            "Status_code": "200",
                            "response_data":var
                           })
        else:
            return jsonify({"Status": "Failed",
                            "Status_code": "400",
                            })

#This API is called to upload the data to a google sheet.
@app.route("/upload/data_to_googlesheets/<form_id>",methods=['PUT'])
def data_to_googlesheets(form_id):
    if request.method=='PUT':
        var=data_google_sheet(form_id)
        if var:
            return jsonify({"Status": "Succesfully loaded",
                            "Status_code" : "200"
                           })
        else:
            return jsonify({"Status": "Unsuccessfull",
                            "Status_code": "400",
                            })
        



if __name__ == "__main__":
    app.run(debug=True)
