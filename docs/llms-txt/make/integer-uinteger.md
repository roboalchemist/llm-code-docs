# Source: https://developers.make.com/custom-apps-documentation/block-elements/parameters/integer-uinteger.md

# Integer, Uinteger

## Specification

### validate

* Type: `Object`
* Specifies parameter validation

Available parameters:

<table><thead><tr><th width="130">Parameter</th><th width="92">Type</th><th>Specification</th></tr></thead><tbody><tr><td><strong>max</strong></td><td>number</td><td>Specifies the maximum numeric value.</td></tr><tr><td><strong>min</strong></td><td>number</td><td>Specifies the minimum numeric value.</td></tr></tbody></table>

### nested

Available types:

<table><thead><tr><th width="149" valign="top">Type</th><th valign="top">Specification</th></tr></thead><tbody><tr><td valign="top"><strong>array</strong></td><td valign="top">Provides an array of nested parameters that are shown when the value of the parameter is set (value is not empty)</td></tr><tr><td valign="top"><strong>string</strong></td><td valign="top">Provides the URL address of an RPC to load a list of nested parameters.</td></tr><tr><td valign="top"><strong>object</strong></td><td valign="top">Provides a detailed specification of nested parameters.</td></tr></tbody></table>

{% tabs %}
{% tab title="Use of nested fields" %}

```json
{
    "name": "myInteger",
    "type": "integer",
    "label": "My Integer",
    "nested": "rpc://getNestedFields"
}
```

{% endtab %}
{% endtabs %}

## Examples

### Basic integer and uinteger input

{% tabs %}
{% tab title="Appearance" %}

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-799145cdc687b56b541c58c04a0259d2ca5f18d4%2Finteger2b.png?alt=media" alt="" width="544"><figcaption></figcaption></figure></div>
{% endtab %}

{% tab title="Source" %}

```json
[
	{
		"name": "wholenumber",
		"label": "Enter a whole number",
		"type": "integer"
	},
	{
		"name": "positivewholenumber",
		"label": "Enter a positive whole number",
		"type": "uinteger"
	}
]
```

{% endtab %}
{% endtabs %}

### Set minimum and maximum value

{% tabs %}
{% tab title="Appearance" %}

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-7370ce8338c324a6803e2067d1aaa77badfe21ca%2Finteger2a.png?alt=media" alt="" width="543"><figcaption></figcaption></figure></div>
{% endtab %}

{% tab title="Source" %}

```json
[
	{
		"name": "thinking",
		"label": "Input a number from 1 to 10",
		"type": "integer",
		"validate": {
			"min": 1,
			"max": 10
		}
	}
]
```

{% endtab %}
{% endtabs %}
