#!/usr/bin/python3

import numpy as np
import pandas as pd
import seaborn as sns
from tensorflow.keras import (
    models,
    optimizers,
    layers
)

import matplotlib.pyplot as plt
import os
from tensorflow.keras.models import model_from_json
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import (
    LabelEncoder
)
from tensorflow.keras.utils import (
    to_categorical
)

def spliting_data():

    """Spliting the data and converting in categorical."""
    data_master = pd.read_csv("data/classification_data.csv")
    y = data_master["quality_product_"]
    X = data_master.drop(["quality_product","quality_product_"], axis= 1)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
    train_data, test_data = X_train.to_numpy(), X_test.to_numpy()

    train_labels = to_categorical(y_train)
    test_labels = to_categorical(y_test)

    return train_data, test_data, train_labels, test_labels


def making_model():

    model = models.Sequential()
    model.add(layers.Dense(64, activation="relu", input_shape=(9,)))
    model.add(layers.Dense(64, activation="relu"))
    model.add(layers.Dense(3, activation="softmax"))
    model.compile(optimizer="rmsprop", loss="categorical_crossentropy", metrics=["accuracy"])

    return model

def main():

    """Calling the data previously splited"""
    train_data, test_data, train_labels. test_labels = spliting_data()
        x_val = train_data[:241]
    partial_x_train = train_data[241:]

    """Calling model"""
    model = making_model()

    y_val = train_labels[:241]
    partial_y_train = train_labels[241:]
    history = model.fit(partial_x_train, partial_y_train,
          epochs=1000,
          batch_size=512, verbose=False,
          validation_data=(x_val, y_val))


    history_dict = history.history
    loss_values = history_dict["loss"]
    val_loss_values = history_dict["val_loss"]

    epoch = range(1, len(loss_values)+1)
    plt.figure(figsize=(12,12))
    plt.plot(epoch, loss_values, "o", label="entrenamiento")
    plt.plot(epoch, val_loss_values, "--", label="validación")
    plt.legend()
    plt.show()

    prediction  = model.evaluate(test_data, test_labels)
    print("{0:.2f}% the accuracy".format(prediction[1]*100))



if __name__ == "__main__":
    main()


