# Source: https://redocly.com/learn/openapi/openapi-visual-reference/external-docs.md

# `externalDocs`

Type: object (map)

| Field name | Type | Description |
|  --- | --- | --- |
| url | string | **REQUIRED.** The URL for the target documentation. |
| description | string | A description of the target documentation. Used as the link anchor text in Redocly. If not provided, the `url` is used as the link anchor text. |


You may only define one `externalDocs` url.

Placement
The external docs link renders before the `info.description` but after the `info.summary`.

## Visuals

The highlights are added for effect in the screenshots to call out the placement of the external docs link.


```yaml
externalDocs:
  url: https://redocly.com/docs/
  description: Read the Redocly docs
```

![externalDocs with description](/assets/external-docs-02.94bebb68cf64c42e00c4d5eaa403c6d87f2ab2e3780d363a9aedc5ff14b3afc8.6f948c6e.png)

### Example without `description`


```yaml
externalDocs:
  url: https://redocly.com/docs/
```

![externalDocs without description](/assets/external-docs-01.6b898ecf0efb703c820308a6f13beaf329ce3873043d76b1736af130c02e692f.6f948c6e.png)

## Recommended usage

Don't use `externalDocs` in combination with the `info.description`.
Instead, if there are external docs, include the links from the `info.description`.
This recommendation enables:

- more control of the context
- the possibility to include more than one link.


## Types

- `ExternalDocs`



```js
const ExternalDocs: NodeType = {
  properties: {
    description: { type: 'string' },
    url: { type: 'string' },
  },
  required: ['url'],
};
```