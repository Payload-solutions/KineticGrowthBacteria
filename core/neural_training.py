#!/usr/bin/python3

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline
from tensorflow.keras import (
    models,
    layers,
    optimizers
)
from sklearn.model_selection import train_test_split
from tensorflow.keras.utils import to_categorical
from pprint import pprint
import time



data_master = pd.read_csv("data/data_regression_set.csv")
y_strep = data_master["streptococcus_initial_strain_cfu_ml"]


X = data_master.drop(["streptococcus_initial_strain_cfu_ml",
                        "lactobacillus_initial_strain_cfu_ml",
                        "quality_product",
                        "ideal_temperature_c",
                        "lactobacillus_final_cfu_ml",
                        "streptococcus_final_cfu_ml"], axis=1)

X_train, X_test, y_train, y_test = train_test_split(X, y_strep, test_size=0.3, random_state=42)

# Reshaping data
train_data, test_data = X_train.to_numpy(), X_test.to_numpy()

# Normalizing train data
mean = train_data.mean(axis = 0)
train_data = train_data - mean
standard = train_data.std(axis = 0)
train_data = train_data / standard

# Normalizing test data
test_data = test_data - mean
test_data = test_data / standard



def defining_model(input_data: int, learning_rate_val: float):
    model = models.Sequential()
    model.add(layers.Dense(64, activation = "relu", input_shape = (input_data,)))
    # model.add(layers.Dense(16, activation = "relu"))
    model.add(layers.Dense(64, activation = "relu"))
    # model.add(layers.Dense(4, activation = "relu"))
    # model.add(layers.Dense(4, activation = "relu"))
    # model.add(layers.Dense(4, activation = "relu"))
    # as this result is a regression; is a continuous number, that's lineal
    # doesn't need an activation layer
    model.add(layers.Dense(1))

    model.compile(optimizer=optimizers.RMSprop(learning_rate= learning_rate_val),
        loss="mse",
        metrics=["mae"])

    # return model


    # model = defining_model(5, 0,00023)
    # model.fit(train_data, y_train, 
    #           epochs=120, batch_size = 16,
    #           validation_data=())
    k_fold_validations = 4

    num_val_samples = len(train_data) // k_fold_validations
    num_epochs = 120
    all_histories = list()

    for i in range(k_fold_validations):
        print("Fold: %s"%i)
        val_data = train_data[i*num_val_samples: (i+1)*num_val_samples]
        val_target = y_train[i*num_val_samples: (i+1)*num_val_samples]

        partial_train_data = np.concatenate(
            [train_data[:i * num_val_samples],
            train_data[(i+1)*num_val_samples:]
            ], axis = 0)

        partial_train_target = np.concatenate(
            [y_train[:i * num_val_samples],
            y_train[(i+1)*num_val_samples:]
            ], axis = 0)

        # model = defining_model(5, 0.0001)
        # model = defining_model(5, 0.23) # that can be the right value
        # model = defining_model(4, 0.0155)
        history = model.fit(partial_train_data, partial_train_target,
                epochs=num_epochs,
                batch_size=16,
                validation_data=(val_data, val_target),
                verbose=False)

        all_histories.append(history.history["val_mae"])

    return model, all_histories



def main():
    model, all_histories = defining_model(4, 0.0155)
    time.sleep(0.005)
    all_mae_avg = pd.DataFrame(all_histories).mean(axis = 0)

    plt.figure(figsize=(12,12))
    plt.plot(range(1, len(all_mae_avg)+1), all_mae_avg)
    plt.title("Medición del error medio absoluto")
    plt.show()

if __name__ == "__main__":
    main()





