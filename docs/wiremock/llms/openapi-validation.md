# Source: https://docs.wiremock.io/openAPI/openapi-validation.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wiremock.io/llms.txt
> Use this file to discover all available pages before exploring further.

# OpenAPI Validation

> Validating mock API requests and responses against OpenAPI

Validation settings can be used to ensure that requests made to your mock API and responses returned by your mock API
are compliant with your OpenAPI specification.
Settings for OpenAPI validation can be found in the Settings tab on the OpenAPI page.
There are three options for OpenAPI validation: no validation (the default), soft validation, and hard validation.

<img src="https://mintcdn.com/wiremockinc/9niDaTpLrBsVTNkq/images/openapi/validation-settings.png?fit=max&auto=format&n=9niDaTpLrBsVTNkq&q=85&s=d2cd1097d81540381919ea1497dc4ce6" width="50%" data-og-width="589" data-og-height="597" data-path="images/openapi/validation-settings.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/9niDaTpLrBsVTNkq/images/openapi/validation-settings.png?w=280&fit=max&auto=format&n=9niDaTpLrBsVTNkq&q=85&s=6d3bf65e92103c008f37f5d609f8d8c1 280w, https://mintcdn.com/wiremockinc/9niDaTpLrBsVTNkq/images/openapi/validation-settings.png?w=560&fit=max&auto=format&n=9niDaTpLrBsVTNkq&q=85&s=f82f0f378ddba2a026eb5b41f31c1a06 560w, https://mintcdn.com/wiremockinc/9niDaTpLrBsVTNkq/images/openapi/validation-settings.png?w=840&fit=max&auto=format&n=9niDaTpLrBsVTNkq&q=85&s=9a30848455950216e0f32e79f3346e9c 840w, https://mintcdn.com/wiremockinc/9niDaTpLrBsVTNkq/images/openapi/validation-settings.png?w=1100&fit=max&auto=format&n=9niDaTpLrBsVTNkq&q=85&s=e7b780eeb3fb0dac570a4ab645f89054 1100w, https://mintcdn.com/wiremockinc/9niDaTpLrBsVTNkq/images/openapi/validation-settings.png?w=1650&fit=max&auto=format&n=9niDaTpLrBsVTNkq&q=85&s=6d85d922c5396705d338a1e40b35758d 1650w, https://mintcdn.com/wiremockinc/9niDaTpLrBsVTNkq/images/openapi/validation-settings.png?w=2500&fit=max&auto=format&n=9niDaTpLrBsVTNkq&q=85&s=9e4d63003eb2daeaa6fe696ed10d2d69 2500w" />

The "no validation" option will have no effect on your mock API.

Enabling soft validation will cause non-compliant requests to contain validation warnings in your mock API's request log.
Any request to the mock API and/or any response returned by the mock API containing data/attributes that do not conform
to the mock API's OpenAPI document will be highlighted on the request log page.
Details of how the request was invalid can also be viewed in the request log.

<img src="https://mintcdn.com/wiremockinc/9niDaTpLrBsVTNkq/images/openapi/validation-logs-soft.gif?s=1817df0cc72cc0b9fd04f35d24edcc2d" alt="OpenAPI validation logs" data-og-width="1262" width="1262" data-og-height="960" height="960" data-path="images/openapi/validation-logs-soft.gif" data-optimize="true" data-opv="3" />

Enabling hard validation will cause the same request log behavior as soft validation, with the added functionality of
returning error responses containing details of validation issues to invalid requests.
