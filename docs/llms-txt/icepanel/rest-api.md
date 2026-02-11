# Source: https://docs.icepanel.io/integrations/rest-api.md

# REST API

## Introduction

The IcePanel REST API is publicly accessible to write automated scripts or custom integrations with external tools.

## Authentication

First generate an API key on your organization management screen. Make sure to copy your key now as you won't be able to see it again for security reasons!

You can then set the `Authorization` HTTP header on any authenticated requests.

```bash
Authorization: ApiKey SH5XAiWtgevC2ZfQym3i:17a9c60035eed62c8f4f195c754ee6972ffc40ce975c5571ec521f463ebefa7f
```

## Example

See the example below for how to request a list of projects using `curl`.

```bash
curl 'https://api.icepanel.io/v1/organizations/{organizationId}/landscapes' \
  -H 'Accept: application/json' \                                                                                
  -H 'Authorization: ApiKey SH5XAiWtgevC2ZfQym3i:17a9c60035eed62c8f4f195c754ee6972ffc40ce975c5571ec521f463ebefa7f'
```

## API reference

Checkout the full API reference here: <https://developer.icepanel.io/api-reference/>
