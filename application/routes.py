from flask import render_template,request

from application.forms import BasicForm
from application import app


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/welcome/<name>')
def template_base(name):
    return render_template('base.html',name=name,group='Everyone')

@app.route('/about_us')
def about_us():
    return render_template('about.html', title='About Us')

@app.route('/favourites')
def favourites():
    data = ['food', 'cake', 'elephant', 'rainbow']
    return render_template('favourites.html',data=data)



@app.route('/register', methods=['GET', 'POST'])
def register():
    error = ""
    form = BasicForm()

    if request.method == 'POST':
        first_name = form.first_name.date
        last_name = form.last_name.data

        if len(first_name) == 0 or len(last_name) == 0:
            error = "Please supply both first and last name"
        else:

            return "Thank you!"

    return render_template("register.html", form=form, message=error)

