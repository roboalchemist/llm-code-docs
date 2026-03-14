# Source: https://developers.make.com/custom-apps-documentation/best-practices/connections/connection-metadata.md

# Connection metadata

We recommend you use the `metadata` parameter to store the account's name or email. This allows users to easily distinguish their stored connections.

Always save the metadata in the connection if:

* the endpoint that can obtain the authenticated user’s information is available, and
* the information provided is able to distinguish the connection.

Saving the metadata allows for better identification on the Connections page.

We suggest saving the following information:

* Name
* Email
* User ID
* Organization, Company, Location, etc.

{% hint style="info" %}
When a string is stored as `metadata`, Make sets a limit of 512 characters.
{% endhint %}

{% tabs %}
{% tab title="Occurrence" %}

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-427a0fc6bd2b4b0fbfb02528a613609c318d6835%2Fconnection_metadata.png?alt=media" alt="" width="470"><figcaption></figcaption></figure></div>

{% hint style="info" %}
The value in the brackets after the user's connection name is taken from the `metadata` parameter.
{% endhint %}
{% endtab %}

{% tab title="Source" %}

```javascript
...
"response": {
    "metadata": {
            "type": "email", //allowed values are "email" and "text"
            "value": "{{body.data.user.email}}"
        }
},
...
```

{% endtab %}
{% endtabs %}
