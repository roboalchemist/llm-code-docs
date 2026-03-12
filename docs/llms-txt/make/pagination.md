# Source: https://developers.make.com/custom-apps-documentation/component-blocks/api/pagination.md

# Pagination

It is often necessary to paginate the results that the server returns in order to retrieve additional items because the server may not return how many items you want.

## Specification

The `pagination` collection is placed in the root level of Request Specification, along with `url`, `method` , `body` and `response`.

Pagination directives should be placed inside the `pagination` collection.

### mergeWithParent

**Type:** Boolean\
**Default:** `true`

Specifies the condition to merge pagination parameters with the original request parameters or not. The default value is `true`, which means that all of your pagination request parameters are merged with the original request parameters.

If the value is set to `false`, then no parameters are merged, but instead directly used to make a pagination request.

### url

**Type:** IML string

Specifies the URL that is called when the pagination request is executed. It overrides the original request URL no matter the value of `mergeWithParent`.

### method

**Type:** IML string

Specifies the HTTP method to be used when executing the pagination request. It overrides the original request method no matter the value of `mergeWithParent`.

### headers

**Type:** IML flat object

Specifies the request headers to be used when executing the pagination request. It merges with headers of the original request, overriding headers with the same name when `mergeWithParent` is set to `true` (default).

### qs

**Type:** IML flat object

Specifies the request query string parameters to be used when executing the pagination request. It merges with query string parameters of the original request, overriding ones with the same name when `mergeWithParent` is set to `true` (default).

### body

**Type:** Any IML type

Specifies the request body when the request method is anything but `GET` to be used when executing the pagination request. It overrides the original request body no matter the value of`mergeWithParent`.

### condition

**Type:** IML string or Boolean

Specifies whether to execute the pagination request or not. It has all context variables available to it like the `response` collection, such as `body`, `headers`, and `temp` . Use this to stop paginating if the server is sending you information about the number of pages or items, or if the next page is available or not.

## Limits

As we cannot paginate to infinity, there are four limits on the paginated requests.

<table><thead><tr><th width="221.16668701171875">Name</th><th width="364.0000813802083">Total limit of ...</th><th>Value</th></tr></thead><tbody><tr><td><strong>Max Request Count</strong></td><td>... all requests performed by a single module</td><td>100</td></tr><tr><td><strong>Max Pagination Request Count</strong></td><td>... pagination requests performed by a single module</td><td>50</td></tr><tr><td><strong>Max Past Record</strong></td><td>... paginated records</td><td>3200</td></tr><tr><td><strong>Max Call Timeout</strong></td><td>... seconds</td><td>40</td></tr></tbody></table>

## Examples

### Total pages

The common method of pagination is to use `total pages` or `pages count` . The service gives information about how many pages of content (the total count) are available and you have to iterate over those pages.

{% tabs %}
{% tab title="Response from a service" %}

```json
{
  "Data": [
    {...},
    {...},
    {...},
    {...},
    {...}
  ]
  "TotalItems": 42,
  "TotalPages": 10
}
```

{% hint style="info" %}
This is a sample response from the service. The service returns some items in the `Data` array, `TotalItems`, and `TotalPages` metadata. The `TotalPages` is the one we use to set up pagination in Make.
{% endhint %}
{% endtab %}

{% tab title="Pagination code" %}

```json
"pagination": {
	"qs": {
		"Page": "{{pagination.page}}"
	},
	"condition": "{{body.TotalPages >= pagination.page}}"
}
```

{% hint style="info" %}
The service accepts `Page` in the query string as a parameter, which tells the service which page you want to retrieve. There's no need to set some temporary variables. Send `{{pagination.page}}` in the correct query parameter and set the condition so the pagination directive knows when to stop requesting more pages.
{% endhint %}
{% endtab %}
{% endtabs %}

{% hint style="info" %}
Some services index pages **from 0**, and some index **from 1**. The `pagination.page` directive indexes pages **from 1**. Verify this information to set up the pagination correctly.
{% endhint %}

### Limit - offset

This is another common way to implement pagination. Set the paging cursor using two parameters:

* `limit` - sets the maximum amount of records being retrieved per page
* `offset` - sets the number of skipped records from the beginning of the data set

Use two parameters to control the pagination.

{% tabs %}
{% tab title="Response from a service" %}

```javascript
[
    {...},
    {...},
    {...},
    {...},
    {...}
]
```

{% hint style="info" %}
The service doesn't need to return any pagination information to you. The service may return `PageSize` , for example, but that is not relevant in this case.
{% endhint %}
{% endtab %}

{% tab title="Pagination code" %}

```json
"qs": {
    "limit": 100
},
"response": {
    "limit": "{{parameters.limit}}",
    "output": "{{item}}",
    "iterate": "{{body.users}}"
},
"pagination": {
    "qs": {
        "offset": "{{(pagination.page - 1) * 100}}"
    }
}
```

{% hint style="info" %}
Note that the `limit` parameter is set statically in the query string for a request. It represents the size of a page.

Inside the pagination directive, we'll set the `offset` parameter.

After the first request, the value of `pagination.page` will be 2, as it's prepared to retrieve a second page. We transform it to the offset we want. `pagination.page - 1 = 1` and `1 * 100` is 100. The value for computing the offset is the same as in the limit parameter.

The second request will have `limit: 100` and `offset: 100`, so it will skip first 100 records and retrieve records 101-200. The third request will skip first 200 (as (3-1)\*100 = 200) and retrieve records 201-300. And so on.
{% endhint %}
{% endtab %}
{% endtabs %}

{% hint style="info" %}
The pagination stops automatically after the response with 0 records or once the condition `response.limit` is met. If that behavior does not fit your needs, you can specify the additional [**condition**](#condition).
{% endhint %}

### Next page token

The next page token is a unique identifier of a next page that is provided in the response. You can get the next page without counting some pages or offsets using this token only. Sometimes the "Next page URL" is provided instead of only the token, but the flow is quite similar.

{% tabs %}
{% tab title="Response from a service" %}

```javascript
{
    "data": [
        {...},
        {...},
        {...},
        {...},
        {...}
    ],
    "nextPageToken": "ABCDEFGHHGFEDCBA"
}
```

{% hint style="info" %}
The service returns a `nextPageToken` for retrieving the next page.
{% endhint %}
{% endtab %}

{% tab title="Pagination code" %}

```json
"pagination": {
	"qs": {
		"nextPageToken": "{{body.nextPageToken}}"
	},
	"condition": "{{body.nextPageToken}}"
}
```

{% hint style="info" %}
In every following request, use the `nextPageToken` provided with the previous one. Stop the pagination when no other `nextPageToken` is received.
{% endhint %}
{% endtab %}
{% endtabs %}

### Next page URL

The next page URL is a link to the next page that is provided in the response.

If the next page URL is provided, you can map it directly in the pagination directive.

{% tabs %}
{% tab title="Response from a service" %}

```json
{
    "items": [
        {...},        },
        {...}
    ],
    "_links": {
        "next": {
            "href": "https://api.abc.com/locations?page=ZmFsc2V8aHR...."
        },
        "previous": null
    }
}
```

{% endtab %}

{% tab title="Pagination code" %}

```json
"pagination": {
        "condition": "{{body._links.next.href}}",
        "url": "{{body._links.next.href}}"
    }
```

{% endtab %}
{% endtabs %}

### Has more items

When using this method, you get information on whether the data set contains more records or not.

{% tabs %}
{% tab title="Response from a service" %}

```javascript
{
    "data": [
        {...},
        {...},
        {...},
        {...},
        {...}
    ],
    "has_more_items": true
}
```

{% hint style="info" %}
The service returns a `has_more_items` Boolean which tells you if you can get more pages or not.
{% endhint %}
{% endtab %}

{% tab title="Pagination code" %}

```json
"pagination": {
	"qs": {
		"page": "{{pagination.page}}"
	},
	"condition": "{{body.has_more_items}}"
}
```

{% hint style="info" %}
Continue to ask for the next page until the `has_more_items` becomes `false`. When that happens, no records can be retrieved.
{% endhint %}
{% endtab %}
{% endtabs %}

### Page only

This type of pagination isn't ideal, but some services use this. With this method, you continue to ask for the next page until you get an empty response.

{% tabs %}
{% tab title="Response from a service" %}

```javascript
[
    {...},
    {...},
    {...},
    {...},
    {...}
]
```

{% hint style="info" %}
No additional info about pagination is provided.
{% endhint %}
{% endtab %}

{% tab title="Pagination code" %}

```json
"pagination": {
	"qs": {
		"page": "{{pagination.page}}"
	}
}
```

{% hint style="info" %}
Continue to ask for the next page until the body (or some key in the body) is not empty.
{% endhint %}
{% endtab %}
{% endtabs %}

{% hint style="info" %}
The pagination should stop after an empty response or empty data in the body. But some services think that it's a good practice to keep returning the last page after the maximum amount of pages has been reached. Always check the behavior of the service when using this type of pagination.
{% endhint %}
