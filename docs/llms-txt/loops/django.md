# Source: https://loops.so/docs/smtp/django.md

> ## Documentation Index
> Fetch the complete documentation index at: https://loops.so/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Django

> Send transactional emails from your Django project using Loops' SMTP service.

<Tip>
  As Loops' SMTP service requires sending an API-like email body rather than a full email, it's not recommended to use Loops as the default SMTP service for your app in your settings file.\
  Instead, use a custom `connection` for each email request that you want to send through Loops.
</Tip>

Sending email from Django with Loops' SMTP service is easy but there's one gotcha: the email body needs to be an [API-like payload](/smtp#how-it-works).

This may seem strange at first but it allows you to use Loops' WYSIWYG editor to craft your emails and keep email templating outside of your code repo.

We are using a custom `connection` for sending this email as typically only some emails in a project will be sent through Loops.

Add these settings to your project (e.g. in an `.env` file).

| Field       | Value                                                                                      |
| ----------- | ------------------------------------------------------------------------------------------ |
| Host        | `smtp.loops.so`                                                                            |
| Port number | `587`                                                                                      |
| Username    | `loops`                                                                                    |
| Password    | An API key copied from your [API settings](http://app.loops.so/settings?page=api) in Loops |

<Warning>
  Every email sent from Django over Loops SMTP requires a transactional email to be set up in your Loops account. Note the `transactionalId` value in the email payload.
</Warning>

```python  theme={"dark"}
from django.core.mail import send_mail, get_connection
import json
import os

with get_connection(
    host=os.environ['LOOPS_SMTP_HOST'],
    port=os.environ['LOOPS_SMTP_PORT'],
    username=os.environ['LOOPS_SMTP_USER'],
    password=os.environ['LOOPS_SMTP_PASSWORD'],
    use_tls=True # Has to be True
) as connection:

    email = 'dan@loops.so'

    # This payload can be copied from a transactional email's 
    #  Publish page in Loops
    payload = {
        "transactionalId": "clomzp89u635xl30px7wrl0ri",
        "email": email,
        "dataVariables": {
            "buttonUrl": "https://myapp.com/login/",
            "userName": "Bob"
        }
    }

    send_mail(
        "Subject here", # Overwritten by Loops template
        json.dumps(payload), # Stringify the payload
        "from@example.com", # Overwritten by Loops template
        [email],
        fail_silently=False,
        connection=connection
    )
```
