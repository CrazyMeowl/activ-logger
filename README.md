# _ActivLogger project_


## Note to self
To init the venv
```
python -m venv activ-logger
```
- Run this in administrator mode in order to use Script\activate
```sh
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```
```
Script\activate
```
## Requirement
- Python 3.8+

## Installation
#### For dev env
```
pip install "fastapi[all]"
```



## Running Backend
#### For dev env
```
uvicorn main:app --reload
```

#### For deployment
```
uvicorn main:app
```
