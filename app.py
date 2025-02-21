from flask import Flask,request,render_template
app = Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")

@app.route('/home',methods=["post"])
def result():
    try:
        if request.method=="POST":
            percentage = int(request.form.get("percentage"))
            present = int(request.form.get("present"))
            total = int(request.form.get("total"))

            if total == 0 or total < present:
                raise ValueError("Total attendance cannot be zero or less than present.")
        
            print(percentage,present,total)
            day_to_bunk=int((100 * present - percentage * total) // percentage)
            current_attendence =  (present/total)*100
            rem_att = int((percentage * total - 100 * present) / (100 - percentage))

            x=total+rem_att
            i=0
            bunk=f"You can bunk for {day_to_bunk} more days/lectures."
            current=f"Current Attendance {current_attendence:.2f}"
            
            print(day_to_bunk,current_attendence,bunk)
 

            if day_to_bunk<0:
                i=present+rem_att
                bunk = rem_att
                bunk=f"You need to attend {bunk:.2f} more classes to attain {percentage}% attendance"
            att_then = f"Attendance then {i}/{x} = {(i/x)*100:.2f}%"
            return render_template('index.html',bunk=bunk,current=current,att_then=att_then)
            

    except Exception as e:
        error=str(e)
        return render_template("index.html",e=error)
 
# app.run(host="localhost",port=5500,debug=True)
