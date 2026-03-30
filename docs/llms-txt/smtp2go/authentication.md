# Source: https://developers.smtp2go.com/reference/authentication.md

# Authentication

All requests to the API must be authenticated using an API Key.

## Obtain your API Key

To obtain an API key, log in to the [SMTP2GO App](https://app.smtp2go.com) and navigate to the "**Sending** > **API Keys**" section.

On the API Keys page, click the "**Add API Key**" button to create an API Key. If you have an existing API Key, you can copy that or manage the settings by clicking on the API Key.

<Image align="center" src="https://files.readme.io/1fb8e14-API_Keys_-_Authentication.png" />

## API Key Settings and Customisation

During the setup of your API Key and at any time thereafter, you can modify the following:

* Set the Description of your API Key to show a friendly identifier.
* Set a Rate Limit for your API Key. This defaults to unlimited.
* Set the Permissions for your API Key. You can specify permissions to determine whether the key can access a particular endpoint.
* Enable the [Unsubscribe Footer](https://support.smtp2go.com/hc/en-gb/articles/223087607-Unsubscribe-Footer).
* Enable [Open Tracking](https://support.smtp2go.com/hc/en-gb/articles/360003124714-Open-Tracking).
* Enable [Click Tracking](https://support.smtp2go.com/hc/en-gb/articles/900002237106-Click-Tracking).
* Temporarily [Disable your API Key](https://support.smtp2go.com/hc/en-gb/articles/900003891586-Disabling-an-SMTP-Username-IP-Address-or-API-Key) or set it to [Sandbox Mode](https://support.smtp2go.com/hc/en-gb/articles/29736421853337-Sandbox-Mode).
* Enable [Email Archiving](https://support.smtp2go.com/hc/en-gb/articles/115003599568-Email-Archiving).
* Set a BCC Address for [Email Auditing](https://support.smtp2go.com/hc/en-gb/articles/115004851734-Email-Auditing).
* Enable [Bounce Notifications](https://support.smtp2go.com/hc/en-gb/articles/360023602974-Bounce-Notifications).

## Using your API Key

Every request you make to the SMTP2GO API must authenticate with an API Key by either including the **api\_key** field or you can include an **X-Smtp2go-Api-Key** field in your header.

```json Example api_key field
{
    "api_key": "YourAPIKeyHere",
    "search_subject": "Booking",
    "event_types": ["opened", "clicked"],
    "only_latest": true,
    "limit": 1
}
```

```json Example Headers
{
  'Content-Type': 'application/json',
  'X-Smtp2go-Api-Key': 'YourAPIKeyHere'
}
```

Failure to supply an API Key, or supplying an API Key that is invalid or disabled, will result in a `401 - Unauthorised`error.