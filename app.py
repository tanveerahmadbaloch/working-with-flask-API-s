### flask app routing
from flask import Flask,render_template,request,redirect,url_for

# create a simple flask web application
app=Flask(__name__)

@app.route("/", methods=["Get"])
def welcome():
    return "<h1>this is my first app</h1>"

@app.route("/index",methods=["Get"])
def index():
        return "this is second"
    
## variable rule
@app.route('/sucess/<int:score>')
def success(score):
    return "the person is passed and score is: "+ str(score)

## Create a form
# @app.route('/form',methods=['GET','POST'])
# def form():
#     if request.method=="GET":
#         return render_template('form.html')
#     else:
#         math=float(request.form['maths'])
#         science=float(request.form('science'))
#         history=float(request.form['history'])
        
#         average_marks=(math+science+history)/3
        
#         return render_template('form.html',score=average_marks)

@app.route('/calculate',methods=['POST','GET'])
def calculate():
    if request.method=='GET':
        return render_template('calculate.html')
    else:
        maths=float(request.form['maths'])
        science=float(request.form['science'])
        history=float(request.form['history'])

        average_marks=(maths+science+history)/3
        result="" 
        if average_marks>=50:
            result="success"
        else:
            result="fail"

        return redirect(url_for(result,score=average_marks))


        #return render_template('form.html',results=average_marks)

    

if __name__=="__main__":
    app.run(debug=True)
    