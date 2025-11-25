# Source: https://docs.comfy.org/api-reference/registry/list-all-versions-of-a-node.md

# List all versions of a node

## OpenAPI

````yaml https://api.comfy.org/openapi get /nodes/{nodeId}/versions
paths:
  path: /nodes/{nodeId}/versions
  method: get
  servers:
    - url: https://api.comfy.org
  request:
    security: []
    parameters:
      path:
        nodeId:
          schema:
            - type: string
              required: true
      query:
        statuses:
          schema:
            - type: array
              items:
                allOf:
                  - $ref: '#/components/schemas/NodeVersionStatus'
        include_status_reason:
          schema:
            - type: boolean
              default: false
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
                - $ref: '#/components/schemas/NodeVersion'
        examples:
          example:
            value:
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
    '403':
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
        description: Node banned
    '404':
      application/json:
        schemaArray:
          - type: object
            properties:
              details:
                allOf:
                  - description: >-
                      Optional detailed information about the error or hints for
                      resolving it.
                    items:
                      type: string
                    type: array
              message:
                allOf:
                  - description: A clear and concise description of the error.
                    type: string
            refIdentifier: '#/components/schemas/Error'
        examples:
          example:
            value:
              details:
                - <string>
              message: <string>
        description: Node not found
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