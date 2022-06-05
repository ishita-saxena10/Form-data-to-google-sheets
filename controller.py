from model import *
import pandas as pd
import pygsheets

def post_data_form(data):
    """This Function is being called in the submit form data API.We need to pass info about
    the various entities of the Tables: Form and FormResponse."""
    try:
        data_form=Form(user_id=data["user_id"],
                    form_category=data["form_category"],
                    question_no=data["question_no"],
                    answer_no=data["answer_no"])
        
        #db.session object can be used to manage database changes
        db.session.add(data_form)  #this statments issues a INSERT Statement
        db.session.commit()       #This commits the changes to the database
        
    
    except Exception as e:
        print (e)
        return False
    
    try:

        for i in range(data_form.question_no):
            response_form=FormResponse(form_id=data_form.id,
                                    questions=data[f"questions{i+1}"],
                                    answers=data[f"answers{i+1}"])
            
            db.session.add(response_form)
            db.session.commit()
    except Exception as e:
        print (e)
        return False
    return True
    

def fetch_data(form_id):
    """This Function is being called in the fetch form data API.We need to fetch info from
    the Tables: Form and FormResponse and display it to the user."""
    resp=db.engine.execute(f"select * from form f inner join form_response fr on f.id=fr.form_id where form_id={form_id};")
    result = [dict(res) for res in resp]
    print (result)
    return (result)


def data_google_sheet(form_id):
    """This Function is being called in the upload form data to google sheets API.
    Firstly,With the help of Pandas Library,we will create a dataframe that stores information from
    the Tables: Form and FormResponse"""
    try:
        df = pd.read_sql_query(f"""
                select * from form f inner join form_response fr on f.id=fr.form_id 
                where form_id={form_id};
                """, db.session.bind)
        
    
        gc = pygsheets.authorize(service_file=r'C:\Users\HP\Desktop\Atlan_Assignment\ishita-saxena-9db534b6db63.json')
        #To open the google spreadsheet (where 'PY' is the name of my sheet)
        sheet = gc.open('PY')
        #select the first sheet
        wks = sheet[0]
        #update the first sheet with df
        wks.set_dataframe(df,(1,1))
        return True
    
    except Exception as e:
        print (e)
        return False
    

    