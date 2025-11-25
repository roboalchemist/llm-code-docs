# Source: https://docs.fireworks.ai/getting-started/introduction.md

# Source: https://docs.fireworks.ai/examples/introduction.md

# Source: https://docs.fireworks.ai/api-reference/introduction.md

# Source: https://docs.fireworks.ai/getting-started/introduction.md

# Source: https://docs.fireworks.ai/examples/introduction.md

# Source: https://docs.fireworks.ai/api-reference/introduction.md

# Introduction

Fireworks AI REST API enables you to interact with various language, image and embedding models using an API Key. It also lets you automate management of models, deployments, datasets, and more.

## Authentication

All requests made to the Fireworks AI REST API must include an `Authorization` header with a valid `Bearer` token using your API key, along with the `Content-Type: application/json` header.

### Getting your API key

You can obtain an API key by:

* Using the [`firectl create api-key`](/tools-sdks/firectl/commands/create-api-key) command
* Generating one through the [Fireworks AI dashboard](https://app.fireworks.ai/settings/users/api-keys)

### Request headers

Include the following headers in your REST API requests:

```json  theme={null}
authorization: Bearer <API_KEY>
content-type: application/json
```
