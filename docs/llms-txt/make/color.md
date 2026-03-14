# Source: https://developers.make.com/custom-apps-documentation/block-elements/parameters/color.md

# Color

## Specification

### nested

Available types:

<table><thead><tr><th width="129.83331298828125">Type</th><th>Specification</th></tr></thead><tbody><tr><td><strong>array</strong></td><td>Provides an array of nested parameters that are shown when the value of the parameter is set (value is not empty).</td></tr><tr><td><strong>string</strong></td><td>Provides the URL address of an RPC to load a list of nested parameters.</td></tr><tr><td><strong>object</strong></td><td>Provides a detailed specification of nested parameters.</td></tr></tbody></table>

{% tabs %}
{% tab title="Use of nested fields" %}

```json
{
    "name": "myColor",
    "type": "color",
    "label": "My Color",
    "nested": "rpc://getNestedFields"
}
```

{% endtab %}
{% endtabs %}

## Example

### Color input

Color input accepts three or six hexadecimal characters prefixed with `#`.

{% tabs %}
{% tab title="Appearance" %}

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-504f3806e455e2354ee472af0946b47b9e29d33e%2Fcolor2.png?alt=media" alt="" width="544"><figcaption><p>Example of an incorrect color input</p></figcaption></figure></div>
{% endtab %}

{% tab title="Source" %}

```json
[
	{
		"name": "color",
		"type": "color",
		"label": "Color"
	}
]
```

{% endtab %}
{% endtabs %}
