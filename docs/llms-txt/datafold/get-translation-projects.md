# Source: https://docs.datafold.com/api-reference/dma/get-translation-projects.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.datafold.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get translation projects

> Get all translation projects for an organization.
This is used for DMA v1 and v2, since it's TranslationProject is a SQLAlchemy model.
Version is used to track if it's a DMA v1 or v2 project.



## OpenAPI

````yaml openapi-public.json get /api/v1/dma/projects
openapi: 3.1.0
info:
  contact:
    email: support@datafold.com
    name: API Support
  description: >-
    The Datafold API reference is a guide to our available endpoints and
    authentication methods.

    If you're just getting started with Datafold, we recommend first checking
    out our [documentation](https://docs.datafold.com).


    :::info
      To use the Datafold API, you should first create a Datafold API Key,
      which should be stored as a local environment variable named DATAFOLD_API_KEY.
      This can be set in your Datafold Cloud's Settings under the Account page.
    :::
  title: Datafold API
  version: latest
servers:
  - description: Default server
    url: https://app.datafold.com
security:
  - ApiKeyAuth: []
paths:
  /api/v1/dma/projects:
    get:
      tags:
        - DMA
      summary: Get translation projects
      description: >-
        Get all translation projects for an organization.

        This is used for DMA v1 and v2, since it's TranslationProject is a
        SQLAlchemy model.

        Version is used to track if it's a DMA v1 or v2 project.
      operationId: list_translation_projects
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiGetTranslationProjectsResponse'
          description: Successful Response
components:
  schemas:
    ApiGetTranslationProjectsResponse:
      properties:
        projects:
          items:
            $ref: '#/components/schemas/ApiTranslationProjectMeta'
          title: Projects
          type: array
      required:
        - projects
      title: ApiGetTranslationProjectsResponse
      type: object
    ApiTranslationProjectMeta:
      description: Translation project metadata. Used for DMA v1 and v2.
      properties:
        from_data_source_id:
          anyOf:
            - type: integer
            - type: 'null'
          title: From Data Source Id
        id:
          title: Id
          type: integer
        name:
          title: Name
          type: string
        org_id:
          title: Org Id
          type: integer
        repo_name:
          anyOf:
            - type: string
            - type: 'null'
          title: Repo Name
        temp_data_source_id:
          anyOf:
            - type: integer
            - type: 'null'
          title: Temp Data Source Id
        to_data_source_id:
          anyOf:
            - type: integer
            - type: 'null'
          title: To Data Source Id
        version:
          title: Version
          type: integer
      required:
        - id
        - org_id
        - version
        - from_data_source_id
        - to_data_source_id
        - name
        - repo_name
        - temp_data_source_id
      title: ApiTranslationProjectMeta
      type: object
  securitySchemes:
    ApiKeyAuth:
      description: Use the 'Authorization' header with the format 'Key <api-key>'
      in: header
      name: Authorization
      type: apiKey

````