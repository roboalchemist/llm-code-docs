# Source: https://docs.edenai.co/api-reference/universal-ai-info/list-features.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edenai.co/llms.txt
> Use this file to discover all available pages before exploring further.

# List Features

> List all available features and their subfeatures.

Returns a simple dictionary mapping feature names to lists of subfeature names.



## OpenAPI

````yaml openapi/v3-openapi.json get /v3/info
openapi: 3.1.0
info:
  title: Eden AI API V3
  version: 3.0.0
servers:
  - url: https://api.edenai.run
    description: Production server
security: []
paths:
  /v3/info:
    get:
      tags:
        - Universal-ai-info
      summary: List Features
      description: >-
        List all available features and their subfeatures.


        Returns a simple dictionary mapping feature names to lists of subfeature
        names.
      operationId: list_features_v3_info_get
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                additionalProperties:
                  items:
                    type: string
                  type: array
                type: object
                title: Response List Features V3 Info Get

````

Built with [Mintlify](https://mintlify.com).