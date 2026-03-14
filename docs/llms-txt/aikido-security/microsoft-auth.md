# Source: https://help.aikido.dev/pentests/setting-up-authenticated-testing/microsoft-auth.md

# Microsoft Auth

{% stepper %}
{% step %}

#### Navigate to security settings

Go to the settings page of your account: <https://account.microsoft.com/security> and start the setup of Two-step verification

<div data-with-frame="true"><figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FhnTfTMpI5PcX0yOI9ASL%2FScreenshot%202025-12-19%20at%2017.52.15.png?alt=media&#x26;token=429cbe6d-74d2-4f23-89d4-6adbc74b35de" alt=""><figcaption></figcaption></figure></div>
{% endstep %}

{% step %}

#### Set up Two-step verification

Choose to set it up with a different Authenticator app.

<div data-with-frame="true"><figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FsnX1mFYXp8BRTmcoiXTy%2FScreenshot%202025-12-19%20at%2017.53.19.png?alt=media&#x26;token=2499f20b-41f2-4ac7-a00c-03e4bca24b92" alt=""><figcaption></figcaption></figure></div>
{% endstep %}

{% step %}

### Get secret instead of code

When seeing the QR code, select the option "I can't scan the bar code"&#x20;

<div data-with-frame="true"><figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FMsXsUGlj32QtfgdQX78s%2FScreenshot%202025-12-19%20at%2017.53.31.png?alt=media&#x26;token=7bbb06e7-008e-4a31-9577-84c833dc4e6a" alt=""><figcaption></figcaption></figure></div>
{% endstep %}

{% step %}

### Copy the key

<div data-with-frame="true"><figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FZauJH5oNpFy5oIqLL7o8%2FScreenshot%202025-12-19%20at%2017.54.09.png?alt=media&#x26;token=ce85d536-ae5f-44a5-b53c-3289c5c02684" alt=""><figcaption></figcaption></figure></div>
{% endstep %}

{% step %}

### Store key in password manager

Now add the key for the password manager in a password manager of choice. We recommend using a password manager that easily allows for the extraction of the key like 1Password or Bitwarden.&#x20;
{% endstep %}

{% step %}

### Fulfill the the flow and enable 2-Step Verification

<div data-with-frame="true"><figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FZlUdv1xIOe4cKjZjiinm%2FScreenshot%202025-12-19%20at%2017.55.13.png?alt=media&#x26;token=48d4fd1c-e37e-4506-83a2-e83256b59867" alt=""><figcaption></figcaption></figure></div>
{% endstep %}

{% step %}

### Set up authentication in Aikido Pentest

Write your instructions in a similar format as below

```
Step 1: Go to domain.com/login
Step 2: Select "Microsoft Login". You will be redirected to login.microsoftonline.com
Step 3: provide the following credentials:
- username: <username>
- password: <password>
Step 4: Generate the TOTP and log in
Success criteria: When successfully logged in, you will see "Hello Aikido" on the homescreen
```

{% endstep %}

{% step %}

### Add the TOTP URL

Add the key in the correct base32 format. When adding the key from Microsoft, make sure to remove the spaces

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2F7drEWkPjCSSf7oqWw4LB%2Fimage.png?alt=media&#x26;token=262fa056-62dd-4da0-8982-79b2d7b5cb10" alt=""><figcaption></figcaption></figure>

{% endstep %}
{% endstepper %}
