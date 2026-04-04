# Source: https://developers.make.com/custom-apps-documentation/block-elements/parameters/boolean.md

# Boolean

## Specification

### nested

Available types:

<table><thead><tr><th width="145.6666259765625" valign="top">Type</th><th valign="top">Specification</th></tr></thead><tbody><tr><td valign="top"><strong>array</strong></td><td valign="top">Provides an array of nested parameters that are shown when the value of the parameter is true (the checkbox is checked).</td></tr><tr><td valign="top"><strong>string</strong></td><td valign="top">Provides the URL address of an RPC to load list of nested parameters.</td></tr><tr><td valign="top"><strong>object</strong></td><td valign="top">Provides a detailed specification of nested parameters.</td></tr></tbody></table>

### editable (deprecated)

* Type: `Boolean`
* Default: `false`
* If set to `true` , the user can map (or manually edit) the value of the parameter.

## Example

### Basic Boolean

A basic Boolean offers three options: `true`, `false` and `undefined`.

{% tabs %}
{% tab title="Appearance" %}

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-d21927dc095a5152dcfa2632281494634ad8e5aa%2Fboolean1a.png?alt=media" alt="" width="542"><figcaption></figcaption></figure></div>
{% endtab %}

{% tab title="Source" %}

```json
[
	{
		"type": "boolean",
		"label": "My Boolean",
		"name": "myBoolean"
	}
]
```

{% endtab %}
{% endtabs %}

### Checkbox style

You can turn the radio buttons into a checkbox by adding a `"required": true` property. Additionally, you can set the default state by setting the `default` property.

{% tabs %}
{% tab title="Appearance" %}

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-bae03a4b89ddce1f92827e7d94f70128521202c7%2Fboolean2a.png?alt=media" alt="" width="539"><figcaption></figcaption></figure></div>
{% endtab %}

{% tab title="Source" %}

```json
[
	{
		"type": "boolean",
		"label": "Enable this feature?",
		"name": "enable",
		"required": true
	},
	{
		"type": "boolean",
		"label": "Subscribe?",
		"name": "subscribe",
		"required": true,
		"default": true
	}
]
```

{% endtab %}
{% endtabs %}

### Nested parameters

By adding nested fields, you can add fields that will be shown to the user if this field’s value is `true`.

{% tabs %}
{% tab title="Appearance 1" %}

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-b5488053cf98a650a5ce45a027c9cdb73900a17a%2Fboolean3a.png?alt=media" alt="" width="535"><figcaption><p>Boolean set to false</p></figcaption></figure></div>
{% endtab %}

{% tab title="Appearance 2" %}

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-551ecd4d114e76a2769f3cb9a472e58116793a6d%2Fboolean3b.png?alt=media" alt="" width="541"><figcaption><p>Boolean set to true</p></figcaption></figure></div>
{% endtab %}

{% tab title="Source" %}

```json
[
 {
    "name": "myBoolean",
    "type": "boolean",
    "label": "My Boolean",
    "nested": [
        {
            "name": "nestedField1",
            "type": "text",
            "label": "Nested Field 1"
        },
        {
            "name": "nestedField2",
            "type": "text",
            "label": "Nested Field 2"
        }
    ]
  }
]
```

{% endtab %}
{% endtabs %}

### Editable (deprecated)

{% hint style="info" %}
Since **Apps platform version 2**, all Booleans have set `mappable`(editable) to `true` by default.
{% endhint %}

You can allow mapping to the field by setting `editable` to `true`.

{% tabs %}
{% tab title="Appearance" %}

<div align="left"><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-25b0d91440b92aa5f2f017426752188bb2c33956%2Fboolean_editable.png?alt=media" alt="" width="563"></div>
{% endtab %}

{% tab title="Source" %}

```json
[
	{
		"type": "boolean",
		"label": "Editable boolean",
		"name": "myBoolean",
		"editable": true
	}
]
```

{% endtab %}
{% endtabs %}
