# Backends/Telegram

Source: https://python-social-auth.readthedocs.io/en/latest/backends/telegram.html

Telegram
¶

Telegram uses a widget-based authentication method for login.

Create a bot using 
BotFather
 on Telegram to get a bot token.

Add the Telegram backend to 

AUTHENTICATION_BACKENDS

:

AUTHENTICATION_BACKENDS

=

(

...

&#39;social_core.backends.telegram.TelegramAuth&#39;

,

...

)

Fill the 

Bot

Token

 value in the settings:

SOCIAL_AUTH_TELEGRAM_BOT_TOKEN

=

&#39;&#39;

Add the Telegram Login Widget to your login page. The widget should be configured
to send authentication data to your callback URL, which should be something like

http://example.com/complete/telegram/

 replacing 

example.com

 with your domain.

The Telegram Login Widget can be added using the following HTML:

&lt;

script

async

src

=

&quot;https://telegram.org/js/telegram-widget.js?22&quot;

data

-

telegram

-

login

=

&quot;YOUR_BOT_USERNAME&quot;

data

-

size

=

&quot;large&quot;

data

-

auth

-

url

=

&quot;http://example.com/complete/telegram/&quot;

data

-

request

-

access

=

&quot;write&quot;

&gt;&lt;/

script

&gt;

Replace 

YOUR_BOT_USERNAME

 with your bot’s username (without the &#64; symbol)
and update the 

data-auth-url

 to match your domain.

The authentication process verifies the data integrity using HMAC-SHA256 with
the bot token. Authentication data is considered valid for 24 hours from the

auth_date

 timestamp.

The backend extracts the following user information:
- User ID (required)
- Username
- First name
- Last name
- Photo URL (if available)