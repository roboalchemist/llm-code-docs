# Source: https://www.zuplo.com/docs/policies/set-headers-inbound.md

# Add or Set Request Headers Policy

The set header policy adds a header to the request in the inbound pipeline. This
can be used to set a security header required by the downstream service.

## Configuration

The configuration shows how to configure the policy in the 'policies.json' document.

```json title="config/policies.json"
{
  "name": "my-set-headers-inbound-policy",
  "policyType": "set-headers-inbound",
  "handler": {
    "export": "SetHeadersInboundPolicy",
    "module": "$import(@zuplo/runtime)",
    "options": {
      "headers": [
        {
          "name": "my-custom-header",
          "value": "test"
        }
      ]
    }
  }
}
```

### Policy Configuration

- `name` <code className="text-green-600">&lt;string&gt;</code> - The name of your policy instance. This is used as a reference in your routes.
- `policyType` <code className="text-green-600">&lt;string&gt;</code> - The identifier of the policy. This is used by the Zuplo UI. Value should be `set-headers-inbound`.
- `handler.export` <code className="text-green-600">&lt;string&gt;</code> - The name of the exported type. Value should be `SetHeadersInboundPolicy`.
- `handler.module` <code className="text-green-600">&lt;string&gt;</code> - The module containing the policy. Value should be `$import(@zuplo/runtime)`.
- `handler.options` <code className="text-green-600">&lt;object&gt;</code> - The options for this policy. [See Policy Options](#policy-options) below.

### Policy Options

The options for this policy are specified below. All properties are optional unless specifically marked as required.

- `headers` **(required)** <code className="text-green-600">&lt;object[]&gt;</code> - An array of headers to set in the request. By default, headers will be overwritten if they already exists in the request, specify the overwrite property to change this behavior.
  - `name` **(required)** <code className="text-green-600">&lt;string&gt;</code> - The name of the header.
  - `value` **(required)** <code className="text-green-600">&lt;string&gt;</code> - The value of the header.
  - `overwrite` <code className="text-green-600">&lt;boolean&gt;</code> - Overwrite the value if the header is already present in the request. Defaults to `true`.

## Using the Policy

An example for using this policy is if your backend service uses basic
authentication you might use this policy to attach the Basic auth header to the
request:

```json
{
  "export": "SetHeadersInboundPolicy",
  "module": "$import(@zuplo/runtime)",
  "options": {
    "headers": [
      {
        "name": "Authorization",
        "value": "Basic DIGEST_HERE",
        "overwrite": true
      }
    ]
  }
}
```

When doing this, you most likely want to set the secret as an environment
variable, which can be accessed in the policy as follows

```json
{
  "export": "SetHeadersInboundPolicy",
  "module": "$import(@zuplo/runtime)",
  "options": {
    "headers": [
      {
        "name": "Authorization",
        "value": "$env(BASIC_AUTHORIZATION_HEADER_VALUE)",
        "overwrite": true
      }
    ]
  }
}
```

And you would set the environment variable `BASIC_AUTHORIZATION_HEADER_VALUE` to
`Basic DIGEST_HERE`.

Read more about [how policies work](/articles/policies)
