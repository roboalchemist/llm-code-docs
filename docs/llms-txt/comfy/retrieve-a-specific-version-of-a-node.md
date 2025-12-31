# Source: https://docs.comfy.org/api-reference/registry/retrieve-a-specific-version-of-a-node.md

# Retrieve a specific version of a node

## OpenAPI

````yaml https://api.comfy.org/openapi get /nodes/{nodeId}/versions/{versionId}
paths:
  path: /nodes/{nodeId}/versions/{versionId}
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
        versionId:
          schema:
            - type: string
              required: true
              description: The version of the node. (Not a UUID).
      query: {}
      header: {}
      cookie: {}
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              changelog:
                allOf:
                  - description: Summary of changes made in this version
                    type: string
              comfy_node_extract_status:
                allOf:
                  - description: The status of comfy node extraction process.
                    type: string
              createdAt:
                allOf:
                  - description: The date and time the version was created.
                    format: date-time
                    type: string
              dependencies:
                allOf:
                  - description: A list of pip dependencies required by the node.
                    items:
                      type: string
                    type: array
              deprecated:
                allOf:
                  - description: Indicates if this version is deprecated.
                    type: boolean
              downloadUrl:
                allOf:
                  - description: '[Output Only] URL to download this version of the node'
                    type: string
              id:
                allOf:
                  - type: string
              node_id:
                allOf:
                  - description: The unique identifier of the node.
                    type: string
              status:
                allOf:
                  - $ref: '#/components/schemas/NodeVersionStatus'
              status_reason:
                allOf:
                  - type: string
              supported_accelerators:
                allOf:
                  - description: >-
                      List of accelerators (e.g. CUDA, DirectML, ROCm) that this
                      node supports
                    items:
                      type: string
                    type: array
              supported_comfyui_frontend_version:
                allOf:
                  - description: Supported versions of ComfyUI frontend
                    type: string
              supported_comfyui_version:
                allOf:
                  - description: Supported versions of ComfyUI
                    type: string
              supported_os:
                allOf:
                  - description: List of operating systems that this node supports
                    items:
                      type: string
                    type: array
              tags:
                allOf:
                  - items:
                      type: string
                    type: array
              tags_admin:
                allOf:
                  - description: Admin-only tags for security warnings and admin metadata
                    items:
                      type: string
                    type: array
              version:
                allOf:
                  - description: >-
                      The version identifier, following semantic versioning.
                      Must be unique for the node.
                    type: string
            refIdentifier: '#/components/schemas/NodeVersion'
        examples:
          example:
            value:
              changelog: <string>
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
        description: Detailed information about a specific node version
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
        description: Node version not found
    '500':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - type: string
              message:
                allOf:
                  - type: string
            refIdentifier: '#/components/schemas/ErrorResponse'
            requiredProperties:
              - error
              - message
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
    NodeVersionStatus:
      enum:
        - NodeVersionStatusActive
        - NodeVersionStatusDeleted
        - NodeVersionStatusBanned
        - NodeVersionStatusPending
        - NodeVersionStatusFlagged
      type: string

````