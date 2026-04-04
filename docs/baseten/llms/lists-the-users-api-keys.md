# Source: https://docs.baseten.co/reference/management-api/api-keys/lists-the-users-api-keys.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.baseten.co/llms.txt
> Use this file to discover all available pages before exploring further.

# Get all API keys

> Lists all API keys your account has access to.

<ResponseExample>
  ```json 200 theme={"system"}
  {
    "name": "my-api-key", 
    "type": "PERSONAL"
  }
  ```
</ResponseExample>


## OpenAPI

````yaml get /v1/api_keys
openapi: 3.1.0
info:
  description: REST API for management of Baseten resources
  title: Baseten management API
  version: 1.0.0
servers:
  - url: https://api.baseten.co
security:
  - ApiKeyAuth: []
paths:
  /v1/api_keys:
    get:
      summary: Lists the user's API keys
      responses:
        '200':
          description: A list of API keys.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/APIKeysV1'
components:
  schemas:
    APIKeysV1:
      description: A list of API keys.
      properties:
        keys:
          description: A list of API key information
          items:
            $ref: '#/components/schemas/APIKeyInfoV1'
          title: Keys
          type: array
      required:
        - keys
      title: APIKeysV1
      type: object
    APIKeyInfoV1:
      description: Represents the metadata of an API key.
      properties:
        prefix:
          description: The prefix of the API key
          title: Prefix
          type: string
        name:
          anyOf:
            - type: string
            - type: 'null'
          default: null
          description: Optional name for the API key
          examples:
            - my-api-key
          title: Name
        type:
          $ref: '#/components/schemas/APIKeyCategory'
          description: Type of the API key.
          examples:
            - PERSONAL
            - WORKSPACE_EXPORT_METRICS
            - WORKSPACE_INVOKE
            - WORKSPACE_MANAGE_ALL
        model_ids:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          default: null
          description: >-
            List of model IDs to scope the API key to, only present if type is
            'WORKSPACE_EXPORT_METRICS' or 'WORKSPACE_INVOKE'
          examples:
            - - aaaaaaaa
          title: Model Ids
        team_name:
          anyOf:
            - type: string
            - type: 'null'
          default: null
          description: The name of the team associated with the API key
          title: Team Name
      required:
        - prefix
        - type
      title: APIKeyInfoV1
      type: object
    APIKeyCategory:
      description: Enum representing the category of an API key.
      enum:
        - PERSONAL
        - WORKSPACE_MANAGE_ALL
        - WORKSPACE_EXPORT_METRICS
        - WORKSPACE_INVOKE
      title: APIKeyCategory
      type: string
  securitySchemes:
    ApiKeyAuth:
      type: apiKey
      in: header
      name: Authorization
      description: >-
        You must specify the scheme 'Api-Key' in the Authorization header. For
        example, `Authorization: Api-Key <Your_Api_Key>`

````