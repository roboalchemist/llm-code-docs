# Source: https://developers.make.com/custom-apps-documentation/component-blocks/api/handling-responses/iterate.md

# Iterate

**Required**: no

This directive specifies the container of an array of items that the module must process and output. In its simplest form, the `iterate` directive is an IML string that points to a container of your items. It must be an array.

{% tabs %}
{% tab title="Source" %}

```json
{
    "response": {
        "iterate": "{{body.data}}"
    }
}
```

{% endtab %}
{% endtabs %}

When you need to filter out some items for processing, you can specify the `iterate` directive as an object, in which case it will have the following properties:

<table><thead><tr><th width="195.33333333333331">Property</th><th width="168.22216796875">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>container</code></td><td>IML string</td><td>Specifies the array with the data you want to process.</td></tr><tr><td><code>condition</code></td><td>IML string</td><td>Specifies a filter that can be used to filter out unwanted items.</td></tr></tbody></table>

## Properties

### container

**Required**: yes

The `iterate.container` directive must point to an array of items that are to be processed.

### condition

**Required**: no\
**Default**: `true`

An optional expression to filter out unwanted items. It must resolve into a Boolean value where `true` passes the item through and `false` drops the item from processing. The `item` variable is available in this directive, which represents the current item being processed.

## Example

The `iterate` directive changes the behavior of the `output` directive and allows you to use a special variable `item` that represents the currently processed item. The `output` directive is executed for each item in the container that you have specified in `iterate.container`. You can use the `item` variable in the `output` directive to access properties of iterated objects.

To iterate this response:

{% tabs %}
{% tab title="Response" %}

```json
{
    "success": true,
    "data": [{
        "id": 1,
        "foo": "bar"
    }, {
        "id": 2,
        "foo": "baz"
    }, {
        "id": 3,
        "foo": "qux"
    }]
}
```

{% endtab %}
{% endtabs %}

To process all items contained in the `data` array, specify the `iterate` directive:

{% tabs %}
{% tab title="Iterate directive" %}

```json
{
    "response": {
        "iterate": "body.data",
        "output": {
            "id": "{{item.id}}",
            "text": "{{item.foo}}"
        }
    }
}
```

{% endtab %}
{% endtabs %}

Specify how the output should look in the `output` directive. The `item` variable represents the currently processed item from the `data` array.

{% tabs %}
{% tab title="Output directive" %}

```json
[{
    "id": 1,
    "text": "bar"
}, {
    "id": 2,
    "text": "baz"
}, {
    "id": 3,
    "text": "qux"
}]
```

{% endtab %}
{% endtabs %}
