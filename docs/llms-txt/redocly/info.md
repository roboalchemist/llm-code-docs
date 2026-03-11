# Source: https://redocly.com/docs/realm/config/graphql/info.md

# Source: https://redocly.com/learn/openapi/openapi-visual-reference/info.md

# `info`

**REQUIRED**

Type: object (map)

| Field name | Type | Description |
|  --- | --- | --- |
| title | string | **REQUIRED.** The title of the API. |
| version | string | **REQUIRED.** The version of the OpenAPI document (which is distinct from the OpenAPI Specification version or the API implementation version). |
| description | string | **RECOMMENDED.** A description of the API (Markdown may be used). |
| summary | string | A short summary of the API. |
| termsOfService | string | A URL to the Terms of Service for the API. |
| contact | [Contact object](/learn/openapi/openapi-visual-reference/contact) | The contact information for the exposed API. |
| license | [License object](/learn/openapi/openapi-visual-reference/license) | The license information for the exposed API. |
| x-logo | [Logo object](https://redoc.ly/docs-legacy/api-reference-docs/specification-extensions/x-logo/) | A commonly used specification extension containing the information about the API logo. |


## Visuals

The following is an example of a minimally recommended OpenAPI `info` object:


```yaml
info:
  title: Example
  version: '1.0'
  description: |
    # My API description in Markdown

    This is a sample of an info description.
```

See how it renders in Redocly OpenAPI documentation.

![info-render](/assets/info-1.ec44d4f61b83e2ee327635975a9bf92b72bc75c56051987a74c1b792f1f4bdb4.6f948c6e.png)

### `version` Examples

The version is required.
But sometimes an API document doesn't have a sensible version.
To hide it from the documentation, change it to an empty string.


```yaml
info:
  title: Example
  version: ''
  description: |
    # My API description in Markdown

    This is a sample of an info description.
```

![info without version](/assets/info-2.babd28313d0ce0bb77e5d091933d0b7f0159a3d1b3645e73e850ea66154363bb.6f948c6e.png)

### `description` Examples

The H1 and H2 tags from the `description` are pulled into the sidebar navigation.
When an H2 appears after an H1 tag, the preceding H1 tag turns into a group in the sidebar navigation.
The chevron indicates that a group can be expanded.


```yaml
info:
  title: Example
  version: ''
  description: |
    # My API description in Markdown

    This is a sample of an info description.

    # Another H1

    This is body paragraph text.

    ## H2 level heading
```

![headings in info description](/assets/info-3.6a1982bc4c08f4040b8cbc01d6ecac1ee68057196b088601d20eabf9ce97bfe3.6f948c6e.png)

The following image shows the expansion of the group.

![headings in info description with group expansion](/assets/info-4.7060064ee72f7315cbcfe72da5eba8b1e3c7a3e6e7539182575b05fd94351548.6f948c6e.png)

### `summary` Examples

The following example contains a summary.


```yaml
info:
  title: Example
  version: ''
  description: |
    # My API description in Markdown

    This is a sample of an info description.
  summary: This is a sample summary
```

The `summary` renders before the `description`.

![info summary](/assets/info-5.a0d4f398171ac94680c7a432742f490b048a8e0d48028a0981ce3b0cfe9c67b1.6f948c6e.png)

### `termsOfService` example

The following example defines a `termsOfService` URL.


```yaml
info:
  title: Example
  version: ''
  description: |
    # My API description in Markdown

    This is a sample of an info description.
  termsOfService: https://redoc.ly/subscription-agreement/
```

![info termsOfService](/assets/info-6.c9f4ebc1dfeb748b55bba3555e3dbc02978040d34b409366d4f6985d86f6420b.6f948c6e.png)

### Example with everything


```yaml
info:
  title: Example
  version: ''
  description: |
    # My API description in Markdown

    This is a sample of an info description.
  summary: This is a summary
  termsOfService: https://redoc.ly/subscription-agreement/
  contact:
    name: API team
    email: team@redocly.com
    url: https://redocly.com/contact-us/
  license:
    name: MIT
    url: https://opensource.org/licenses/MIT
```

![info everything](/assets/info-9.506e55bc8e77e4bdd6fb82d89091b0f20f44bfb9433ad8beb655a665b6340d44.6f948c6e.png)

## Types

- `Info`



```js
const Info: NodeType = {
  properties: {
    title: { type: 'string' },
    version: { type: 'string' },
    description: { type: 'string' },
    termsOfService: { type: 'string' },
    contact: 'Contact',
    license: 'License',
  },
  required: ['title', 'version'],
};
```