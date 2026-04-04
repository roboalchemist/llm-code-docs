# Backends/Discourse

Source: https://python-social-auth.readthedocs.io/en/latest/backends/discourse.html

Discourse
¶

Discourse can serve as a Single Sign On provider for Authentication.

Deploy a Discourse application and 
configure
&lt;https://meta.discourse.org/t/using-discourse-as-a-sso-provider/32974&gt;
 the
application to enable Discourse as an SSO provider.

Fill in the shared secret and url of the Discourse server in the settings:

SOCIAL_AUTH_DISCOURSE_SECRET

=

&quot;myDiscourseSecret&quot;

SOCIAL_AUTH_DISCOURSE_SERVER_URL

=

&quot;https://my-discourse-site.com&quot;

Using multiple Discourse instances
¶

Since Discourse is a distributed application, multiple Discourse instances can
be used as SSO providers. If this is the case, the DiscourseAuth class can be
extended and configured as follows:

from

social_core.backends.discourse

import

DiscourseAuth

class

DiscourseAuthFoo

(

DiscourseAuth

):

name

=

&#39;discourse-foo&#39;

class

DiscourseAuthBar

(

DiscourseAuth

):

name

=

&#39;discourse-bar&#39;

Fill in the settings like so:

SOCIAL_AUTH_DISCOURSE_FOO_SECRET

=

&quot;myDiscourseFooSecret&quot;

SOCIAL_AUTH_DISCOURSE_FOO_SERVER_URL

=

&quot;https://my-discourse-foo-site.com&quot;

SOCIAL_AUTH_DISCOURSE_BAR_SECRET

=

&quot;myDiscourseBarSecret&quot;

SOCIAL_AUTH_DISCOURSE_BAR_SERVER_URL

=

&quot;https://my-discourse-bar-site.com&quot;