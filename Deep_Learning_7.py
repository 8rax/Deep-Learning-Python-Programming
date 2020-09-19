import tensorflow as tf 
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, LSTM

#Mnist data - the numbers
mnist=tf.keras.datasets.mnist

#Unpack the data
(x_train, y_train),(x_test, y_test) = mnist.load_data()

print(x_train.shape)
print(x_train[0].shape)
