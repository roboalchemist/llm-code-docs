# Source: https://redocly.com/docs/realm/config/openapi/hide-download-buttons.md

# `hideDownloadButtons`

Publishing an API description is as valuable to your users as publishing documentation, and by default your users can download the OpenAPI file from the API reference docs.
We recommend making the files available but in some situations, you may want to hide the buttons to discourage downloading, for example of a legacy API.

The `hideDownloadButtons` option controls whether the **Download OpenAPI description** section on the info page of the API documentation is hidden.

The `hideDownloadButtons` setting doesn't make your API description private.
It only stops the download buttons being visible.

## Options

| Option | Type | Description |
|  --- | --- | --- |
| hideDownloadButtons | boolean | Show or hide the **Download OpenAPI description** section of your API reference info page, which contains download buttons.
Defaults to `false`. |


## Examples

The following example allows the default description-downloading behavior, but overrides it for a legacy version of an API:


```yaml redocly.yaml

apis:
  museum@v2.3:
    root: 'openapi/museum.yaml'
  museum@v1.8:
    root: 'openapi/museum-1_8.yaml'
    openapi:
      hideDownloadButtons: true
```

## Resources

- **[Download URLs](/docs/realm/config/openapi/download-urls)** - Configure the URLs that download buttons point to for customized file access and distribution
- **[OpenAPI configuration](/docs/realm/config/openapi)** - Complete guide to OpenAPI configuration options for customizing API reference documentation
- **[OpenAPI Specification](https://spec.openapis.org/oas/latest.html)** - Official OpenAPI Specification documentation for understanding API description standards
- **[OpenAPI visual reference](https://redocly.com/learn/openapi/openapi-visual-reference)** - Visual guide to OpenAPI specification structure and download button customization
- **[Configuration options](/docs/realm/config)** - Explore other project configuration options for comprehensive documentation customization