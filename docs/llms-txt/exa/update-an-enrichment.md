# Source: https://docs.exa.ai/websets/api/websets/enrichments/update-an-enrichment.md

# Update an Enrichment

> Update an Enrichment configuration for a Webset.

## OpenAPI

````yaml patch /v0/websets/{webset}/enrichments/{id}
paths:
  path: /v0/websets/{webset}/enrichments/{id}
  method: patch
  servers:
    - url: https://api.exa.ai/websets/
      description: Production
  request:
    security:
      - title: api key
        parameters:
          query: {}
          header:
            x-api-key:
              type: apiKey
              description: Your Exa API key
          cookie: {}
    parameters:
      path:
        webset:
          schema:
            - type: string
              required: true
        id:
          schema:
            - type: string
              required: true
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              description:
                allOf:
                  - type:
                      - string
                    minLength: 1
                    maxLength: 5000
                    description: >-
                      Provide a description of the enrichment task you want to
                      perform to each Webset Item.
              format:
                allOf:
                  - type:
                      - string
                    enum:
                      - text
                      - date
                      - number
                      - options
                      - email
                      - phone
                      - url
                    description: >-
                      Format of the enrichment response.


                      We automatically select the best format based on the
                      description. If you want to explicitly specify the format,
                      you can do so here.
              options:
                allOf:
                  - type:
                      - array
                    items:
                      type:
                        - object
                      properties:
                        label:
                          type:
                            - string
                          description: The label of the option
                      required:
                        - label
                    minItems: 1
                    maxItems: 150
                    description: >-
                      When the format is options, the different options for the
                      enrichment agent to choose from.
              metadata:
                allOf:
                  - description: >-
                      Set of key-value pairs you want to associate with this
                      object.
                    type: object
                    additionalProperties:
                      type:
                        - string
                      maxLength: 1000
                    nullable: true
            required: true
            refIdentifier: '#/components/schemas/UpdateEnrichmentParameters'
        examples:
          example:
            value:
              description: <string>
              format: text
              options:
                - label: <string>
              metadata: {}
    codeSamples:
      - label: JavaScript
        lang: javascript
        source: >-
          // npm install exa-js

          import Exa from 'exa-js';

          const exa = new Exa('YOUR_EXA_API_KEY');


          const enrichment = await exa.websets.enrichments.update('webset_id',
          'enrichment_id', {
            description: 'Updated company revenue and growth metrics',
            format: 'number'
          });


          console.log(`Updated enrichment: ${enrichment.id}`);
      - label: Python
        lang: python
        source: >-
          # pip install exa-py

          from exa_py import Exa

          exa = Exa('YOUR_EXA_API_KEY')


          enrichment = exa.websets.enrichments.update('webset_id',
          'enrichment_id', params={
              'description': 'Updated company revenue and growth metrics',
              'format': 'number'
          })


          print(f'Updated enrichment: {enrichment.id}')
  response:
    '200': {}
  deprecated: false
  type: path
components:
  schemas: {}

````

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.exa.ai/llms.txt