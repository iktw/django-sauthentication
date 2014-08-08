django-sauthentication
======================

Simple **session authentication** for e.g. webb applications.

* Copy **sauthentication.py** to the folder where **settings.py** is located.
* Open root *urls.py* and add the following line:
```
url(r'sauth/', 'myproject.sauthentication.auth', name='auth'),
```
*Change < myproject > to your folder name.*

## Usage
Allowed methods are: POST and GET=?logout=True *(localhost:8000/sauth/?logout=True)*

### E.g. of usage with angularjs to authenticate user:
```
$http.post('/sauth/', {username:'admin', password:'iloveangular'});
```
