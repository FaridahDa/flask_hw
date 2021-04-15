from application import app
app.config['SECRET_KEY']='TEAMD'

if __name__ == "__main__":
    app.run(debug=True)