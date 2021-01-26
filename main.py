from flask import Flask, render_template

app = Flask(__name__)

@app.route('/') #to route the code to webpage

def index():

    return render_template("login.html")
    return render_template("register.html")
    return render_template("profile.html")

if __name__ == '__main__':
    app.run(debug=True)
