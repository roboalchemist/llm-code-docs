# Source: https://docs.comfy.org/api-reference/registry/list-all-node-versions-given-some-filters.md

# List all node versions given some filters.

## OpenAPI

````yaml https://api.comfy.org/openapi get /versions
paths:
  path: /versions
  method: get
  servers:
    - url: https://api.comfy.org
  request:
    security: []
    parameters:
      path: {}
      query:
        nodeId:
          schema:
            - type: string
        statuses:
          schema:
            - type: array
              items:
                allOf:
                  - $ref: '#/components/schemas/NodeVersionStatus'
          style: form
          explode: true
        include_status_reason:
          schema:
            - type: boolean
              default: false
        page:
          schema:
            - type: integer
              description: The page number to retrieve.
              default: 1
        pageSize:
          schema:
            - type: integer
              description: The number of items to include per page.
              default: 10
        status_reason:
          schema:
            - type: string
              description: search for status_reason, case insensitive
      header: {}
      cookie: {}
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              page:
                allOf:
                  - description: Current page number
                    type: integer
              pageSize:
                allOf:
                  - description: Maximum number of node versions per page. Maximum is 100.
                    type: integer
              total:
                allOf:
                  - description: Total number of node versions available
                    type: integer
              totalPages:
                allOf:
                  - description: Total number of pages available
                    type: integer
              versions:
                allOf:
                  - items:
                      $ref: '#/components/schemas/NodeVersion'
                    type: array
        examples:
          example:
            value:
              page: 123
              pageSize: 123
              total: 123
              totalPages: 123
              versions:
                - changelog: <string>
                  comfy_node_extract_status: <string>
                  createdAt: '2023-11-07T05:31:56Z'
                  dependencies:
                    - <string>
                  deprecated: true
                  downloadUrl: <string>
                  id: <string>
                  node_id: <string>
                  status: NodeVersionStatusActive
                  status_reason: <string>
                  supported_accelerators:
                    - <string>
                  supported_comfyui_frontend_version: <string>
                  supported_comfyui_version: <string>
                  supported_os:
                    - <string>
                  tags:
                    - <string>
                  tags_admin:
                    - <string>
                  version: <string>
        description: List of all node versions
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
        description: Invalid input, object invalid
    '403':
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
        description: Node banned
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
    NodeVersion:
      properties:
        changelog:
          description: Summary of changes made in this version
          type: string
        comfy_node_extract_status:
          description: The status of comfy node extraction process.
          type: string
        createdAt:
          description: The date and time the version was created.
          format: date-time
          type: string
        dependencies:
          description: A list of pip dependencies required by the node.
          items:
            type: string
          type: array
        deprecated:
          description: Indicates if this version is deprecated.
          type: boolean
        downloadUrl:
          description: '[Output Only] URL to download this version of the node'
          type: string
        id:
          type: string
        node_id:
          description: The unique identifier of the node.
          type: string
        status:
          $ref: '#/components/schemas/NodeVersionStatus'
        status_reason:
          type: string
        supported_accelerators:
          description: >-
            List of accelerators (e.g. CUDA, DirectML, ROCm) that this node
            supports
          items:
            type: string
          type: array
        supported_comfyui_frontend_version:
          description: Supported versions of ComfyUI frontend
          type: string
        supported_comfyui_version:
          description: Supported versions of ComfyUI
          type: string
        supported_os:
          description: List of operating systems that this node supports
          items:
            type: string
          type: array
        tags:
          items:
            type: string
          type: array
        tags_admin:
          description: Admin-only tags for security warnings and admin metadata
          items:
            type: string
          type: array
        version:
          description: >-
            The version identifier, following semantic versioning. Must be
            unique for the node.
          type: string
      type: object
    NodeVersionStatus:
      enum:
        - NodeVersionStatusActive
        - NodeVersionStatusDeleted
        - NodeVersionStatusBanned
        - NodeVersionStatusPending
        - NodeVersionStatusFlagged
      type: string

````