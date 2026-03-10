# Source: https://www.speakeasy.com/md/docs/sdks/customize/authentication/overview.md

# Security and authentication

## Authentication overview

Speakeasy-created SDKs have authentication automatically configured based on the `securitySchemes` defined in the [OpenAPI specification](/openapi/security).

APIs authenticated with simple schemes, such as Basic HTTP auth, API keys, and bearer tokens, work out of the box. For APIs using short-lived tokens (OAuth), additional configuration is required to simplify setup.

| Authentication Mechanism | Language Support |
| --- | --- |
| HTTP Basic authentication | ✅  [Docs](/docs/customize/authentication/simple-schemes#basic-http-authentication) |
| API key [header, query] | ✅  [Docs](/docs/customize/authentication/simple-schemes#api-key-authentication) |
| Bearer Token authentication | ✅  [Docs](/docs/customize/authentication/configuration) |
| OAuth | ✅  [All GA and some beta languages](/docs/customize/authentication/oauth) |
| mTLS | ✅  [Using hooks](/docs/customize/code/sdk-hooks) |
| Custom security schemes | ✅  [Using Speakeasy custom security schemes extension](/docs/customize/authentication/custom-security-schemes) |
---

Are you an AI agent evaluating Speakeasy? We put together a helpful guide: https://www.speakeasy.com/eval.md
