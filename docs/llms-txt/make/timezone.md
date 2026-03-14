# Source: https://developers.make.com/custom-apps-documentation/block-elements/parameters/timezone.md

# Timezone

## Specification

### editable

* Type: `Boolean`
* If `true`, the user can manually edit (map) a time zone. The time zone name must be valid.

## Example

### Basic timezone input

By default, the `timezone` parameter is displayed as `select` with all available time zones as options.

{% tabs %}
{% tab title="Appearance" %}

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-3d510e12965bdb592e0f973996256ff2882eb857%2Ftimezone_para.png?alt=media" alt="" width="538"><figcaption></figcaption></figure></div>
{% endtab %}

{% tab title="Source" %}

```json
[
	{
		"name": "timezone",
		"type": "timezone",
		"label": "Time zone"
	}
]
```

{% endtab %}
{% endtabs %}
