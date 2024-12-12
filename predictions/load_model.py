import pickle

def get_model():
    model = pickle.load('heart_model.pkl')
    return model