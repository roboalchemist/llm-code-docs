# Source: https://developers.make.com/custom-apps-documentation/block-elements/parameters/timestamp.md

# Timestamp

## Specification

### nested

Available types:

<table><thead><tr><th width="109">Type</th><th>Specification</th></tr></thead><tbody><tr><td><strong>array</strong></td><td>Provides an array of nested parameters that are shown when the value of the parameter is set (value is not empty)</td></tr><tr><td><strong>string</strong></td><td>Provides a URL address of an RPC to load a list of nested parameters.</td></tr><tr><td><strong>object</strong></td><td>Provides a detailed specification of nested parameters.</td></tr></tbody></table>

{% tabs %}
{% tab title="Use of nested fields" %}

```json
{
    "name": "myTimestamp",
    "type": "timestamp",
    "label": "My Timestamp",
    "nested": "rpc://getNestedFields"
}
```

{% endtab %}
{% endtabs %}

## Example

### Basic timestamp input

The value from the timestamp input is validated as a UNIX timestamp. If it doesn't match the UNIX timestamp pattern, the validation will fail.

{% tabs %}
{% tab title="Appearance" %}

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-0b3d24beeca45b73fd0bad344392c27551c2a645%2Ftimestamp2.png?alt=media" alt="" width="546"><figcaption></figcaption></figure></div>
{% endtab %}

{% tab title="Source" %}

```json
[
	{
		"label": "Timestamp",
		"name": "timestamp",
		"type": "timestamp"
	}
]
```

{% endtab %}

{% tab title="Output" %}

```javascript
1536593945
```

{% endtab %}
{% endtabs %}
