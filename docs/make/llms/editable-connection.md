# Source: https://developers.make.com/custom-apps-documentation/best-practices/connections/editable-connection.md

# Editable connection

We recommend allowing users to [edit their connections](https://help.make.com/connect-an-application#tN2pJ) after they create them. Updating a connection simplifies scenario and user credential maintenance when there's a change in the user's organization.

To allow users to edit a connection:

{% stepper %}
{% step %}
Go to the **Parameters** tab of the connection.
{% endstep %}

{% step %}
For each parameter with a value that should be kept secret, make sure that it is marked as type `password`.

Parameters with the `password` type don't show the original connection's parameter value, while the parameters with the `text` type show the value used by the current connection.
{% endstep %}

{% step %}
Add the `editable: true` property for each parameter in the connection.

```json
[
    {
        "help": "Your MailerLite API Key.",
        "name": "apiKey",
        "type": "password",
        "label": "API Key",
        "editable":true,
        "required": true
    }
]
```

{% endstep %}
{% endstepper %}

{% hint style="info" %}
**Exception**: If the service provides each user with a unique URL or domain, the corresponding URL or domain parameter must be non-editable to prevent any potential credential leaks.
{% endhint %}
