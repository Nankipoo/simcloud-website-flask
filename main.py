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

from flask import Flask, render_template, request, redirect

from lib.flask_login import (
    LoginManager,
    logout_user,
    login_user,
    current_user,
    login_required
)



import datetime
# [START gae_python38_datastore_store_and_fetch_times]
# [START gae_python3_datastore_store_and_fetch_times]
from google.cloud import datastore
datastore_client = datastore.Client()
from lib.google.cloud import ndb
from models import User
# [END gae_python3_datastore_store_and_fetch_times]
# [END gae_python38_datastore_store_and_fetch_times]
app = Flask(__name__)
app.secret_key = 'simcloud6666'
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

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




@login_manager.user_loader
def load_user(user_id):
    client = ndb.Client()
    with client.context():
        return User.get_by_id(int(user_id))

@app.route("/register", methods=['GET', 'POST'])
def register():

    if request.method == 'POST':
        print(request.form.to_dict())
        # The kind for the new entity
        client = ndb.Client()
        with client.context():
            contact1 = User(email_address=request.form.get("email_address"),
                               cell_number=request.form.get("cell_number"),
                               password=request.form.get("password"))
            contact1.put() ## save user to data to database


    return render_template('register.html')

@app.route("/logout")
def logout():
    logout_user()
    return redirect("/index")

@app.route("/dashboard", methods=['GET', 'POST'])
def dashboard():
    return render_template("dashboard.html")

@app.route("/login", methods=['GET', 'POST'])
def login():

    if current_user.is_authenticated:
        return redirect("/index")
    ## to update indexes: gcloud datastore indexes create path/to/index.yaml
    if request.method == 'POST':

        client = ndb.Client()
        with client.context():

            print(request.form.to_dict())
            cell_no = request.form.get("cellNumberInput")
            password = request.form.get("passwordInput")


            records = User.query().fetch()
            user = None
            for r in records:
                if r.cell_number == cell_no:
                    user = r

            if user is not None:
                login_user(user)
                print("logging in user")
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


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.

    # Flask's development server will automatically serve static files in
    # the "static" directory. See:
    # http://flask.pocoo.org/docs/1.0/quickstart/#static-files. Once deployed,
    # App Engine itself will serve those files as configured in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
