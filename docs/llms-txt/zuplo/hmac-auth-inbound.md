# Source: https://www.zuplo.com/docs/policies/hmac-auth-inbound.md

# HMAC Auth Policy

:::tip{title="Custom Policy Example"}

Zuplo is extensible, so we don't have a built-in policy for HMAC Auth, instead we've a template here that shows you how you can use your superpower (code) to achieve your goals. To learn more about custom policies [see the documentation](/policies/custom-code-inbound).

:::

This example policy demonstrates how to use a shared secret to create an
[HMAC](https://en.wikipedia.org/wiki/HMAC) signature to sign a payload (in this
case the body). When the request is sent, the signature is sent in the request
header. The policy can then verify that the signature matches the payload - thus
ensuring that the sender had the same shared secret.

This policy is configured with the value of the `secret`. Normally, you would
store this as an environment variable secret. Additionally, the policy option
`headerName` is used to set the header that will be used by the client to send
the signature.

```ts title="modules/my-policy.ts"
import { HttpProblems, ZuploContext, ZuploRequest } from "@zuplo/runtime";

interface PolicyOptions {
  secret: string;
  headerName: string;
}

export default async function (
  request: ZuploRequest,
  context: ZuploContext,
  options: PolicyOptions,
  policyName: string,
) {
  // Validate the policy options
  if (typeof options.secret !== "string") {
    throw new Error(
      `The option 'secret' on policy '${policyName}' must be a string. Received ${typeof options.secret}.`,
    );
  }
  if (typeof options.headerName !== "string") {
    throw new Error(
      `The option 'headerName' on policy '${policyName}' must be a string. Received ${typeof options.headerName}.`,
    );
  }

  // Get the authorization header
  const token = request.headers.get(options.headerName);

  // No auth header, unauthorized
  if (!token) {
    return HttpProblems.unauthorized(request, context);
  }

  // Convert the hex encoded token to an Uint8Array
  const tokenData = new Uint8Array(
    token.match(/../g)!.map((h) => parseInt(h, 16)),
  );

  // Get the data to verify
  // This could be anything (headers, query parameter, etc.)
  // For this example, we will just verify the entire body value
  const data = await request.text();

  // Create a crypto key from a secret stored as an environment variable
  const encoder = new TextEncoder();
  const encodedSecret = encoder.encode(options.secret);
  const key = await crypto.subtle.importKey(
    "raw",
    encodedSecret,
    { name: "HMAC", hash: "SHA-256" },
    false,
    ["verify"],
  );

  // Verify that the data
  const verified = await crypto.subtle.verify(
    "HMAC",
    key,
    tokenData,
    encoder.encode(data),
  );

  // Check if the data is verified, if not return unauthorized
  if (!verified) {
    return HttpProblems.unauthorized(request, context);
  }

  // Request is authorized, continue
  return request;
}
```

## Configuration

The example below shows how to configure a custom code policy in the 'policies.json' document that utilizes the above example policy code.

```json title="config/policies.json"
{
  "name": "my-hmac-auth-inbound-policy",
  "policyType": "hmac-auth-inbound",
  "handler": {
    "export": "default",
    "module": "$import(./modules/YOUR_MODULE)",
    "options": {
      "secret": "$env(MY_SECRET)",
      "headerName": "signed-request"
    }
  }
}
```

### Policy Configuration

- `name` <code className="text-green-600">&lt;string&gt;</code> - The name of your policy instance. This is used as a reference in your routes.
- `policyType` <code className="text-green-600">&lt;string&gt;</code> - The identifier of the policy. This is used by the Zuplo UI. Value should be `hmac-auth-inbound`.
- `handler.export` <code className="text-green-600">&lt;string&gt;</code> - The name of the exported type. Value should be `default`.
- `handler.module` <code className="text-green-600">&lt;string&gt;</code> - The module containing the policy. Value should be `$import(./modules/YOUR_MODULE)`.
- `handler.options` <code className="text-green-600">&lt;object&gt;</code> - The options for this policy. [See Policy Options](#policy-options) below.

### Policy Options

The options for this policy are specified below. All properties are optional unless specifically marked as required.

- `secret` **(required)** <code className="text-green-600">&lt;string&gt;</code> - The secret to use for HMAC authentication
- `headerName` **(required)** <code className="text-green-600">&lt;string&gt;</code> - The header where the HMAC signature is send

## Using the Policy

The example below demonstrates how you could sign a value in order to create an
HMAC signature for use with this policy.

```ts
const token = await sign("my data", environment.MY_SECRET);

async function sign(
  key: string | ArrayBuffer,
  val: string,
): Promise<ArrayBuffer> {
  const encoder = new TextEncoder();
  const cryptoKey = await crypto.subtle.importKey(
    "raw",
    typeof key === "string" ? encoder.encode(key) : key,
    { name: "HMAC", hash: { name: "SHA-256" } },
    false,
    ["sign"],
  );
  const token = await crypto.subtle.sign(
    "HMAC",
    cryptoKey,
    encoder.encode(val),
  );
  return Array.prototype.map
    .call(new Uint8Array(token), function (x) {
      return ("0" + x.toString(16)).slice(-2);
    })
    .join("");
}
```

Read more about [how policies work](/articles/policies)
