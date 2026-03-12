# Source: https://developers.make.com/custom-apps-documentation/app-components/rpcs/dynamic-fields-rpc.md

# Dynamic fields RPC

The dynamic fields RPC generates dynamic fields inside a module. You can do this by adding a couple of properties to the `output` with some modification to match the syntax of the app builder.

## Details to consider

* Pay attention to the `type`. For example, Make doesn't accept `"type": "string"`. In this case, you need to change it to `"type": "text"`.
* Specify the `name` for a field. Otherwise, you will not be able to access it in the communication of a module.
* Properly convert field types between your service types and Make types. One of the ways to resolve it is to use [custom IML functions](https://developers.make.com/custom-apps-documentation/app-components/iml-functions/dynamic-mappable-parameters).

The rest of the properties (like `options`, `default`, `nested`, etc.) are also available and can be used according to the selected parameter type. The only difference is that instead of creating parameters manually you create dynamic parameters.

{% tabs %}
{% tab title="Source" %}

```json
{
    "response": {
        "iterate": "{{body}}",
        "output": {
            "name": "{{item.key}}",
            "label": "{{item.label}}",
            "type": "text",
            "required": "{{item.isRequired == 1}}"
        }
    }
}
```

{% endtab %}
{% endtabs %}

## Examples

### RPC with only dynamic parameters

{% tabs %}
{% tab title="Source" %}

```json
[
    "rpc://nameOfMyRemoteProcedure"
]
```

{% hint style="info" %}
You might need to implement a [custom IML function](https://developers.make.com/custom-apps-documentation/app-components/iml-functions/dynamic-mappable-parameters) if the service types of fields don't match with Make types.
{% endhint %}
{% endtab %}
{% endtabs %}

### RPC with custom fields (additional dynamic parameters)

{% tabs %}
{% tab title="Source" %}

```json
[
    {
        "name": "defaultField",
        "label" : "Default Field",
        "type": "text"
    },
    
    "rpc://nameOfMyRemoteProcedure"
]
```

{% endtab %}
{% endtabs %}

### Select parameter with nested dynamic parameters under a specific option

{% tabs %}
{% tab title="Source" %}

```json
[
    {
        "name": "param",
        "label": "Parameter",
        "type": "select",
        "options": [
            {
                "label": "Option 1",
                "value": 1,
                "nested": "rpc://NameOfMyRemoteProcedure"
            }
        ]
    }
]
```

{% endtab %}
{% endtabs %}
