# Welcome to Secure Code Game Season-1/Level-3!

# You know how to play by now, good luck!

import os
from flask import Flask, request

### Unrelated to the exercise -- Starts here -- Please ignore
app = Flask(__name__)
@app.route("/")
def source():
    TaxPayer('foo', 'bar').get_tax_form_attachment(request.args["input"])
    TaxPayer('foo', 'bar').get_prof_picture(request.args["input"])
### Unrelated to the exercise -- Ends here -- Please ignore

class TaxPayer:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.prof_picture = None
        self.tax_form_attachment = None

    def sanitize_path(self, path):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        full_path = os.path.realpath(os.path.join(base_dir, path))
        if not full_path.startswith(base_dir):
            return None
        return full_path

    # returns the path of an optional profile picture that users can set
    def get_prof_picture(self, path=None):
        # setting a profile picture is optional
        if not path:
            return None

        # defends against path traversal attacks
        full_path = self.sanitize_path(path)
        if full_path is None:
            return None

        try:
            with open(full_path, 'rb') as pic:
                picture = bytearray(pic.read())
            return full_path
        except (FileNotFoundError, IOError):
            return None
    # returns the path of an attached tax form that every user should submit
    def get_tax_form_attachment(self, path=None):
        if not path:
            raise Exception("Error: Tax form is required for all users")

        full_path = self.sanitize_path(path)
        if full_path is None:
            return None

        try:
            with open(full_path, 'rb') as form:
                tax_data = bytearray(form.read())
            return full_path
        except (FileNotFoundError, IOError):
            return None
