# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import datetime

import random

import lib.requests
from flask import Flask, render_template, json, request, jsonify, abort, make_response, redirect, flash, session, \
    url_for
from lib.flask_login import (
    LoginManager,
    logout_user,
    login_user,
    current_user,
    login_required
)
import logging
import datetime
# [START gae_python38_datastore_store_and_fetch_times]
# [START gae_python3_datastore_store_and_fetch_times]

from lib.google.cloud import ndb
from models import User

# [END gae_python3_datastore_store_and_fetch_times]
# [END gae_python38_datastore_store_and_fetch_times]
app = Flask(__name__)
app.secret_key = 'simcloud6666777'
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    ndb_client = ndb.Client()
    with ndb_client.context():
        return User.get_by_id(int(user_id))


@app.route('/')
def root():
    return redirect("/index")


# [END gae_python3_datastore_render_times]
# [END gae_python38_datastore_render_times]


@app.route("/index")
def index():
    print("test")
    return render_template('index.html')


@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        client = ndb.Client()
        with client.context():
            ## TODO: add validation - check for duplicates, check if confirm password matches
            user_record = User(firstname=request.form.get("firstname"),
                               surname=request.form.get("surname"),
                               cell_number=request.form.get("cell_number"),
                               id_number=request.form.get("id_number"),
                               email_address=request.form.get("email_address"),
                               business_address=request.form.get("business_address"),
                               business_registration_number=request.form.get("business_registration_number"),
                               vat_number=request.form.get("vat_number"),
                               address=request.form.get("address"),
                               password=request.form.get("password"),
                               confirm_password=request.form.get("confirm_password"))
            user_record.put()  ## save user to data to database

    return render_template('register.html')


@app.route("/logout")
def logout():
    ## logout_user()
    return redirect("/index")


@app.route("/dashboard", methods=['GET', 'POST'])
def dashboard():
    return render_template("dashboard.html")


@app.route("/login", methods=['GET', 'POST'])
def login():
    ## TODO: add check if user already logged in
    ##   if current_user.is_authenticated:
    ## user already logged in
    ##    return redirect("/index")
    ## to update indexes: gcloud datastore indexes create path/to/index.yaml
    if request.method == 'POST':

        ndb_client = ndb.Client()
        with ndb_client.context():

            cell_no = request.form.get("cellNumberInput")
            password = request.form.get("passwordInput")

            records = User.query().fetch()
            user = None
            for r in records:
                if r.cell_number == cell_no:
                    user = r

            if user is not None:
                ## user found in database
                ## check if password matches
                if password == user.password:
                    # password matches now login user
                    ## login_user(user)
                    return redirect("/dashboard")

    ##cellNumberInput
    ## user = User().get_obj('username', 'komla')
    return render_template("login.html")


@app.route("/pricing")
def pricing():
    return render_template('pricing.html')


@app.route("/terms")
def terms():
    return render_template('terms-and-conditions.html')


if __name__ == "__main__":
    app.run(debug=True)
