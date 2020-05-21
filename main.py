from flask import Flask,render_template,request

app=Flask(__name__)
@app.route('/')

def index():
    return render_template('nav.html')

@app.route('/',methods=['POST'])

def get_value():
    team1=request.form['team1']
    team2=request.form['team2']

    def custom_accuracy(y_test,y_pred,thresold):
            right = 0
            l = len(y_pred)
            for i in range(0,l):
                if(abs(y_pred[i]-y_test[i]) <= thresold):
                    right += 1
            return ((right/l)*100)
    
    import numpy as np
    import pandas as pd
    # Importing the dataset

    dataset = pd.read_csv('https://raw.githubusercontent.com/codophobia/CricketScorePredictor/master/data/ipl.csv')

    X = dataset.iloc[:,[7,8,9,12,13]].values
    y = dataset.iloc[:, 14].values


    # Splitting the dataset into the Training set and Test set
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)

    # Feature Scaling
    from sklearn.preprocessing import StandardScaler
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    X_test = sc.transform(X_test)

    # Training the dataset
    from sklearn.linear_model import LinearRegression
    lin = LinearRegression()
    lin.fit(X_train,y_train)

    # Testing the dataset on trained model
    y_pred = lin.predict(X_test)
    score = lin.score(X_test,y_test)*100
    #print("R square value:" , score)
    print("Custom accuracy:" , custom_accuracy(y_test,y_pred,10))
    

    # Testing with a custom input

    #a=input("enter current score : ")
    #b=input("enter wickets fall : ")
    #c=input("enter current over :")
    #d=input("striker score up to that instance :")
    #e=input("non-striker score up to that instance :")
    #a,b,c,d,e=float(a),float(b),float(c),float(d),float(e)

    if((team1=='KKR' and team2=='CSK') or (team1=='CSK' and team2=='KKR')):
        new_predictionKKR = lin.predict(sc.transform(np.array([[100,3,13,36,18]])))
        new_predictionCSK = lin.predict(sc.transform(np.array([[101,2,13,42,11]])))
        if(new_predictionKKR > new_predictionCSK):
            i='KKR'
        else:
            i='CSK'
    elif((team1=='KKR' and team2=='MI') or (team1=='MI' and team2=='KKR')):
        new_predictionKKR = lin.predict(sc.transform(np.array([[100,3,13,36,18]])))
        new_predictionMI = lin.predict(sc.transform(np.array([[82,3.5,13,29,6.5]])))
        if(new_predictionKKR > new_predictionCSK):
            i='KKR'
        else:
            i='MI'
    elif((team1=='KKR' and team2=='DD') or (team1=='DD' and team2=='KKR')):
        new_predictionKKR = lin.predict(sc.transform(np.array([[100,3,13,36,18]])))
        new_predictionDD = lin.predict(sc.transform(np.array([[101,3,13,39,19]])))
        if(new_predictionKKR > new_predictionCSK):
            i='KKR'
        else:
            i='DD'
    elif((team1=='KKR' and team2=='RR') or (team1=='RR' and team2=='KKR')):
        new_predictionKKR = lin.predict(sc.transform(np.array([[100,3,13,36,18]])))
        new_predictionRR = lin.predict(sc.transform(np.array([[92,3,13,33,8]])))
        if(new_predictionKKR > new_predictionRR):
            i='KKR'
        else:
            i='RR'

    elif((team1=='KKR' and team2=='RCB') or (team1=='RCB' and team2=='KKR')):
        new_predictionKKR = lin.predict(sc.transform(np.array([[100,3,13,36,18]])))
        new_predictionRCB = lin.predict(sc.transform(np.array([[98,2,13,42,10]])))
        if(new_predictionKKR > new_predictionCSK):
            i='KKR'
        else:
            i='RCB'

    elif((team1=='KKR' and team2=='KXIP') or (team1=='KXIP' and team2=='KKR')):
        new_predictionKKR = lin.predict(sc.transform(np.array([[100,3,13,36,18]])))
        new_predictionKXIP = lin.predict(sc.transform(np.array([[100.5,3.5,13,44,6.5]])))
        if(new_predictionKKR > new_predictionCSK):
            i='KKR'
        else:
            i='KXIP'

    elif((team1=='KKR' and team2=='SRH') or (team1=='SRH' and team2=='KKR')):
        new_predictionKKR = lin.predict(sc.transform(np.array([[100,3,13,36,18]])))
        new_predictionSRH = lin.predict(sc.transform(np.array([[98.5,2,13,39.5,11]])))
        if(new_predictionKKR > new_predictionCSK):
            i='KKR'
        else:
            i='SRH'
            
    if((team1=='CSK' and team2=='MI') or (team1=='MI' and team2=='CSK')):
        new_predictionCSK = lin.predict(sc.transform(np.array([[100,3,13,36,18]])))
        new_predictionMI = lin.predict(sc.transform(np.array([[82,3.5,13,29,6.5]])))
        if(new_predictionCSK > new_predictionMI):
            i='CSK'
        else:
            i='MI'
    elif((team1=='CSK' and team2=='DD') or (team1=='DD' and team2=='CSK')):
        new_predictionCSK = lin.predict(sc.transform(np.array([[101,2,13,42,11]])))
        new_predictionDD = lin.predict(sc.transform(np.array([[101,3,13,39,19]])))
        if(new_predictionCSK > new_predictionDD):
            i='CSK'
        else:
            i='DD'
    elif((team1=='CSK' and team2=='RR') or (team1=='RR' and team2=='CSK')):
        new_predictionCSK = lin.predict(sc.transform(np.array([[101,2,13,42,11]])))
        new_predictionRR = lin.predict(sc.transform(np.array([[92,3,13,33,8]])))
        if(new_predictionCSK > new_predictionRR):
            i='CSK'
        else:
            i='RR'

    elif((team1=='CSK' and team2=='RCB') or (team1=='RCB' and team2=='CSK')):
        new_predictionCSK = lin.predict(sc.transform(np.array([[101,2,13,42,11]])))
        new_predictionRCB = lin.predict(sc.transform(np.array([[98,2,13,42,10]])))
        if(new_predictionKKR > new_predictionCSK):
            i='CSK'
        else:
            i='RCB'

    elif((team1=='CSK' and team2=='KXIP') or (team1=='KXIP' and team2=='CSK')):
        new_predictionCSK = lin.predict(sc.transform(np.array([[101,2,13,42,11]])))
        new_predictionKXIP = lin.predict(sc.transform(np.array([[100.5,3.5,13,44,6.5]])))
        if(new_predictionCSK > new_predictionKXIP):
            i='CSK'
        else:
            i='KXIP'
    elif((team1=='CSK' and team2=='SRH') or (team1=='KXIP' and team2=='SRH')):
        new_predictionCSK = lin.predict(sc.transform(np.array([[101,2,13,42,11]])))
        new_predictionSRH = lin.predict(sc.transform(np.array([[98.5,2,13,39.5,11]])))
        if(new_predictionCSK > new_predictionSRH):
            i='CSK'
        else:
            i='SRH'

    elif((team1=='MI' and team2=='DD') or (team1=='DD' and team2=='MI')):
        new_predictionMI = lin.predict(sc.transform(np.array([[82,3.5,13,29,6.5]])))
        new_predictionDD = lin.predict(sc.transform(np.array([[101,3,13,39,19]])))
        if(new_predictionMI > new_predictionDD):
            i='MI'
        else:
            i='DD'

    elif((team1=='MI' and team2=='RR') or (team1=='RR' and team2=='MI')):
        new_predictionMI = lin.predict(sc.transform(np.array([[82,3.5,13,29,6.5]])))
        new_predictionRR = lin.predict(sc.transform(np.array([[92,3,13,33,8]])))
        if(new_predictionMI > new_predictionRR):
            i='MI'
        else:
            i='RR'

    elif((team1=='MI' and team2=='RCB') or (team1=='RCB' and team2=='MI')):
        new_predictionMI = lin.predict(sc.transform(np.array([[82,3.5,13,29,6.5]])))
        new_predictionRCB = lin.predict(sc.transform(np.array([[98,2,13,42,10]])))
        if(new_predictionMI > new_predictionRCB):
            i='MI'
        else:
            i='RCB'

    elif((team1=='MI' and team2=='KXIP') or (team1=='KXIP' and team2=='MI')):
        new_predictionMI = lin.predict(sc.transform(np.array([[82,3.5,13,29,6.5]])))
        new_predictionKXIP = lin.predict(sc.transform(np.array([[100.5,3.5,13,44,6.5]])))
        if(new_predictionMI > new_predictionKXIP):
            i='MI'
        else:
            i='KXIP'
            
    elif((team1=='MI' and team2=='SRH') or (team1=='SRH' and team2=='MI')):
        new_predictionMI = lin.predict(sc.transform(np.array([[82,3.5,13,29,6.5]])))
        new_predictionSRH = lin.predict(sc.transform(np.array([[98.5,2,13,39.5,11]])))
        if(new_predictionMI > new_predictionSRH):
            i='MI'
        else:
            i='SRH'
   
    elif((team1=='DD' and team2=='RR') or (team1=='RR' and team2=='DD')):
        new_predictionDD = lin.predict(sc.transform(np.array([[101,3,13,39,19]])))
        new_predictionRR = lin.predict(sc.transform(np.array([[92,3,13,33,8]])))
        if(new_predictionDD > new_predictionRR):
            i='DD'
        else:
            i='RR'
    
    elif((team1=='DD' and team2=='RCB') or (team1=='RCB' and team2=='DD')):
        new_predictionDD = lin.predict(sc.transform(np.array([[101,3,13,39,19]])))
        new_predictionRCB = lin.predict(sc.transform(np.array([[98,2,13,42,10]])))
        if(new_predictionMI > new_predictionSRH):
            i='DD'
        else:
            i='RCB'

    elif((team1=='DD' and team2=='KXIP') or (team1=='KXIP' and team2=='DD')):
        new_predictionDD = lin.predict(sc.transform(np.array([[101,3,13,39,19]])))
        new_predictionKXIP = lin.predict(sc.transform(np.array([[100.5,3.5,13,44,6.5]])))
        if(new_predictionDD > new_predictionKXIP):
            i='DD'
        else:
            i='KXIP'
    
    elif((team1=='DD' and team2=='SRH') or (team1=='SRH' and team2=='DD')):
        new_predictionDD = lin.predict(sc.transform(np.array([[101,3,13,39,19]])))
        new_predictionSRH = lin.predict(sc.transform(np.array([[98.5,2,13,39.5,11]])))
        if(new_predictionDD > new_predictionSRH):
            i='DD'
        else:
            i='SRH'
    
    elif((team1=='RR' and team2=='RCB') or (team1=='RCB' and team2=='RR')):
        new_predictionRR = lin.predict(sc.transform(np.array([[92,3,13,33,8]])))
        new_predictionRCB = lin.predict(sc.transform(np.array([[98,2,13,42,10]])))
        if(new_predictionRR > new_predictionRCB):
            i='RR'
        else:
            i='RCB'

    elif((team1=='RR' and team2=='KXIP') or (team1=='KXIP' and team2=='RR')):
        new_predictionRR = lin.predict(sc.transform(np.array([[92,3,13,33,8]])))
        new_predictionKXIP = lin.predict(sc.transform(np.array([[100.5,3.5,13,44,6.5]])))
        if(new_predictionRR > new_predictionKXIP):
            i='RR'
        else:
            i='KXIP'
    
    elif((team1=='RR' and team2=='SRH') or (team1=='SRH' and team2=='RR')):
        new_predictionRR = lin.predict(sc.transform(np.array([[92,3,13,33,8]])))
        new_predictionSRH = lin.predict(sc.transform(np.array([[98.5,2,13,39.5,11]])))
        if(new_predictionRR > new_predictionSRH):
            i='RR'
        else:
            i='SRH'

    elif((team1=='RCB' and team2=='KXIP') or (team1=='KXIP' and team2=='RCB')):
        new_predictionRCB = lin.predict(sc.transform(np.array([[98,2,13,42,10]])))
        new_predictionKXIP = lin.predict(sc.transform(np.array([[100.5,3.5,13,44,6.5]])))
        if(new_predictionRCB > new_predictionKXIP):
            i='RCB'
        else:
            i='KXIP'

    elif((team1=='RCB' and team2=='SRH') or (team1=='SRH' and team2=='RCB')):
        new_predictionRCB = lin.predict(sc.transform(np.array([[98,2,13,42,10]])))
        new_predictionSRH = lin.predict(sc.transform(np.array([[98.5,2,13,39.5,11]])))
        if(new_predictionRCB > new_predictionSRH):
            i='RCB'
        else:
            i='SRH'
   
    elif((team1=='KXIP' and team2=='SRH') or (team1=='SRH' and team2=='KXIP')):
        new_predictionKXIP = lin.predict(sc.transform(np.array([[100.5,3.5,13,44,6.5]])))
        new_predictionSRH = lin.predict(sc.transform(np.array([[98.5,2,13,39.5,11]])))
        if(new_predictionKXIP > new_predictionSRH):
            i='KXIP'
        else:
            i='SRH'

    return render_template('return.html',team1=team1,team2=team2,i=i)


if __name__=="__main__":
    app.run(debug=True)
