# Backends/Readability

Source: https://python-social-auth.readthedocs.io/en/latest/backends/readability.html

Readability
¶

Readability works similarly to Twitter, in that you’ll need a 

Consumer

Key

and 

Consumer

Secret

.  These can be obtained in the 

Connections

 section
of your 

Account

 page.

Fill the 
Consumer Key
 and 
Consumer Secret
 values in your settings:

SOCIAL_AUTH_READABILITY_KEY

=

&#39;&#39;

SOCIAL_AUTH_READABILITY_SECRET

=

&#39;&#39;

That’s it! By default you’ll get back:

username

first_name

last_name

with EXTRA_DATA, you can get:

date_joined

kindle_email_address

avatar_url

email_into_address