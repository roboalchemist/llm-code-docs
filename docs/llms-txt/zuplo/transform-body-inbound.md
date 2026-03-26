# Source: https://www.zuplo.com/docs/policies/transform-body-inbound.md

# Transform Request Body Policy

:::tip{title="Custom Policy Example"}

Zuplo is extensible, so we don't have a built-in policy for Transform Request Body, instead we've a template here that shows you how you can use your superpower (code) to achieve your goals. To learn more about custom policies [see the documentation](/policies/custom-code-inbound).

:::

This example policy shows how to use `request.json()` to read the incoming
request as a JSON object. The object can then be modified as appropriate. It's
then converted back to a string and a new `Request` is returned in the policy
with the new body.

If the incoming request body isn't JSON, you can use `request.text()` or
`request.blob()` to access the contents as raw text or a
[blob](https://developer.mozilla.org/en-US/docs/Web/API/Request/blob).

```ts title="modules/my-policy.ts"
import { ZuploContext, ZuploRequest } from "@zuplo/runtime";

export default async function (request: ZuploRequest, context: ZuploContext) {
  // Get the incoming body as an Object
  const obj = await request.json();

  // Modify the object as required
  obj.myNewProperty = "Hello World";

  // Stringify the object
  const body = JSON.stringify(obj);

  // Return a new request based on the
  // original but with the new body
  return new ZuploRequest(request, { body });
}
```

## Configuration

The example below shows how to configure a custom code policy in the 'policies.json' document that utilizes the above example policy code.

```json title="config/policies.json"
{
  "name": "transform-body-inbound",
  "policyType": "custom-code-inbound",
  "handler": {
    "export": "default",
    "module": "$import(./modules/transform-body-inbound)"
  }
}
```

### Policy Configuration

- `name` <code className="text-green-600">&lt;string&gt;</code> - The name of your policy instance. This is used as a reference in your routes.
- `policyType` <code className="text-green-600">&lt;string&gt;</code> - The identifier of the policy. This is used by the Zuplo UI. Value should be `transform-body-inbound`.
- `handler.export` <code className="text-green-600">&lt;string&gt;</code> - The name of the exported type. Value should be `default`.
- `handler.module` <code className="text-green-600">&lt;string&gt;</code> - The module containing the policy. Value should be `$import(./modules/YOUR_MODULE)`.

## Using the Policy

Read more about [how policies work](/articles/policies)
