# Source: https://developers.make.com/custom-apps-documentation/block-elements/types.md

# Source: https://developers.make.com/custom-apps-documentation/app-components/modules/action/types.md

# Module actions

## Create

Used for modules that are creating an object. Most of the time these modules use a POST request.

{% tabs %}
{% tab title="Create a contact example 1" %}

<pre class="language-json"><code class="lang-json">{
    "url": "/contacts",
    "method": "POST",
    "body": {
        "{{...}}": "{{omit(parameters, 'date')}}",
        "date": "{{formatDate(parameters.date, 'YYYY-MM-DD')}}"
<strong>    },
</strong>    "response": {
        "output": "{{body}}"
    }
}
</code></pre>

{% endtab %}

{% tab title="Create a contact example 2" %}

```json
{
    "url": "/contacts",
    "method": "POST",
    "body": "{{parameters}}",
    "response": {
        "output": "{{body}}"
    }
}
```

{% endtab %}

{% tab title="Create a contact example 3" %}

```json
{
    "url": "/contacts"
    "method": "POST",
    "qs": {},
    "headers": {},
    "body": {
        "name": "{{parameters.name}}",
        "email": "{{parameters.email}}",
        "phone": "{{parameters.phone}}",
        "address": "{{parameters.address}}"
    },
    "response": {
        "output": "{{body}}"
    }
}
```

{% endtab %}
{% endtabs %}

{% hint style="info" %}
There are two types of responsiveness - synchronous and asynchronous. Read more about it in [responsiveness approaches](https://developers.make.com/custom-apps-documentation/best-practices/modules/batch-actions#responsiveness-approaches).
{% endhint %}

## Read

Used for modules that are retrieving an object. Most of the time these modules use a GET request.

{% tabs %}
{% tab title="Get a contact example" %}

```json
{
    "url": "/contacts/{{parameters.contact_id}}",
    "method": "GET",
    "response": {
        "output": "{{body}}"
    }
}
```

{% hint style="info" %}
There is a difference between List/Search and Get modules although they use the same GET method.

List/Search modules return multiple bundles and should be a Search module type.

Get modules return only one bundle (specified by the entered ID) and should be Action modules.
{% endhint %}
{% endtab %}
{% endtabs %}

### Search module

If you happen to receive this error: `Invalid module output. Expected Object, but found Array.`, it means that your module should be a Search type. A [search](https://developers.make.com/custom-apps-documentation/app-components/modules/search) module expects an array output type and, unlike the action type module, supports the [pagination](https://developers.make.com/custom-apps-documentation/component-blocks/api/pagination) directive.

{% tabs %}
{% tab title="Code" %}

```json
"response": {
            "output":
            {
                "myArray": "{{body}}"
            }
        }
```

{% hint style="info" %}
If you don't want to iterate the array returned from the API, you can wrap it in an object.
{% endhint %}
{% endtab %}
{% endtabs %}

## Update

Used for modules that are updating an object. Most of the time these modules use a PATCH or PUT request.

{% hint style="info" %}
When a module is type **Update**, a new keyword appears inside Make - [**erase**](https://developers.make.com/custom-apps-documentation/other/processing-of-empty-values).
{% endhint %}

{% tabs %}
{% tab title="Update a contact example 1" %}

```json
{
    "url": "/contacts/{{parameters.contact_id}}",
    "method": "PUT",
    "body": "{{omit(parameters,'contact_id')}}",
    "response": {
        "output": "{{body}}"
    }
}

```

{% endtab %}

{% tab title="Update a contact example 2" %}

```json
{
    "url": "/contacts/{{parameters.contact_id}}",
    "method": "PUT",
    "body": {
        "name": "{{parameters.name}}",
        "email": "{{parameters.email}}",
        "phone": "{{parameters.phone}}",
        "address": "{{parameters.address}}"
    },
    "response": {
        "output": "{{body}}"
    }
} {
```

{% endtab %}
{% endtabs %}

{% hint style="info" %}
There are two types of update approaches - partial and full.
{% endhint %}

## Delete

Used for modules that are deleting an object. Most of the time these modules use a DELETE request.

{% tabs %}
{% tab title="Delete a contact example" %}

```json
{
    "url": "/contacts/{{parameters.contact_id}}",
    "method": "DELETE",
    "response": {
        "output": "{{undefined}}"
    }
}
```

{% endtab %}
{% endtabs %}
