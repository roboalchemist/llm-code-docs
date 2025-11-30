# Source: https://docs.exa.ai/websets/api/websets/enrichments/create-an-enrichment.md

# Create an Enrichment

> Create an Enrichment for a Webset.

## OpenAPI

````yaml post /v0/websets/{webset}/enrichments
paths:
  path: /v0/websets/{webset}/enrichments
  method: post
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
              description: The id or externalId of the Webset
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
                    type:
                      - object
                    additionalProperties:
                      type:
                        - string
                      maxLength: 1000
            required: true
            refIdentifier: '#/components/schemas/CreateEnrichmentParameters'
            requiredProperties:
              - description
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
        source: |-
          // npm install exa-js
          import Exa from 'exa-js';
          const exa = new Exa('YOUR_EXA_API_KEY');

          const enrichment = await exa.websets.enrichments.create('webset_id', {
            description: 'Company revenue information',
            format: 'text'
          });

          console.log(`Created enrichment: ${enrichment.id}`);
      - label: Python
        lang: python
        source: |-
          # pip install exa-py
          from exa_py import Exa
          exa = Exa('YOUR_EXA_API_KEY')

          enrichment = exa.websets.enrichments.create('webset_id', params={
              'description': 'Company revenue information',
              'format': 'text'
          })

          print(f'Created enrichment: {enrichment.id}')
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              id:
                allOf:
                  - type:
                      - string
                    description: The unique identifier for the enrichment
              object:
                allOf:
                  - type: string
                    const: webset_enrichment
                    default: webset_enrichment
              status:
                allOf:
                  - type:
                      - string
                    enum:
                      - pending
                      - canceled
                      - completed
                    description: The status of the enrichment
                    title: WebsetEnrichmentStatus
              websetId:
                allOf:
                  - type:
                      - string
                    description: >-
                      The unique identifier for the Webset this enrichment
                      belongs to.
              title:
                allOf:
                  - type: string
                    description: >-
                      The title of the enrichment.


                      This will be automatically generated based on the
                      description and format.
                    nullable: true
              description:
                allOf:
                  - type:
                      - string
                    description: >-
                      The description of the enrichment task provided during the
                      creation of the enrichment.
              format:
                allOf:
                  - type: string
                    $ref: '#/components/schemas/WebsetEnrichmentFormat'
                    description: The format of the enrichment response.
                    nullable: true
              options:
                allOf:
                  - type: array
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
                    description: >-
                      When the format is options, the different options for the
                      enrichment agent to choose from.
                    title: WebsetEnrichmentOptions
                    nullable: true
              instructions:
                allOf:
                  - type: string
                    description: >-
                      The instructions for the enrichment Agent.


                      This will be automatically generated based on the
                      description and format.
                    nullable: true
              metadata:
                allOf:
                  - default: {}
                    description: The metadata of the enrichment
                    type:
                      - object
                    additionalProperties:
                      type:
                        - string
                      maxLength: 1000
              createdAt:
                allOf:
                  - type:
                      - string
                    format: date-time
                    description: The date and time the enrichment was created
              updatedAt:
                allOf:
                  - type:
                      - string
                    format: date-time
                    description: The date and time the enrichment was updated
            refIdentifier: '#/components/schemas/WebsetEnrichment'
            requiredProperties:
              - id
              - object
              - status
              - websetId
              - title
              - description
              - format
              - options
              - instructions
              - createdAt
              - updatedAt
        examples:
          example:
            value:
              id: <string>
              object: webset_enrichment
              status: pending
              websetId: <string>
              title: <string>
              description: <string>
              format: text
              options:
                - label: <string>
              instructions: <string>
              metadata: {}
              createdAt: '2023-11-07T05:31:56Z'
              updatedAt: '2023-11-07T05:31:56Z'
        description: Enrichment created
  deprecated: false
  type: path
components:
  schemas:
    WebsetEnrichmentFormat:
      type: string
      enum:
        - text
        - date
        - number
        - options
        - email
        - phone
        - url

````

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.exa.ai/llms.txt