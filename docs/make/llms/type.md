# Source: https://developers.make.com/custom-apps-documentation/component-blocks/api/handling-responses/type.md

# Type

**Required**: no\
**Default**: `automatic` (based on `Content-Type` header)\
**Values**: `automatic`, `json`, `urlencoded`, `text` (or `string`), `binary` , and `xml`.

This directive specifies how to parse the data received from the server.

When `automatic` is used for the response type, Make tries to parse the response based on its `Content-Type` header.

Currently, Make recognizes only `text/plain`, `application/json`, `application/x-www-form-urlencoded` and `application/xml`(or `text/xml`).

When specifying other types, Make ignores the `Content-Type` header and tries to parse the response in the format that you have specified.

{% tabs %}
{% tab title="Example" %}

```json
{
    "response": {
        "type": "json"
    }
}
```

{% hint style="info" %}
This will parse all responses as JSON.

You can specify the type as a `string`, in which case every response, no matter the status code, will be processed based on your selected type.
{% endhint %}
{% endtab %}
{% endtabs %}

## Custom response types based on status code

You can specify the type as a special object where keys are status codes, wildcard, or status code ranges. This may be necessary because some services return different responses with different status codes: JSON on success and TEXT on error, for example.

### **Type object specification**

* The `*` (wildcard) represents all responses and should always be present.
* The `[number]-[number]` represents a status code range.
* The `[number]` represents a status code.\\

When specifying ranges and multiple ranges include the same status code, the smallest range is selected. The `*` has the largest range (1-999) and a number has the smallest range, for example, `455` is `455-455` range.

Ranges are counted inclusive from both sides, so if you specify a range `401-402`, both the `401` and `402` status codes will be processed by this range.

{% tabs %}
{% tab title="Example" %}

```json
{
    "response": {
        "type": {
            "*": "json", // parse all responses as JSON
            "400-408": "text", // parse all 400-408 responses as text, overrides "*",
            "406": "xml" // parse the 406 response as XML, overrides above definitions
        }
    }
}
```

{% hint style="info" %}
If a response returns with status `406`, it will be parsed as XML.\
If a response returns with status `401`, it will be parsed as text.\
If a response returns with status `200`, it will be parsed as JSON.
{% endhint %}
{% endtab %}
{% endtabs %}

## **XML type**

It is not possible to convert XML to JSON objects one-to-one. However, in Make, there are methods to accessing nodes and attributes to parsed XML.

#### Everything is an array

Each parsed node is an array, even the root node. Even if in XML a node is single, it will still be represented in Make as an array.

{% tabs %}
{% tab title="Example" %}

```xml
<data>
    <text>Hello, world</text>
</data>
```

Is parsed in Make as:

```json
{
    "data": {
        "text": ["Hello, world"]
    }
}
```

To access the value of `<text>` node in the output, for example:

```json
{
    "response": {
        "output": "body.data[].text[]"
    }
}
```

{% hint style="info" %}
Note the `[]` notation. This is a shortcut to getting the first element of an array in IML.
{% endhint %}
{% endtab %}
{% endtabs %}

#### Access the value of a node with attributes

If there are attributes present on the node you want to get the value of, you need to use `_value` .

{% tabs %}
{% tab title="Example" %}

```xml
<data>
    <text foo="bar">Hello, world</text>
</data>
```

Here, the previous example will not work, because the `<text>` node has attributes.

Use this to access the value of the `<text>` node:

```json
{
    "response": {
        "output": "body.data[].text[]._value"
    }
}
```

{% endtab %}
{% endtabs %}

#### Access node attributes

In a similar manner, you can access node attributes with `_attributes`:

{% tabs %}
{% tab title="Example " %}

```xml
<data>
    <text foo="bar">Hello, world</text>
</data>
```

`_attributes` is a collection where you can access each attribute’s value by its name:

```json
{
    "response": {
        "output": "body.data[].text[]._attributes.foo"
    }
}
```

{% endtab %}
{% endtabs %}

#### Access nested nodes

When accessing nested XML nodes, access them via the array notation. When accessing nested elements, it doesn’t matter if the parent has attributes or not:

{% tabs %}
{% tab title="Example" %}

```xml
<data>
    <items length="2">
        <item>
            <name>Foo</name>
        </item>
        <item>
            <name>Bar</name>
        </item>
    </items>
</data>
```

To process these two items in the `iterate` directive:

```json
{
    "response": {
        "iterate": "body.data[].items[].item",
        "output": {
            "name": "{{item.name[]}}"
        }
    }
}
```

{% hint style="info" %}
It is the `item` array that contains `<item>` nodes, and not the `items` array.
{% endhint %}
{% endtab %}
{% endtabs %}

## Rounded long ID numbers

In some cases, services might send JSON or XML with long IDs:

{% tabs %}
{% tab title="Example" %}

```json
{
"id": 5189203162509781230504938,
"name": "blabla",
...
}
```

{% endtab %}
{% endtabs %}

Since Make uses JavaScript, numbers exceeding the [MAX\_SAFE\_INTEGER value](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/MAX_SAFE_INTEGER) may be rounded.

In this case, use `type: text` to handle the response. Then, use the `replace` (with RegEx) and `parseJSON` functions to convert these long numbers to strings.

{% tabs %}
{% tab title="Communication" %}

```json
"response": {
"type": "text",
"output": "{{fixLongNumbers(body)}}"
}
```

{% endtab %}

{% tab title="Custom function" %}

```javascript
function fixLongNumbers(body) {
try {
const fixedBody = body.replaceAll(/(?<!"|\d)(?<value>\d{16,})/g, '"$<value>"');
const output = JSON.parse(fixedBody);
return output;
} catch {
return body;
}
}
```

{% endtab %}
{% endtabs %}

This is not a problem when the third party sends an ID as a `string`.

{% tabs %}
{% tab title="First Tab" %}

```javascript
{
"id": "5189203162509781230504938",
"name": "blabla",
...
}
```

{% endtab %}
{% endtabs %}
