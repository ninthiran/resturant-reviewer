from flask import Flask,render_template,url_for,request
from flask_bootstrap import Bootstrap 

import pandas as pd
import numpy as np
import json
import datetime
import os
import csv


from sklearn.pipeline import Pipeline
from sklearn.svm import LinearSVC
from sklearn.multiclass import OneVsRestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.externals import joblib


app = Flask(__name__)
Bootstrap (app)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/edit', methods=['POST'])
def edit():
    
	csvFile = open('models/ReviewScraped.csv', 'a', newline='',encoding='utf-8')
	csvWriter = csv.writer(csvFile)

	if request.method == 'POST':
		starquery = request.form['starquery']
		restname = request.form['editRestname']
		reviewText = request.form['editText']
		latitude = request.form['editLatitude']
		longitude = request.form['editLongitude']

		csvWriter.writerow([reviewText ,starquery])

		csvFile.close()

	return render_template('edit.html',star = starquery,name = restname,longitude = longitude, latitude = latitude, reviewText  = reviewText )




@app.route('/predict', methods=['POST'])
def predict():
	file_path = 'models/ReviewScraped.csv'
	review_scraped_data = pd.read_csv(file_path)

	pipeline = Pipeline([('tfidf', TfidfVectorizer(analyzer='word', ngram_range=(1, 2),sublinear_tf=True,
                                    token_pattern=r'\w{1,}', max_features=20000, stop_words='english')),
                      ('bayes', OneVsRestClassifier(LinearSVC()))])

	NaiveBayes_model = pipeline.fit(review_scraped_data['text'],review_scraped_data['star'])
	text = []
	if request.method == 'POST':
		namequery = request.form['namequery']
		reviewText = request.form['reviewText']
		latitude = request.form['latitude']
		longitude = request.form['longitude']
		
		

		text.append(reviewText)

		my_prediction  = NaiveBayes_model.predict(text)

		my_prediction = my_prediction[0]
	return render_template('results.html',name = namequery,longitude = longitude, latitude = latitude, reviewText  = reviewText ,my_prediction = my_prediction)



@app.route('/view', methods=['POST'])
def view():
	if request.method == 'POST':
		restname = request.form['restname']
		
	return render_template('view.html',restname = restname)


''' SAVE PAGE '''
@app.route('/save', methods=['POST'])
def save():
	geo_data = {
    "type": "FeatureCollection",
    "features": []
	}

	if request.method == 'POST':
		starquery = request.form['saveStarvalue']
		restname = request.form['saveRestname']
		reviewText = request.form['saveText']
		latitude = request.form['saveLatitude']
		longitude = request.form['saveLongitude']

		
		geo_json_feature = {
	            "type": "Feature",
	            "geometry":{
	                "type": "Point",
	                "coordinates": [longitude,latitude]},
	            "properties": {
	                "text": reviewText,
	                "star":starquery,
	                "created_at": datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
	            }
			}

		filename = 'static/src/js/'+restname+'.json'

		if ((os.path.exists(filename)) and (os.stat(filename).st_size != 0)):
    
			with open(filename) as f:
				data = json.load(f)

			data['features'].append(geo_json_feature)
	        
			with open(filename, 'w') as fout:
				fout.write(json.dumps(data, indent=4))
		else:

			geo_data['features'].append(geo_json_feature)
	        
			with open(filename, 'w') as fout:
				fout.write(json.dumps(geo_data, indent=4))


	return render_template('save.html',star = starquery, reviewText = reviewText, restname = restname)


if __name__ == '__main__':
	app.run(debug=True)
