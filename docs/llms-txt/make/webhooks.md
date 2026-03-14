# Source: https://developers.make.com/custom-apps-documentation/app-components/webhooks.md

# Webhooks

To use webhooks, you must always create an instant trigger and link it to a webhook.

## Specification

Specifies how to get data from the payload and how to reply to a remote server.

{% tabs %}
{% tab title="Code" %}

```json
{
    "verification": {
        "condition": String|Boolean,
        "respond": {
            "type": Enum[json, urlencoded, text],
            "status": String|Number,
            "headers": Object
            "body": String|Object,
        }
    },
    "respond": {
        "type": Enum[json, urlencoded, text],
        "status": String|Number,
        "headers": Object
        "body": String|Object,
    },
    "iterate": {
        "container": String,
        "condition": String|Boolean
    },
    "output": String|Object,
    "condition": String|Boolean,
    "uid": String
}
```

{% hint style="info" %}
If the webhook returns multiple items in one batch, you might need to use the `iterate` directive to specify which items to output. Then you might want to specify the `output` directive to map items to output. If you do not specify the `output` directive, items will be returned as-is.
{% endhint %}
{% endtab %}
{% endtabs %}

<table><thead><tr><th width="164.70369466145831" valign="top">Key</th><th width="230" valign="top">Type</th><th valign="top">Description</th></tr></thead><tbody><tr><td valign="top"><code>respond</code></td><td valign="top">Response specification</td><td valign="top">Specifies how to respond to the remote server.</td></tr><tr><td valign="top"><code>verification</code></td><td valign="top">Verification specification</td><td valign="top">Specifies how to reply to the remote server. Used for webhooks that require a verification mechanism, such as challenge responses.</td></tr><tr><td valign="top"><code>iterate</code></td><td valign="top">IML string or iterate specification</td><td valign="top">Specifies how the response items (in case of multiple) are retrieved and processed.</td></tr><tr><td valign="top"><code>output</code></td><td valign="top">Any IML type</td><td valign="top">Describes the structure of the output bundle.</td></tr><tr><td valign="top"><code>condition</code></td><td valign="top">IML string or boolean</td><td valign="top">Determines whether to execute the current request.</td></tr><tr><td valign="top"><code>uid</code></td><td valign="top">IML string</td><td valign="top">Specifies how to get the user ID from the request body. Necessary to associate the recipient when using a shared webhook.</td></tr></tbody></table>

### respond

**Required**: no

This directive lets you customize Make's response on the webhook or a verification request.

<table><thead><tr><th width="126" valign="top">Key</th><th width="148" valign="top">Type</th><th width="97" align="center" valign="top">Required</th><th valign="top">Description</th></tr></thead><tbody><tr><td valign="top"><code>type</code></td><td valign="top">IML string</td><td align="center" valign="top">no</td><td valign="top"><p>Specifies how to encode data into the body.</p><p>Default: <code>json</code></p><p>Available values: <code>json</code>, <code>urlencoded</code>, <code>text</code></p></td></tr><tr><td valign="top"><code>status</code></td><td valign="top">IML string</td><td align="center" valign="top">no</td><td valign="top">Specifies the HTTP status code that will be returned with the response.</td></tr><tr><td valign="top"><code>headers</code></td><td valign="top">IML flat object</td><td align="center" valign="top">no</td><td valign="top">Specifies custom headers that are to be sent with the response.</td></tr><tr><td valign="top"><code>body</code></td><td valign="top">Any IML type</td><td align="center" valign="top">no</td><td valign="top">Specifies the response body.</td></tr></tbody></table>

### verification

**Required**: no

This directive allows you to reply to webhook verification requests. Some systems issue a verification request during webhook creation to ensure your webhook is prepared to handle incoming data. Such systems may send a code and request Make to return it and maybe some other value with it. In such case, this directive will help you.

<table><thead><tr><th width="145.33333333333331" valign="top">Key</th><th width="126" valign="top">Type</th><th valign="top">Description</th></tr></thead><tbody><tr><td valign="top"><code>condition</code></td><td valign="top">IML string</td><td valign="top">Specifies when to treat the incoming data as a verification request.</td></tr><tr><td valign="top"><code>respond</code></td><td valign="top">IML string</td><td valign="top">Specifies the response.</td></tr></tbody></table>

{% tabs %}
{% tab title="Code" %}

```json
{
    "verification": {
        "condition": "{{if(body.code, true, false)}}",
        "respond": {
            "status": 202,
            "type": "json",
            "body": {
                "code": "{{body.code}}"
            }
        }
    }
}
```

{% endtab %}
{% endtabs %}

#### **verification.condition**

**Required**: no

**Default**: `true`

This directive distinguishes normal webhook requests from verification requests. Usually, the remote service will send some code to verify that Make is capable of receiving data. In such cases, you want to check for the existence of this code variable in the request body. If it exists, this request is a verification request. Otherwise, it would be a normal webhook request with data.

#### **verification.respond**

**Required**: no

This directive is exactly the same as the `respond` directive, except that it is nested in `verification`. The behavior of `verification.respond`, is the same as the normal `respond`.

### iterate <a href="#iterate" id="iterate"></a>

Properties of the iterate directive are described in the [communication](https://developers.make.com/custom-apps-documentation/component-blocks/api/handling-responses) documentation.

### output <a href="#output" id="output"></a>

Properties of the output directive are described in the [communication](https://developers.make.com/custom-apps-documentation/component-blocks/api/handling-responses) documentation.

### condition <a href="#condition" id="condition"></a>

Properties of the condition directive are described in the [communication](https://developers.make.com/custom-apps-documentation/component-blocks/api/handling-responses) documentation.

### **uid** <a href="#uid" id="uid"></a>

**Required**: only in shared webhooks

Specifies how to get the user ID from the request body. This value is then used to search for the recipient of the message in the database of connections. Remember to specify the `uid` parameter in the connection definition.

## Available IML variables <a href="#available-iml-variables" id="available-iml-variables"></a>

These IML variables are available for you to use everywhere in a webhook:

<table><thead><tr><th width="166.59259033203125" valign="top">Variable</th><th valign="top">Description</th></tr></thead><tbody><tr><td valign="top"><code>now</code></td><td valign="top">Current date and time</td></tr><tr><td valign="top"><code>environment</code></td><td valign="top">TBD</td></tr><tr><td valign="top"><code>parameters</code></td><td valign="top">Contains the webhook's input parameters.</td></tr><tr><td valign="top"><code>data</code></td><td valign="top">Alias for parameters.</td></tr><tr><td valign="top"><code>body</code></td><td valign="top">Contains the body of an incoming webhook.</td></tr><tr><td valign="top"><code>query</code></td><td valign="top">Contains query string parameters of an incoming webhook.</td></tr><tr><td valign="top"><code>method</code></td><td valign="top">Contains HTTP method of an incoming webhook.</td></tr><tr><td valign="top"><code>headers</code></td><td valign="top">Contains headers of an incoming webhook.</td></tr></tbody></table>

## Types of webhooks

### Shared <a href="#shared" id="shared"></a>

[Shared webhooks](https://developers.make.com/custom-apps-documentation/app-components/webhooks/shared) are used when the external service sends all events from all users to a single URL that you control. With this, the user is not able to see the URL and you must use the `uid` in the connection and in the webhook communication to associate the payloads to the right users.

### Dedicated <a href="#dedicated" id="dedicated"></a>

[​Dedicated webhooks](https://developers.make.com/custom-apps-documentation/app-components/webhooks/dedicated) are the most common type. An individual URL is created and either automatically registered to the external platform or the user may need to configure it manually. The user can see the URL and copy it from the scenario.
