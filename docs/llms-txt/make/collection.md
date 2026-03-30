# Source: https://developers.make.com/custom-apps-documentation/block-elements/parameters/collection.md

# Collection

## Specification

### spec

* Type: `Array`
* Description of the collection.
* Array of parameters. Standard parameters syntax is used.

{% tabs %}
{% tab title="Example" %}

```json
{
    "name": "myCollection",
    "type": "collection",
    "label": "My Collection",
    "spec": [
        {
            "name": "email",
            "type": "email"
        },
        {
            "name": "phone",
            "type": "text"
        }
    ]
}
```

{% endtab %}
{% endtabs %}

### sequence

* Type: `Boolean`
* If set to `true` , all properties of the object will be in the same order as they are defined in the `spec`.

## Examples

### Simple collection

Create a collection by specifying its parameters in the `spec`.

{% tabs %}
{% tab title="Appearance" %}

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-d6fb96b243ff5dc342c392c86944aa1f252c08e5%2Fcollection1a.png?alt=media" alt="" width="543"><figcaption></figcaption></figure></div>
{% endtab %}

{% tab title="Source" %}

```json
[
	{
		"name": "contact",
		"spec": [
			{
				"name": "firstname",
				"type": "text",
				"label": "First name"
			},
			{
				"name": "lastname",
				"type": "text",
				"label": "Last name"
			}
		],
		"type": "collection",
		"label": "Contact"
	}
]
```

{% endtab %}

{% tab title="Output" %}

```json
{
    "contact": {
        "lastname": "Doe",
        "firstname": "Jane"
    }
}
```

{% endtab %}
{% endtabs %}

### Collection in a collection

Collections can be also nested in another collection.

{% tabs %}
{% tab title="Appearance" %}

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-fb61f078fe10ff7b6c99c0ee03ece6daca2c9d87%2Fcollection2a.png?alt=media" alt="" width="543"><figcaption></figcaption></figure></div>
{% endtab %}

{% tab title="Source" %}

```json
[
	{
		"name": "contact",
		"spec": [
			{
				"name": "firstname",
				"type": "text",
				"label": "First name"
			},
			{
				"name": "lastname",
				"type": "text",
				"label": "Last name"
			},
			{
				"name": "address",
				"label": "Address",
				"type": "collection",
				"spec": [
					{
						"label": "Street",
						"name": "street",
						"type": "text"
					},
					{
						"label": "City",
						"name": "city",
						"type": "text"
					}
				]
			}
		],
		"type": "collection",
		"label": "Contact"
	}
]
```

{% endtab %}

{% tab title="Output" %}

```json
{
    "contact": {
        "address": {
               "city": "Prague",
               "street": "Novakovych"
         },
        "lastname": "Doe",
        "firstname": "Jane"
    }
}
```

{% endtab %}
{% endtabs %}
