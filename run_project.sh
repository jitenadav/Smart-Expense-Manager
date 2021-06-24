#!/bin/bash

source flaskenv/bin/activate

cd ../

export FLASK_APP=SmtExpMngr

export FLASK_ENV=development

flask run
