# Source: https://developers.make.com/custom-apps-documentation/block-elements/parameters/cert.md

# Cert

## Specification

This type of parameter has no extra options.

## Example

### Certificate Input

If your service requires providing a certificate in PEM format, you can use the `cert` parameter. It's possible to paste a PEM string into the file or you can extract it directly from a P12 or PFX file.

{% tabs %}
{% tab title="Appearance" %}

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-1e050421e1994efe84cffc095a61070f2919c16b%2Fcert.png?alt=media" alt="" width="563"><figcaption></figcaption></figure></div>
{% endtab %}

{% tab title="Source" %}

```json
[
	{
		"name": "cert",
		"label": "Certificate",
		"type": "cert"
	}
]
```

{% endtab %}
{% endtabs %}
