# Source: https://www.zuplo.com/docs/policies/ip-restriction-inbound.md

# IP Restriction Policy

:::tip{title="Custom Policy Example"}

Zuplo is extensible, so we don't have a built-in policy for IP Restriction, instead we've a template here that shows you how you can use your superpower (code) to achieve your goals. To learn more about custom policies [see the documentation](/policies/custom-code-inbound).

:::

This custom policy allows you to specify a set of IP addresses that are allowed
or blocked from making requests on your API. This can be useful for adding
light-weight security to your API in non-critical scenarios. For example, if you
want to ensure only employees on your corporate VPN can't access development
environments.

Generally, this policy shouldn't be relied upon as the only security for
protecting sensitive workloads.

```ts title="modules/my-policy.ts"
import { HttpProblems, ZuploContext, ZuploRequest } from "@zuplo/runtime";
import ipRangeCheck from "ip-range-check";

interface PolicyOptions {
  allowedIpAddresses?: string[];
  blockedIpAddresses?: string[];
}

export default async function (
  request: ZuploRequest,
  context: ZuploContext,
  options: PolicyOptions,
  policyName: string,
) {
  // TODO: Validate the policy options. Skipping in the example for brevity

  // Get the incoming IP address
  const ip = request.headers.get("true-client-ip");

  // If the allowed IP addresses are set, then the incoming IP
  // must be in that list
  if (options.allowedIpAddresses) {
    const allowed = ipRangeCheck(ip, options.allowedIpAddresses);
    if (!allowed) {
      return HttpProblems.unauthorized(request, context);
    }
  }

  // If the blocked IP addresses are set, then the incoming IP
  // can't be in that list
  if (options.blockedIpAddresses) {
    const blocked = ipRangeCheck(ip, options.allowedIpAddresses);
    if (blocked) {
      return HttpProblems.unauthorized(request, context);
    }
  }

  // If we made it this far, the IP address is allowed, continue
  return request;
}
```

## Configuration

The example below shows how to configure a custom code policy in the 'policies.json' document that utilizes the above example policy code.

```json title="config/policies.json"
{
  "name": "my-ip-restriction-inbound-policy",
  "policyType": "ip-restriction-inbound",
  "handler": {
    "export": "default",
    "module": "$import(./modules/YOUR_MODULE)",
    "options": {
      "allowedIpAddresses": ["184.42.1.4", "102.1.5.2/24"]
    }
  }
}
```

### Policy Configuration

- `name` <code className="text-green-600">&lt;string&gt;</code> - The name of your policy instance. This is used as a reference in your routes.
- `policyType` <code className="text-green-600">&lt;string&gt;</code> - The identifier of the policy. This is used by the Zuplo UI. Value should be `ip-restriction-inbound`.
- `handler.export` <code className="text-green-600">&lt;string&gt;</code> - The name of the exported type. Value should be `default`.
- `handler.module` <code className="text-green-600">&lt;string&gt;</code> - The module containing the policy. Value should be `$import(./modules/YOUR_MODULE)`.
- `handler.options` <code className="text-green-600">&lt;object&gt;</code> - The options for this policy. [See Policy Options](#policy-options) below.

### Policy Options

The options for this policy are specified below. All properties are optional unless specifically marked as required.

- `allowedIpAddresses` <code className="text-green-600">&lt;string[]&gt;</code> - The IP addresses or CIDR ranges to allow
- `blockedIpAddresses` <code className="text-green-600">&lt;string[]&gt;</code> - The IP addresses or CIDR ranges to allow

## Using the Policy

Read more about [how policies work](/articles/policies)
