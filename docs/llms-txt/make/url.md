# Source: https://developers.make.com/custom-apps-documentation/block-elements/parameters/url.md

# URL

## Specification

### nested

Available types:

<table><thead><tr><th width="139.83331298828125">Type</th><th>Specification</th></tr></thead><tbody><tr><td><strong>array</strong></td><td>Provides an array of nested parameters that are shown when the value of the parameter is set (value is not empty).</td></tr><tr><td><strong>string</strong></td><td>Provides the URL address of an RPC to load a list of nested parameters.</td></tr><tr><td><strong>object</strong></td><td>Provides a detailed specification of nested parameters.</td></tr></tbody></table>

{% tabs %}
{% tab title="Use of nested fields" %}

```json
{
    "name": "myUrl",
    "type": "url",
    "label": "My URL",
    "nested": "rpc://getNestedFields"
}
```

{% endtab %}
{% endtabs %}

## Example

The URL address is validated as `protocol://host:port/path/file?parameters#anchor`

{% tabs %}
{% tab title="Appearance" %}

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-1d8f8606ef58f65b03a597cf046a48a7402f6463%2Furl_para.png?alt=media" alt="" width="544"><figcaption><p>Validation error after an attempt to use an incorrect URL</p></figcaption></figure></div>
{% endtab %}

{% tab title="Source" %}

```json
[
	{
		"name": "url",
		"type": "url",
		"label": "URL"
	}
]
```

{% endtab %}
{% endtabs %}
