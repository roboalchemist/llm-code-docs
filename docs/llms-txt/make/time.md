# Source: https://developers.make.com/custom-apps-documentation/block-elements/parameters/time.md

# Time

## Specification

### nested

Available types:

<table><thead><tr><th width="146.77777099609375">Type</th><th>Specification</th></tr></thead><tbody><tr><td><strong>array</strong></td><td>Provides an array of nested parameters that are shown when the value of the parameter is set (value is not empty).</td></tr><tr><td><strong>string</strong></td><td>Provides the URL address of an RPC to load list of nested parameters.</td></tr><tr><td><strong>object</strong></td><td>Provides a detailed specification of nested parameters.</td></tr></tbody></table>

{% tabs %}
{% tab title="Use of nested fields" %}

```json
{
    "name": "myTime",
    "type": "time",
    "label": "My Time",
    "nested": "rpc://getNestedFields"
}
```

{% endtab %}
{% endtabs %}

## Example

### Basic time input

The time field expects a time entry in `hh:mm` format.

{% tabs %}
{% tab title="Appearance" %}

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-df74e7bf14270767c9d82b381ac67a50cd7e16ef%2Ftime2.png?alt=media" alt="" width="542"><figcaption></figcaption></figure></div>
{% endtab %}

{% tab title="Source" %}

```json
[
	{
		"label": "Time",
		"name": "time",
		"type": "time"
	}
]
```

{% endtab %}
{% endtabs %}
