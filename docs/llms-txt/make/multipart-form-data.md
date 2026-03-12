# Source: https://developers.make.com/custom-apps-documentation/component-blocks/api/multipart-form-data.md

# Multipart/form-data

## Upload a file

A module that uploads a file to the service works with data type `buffer` in mappable parameters and type `multipart/form-data` in communication.

{% tabs %}
{% tab title="Occurrence in a Module" %}

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-b610dc11bc01083c7a8cc17fd5142cc8ba7fa344%2Fuploadfile.png?alt=media" alt="" width="563"><figcaption></figcaption></figure></div>

{% hint style="info" %}
The file input dialog is where the user can either choose the module that has a file available or manually map the file's name and data on their own.

This works only if the `buffer` is correctly implemented in [interface](#download-a-file) in preceding modules.
{% endhint %}
{% endtab %}

{% tab title="Mappable Parameters" %}

```json
[
	{
		"name": "file_name",
		"type": "text",
		"label": "Name",
		"required": true,
		"semantic": "file:name"
	},
	{
		"name": "file_data",
		"type": "buffer",
		"label": "Data",
		"required": true,
		"semantic": "file:data"
	}
]
```

{% endtab %}

{% tab title="Communication" %}

```json
{
    "url": "http://example.com",
    "body": {
        "file": {
            "value": "{{parameters.file_data}}",
            "options": {
                "filename": "{{parameters.file_name}}"
            }
        }
    },
    "type": "multipart/form-data",
    "method": "POST"
}
```

{% hint style="info" %}
The type of the request is `multipart/form-data`.
{% endhint %}
{% endtab %}
{% endtabs %}
