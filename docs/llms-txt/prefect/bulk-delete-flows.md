# Source: https://docs.prefect.io/v3/api-ref/rest-api/server/flows/bulk-delete-flows.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Bulk Delete Flows

> Bulk delete flows matching the specified filter criteria.

This also deletes all associated deployments.

Returns the IDs of flows that were deleted.



## OpenAPI

````yaml post /flows/bulk_delete
openapi: 3.1.0
info:
  title: Prefect Prefect REST API
  version: v3
  x-logo:
    url: static/prefect-logo-mark-gradient.png
servers: []
security: []
paths:
  /flows/bulk_delete:
    post:
      tags:
        - Flows
      summary: Bulk Delete Flows
      description: |-
        Bulk delete flows matching the specified filter criteria.

        This also deletes all associated deployments.

        Returns the IDs of flows that were deleted.
      operationId: bulk_delete_flows_flows_bulk_delete_post
      parameters:
        - name: x-prefect-api-version
          in: header
          required: false
          schema:
            type: string
            title: X-Prefect-Api-Version
      requestBody:
        content:
          application/json:
            schema:
              $ref: >-
                #/components/schemas/Body_bulk_delete_flows_flows_bulk_delete_post
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/FlowBulkDeleteResponse'
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
components:
  schemas:
    Body_bulk_delete_flows_flows_bulk_delete_post:
      properties:
        flows:
          anyOf:
            - $ref: '#/components/schemas/FlowFilter'
            - type: 'null'
          description: Filter criteria for flows to delete
        limit:
          type: integer
          maximum: 50
          minimum: 1
          title: Limit
          description: Maximum number of flows to delete. Defaults to 50.
          default: 50
      type: object
      title: Body_bulk_delete_flows_flows_bulk_delete_post
    FlowBulkDeleteResponse:
      properties:
        deleted:
          items:
            type: string
            format: uuid
          type: array
          title: Deleted
      type: object
      title: FlowBulkDeleteResponse
      description: Response from bulk flow deletion.
    HTTPValidationError:
      properties:
        detail:
          items:
            $ref: '#/components/schemas/ValidationError'
          type: array
          title: Detail
      type: object
      title: HTTPValidationError
    FlowFilter:
      properties:
        operator:
          $ref: '#/components/schemas/Operator'
          description: Operator for combining filter criteria. Defaults to 'and_'.
          default: and_
        id:
          anyOf:
            - $ref: '#/components/schemas/FlowFilterId'
            - type: 'null'
          description: Filter criteria for `Flow.id`
        deployment:
          anyOf:
            - $ref: '#/components/schemas/FlowFilterDeployment'
            - type: 'null'
          description: Filter criteria for Flow deployments
        name:
          anyOf:
            - $ref: '#/components/schemas/FlowFilterName'
            - type: 'null'
          description: Filter criteria for `Flow.name`
        tags:
          anyOf:
            - $ref: '#/components/schemas/FlowFilterTags'
            - type: 'null'
          description: Filter criteria for `Flow.tags`
      additionalProperties: false
      type: object
      title: FlowFilter
      description: Filter for flows. Only flows matching all criteria will be returned.
    ValidationError:
      properties:
        loc:
          items:
            anyOf:
              - type: string
              - type: integer
          type: array
          title: Location
        msg:
          type: string
          title: Message
        type:
          type: string
          title: Error Type
        input:
          title: Input
        ctx:
          type: object
          title: Context
      type: object
      required:
        - loc
        - msg
        - type
      title: ValidationError
    Operator:
      type: string
      enum:
        - and_
        - or_
      title: Operator
      description: Operators for combining filter criteria.
    FlowFilterId:
      properties:
        any_:
          anyOf:
            - items:
                type: string
                format: uuid
              type: array
            - type: 'null'
          title: Any
          description: A list of flow ids to include
        not_any_:
          anyOf:
            - items:
                type: string
                format: uuid
              type: array
            - type: 'null'
          title: Not Any
          description: A list of flow ids to exclude
      additionalProperties: false
      type: object
      title: FlowFilterId
      description: Filter by `Flow.id`.
    FlowFilterDeployment:
      properties:
        operator:
          $ref: '#/components/schemas/Operator'
          description: Operator for combining filter criteria. Defaults to 'and_'.
          default: and_
        is_null_:
          anyOf:
            - type: boolean
            - type: 'null'
          title: Is Null
          description: If true, only include flows without deployments
      additionalProperties: false
      type: object
      title: FlowFilterDeployment
      description: Filter by flows by deployment
    FlowFilterName:
      properties:
        any_:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          title: Any
          description: A list of flow names to include
          examples:
            - - my-flow-1
              - my-flow-2
        like_:
          anyOf:
            - type: string
            - type: 'null'
          title: Like
          description: >-
            A case-insensitive partial match. For example,  passing 'marvin'
            will match 'marvin', 'sad-Marvin', and 'marvin-robot'.
          examples:
            - marvin
      additionalProperties: false
      type: object
      title: FlowFilterName
      description: Filter by `Flow.name`.
    FlowFilterTags:
      properties:
        operator:
          $ref: '#/components/schemas/Operator'
          description: Operator for combining filter criteria. Defaults to 'and_'.
          default: and_
        all_:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          title: All
          description: >-
            A list of tags. Flows will be returned only if their tags are a
            superset of the list
          examples:
            - - tag-1
              - tag-2
        is_null_:
          anyOf:
            - type: boolean
            - type: 'null'
          title: Is Null
          description: If true, only include flows without tags
      additionalProperties: false
      type: object
      title: FlowFilterTags
      description: Filter by `Flow.tags`.

````

Built with [Mintlify](https://mintlify.com).