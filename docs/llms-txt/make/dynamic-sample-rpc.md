# Source: https://developers.make.com/custom-apps-documentation/app-components/rpcs/dynamic-sample-rpc.md

# Dynamic sample RPC

Dynamic sample RPCs replace hard-coded samples that might become outdated quickly.

Sample is an object representing one item from the response. If you iterate, don’t forget to set `"limit": 1`, so only one item is processed for sample data.

{% tabs %}
{% tab title="Source" %}

```json
{
    "url": "/list",
    "method": "GET",
    "response": {
        "limit": 1,
        "iterate": "{{body}}",
        "output": "{{item}}"
    }
}
```

{% endtab %}

{% tab title="Usage in Samples tab" %}

```json
pc://NameOfMyRemoteProcedure"
```

{% endtab %}
{% endtabs %}
