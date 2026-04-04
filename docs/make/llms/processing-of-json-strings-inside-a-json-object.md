# Source: https://developers.make.com/custom-apps-documentation/component-blocks/api/processing-of-json-strings-inside-a-json-object.md

# Processing of JSON strings inside a JSON object

In Make, JSON-based APIs are natively supported. Nevertheless, some APIs may have a JSON string inside a JSON object.

If an API returns a JSON string inside a JSON object, the data inside a JSON string is treated as text and the child parameters cannot be directly mapped.

However, if the API requires a parameter in JSON string format, Make has to send it in the required format.

{% tabs %}
{% tab title="Occurrence in a module" %}

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-8d7cbe540e835a27291087c6e8d28c140d4e4257%2Fjson_inside_json.png?alt=media" alt="" width="563"><figcaption></figcaption></figure></div>

{% hint style="info" %}
Note the `address` parameter. Since the parameter is a JSON string, the content is not parsed as a collection.
{% endhint %}
{% endtab %}

{% tab title="JSON String" %}

```json
{
    "address": "{\"zip\":\"18000\",\"city\":\"Prague\",\"state\":\"Czechia\",\"country\":\"Czechia\",\"address1\":\"Menclova 2\"}",
    "id": "123",
    "name": "Make Office"
}
```

{% hint style="info" %}
Example of an `address` parameter that has a value in the JSON string format.
{% endhint %}
{% endtab %}
{% endtabs %}

## Create a JSON String

If the API requires a parameter to be sent as a JSON string, the `createJSON()` function can be used.

{% tabs %}
{% tab title="Communication" %}

```json
{
    ...
	"body": {
		"{{...}}": "{{omit(parameters, 'address')}}",
		"address": "{{createJSON(parameters.address)}}"
	},
    ...
}
```

{% hint style="info" %}
The `createJSON()` function is used to format the `address` value to a JSON strin&#x67;**.**
{% endhint %}
{% endtab %}

{% tab title="Request body" %}

```json
{
    "address": "{\"zip\":\"18000\",\"city\":\"Prague\",\"state\":\"Czechia\",\"country\":\"Czechia\",\"address1\":\"Menclova 2\"}",
    "id": "123",
    "name": "Make Office"
}
```

{% hint style="info" %}
The `address` parameter is sent in JSON string format.
{% endhint %}
{% endtab %}
{% endtabs %}

## Parse a JSON String

If the API output contains a parameter in a JSON string format, the `parseJSON()` function can be used.

{% tabs %}
{% tab title="Communication" %}

```json
{
    ...
	"output": {
		"{{...}}": "{{omit(body, 'address')}}",
		"address": "{{parseJSON(body.address)}}"
	},
    ...
}
```

{% hint style="info" %}
The `parseJSON()` function is used to parse the `address` value to JSON.
{% endhint %}
{% endtab %}

{% tab title="Raw response body" %}

```json
{
    "address": "{\"zip\":\"18000\",\"city\":\"Prague\",\"state\":\"Czechia\",\"country\":\"Czechia\",\"address1\":\"Menclova 2\"}",
    "id": "123",
    "name": "Make Office"
}
```

{% hint style="info" %}
If the `parseJSON()` function is not used, the JSON string is returned in a raw format.
{% endhint %}
{% endtab %}

{% tab title="Parsed response body" %}

```json
[
    {
        "address": {
            "zip": "18000",
            "city": "Prague",
            "state": "Czechia",
            "country": "Czechia",
            "address1": "Menclova 2"
        },
        "id": "123",
        "name": "Make Office"
    }
]
```

{% hint style="info" %}
If the `parseJSON()` function is used, the value in `address` parameter is parsed to JSON. The `address` parameter is returned as a collection.
{% endhint %}
{% endtab %}
{% endtabs %}
