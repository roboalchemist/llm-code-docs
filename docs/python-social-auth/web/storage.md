# Storage

Source: https://python-social-auth.readthedocs.io/en/latest/storage.html

Storage
¶

Different frameworks support different ORMs, Storage solves the different
interfaces moving the common API to mixins classes. These mixins are used on
apps when defining the different models used by 

python-social-auth

.

Social User
¶

This model associates a social account data with a user in the system, it
contains the provider name and user ID (

uid

) which should identify the
social account in the remote provider, plus some extra data (

extra_data

)
which is JSON encoded field with extra information from the provider (usually
avatars and similar).

When implementing this model, it must inherits from 
UserMixin
 and extend the
needed methods:

Username:

@classmethod

def

get_username

(

cls

,

user

):

&quot;&quot;&quot;Return the username for given user&quot;&quot;&quot;

raise

NotImplementedError

(

&#39;Implement in subclass&#39;

)

@classmethod

def

username_max_length

(

cls

):

&quot;&quot;&quot;Return the max length for username&quot;&quot;&quot;

raise

NotImplementedError

(

&#39;Implement in subclass&#39;

)

User model:

@classmethod

def

user_model

(

cls

):

&quot;&quot;&quot;Return the user model&quot;&quot;&quot;

raise

NotImplementedError

(

&#39;Implement in subclass&#39;

)

@classmethod

def

changed

(

cls

,

user

):

&quot;&quot;&quot;The given user instance is ready to be saved&quot;&quot;&quot;

raise

NotImplementedError

(

&#39;Implement in subclass&#39;

)

@classmethod

def

user_exists

(

cls

,

username

):

&quot;&quot;&quot;

    Return True/False if a User instance exists with the given arguments.

    Arguments are directly passed to filter() manager method.

    &quot;&quot;&quot;

raise

NotImplementedError

(

&#39;Implement in subclass&#39;

)

@classmethod

def

create_user

(

cls

,

username

,

email

=

None

):

&quot;&quot;&quot;Create a user with given username and (optional) email&quot;&quot;&quot;

raise

NotImplementedError

(

&#39;Implement in subclass&#39;

)

@classmethod

def

get_user

(

cls

,

pk

):

&quot;&quot;&quot;Return user instance for given id&quot;&quot;&quot;

raise

NotImplementedError

(

&#39;Implement in subclass&#39;

)

Social user:

@classmethod

def

get_social_auth

(

cls

,

provider

,

uid

):

&quot;&quot;&quot;Return UserSocialAuth for given provider and uid&quot;&quot;&quot;

raise

NotImplementedError

(

&#39;Implement in subclass&#39;

)

@classmethod

def

get_social_auth_for_user

(

cls

,

user

):

&quot;&quot;&quot;Return all the UserSocialAuth instances for given user&quot;&quot;&quot;

raise

NotImplementedError

(

&#39;Implement in subclass&#39;

)

@classmethod

def

create_social_auth

(

cls

,

user

,

uid

,

provider

):

&quot;&quot;&quot;Create a UserSocialAuth instance for given user&quot;&quot;&quot;

raise

NotImplementedError

(

&#39;Implement in subclass&#39;

)

Social disconnection:

@classmethod

def

allowed_to_disconnect

(

cls

,

user

,

backend_name

,

association_id

=

None

):

&quot;&quot;&quot;Return if it&#39;s safe to disconnect the social account for the

    given user&quot;&quot;&quot;

raise

NotImplementedError

(

&#39;Implement in subclass&#39;

)

@classmethod

def

disconnect

(

cls

,

name

,

user

,

association_id

=

None

):

&quot;&quot;&quot;Disconnect the social account for the given user&quot;&quot;&quot;

raise

NotImplementedError

(

&#39;Implement in subclass&#39;

)

Nonce
¶

This is a helper class for OpenID mechanism, it stores a one-use number,
shouldn’t be used by the project since it’s for internal use only.

When implementing this model, it must inherit from 
NonceMixin
, and override
the needed methods:

@classmethod

def

use

(

cls

,

server_url

,

timestamp

,

salt

):

&quot;&quot;&quot;Create a Nonce instance&quot;&quot;&quot;

raise

NotImplementedError

(

&#39;Implement in subclass&#39;

)

@classmethod

def

get

(

cls

,

server_url

,

salt

):

&quot;&quot;&quot;Retrieve a Nonce instance&quot;&quot;&quot;

raise

NotImplementedError

(

&#39;Implement in subclass&#39;

)

@classmethod

def

delete

(

cls

,

nonce

):

&quot;&quot;&quot;Delete a Nonce instance&quot;&quot;&quot;

raise

NotImplementedError

(

&#39;Implement in subclass&#39;

)

Association
¶

Another OpenID helper class, it stores basic data to keep the OpenID
association. Like 
Nonce
 this is for internal use only.

When implementing this model, it must inherits from 
AssociationMixin
, and
override the needed methods:

@classmethod

def

store

(

cls

,

server_url

,

association

):

&quot;&quot;&quot;Create an Association instance&quot;&quot;&quot;

raise

NotImplementedError

(

&#39;Implement in subclass&#39;

)

@classmethod

def

get

(

cls

,

*

args

,

**

kwargs

):

&quot;&quot;&quot;Get an Association instance&quot;&quot;&quot;

raise

NotImplementedError

(

&#39;Implement in subclass&#39;

)

@classmethod

def

remove

(

cls

,

ids_to_delete

):

&quot;&quot;&quot;Remove an Association instance&quot;&quot;&quot;

raise

NotImplementedError

(

&#39;Implement in subclass&#39;

)

Validation code
¶

This class is used to keep track of email validations codes following the usual
email validation mechanism of sending an email to the user with a unique code.
This model is used by the partial pipeline 

social_core.pipeline.mail.mail_validation

.
Check the docs at 
Email validation
 in 
pipeline docs
.

When implementing the model for your framework only one method needs to be
overridden:

@classmethod

def

get_code

(

cls

,

code

):

&quot;&quot;&quot;Return the Code instance with the given code value&quot;&quot;&quot;

raise

NotImplementedError

(

&#39;Implement in subclass&#39;

)

Storage interface
¶

There’s a helper class used by strategies to hide the real models names under
a common API, an instance of this class is used by strategies to access the
storage modules.

When implementing this class it must inherits from 
BaseStorage
, add the needed
models references and implement the needed method:

class

StorageImplementation

(

BaseStorage

):

user

=

UserModel

nonce

=

NonceModel

association

=

AssociationModel

code

=

CodeModel

@classmethod

def

is_integrity_error

(

cls

,

exception

):

&quot;&quot;&quot;Check if given exception flags an integrity error in the DB&quot;&quot;&quot;

raise

NotImplementedError

(

&#39;Implement in subclass&#39;

)

SQLAlchemy and Django mixins
¶

Currently there are partial implementations of mixins for 
SQLAlchemy ORM
 and

Django ORM
 with common code used later on current implemented applications.

Note

When using 
SQLAlchemy ORM
 and 

ZopeTransactionExtension

, it’s
recommended to use the 
transaction
 application to handle them.

Models Examples
¶

Check for current implementations for 
Django App
, 
Flask App
, 
Pyramid
App
, and 
Webpy App
 for examples of implementations.