# Source: https://developers.make.com/custom-apps-documentation/component-blocks/api/request-less-communication.md

# Request-less communication

When you need the module to output some static (or computed) content, you can use the request-less/static mode by omitting the URL and specifying only the `response.output` directives.

## Specification

You can mix static definitions with normal requests and have more than two static requests.

When using this mode, the following directives are completely ignored: `method`, `qs`, `headers`, `body`, `ca`, `type`and `pagination` - almost all request-related directives.

All response-related directives, such as `response.output`, `response.wrapper`, `response.iterate` are available, as well as `response.valid` and `response.error`. However, the latter directives lose their value in static mode.

## Examples

### **Example 1**:

{% tabs %}
{% tab title="Example 1 " %}

```json
{
    "response": {
        "output": {
            "id": "{{parameters.itemId}}",
            "text": "[{{parameters.itemId}}] {{parameters.text}}"
        }
    }
}
```

{% endtab %}

{% tab title="Example 2" %}

```json
[
  {
    "condition": "{{parameters.mode == 'self'}}",
    "response": {
      "output": {
        "text": "No items"
      }
    }
  },
  {
    "condition": "{{parameters.mode != 'self'}}",
    "response": {
      "output": {
        "text": "Some items found"
      }
    }
  }
]
```

{% hint style="info" %}
Includes different outputs depending on condition.
{% endhint %}
{% endtab %}
{% endtabs %}
