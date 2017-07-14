============
API Security
============

A password will be sent to the email IDs of the users/clients. In the login section of the API, they can use
their email ID as the username and the password provided in the email to generate an authorization key(which
will be randomly generated each time the user loads the API page and enters his/her login details).

When they click on 'Try it out', they will be asked for their authorization key. If it matches the
authorization key generated in the login section, the post/get request is executed.

-------
Summary
-------
