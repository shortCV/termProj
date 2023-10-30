# termProj
https://github.com/shortCV/termProj
- pip install django
- django-admin startproject testData
- cd testData
- python [manage.py](http://manage.py/) startapp testApp
- add ‘testApp’ to INSTALLED_APP in testData/setting.py

- set up server:
   <img width="642" alt="Screenshot 2023-10-29 at 10 24 31 PM" src="https://github.com/shortCV/termProj/assets/82280581/641c6cc8-600f-42dd-8862-4d0c6dc619d3">

    
 
- install these pips:
  pip pillow
  pip install django-crispy-forms
  pip install crispy-bootstrap4
  pip install django-bootstrap4
  install flask
- python [manage.py](http://manage.py/) makemigrations testApp
- python [manage.py](http://manage.py/) sqlmigrate testapp 0001
- python [manage.py](http://manage.py/) migrate

