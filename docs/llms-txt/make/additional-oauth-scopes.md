# Source: https://developers.make.com/custom-apps-documentation/best-practices/connections/additional-oauth-scopes.md

# Additional OAuth scopes

The Make an API Call module connection will not work if the required scopes of the endpoint are not in the OAuth connection. To correct this, allow users to define additional scopes when they create a connection.

## Make an API Call parameters: non-editable connection <a href="#make-an-api-call-parameters-if-connection-is-not-editable" id="make-an-api-call-parameters-if-connection-is-not-editable"></a>

{% tabs %}
{% tab title="Module message" %}

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-bb97a783437c54f65c4c0150ffd2cdbe941ede35%2Fnoneditableconnectionmessage.png?alt=media" alt="" width="375"><figcaption></figcaption></figure></div>
{% endtab %}

{% tab title="Source" %}

```json
{
	"type": "banner",
	"text": "Your connection must contain the required scopes for your API call. If you receive an error, create a new connection with the necessary Additional scopes.",
	"theme": "info"
}
```

{% hint style="info" %}
If you encounter the warning `String is longer than the maximum length of 256.` , wrap it in an RPC.
{% endhint %}
{% endtab %}
{% endtabs %}

## Make an API Call parameters: editable connection

{% tabs %}
{% tab title="Source" %}

```json
{
	"type": "banner",
	"text": "Your connection must contain the required scopes for your API call. If you receive an error, edit your connection with the necessary Additional scopes.",
	"theme": "info"
}
```

{% endtab %}
{% endtabs %}

## Connection parameters

{% tabs %}
{% tab title="Module" %}

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-25a943d4ad7afbd313050ef5fe0650f440298b57%2Fadditionalscopesconnection.png?alt=media" alt="" width="375"><figcaption></figcaption></figure></div>
{% endtab %}

{% tab title="Source" %}

```json
[
    {
        "name": "additionalScopes",
        "label": "Additional Scopes",
        "type": "array",
        "spec": {
            "type": "text",
            "label": "Scope"
        },
        "help": "Additional scopes are required for the __Make an API Call__ module. For details, see the [App Name API Documentation](https://link-to-doc). Add scopes for every API call you will make with this connection.",
		"labels": {
			"add": "Add scope"
		}
    },
    {
        "name": "clientId",
        "type": "text",
        "label": "Client ID",
        "advanced": true
    },
    {
        "name": "clientSecret",
        "type": "password",
        "label": "Client Secret",
        "advanced": true
    }
]
```

{% endtab %}
{% endtabs %}

## Connection communication

{% tabs %}
{% tab title="Source" %}

```json
{
    "authorize": {
        "qs": {
            "scope": "{{join(distinct(merge(oauth.scope, ifempty(parameters.additionalScopes, emptyarray))), ',')}}",
            ...
        },
        "url": "...",
        "response": {
            "temp": {
                "code": "{{query.code}}"
            }
        }
    }
}
```

{% endtab %}
{% endtabs %}
