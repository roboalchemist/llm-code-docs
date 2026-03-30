# Source: https://redocly.com/learn/openapi/openapi-visual-reference/server-variables.md

# Server `variables`

## Server variable object

Server variables are used when you need to make a substitution into the server URL such as when the subdomain is unique per tenant.

| Field Name | Type | Description |
|  --- | --- | --- |
| default | string | **REQUIRED**. The default value to use for substitution, which SHALL be sent if an alternate value is *not* supplied. Note this behavior is different than the Schema Object's treatment of default values, because in those cases parameter values are optional. If the `enum` is defined, the value MUST exist in the enum's values. |
| enum | [string] | An enumeration of string values to be used if the substitution options are from a limited set. The array MUST NOT be empty. If defined, the array MUST contain the default value. |
| description | string | An optional description for the server variable. |


## Visuals

The following example defines a server variable `project` with a default value of `app`.


```yaml
servers:
  - url: https://{project}.redoc.ly
    description: Hosted docs
    variables:
      project:
        default: app
        description: The project name
```

The default server variable value displays in the documentation when `expandDefaultServerVariables: true`.

![default server variable substituted into server url](/assets/server-variables-01.88492afc19a12b07f583d7aba94f6721673e65b77def0ca7ae336d8caf1a8660.6f948c6e.png)

The placeholder server variable value displays in the documentation when `expandDefaultServerVariables: false`.

![server variable substituted into server url](/assets/server-variables-02.a921734f7724cfdba123fe9b736bc5dd8137ac0c41613b4fc6577f7379975b12.6f948c6e.png)

The try it console has server variable fields regardless of that setting.

![try it console server variable fields](/assets/server-variables-03.9e9825f67b1d1c6c8cb424ae1a2191f33c7d8884415d40a63f728edf61cae9e4.6f948c6e.png)

## Types

- `ServerVariable`



```ts
const ServerVariable: NodeType = {
  properties: {
    enum: {
      type: 'array',
      items: { type: 'string' },
    },
    default: { type: 'string' },
    description: null,
  },
  required: ['default'],
};
```