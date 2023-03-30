<!--  -->
## FASTAPI ML Backend
A basic FASTAPI ML backend performing clustering on user click information. Clustering method used is DBSCAN
![alt text](https://github.com/AashayBhupendraDoshi/Python_FASTAPI_ML_test/blob/main/block__diagrm.png)
# Setup
To setup perform the following steps
```
python -m venv venv
./venv/Scripts/Activate.psi
pip install -r requirements.txt
```

To start the webserver run the following command
```
uvicorn app.main:app --reload
```

You can run tests by running:
```
python ./data/apptest.py
```
You can visualize appdata by running the ```./data/Visualize_current_model.ipynb``` notebook
