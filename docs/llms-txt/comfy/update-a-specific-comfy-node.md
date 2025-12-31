# Source: https://docs.comfy.org/api-reference/registry/update-a-specific-comfy-node.md

# Update a specific comfy-node

## OpenAPI

````yaml https://api.comfy.org/openapi put /nodes/{nodeId}/versions/{version}/comfy-nodes/{comfyNodeName}
paths:
  path: /nodes/{nodeId}/versions/{version}/comfy-nodes/{comfyNodeName}
  method: put
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
        version:
          schema:
            - type: string
              required: true
        comfyNodeName:
          schema:
            - type: string
              required: true
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              category:
                allOf:
                  - description: >-
                      UI category where the node is listed, used for grouping
                      nodes.
                    type: string
              deprecated:
                allOf:
                  - description: >-
                      Indicates if the node is deprecated. Deprecated nodes are
                      hidden in the UI.
                    type: boolean
              description:
                allOf:
                  - description: Brief description of the node's functionality or purpose.
                    type: string
              experimental:
                allOf:
                  - description: >-
                      Indicates if the node is experimental, subject to changes
                      or removal.
                    type: boolean
              function:
                allOf:
                  - description: Name of the entry-point function to execute the node.
                    type: string
              input_types:
                allOf:
                  - description: Defines input parameters
                    type: string
              output_is_list:
                allOf:
                  - description: Boolean values indicating if each output is a list.
                    items:
                      type: boolean
                    type: array
              policy:
                allOf:
                  - $ref: '#/components/schemas/ComfyNodePolicy'
              return_names:
                allOf:
                  - description: Names of the outputs for clarity in workflows.
                    type: string
              return_types:
                allOf:
                  - description: Specifies the types of outputs produced by the node.
                    type: string
            required: true
            refIdentifier: '#/components/schemas/ComfyNodeUpdateRequest'
        examples:
          example:
            value:
              category: <string>
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
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              category:
                allOf:
                  - description: >-
                      UI category where the node is listed, used for grouping
                      nodes.
                    type: string
              comfy_node_name:
                allOf:
                  - description: Unique identifier for the node
                    type: string
              deprecated:
                allOf:
                  - description: >-
                      Indicates if the node is deprecated. Deprecated nodes are
                      hidden in the UI.
                    type: boolean
              description:
                allOf:
                  - description: Brief description of the node's functionality or purpose.
                    type: string
              experimental:
                allOf:
                  - description: >-
                      Indicates if the node is experimental, subject to changes
                      or removal.
                    type: boolean
              function:
                allOf:
                  - description: Name of the entry-point function to execute the node.
                    type: string
              input_types:
                allOf:
                  - description: Defines input parameters
                    type: string
              output_is_list:
                allOf:
                  - description: Boolean values indicating if each output is a list.
                    items:
                      type: boolean
                    type: array
              policy:
                allOf:
                  - $ref: '#/components/schemas/ComfyNodePolicy'
              return_names:
                allOf:
                  - description: Names of the outputs for clarity in workflows.
                    type: string
              return_types:
                allOf:
                  - description: Specifies the types of outputs produced by the node.
                    type: string
            refIdentifier: '#/components/schemas/ComfyNode'
        examples:
          example:
            value:
              category: <string>
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
        description: Comfy Node updated successfully
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
        description: Bad request, invalid input data
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
    '404':
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
        description: ComfyNode not found
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
    ComfyNodePolicy:
      enum:
        - ComfyNodePolicyActive
        - ComfyNodePolicyBanned
        - ComfyNodePolicyLocalOnly
      type: string

````