# importing the necessary dependencies
from flask import Flask, render_template, request
from flask_cors import cross_origin
import training_file as train
import training_val as train_val_link
import Prediction as pred
import pickle
from data_ingestion import data_loader
from application_logging.logging import logger_app
import warnings
warnings.filterwarnings("ignore")

app = Flask(__name__) # initializing a flask app

loaded_scalar = pickle.load(open('finalized_scalar.pickle', 'rb'))
loaded_model = pickle.load(open('Model/Random Forest/Random Forest.sav', 'rb'))

@app.route('/',methods=['GET'])  # route to display the home page
@cross_origin()
def homePage():
    return render_template("index.html")


@app.route('/train' , methods=['POST','GET'])
@cross_origin()
def training():
    train_val_obj = train_val_link.Train_Validation()  # object initialization

    train_val_obj.train_validation()#calling the training_validation function
    train_obj = train.training()
    train_obj.trainingModel()
    return render_template("index.html")

@app.route('/predict',methods=['POST','GET']) # route to show the predictions in a web UI
@cross_origin()
def index():
    if request.method == 'POST':
        file_object = open("Prediction_Logs/PredictionLog.txt", 'a+')
        log_writer = logger_app()
        log_writer.log(file_object, 'Start For Gathering Data for prediction')
        try:
            # reading the inputs given by the user
            national_inv = float(request.form['national_inv'])
            sales_3_month = float(request.form['sales_3_month'])
            sales_6_month = float(request.form['sales_6_month'])
            sales_9_month = float(request.form['sales_9_month'])
            forecast_3_month = float(request.form['forecast_3_month'])
            forecast_6_month = float(request.form['forecast_6_month'])
            forecast_9_month = float(request.form['forecast_9_month'])
            perf_6_month_avg = float(request.form['perf_6_month_avg'])
            perf_9_month_avg = float(request.form['perf_9_month_avg'])

            """
            CURRENTLY WORKING ON THIS 
            p = pred.prediction() #Predict A File
            data = p.convert_input_into_data([forecast_3_month,forecast_6_month,forecast_9_month,sales_1_month,sales_3_month,sales_6_month,sales_9_month,perf_6_month_avg,perf_9_month_avg])
            p.get_prediction(data)
            log_writer.log(file_object, 'Start For Prediction')

            predict = data_loader.Data_Getter()
            prediction = predict.prediction_data()
            """
            #using pickle
            tranfm_f = loaded_scalar.transform([[national_inv,sales_3_month,sales_6_month,sales_9_month,forecast_3_month,forecast_6_month,forecast_9_month,perf_6_month_avg,perf_9_month_avg]])
            ans = loaded_model.predict(tranfm_f)
            # showing the prediction results in a UI
            if(ans[0]==0):
                return render_template('predict.html', prediction = 0)
            else:
                return render_template('predict.html', prediction= 1)
            log_writer.log(file_object , "Prediction process Completed...")
            file_object.close()

        except Exception as e:
            print('The Exception message is: ', e)
            return 'something is wrong'

    else:
        return render_template('index.html')


if __name__ == "__main__":
    #app.run(debug=True)
     app.run(debug=True , port='8080')
