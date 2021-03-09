from flask import Flask, render_template, request
from APP_Module import Get_Token

posts = [{'ConsentLifeSpan': '0',
  'DefaultLanguage': 'th',
  'Description': 'ทดสอบสร้างจาก API',
  'Label': 'P1 : สร้างจาก API',
  'Languages': [{'Default': 'true',
                 'Description': 'ทดสอบสร้างจาก API',
                 'Language': 'th',
                 'Name': 'P1 : สร้างจาก API'},
                {'Default': 'false',
                 'Description': 'Test create from API',
                 'Language': 'en-us',
                 'Name': 'P1 : Create from API'}],
  'Name': 'P1 : สร้างจาก API',
  'Organizations': ['MSC_TEST_SUB1'],
  'Status': 'ACTIVE',
  'Version': 1,
  'purposeId': 'ccca4536-934a-4ba2-aa8b-82c06e286568'},
 {'ConsentLifeSpan': '0',
  'DefaultLanguage': 'th',
  'Description': 'ทดสอบสร้างจาก API',
  'Label': 'P2 : สร้างจาก API',
  'Languages': [{'Default': 'true',
                 'Description': 'ทดสอบสร้างจาก API',
                 'Language': 'th',
                 'Name': 'P2 : สร้างจาก API'},
                {'Default': 'false',
                 'Description': 'Test create from API',
                 'Language': 'en-us',
                 'Name': 'P2 : Create from API'}],
  'Name': 'P2 : สร้างจาก API',
  'Organizations': ['MSC_TEST_SUB2'],
  'Status': 'ACTIVE',
  'Version': 1,
  'purposeId': '32bfe6a1-9c0f-4fe2-a2eb-82de85a3db68'},
 {'ConsentLifeSpan': '0',
  'DefaultLanguage': 'en-us',
  'Description': 'Test create from API',
  'Label': 'P3 : Create from API',
  'Languages': [{'Default': 'true',
                 'Description': 'Test create from API',
                 'Language': 'en-us',
                 'Name': 'P3 : Create from API'},
                {'Default': 'false',
                 'Description': 'ทดสอบสร้างจาก API',
                 'Language': 'th',
                 'Name': 'P3 : สร้างจาก API'}],
  'Name': 'P3 : Create from API',
  'Organizations': ['MSC_TEST_SUB1'],
  'Status': 'ACTIVE',
  'Version': 1,
  'purposeId': '693712bf-2d76-4f7e-b15c-02fa694f0127'},
 {'ConsentLifeSpan': '0',
  'DefaultLanguage': 'en-us',
  'Description': 'Test create from API',
  'Label': 'P4 : Create from API',
  'Languages': [{'Default': 'true',
                 'Description': 'Test create from API',
                 'Language': 'en-us',
                 'Name': 'P4 : Create from API'},
                {'Default': 'false',
                 'Description': 'ทดสอบสร้างจาก API',
                 'Language': 'th',
                 'Name': 'P4 : สร้างจาก API'}],
  'Name': 'P4 : Create from API',
  'Organizations': ['MSC_TEST_SUB2'],
  'Status': 'ACTIVE',
  'Version': 1,
  'purposeId': 'c3287833-a815-429d-8655-c5d204fe9c56'}]

class credential_form(Form):
    name = StringField('name')
    submit1 = SubmitField('submit')

app = Flask(__name__)
@app.route('/')
def index():
  credential_form = credential_form()
  return render_template('index.html', title='OneTrust Consent' , posts=posts , form=credential_form)

if __name__ == '__main__':
    app.run(debug=True)

 