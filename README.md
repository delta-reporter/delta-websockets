# Delta Reporter Websockets Service

This service is intended to send real time events into Delta Reporter

## Local development

To develop locally, create a virtual environment and install your dependencies:

```
pip install virtualenv
virtualenv venv --python=python3
source venv/bin/activate
pip install -r requirements.txt
pre-commit install
```

Then, run your app:

```
python app.py
 * Running on http://localhost:8080/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
```
