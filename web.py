from flask import Flask, render_template, url_for, request, redirect
app = Flask(__name__)
import csv
def write_to_csv(data):
     with open('database.csv', newline='', mode='a') as database:
          email = data['email']
          message = data['subject']
          subject = data['message']
          csv_writer= csv.writer(database, delimiter = ',', quotechar='/', quoting= csv.QUOTE_MINIMAL)
          csv_writer.writerow([email, subject, message])

@app.route('/<page_name>')
@app.route('/<page_name>')
def page(page_name):
     return render_template(page_name)

@app.route('/submit_form', methods=['GET', 'POST'])
def submit_form():
     if request.method == 'POST':
          data = request.form.to_dict()
          print(data)
          write_to_csv(data)
          return redirect('/thanks.html')
     else:
          return 'something went wrong'



          
