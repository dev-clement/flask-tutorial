## Python package

This folder is considered as a Python package because of the __init__.py file that make the folder a
python package. This file init.py will be used to create the app using the create_app factory method.

The init is the constructor related to the package where its name is the name of the folder, in this
case, the folder is called flaskr so the package also. This file init is the entry point once we run
the app like so:

```shell
python -m flask run
```

or
```shell
flask run
```

or
```shell
flask run --app flaskr run
```

The 2 first command can be executed inside of the flaskr folder, and the last one need to be on the parent folder
which is the flask-tutorial folder.