from flask import Flask ,render_template


app = Flask(__name__)

@app.route("/")
def default():
    return render_template("index.html",x=8,y=8,color1="red",color2="black")


@app.route("/<int:x>")
def passX(x):
    return render_template("index.html",x=x,y=8,color1="red",color2="black")

@app.route("/<int:x>/<int:y>")
def passXY(x,y):
    return render_template("index.html",x=x,y=y,color1="red",color2="black")


@app.route("/<int:x>/<int:y>/<color1>/<color2>")
def passXYcolors(x,y,color1,color2):
    return render_template("index.html",x=x,y=y,color1=color1,color2=color2)

@app.errorhandler(404)
def not_found_error(error):
    return "404,Sorry! No response. Try again."
    

if __name__=="__main__": 
    app.run(debug=True)
