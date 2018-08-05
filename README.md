# Photo Album Manager REST API test automation

## Test Env Setup
Setup testing environment install following dependancies:
java 8
python 2.7

pip 18
```
sudo pip install --upgrade pip
```

virtualenv 16
```
sudo pip install virtualenv
```

pytest 3.7.1
```
sudo pip install pytest
```

requests 2.19.1
```
sudo pip install requests
```

## Run API Tests
Use following command to run tests:
```
pytest
```

Use the following command to run tests from specific file;
```
pytest -v ./tests/users-api-tests/get-users-api-tests/test_getUsersApi.py
```

Use the following command to print test message;
```
pytest -v --capture=no 
```

## Report
Use the following command to install html report:

```
sudo pip install pytest-html
```
Use the following command to generate report:

```
pytest --html=report.html
```
