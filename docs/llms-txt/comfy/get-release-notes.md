# Source: https://docs.comfy.org/api-reference/releases/get-release-notes.md

# Get release notes

> Fetch release notes from Strapi with caching

## OpenAPI

````yaml https://api.comfy.org/openapi get /releases
paths:
  path: /releases
  method: get
  servers:
    - url: https://api.comfy.org
  request:
    security: []
    parameters:
      path: {}
      query:
        project:
          schema:
            - type: enum<string>
              enum:
                - comfyui
                - comfyui_frontend
                - desktop
              required: true
              description: The project to get release notes for
        current_version:
          schema:
            - type: string
              description: The current version to filter release notes
        locale:
          schema:
            - type: enum<string>
              enum:
                - en
                - es
                - fr
                - ja
                - ko
                - ru
                - zh
              description: The locale for the release notes
              default: en
        form_factor:
          schema:
            - type: string
              description: The platform requesting the release notes
      header: {}
      cookie: {}
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: array
            items:
              allOf:
                - $ref: '#/components/schemas/ReleaseNote'
        examples:
          example:
            value:
              - attention: low
                content: <string>
                id: 123
                project: comfyui
                published_at: '2023-11-07T05:31:56Z'
                version: <string>
        description: Release notes retrieved successfully
    '400':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - &ref_0
                    type: string
              message:
                allOf:
                  - &ref_1
                    type: string
            refIdentifier: '#/components/schemas/ErrorResponse'
            requiredProperties: &ref_2
              - error
              - message
        examples:
          example:
            value:
              error: <string>
              message: <string>
        description: Bad request
    '500':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - *ref_0
              message:
                allOf:
                  - *ref_1
            refIdentifier: '#/components/schemas/ErrorResponse'
            requiredProperties: *ref_2
        examples:
          example:
            value:
              error: <string>
              message: <string>
        description: Internal server error
  deprecated: false
  type: path
components:
  schemas:
    ReleaseNote:
      properties:
        attention:
          description: The attention level for this release
          enum:
            - low
            - medium
            - high
          type: string
        content:
          description: The content of the release note in markdown format
          type: string
        id:
          description: Unique identifier for the release note
          type: integer
        project:
          description: The project this release note belongs to
          enum:
            - comfyui
            - comfyui_frontend
            - desktop
          type: string
        published_at:
          description: When the release note was published
          format: date-time
          type: string
        version:
          description: The version of the release
          type: string
      required:
        - id
        - project
        - version
        - attention
        - content
        - published_at
      type: object

````