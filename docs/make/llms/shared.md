# Source: https://developers.make.com/custom-apps-documentation/app-components/webhooks/shared.md

# Shared

{% hint style="info" %}
When the service sends all the notifications to only one webhook URL but the webhook has to be registered under a user account, that's a [dedicated webhook](https://developers.make.com/custom-apps-documentation/app-components/webhooks/dedicated), not a shared one.
{% endhint %}

In order to activate the shared webhook so it listens to incoming traffic, you must publish your app. Before doing so, please read the [app visibility article](https://developers.make.com/custom-apps-documentation/app-visibility) to understand how that affects your app.

## Implementation

Shared webhooks must be registered in the external platform by the developer of the app. All notifications from the service for all users will be sent to Make through this single URL, which is generated when creating the shared webhook. On Make's end, the corresponding user account will be matched by it's `uid`.

{% hint style="info" %}
You should always follow the API documentation for the platform for which you are developing the integration.
{% endhint %}

## Matching the user's account with an incoming event

Since the webhook URL is shared among multiple users, there must be a way to match the incoming events with their owners and deliver them correctly. This is done through the `uid` parameter, which **must** be defined both in the connection and in the webhook communication.

{% hint style="info" %}
Since the `uid` from the connection is needed to allow Make to match the incoming data to its intended recipient, **all** shared webhooks **must** have a connection attached to the webhook.
{% endhint %}

{% tabs %}
{% tab title="Connection" %}

```json
{
    ...

    "info": {
        "url": "https://example.com/api/me",
        "headers": {
            "authorization": "Bearer {{connection.accessToken}}"
        },
        "response": {
            "uid": "{{body.user.id}}",
            "valid": "{{body.ok}}",
            "metadata": {
                "type": "text",
                "value": "{{body.user.fullName}} ({{body.user.email}})"
            }
        },
        "log": {
            "sanitize": [
                "request.headers.authorization"
            ]
        }
    }

    ...
}
```

{% hint style="info" %}
Notice the `uid` parameter in the `response` object.
{% endhint %}
{% endtab %}

{% tab title="Webhook communication" %}

```json
{
	"uid": "{{item.uid}}",
	"output": "{{item.data}}",
	...
}
```

{% hint style="info" %}
Notice the `uid` parameter in the webhook's communication.
{% endhint %}
{% endtab %}
{% endtabs %}
