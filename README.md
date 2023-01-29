<!--  -->

To setup perform the following steps
- python -m venv venv
- ./venv/Scripts/Activate.psi
- pip install -r requirements.txt

To start the webserver run the following command
- uvicorn app.main:app --reload

You can run tests by running:
- python ./data/apptest.py

You can visualize appdata by running the Visualize_current_model.ipynb notebook