# Source: https://developers.make.com/custom-apps-documentation/block-elements/parameters/path.md

# Path

The `path` parameter type is used for validating paths. However, no validation is performed. Still, it's good practice to use this parameter for paths.

## Specification

This type of parameter has no extra options.

## Example

### Path to a file

You can prompt for a path to a file by using this type of parameter.

{% tabs %}
{% tab title="Appearance" %}

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-9c68a515ea58967860f5ff0b7da5567f937efc63%2Fpath2.png?alt=media" alt="" width="539"><figcaption></figcaption></figure></div>
{% endtab %}

{% tab title="Source" %}

```json
[
	{
		"name": "path",
		"label": "Path to a file",
		"type": "path"
	}
]
```

{% endtab %}
{% endtabs %}
