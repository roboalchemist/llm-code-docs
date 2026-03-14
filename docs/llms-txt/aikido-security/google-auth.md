# Source: https://help.aikido.dev/pentests/setting-up-authenticated-testing/google-auth.md

# Google Auth

## General

In order to enable the agents to log in with Google Auth, follow the steps below:&#x20;

{% stepper %}
{% step %}

#### Navigate to security settings

Go to the settings page of your account: <https://myaccount.google.com/u/1/security>

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2F85IQEE6cXelFwVWwrZIF%2Fimage.png?alt=media&#x26;token=feb5071c-f5d4-4dd6-b426-83a39ca4c395" alt=""><figcaption></figcaption></figure>

Start the authenticator flow
{% endstep %}

{% step %}

#### MFA Onboarding

Click on the authenticator app option to configure the MFA.&#x20;

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FmTA1GWw6FdxUaZQLhRbs%2Fimage.png?alt=media&#x26;token=e04a05f6-778f-4390-9b46-4836baa41c65" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}

### Get secret instead of code

When seeing the QR code, select the option "Can't scan it?"&#x20;

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2F8YC5HcyPsgkZtGFQyvSd%2Fimage.png?alt=media&#x26;token=685b21d8-82cd-42ec-8e3b-6dbe72a1f635" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}

### Copy the key

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FiO5nw0F6idwF5atjGdkC%2Fimage.png?alt=media&#x26;token=82bc77ad-0eda-4e53-9861-7f2ed578b329" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}

### Store key in password manager

Now add the key for the password manager in a password manager of choice. We recommend using a password manager that easily allows for the extraction of the key like 1Password or Bitwarden
{% endstep %}

{% step %}

### Fulfil the the flow and enable 2-Step Verification

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FeBtKB1zLDHvTXUuqZxqD%2Fimage.png?alt=media&#x26;token=502a8d65-eca5-4c1c-8e52-f53e63bcdac9" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}

### Set up authentication in Aikido Pentest

Write your instructions in a similar format as below

```
Step 1: Go to domain.com/login
Step 2: Select "Google Login". You will be redirected to accounts.google.com
Step 3: provide the following credentials:
- username: patrickprinterservices@gmail.com
- password: wrongpassword
Step 4: Generate the TOTP and log in
Success criteria: When successfully logged in, you will see "Hello Patrick" on the homescreen
```

{% endstep %}

{% step %}

### Add the TOTP URL

Add the key in the correct base32 format. When adding the key from Google, make sure to remove the spaces

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2F7drEWkPjCSSf7oqWw4LB%2Fimage.png?alt=media&#x26;token=262fa056-62dd-4da0-8982-79b2d7b5cb10" alt=""><figcaption></figcaption></figure>

{% endstep %}
{% endstepper %}
