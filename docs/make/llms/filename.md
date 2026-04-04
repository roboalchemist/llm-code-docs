# Source: https://developers.make.com/custom-apps-documentation/block-elements/parameters/filename.md

# Filename

## Specification

### extension

* Type: `String or Array`.
* Allowed extension or array of allowed extensions.

### nested

Available types:

<table><thead><tr><th width="109" valign="top">Type</th><th valign="top">Specification</th></tr></thead><tbody><tr><td valign="top"><strong>array</strong></td><td valign="top">Provides an array of nested parameters that are shown when the value of the parameter is set (value is not empty).</td></tr><tr><td valign="top"><strong>string</strong></td><td valign="top">Provides the URL address of an RPC to load the list of nested parameters.</td></tr><tr><td valign="top"><strong>object</strong></td><td valign="top">Provides a detailed specification of nested parameters.</td></tr></tbody></table>

{% tabs %}
{% tab title="Use of nested fields" %}

```json
{
    "name": "myFilename",
    "type": "filename",
    "label": "My Filename",
    "nested": "rpc://getNestedFields"
}
```

{% endtab %}
{% endtabs %}

## Examples

### File input

When combined with `filename` parameter, the buffer can be used for a file input dialog.

{% tabs %}
{% tab title="Appearance" %}

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-b5650308973f7d4ea0f4e8bcc5d0b1aeae67c8b1%2Ffilename1.png?alt=media" alt="" width="563"><figcaption></figcaption></figure></div>
{% endtab %}

{% tab title="Source" %}

```json
[
	{
		"name": "fileName",
		"type": "filename",
		"label": "File name",
		"semantic": "file:name"
	},
	{
		"name": "data",
		"type": "buffer",
		"label": "Data",
		"semantic": "file:data"
	}
]
```

{% endtab %}
{% endtabs %}

### Allowed file extensions

Restrict allowed extensions by adding `extension` option.

{% tabs %}
{% tab title="Appearance" %}

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-5fee9333c5992ccac41ba305354f226b4306a2a0%2Ffilename2.png?alt=media" alt="" width="563"><figcaption></figcaption></figure></div>
{% endtab %}

{% tab title="Source" %}

```json
[
	{
		"name": "fileName",
		"type": "filename",
		"label": "File name",
		"semantic": "file:name",
		"extension": ["jpg", "bmp", "png"],
		"help": "Only files with the following extensions are allowed: `jpg`, `bmp`, `png`."
	},
	{
		"name": "data",
		"type": "buffer",
		"label": "Data",
		"semantic": "file:data"
	}
]
```

{% endtab %}
{% endtabs %}
