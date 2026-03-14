# Source: https://developers.make.com/custom-apps-documentation/block-elements/parameters/number.md

# Number

## Specification

### validate

* Type: `Object`
* Specifies parameter validation

Available parameters:

<table><thead><tr><th width="130" valign="top">Parameter</th><th width="92" valign="top">Type</th><th valign="top">Specification</th></tr></thead><tbody><tr><td valign="top"><strong>max</strong></td><td valign="top">number</td><td valign="top">Specifies the maximum numeric value.</td></tr><tr><td valign="top"><strong>min</strong></td><td valign="top">number</td><td valign="top">Specifies the minimum numeric value.</td></tr></tbody></table>

### nested

Available types:

<table><thead><tr><th width="109" valign="top">Type</th><th valign="top">Specification</th></tr></thead><tbody><tr><td valign="top"><strong>array</strong></td><td valign="top">Provides an array of nested parameters that are shown when the value of the parameter is set (value is not empty)</td></tr><tr><td valign="top"><strong>string</strong></td><td valign="top">Provides the URL address of an RPC to load the list of nested parameters.</td></tr><tr><td valign="top"><strong>object</strong></td><td valign="top">Provides a detailed specification of nested parameters.</td></tr></tbody></table>

{% tabs %}
{% tab title="Use of nested fields" %}

```json
{
    "name": "myNumber",
    "type": "number",
    "label": "My Number",
    "nested": "rpc://getNestedFields"
}
```

{% endtab %}
{% endtabs %}

## Example

### Basic numeric input

{% tabs %}
{% tab title="Appearance" %}

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-7b602c496edc9016c460ff49fc454cb0e5966ddc%2Fnumber2.png?alt=media" alt="" width="540"><figcaption></figcaption></figure></div>
{% endtab %}

{% tab title="Source" %}

```json
[
	{
		"name": "temperature",
		"label": "Enter the target temperature",
		"type": "number"
	}
]
```

{% endtab %}

{% tab title="Output" %}

```json
12.345
```

{% endtab %}
{% endtabs %}

{% hint style="info" %}
For more examples, see the [Integer/Uinteger parameter specification](https://developers.make.com/custom-apps-documentation/block-elements/parameters/integer-uinteger).
{% endhint %}
