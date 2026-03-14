# Source: https://developers.make.com/custom-apps-documentation/app-components/modules/action/components.md

# Components

## Communication

For more information, see the [communication documentation](https://developers.make.com/custom-apps-documentation/component-blocks/api).

* The communication `response` is extended with the `wrapper` object.
* `limit` is not available in `response` as the result of the action should always be only one bundle
* Communication can be [request-less](https://developers.make.com/custom-apps-documentation/component-blocks/api/request-less-communication).

### Static parameters

You can use [static parameters](https://developers.make.com/custom-apps-documentation/component-blocks/parameters) inside the action module without any restrictions.

### Mappable parameters

You can use [mappable parameters](https://developers.make.com/custom-apps-documentation/component-blocks/mappable-parameters) inside the action module without any restrictions.

### Interface

The action module should always [output only one bundle](https://developers.make.com/custom-apps-documentation/component-blocks/interface).

### Samples

To help the users with setting up your module, you can provide [samples](https://developers.make.com/custom-apps-documentation/component-blocks/samples).

### Scope

When using an OAuth type of connection, use the [scope](https://developers.make.com/custom-apps-documentation/component-blocks/scope) to define scopes required by this action.

### Available IML variables <a href="#available-iml-variables" id="available-iml-variables"></a>

These IML variables are available for you to use everywhere in this module:

<table><thead><tr><th width="220.66668701171875" valign="top">Variable</th><th valign="top">Description</th></tr></thead><tbody><tr><td valign="top"><code>now</code></td><td valign="top">Current date and time</td></tr><tr><td valign="top"><code>environment</code></td><td valign="top">TBD</td></tr><tr><td valign="top"><code>temp</code></td><td valign="top">Contains custom variables created via the <code>temp</code> directive.</td></tr><tr><td valign="top"><code>parameters</code></td><td valign="top">Contains the module’s input parameters.</td></tr><tr><td valign="top"><code>connection</code></td><td valign="top">Contains the connection’s data collection.</td></tr><tr><td valign="top"><code>common</code></td><td valign="top">Contains the app’s common data collection.</td></tr><tr><td valign="top"><code>data</code></td><td valign="top">Contains the module’s data collection.</td></tr><tr><td valign="top"><code>scenario</code></td><td valign="top">TBD</td></tr><tr><td valign="top"><code>metadata.expect</code></td><td valign="top">Contains the module’s raw parameters array in the way you have specified it in the configuration.</td></tr><tr><td valign="top"><code>metadata.interface</code></td><td valign="top">Contains module’s raw interface array in the way you have specified it in the configuration.</td></tr></tbody></table>

Additional variables available for the response object:

<table><thead><tr><th width="130.573974609375" valign="top">Variable</th><th valign="top">Description</th></tr></thead><tbody><tr><td valign="top"><code>output</code></td><td valign="top">When using the <code>wrapper</code> directive, the <code>output</code> variable represents the result of the <code>output</code>directive.</td></tr></tbody></table>

Additional variables available after using the `iterate` directive, i.e. in `wrapper` or `pagination` directives:

<table><thead><tr><th width="225.66668701171875" valign="top">Variable</th><th valign="top">Description</th></tr></thead><tbody><tr><td valign="top"><code>iterate.container.first</code></td><td valign="top">Represents the first item of the array you iterated.</td></tr><tr><td valign="top"><code>iterate.container.last</code></td><td valign="top">Represents the last item of the array you iterated.</td></tr></tbody></table>

Additional variables available for pagination and response objects:

<table><thead><tr><th width="153.907470703125" valign="top">Variable</th><th valign="top">Description</th></tr></thead><tbody><tr><td valign="top"><code>body</code></td><td valign="top">Contains the body that was retrieved from the last request.</td></tr><tr><td valign="top"><code>headers</code></td><td valign="top">Contains the response headers that were retrieved from the last request.</td></tr><tr><td valign="top"><code>items</code></td><td valign="top">When iterating this variable represents the current item that is being iterated.</td></tr></tbody></table>

## Action module example

{% tabs %}
{% tab title="Appearance" %}

<div align="left"><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-5c724402b36bd08c7f7ea50baa878f067dc529cd%2Faction_module.png?alt=media" alt="" width="544"></div>
{% endtab %}

{% tab title="Communication" %}

```json
{
	"url": "/api/users/create",
	"body": {
		"name": "{{parameters.name}}",
		"email": "{{lower(parameters.email)}}"
	},
	"method": "POST",
	"response": {
		"output": {
			"id": "{{body.id}}"
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
		"name": "email",
		"type": "email",
		"label": "Email address",
		"required": true
	},
	{
		"name": "name",
		"type": "text",
		"label": "Name",
		"required": true
	}
]
```

{% endtab %}

{% tab title="Interface" %}

```json
[
	{
		"name": "id",
		"type": "uinteger",
		"label": "User ID"
	}
]
```

{% endtab %}

{% tab title="Samples" %}

```json
{
	"id": 1
}
```

{% endtab %}
{% endtabs %}
