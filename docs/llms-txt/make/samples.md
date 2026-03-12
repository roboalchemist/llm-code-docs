# Source: https://developers.make.com/custom-apps-documentation/component-blocks/samples.md

# Samples

## Specification

Samples are used to provide a sample of the outgoing bundle.

## Static samples

You can define the samples manually.

{% tabs %}
{% tab title="Appearance" %}

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-b4ace1a21a8a4ff7e15dca1f598126bd88829dd0%2Fstatic_samples.png?alt=media" alt="" width="563"><figcaption></figcaption></figure></div>
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
		"label": "Email"
	},
	{
		"name": "name",
		"type": "text",
		"label": "Name"
	}
]
```

{% endtab %}

{% tab title="Samples" %}

```json
{
	"id": 1399,
	"email": "johndoe@email.com",
	"name": "John Doe"
}
```

{% endtab %}
{% endtabs %}

## Dynamic samples

See [Samples RPC ](https://developers.make.com/custom-apps-documentation/app-components/rpcs#samples-rpc)for information on how to specify dynamic sample data.
