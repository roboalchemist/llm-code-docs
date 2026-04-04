# Source: https://docs.xano.com/api-reference/table-index/create-a-full-text-search-index-on-table-columns.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Create a full-text search index on table columns

> Create a full-text search index for table columns with language-specific optimization
<br /><br />
<b>Authentication:</b> required
<br /><br />
<b>Required API Scope:</b>
Workspace Database: Create



## OpenAPI

````yaml apispec_meta_instance.json post /workspace/{workspace_id}/table/{table_id}/index/search
openapi: 3.0.0
info:
  title: Xano Metadata API
  description: >-
    The <a href="https://docs.xano.com/xano-features/metadata-api"
    target="_blank">Metadata API</a> provides support

    to programatically manage your Xano instance and uses Access Tokens to

    control access.
  version: 0.0.1
servers:
  - url: https://your-xano-instance.xano.io/api:meta
security: []
paths:
  /workspace/{workspace_id}/table/{table_id}/index/search:
    post:
      tags:
        - table / index
      summary: Create a full-text search index on table columns
      description: >-
        Create a full-text search index for table columns with language-specific
        optimization

        <br /><br />

        <b>Authentication:</b> required

        <br /><br />

        <b>Required API Scope:</b>

        Workspace Database: Create
      operationId: >-
        Xano Metadata
        API/workspace/{workspace_id}/table/{table_id}/index/search|POST
      parameters:
        - name: workspace_id
          in: path
          description: ''
          required: true
          schema:
            type: integer
            format: int64
        - name: table_id
          in: path
          description: ''
          required: true
          schema:
            type: integer
            format: int64
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                name:
                  type: string
                  description: ''
                lang:
                  type: string
                  description: ''
                  enum:
                    - simple
                    - arabic
                    - danish
                    - dutch
                    - english
                    - finnish
                    - french
                    - german
                    - hungarian
                    - indonesian
                    - irish
                    - italian
                    - lithuanian
                    - nepali
                    - norwegian
                    - portuguese
                    - romanian
                    - russian
                    - spanish
                    - swedish
                    - tamil
                    - turkish
                fields:
                  type: array
                  items:
                    type: object
                    properties:
                      name:
                        type: string
                        description: ''
                      priority:
                        type: integer
                        format: int64
                        description: ''
                    required:
                      - name
                      - priority
              required:
                - name
                - lang
                - fields
              example:
                name: search_label
                lang: english
                fields:
                  - name: name
                    priority: 1
          multipart/form-data:
            schema:
              type: object
              properties:
                name:
                  type: string
                  description: ''
                lang:
                  type: string
                  description: ''
                  enum:
                    - simple
                    - arabic
                    - danish
                    - dutch
                    - english
                    - finnish
                    - french
                    - german
                    - hungarian
                    - indonesian
                    - irish
                    - italian
                    - lithuanian
                    - nepali
                    - norwegian
                    - portuguese
                    - romanian
                    - russian
                    - spanish
                    - swedish
                    - tamil
                    - turkish
                fields:
                  type: array
                  items:
                    type: object
                    properties:
                      name:
                        type: string
                        description: ''
                      priority:
                        type: integer
                        format: int64
                        description: ''
                    required:
                      - name
                      - priority
              required:
                - name
                - lang
                - fields
              example:
                name: search_label
                lang: english
                fields:
                  - name: name
                    priority: 1
      responses:
        '200':
          description: Success!
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    type: string
        '400':
          description: Input Error. Check the request payload for issues.
        '401':
          description: Unauthorized
        '403':
          description: >-
            Access denied. Additional privileges are needed access the requested
            resource.
        '404':
          description: Not Found. The requested resource does not exist.
        '429':
          description: Rate Limited. Too many requests.
        '500':
          description: Unexpected error
      security:
        - bearerAuth: []
components:
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT

````

Built with [Mintlify](https://mintlify.com).