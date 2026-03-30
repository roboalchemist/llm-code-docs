# Source: https://www.zuplo.com/docs/policies/web-bot-auth-inbound.md

# Web Bot Auth Policy

Authenticate bots using HTTP Message Signatures via the official web-bot-auth
npm package. This policy allows you to specify friendly bots and block others
based on configuration.

With this policy, you'll benefit from:

- **Enhanced API Security**: Protect your endpoints from unauthorized bot
  traffic while allowing legitimate bots
- **Cryptographic Verification**: Leverage HTTP Message Signatures to ensure
  bots are who they claim to be
- **Flexible Bot Management**: Easily configure which bots are allowed to access
  your API
- **Detailed Request Context**: Access bot identity information in subsequent
  policies or handlers
- **Seamless Integration**: Works with standard HTTP Message Signatures used by
  major bot providers

## Configuration

The configuration shows how to configure the policy in the 'policies.json' document.

```json title="config/policies.json"
{
  "name": "my-web-bot-auth-inbound-policy",
  "policyType": "web-bot-auth-inbound",
  "handler": {
    "export": "WebBotAuthInboundPolicy",
    "module": "$import(@zuplo/runtime)",
    "options": {
      "allowUnauthenticatedRequests": false,
      "allowedBots": [],
      "blockUnknownBots": true,
      "directoryUrl": null
    }
  }
}
```

### Policy Configuration

- `name` <code className="text-green-600">&lt;string&gt;</code> - The name of your policy instance. This is used as a reference in your routes.
- `policyType` <code className="text-green-600">&lt;string&gt;</code> - The identifier of the policy. This is used by the Zuplo UI. Value should be `web-bot-auth-inbound`.
- `handler.export` <code className="text-green-600">&lt;string&gt;</code> - The name of the exported type. Value should be `WebBotAuthInboundPolicy`.
- `handler.module` <code className="text-green-600">&lt;string&gt;</code> - The module containing the policy. Value should be `$import(@zuplo/runtime)`.
- `handler.options` <code className="text-green-600">&lt;object&gt;</code> - The options for this policy. [See Policy Options](#policy-options) below.

### Policy Options

The options for this policy are specified below. All properties are optional unless specifically marked as required.

- `allowedBots` **(required)** <code className="text-green-600">&lt;string[]&gt;</code> - List of bot identifiers that are allowed to access the API.
- `blockUnknownBots` **(required)** <code className="text-green-600">&lt;boolean&gt;</code> - Whether to block bots that aren't in the allowed list. Defaults to `true`.
- `allowUnauthenticatedRequests` <code className="text-green-600">&lt;boolean&gt;</code> - Allow requests without bot signatures to proceed. This is useful if you want to use multiple authentication policies or if you want to allow both authenticated and non-authenticated traffic. Defaults to `false`.
- `directoryUrl` <code className="text-green-600">&lt;string&gt;</code> - Optional URL to a directory of known bots (for verification). Defaults to `null`.

## Using the Policy

## How It Works

The policy checks for HTTP Message Signatures in the request headers
(`Signature` and `Signature-Input`). These signatures are verified using the
`web-bot-auth` npm package.

When a bot makes a request to your API, the policy:

1. Checks if the request has signature headers
2. Verifies the signature using the `web-bot-auth` library
3. Extracts the bot identity from the verified signature
4. Checks if the bot is in the allowed list
5. Either allows or blocks the request based on configuration

## Configuration Options

| Option                         | Type     | Required | Default | Description                                                  |
| ------------------------------ | -------- | -------- | ------- | ------------------------------------------------------------ |
| `allowedBots`                  | string[] | Yes      | -       | List of bot identifiers that are allowed to access the API   |
| `blockUnknownBots`             | boolean  | Yes      | true    | Whether to block bots that aren't in the allowed list        |
| `allowUnauthenticatedRequests` | boolean  | No       | false   | Allow requests without bot signatures to proceed             |
| `directoryUrl`                 | string   | No       | -       | Optional URL to a directory of known bots (for verification) |

## Example Configuration

```json
{
  "allowedBots": ["googlebot", "bingbot", "yandexbot"],
  "blockUnknownBots": true,
  "allowUnauthenticatedRequests": false,
  "directoryUrl": "https://example.com/bot-directory.json"
}
```

## Bot Directory

If you specify a `directoryUrl`, the policy will fetch the directory of known
bots from that URL. The directory should be a JSON object mapping bot
identifiers to their public keys in JWK format.

Example directory:

```json
{
  "googlebot": {
    "kty": "OKP",
    "crv": "Ed25519",
    "kid": "googlebot",
    "x": "..."
  },
  "bingbot": {
    "kty": "OKP",
    "crv": "Ed25519",
    "kid": "bingbot",
    "x": "..."
  }
}
```

## Request Context

When a bot is successfully authenticated, the policy adds the bot identity to
the request context. You can access this in subsequent policies or handlers
using the `getBotId` helper function:

```typescript
import { getBotId } from "@zuplo/runtime";

// In your policy or handler
const botId = getBotId(context);
```

## Error Handling

If a bot fails authentication, the policy returns a 401 Unauthorized response
with an error message. If a request doesn't have signature headers and
`allowUnauthenticatedRequests` is false, the policy also returns a 401 response.

## Cryptographic Verification

When a directory URL is provided, the policy performs cryptographic verification
of the bot signatures:

1. It fetches the bot's public key from the directory
2. Imports the key using the Web Crypto API
3. Verifies the signature against the request data

This provides strong cryptographic assurance that the bot is who it claims to
be.

## Implementation Details

The policy uses the `web-bot-auth` npm package to implement HTTP Message
Signatures verification. The implementation:

1. Uses the `verify` function from the `web-bot-auth` package to handle
   signature verification
2. Validates that the bot is in the allowed list
3. Optionally verifies the signature against a directory of known bots
4. Adds the verified bot identity to the request context

This implementation leverages the standard web-bot-auth library for bot
authentication, ensuring compatibility and security across different bot
providers.

Read more about [how policies work](/articles/policies)
