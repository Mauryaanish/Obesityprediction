from flask import Flask , request , render_template,jsonify
from src.pipeline.prediction_pipeline import CustomData , PredictionPipeline



application = Flask(__name__)
app = application


@app.route('/')

def home_page():
    return render_template('index.html')

@app.route('/predict' , methods = ["GET" , "POST"])

def predict_datapoint():
    if request.method =='GET':
        return render_template('form.html')
    
    else:
        data = CustomData(
            Gender=str(request.form.get('Gender')),
            Age = int(request.form.get('Age')),
            Height = float(request.form.get('Height')),
            Weight = int(request.form.get('Weight')),
            family_history_with_overweight=str(request.form.get('family_history_with_overweight')),
            FAVC=str(request.form.get('FAVC')),
            FCVC= int(request.form.get('FCVC')),
            NCP = int(request.form.get('NCP')),
            CAEC= str(request.form.get('CAEC')),
            SMOKE = str(request.form.get('SMOKE')),
            CH2O = int(request.form.get('CH2O')),
            SCC = str(request.form.get('SCC')),
            FAF = int(request.form.get('FAF')),
            TUE = int(request.form.get('TUE')),
            CALC = str(request.form.get('CALC')),
            MTRANS=str(request.form.get('MTRANS'))

        )

        
        final_new_data = data.get_data_as_dataframe()
        predict_pipeline = PredictionPipeline()
        pred = predict_pipeline.predict(final_new_data)

        results = pred[0]

        return render_template('results.html' , final_result =results)
    




if __name__ == '__main__':
    app.run(host = '0.0.0.0' , debug = True , port = 5500)
