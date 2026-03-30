# Source: https://developers.make.com/custom-apps-documentation/app-components/base/advanced-inheritance.md

# Advanced inheritance

Consider this as the base:

{% tabs %}
{% tab title="Code" %}

```json
{
    "headers": {
        "authorization": "Bearer {{connection.accessToken}}"
    }
}
```

{% endtab %}
{% endtabs %}

In a module, you need to add a custom header programmatically:

{% tabs %}
{% tab title="Code" %}

```json
{
    "headers": "{{headerBuilderFunction()}}"
}
```

{% endtab %}
{% endtabs %}

This results in the base being overwritten by the result from the IML function.

To merge both collections, use this special IML syntax inside the module:

{% tabs %}
{% tab title="Code" %}

```json
{
    "headers": {
        "{{...}}": "{{headerBuilderFunction()}}"
    }
}
```

{% endtab %}
{% endtabs %}
