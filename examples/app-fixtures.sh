#!/bin/sh

# quit on errors:
set -o errexit

# quit on unbound symbols:
set -o nounset

DIR=`dirname "$0"`

cd $DIR
export FLASK_APP=app.py

## Load fixtures

# create users
flask users create info@inveniosoftware.org -a --password 123456
flask users create reader@inveniosoftware.org -a --password 123456
flask users create editor@inveniosoftware.org -a --password 123456
flask users create admin@inveniosoftware.org -a --password 123456

# create admin role and add the role to a user
flask roles create admin
flask roles add info@inveniosoftware.org admin
flask roles add admin@inveniosoftware.org admin

# assign some allowed actions to this users
flask access allow open -e editor@inveniosoftware.org
flask access deny open -e info@inveniosoftware.org
flask access allow read -e reader@inveniosoftware.org
flask access allow open -r admin
flask access allow read -r admin
flask access allow admin-access -r admin
flask access allow superuser-access -r admin
