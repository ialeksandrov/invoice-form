# invoice-form
Short description:
This is invoicing form which generates PDF and docx invoice files.

### How to run it on your computer:
It is a good idea to create a virtual environment on which you can safely install the required packages.

### To Create virtual environment execute:
Example:
virtuanenv invoice 

### Activate this environment:
. invoice/bin/activate // for example (or replace the . with "source" both ways are valid).

### Install the required packages:
pip install -r requirements.txt

### After this step you have completely ready for use environment. To run the application go in the directory where the manage.py file is located and type:

python manage.py runserver

This command will start the development server and you will be able to fill the simple form ( with not very nice front-end ) and generate some simple invoice document.
