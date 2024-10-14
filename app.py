from flask import Flask,render_template,request,redirect,url_for

app=Flask(__name__)

@app.route("/",methods=['POST','GET'])
def  index():
    return render_template("index.html")

@app.route("/index",methods=['POST','GET'])
def  indexs():
    return render_template("index.html")

@app.route("/estilos")
def est():
     return render_template("estilos.css")

@app.route("/somos")
def somos():
     return render_template("somos.html")

@app.route("/Solicitud")
def soli():
    return render_template("Solicitud.html")

@app.route("/servicios")
def serv():
    return render_template("servicios.html")

@app.route("/noticias")
def noti():
    return render_template("noticias.html")

@app.route("/contacto",methods=['POST','GET'])
def  contacto():
    if request.method =='POST': #si es una llamada del formulario
        nombre=request.form.get('usuario')
        correo=request.form.get('email')
        desc=request.form.get('descrip')
        return render_template("Solicitud.html",usuario=nombre,correo=correo,desc=desc)
    return render_template("contacto.html")

if __name__ == "__main__":
    app.run(debug=True)