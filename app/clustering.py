import os
import pickle
import numpy as np
import scipy as sp
from sklearn.utils import shuffle
from sklearn.cluster import DBSCAN
from . import models
from .database import engine, get_db

FILENAME = "./trained_models/cluster_model.pkl"


def train(db):
    # db: database session object
    #  
    # No classification below 40 points
    # eps=0.4 for points between 40-500
    # eps=0.28 for points between 500-5000
    # eps=0.19 for points between 5000-
    # Train every time number of points double
    

    X = db.query(models.clicks).all()
    x = []
    y = []
    # id = []
    for i in X:
        x.append(i.x)
        y.append(i.y)
        # id.append(i.cluster_id)
    X = np.array([x,y]).T
    if X.shape[0]>40:
        # Variable to see if the model is trained/re-trained or not
        trained = 0
        try:
            # Does not exist
            clustering = pickle.load(open(FILENAME, 'rb'))
            y_pred = clustering.labels_
            # print("IN TRY ", X.shape[0], len(y_pred))
            if X.shape[0]>2*len(y_pred):
                print(X.shape[0])
                trained=1
                print("Training New Model")
                if 40<X.shape[0]<500:
                    clustering = DBSCAN(eps=0.04, min_samples=3).fit(X)
                elif 500<X.shape[0]<5000:
                    clustering = DBSCAN(eps=0.028, min_samples=5).fit(X)
                else:
                    clustering = DBSCAN(eps=0.019, min_samples=5).fit(X)
        except FileNotFoundError:
            print("First Clustering Model")
            clustering = DBSCAN(eps=0.04, min_samples=3).fit(X)
            trained=1
        finally:
            # Save model and labels only if model is trained/re-trained
            if trained==1:
                # Save values
                pickle.dump(clustering, open(FILENAME, 'wb'))
                print("Saving Trained  Model")
                # Update Labels
                y_pred = clustering.labels_
                for i in range(len(y_pred)):
                    rquery = db.query(models.clicks).filter(models.clicks.id == i+1)
                    rquery.update({'cluster_id': int(y_pred[i])}, synchronize_session=False)
                # Commit values to database
                db.commit()
    

        
    return



def dbscan_predict(dbscan_model, X_new, metric=sp.spatial.distance.euclidean):
    # Result is noise by default
    y_new = np.ones(shape=len(X_new), dtype=int)*-1 

    # Iterate all input samples for a label
    for j, x_new in enumerate(X_new):
        # Find a core sample closer than EPS
        for i, x_core in enumerate(dbscan_model.components_): 
            if metric(x_new, x_core) < dbscan_model.eps:
                # Assign label of x_core to x_new
                y_new[j] = dbscan_model.labels_[dbscan_model.core_sample_indices_[i]]
                break

    return y_new



def predict(x):
    # Predicts single inputs, not batches
    try:
        # Does not exist
        clustering = pickle.load(open(FILENAME, 'rb'))
        y = dbscan_predict(clustering, np.array([x]))
        y = y[0]
        # print('FOUND FILE')
    except:
        y = -1
    
    return y


# print(predict([0.4,0.5]))
# print(dbscan_predict(clustering, np.array([[0.5,0.6]])))