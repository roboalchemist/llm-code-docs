# Source: https://docs.comfy.org/api-reference/registry/list-all-comfy-nodes.md

# list all comfy-nodes

## OpenAPI

````yaml https://api.comfy.org/openapi get /comfy-nodes
paths:
  path: /comfy-nodes
  method: get
  servers:
    - url: https://api.comfy.org
  request:
    security: []
    parameters:
      path: {}
      query:
        pageSize:
          schema:
            - type: integer
              default: 100
        page:
          schema:
            - type: integer
              description: Page number (1-based indexing)
              default: 1
        node_id:
          schema:
            - type: string
              description: Filter by node ID
        node_version:
          schema:
            - type: string
              description: Filter by node version
        comfy_node_name:
          schema:
            - type: string
              description: Filter by ComfyUI node name
      header: {}
      cookie: {}
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              comfy_nodes:
                allOf:
                  - items:
                      $ref: '#/components/schemas/ComfyNode'
                    type: array
              total:
                allOf:
                  - description: Total number of comfy nodes
                    type: integer
        examples:
          example:
            value:
              comfy_nodes:
                - category: <string>
                  comfy_node_name: <string>
                  deprecated: true
                  description: <string>
                  experimental: true
                  function: <string>
                  input_types: <string>
                  output_is_list:
                    - true
                  policy: ComfyNodePolicyActive
                  return_names: <string>
                  return_types: <string>
              total: 123
        description: OK
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
        description: Bad request, invalid input data.
    '401':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: Unauthorized
        examples: {}
        description: Unauthorized
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
        description: Forbidden
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
    ComfyNode:
      properties:
        category:
          description: UI category where the node is listed, used for grouping nodes.
          type: string
        comfy_node_name:
          description: Unique identifier for the node
          type: string
        deprecated:
          description: >-
            Indicates if the node is deprecated. Deprecated nodes are hidden in
            the UI.
          type: boolean
        description:
          description: Brief description of the node's functionality or purpose.
          type: string
        experimental:
          description: >-
            Indicates if the node is experimental, subject to changes or
            removal.
          type: boolean
        function:
          description: Name of the entry-point function to execute the node.
          type: string
        input_types:
          description: Defines input parameters
          type: string
        output_is_list:
          description: Boolean values indicating if each output is a list.
          items:
            type: boolean
          type: array
        policy:
          $ref: '#/components/schemas/ComfyNodePolicy'
        return_names:
          description: Names of the outputs for clarity in workflows.
          type: string
        return_types:
          description: Specifies the types of outputs produced by the node.
          type: string
      type: object
    ComfyNodePolicy:
      enum:
        - ComfyNodePolicyActive
        - ComfyNodePolicyBanned
        - ComfyNodePolicyLocalOnly
      type: string

````