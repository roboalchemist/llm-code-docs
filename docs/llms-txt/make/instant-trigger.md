# Source: https://developers.make.com/custom-apps-documentation/app-components/modules/instant-trigger.md

# Instant trigger (webhook)

There is nothing to configure in this module except the interface. The data processing is handled by a selected [webhook](https://developers.make.com/custom-apps-documentation/app-components/webhooks).

## Components

### Communication

* [Communication](https://developers.make.com/custom-apps-documentation/component-blocks/api) is only optional in the instant trigger.
* It can be used for retrieving additional data.
* The `iterate` directive is not available.
* The `pagination` directive is not available.
* Only a single request can be performed.

#### Retrieving additional data for each bundle

If you need to retrieve additional data for each bundle, describe a request to execute for each bundle of the webhook

{% tabs %}
{% tab title="Source" %}

```json
{
    "url": "http://example.com/api/item/{{payload.id}}",
    "response": {
        "output": {
          "id": "{{payload.id}}",
          "data": "{{body}}"
        }
    }
}
```

{% endtab %}
{% endtabs %}

### Interface

Exactly [one bundle](https://developers.make.com/custom-apps-documentation/component-blocks/interface) is generated with each incoming webhook.

### Samples

To help the users with setting up your module, provide [samples](https://developers.make.com/custom-apps-documentation/component-blocks/samples).

### Available IML variables <a href="#available-iml-variables" id="available-iml-variables"></a>

These IML variables are available for you to use everywhere in this module:

<table><thead><tr><th width="220.66668701171875" valign="top">Variable</th><th valign="top">Description</th></tr></thead><tbody><tr><td valign="top"><code>now</code></td><td valign="top">Current date and time</td></tr><tr><td valign="top"><code>environment</code></td><td valign="top">TBD</td></tr><tr><td valign="top"><code>temp</code></td><td valign="top">Contains custom variables created via the <code>temp</code> directive.</td></tr><tr><td valign="top"><code>parameters</code></td><td valign="top">Contains the module’s input parameters.</td></tr><tr><td valign="top"><code>connection</code></td><td valign="top">Contains the connection’s data collection.</td></tr><tr><td valign="top"><code>common</code></td><td valign="top">Contains the app’s common data collection.</td></tr><tr><td valign="top"><code>data</code></td><td valign="top">Contains the module’s data collection.</td></tr><tr><td valign="top"><code>scenario</code></td><td valign="top">TBD</td></tr><tr><td valign="top"><code>metadata.expect</code></td><td valign="top">Contains the module’s raw parameters array in the way you have specified it in the configuration.</td></tr><tr><td valign="top"><code>metadata.interface</code></td><td valign="top">Contains module’s raw interface array in the way you have specified it in the configuration.</td></tr></tbody></table>

Additional variables available for the response object:

<table><thead><tr><th width="203.16656494140625" valign="top">Variable</th><th valign="top">Description</th></tr></thead><tbody><tr><td valign="top"><code>output</code></td><td valign="top">When using the <code>wrapper</code> directive, the <code>output</code> variable represents the result of the <code>output</code>directive.</td></tr></tbody></table>

Additional variables available after using the `iterate` directive, i.e. in `wrapper` or `pagination` directives:

<table><thead><tr><th width="225.66668701171875" valign="top">Variable</th><th valign="top">Description</th></tr></thead><tbody><tr><td valign="top"><code>iterate.container.first</code></td><td valign="top">Represents the first item of the array you iterated.</td></tr><tr><td valign="top"><code>iterate.container.last</code></td><td valign="top">Represents the last item of the array you iterated.</td></tr></tbody></table>

Additional variables available for pagination and response objects:

<table><thead><tr><th width="152.42596435546875" valign="top">Variable</th><th valign="top">Description</th></tr></thead><tbody><tr><td valign="top"><code>body</code></td><td valign="top">Contains the body that was retrieved from the last request.</td></tr><tr><td valign="top"><code>headers</code></td><td valign="top">Contains the response headers that were retrieved from the last request.</td></tr><tr><td valign="top"><code>items</code></td><td valign="top">When iterating this variable represents the current item that is being iterated.</td></tr></tbody></table>

Additional variables available in the instant trigger:

<table><thead><tr><th width="141.0369873046875" valign="top">Variable</th><th valign="top">Description</th></tr></thead><tbody><tr><td valign="top"><code>payload</code></td><td valign="top">Represents the current webhook item that is being processed.</td></tr></tbody></table>

## Example

{% tabs %}
{% tab title="Appearance" %}

<div align="left"><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-2a3845af8ee6fabc361c1a197700390a82d0159a%2Fwebhook_sample.png?alt=media" alt="" width="544"></div>
{% endtab %}

{% tab title="Communication" %}

```json
{}
```

{% endtab %}

{% tab title="Static parameters" %}

```json
[]
```

{% endtab %}

{% tab title="Interface" %}

```json
[
	{
		"name": "id",
		"type": "uinteger",
		"label": "User ID"
	},
	{
		"name": "email",
		"type": "email",
		"label": "Email address"
	},
	{
		"name": "name",
		"type": "text",
		"label": "Name"
	},
	{
		"name": "created",
		"type": "date",
		"label": "Date created"
	}
]
```

{% endtab %}

{% tab title="Samples" %}

```json
{
	"id": 1,
	"email": "johndoe@email.com",
	"name": "John Doe",
	"created": "2018-01-01T12:00:00.000Z"
}
```

{% endtab %}
{% endtabs %}
