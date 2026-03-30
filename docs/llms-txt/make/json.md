# Source: https://developers.make.com/custom-apps-documentation/block-elements/parameters/json.md

# JSON

## Specification

This type of parameter has no extra options.

It acts as a multi-line text field to the user, with one notable difference: the module automatically converts the input to a JSON object. So if you map `"{{parameters.myJsonField}}"` in Communication, that value will be an object (or array).

If the provided value is not valid JSON, the module throws a validation error.

### Example

#### JSON input

{% tabs %}
{% tab title="Appearance" %}

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-85de7202ed97844953932a212157cd302848e973%2Fjson.png?alt=media" alt="" width="555"><figcaption></figcaption></figure></div>
{% endtab %}

{% tab title="Source" %}

```json
[
    {
        "name": "json",
        "label": "JSON",
        "type": "json"
    }
]
```

{% endtab %}
{% endtabs %}
