# Source: https://developers.make.com/custom-apps-documentation/block-elements/parameters/port.md

# Port

## Specification

### validate

* Type: `Object`
* Specifies parameter validation.

Available parameters:

<table><thead><tr><th width="119" valign="top">Parameter</th><th width="92" valign="top">Type</th><th valign="top">Specification</th></tr></thead><tbody><tr><td valign="top"><strong>max</strong></td><td valign="top">number</td><td valign="top">Specifies the maximum numeric value.</td></tr><tr><td valign="top"><strong>min</strong></td><td valign="top">number</td><td valign="top">Specifies the minimum numeric value.</td></tr></tbody></table>

### nested

Available types:

<table><thead><tr><th width="109" valign="top">Type</th><th valign="top">Specification</th></tr></thead><tbody><tr><td valign="top"><strong>array</strong></td><td valign="top">Provides an array of nested parameters that are shown when the value of the parameter is set (value is not empty).</td></tr><tr><td valign="top"><strong>string</strong></td><td valign="top">Provides the URL address of an RPC to load the list of nested parameters.</td></tr><tr><td valign="top"><strong>object</strong></td><td valign="top">Provides a detailed specification of nested parameters.</td></tr></tbody></table>

{% tabs %}
{% tab title="Use of nested fields" %}

```json
{
    "name": "myPort",
    "type": "port",
    "label": "My Port",
    "nested": "rpc://getNestedFields"
}
```

{% endtab %}
{% endtabs %}

## Example

### Basic numeric input

{% tabs %}
{% tab title="Appearance" %}

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-3775ac02e70a8142e51d2b70b2e8f62e6f568e08%2Fport2.png?alt=media" alt="" width="546"><figcaption></figcaption></figure></div>
{% endtab %}

{% tab title="Source" %}

```json
[
	{
		"name": "port",
		"label": "Port",
		"type": "port"
	}
]
```

{% endtab %}
{% endtabs %}

{% hint style="info" %}
For more examples, see the [Integer/Uinteger parameter specification](https://developers.make.com/custom-apps-documentation/block-elements/parameters/integer-uinteger).
{% endhint %}
