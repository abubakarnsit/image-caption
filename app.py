from flask import Flask,render_template,redirect,request
import caption_it

app=Flask(__name__)

@app.route('/')#routing i.e when a client will enter this url the below function will performed
def hello():
	return render_template("index.html")  #write html code in this index.html file saved in templates folder
   


@app.route('/', methods=['POST'])
def marks():
	if request.method=='POST':
		f=request.files['userfile']
		path="./static/{}".format(f.filename)
		f.save(path)
		caption=caption_it.caption_this_image(path)
		diction={
		'image':path,
		'caption':caption
		}
	return render_template('index.html',your_result=diction)



if __name__=='__main__':
	app.run(debug=False,threaded=False)
