# Source: https://www.zuplo.com/docs/policies/moesif-inbound.md

# Moesif Analytics & Billing Policy

Moesif [moesif.com](https://moesif.com) is an API analytics and monetization
platform. This policy allows you to measure (and meter) API calls flowing
through your Zuplo gateway.

Add the policy to each route you want to meter. Note you can specify the Meter
API Name and Meter Value (meter increment) at the policy level.

## Configuration

The configuration shows how to configure the policy in the 'policies.json' document.

```json title="config/policies.json"
{
  "name": "my-moesif-inbound-policy",
  "policyType": "moesif-inbound",
  "handler": {
    "export": "MoesifInboundPolicy",
    "module": "$import(@zuplo/runtime)",
    "options": {
      "applicationId": "$env(MOESIF_APPLICATION_ID)",
      "logRequestBody": true,
      "logResponseBody": true
    }
  }
}
```

### Policy Configuration

- `name` <code className="text-green-600">&lt;string&gt;</code> - The name of your policy instance. This is used as a reference in your routes.
- `policyType` <code className="text-green-600">&lt;string&gt;</code> - The identifier of the policy. This is used by the Zuplo UI. Value should be `moesif-inbound`.
- `handler.export` <code className="text-green-600">&lt;string&gt;</code> - The name of the exported type. Value should be `MoesifInboundPolicy`.
- `handler.module` <code className="text-green-600">&lt;string&gt;</code> - The module containing the policy. Value should be `$import(@zuplo/runtime)`.
- `handler.options` <code className="text-green-600">&lt;object&gt;</code> - The options for this policy. [See Policy Options](#policy-options) below.

### Policy Options

The options for this policy are specified below. All properties are optional unless specifically marked as required.

- `applicationId` **(required)** <code className="text-green-600">&lt;string&gt;</code> - Your Moesif application ID.
- `logRequestBody` <code className="text-green-600">&lt;boolean&gt;</code> - Set to false to disable sending the request body to Moesif. Defaults to `true`.
- `logResponseBody` <code className="text-green-600">&lt;boolean&gt;</code> - Set to false to disable sending the response body to Moesif. Defaults to `true`.

## Using the Policy

By default, Zuplo will read the `request.user.sub` property and assign this as
the moesif `user_id` attribute when sending to Moesif. However, this and the
following attributes can be overriden in a
[custom code policy](/docs/policies/custom-code-inbound).

- `api_version`
- `company_id`
- `session_token`
- `user_id`
- `metadata`

Here is some example code that shows how to override two of these attributes

```ts
// Add this import at the top of your doc
import { setMoesifContext } from "@zuplo/runtime";

setMoesifContext(context, {
  userId: "user-1234",
  metadata: {
    some: "arbitrary",
    meta: "data",
  },
});
```

## Execute on every route

If you want to execute this policy on every route, you can add a hook in your
[runtime extensions](/docs/programmable-api/runtime-extensions) file
`zuplo.runtime.ts`:

```ts
import { RuntimeExtensions } from "@zuplo/runtime";

export function runtimeInit(runtime: RuntimeExtensions) {
  runtime.addRequestHook((request, context) => {
    return context.invokeInboundPolicy("moesif-inbound", request);
  });
}
```

Note you can add a guard clause around the context.invokeInboundPolicy if you
want to exclude a few routes.

Read more about [how policies work](/articles/policies)
