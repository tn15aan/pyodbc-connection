# Modules, Libraries and Packages
## --> Specifically pyodbc package

### Libraries
Refer to python standard libraries.
They come standard with python but need to be imported

### Modules
These are python files / like our MonsterStudent that we import into our own program.
We create and import our own modules internally

### Packages
These are external modules, that we need to install and then import them.

These are modules usually written in OOP style, that abstract something

The things that are abstracted include:
- Connection to a service (google maps or google image recognition api, 
price of stocks, price of bitcoin)
- Tools or calculators (Prime number calculator, other complex calculators)

- Front-end-tools - Like JS compiler or other things like scss

- Full fledged frameworks

- Connection to Databases or using HTTP protocols

#### Searching
* google
* look at good git repos
* previous experience
* https://pypi.org/
* -->Analyse if it's contained and how/why you will use it

#### Installing
pip - pythons package manager
(deals with dependencies and installs in virtual environment) - using command line
pycharm - you can just add to interpreter

#### Using
- Import and call your functions
- Follow the documentation


## PYODBC
This package allows us to connect to a DB

#### Cursor
Represents a database cursor which is typically used to manage the context of
a fetch operation

#### Execute
Prepares & executes SQL. The optional parameters may be passed as a sequence
as specified by the DB API, or as individual values

#### Fetchone
Returns the next row or None when no more data is available

#### Fetchall
Returns a list of all remaining rows