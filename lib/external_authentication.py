## $Id$
## CDSware Access Control Config in mod_python.

## This file is part of the CERN Document Server Software (CDSware).
## Copyright (C) 2002, 2003, 2004, 2005 CERN.
##
## The CDSware is free software; you can redistribute it and/or
## modify it under the terms of the GNU General Public License as
## published by the Free Software Foundation; either version 2 of the
## License, or (at your option) any later version.
##
## The CDSware is distributed in the hope that it will be useful, but
## WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
## General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with CDSware; if not, write to the Free Software Foundation, Inc.,
## 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.
#include "config.wml"
#include "configbis.wml"
import httplib
import urllib
import re

class external_auth_nice:
    users = {}
    name = ""

    def __init__(self):
        #Initialize stuff here
        pass

    def auth_user(self, username, password):
        #login user here

        params = urllib.urlencode({'Username': username, 'Password': password})
        headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
        conn = httplib.HTTPSConnection("winservices.web.cern.ch") 
        conn.request("POST", "/WinServices/Authentication/CDS/default.asp", params, headers)
        response = conn.getresponse()
        data = response.read()
        conn.close()
        m = re.search('<CCID>\d+</CCID>', data)
        if m:
            m = m.group()
            CCID = int(re.search('\d+',m).group())
            if CCID > 0:
                m = re.search('<EMAIL>.*?</EMAIL>', data)
                if m:
                    email = m.group()
                    email = email.replace('<EMAIL>', '')   
                    email = email.replace('</EMAIL>', '')  
                    return email 
        return None

class external_auth_template:
    def __init__(self):
        #Initialize stuff here
        pass

    def auth_user(self, username, password):
        #login user here
        return email
        return None