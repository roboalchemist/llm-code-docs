# Source: https://developers.make.com/custom-apps-documentation/block-elements/parameters/pkey.md

# Pkey

## Specification

This type of parameter has no extra options.

## Example

### Private key input

If your service requires providing a private key in PEM format, you can use the `pkey` parameter. It's possible to paste a PEM string into the file or you can extract it directly from a P12 or PFX file.

{% tabs %}
{% tab title="Appearance" %}

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-37ea02435e33d45e4f41f4a89a6c9d4c2215cfee%2Fpkay2.png?alt=media" alt="" width="563"><figcaption></figcaption></figure></div>
{% endtab %}

{% tab title="Source" %}

```json
[
	{
		"name": "pkey",
		"label": "Private key",
		"type": "pkey"
	}
]
```

{% endtab %}
{% endtabs %}
