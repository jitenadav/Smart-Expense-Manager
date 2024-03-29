from pandas import read_csv
from matplotlib import pyplot
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.arima.model import ARIMAResults
from sklearn.metrics import mean_squared_error
from math import sqrt
import numpy
import logging

# create a differenced series
def difference(dataset, interval=1):
	diff = list()
	for i in range(interval, len(dataset)):
		value = dataset[i] - dataset[i - interval]
		diff.append(value)
	return diff

# invert differenced value
def inverse_difference(history, yhat, interval=1):
	return yhat + history[-interval]

# load and prepare datasets
def predict():
	dataset = read_csv('SmtExpMngr/models/train_data.csv', header=None, index_col=0, parse_dates=True, squeeze=True)
	X = dataset.values.astype('float32')
	history = [x for x in X]
	months_in_year = 1
	validation = read_csv('validation.csv', header=None, index_col=0, parse_dates=True, squeeze=True)
	y = validation.values.astype('float32')
	# load model
	model_fit = ARIMAResults.load('/home/termi/beproject/SmtExpMngr/models/model.pkl')
	bias = numpy.load('/home/termi/beproject/SmtExpMngr/models/model_bias.npy')
	# make first prediction
	predictions = list()
	yhat = float(model_fit.forecast())
	yhat = bias + inverse_difference(history, yhat, months_in_year)
	predictions.append(yhat)
	history.append(y[0])
	return yhat
# rolling forecasts
# for i in range(1, len(y)):
# 	# difference data
# 	months_in_year = 12
# 	diff = difference(history, months_in_year)
# 	# predict
# 	model = ARIMA(diff, order=(0,0,1))
# 	model_fit = model.fit()
# 	yhat = model_fit.forecast()
# 	yhat = bias + inverse_difference(history, yhat, months_in_year)
# 	predictions.append(yhat)
# 	# observation
# 	obs = y[i]
# 	history.append(obs)
# 	print('>Predicted=%.3f, Expected=%.3f' % (yhat, obs))
# # report performance
# rmse = sqrt(mean_squared_error(y, predictions))
# print('RMSE: %.3f' % rmse)
