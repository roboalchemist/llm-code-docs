# Source: https://developers.make.com/custom-apps-documentation/component-blocks/api/making-requests.md

# Requests

To make a request, specify at least a URL. All other directives are optional.

## Specification

### url

**Required**: yes\
**Type:** IML string

Specifies the request URL.

This directive must be present. The trigger does not support request-less/static mode. The URL may be defined as a full URL `https://example.com/api/v1/endpoint` or partial `/endpoint`, in which case it is appended to the `baseUrl` defined in the app's Base. However, for app approval, partial URLs are suggested.

### method

**Required**: no\
**Type:** IML string\
**Default**: `GET`\
**Values**: `GET`, `POST`, `PUT`, `DELETE`, `PATCH` (and other HTTP methods)

Specifies the HTTP method that should be used when issuing a request.

Specify the method with an IML expression based on module parameters:

{% tabs %}
{% tab title="Example" %}

```json
{
    "url": "http://example.com/entity",
    "method": "{{if(parameters.create, 'POST', 'PUT')}}" 
}
```

{% endtab %}
{% endtabs %}

### headers

**Required**: no\
**Type:** IML flat object

A single level (flat) collection that specifies request headers.

All header names should be case insensitive so `x-requested-with` should be handled the same as `X-Requested-With`.

{% tabs %}
{% tab title="Example" %}

```json
{
    "url": "http://example.com/data",
    "headers": {
        "X-Item-Id": "{{parameters.id}}"
    }
}
```

How Make handles headers:

Input:

```json
"headers": {
    "tEsT": 123,
    "tESt-wiTh-dAsh": 123
}
```

Sent by Make:

```
Test: 123
Test-With-Dash: 123
```

{% endtab %}
{% endtabs %}

### qs

**Required**: no\
**Type:** IML flat object

A single level (flat) collection that specifies request query string parameters.

{% tabs %}
{% tab title="Example" %}

```jsonc
{
    "url": "http://example.com",
    "qs": {
        "foo": "foobar",
        "hello": "world",
        "list": ["one", "two", "three"]
    },
    // ... other directives
}
```

This will use a request to this URL:

`http://example.com?foo=foobar&hello=world&list=one&list=two&list=three`
{% endtab %}
{% endtabs %}

### type

**Required**: no\
**Type:** String\
**Default**: `json`\
**Values**: `json`, `urlencoded`, `multipart/form-data`, `text` (or `string` or `raw`), `binary`.

Specifies how the request body is encoded and sent when the the `method` is anything except `GET`: `POST`, `PUT`, etc.

When the `method` is `GET` this directive will be ignored.

When using `text` (or `string` or `raw`) the body should be a string. If it is not, it will be converted to a string.

When using `json` or `multipart/form-data` or `urlencoded` , the appropriate value of the `Content-Type` header is set automatically based on the specified type.

### body

**Required**: no\
**Type:** Any IML type

Specifies the request body when the `method` directive is set to anything except `GET`.

If the body is specified and the `method` directive is set to `GET` , the body is ignored and appropriate `Content-Type` headers are not set.

{% tabs %}
{% tab title="Example" %}

```json
{
    "url": "http://example.com/post",
    "body": {
        "first_name": "{{parameters.firstName}}",
        "last_name": "{{parameters.lastName}}"
    }
}
```

If you want to specify an XML request body, specify it as a string that will use IML expressions to pass values to XML nodes:

```json
{
    "url": "http://example.com/post",
    "body": "<request><rows><row><column name=\"first_name\">{{parameters.firstName}}</column><column name=\"last_name\">{{parameters.lastName}}</column></row></rows></request>"
}
```

If you need to send a [JSON string inside a JSON object](https://developers.make.com/custom-apps-documentation/component-blocks/api/processing-of-json-strings-inside-a-json-object), use the `createJSON()` function.
{% endtab %}
{% endtabs %}

### response

Collection of directives controlling the processing of the response.

### pagination

Collection of directives controlling the [pagination](https://developers.make.com/custom-apps-documentation/component-blocks/api/pagination) logic.

### log

**Required**: yes\
**Type:** IML flat object

A single level (flat) collection that contains logging options.

This directive specifies logging options for both the request and the response.

{% tabs %}
{% tab title="Example" %}

```json
{
    "url": "http://example.com/post",
    "headers": {
        "authorization": "Bearer {{connection.accessToken}}"
    },
    "log": {
        "sanitize": ["request.headers.authorization"]
    }
}
```

{% endtab %}
{% endtabs %}

### repeat

**Required**: no\
**Type:** IML object

Repeats a request under a certain condition with a predefined delay in milliseconds. The maximum number of repeats can be bounded by the `repeat.limit`.

The `repeat` directive repeats a request as long as the test `condition` evaluates to true. The `condition` is evaluated after each request. A `delay` can be defined between each request. The maximum number of repeats can be bound by the `limit`.

The `temp` directive must be used within `repeat` in common cases. The `condition` expression has no access to the `body.data` directly, so the response must be stored to the `temp` object first, then you can use `temp` in the `condition` expression.

<table><thead><tr><th width="150" valign="top">Key</th><th width="123" valign="top">Type</th><th valign="top">Description</th></tr></thead><tbody><tr><td valign="top"><code>condition</code></td><td valign="top">IML string</td><td valign="top"><p>A condition expression evaluated after each request iteration. If this condition evaluates to true, the request is called again after a specified delay. When the condition evaluates to false, the repetition is finished.</p><p>The condition has access to the <code>temp</code> object only, not to the <code>body</code>.</p></td></tr><tr><td valign="top"><code>delay</code></td><td valign="top">Number</td><td valign="top">Specifies the delay between two repeats in milliseconds.</td></tr><tr><td valign="top"><code>limit</code></td><td valign="top">Number</td><td valign="top">Specifies the maximum number of iterations. Optional. Not limited if not specified.</td></tr></tbody></table>

{% tabs %}
{% tab title="Example" %}

```json
{
    "url": "...",
    ...,
    "response": {
        "temp": {...},  // Store response data to be able to access it in `condition`
        "output": null
    },
    "repeat": {
        "condition": "{{expression}}",  // Condition returning boolean
        "delay": 1000,                  // Delay in miliseconds
        "limit": 10                     // Max iterations
    }
}
```

{% hint style="warning" %}
`delay` and `limit` must be hard-coded. They do not support `{{ }}`.

It is strongly recommended to set the `limit` to prevent an infinite loop.
{% endhint %}

It is strongly recommended to set the `limit` to prevent an infinite loop.
{% endtab %}

{% tab title="Use case" %}
Handling an asynchronous file upload, waiting for completion of background processes.

1. Request an API to initiate some server task (in this case a PDF generation task).
2. Periodically check the status of the task and wait until task is done. Uses the `repeat` directive.
3. Output the task result.

Keep the module timeout limit of 40s in mind when setting up the `delay` and `limit` values.

```jsonc
[
        {
        url: '/api/pdf-generate/start-job',
        method: 'POST',
        body: {
            'document-id': 'abc123'
        },
        response: {
            temp: {
                jobId: '{{body.data.jobId}}'
            },
            output: null
        }
    },
    {
        url: '/api/pdf-generate/status/{{temp.jobId}}',
        method: 'GET',
        response: {
            // Store the response data into `temp` so the `repeat` directive can access it:
            temp: {
                status: '{{body.data.status}}'
            },
            output: null
        },
        repeat: {
            condition:
                "{{temp.status === 'waiting' || temp.status === 'processing'}}",
            delay: 3000, // Wait 3s
            limit: 10 // Repeat up to 10 times
        }
    },
    {
        // Ensure the next API call is only executed if the document finished being processed:
        condition: "{{temp.status === 'done'}}",
        url: '/api/pdf-generate/result/{{temp.jobId}}',
        method: 'GET',
        response: {
            output: '{{body.data}}'
        }
    }
]
```

{% endtab %}
{% endtabs %}

### temp

**Required**: no\
**Type:** IML object

Specifies an object that can be used to create custom temporary variables.

Also creates a `temp` variable in IML, through which you then access your variables. The `temp` collection is not persisted and will be lost after the module is done executing.

This directive is executed prior to everything else: before `condition`, `url`, `qs`, `body` or any other directive. This makes it a good place to store some values that you need receptively.

When you have multiple requests, this directive is also useful for passing values between requests.

When specifying the `temp` directives in different requests and in the `response` section (`response.temp` directive), the contents of the `temp` collection are not overwritten, but instead merged.

{% tabs %}
{% tab title="Example" %}

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

{% endtab %}
{% endtabs %}

### condition

**Required**: no\
**Type:** IML string or Boolean\
**Default**: `true`

Specifies whether to execute the request or not.

If this directive is not specified, the request will always be executed.

If the value of this directive is `false`, then the request will not be executed, and the flow will go to the next request, if present, or return nothing.

When you need to return some data when the condition is false, Specify the `condition` directive as an object, in which case it will have the following properties:

<table><thead><tr><th width="150">Key</th><th width="136">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>condition</code></td><td>IML string</td><td>Specifies if the request should be executed or not.</td></tr><tr><td><code>default</code></td><td>Any IML Type</td><td>Specifies the module output when the condition is false.</td></tr></tbody></table>

### aws

Collection of parameters for AWS signing.

<table><thead><tr><th width="146.40728759765625" valign="top">Property</th><th width="219.4444580078125" valign="top">Type</th><th valign="top">Description</th></tr></thead><tbody><tr><td valign="top"><code>secret</code></td><td valign="top">IML string</td><td valign="top">AWS secret</td></tr><tr><td valign="top"><code>session</code></td><td valign="top">IML string</td><td valign="top">AWS session. This only works for services that require session as part of the canonical string.</td></tr><tr><td valign="top"><code>bucket</code></td><td valign="top">IML string</td><td valign="top">AWS bucket, unless you’re specifying your bucket as part of the path, or the request doesn’t use a bucket.</td></tr><tr><td valign="top"><code>sign_version</code></td><td valign="top">IML string</td><td valign="top"><p>Default: 2.</p><p>AWS sign version. Must be either 2 or 4.</p></td></tr><tr><td valign="top"><code>service</code></td><td valign="top">IML string</td><td valign="top">AWS service name<br>Condition: <code>sign_version</code> must be 4.</td></tr></tbody></table>

### ca

**Required**: no\
**Type:** IML string

Allows you to enter your self-signed certificate.

The value should be the PEM encoded self-signed certificate.

{% tabs %}
{% tab title="Certificate" %}

```
-----BEGIN CERTIFICATE-----
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy
zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz
adfadsfasdfnaludfhjkasdfadsfadfadfabas
iouqrpoernqepcqoweiqjcqponopqqfowepfqo
-----END CERTIFICATE-----
```

{% endtab %}

{% tab title="Communication" %}

```json
{
    "url": "https://www.example.com",
    "qs": {},
    "ca": "-----BEGIN CERTIFICATE-----\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\nyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy\nzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz\nadfadsfasdfnaludfhjkasdfadsfadfadfabas\niouqrpoernqepcqoweiqjcqponopqqfowepfqo\n-----END CERTIFICATE-----",
    "body": {},
}
```

{% endtab %}
{% endtabs %}

### encodeUrl

**Required**: no\
**Type:** Boolean\
**Default**: `true`

Specifies if the URL should be auto encoded or not.

This directive is on by default, so if you have any special characters in your URL they will be automatically encoded.

If you don't want your URL to be encoded automatically or if you want to control the parts of the URL that are included, set this directive to `false`.

### followAllRedirect

**Required**: no\
**Type:** Boolean\
**Default**: `true`

Specifies whether or not to follow non-GET HTTP 3xx responses as redirects.

This parameter allows only static input `true` or `false`.

Mapping `"followAllRedirect": "{{parameters.followAllRedirect}}"` is not supported.

### followRedirect

**Required**: no\
**Type:** Boolean\
**Default**: `true`

Specifies whether or not to follow GET HTTP 3xx responses as redirects.

This parameter allows only static input `true` or `false`.

Mapping `"followRedirect": "{{parameters.followRedirect}}"` is not supported.

### gzip

**Required:** no\
**Type:** Boolean\
**Default:** `false`

Adds an `Accept-Encoding` header to request compressed content encodings from the server (if not already present) and decodes supported content encodings in the response.

### rejectUnauthorized (deprecated)

**Required**: no\
**Default**: `true`\
**Type:** `Boolean`\
**Values**: `true`, `false`

Verifies the TLS certificate.

If set to `true`, the TLS certificate of the HTTPS server is verified. If the verification fails, an error is thrown.

If set to `false`, the server's certificate is not verified, allowing requests to proceed even if the certificate is invalid or insecure.

{% hint style="warning" %}
Disabling certificate verification (`rejectUnauthorized: false`) significantly reduces communication security and increases the risk of man-in-the-middle attacks. Only override the default value when absolutely necessary.

A typical use case for setting `rejectUnauthorized: false` is when a non-production HTTPS server uses a self-signed certificate.

Self-signed certificates should never be used in production environments.
{% endhint %}

### sanitize

An array of paths to sanitize when logging a request or response.

Sanitizing sensitive information such as tokens, API keys or passwords is mandatory.

{% tabs %}
{% tab title="Request authorization header" %}

```json
{
    "url": "http://example.com/post",
    "headers": {
        "authorization": "Bearer {{connection.accessToken}}"
    },
    "log": {
        "sanitize": ["request.headers.authorization"]
    }
}
```

{% hint style="info" %}
Each item in the sanitizing directive is defined in dot notation and is case insensitive. You can also access nested structures of response bodies.
{% endhint %}
{% endtab %}

{% tab title="Response" %}

```json
{
    "url": "http://example.com/post",
    "log": {
        "sanitize": ["response.body.access_token"]
    }
}
```

{% hint style="info" %}
Each item in the sanitizing directive is defined in dot notation and is case insensitive. You can also access nested structures of response bodies.
{% endhint %}
{% endtab %}
{% endtabs %}

### shareCookies

**Required**: no\
**Type:** Boolean\
**Default**: `false`

This directive specifies remembering cookies for future use.
