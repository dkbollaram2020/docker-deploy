import pickle
import json
import numpy as np

__model = None

def get_estimated_price(sqft,bhk,bath):

    x = np.zeros(3)
    x[0] = sqft
    x[1] = bath
    x[2] = bhk

    return round(__model.predict([x])[0],2)


def load_saved_artifacts():
    print("loading saved artifacts...start")

    global __model
    if __model is None:
        with open('./artifacts/home_prices_model.pickle', 'rb') as f:
            __model = pickle.load(f)
    print("loading saved artifacts...done")


if __name__ == '__main__':
    load_saved_artifacts()
    print(get_estimated_price(1000, 3, 3))
    print(get_estimated_price(1000, 2, 2))