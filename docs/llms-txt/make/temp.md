# Source: https://developers.make.com/custom-apps-documentation/component-blocks/api/handling-responses/temp.md

# Temp

**Required**: no

The `temp` directive in the `response` section specifies an object that can be used to create custom temporary variables. It also creates a `temp` variable in IML through which you then access your variables. The `temp` collection is not persisted and is lost after the module execution is complete.

This directive is executed after the request has been made, but prior to everything else in the `response` section: `condition`, `iterate`, `output` or any other `response` directive.

When you have multiple requests, this directive is also useful for passing values between requests.

{% tabs %}
{% tab title="Source" %}

```json
[
    {
        "temp": {
            "foo": "bar"
        },
        "response": {
            "temp": {
                "foo": "baz",
                "hello": "world"
            }
        }
    },
    {
        "temp": {
            "param1": "bar-{{temp.foo}}", // will be "bar-baz"
            "param2": "hello, {{temp.hello}}" // will be "hello, world"
        },
        "response": {
            "temp": {} // will have the following properties:
                       // temp.foo == "baz"
                       // temp.hello == "world"
                       // temp.param1 == "bar-baz"
                       // temp.param2 == "hello, world"
        }
    }
]
```

{% hint style="info" %}
When specifying `temp` directives in different requests and in the `response` section, the contents of the `temp` collection are not overwritten, but instead merged.
{% endhint %}
{% endtab %}
{% endtabs %}
