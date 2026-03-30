# Source: https://redocly.com/learn/openapi/openapi-visual-reference/servers.md

# `servers`

> A server object to be used by the target operation.


Type: List of Server Objects

| Field Name | Type | Description |
|  --- | --- | --- |
| url | `string` | **REQUIRED**. A URL to the target host. This URL supports Server Variables and MAY be relative, to indicate that the host location is relative to the location where the OpenAPI document is being served. Variable substitutions are made when a variable is named in `{` curly braces `}`. |
| description | `string` | An optional string describing the host designated by the URL. |
| variables | Map[`string`, [Server Variable Object](/learn/openapi/openapi-visual-reference/server-variables)] | A map between a variable name and its value. The value is used for substitution in the server's URL template. |


Servers can be defined at the definition root and also at the path item level.
The path item servers, if defined, take precedence over the definition root servers.

## Visuals

### Example with a single server

The following example is of a single server.


```yaml
servers:
  - url: https://api.redocly.com
```

### Example with two servers


```yaml
servers:
  - url: https://api.redocly.com
  - url: https://sandbox.redocly.com
```

![two servers](/assets/servers-03.b1c7045866216e5540d85b41268090aa85b0d945063ac96ed817e2bd3a9dd43c.6f948c6e.png)

### Example with description


```yaml
servers:
  - url: https://api.redocly.com
    description: Production
  - url: https://sandbox.redocly.com
    description: Sandbox
```

![two servers with descriptions](/assets/servers-03.b1c7045866216e5540d85b41268090aa85b0d945063ac96ed817e2bd3a9dd43c.6f948c6e.png)

The servers can be displayed in the center panel by setting the `pathInMiddlePanel: true` option.

![server urls with descriptions](/assets/servers-04.592bfd6f5f1a1db4067c3b89dbec5bf1a045c549d86934e168f7455670de1cc8.6f948c6e.png)

## Types

- `ServerList`
- `Server`
- `ServerVariable`


![server-list](/assets/server-list.40fa7d1e15f61ba27ff9273998c0196dcd7c18a1dd25233e170cd5aacb3d2e55.6f948c6e.png)


```mermaid
erDiagram
          ServerList ||..|{ Server : has
          Server ||..o{ ServerVariable : has
```