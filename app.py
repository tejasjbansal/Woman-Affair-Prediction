from wsgiref import simple_server
from flask import Flask, request, app,render_template
from flask import Response
from flask_cors import CORS
from logistic_deploy import predObj

app = Flask(__name__)
CORS(app)
app.config['DEBUG'] = True


class ClientApi:

    def __init__(self):
        self.predObj = predObj()



@app.route('/')
def home():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predictRoute():
    try:
        rateMarriage=int(request.form['rateMarriage'])
        age = int(request.form['age'])
        yearsMarried = int(request.form['yearsMarried'])
        children = int(request.form['children'])
        education =  int(request.form['education'])
        occupation = int(request.form['occupation'])
        husbandOccupation = int(request.form['husbandOccupation'])
        religious = int(request.form['religious'])
        occ_2 = 0
        occ_3=0
        occ_4=0
        occ_5=0
        occ_6=0
        occ_husb_2=0
        occ_husb_3=0
        occ_husb_4=0
        occ_husb_5=0
        occ_husb_6=0
        if occupation == 2:
            occ_2 = 1
        elif occupation == 3:
            occ_3 = 1
        elif occupation == 4:
            occ_4 = 1
        elif occupation == 5:
            occ_5 = 1
        elif occ_6 == 6:
            occ_6 = 1
        else:
            print(occupation)
        
        if husbandOccupation == 2:
            occ_husb_2 = 1
        elif husbandOccupation == 3:
            occ_husb_3 = 1
        elif husbandOccupation == 4:
            occ_husb_4 = 1
        elif husbandOccupation == 5:
            occ_husb_5 = 1
        elif husbandOccupation == 6:
            occ_husb_6 = 1
        else:
            print(husbandOccupation)
        data = [[1,occ_2,occ_3,occ_4,occ_5,occ_6,occ_husb_2,occ_husb_3,occ_husb_4,occ_husb_5,occ_husb_6,rateMarriage,age,yearsMarried,children,religious,education]]
        print('data is:     ', data)
        pred=predObj()
        res = pred.predict_log(data)

        print('result is        ',res)
        return render_template('result.html', prediction_text='{}'.format(res))
    except ValueError:
        return Response("Value not found")
    except Exception as e:
        print('exception is   ',e)
        return Response(e)


if __name__ == "__main__":
    clntApp = ClientApi()
    #host = '0.0.0.0'
    #port = 5000
    app.run(debug=True)