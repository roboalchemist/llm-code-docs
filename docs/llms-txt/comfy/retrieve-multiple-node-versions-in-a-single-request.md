# Source: https://docs.comfy.org/api-reference/registry/retrieve-multiple-node-versions-in-a-single-request.md

# Retrieve multiple node versions in a single request

## OpenAPI

````yaml https://api.comfy.org/openapi post /bulk/nodes/versions
paths:
  path: /bulk/nodes/versions
  method: post
  servers:
    - url: https://api.comfy.org
  request:
    security: []
    parameters:
      path: {}
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              node_versions:
                allOf:
                  - description: List of node ID and version pairs to retrieve
                    items:
                      $ref: '#/components/schemas/NodeVersionIdentifier'
                    type: array
            required: true
            refIdentifier: '#/components/schemas/BulkNodeVersionsRequest'
            requiredProperties:
              - node_versions
        examples:
          example:
            value:
              node_versions:
                - node_id: <string>
                  version: <string>
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              node_versions:
                allOf:
                  - description: List of retrieved node versions with their status
                    items:
                      $ref: '#/components/schemas/BulkNodeVersionResult'
                    type: array
            refIdentifier: '#/components/schemas/BulkNodeVersionsResponse'
            requiredProperties:
              - node_versions
        examples:
          example:
            value:
              node_versions:
                - error_message: <string>
                  identifier:
                    node_id: <string>
                    version: <string>
                  node_version:
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
                  status: success
        description: Successfully retrieved node versions
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
        description: Bad request, invalid input
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
    BulkNodeVersionResult:
      properties:
        error_message:
          description: Error message if retrieval failed (only present if status is error)
          type: string
        identifier:
          $ref: '#/components/schemas/NodeVersionIdentifier'
        node_version:
          $ref: '#/components/schemas/NodeVersion'
        status:
          description: Status of the retrieval operation
          enum:
            - success
            - not_found
            - error
          type: string
      required:
        - identifier
        - status
      type: object
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
    NodeVersionIdentifier:
      properties:
        node_id:
          description: The unique identifier of the node
          type: string
        version:
          description: The version of the node
          type: string
      required:
        - node_id
        - version
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