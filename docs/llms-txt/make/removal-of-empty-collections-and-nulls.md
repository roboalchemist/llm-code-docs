# Source: https://developers.make.com/custom-apps-documentation/app-components/iml-functions/removal-of-empty-collections-and-nulls.md

# Removal of empty collections and nulls

There are API services that throw an error when you pass an empty collection or null for certain optional fields.

{% tabs %}
{% tab title="Request" %}

```json
{
    "name": "John Doe",
    "dob": "1970-01-01",
    ...
    "address": {}
}
```

{% hint style="info" %}
The collection `"address"` has empty data, which will cause an error response.
{% endhint %}
{% endtab %}

{% tab title="Error response" %}

> Validation Error
>
> Field "address" cannot be empty.
> {% endtab %}
> {% endtabs %}

{% tabs %}
{% tab title="Custom IML function: remove empty collections/arrays" %}

```javascript
function removeEmpty(input) {
    if (typeof input !== "object" || input === null) return undefined;
    return Object.entries(input).reduce((acc, [key, value]) => {
        if (Array.isArray(value)) {
            acc[key] = value.map(item => removeEmpty(item));
            return acc;
        }
        if (typeof value === "object" && value !== null && !(value instanceof Date)) {
            if (Object.keys(value).length === 0) return acc;
            acc[key] = removeEmpty(value);
            return acc;
        }
        if (value === null) return acc; // comment this line if you have to pass null values.
        acc[key] = value;
        return acc;
    }, {});
}
```

{% endtab %}
{% endtabs %}

In the module:

{% tabs %}
{% tab title="Variant 1" %}

```json
{
    "body": "{{removeEmpty(parameters)}}"
}
```

{% endtab %}

{% tab title="Variant 2" %}

```json
{
    "body": {
        "parameter1": "value1",
        "{{...}}": "{{removeEmpty(parameters)}}"
        }
}
```

{% endtab %}
{% endtabs %}

{% tabs %}
{% tab title="Correct request" %}

```json
{
    "name": "John Doe",
    "dob": "1970-01-01"
}
```

{% hint style="info" %}
The collection "address" was not entered in the request.
{% endhint %}
{% endtab %}

{% tab title="Successful response" %}

> 200 Success
> {% endtab %}
> {% endtabs %}
