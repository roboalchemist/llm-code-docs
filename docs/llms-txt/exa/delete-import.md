# Source: https://docs.exa.ai/websets/api/imports/delete-import.md

# Delete Import

> Deletes a import.

## OpenAPI

````yaml delete /v0/imports/{id}
paths:
  path: /v0/imports/{id}
  method: delete
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
        id:
          schema:
            - type: string
              required: true
              description: The id of the Import
      query: {}
      header: {}
      cookie: {}
    body: {}
    codeSamples:
      - label: JavaScript
        lang: javascript
        source: |-
          // npm install exa-js
          import Exa from 'exa-js';
          const exa = new Exa('YOUR_EXA_API_KEY');

          await exa.websets.imports.delete('webset_id', 'import_id');

          console.log('Import deleted successfully');
      - label: Python
        lang: python
        source: |-
          # pip install exa-py
          from exa_py import Exa
          exa = Exa('YOUR_EXA_API_KEY')

          exa.websets.imports.delete('webset_id', 'import_id')

          print('Import deleted successfully')
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
                    description: The unique identifier for the Import
              object:
                allOf:
                  - type:
                      - string
                    enum:
                      - import
                    description: The type of object
              status:
                allOf:
                  - type:
                      - string
                    enum:
                      - pending
                      - processing
                      - completed
                      - failed
                    description: The status of the Import
              format:
                allOf:
                  - type:
                      - string
                    enum:
                      - csv
                      - webset
                    description: The format of the import.
              entity:
                allOf:
                  - $ref: '#/components/schemas/Entity'
                    description: The type of entity the import contains.
                    nullable: true
              title:
                allOf:
                  - type:
                      - string
                    description: The title of the import
              count:
                allOf:
                  - type:
                      - number
                    description: The number of entities in the import
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
              failedReason:
                allOf:
                  - type: string
                    enum:
                      - invalid_format
                      - invalid_file_content
                      - missing_identifier
                    description: The reason the import failed
                    nullable: true
              failedAt:
                allOf:
                  - type: string
                    format: date-time
                    description: When the import failed
                    nullable: true
              failedMessage:
                allOf:
                  - type: string
                    description: A human readable message of the import failure
                    nullable: true
              createdAt:
                allOf:
                  - type:
                      - string
                    format: date-time
                    description: When the import was created
              updatedAt:
                allOf:
                  - type:
                      - string
                    format: date-time
                    description: When the import was last updated
            refIdentifier: '#/components/schemas/Import'
            requiredProperties:
              - id
              - object
              - status
              - format
              - entity
              - title
              - count
              - metadata
              - failedReason
              - failedAt
              - failedMessage
              - createdAt
              - updatedAt
        examples:
          example:
            value:
              id: <string>
              object: import
              status: pending
              format: csv
              entity:
                type: company
              title: <string>
              count: 123
              metadata: {}
              failedReason: invalid_format
              failedAt: '2023-11-07T05:31:56Z'
              failedMessage: <string>
              createdAt: '2023-11-07T05:31:56Z'
              updatedAt: '2023-11-07T05:31:56Z'
        description: Import deleted successfully
  deprecated: false
  type: path
components:
  schemas:
    CompanyEntity:
      type:
        - object
      properties:
        type:
          type: string
          const: company
          default: company
      required:
        - type
      title: Company
    PersonEntity:
      type:
        - object
      properties:
        type:
          type: string
          const: person
          default: person
      required:
        - type
      title: Person
    ArticleEntity:
      type:
        - object
      properties:
        type:
          type: string
          const: article
          default: article
      required:
        - type
      title: Article
    ResearchPaperEntity:
      type:
        - object
      properties:
        type:
          type: string
          const: research_paper
          default: research_paper
      required:
        - type
      title: Research Paper
    CustomEntity:
      type:
        - object
      properties:
        type:
          type: string
          const: custom
          default: custom
        description:
          type:
            - string
          minLength: 2
          maxLength: 200
      required:
        - type
        - description
      title: Custom
    Entity:
      oneOf:
        - type:
            - object
          $ref: '#/components/schemas/CompanyEntity'
        - type:
            - object
          $ref: '#/components/schemas/PersonEntity'
        - type:
            - object
          $ref: '#/components/schemas/ArticleEntity'
        - type:
            - object
          $ref: '#/components/schemas/ResearchPaperEntity'
        - type:
            - object
          $ref: '#/components/schemas/CustomEntity'

````

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.exa.ai/llms.txt