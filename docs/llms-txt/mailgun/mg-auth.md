# Source: https://documentation.mailgun.com/docs/mailgun/api-reference/mg-auth.md

# Authentication

Authentication to the Mailgun API is done by providing an Authorization header using [HTTP Basic Auth:](http://en.wikipedia.org/wiki/Basic_access_authentication)

- **Username:** `api`
- **Password:** `YOUR_API_KEY`


### API keys

Mailgun provides two types of API keys for authenticating against the API

#### Primary account API key

When you sign up for Mailgun, a primary account API key is generated. This key allows you to perform all CRUD operations via our various API endpoints and for any of your sending domains. To view your primary account API key:

1. **Go** to the **Mailgun Dashboard**
2. **Click** on **Account Settings** on the right-hand side.
3. **Select API Keys** and **click** on the eye icon next to **Private API** key.


#### Domain Sending Keys

Domain Sending Keys are API keys that only allow sending messages via a POST call on /messages and /messages.mime endpoints for the domain in which they are created for. To create a sending API key:

1. **Go** to the **Mailgun Dashboard**
2. **Click** the **Sending** tab on the left-hand side of the Mailgun dashboard
3. **Click** the **Domains** tab and select the domain in which you wish to add a sending key to
4. **Click** the **Domain Settings** and navigate to the **Sending API keys** tab
5. **Click** on **Add Sending Key**


Give your key a suitable description (such as the name of the application or client you are creating the key for) and click Create Sending Key

Copy your API key and keep it in a safe place. For security purposes, we will not be able to show you the key again. If you lose your key, you will need to create a new key.

Here is how you use basic HTTP auth with curl:


```curl
curl --user 'api:YOUR_API_KEY'
```

Warning!
Important reminder to keep your API key safe and secure!