# Source: https://www.zuplo.com/docs/policies/secret-masking-outbound.md

# Secret Masking Policy

The Secret Masking policy searches for and masks common secrets and replaces
them with a placeholder. Secrets that are automatically masked include:

- Zuplo API keys
- GitHub Tokens and Personal Access Tokens
- Private key blocks
- And more!

See the [policy documentation](https://zuplo.com/docs/policies/overview) for a
full description of secrets that are masked via this policy.

This is especially useful as an outbound policy for MCP servers, APIs that
interface with user generated content, or AI consumers.

## Configuration

The configuration shows how to configure the policy in the 'policies.json' document.

```json title="config/policies.json"
{
  "name": "my-secret-masking-outbound-policy",
  "policyType": "secret-masking-outbound",
  "handler": {
    "export": "SecretMaskingOutboundPolicy",
    "module": "$import(@zuplo/runtime)",
    "options": {
      "additionalPatterns": [],
      "mask": "[REDACTED]"
    }
  }
}
```

### Policy Configuration

- `name` <code className="text-green-600">&lt;string&gt;</code> - The name of your policy instance. This is used as a reference in your routes.
- `policyType` <code className="text-green-600">&lt;string&gt;</code> - The identifier of the policy. This is used by the Zuplo UI. Value should be `secret-masking-outbound`.
- `handler.export` <code className="text-green-600">&lt;string&gt;</code> - The name of the exported type. Value should be `SecretMaskingOutboundPolicy`.
- `handler.module` <code className="text-green-600">&lt;string&gt;</code> - The module containing the policy. Value should be `$import(@zuplo/runtime)`.
- `handler.options` <code className="text-green-600">&lt;object&gt;</code> - The options for this policy. [See Policy Options](#policy-options) below.

### Policy Options

The options for this policy are specified below. All properties are optional unless specifically marked as required.

- `mask` <code className="text-green-600">&lt;string&gt;</code> - The string to replace detected secrets with. Defaults to `"[REDACTED]"`.
- `additionalPatterns` <code className="text-green-600">&lt;string[]&gt;</code> - Extra regex patterns for secrets to mask.

## Using the Policy

This policy masks sensitive secrets in outgoing requests to prevent exposure to
downstream consumers. This is especially useful for AI agents and MCP clients
(where LLMs should not consume potentially sensitive user generated information
or poisoned agents are attempting to leak information they have access to).

## Configuration

- `mask`: The mask to use when redacting information. **Default:** `[REDACTED]`
- `additionalPatterns`: Additional Regex patterns to mask secrets with (make
  sure to correctly escape "meta escape" characters: i.e., `\b` should be
  escaped `\\b` to avoid a JSON parsing error. Otherwise, you may see build
  errors).

## Usage

Apply this policy to outbound requests in your route configuration:

```json
{
  "policies": [
    {
      "name": "secret-masking-policy",
      "policyType": "secret-masking-outbound",
      "handler": {
        "export": "SecretMaskingOutboundPolicy",
        "module": "$import(@zuplo/runtime)",
        "options": {
          "mask": "<SECRET MASKED>",
          "additionalPatterns": ["\\b(\\w+)=\\w+\\b"]
        }
      }
    }
  ]
}
```

# Masked secrets

- Zuplo API keys (i.e. `zpka_xxx`)
- GitHub Tokens and Personal Access Tokens (i.e. `ghp_xxx`)
- Private key blocks (i.e. `BEGIN PRIVATE KEY` and `END PRIVATE KEY`)

Read more about [how policies work](/articles/policies)
