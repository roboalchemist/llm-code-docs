# Source: https://developers.make.com/custom-apps-documentation/component-blocks/api/handling-responses/valid.md

# Valid

**Required**: no\
**Default**: `true`

This directive lets you decide whether the HTTP response returned by a service is valid or not. If this directive is not present, the response is considered always valid when the status code is between 200 and 399 (inclusive).

Some services might return an HTTP status code >= 400 if there is an error. These are handled by standard [error handling](https://developers.make.com/custom-apps-documentation/app-components/base/error-handling). But some services might return an HTTP status code < 400 (mostly the HTTP 200) and indicate an error in the response body or headers. In that case, it makes no sense to output anything from the module, but instead indicate that there is an error.

## Behavior

* If the `valid` directive evaluates to a false value (`false`, `undefined`, `null`, etc.), module execution stops and Make throws an error. The execution log will display either your custom error message or a fallback message.
* If the `valid` directive resolves to a truthy value, the module will continue execution normally.

### Basic usage examples

Both of the following forms are equivalent. You can define `valid` as as simple condition (`valid": "{{!body.error}}`) or as an object within a condition property plus optional message and type.

{% tabs %}
{% tab title="Example 1" %}

```jsonc
{
    "response": {
        "valid": {
            "condition": "{{!body.error}}"
            // Causes error 'Response marked as invalid.' if `error` property exists in HTTP json response body.
        }
    }
}
```

{% endtab %}

{% tab title="Example 2" %}

```jsonc
{
    "response": {
        "valid": "{{!body.error}}"
        // Causes error 'Response marked as invalid.' if `error` property exists in HTTP json response body.
    }
}
```

{% endtab %}
{% endtabs %}

## Custom error message

It is also possible to define an expected error message in this way:

{% tabs %}
{% tab title="Custom error message" %}

```json
{
    "response": {
        "valid": {
            "condition": "{{!body.error}}",
            "message": "Service returned HTTP {{statusCode}} with error: {{body.error}}",
            "type": "UnknownError" // `RuntimeError` is the default, if type is not specified
        }
    }
}
```

{% hint style="info" %}
If no type is specified, the default `RuntimeError` is used. In the example above, setting "`type": "UnknownError"` overrides this default.
{% endhint %}
{% endtab %}
{% endtabs %}

## Fallback error messages

{% tabs %}
{% tab title="Fallback error message" %}

```json
{
    "response": {
            "valid": {
                "condition": "{{body.status != 'error'}}"
                // `message` not specified here, so fallback to `response.error.200` is used
            },
            "error": {
                "200": {
                    "message": "Service returned error: {{body.message}}"
                }
            }
        }
}
```

{% hint style="info" %}
The `response.error.<statusCode>` directive is used as a fallback if `valid.message` is not specified.
{% endhint %}
{% endtab %}
{% endtabs %}

{% tabs %}
{% tab title="Source" %}

```json
{
    "response": {
            "valid": {
                "condition": "{{body.status != 'error'}}"
                // `message` not specified here, so `response.error.200` is tried as fallback
            },
            // `200: {...}` code specific error directive also not specified, so generic `response.error` is used as fallback
            "error": {
                "message": "Service returned invalid status '{{body.status}}'."
            }
        }
}
```

{% hint style="info" %}
The `response.error` directive is used as a fallback if `valid.message` and `response.error.<statusCode>` are not specified.
{% endhint %}
{% endtab %}
{% endtabs %}

The priority of error message resolution is as follows. The first matching is used, the rest are ignored.

1. Directive `response.valid.message`
2. Directive `response.error.<statusCode>.message`
3. Directive `response.error.message`
4. Static message: `Response marked as invalid.`

## Error type resolution

The priority of error type resolution is the same as for error `message` above:

1. Directive `response.valid.type`
2. Directive `response.error.<statusCode>.type`
3. Directive `response.error.type`
4. Default type: `RuntimeError`
