# Source: https://docs.fireworks.ai/api-reference-dlde/list-node-pool-bindings.md

# List Node Pool Bindings

## OpenAPI

````yaml get /v1/accounts/{account_id}/nodePoolBindings
paths:
  path: /v1/accounts/{account_id}/nodePoolBindings
  method: get
  servers:
    - url: https://api.fireworks.ai
  request:
    security:
      - title: BearerAuth
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
              description: >-
                Bearer authentication using your Fireworks API key. Format:
                Bearer <API_KEY>
          cookie: {}
    parameters:
      path:
        account_id:
          schema:
            - type: string
              required: true
              description: The Account Id
      query:
        pageSize:
          schema:
            - type: integer
              required: false
              description: >-
                The maximum number of bindings to return. The maximum page_size
                is 200,

                values above 200 will be coerced to 200.

                If unspecified, the default is 50.
        pageToken:
          schema:
            - type: string
              required: false
              description: >-
                A page token, received from a previous ListNodePoolBindings
                call.

                Provide this to retrieve the subsequent page. When paginating,
                all other

                parameters provided to ListNodePoolBindings must match the call
                that

                provided the page token.
        filter:
          schema:
            - type: string
              required: false
              description: >-
                Only bindings satisfying the provided filter (if specified) will
                be

                returned. See https://google.aip.dev/160 for the filter grammar.
        orderBy:
          schema:
            - type: string
              required: false
              description: >-
                A comma-separated list of fields to order by. e.g. "foo,bar"

                The default sort order is ascending. To specify a descending
                order for a

                field, append a " desc" suffix. e.g. "foo desc,bar"

                Subfields are specified with a "." character. e.g. "foo.bar"

                If not specified, the default order is by "name".
        readMask:
          schema:
            - type: string
              required: false
              description: >-
                The fields to be returned in the response. If empty or "*", all
                fields will be returned.
      header: {}
      cookie: {}
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              nodePoolBindings:
                allOf:
                  - type: array
                    items:
                      type: object
                      $ref: '#/components/schemas/gatewayNodePoolBinding'
              nextPageToken:
                allOf:
                  - type: string
                    description: >-
                      A token, which can be sent as `page_token` to retrieve the
                      next page.

                      If this field is omitted, there are no subsequent pages.
              totalSize:
                allOf:
                  - type: integer
                    format: int32
                    description: The total number of node pool bindings.
            refIdentifier: '#/components/schemas/gatewayListNodePoolBindingsResponse'
        examples:
          example:
            value:
              nodePoolBindings:
                - accountId: <string>
                  clusterId: <string>
                  nodePoolId: <string>
                  createTime: '2023-11-07T05:31:56Z'
                  principal: <string>
              nextPageToken: <string>
              totalSize: 123
        description: A successful response.
  deprecated: false
  type: path
components:
  schemas:
    gatewayNodePoolBinding:
      type: object
      properties:
        accountId:
          type: string
          description: The account ID that this binding is associated with.
          readOnly: true
        clusterId:
          type: string
          description: The cluster ID that this binding is associated with.
          readOnly: true
        nodePoolId:
          type: string
          description: The node pool ID that this binding is associated with.
          readOnly: true
        createTime:
          type: string
          format: date-time
          description: The creation time of the node pool binding.
          readOnly: true
        principal:
          type: string
          description: |-
            The principal that is allowed use the node pool. This must be
            the email address of the user.
      required:
        - principal

````