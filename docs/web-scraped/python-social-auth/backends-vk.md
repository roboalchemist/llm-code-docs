# Backends/Vk

Source: https://python-social-auth.readthedocs.io/en/latest/backends/vk.html

VK.com (former Vkontakte)
¶

VK.com (former Vkontakte) auth service support.

OAuth2
¶

VK.com uses OAuth2 for Authentication.

Register a new application at the 
VK.com API
,

fill 

Application

Id

 and 

Application

Secret

 values in the settings:

SOCIAL_AUTH_VK_OAUTH2_KEY

=

&#39;&#39;

SOCIAL_AUTH_VK_OAUTH2_SECRET

=

&#39;&#39;

Add 

'social_core.backends.vk.VKOAuth2'

 into your 

SOCIAL_AUTH_AUTHENTICATION_BACKENDS

.

Then you can start using 

/login/vk-oauth2

 in your link href.

Also it’s possible to define extra permissions with:

SOCIAL_AUTH_VK_OAUTH2_SCOPE

=

[

...

]

See the 
VK.com list of permissions
.

OAuth2 Application
¶

To support OAuth2 authentication for VK.com applications:

Create your IFrame application at VK.com.

In application settings specify your IFrame URL 

https://mysite.com/complete/vk-app

 (current
default).

In application settings specify the first API request. For example:

method

=

getProfiles

&amp;

uids

=

{

viewer_id

}

&amp;

format

=

json

&amp;

v

=

5.53

&amp;

fields

=

id

,

first_name

,

last_name

,

screen_name

,

photo

See the 
documentation on available fields
.

Add 

'social_core.backends.vk.VKAppOAuth2'

 into your 

SOCIAL_AUTH_AUTHENTICATION_BACKENDS

.

Fill 

Application

ID

 and 

Application

Secret

 settings:

SOCIAL_AUTH_VK_APP_KEY

=

&#39;&#39;

SOCIAL_AUTH_VK_APP_SECRET

=

&#39;&#39;

Fill 

user_mode

:

SOCIAL_AUTH_VK_APP_USER_MODE

=

2

Possible values:

0

: there will be no check whether a user connected to your
application or not

1

: 

python-social-auth

 will check 

is_app_user

 parameter
VK.com sends when user opens application page one time

2

: (safest) 

python-social-auth

 will check status of user
interactively (useful when you have interactive authentication via AJAX)

Add a snippet similar to this into your login template:

&lt;

script

src

=

&quot;http://vk.com/js/api/xd_connection.js?2&quot;

type

=

&quot;text/javascript&quot;

&gt;&lt;/

script

&gt;

&lt;

script

type

=

&quot;text/javascript&quot;

&gt;

VK

.

init

(

function

()

{

VK

.

addCallback

(

&quot;onApplicationAdded&quot;

,

requestRights

);

VK

.

addCallback

(

&quot;onSettingsChanged&quot;

,

onSettingsChanged

);

}

);

function

startConnect

()

{

VK

.

callMethod

(

&#39;showInstallBox&#39;

);

}

function

requestRights

()

{

VK

.

callMethod

(

&#39;showSettingsBox&#39;

,

1

+

2

);

//

1

+

2

is

just

an

example

}

function

onSettingsChanged

(

settings

)

{

window

.

location

.

reload

();

}

&lt;/

script

&gt;

&lt;

a

href

=

&quot;#&quot;

onclick

=

&quot;startConnect(); return false;&quot;

&gt;

Click

to

authenticate

&lt;/

a

&gt;

To test, launch the server using 

sudo

./manage.py

mysite.com:80

 for
browser to be able to load it when VK.com calls IFrame URL. Open your
VK.com application page via 
http://vk.com
/app&lt;app_id&gt;. Now you are able to
connect to application and login automatically after connection when visiting
application page.

For more details see 
authentication for VK.com applications

OpenAPI
¶

You can also use VK.com’s own OpenAPI to log in, but you need to provide
HTML template with JavaScript code to authenticate, check below for an example.

Get an OpenAPI App Id and add it to the settings:

SOCIAL_AUTH_VK_OPENAPI_APP_ID

=

&#39;&#39;

This app id will be passed to the template as 

VK_APP_ID

.

Add 

'social_core.backends.vk.VKontakteOpenAPI'

 into your 

SOCIAL_AUTH_AUTHENTICATION_BACKENDS

.

Snippet example:

&lt;script src=&quot;http://vk.com/js/api/openapi.js&quot; type=&quot;text/javascript&quot;&gt;&lt;/script&gt;
&lt;script type=&quot;text/javascript&quot;&gt;
    var vkAppId = {{ VK_APP_ID|default:&quot;null&quot; }};
    if (vkAppId) {
        VK.init({ apiId: vkAppId });
    }
    function authVK () {
        if (!vkAppId) {
            alert (&quot;Please specify VK.com APP ID in your local settings file&quot;);
            return false;
        }
        VK.Auth.login(function(response) {
            var params = &quot;&quot;;
            if (response.session) {
                params = &quot;first_name=&quot; + encodeURI(response.session.user.first_name) + &quot;&amp;last_name=&quot; + encodeURI(response.session.user.last_name);
                params += &quot;&amp;nickname=&quot; + encodeURI(response.session.user.nickname) + &quot;&amp;id=&quot; + encodeURI(response.session.user.id);
            }
            window.location = &quot;{{ VK_COMPLETE_URL }}?&quot; + params;
        });
        return false;
    }
&lt;/script&gt;
&lt;a href=&quot;javascript:void(0);&quot; onclick=&quot;authVK();&quot;&gt;Click to authorize&lt;/a&gt;