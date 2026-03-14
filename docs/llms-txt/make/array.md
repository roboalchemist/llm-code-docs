# Source: https://developers.make.com/custom-apps-documentation/block-elements/parameters/array.md

# Array

## Specification

### spec

* Describes the data structure of array items.
* Parameters inside spec use the syntax of the regular parameters.

Available types:

<table><thead><tr><th width="138" valign="top">Type</th><th valign="top">Specification</th></tr></thead><tbody><tr><td valign="top"><strong>object</strong></td><td valign="top">The output is an array of primitive types. If the object contains a <code>name</code>, it will be ignored.</td></tr><tr><td valign="top"><strong>array</strong></td><td valign="top">The output is a complex array of Objects.</td></tr></tbody></table>

{% tabs %}
{% tab title="Object" %}

```json
{
	"name": "tags",
	"spec": {
		"type": "text",
		"label": "Tag"
	},
	"type": "array",
	"label": "Tags"
}
```

{% hint style="info" %}
When no spec is provided, the array behaves as a primitive array of strings. However, the preferred approach is setting the spec to `{"type": "text"}`.
{% endhint %}
{% endtab %}

{% tab title="Array" %}

```json
{
	"name": "contacts",
	"spec": [
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
	],
	"type": "array",
	"label": "Contacts"
```

{% endtab %}
{% endtabs %}

### validate

* Type: `Object`
* Collection of validation directives.

Available parameters:

<table><thead><tr><th width="149">Parameter</th><th width="95">Type</th><th>Specification</th></tr></thead><tbody><tr><td><strong>maxItems</strong></td><td>number</td><td>Specifies the maximum length that an array parameter can have.</td></tr><tr><td><strong>minItems</strong></td><td>number</td><td>Specifies the minimum length that an array parameter can have.</td></tr><tr><td><strong>enum</strong></td><td>array</td><td>Array of allowed values in the array.</td></tr></tbody></table>

{% tabs %}
{% tab title="maxItems example" %}

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-536dbaedac1063ccecbbe52b8cd459b4fac08bc7%2Farray_maximum.png?alt=media" alt="" width="416"><figcaption></figcaption></figure></div>
{% endtab %}

{% tab title="minItems example" %}

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-2eb1fd0dab2a3f423d2c3c1aad1680b253bbd60c%2Farray_minimum.png?alt=media" alt="" width="422"><figcaption></figcaption></figure></div>
{% endtab %}

{% tab title="Error message" %}

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-077a9e0fea0e4255a4458626d70d50525c1fb2dc%2Farray_errormessage1.png?alt=media" alt="" width="365"><figcaption></figcaption></figure></div>
{% endtab %}

{% tab title="Source" %}

```json
[
	{
		"name": "members",
		"type": "array",
		"label": "Members",
		"validate": {
			"minItems": 1,
			"maxItems": 4,
			"enum": [
				"member1",
				"member2",
				"member3",
				"member4"
			]
		}
	}
]
```

{% endtab %}
{% endtabs %}

### mode

* Type: `String`
* Allowed values are `edit` and `choose`.

When the array is `editable` , you can set the default state by using `mode`.

{% tabs %}
{% tab title="Appearance" %}

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-ec9392d6945380a4bd7823fc7799fecb57f7947e%2Farray1.png?alt=media" alt="" width="542"><figcaption></figcaption></figure></div>
{% endtab %}

{% tab title="Source" %}

```json
[
	{
		"name": "choose",
		"type": "array",
		"label": "Choosable array",
		"mode": "choose"
	},
	{
		"name": "edit",
		"type": "array",
		"label": "Editable array",
		"mode": "edit"
	}
]
```

{% endtab %}
{% endtabs %}

### labels

Available parameters:

<table><thead><tr><th width="139.66668701171875" valign="top">Parameter</th><th width="95" valign="top">Type</th><th valign="top">Specification</th></tr></thead><tbody><tr><td valign="top"><strong>add</strong></td><td valign="top">string</td><td valign="top">Default: <code>Add item</code>. The text is displayed on the adding button.</td></tr></tbody></table>

## Examples

### Primitive array

The primitive array is an array of simple variables, like numbers or strings.

{% tabs %}
{% tab title="Appearance" %}

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-aaeac97d9339023a7baa4e45e8e4a1b35b9ff72e%2Farray2.png?alt=media" alt="" width="542"><figcaption></figcaption></figure></div>
{% endtab %}

{% tab title="Source" %}

```json
[
	{
		"name": "tags",
		"spec": {
			"type": "text",
			"label": "Tag"
		},
		"type": "array",
		"label": "Tags"
	}
]
```

{% endtab %}

{% tab title="Output" %}

```json
["old", "new"]
```

{% endtab %}
{% endtabs %}

### Complex array

The complex array is an array of complex objects - collections.

{% tabs %}
{% tab title="Appearance" %}

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-55f7d0812a2f2f040f0ad2abf6214add4408c5c1%2Farray3.png?alt=media" alt="" width="541"><figcaption></figcaption></figure></div>
{% endtab %}

{% tab title="Source" %}

```json
[
	{
		"name": "contacts",
		"spec": [
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
		],
		"type": "array",
		"label": "Contacts"
	}
]
```

{% endtab %}

{% tab title="Output" %}

```json
[
    {
        "name": "John Doe",
        "email": "john@doe.com"
    },
    {
        "name": "Foo Bar",
        "email": "foo@bar.baz"
    }
]
```

{% endtab %}
{% endtabs %}

### Complex array with labeled collections

{% tabs %}
{% tab title="Appearance" %}

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-ca8822898b667c88332e7940d83c9d8df6a8967b%2Farray4.png?alt=media" alt="" width="542"><figcaption></figcaption></figure></div>
{% endtab %}

{% tab title="Source" %}

```json
[
	{
		"name": "contacts",
		"spec": {
			"type": "collection",
			"label": "Contact",
			"spec": [
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
	},
		"type": "array",
		"label": "Contacts"
	}
]
```

{% endtab %}

{% tab title="Output" %}

```json
[
    {
        "name": "John Doe",
        "email": "john@doe.com"
    },
    {
        "name": "Foo Bar",
        "email": "foo@bar.baz"
    }
]
```

{% endtab %}
{% endtabs %}

### Amount of items

Use the `validate` object to set `minItems` and `maxItems` to control the minimum and/or maximum amount of items in the array.

{% tabs %}
{% tab title="Appearance" %}

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-7412fea03e45c099972eb1ce60a8d0b1400d21e6%2Farray5.png?alt=media" alt="" width="542"><figcaption></figcaption></figure></div>
{% endtab %}

{% tab title="Source" %}

```json
[
	{
		"name": "members",
		"type": "array",
		"label": "Members",
		"validate": {
			"minItems": 1,
			"maxItems": 4
		}
	}
]
```

{% endtab %}
{% endtabs %}

### Custom labels

Customize the button labels using the `labels` object.

{% tabs %}
{% tab title="Appearance" %}

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-ad10b28323b96760c502e8bcaff710c83246a274%2Farray6.png?alt=media" alt="" width="539"><figcaption></figcaption></figure></div>
{% endtab %}

{% tab title="Source" %}

```json
[
	{
		"name": "labels",
		"type": "array",
		"label": "Customized array",
		"labels": {
			"add": "Add an item to my array"
		}
	}
]
```

{% endtab %}
{% endtabs %}
