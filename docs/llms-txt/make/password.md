# Source: https://developers.make.com/custom-apps-documentation/block-elements/parameters/password.md

# Password

The `password` type is dedicated to marking parameters in a connection that should be kept secret when the user is editing a connection.

In addition, when the user types in a `password` field, the text in the field is masked.

{% hint style="info" %}
The `password` parameter type is only available in a connection. If used in other modules, this parameter behaves like a `text` parameter.
{% endhint %}

## Example

The user is updating an app connection:

{% tabs %}
{% tab title="Appearance" %}

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-c88f0201d296d33bac8335400fa67ae6f6f1f5eb%2Fpassword2.png?alt=media" alt="" width="544"><figcaption></figcaption></figure></div>
{% endtab %}

{% tab title="Source" %}

```json
[
    {
        "name": "serviceUrl",
        "type": "url",
        "required": true,
        "editable": true,
        "label": "Service URL"
    },
    {
        "name": "username",
        "type": "email",
        "required": true,
        "editable": true,
        "label": "Username"
    },
    {
        "name": "apiToken",
        "type": "password",
        "required": true,
        "editable": true,
        "label": "API Token"
    }
]
```

{% endtab %}
{% endtabs %}
