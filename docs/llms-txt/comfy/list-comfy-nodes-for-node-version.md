# Source: https://docs.comfy.org/api-reference/registry/list-comfy-nodes-for-node-version.md

# list comfy-nodes for node version

## OpenAPI

````yaml https://api.comfy.org/openapi get /nodes/{nodeId}/versions/{version}/comfy-nodes
paths:
  path: /nodes/{nodeId}/versions/{version}/comfy-nodes
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
        version:
          schema:
            - type: string
              required: true
      query:
        page:
          schema:
            - type: integer
              description: The page number to retrieve.
              default: 1
        limit:
          schema:
            - type: integer
              description: The number of items to include per page.
              default: 10
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
              totalNumberOfPages:
                allOf:
                  - type: integer
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
              totalNumberOfPages: 123
        description: Comy Nodes obtained successfully
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
        description: Version not found
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