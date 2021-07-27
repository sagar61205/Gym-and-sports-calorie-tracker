from flask import Flask, request, render_template
from flask import Response
import os
from flask_cors import CORS, cross_origin
from prediction_Validation_Insertion import pred_validation
from trainingModel import trainModel
from training_Validation_Insertion import train_validation
import flask_monitoringdashboard as dashboard
from predictFromModel import prediction
import pickle
import numpy as np

os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)
dashboard.bind(app)
CORS(app)

@app.route("/", methods=['GET'])
@cross_origin()
def home():
    return render_template('home.html')


@app.route("/batch_prediction", methods=['GET'])
@cross_origin()
def batch_prediction():
    return render_template('batch_prediction.html')


fitbit_model_path = 'XGBoost2.sav'
fitbit_model = pickle.load(
    open(fitbit_model_path, 'rb'))


@ app.route('/value-prediction', methods=['GET'])
def value_prediction():
    title = 'Calorie tracker'
    return render_template('value-based-prediction.html', title=title)


@ app.route('/value-prediction-result', methods=['POST'])
def value_prediction_result():
    title = 'Calorie tracker'

    if request.method == 'POST':
        TotalSteps = float(request.form['total'])
        VeryActiveDistance = float(request.form['veryd'])
        ModeratelyActiveDistance = float(request.form['moderated'])
        LightActiveDistance = float(request.form['lightd'])
        VeryActiveMinutes = float(request.form['verym'])
        FairlyActiveMinutes = float(request.form['fairlym'])
        LightlyActiveMinutes = float(request.form['lightm'])
        SedentaryMinutes = float(request.form['sedentarym'])


        data = np.array([[TotalSteps, VeryActiveDistance, ModeratelyActiveDistance, LightActiveDistance,
                          VeryActiveMinutes, FairlyActiveMinutes, LightlyActiveMinutes, SedentaryMinutes]])
        my_prediction = fitbit_model.predict(data,validate_features=False)
        final_prediction = my_prediction[0]

        return render_template('value-result.html', prediction=final_prediction, title=title)

    else:

        return render_template('try_again.html', title=title)



@app.route("/predict", methods=['POST'])
@cross_origin()
def predictRouteClient():
    try:
        if request.json is not None:
            path = request.json['filepath']

            pred_val = pred_validation(path) #object initialization

            pred_val.prediction_validation() #calling the prediction_validation function

            pred = prediction(path) #object initialization

            # predicting for dataset present in database
            path = pred.predictionFromModel()
            return Response("Prediction File created at %s!!!" % path)
        elif request.form is not None:
            path = request.form['filepath']

            pred_val = pred_validation(path) #object initialization

            pred_val.prediction_validation() #calling the prediction_validation function

            pred = prediction(path) #object initialization

            # predicting for dataset present in database
            path = pred.predictionFromModel()
            return Response("Prediction File created at %s!!!" % path)

    except ValueError:
        return Response("Error Occurred! %s" %ValueError)
    except KeyError:
        return Response("Error Occurred! %s" %KeyError)
    except Exception as e:
        return Response("Error Occurred! %s" %e)



@app.route("/train", methods=['POST'])
@cross_origin()
def trainRouteClient():

    try:
        if request.json['folderPath'] is not None:
            path = request.json['folderPath']
            train_valObj = train_validation(path) #object initialization

            train_valObj.train_validation()#calling the training_validation function


            trainModelObj = trainModel() #object initialization
            trainModelObj.trainingModel() #training the model for the files in the table


    except ValueError:

        return Response("Error Occurred! %s" % ValueError)

    except KeyError:

        return Response("Error Occurred! %s" % KeyError)

    except Exception as e:

        return Response("Error Occurred! %s" % e)
    return Response("Training successfull!!")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
