# Logging_Out

Source: https://python-social-auth.readthedocs.io/en/latest/logging_out.html

Disconnect and Logging Out
¶

It’s a common misconception that the 

disconnect

 action is the same as
logging the user out, but this is not the case.

Disconnect

 is the way that your users can ask your project to “forget about
my account”. This implies removing the 

UserSocialAuth

 instance that was
created, this also implies that the user won’t be able to login back into your
site with the social account. Instead the action will be a signup, a new user
instance will be created, not related to the previous one.

Logging out is just a way to say “forget my current session”, and usually
implies removing cookies, invalidating a session hash, etc. The many frameworks
have their own ways to logout an account (Django has 

django.contrib.auth.logout

),

flask-login

 has it’s own way too with 
logout_user()
.

Since disconnecting a social account means that the user won’t be able to log
back in with that social provider into the same user, python-social-auth will
check that the user account is in a valid state for disconnection (it has at
least one more social account associated, or a password, etc). This behavior
can be overridden by changing the 
Disconnection Pipeline
.