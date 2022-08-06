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

from flask import Flask, render_template, request



import datetime
# [START gae_python38_datastore_store_and_fetch_times]
# [START gae_python3_datastore_store_and_fetch_times]
from google.cloud import datastore
datastore_client = datastore.Client()
from models import User
# [END gae_python3_datastore_store_and_fetch_times]
# [END gae_python38_datastore_store_and_fetch_times]
app = Flask(__name__)

# [START gae_python38_datastore_store_and_fetch_times]
# [START gae_python3_datastore_store_and_fetch_times]


def store_time(dt):
    entity = datastore.Entity(key=datastore_client.key('visit'))
    entity.update({
        'timestamp': dt
    })

    datastore_client.put(entity)


def fetch_times(limit):
    query = datastore_client.query(kind='visit')
    query.order = ['-timestamp']

    times = query.fetch(limit=limit)

    return times
# [END gae_python3_datastore_store_and_fetch_times]
# [END gae_python38_datastore_store_and_fetch_times]

# [START gae_python38_datastore_render_times]
# [START gae_python3_datastore_render_times]ggg frank is ger

@app.route('/')
def root():

    # Store the current access time in Datastore.
    store_time(datetime.datetime.now(tz=datetime.timezone.utc))

    # Fetch the most recent 10 access times from Datastore.
    times = fetch_times(10)

    return render_template(
        'index.html', times=times)
# [END gae_python3_datastore_render_times]
# [END gae_python38_datastore_render_times]


@app.route("/index")
def index():

    return render_template('index.html')

@app.route("/register", methods=['GET', 'POST'])
def register():

    if request.method == 'POST':
        print(request.form.to_dict())
        
        # The kind for the new entity
        kind = "User"

        n = random.randint(0, 10000)

        # The name/ID for the new entity
        user_id = "username" + str(n)

        # The Cloud Datastore key for the new entity
        user_key = datastore_client.key(kind, user_id)

        # Prepares the new entity
        user = datastore.Entity(key=user_key)

        user["firstname"] = request.form.get("firstname")
        user["surname"] = request.form.get("surname")
        user["cell_number"] = request.form.get("cell_number")
        user["id_number"] = request.form.get("id_number")
        user["email_address"] = request.form.get("email_address")
        user["business_name"] = request.form.get("business_name")
        user["business_registration_number"] = request.form.get(
            "business_registration_number")
        user["vat_number"] = request.form.get("vat_number")
        user["address"] = request.form.get("address")
        user["password"] = request.form.get("password")
        user["confirm_password"] = request.form.get("confirm_password")

        # Saves the entity
        datastore_client.put(user)

    return render_template('register.html')


@app.route("/register2", methods=['GET', 'POST'])
def register2():
    from datastore_entity import DatastoreEntity, EntityValue
    if request.method == 'POST':
        print(request.form.to_dict())
        # The kind for the new entity
        user = User()
        user.cell_no = request.form.get("cell_number")
        user.email = request.form.get("email_address")  # assign attribute value as a type of EntityValue
        user.password = request.form.get("password")
        user.save()
    return render_template('register.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        print(request.form.to_dict())
        cell_no = request.form.get("cellNumberInput")
        password = request.form.get("passwordInput")
        user = User().get_obj('cell_no', cell_no)
        print(user)


        ##cellNumberInput
       ## user = User().get_obj('username', 'komla')
    return render_template("login.html")


@app.route("/pricing")
def pricing():
    return render_template('pricing.html')


@app.route("/terms")
def terms():
    return render_template('terms-and-conditions.html')


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.

    # Flask's development server will automatically serve static files in
    # the "static" directory. See:
    # http://flask.pocoo.org/docs/1.0/quickstart/#static-files. Once deployed,
    # App Engine itself will serve those files as configured in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
