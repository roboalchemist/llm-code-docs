# Source: https://www.zuplo.com/docs/policies/acl-policy-inbound.md

# Access Control List Policy

:::tip{title="Custom Policy Example"}

Zuplo is extensible, so we don't have a built-in policy for Access Control List, instead we've a template here that shows you how you can use your superpower (code) to achieve your goals. To learn more about custom policies [see the documentation](/policies/custom-code-inbound).

:::

ACL policies can be built many ways depending on your requirements. This example
shows how to perform an authorization check on a hard-coded list of users.

This policy could be extended to fetch data from external sources or even use an
authorization service such as [OpenFGA](https://openfga.dev/).

```ts title="modules/my-policy.ts"
import { HttpProblems, ZuploContext, ZuploRequest } from "@zuplo/runtime";

interface PolicyOptions {
  users: string[];
}

export default async function (
  request: ZuploRequest,
  context: ZuploContext,
  options: PolicyOptions,
  policyName: string,
) {
  // Check that an authenticated user is set
  // NOTE: This policy requires an authentication policy to run before
  if (!request.user) {
    context.log.error(
      "User isn't authenticated. A authorization policy must come before the ACL policy.",
    );
    return HttpProblems.unauthorized(request, context);
  }

  // Check that the user has one of the allowed roles
  if (!options.users.includes(request.user.sub)) {
    context.log.error(
      `The user '${request.user.sub}' isn't authorized to perform this action.`,
    );
    return HttpProblems.forbidden(request, context);
  }

  // If they made it here, they are authorized
  return request;
}
```

## Configuration

The example below shows how to configure a custom code policy in the 'policies.json' document that utilizes the above example policy code.

```json title="config/policies.json"
{
  "name": "my-acl-policy-inbound-policy",
  "policyType": "acl-policy-inbound",
  "handler": {
    "export": "default",
    "module": "$import(./modules/YOUR_MODULE)",
    "options": {
      "users": ["google|12345", "google|23456"]
    }
  }
}
```

### Policy Configuration

- `name` <code className="text-green-600">&lt;string&gt;</code> - The name of your policy instance. This is used as a reference in your routes.
- `policyType` <code className="text-green-600">&lt;string&gt;</code> - The identifier of the policy. This is used by the Zuplo UI. Value should be `acl-policy-inbound`.
- `handler.export` <code className="text-green-600">&lt;string&gt;</code> - The name of the exported type. Value should be `default`.
- `handler.module` <code className="text-green-600">&lt;string&gt;</code> - The module containing the policy. Value should be `$import(./modules/YOUR_MODULE)`.
- `handler.options` <code className="text-green-600">&lt;object&gt;</code> - The options for this policy. [See Policy Options](#policy-options) below.

### Policy Options

The options for this policy are specified below. All properties are optional unless specifically marked as required.

- `users` **(required)** <code className="text-green-600">&lt;string[]&gt;</code> - The list of users authorized to access the resource

## Using the Policy

Read more about [how policies work](/articles/policies)
