from flask import * 
import helmetDetect as h 
import speed as speed
app = Flask(__name__)  

@app.route('/')  
def upload():  
	return render_template("upload.html")  

@app.route('/success', methods = ['POST'])  
def success():  
	if request.method == 'POST':  
		f = request.files['file']  

		f.save("/home/user/Desktop/miniproject-13/vehicle-speed-check-master/"+f.filename)  
		return render_template("1.html", name = f.filename)  


@app.route('/secondfile', methods = ['POST'])  
def successs():  
	if request.method == 'POST':  
		f = request.files['file']  
		f.save("/home/user/Desktop/miniproject-13/yolov3-Helmet-Detection/images/"+f.filename)  
		return render_template("1.html", name = f.filename)  

@app.route('/runFunction',methods = ['GET', 'POST'])  
def abc():  
    if request.method == 'POST':
        h.mainFunction()
    if request.method == 'GET':
        h.mainFunction()
        print("Calling mainFunction")
    
    #return redirect('/',code=320)
    return render_template("upload.html") 
 

@app.route('/runSpeedFunction',methods = ['GET', 'POST'])  
def abcd():  
    if request.method == 'POST':
        speed.mainFunction()
        print("Calling mainFunction")
    if request.method == 'GET':
        speed.mainFunction()
        print("Calling mainFunction")
        
    return render_template("upload.html") 

if __name__ == '__main__':  
	app.run(threaded=True)  
	app.debug = True
