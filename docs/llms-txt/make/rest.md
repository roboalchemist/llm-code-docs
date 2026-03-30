# Source: https://developers.make.com/custom-apps-documentation/app-components/modules/universal-module/rest.md

# REST

## **Naming Convention**

All REST universal modules should have the following module label and description:

* **Module label**: Make an API call
* **Module description**: Performs an arbitrary authorized API call.

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-bc5557f2d9fa33cb9f9b9b3af5958acfa483fd21%2FrestAPI.png?alt=media" alt="" width="324"><figcaption></figcaption></figure></div>

## URL parameter

Expected input from users should start with `/` (for example `/tasks`) so users can copy-paste the endpoint path from the service documentation.

If the API has multiple versions of API available, the user should be allowed to use any of them. The URL set in the universal module should end before the version.

Set the correct URL in `help` and add a working endpoint example.

{% tabs %}
{% tab title="Good practice" %}
**Communication**

```json
{
    "url": "https://www.example.com/{{parameters.url}}"
}
```

**Mappable parameters**

```json
{
        "name": "url",
        "type": "text",
        "label": "URL",
        "help": "Enter a path relative to `https://www.example.com`. For example: `/v1/something`",
        "required": true
}
```

{% hint style="info" %}
Even when the URL in Communication ends with `/` before {{parameters.url}}, we ask users to use `/` in the URL because it is automatically removed.
{% endhint %}
{% endtab %}

{% tab title="Bad practice" %}
**Communication**

```json
{
    "url": "https://www.example.com/v1/{{parameters.url}}"
}
```

**Mappable parameters**

```json
{
        "name": "url",
        "type": "text",
        "label": "URL",
        "help": "Enter a path relative to `https://www.example.com/v1/`. For example: `something`",
        "required": true
}
```

{% hint style="warning" %}
The "url" in the Communication has the API version in it.

The `help` has a misleading example, as the base URL should end without a slash and version, and the example should start with a slash and version.
{% endhint %}
{% endtab %}
{% endtabs %}

## Rest universal module example

{% tabs %}
{% tab title="Appearance" %}

<div align="left"><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-bb9deddabfd24ec730ab35d44b3998051e80d6f1%2FrestAPI_module.png?alt=media" alt="" width="518"></div>
{% endtab %}

{% tab title="Communication" %}

```json
{
	"qs": {
		"{{...}}": "{{toCollection(parameters.qs, 'key', 'value')}}"
	},
	"url": "https://www.example.com/{{parameters.url}}",
	"body": "{{parameters.body}}",
	"type": "text",
	"method": "{{parameters.method}}",
	"headers": {
		"{{...}}": "{{toCollection(parameters.headers, 'key', 'value')}}"
	},
	"response": {
		"output": {
			"body": "{{body}}",
			"headers": "{{headers}}",
			"statusCode": "{{statusCode}}"
		}
	}
}
```

{% endtab %}

{% tab title="Static parameters" %}

```json
[]
```

{% endtab %}

{% tab title="Mappable parameters" %}

```json
[
	{
		"help": "Enter a path relative to `https://www.example.com`.\nFor example: `/v1/api/list`",
		"name": "url",
		"type": "text",
		"label": "URL",
		"required": true
	},
	{
		"name": "method",
		"type": "select",
		"label": "Method",
		"default": "GET",
		"options": [
			{
				"label": "GET",
				"value": "GET"
			},
			{
				"label": "POST",
				"value": "POST"
			},
			{
				"label": "PUT",
				"value": "PUT"
			},
			{
				"label": "PATCH",
				"value": "PATCH"
			},
			{
				"label": "DELETE",
				"value": "DELETE"
			}
		],
		"required": true
	},
	{
		"help": "You don't have to add authorization headers; we already did that for you.",
		"name": "headers",
		"spec": [
			{
				"name": "key",
				"type": "text",
				"label": "Key"
			},
			{
				"name": "value",
				"type": "text",
				"label": "Value"
			}
		],
		"type": "array",
		"label": "Headers",
		"default": [
			{
				"key": "Content-Type",
				"value": "application/json"
			}
		]
	},
	{
		"name": "qs",
		"spec": [
			{
				"name": "key",
				"type": "text",
				"label": "Key"
			},
			{
				"name": "value",
				"type": "text",
				"label": "Value"
			}
		],
		"type": "array",
		"label": "Query String"
	},
	{
		"name": "body",
		"type": "any",
		"label": "Body"
	}
]
```

{% endtab %}

{% tab title="Interface" %}

```json
[
	{
		"name": "body",
		"type": "any",
		"label": "Body"
	},
	{
		"name": "headers",
		"type": "collection",
		"label": "Headers"
	},
	{
		"name": "statusCode",
		"type": "number",
		"label": "Status code"
	}
]
```

{% endtab %}

{% tab title="Samples" %}

```json
{}
```

{% endtab %}
{% endtabs %}

## OAuth scopes

When your app requires specifying scopes to access different groups of endpoints, you need to change the connection code to ensure that it works correctly with the universal module:

{% stepper %}
{% step %}
Add a new advanced parameter called `scopes` to the connection parameters.

{% tabs %}
{% tab title="Preview" %}

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-7af30cbc715e94de4e3611eb3c681ddea0f9d8b7%2Fimage%20(5)%20(1).png?alt=media" alt="" width="563"><figcaption><p>Advanced parameter scopes</p></figcaption></figure></div>
{% endtab %}

{% tab title="Code" %}

```json
[
    {
        "name": "clientId",
        "type": "text",
        "label": "Client ID",
        "advanced": true
    },
    {
        "name": "clientSecret",
        "type": "text",
        "label": "Client Secret",
        "advanced": true
    },
    {
        "name": "scopes",
        "label": "Additional Scopes",
        "type": "array",
        "help": "Use this to get an access to extra scopes.",
        "advanced": true
    }
]
```

{% endtab %}
{% endtabs %}
{% endstep %}

{% step %}
In the `authorize` part of the connection, merge the original scopes with additional scopes added by the parameter from the previous step.

{% tabs %}
{% tab title="Preview" %}

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-5df74df3708f0ac27f0ceefd62ab058cca65e05d%2Fimage%20(6)%20(1).png?alt=media" alt="" width="563"><figcaption><p>Scope parameter in authorization</p></figcaption></figure></div>
{% endtab %}

{% tab title="Code" %}

```json
"authorize": {
        "qs": {
            "scope": "{{join(distinct(merge(oauth.scope, ifempty(parameters.scopes, emptyarray))), ',')}}",
            "client_id": "{{common.clientId}}",
            "redirect_uri": "{{oauth.redirectUri}}",
            "response_type": "code"
        },
        "url": "...",
        "response": {
            "temp": {
                "code": "{{query.code}}"
            }
        }
}
```

{% endtab %}
{% endtabs %}
{% endstep %}
{% endstepper %}

Now a user can add additional scopes manually when creating a connection and these scopes will work with the universal module.
