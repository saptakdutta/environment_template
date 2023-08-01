# Overview
This is a template for all environment.yml files that will be used in my future projects. 

The goal of this template is to standardize how code is written, checked and replicated. This will be done by having a consistent virtual environment, the use of type checking through mypy and formatting stadardization using black. 

The standardized environment template will also have REPL support through ipykernel and pretty printing loops with tqdm which all future projects will benefit from. 

# Included goodies with this conda env template
## Black
Formattiong using the PEP-8 standard. To run on a python file (e.g., main.py), simply cd to the existing directory and run the following:

> black main.py

Black will automatically clean up your code to a standardized format

## MyPy
Optional type checking for functions which help in debugging

## TQDM
Not knowing the estimated time for a loop to end on a computation is annoying. TQDM allows you to get useful iteration updates and completion estimates

## Ipykernel
Having a functioning REPL is quite useful in data exploration (e.g., jupyter), and this allows for notebooks to be run whenever this virtual environment is used

## Tabulate
Not all code or projects use a REPL. In situations where only a terminal output is required, tabulate allows for the pretty printing of dataframes to the terminal, making them a lot more readable.
