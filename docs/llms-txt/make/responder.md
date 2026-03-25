# Source: https://developers.make.com/custom-apps-documentation/app-components/modules/responder.md

# Responder

The responder should be used when you need to send processed data back to the service. The scenario is initiated by an instant trigger, processes the data received, and then sends the results back to the sender. The responder module has no interface; you just pass parameters in.

<div align="left"><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-670d0f1b34b0283410705575468aaae1d3cc8875%2Fscreen_84.png?alt=media" alt="" width="563"></div>

## Components

### Communication

Only a `response` directive is available inside the [communication](https://developers.make.com/custom-apps-documentation/component-blocks/api). Unlike with most modules, where `response` handles the data that comes from the API, in this case `response` defines what the webhook (instant trigger) should send back to the external platform that called it.

### Static Parameters

You can use [static parameters](https://developers.make.com/custom-apps-documentation/component-blocks/parameters) inside the responder module without any restrictions.

### Mappable Parameters

You can use [mappable parameters](https://developers.make.com/custom-apps-documentation/component-blocks/mappable-parameters) inside the responder module without any restrictions.

## Responder example

{% tabs %}
{% tab title="Appearance" %}

<div align="left"><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-19a0b3a5d530e3e31cd1da6322d6cbcf546d5725%2Fresponder.png?alt=media" alt="" width="563"></div>
{% endtab %}

{% tab title="Communication" %}

```json
{
	"response": {
		"body": {
			"text": "{{parameters.text}}"
		},
		"status": 200,
		"headers": {
			"content-type": "application/json"
		}
	}
}
```

{% endtab %}

{% tab title="Static Parameters" %}

```json
[]
```

{% endtab %}

{% tab title="Mappable Parameters" %}

```json
[
	{
		"name": "text",
		"type": "text",
		"label": "Message"
	}
]
```

{% endtab %}
{% endtabs %}
