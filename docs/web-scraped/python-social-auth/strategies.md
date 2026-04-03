# Strategies

Source: https://python-social-auth.readthedocs.io/en/latest/strategies.html

Strategies
¶

Different strategies are defined to encapsulate the different frameworks
capabilities under a common API to reuse as much code as possible.

Description
¶

A strategy’s responsibility is to provide access to:

Request data and host information and URI building

Session access

Project settings

Response types (HTML and redirects)

HTML rendering

Different frameworks implement these features on different ways, thus the need
for these interfaces.

Implementing a new Strategy
¶

The following methods must be defined on strategies sub-classes.

Request:

def

request_data

(

self

):

&quot;&quot;&quot;Return current request data (POST or GET)&quot;&quot;&quot;

raise

NotImplementedError

(

&#39;Implement in subclass&#39;

)

def

request_host

(

self

):

&quot;&quot;&quot;Return current host value&quot;&quot;&quot;

raise

NotImplementedError

(

&#39;Implement in subclass&#39;

)

def

build_absolute_uri

(

self

,

path

=

None

):

&quot;&quot;&quot;Build absolute URI with given (optional) path&quot;&quot;&quot;

raise

NotImplementedError

(

&#39;Implement in subclass&#39;

)

Session:

def

session_get

(

self

,

name

):

&quot;&quot;&quot;Return session value for given key&quot;&quot;&quot;

raise

NotImplementedError

(

&#39;Implement in subclass&#39;

)

def

session_set

(

self

,

name

,

value

):

&quot;&quot;&quot;Set session value for given key&quot;&quot;&quot;

raise

NotImplementedError

(

&#39;Implement in subclass&#39;

)

def

session_pop

(

self

,

name

):

&quot;&quot;&quot;Pop session value for given key&quot;&quot;&quot;

raise

NotImplementedError

(

&#39;Implement in subclass&#39;

)

Settings:

def

get_setting

(

self

,

name

):

&quot;&quot;&quot;Return value for given setting name&quot;&quot;&quot;

raise

NotImplementedError

(

&#39;Implement in subclass&#39;

)

Responses:

def

html

(

self

,

content

):

&quot;&quot;&quot;Return HTTP response with given content&quot;&quot;&quot;

raise

NotImplementedError

(

&#39;Implement in subclass&#39;

)

def

redirect

(

self

,

url

):

&quot;&quot;&quot;Return a response redirect to the given URL&quot;&quot;&quot;

raise

NotImplementedError

(

&#39;Implement in subclass&#39;

)

def

render_html

(

self

,

tpl

=

None

,

html

=

None

,

context

=

None

):

&quot;&quot;&quot;Render given template or raw html with given context&quot;&quot;&quot;

raise

NotImplementedError

(

&#39;Implement in subclass&#39;

)