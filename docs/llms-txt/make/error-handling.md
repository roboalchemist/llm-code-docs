# Source: https://developers.make.com/custom-apps-documentation/app-components/base/error-handling.md

# Source: https://developers.make.com/custom-apps-documentation/best-practices/base/error-handling.md

# Error handling

It is important to implement [error handling](https://developers.make.com/custom-apps-documentation/app-components/base/error-handling) in your app so your users clearly understand the cause of the error.

Each service sends an error message when an error occurs. This usually happens when the request has wrong parameters or values or when the service has an outage.

When an error occurs, the module should indicate the error as well as a detailed message that can then be used in filters. The message should be clear and user-friendly. For example, instead of "Error: contact\_not\_found", your message should be "\[404] The specified contact was not found."

The error handling code should correspond to the structure of the server response.

## Error handling example

In this example, the JSON response has the following format in cases where something goes wrong:

{% tabs %}
{% tab title="JSON response" %}

```json
{
    "error": {
        "code": "E101",
        "message": "The company with the given ID does not exist."
    }
}
```

{% endtab %}
{% endtabs %}

Here's how the error section should (and should not) look:

{% tabs %}
{% tab title="Correct" %}

```javascript
"response": {
    "error": {
        "message": "[{{statusCode}}] {{body.error.message}} (error code: {{body.error.code}})"
    }
}
```

{% hint style="info" %}
The error object in this example contains the `code` and `message` fields. It is also important to show the status code of the error. This can be accessed using the `statusCode` keyword. In the case of HTTP error 400, for example, the error message could look like this:

`[400] The company with the given ID does not exist. (error code: E101)`
{% endhint %}
{% endtab %}

{% tab title="Incorrect" %}

```javascript
"response": {
    "error": {
        "message": "{{body.error.text}}"
    }
}
```

{% hint style="info" %}
The error object in this example contains the `code` and `message` fields, but not a `text` field.
{% endhint %}
{% endtab %}
{% endtabs %}

## Common error messages

### 4xx: Client Error <a href="#id-4xx-client-error" id="id-4xx-client-error"></a>

[4xx errors](https://www.rfc-editor.org/rfc/rfc9110.html#name-client-error-4xx) indicate something wrong on the client side.

### 5xx: Server Error <a href="#id-5xx-server-error" id="id-5xx-server-error"></a>

[5xx errors](https://www.rfc-editor.org/rfc/rfc9110.html#name-server-error-5xx) indicate something wrong on the side of the third-party service.

## Handling status code 200

Sometimes the API returns `status code 200` with an error in the body. In this situation, use the [valid](https://developers.make.com/custom-apps-documentation/component-blocks/api/handling-responses/valid) directive, which tells whether the response should be processed or an error should be thrown.

{% hint style="info" %}
It is NOT possible to use specific HTTP code 200-399 error directives without the using [valid](https://developers.make.com/custom-apps-documentation/component-blocks/api/handling-responses/valid) directive.
{% endhint %}

Sometimes the API returns `status code 200` without errors to an incorrect request. This can happen, for example, if the **Get a/an \[item]** module is developed based on the search endpoint and not based on a separate endpoint. This may be the case if a separate endpoint for that action is not implemented on the service’s side.

{% tabs %}
{% tab title="Incorrect" %}
Incorrect example of the search approach for a Get module:

```
{
	"url": "/items",
	"method": "GET",
	"qs": {
		"id": "{{parameters.itemId}}"
	},
	"response": {
		"output": "{{body.items[1]}}"
	}
}
```

{% hint style="info" %}
If an incorrect ID is provided, this will return an empty response. It is important to validate the call's response and, if empty, return a formatted error message.
{% endhint %}
{% endtab %}

{% tab title="Correct" %}
Correct example of Search approach with validation:

```
{
	"url": "/items",
	"method": "GET",
	"qs": {
		"id": "{{parameters.itemId}}"
	},
	"response": {
		"valid": {
            "condition": "{{body.items[1].id}}",
            "message": "Item with the given id does not exist."
        },
		"output": "{{body.items[1]}}"
	}
}
```

{% hint style="info" %}
In this case, we mark the response as invalid if it has no ID, as the ID should always be returned with other data.

Note that this approach will trigger error handler from the Base, so make sure you have meaningful error messages there.
{% endhint %}
{% endtab %}
{% endtabs %}
