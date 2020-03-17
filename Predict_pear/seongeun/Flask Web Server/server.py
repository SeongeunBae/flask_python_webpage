# -*- coding: utf-8 -*-
from flask import Flask, render_template, request

# 0. 사용할 패키지 불러오기
import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense, LSTM, Dropout
import matplotlib.pyplot as plt
# %matplotlib inline
from keras.callbacks import EarlyStopping
from math import sqrt

app = Flask(__name__)






@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST':
        # 파라미터를 전달 받습니다.
        mean1 = float(request.form['mean1'])
        prep1 = float(request.form['prep1'])
        humidity1 = float(request.form['humidity1'])
        whole_price1 = float(request.form['whole_price1'])
        retail_price1 = float(request.form['retail_price1'])

        mean2 = float(request.form['mean2'])
        prep2 = float(request.form['prep2'])
        humidity2 = float(request.form['humidity2'])
        whole_price2 = float(request.form['whole_price2'])
        retail_price2 = float(request.form['retail_price2'])

        mean3 = float(request.form['mean3'])
        prep3 = float(request.form['prep3'])
        humidity3 = float(request.form['humidity3'])
        whole_price3 = float(request.form['whole_price3'])
        retail_price3 = float(request.form['retail_price3'])

        # 배추 가격 변수를 선언합니다.
        price = 0
        #2. 모델 불러오기
        from keras.models import load_model
        model = load_model('model.h5')
        
        # 입력된 파라미터를 배열 형태로 준비합니다.
        x_test = np.array([[[mean1,prep1,humidity1,whole_price1,retail_price1],
              [mean2,prep2,humidity2,whole_price2,retail_price2],
              [mean3,prep3,humidity3,whole_price3,retail_price3]]])  


        # 입력 값을 토대로 예측 값을 찾아냅니다.
        y_predict = model.predict(x_test)

        # 결과 배추 가격을 저장합니다.
        price = y_predict[0][0]

        return render_template('predict.html', price=price)

@app.route("/predict/")
def predict():
    return render_template('predict.html')

@app.route("/about/")
def about():
    return render_template('index.html')

if __name__ == '__main__':
   app.run(debug = True)
