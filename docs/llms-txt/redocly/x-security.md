# Source: https://redocly.com/docs/respect/extensions/x-security.md

# x-security extension

Use the `x-security` extension to define authorization flows based on OpenAPI security schemes.
[Respect](https://redocly.com/respect) automatically constructs appropriate authorization headers, queries, or cookies based on your parameters.

## Configuration options

| Field name  | Type  | Description |
|  --- | --- | --- |
| schemeName | `string` | **REQUIRED.** Name of the security scheme from your OpenAPI specification.
Use with `operationId` or `operationPath` at the step level. |
| values | `object` | **REQUIRED.** Key-value pairs for security scheme parameters (e.g., `username`, `password` for Basic Authentication). |


**OR**

| Field name  | Type  | Description |
|  --- | --- | --- |
| scheme | [`securitySchemes`](/learn/openapi/openapi-visual-reference/security-schemes) | **REQUIRED.** Inline security scheme definition. |
| values | `object` | **REQUIRED.** Key-value pairs for security scheme parameters. |


## Supported authentication types

| Authentication type | Security scheme | Required values |
|  --- | --- | --- |
| Basic Authentication | type: httpscheme: basic | `username`, `password` |
| Digest Authentication | type: httpscheme: digest | `username`, `password` |
| Bearer Authentication | type: httpscheme: bearerbearerFormat?: JWT | `token` |
| API Keys | type: apiKeyin: header | query | cookiename: `string` | `apiKey` |


## Configure security schemes

Reference existing scheme
Reference a security scheme from your OpenAPI document's `components.securitySchemes`:


```yaml
workflows:
  - workflowId: fetchProducts
    steps:
      - stepId: getItemsStep
        operationId: getItems
        x-security:
          - schemeName: ApiKeyAuth
            values:
              apiKey: $inputs.API_KEY
```

This example uses an API key from your workflow inputs to authenticate requests.

Define inline scheme
Define a security scheme directly in your workflow:


```yaml
workflows:
  - workflowId: fetchProducts
    steps:
      - stepId: getItemsStep
        x-security:
          - scheme:
              type: http
              scheme: basic
            values:
              username: admin
              password: $inputs.PASSWORD
```

This example sets up Basic Authentication using credentials from your workflow inputs.

Combine multiple schemes
Apply multiple security schemes to a single request:


```yaml
workflows:
  - workflowId: fetchProducts
    steps:
      - stepId: getItemsStep
        operationId: getItems
        x-security:
          - schemeName: ApiKeyAuth
            values:
              apiKey: $inputs.API_KEY
          - scheme:
              type: http
              scheme: basic
            values:
              username: admin
              password: $inputs.PASSWORD
```

This example combines API Key authentication with Basic Authentication.

## Apply security at different levels

Apply security configuration at either the step or workflow level:

### Step-level security


```yaml
workflows:
  - workflowId: fetchProducts
    steps:
      - stepId: getItemsStep
        x-security:
          # Security configuration
```

### Workflow-level security


```yaml
workflows:
  - workflowId: fetchProducts
    x-security:
      # Security configuration
    steps:
      - stepId: getItemsStep
```

**Note:** Step-level security takes precedence over workflow-level security when conflicts occur.

## Choose between schemeName and scheme

- `schemeName`: Reference an existing OpenAPI security scheme.
Use at the step level with `operationId` or `operationPath`.
`schemeName` cannot be used with `x-operation`.
- `scheme`: Define a security scheme inline.
Use at any level without OpenAPI specification binding.


## Compare parameters and x-security

Use `x-security` instead of `parameters` for authentication to:

- Automatically handle security scheme transformations.
- Place values in the correct location.
- Simplify configuration.


Using parameters

```yaml
parameters:
  - name: Authorization
    in: header
    value: 'Bearer {$inputs.TOKEN}'
```

Using x-security with schemeName

```yaml
x-security:
  - schemeName: BearerAuth
    values:
      token: $inputs.TOKEN
```

Using x-security with scheme

```yaml
x-security:
  - scheme:
      type: http
      scheme: bearer
    values:
      token: $inputs.TOKEN
```

## Handle multiple security schemes

Process multiple security schemes in top-to-bottom order.
Merge schemes without conflicts.
For conflicting headers (e.g., `Authorization`), the last processed scheme takes precedence.

## Secure secret management

Store secrets in workflow inputs and reference them using `$inputs.<NAME>`:

1. Define an input parameter and use it inside values:



```yaml
workflows:
  - workflowId: fetchProducts
    # Define an input parameter used by this workflow.
    inputs:
      type: object
      properties:
        TOKEN:
          type: string
          format: password
    steps:
      stepId: getItemsStep
      x-security:
        - scheme:
            type: http
            scheme: bearer
          values:
            # Use the input parameter.
            token: $inputs.TOKEN
```

1. Pass the secret when running the workflow:



```bash
npx @redocly/cli respect arazzo-workflow.yaml --input TOKEN=<your-secret-value>
```

## Authentication scheme examples

Basic Auth

```yaml
x-security:
  - scheme:
      type: http
      scheme: basic
    values:
      username: user@example.com
      password: $inputs.PASSWORD
```

Generates: `Authorization: Basic dXNlckBleGFtcGxlLmNvbTpzZWNyZXQ=`

Digest Auth

```yaml
x-security:
  - scheme:
      type: http
      scheme: digest
    values:
      username: user@example.com
      password: $inputs.PASSWORD
```

Handles the Digest Authentication flow automatically:

1. Receives `401` with `WWW-Authenticate` header.
2. Computes required hashes.
3. Sends authenticated request.


Bearer Auth

```yaml
x-security:
  - scheme:
      type: http
      scheme: bearer
    values:
      token: $inputs.TOKEN
```

Generates: `Authorization: Bearer <your-secret-value>`

API Key

```yaml
x-security:
  - scheme:
      type: apiKey
      in: query
      name: key
    values:
      apiKey: $inputs.API_KEY
```

Generates: `?key=<your-secret-value>`

## Resources

- [Arazzo overview](/learn/arazzo/what-is-arazzo)
- [Respect commands](/docs/respect/commands)
- [Security schemes](/learn/openapi/openapi-visual-reference/security-schemes)