# Source: https://redocly.com/docs/realm/config/openapi/download-urls.md

# `downloadUrls`

Set the URLs used to download the OpenAPI description or other documentation related files from the API documentation page.

## Options

| Option | Type | Description |
|  --- | --- | --- |
| downloadUrls | [[downloadUrls object](#api-description-url-object)] | Set the URLs used to download the OpenAPI description or other related to documentation files from the API documentation. |


### API description URL object

| Option | Type | Description |
|  --- | --- | --- |
| title | string | Custom title to use for displaying in *Download OpenAPI specification section* for specific url.
This title can help users quickly identify what the content is about
or what it represents before they access the download URL provided in the object. |
| url | string | --REQUIRED.--
An absolute URL to the file. |


## Examples

The following example sets the download URLs for an OpenAPI description:


```yaml redocly.yaml
openapi:
  downloadUrls:
    - title: Download OpenApiDescription
      url: 'https://example.com/museum.yaml'
```

## Resources

- **[OpenAPI configuration](/docs/realm/config/openapi)** - Complete guide to OpenAPI configuration options for customizing API reference documentation
- **[Hide download buttons](/docs/realm/config/openapi/hide-download-buttons)** - Toggle the appearance of download buttons used to access your API description files
- **[OpenAPI Specification](https://spec.openapis.org/oas/latest.html)** - Official OpenAPI Specification documentation for understanding API description standards
- [OpenAPI visual reference](https://redocly.com/learn/openapi/openapi-visual-reference)
- Explore other [configuration options](/docs/realm/config) for your project.