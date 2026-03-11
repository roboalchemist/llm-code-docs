# Source: https://redocly.com/docs/realm/content/api-docs/openapi-extensions/x-code-samples.md

# OpenAPI extension: `x-codeSamples`

Code samples are snippets of code shown alongside API operations in reference documentation, giving users a quick way to start to interact with an API from their own code.
The `x-codeSamples` addition to OpenAPI allows you to add or override any existing code samples for a particular language or endpoint.

Use the `x-codeSamples` option to make code samples part of the API description, or to replace the generated examples with code that is specific to your use case, such as using a custom library or SDK.

Language options
Control the list of language options by adjusting the [openapi.code-samples](/docs/realm/config/openapi/code-samples) configuration setting.

Environment variables
Use environment variable placeholders like `{{VARIABLE_NAME}}` in code samples.
Configure their values in the `envVariables` field of your request values configuration.
[Learn more about environment variables](/docs/realm/customization/configure-request-values#configure-environment-variables-for-code-samples).

## Location

`x-codeSamples` can be added to Operation objects.

## Options

| Field Name | Type | Description |
|  --- | --- | --- |
| x-codeSamples | [ [Code Sample Object](#code-sample-object) ] | A list of code samples associated with an operation. |


### Code Sample Object

| Field Name | Type | Description |
|  --- | --- | --- |
| lang | string | **REQUIRED** Code sample language.
Can be one of the [automatically supported languages](/docs/realm/config/openapi/code-samples#language-object) or any other language identifier of your choice (for custom code samples). |
| source | string | **REQUIRED** Code sample source code, or a `$ref` to the file containing the code sample. |


## Examples

The following partial OpenAPI snippet shows adding code samples to replace the generated samples for the `getMuseumHours` operation.
One adds the source to the OpenAPI file, the other references a file containing the code sample.


```yaml

...
paths:
  /museum-hours:
    get:
      summary: Get museum hours
      description: Get upcoming museum operating hours.
      operationId: getMuseumHours
      x-codeSamples:
        - lang: PHP
          source: |
            <?php
              $url = "https://example.com/museum";
              $response = file_get_contents($url);
              $data = json_decode($response);
        - lang: Python
          source:
            $ref: "code_samples/python.py"
      tags:
        - Operations
```

## Resources

- **[OpenAPI code samples configuration](/docs/realm/config/openapi/code-samples)** - Control the list of available language options and customize code sample generation settings
- **[Show extensions configuration](/docs/realm/config/openapi/show-extensions)** - Control which extensions are included in your API reference documentation for optimal presentation
- **[OpenAPI configuration settings](/docs/realm/config/openapi)** - Complete reference for all available OpenAPI configuration options and customization settings
- **[Supported OpenAPI extensions](/docs/realm/content/api-docs/openapi-extensions)** - Complete list of all OpenAPI extensions supported by Redocly for enhanced API documentation
- **[Configure environment variables](/docs/realm/customization/configure-request-values)** - Set up environment variable placeholders for dynamic code samples and request customization