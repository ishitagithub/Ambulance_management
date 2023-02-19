from flask import Flask, render_template,request
import geocoder
app = Flask(__name__) 
 
@app.route('/') 
def index(): 
    return render_template("final.html",email=email,phone_no=phone_no,my_add=my_add) 
@app.route('/',methods=['POST'])
def getvalue():
    dname=request.form['dname']
    hname=request.form['hname']
    tel=request.form['tel']
    data=request.form['data']
    g = geocoder.ip("me")
    my_add = g.address
    location = geolocator.geocode(my_add)
    import mysql.connector
    mydb=mysql.connector.connect(user='root',
                                 host='localhost',
                                 password='Ishita.mysql')
    mycur=mydb.cursor(buffered=True)
    mycur.execute("use haxios")
    v="insert into patient_data values(%s,%s,%s,%s)"
    data=(dname,hname,tel,data)
    mycur.execute(v,data)
    mycur.exceute("select * from hospitals")
    least_dis=0
    for i in mycur:
        if i[1]==dname and i[2] is None:
	    distance=geopy.distance.geodesic(coords_1, coords_2).km
	    if (distance<least_dis):
		least_dis=distance
	    	least_dis_h=i[0]
	else if i[1]==dname and i[2]==hname:
	    distance=geopy.distance.geodesic(coords_1, coords_2).km
	    if (distance<least_dis):
		least_dis=distance
	    	least_dis_h=i[0]
    for i in mycur:
	if i[0]==least_dis_h
            email=i[3]
            phone_no=i[4]
	    hosp_add=i[5]
    mydb.commit()
    return render_template('pass.html',dname=dname,hname=hname,tel=tel,data=data,email=email,phone_no=phone_no,my_add=my_add,hosp_add=hosp_add)
if __name__ == '__main__': 
    app.run(debug=True)
