# Source: https://redocly.com/docs/realm/config/openapi.md

# Source: https://redocly.com/learn/openapi/openapi-visual-reference/openapi.md

# `openapi`

**REQUIRED**

Type: `string`

> This string MUST be the semantic version number of the OpenAPI Specification version that the OpenAPI document uses. The openapi field SHOULD be used by tooling specifications and clients to interpret the OpenAPI document. This is not related to the API info.version string.


## Visuals

There is no visual example for this particular property.


```yaml
openapi: 3.0.3
```


```yaml
openapi: 3.1.0
```

The value for the `openapi` map must be a string.
The values `3.0` or `3.1` convert to a number by YAML processors so it isn't correct unless it's quoted to indicate it's a string.


```yaml
openapi: "3.0"
```

The closest thing to a visual is the download button.

![download button](/assets/openapi-download-button.b31883ee2058e82063aa635b9822788e105b0e4bb381062ffe1fa70572872dfe.6f948c6e.png)

The download button can be disabled with the configuration option `hideDownloadButton` set to `true`.

## Types

The `openapi` property is part of the root object.
The name for the root object is `Root`:

- `Root`


Swagger 2.0
Prior to version 3.0.0, the root object property was named `swagger`.