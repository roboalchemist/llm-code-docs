# Source: https://www.zuplo.com/docs/policies/authzen-inbound.md

# AuthZEN Authorization Policy

This policy will authorize requests using a PDP (Policy Decision Point) service
that is compatible with the AuthZen standard. Read more about the
[AuthZen working group](https://openid.net/wg/authzen/).

It is designed to be extremely simple to configure, with a default configuration
that can dynamically read the `subject`, `resource` and `action` id from the
Zuplo request or context objects using the special
`$authzen-prop(request.headers.user-id)` syntax.

Example options:

```json
{
  "authorizerHostname": "authzen.example.com",
  "subject": {
    "type": "identity",
    "id": "$authzen-prop(request.user.sub)"
  },
  "resource": {
    "type": "route",
    "id": "$authzen-prop(context.route.path)"
  },
  "action": {
    "name": "$authzen-prop(request.method)"
  },
  "throwOnError": true // defaults to true if not specified
}
```

Note, the `$authzen-prop` syntax only works on this policy and on the `id` and
`name` properties.

:::caution{title="Beta"}

This policy is in beta. You can use it today, but it may change in non-backward compatible ways before the final release.

:::

:::info{title="Enterprise Feature"}

This policy is only available as part of our enterprise plans. It's free to try only any plan for development only purposes. If you would like to use this in production reach out to us: [sales@zuplo.com](mailto:sales@zuplo.com)

:::

## Configuration

The configuration shows how to configure the policy in the 'policies.json' document.

```json title="config/policies.json"
{
  "name": "my-authzen-inbound-policy",
  "policyType": "authzen-inbound",
  "handler": {
    "export": "AuthZenInboundPolicy",
    "module": "$import(@zuplo/runtime)",
    "options": {
      "action": {
        "name": "$authzen-prop(request.method)"
      },
      "authorizerAuthorizationHeader": "Bearer $env(AUTHZEN_PDP_TOKEN)",
      "authorizerHostname": "authzen.example.com",
      "resource": {
        "id": "$authzen-prop(context.route.path)",
        "type": "route"
      },
      "subject": {
        "id": "$authzen-prop(request.user.sub)",
        "type": "identity"
      },
      "throwOnError": true
    }
  }
}
```

### Policy Configuration

- `name` <code className="text-green-600">&lt;string&gt;</code> - The name of your policy instance. This is used as a reference in your routes.
- `policyType` <code className="text-green-600">&lt;string&gt;</code> - The identifier of the policy. This is used by the Zuplo UI. Value should be `authzen-inbound`.
- `handler.export` <code className="text-green-600">&lt;string&gt;</code> - The name of the exported type. Value should be `AuthZenInboundPolicy`.
- `handler.module` <code className="text-green-600">&lt;string&gt;</code> - The module containing the policy. Value should be `$import(@zuplo/runtime)`.
- `handler.options` <code className="text-green-600">&lt;object&gt;</code> - The options for this policy. [See Policy Options](#policy-options) below.

### Policy Options

The options for this policy are specified below. All properties are optional unless specifically marked as required.

- `authorizerHostname` **(required)** <code className="text-green-600">&lt;string&gt;</code> - The hostname of the AuthZen PDP service.
- `authorizerAuthorizationHeader` <code className="text-green-600">&lt;string&gt;</code> - The authorization header to use when communicating with the AuthZen PDP service.
- `subject` **(required)** <code className="text-green-600">&lt;object&gt;</code> - The subject of the request.
  - `type` **(required)** <code className="text-green-600">&lt;string&gt;</code> - The type of the resource.
  - `id` **(required)** <code className="text-green-600">&lt;string&gt;</code> - The id of the resource. Note you can use the `$authzen-prop()` syntax to reference the resource id.
- `resource` **(required)** <code className="text-green-600">&lt;object&gt;</code> - The resource of the request. Note you can use the `$authzen-prop()` syntax to reference the resource id.
  - `type` **(required)** <code className="text-green-600">&lt;string&gt;</code> - The type of the resource.
  - `id` **(required)** <code className="text-green-600">&lt;string&gt;</code> - The id of the resource. Note you can use the `$authzen-prop()` syntax to reference the resource id.
- `action` **(required)** <code className="text-green-600">&lt;object&gt;</code> - The action of the request. Note you can use the `$authzen-prop()` syntax to reference the action.
  - `name` **(required)** <code className="text-green-600">&lt;string&gt;</code> - The name of the action. Note you can use the `$authzen-prop()` syntax to reference the action name.
- `throwOnError` <code className="text-green-600">&lt;boolean&gt;</code> - If explicitly set to false, the policy will not throw an error if there is any problem communicating with the AuthZen PDP service and allow calls through. By default throwOnError is assumed to be on/true. Defaults to `true`.

## Using the Policy

By default, the policy will use the `subject`, `resource`, and `action`
properties from the policy options file, with the special `$authzen-prop()`
syntax to reference dynamic values.

However, you can also have programmatic control over the payload sent to the PDP
by setting the payload wholly or partially using the `setAuthorizationContext`
method in a custom policy _before_ the AuthZenInboundPolicy.

```ts
AuthZenInboundPolicy.setAuthorizationPayload(context, {
  subject: {
    type: "user",
    id: request.user.data.organization,
  },
  resource: {
    type: "pizza",
    id: ContextData.get(context, "pizza-size"),
  },
  action: { name: request.method },
});
```

This object will be combined with the one generated by the options with this
authorization payload set on context taking priority.

Read more about [how policies work](/articles/policies)
