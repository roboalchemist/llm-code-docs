# Source: https://www.zuplo.com/docs/policies/ab-test-outbound.md

# A/B Test Outbound Policy

:::tip{title="Custom Policy Example"}

Zuplo is extensible, so we don't have a built-in policy for A/B Test Outbound, instead we've a template here that shows you how you can use your superpower (code) to achieve your goals. To learn more about custom policies [see the documentation](/policies/custom-code-outbound).

:::

This example shows how to perform an action on incoming requests based on the
result of a randomly generated number. A/B tests could also be performed on
properties such as the `request.user`.

A/B tests can also be combined with other policies by passing data to downstream
policies. For example, you could save a value in `ContextData` based on the
results of the A/B test and use that value in a later policy to modify the
request.

```ts title="modules/my-policy.ts"
import { ZuploContext, ZuploRequest } from "@zuplo/runtime";

export default async function (
  response: Response,
  request: ZuploRequest,
  context: ZuploContext,
) {
  // Generate a random number to segment the test groups
  const score = Math.random();

  // Get the outgoing response body
  const data = await response.json();

  // Modify the body based on the random value
  if (score < 0.5) {
    data.testEnabled = true;
  } else {
    data.testEnabled = false;
  }

  // Stringify the data object
  const body = JSON.stringify(data);

  // Return a new response with the updated body
  return new Response(body, response);
}
```

## Configuration

The example below shows how to configure a custom code policy in the 'policies.json' document that utilizes the above example policy code.

```json title="config/policies.json"
{
  "name": "ab-test-outbound",
  "policyType": "custom-code-outbound",
  "handler": {
    "export": "default",
    "module": "$import(./modules/ab-test-outbound)"
  }
}
```

### Policy Configuration

- `name` <code className="text-green-600">&lt;string&gt;</code> - The name of your policy instance. This is used as a reference in your routes.
- `policyType` <code className="text-green-600">&lt;string&gt;</code> - The identifier of the policy. This is used by the Zuplo UI. Value should be `ab-test-outbound`.
- `handler.export` <code className="text-green-600">&lt;string&gt;</code> - The name of the exported type. Value should be `default`.
- `handler.module` <code className="text-green-600">&lt;string&gt;</code> - The module containing the policy. Value should be `$import(./modules/YOUR_MODULE)`.

## Using the Policy

Read more about [how policies work](/articles/policies)
