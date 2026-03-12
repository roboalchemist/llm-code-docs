# Source: https://developers.make.com/custom-apps-documentation/best-practices/input-parameters/processing-of-input-parameters.md

# Processing of input parameters

## Mapping all parameters

{% tabs %}
{% tab title="Bad practice" %}

```javascript
{
    ...
    "body": {
        "firstName": "{{parameters.firstName}}",
        "lastName": "{{parameters.lastName}}",
        "email": "{{parameters.email}}"
    },
    // ... other directives
}
```

{% hint style="info" %}
In this example you have to map every parameter correctly.

There is a risk of a typo or omission of a parameter.
{% endhint %}
{% endtab %}

{% tab title="Good practice" %}

```javascript
{
    // ...
    "body": "{{parameters}}",
    // ...
}
```

{% hint style="info" %}
With this approach, all parameters from the modules will be sent to the API.
{% endhint %}
{% endtab %}

{% tab title="Mappable parameters" %}

```json
[
    {
        "name": "email",
        "type": "email",
        "label": "Email address",
        "required": true
    },
    {
        "name": "firstName",
        "type": "text",
        "label": "First Name",
        "required": true
    },
    {
        "name": "lastName",
        "type": "text",
        "label": "Last Name",
        "required": true
    }
]
```

{% endtab %}
{% endtabs %}

## Using an IML function or omitting a parameter

Sometimes, you don't want to map all parameters in the `body`. Some reasons may include:

* The parameter shouldn't be sent at all (technical parameters such as selects, etc.).
* The parameter should be sent somewhere else than in the `body`, e.g. in the `url`.
* The parameter has to be wrapped in an IML or custom IML function.

{% tabs %}
{% tab title=" Bad practice" %}

```javascript
{
    "url": "/contact/{{parameters.id}}",
    "method": "PUT",
    "body": {
        "email": "{{parameters.email}}",
        "firstName": "{{parameters.firstName}}",
        "lastName": "{{parameters.lastName}}",
        "registrationDate": "{{formatDate(parameters.registrationDate, 'YYYY-MM-DD')}}"
        
    },
    // ...
}
```

{% hint style="info" %}
In this example you have to map every parameter correctly.

There is a risk of a typo or omission of a parameter.
{% endhint %}
{% endtab %}

{% tab title="Good practice" %}

```javascript
{
    "url": "/contact/{{parameters.id}}",
    "method": "PUT",
    "body": {
        "{{...}}": "{{omit(parameters, 'id', 'registrationDate')}}",
        "registrationDate": "{{formatDate(parameters.registrationDate, 'YYYY-MM-DD')}}"
    },
    // ...
}
```

{% hint style="info" %}
Note that `"{{...}}"` lists all available parameters from the module and allows adding other parameters.

The `omit()` function allows the removal of parameters that are used somewhere else, shouldn't be used, or require special attention.

In this case, the `id` parameter is already used in the `url`, and the `registrationDate` parameter is wrapped in `formatDate` IML function.
{% endhint %}
{% endtab %}

{% tab title="Mappable parameters" %}

```json
[
    {
        "name": "id",
        "type": "string",
        "label": "Contact ID",
        "required": true
    },
    {
        "name": "email",
        "type": "email",
        "label": "Email address"
    },
    {
        "name": "firstName",
        "type": "text",
        "label": "First Name"
    },
    {
        "name": "lastName",
        "type": "text",
        "label": "Last Name"
    },
    {
        "name": "registrationDate",
        "type": "date",
        "label": "Date of Registration"
    }
]
```

{% endtab %}
{% endtabs %}

## Handling arrays, nulls, and empty strings

Make and other third-party services transport values in many different formats. It is important to know how to handle the value types of arrays, nulls, and empty strings.

### **Bad practices**

{% tabs %}
{% tab title="Omitting of null or empty string parameters" %}

```javascript
{
    "url": "/messages.json",
    "method": "POST",
    "body": {
        "status": "active",
        "content": "{{ifempty(parameters.content, undefined)}}"
    },
    // ...
}
```

{% hint style="info" %}
It isn't possible to send a `null` value to a service.
{% endhint %}

```jsonc
{
    "url": "/messages.json",
    "method": "POST",
    "body": {
        "status": "active",
        "content": "{{if(parameters.content, parameters.content, undefined)}}"
    },
    // ...
}
```

{% hint style="info" %}
It isn't possible to send a `null`, empty string, and 0 (zero) value to a service.
{% endhint %}
{% endtab %}

{% tab title="Omitting of empty arrays" %}

```javascript
{
    "url": "/tasks.json",
    "method": "POST",
    "body": {
        "status": "active",
        "tags": "{{if(length(parameters.tags) > 0, parameters.tags, undefined)}}"
    },
    // ...
}
```

{% hint style="info" %}
It isn't possible to send an empty array to a service. *E.g. User wants to remove all tags from a task.*
{% endhint %}
{% endtab %}
{% endtabs %}

Let users decide which parameters they want to send to the service. Make has a feature to show how to process values. This feature allows users to define exactly how Make should behave when the value is "empty".

For example, if a user defines that they want to send a specific field to a service even if the value is `null` , empty string, or an empty array, it will be sent to the service. In module communication, config passes parameters without any modification.

## Query string (qs)

Query string parameters should be defined using the `qs` directive as a key-value collection, where the key is the parameter name and the value is the parameter value. Values in the `qs` collection are automatically encoded, so you don't need to escape them manually.

{% hint style="info" %}
The same automatic encoding applies to the `headers` and `body` collections for request headers and body payloads, respectively.
{% endhint %}

{% tabs %}
{% tab title="Example" %}

```javascript
{
    "url": "http://yourservice.com/api/items",
    "qs": {
        "limit": 100,
        "since": "{{parameters.since}}",
        "until": "{{parameters.until}}"
    }
    // ... other directives
}
```

This will issue the request to URL in this way:

`http://yourservice.com/api/items?limit=100&since=2023-01-01&until=2023-01-31`
{% endtab %}
{% endtabs %}

If you provide a query string directly in the `url` directive, it won't be automatically encoded. You have to encode it manually. But in common cases, entering the query string in the `url` is not a recommended approach, especially when values are inserted dynamically. See the [Special case: Query string parameters in the URL section](#special-case-query-string-parameters-in-the-url) for more details.

### Special case: Query string parameters in the URL

In most cases, having the query string in the URL is not the best practice. It is better to use the `qs` collection, but sometimes there may be a special case when you need to use the query string directly in the URL.

The main difference is that the query string in the URL is not encoded automatically, so you have to do it manually. This can be useful when the third-party service requires a very specific format or encoding of the query string parameters. In that case, you can add a query string directly to the `url` directive string and manage the encoding yourself.

Example of specific query string parameters in the URL:

{% tabs %}
{% tab title="Example" %}

```javascript
{
    "url": "http://yourservice.com/api/users/{{parameters.userId}}?groups=(1,2,3,4)&specificallyEncodedParameter={{parameters.specific}}",
    // qs: {} // <- Do not include the `qs` collection here
    "method": "POST",
    // ...
}
```

{% endtab %}
{% endtabs %}

The most common use case for this is when a third-party service requires special symbols like brackets `[]` or parentheses `()` to be unencoded in the query string.

{% hint style="info" %}
Important: Never mix the `qs` directive together with the query string in the URL. This will lead to invalid escaping of parameters specified in the `url`.
{% endhint %}

### Using arrays in `qs`

You can also use an array as a value in the `qs` collection. In this case, the resulting query string will repeat the key for each value in the array, e.g. `?tag=one&tag=two&tag=three`.

{% tabs %}
{% tab title="Example" %}

```javascript
{
    "url": "http://yourservice.com/api/items",
    "qs": {
        "anytag": ["one", "two", "three"]
    }
}
```

{% hint style="info" %}
This will issue the request to URL in this way:

`http://yourservice.com/api/items?anytag=one&anytag=two&anytag=three`
{% endhint %}
{% endtab %}
{% endtabs %}

### Using structured data in `qs`

{% hint style="info" %}
`qs` (and also `headers`) are single-level collections only, meaning that you cannot specify a nested collection in their parameters.
{% endhint %}

{% tabs %}
{% tab title="Incorrect structure example" %}

```javascript
{
    "qs": {
        "person": {
            "address": {
                "street": "123 Main Street"
            }
        }
    }
}
```

{% hint style="info" %}
**This example will not work**.

Since there is no defined standard for how to encode nested objects in a query string, you need to implement it manually based on special requirements of the third-party service. The most common approach is to use dot notation (use a `.` to separate the keys in the query string) for nested properties.
{% endhint %}
{% endtab %}

{% tab title="Correct structure example" %}

```javascript
{
   "qs": {    
     "person.address.street": "changethis"
    }
}
```

{% hint style="info" %}
This will issue the request with the query string:

`?someProp.anotherOne.and-one-more=THIS%20WILL%20WORK`
{% endhint %}
{% endtab %}
{% endtabs %}
