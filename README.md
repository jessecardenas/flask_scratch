# flask_scratch

Basic boilerplate and template to get flask app running

## to set up
 edit config.py  
 python3 -m venv venv  
 . venv/bin/activate  
 pip install -r requirements.txt  
 python -m scripts.init_db
 python -m scripts.create_admin

## to run
 venv/bin/python3 app.py  

## features:
 static files  
 templates  
 session based auth  
 test script  
 config  
 basic flask app  

## to do:
 apache setup  
 uwsgi setup  
 sqlite auth backend
 password resets
 sqlite user management
