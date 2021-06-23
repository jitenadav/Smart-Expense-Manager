# save finalized model
from pandas import read_csv
from statsmodels.tsa.arima.model import ARIMA
import numpy

# create a differenced series
def difference(dataset, interval=1):
	diff = list()
	for i in range(interval, len(dataset)):
		value = dataset[i] - dataset[i - interval]
		diff.append(value)
	return diff

def train():
	# load data
	series = read_csv('SmtExpMngr/models/train_data.csv', header=None, index_col=0, parse_dates=True, squeeze=True)
	# prepare data
	X = series.values
	X = X.astype('float32')
	# difference data
	months_in_year = 12
	diff = difference(X)
	# fit model
	model = ARIMA(diff, order=(0,0,1))
	model_fit = model.fit()
	# bias constant, could be calculated from in-sample mean residual
	bias = 165.904728
	# save model
	model_fit.save('SmtExpMngr/models/model.pkl')
	numpy.save('SmtExpMngr/models/model_bias.npy', [bias])
	print("Tarined")
