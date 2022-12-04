# flask-tutorial

## Introduction

Flask is a micro framework developped in Python it is used in order to create small application.
This framework is open source and called as a micro-framework because it is a lightweight one.
Its goal is simple, keeping a simple kernel but extensible... It also doesn't require any particular
tools, nor libraries. It doesn't have any databases abstraction layer, form validation nor any other
components, still some pre-existing libraries are used inside of a Flask application (like sqlalchemy for the
database) meaning that flask doesn't have this kind of third-party libraries, but it use some existing ones

## Application

This application called "Flaskr" has been done in order to understant how Flask works under the hood
and also how a Flask application is made. It is made through a Python 3.10, version.

The flaskr application is just one package called flaskr containing a package constructor `__init__.py`, also all that is
needed to handle the blog application the `static` folder containing all the css and js file, the `templates` folder containing
all the view using the jinja2 extension and the `schema.sql` used to create the database.

### Third-party: database

The database of the application is sqlite3, however we aren't making use of it directly, instead we are using an Object Relationnal Mapper
called `sqlalchemy`, the only moment we are making use of sqlite3 directly is when we're creating the database through the
`db.py` file.

### Third-party: click

During the database creation, we are using the `@click` command decorator, that will be used in order to create command
that will be used when we are running the application like so:

```sh
flask --app flaskr --debug run
```

This command will run the flask application using the debug mode. If we want to make use of a `@click` command, we can do
something like this:

```sh
flask --app flaskr init-db
```

In this command, the click will be:`@click.command('init-db')`, this click command will run the created init-db command
which is at the end a function in the python module `db`

### Creation of a decorator

Inside of some website or web application, some pages can be displayed to the user if and only if the user is logged in
to the website, this is done in Flask by making use of the decorator function. This decorator is created using the `functools`
package. The method used as a decorator is a higher-order function, meaning that this function will contain another function
inside it to make some processing of the parameter injected into it.

In order to create a decorator, we have to create the higher-order function like so:
```python
def user_logged_in(view):
    ...
```

The method is taking a view as parameter and will contain a method instead of the ... to do some processing to the
view passed as parameter like so:

```python
def user_logged_in(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
```

In this scenario, the `wrapped_view` is the function being inside of the higher order called `user_logged_in` meaning that
the `wrapped_view` cannot be called, meaning that it would be called by the `user_logged_in` body and the `user_logged_in`
allows the processing being made correctly.

```python
def user_logged_in(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))
        return view(**kwargs)
    return wrapped_view
```
In this application, this method will check if the user is inside the global context of the request,
if that is not the case, the method return a login page to authenticate to the user. Otherwise it return
the view by passing the keyword arguments into it ```python **kwargs```
