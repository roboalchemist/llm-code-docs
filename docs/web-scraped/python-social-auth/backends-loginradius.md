# Backends/Loginradius

Source: https://python-social-auth.readthedocs.io/en/latest/backends/loginradius.html

LoginRadius
¶

LoginRadius uses OAuth2 for Authentication with other providers with an HTML
widget used to trigger the auth process.

Register a new application at the 
LoginRadius Website
, and

Fill 

Client

Id

 and 

Client

Secret

 values in the settings:

SOCIAL_AUTH_LOGINRADIUS_KEY

=

&#39;&#39;

SOCIAL_AUTH_LOGINRADIUS_SECRET

=

&#39;&#39;

Since the auth process is triggered by LoginRadius JS script, you need to
sever such content to the user, all you need to do that is a template with
the following content:

&lt;div id=&quot;interfacecontainerdiv&quot; class=&quot;interfacecontainerdiv&quot;&gt;&lt;/div&gt;
&lt;script src=&quot;https://hub.loginradius.com/include/js/LoginRadius.js&quot;&gt;&lt;/script&gt;
&lt;script type=&quot;text/javascript&quot;&gt;
    var options = {};
    options.login = true;
    LoginRadius_SocialLogin.util.ready(function () {
        $ui = LoginRadius_SocialLogin.lr_login_settings;
        $ui.interfacesize = &quot;&quot;;
        $ui.apikey = &quot;{{ LOGINRADIUS_KEY }}&quot;;
        $ui.callback = &quot;{{ LOGINRADIUS_REDIRECT_URL }}&quot;;
        $ui.lrinterfacecontainer = &quot;interfacecontainerdiv&quot;;
        LoginRadius_SocialLogin.init(options);
    });
&lt;/script&gt;

Put that content in a template named 

loginradius.html

 (accessible to your
framework), or define a name with 

SOCIAL_AUTH_LOGINRADIUS_TEMPLATE

 setting,
like:

SOCIAL_AUTH_LOGINRADIUS_LOCAL_HTML

=

&#39;loginradius.html&#39;

The template context will have the current backend instance under the

backend

 name, also the application key (

LOGINRADIUS_KEY

) and the
redirect URL (

LOGINRADIUS_REDIRECT_URL

).

Further documentation can be found at 
LoginRadius API Documentation
 and

LoginRadius Datapoints