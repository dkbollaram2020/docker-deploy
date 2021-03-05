import pickle
import json
import numpy as np

__data_columns = None
__model = None

def get_estimated_price(resident_type,bedrooms,bathrooms,square_footage):
    try:
        loc_index = __data_columns.index(resident_type.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = bedrooms
    x[1] = bathrooms
    x[2] = square_footage
    if loc_index>=0:
        x[loc_index] = 1

    return round(__model.predict([x])[0] * 1000, 2)


def load_saved_artifacts():
    print("loading saved artifacts...")
    global  __data_columns
    with open("./artifacts/columns.json", "r") as f:
        __data_columns = json.load(f)["data_columns"]

    global __model
    if __model is None:
        with open('./artifacts/rental_comp_arizona_model.pickle', 'rb') as f:
            __model = pickle.load(f)
    print("Done loading saved artifacts...")


if __name__ == '__main__':
    load_saved_artifacts()