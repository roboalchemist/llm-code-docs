# Source: https://docs.prefect.io/v3/api-ref/rest-api/server/deployments/bulk-delete-deployments.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Bulk Delete Deployments

> Bulk delete deployments matching the specified filter criteria.

Returns the IDs of deployments that were deleted.



## OpenAPI

````yaml post /deployments/bulk_delete
openapi: 3.1.0
info:
  title: Prefect Prefect REST API
  version: v3
  x-logo:
    url: static/prefect-logo-mark-gradient.png
servers: []
security: []
paths:
  /deployments/bulk_delete:
    post:
      tags:
        - Deployments
      summary: Bulk Delete Deployments
      description: |-
        Bulk delete deployments matching the specified filter criteria.

        Returns the IDs of deployments that were deleted.
      operationId: bulk_delete_deployments_deployments_bulk_delete_post
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
                #/components/schemas/Body_bulk_delete_deployments_deployments_bulk_delete_post
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/DeploymentBulkDeleteResponse'
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
components:
  schemas:
    Body_bulk_delete_deployments_deployments_bulk_delete_post:
      properties:
        deployments:
          anyOf:
            - $ref: '#/components/schemas/DeploymentFilter'
            - type: 'null'
          description: Filter criteria for deployments to delete
        limit:
          type: integer
          maximum: 50
          minimum: 1
          title: Limit
          description: Maximum number of deployments to delete. Defaults to 50.
          default: 50
      type: object
      title: Body_bulk_delete_deployments_deployments_bulk_delete_post
    DeploymentBulkDeleteResponse:
      properties:
        deleted:
          items:
            type: string
            format: uuid
          type: array
          title: Deleted
      type: object
      title: DeploymentBulkDeleteResponse
      description: Response from bulk deployment deletion.
    HTTPValidationError:
      properties:
        detail:
          items:
            $ref: '#/components/schemas/ValidationError'
          type: array
          title: Detail
      type: object
      title: HTTPValidationError
    DeploymentFilter:
      properties:
        operator:
          $ref: '#/components/schemas/Operator'
          description: Operator for combining filter criteria. Defaults to 'and_'.
          default: and_
        id:
          anyOf:
            - $ref: '#/components/schemas/DeploymentFilterId'
            - type: 'null'
          description: Filter criteria for `Deployment.id`
        name:
          anyOf:
            - $ref: '#/components/schemas/DeploymentFilterName'
            - type: 'null'
          description: Filter criteria for `Deployment.name`
        flow_or_deployment_name:
          anyOf:
            - $ref: '#/components/schemas/DeploymentOrFlowNameFilter'
            - type: 'null'
          description: Filter criteria for `Deployment.name` or `Flow.name`
        paused:
          anyOf:
            - $ref: '#/components/schemas/DeploymentFilterPaused'
            - type: 'null'
          description: Filter criteria for `Deployment.paused`
        tags:
          anyOf:
            - $ref: '#/components/schemas/DeploymentFilterTags'
            - type: 'null'
          description: Filter criteria for `Deployment.tags`
        work_queue_name:
          anyOf:
            - $ref: '#/components/schemas/DeploymentFilterWorkQueueName'
            - type: 'null'
          description: Filter criteria for `Deployment.work_queue_name`
        concurrency_limit:
          anyOf:
            - $ref: '#/components/schemas/DeploymentFilterConcurrencyLimit'
            - type: 'null'
          description: >-
            DEPRECATED: Prefer `Deployment.concurrency_limit_id` over
            `Deployment.concurrency_limit`. If provided, will be ignored for
            backwards-compatibility. Will be removed after December 2024.
          deprecated: true
      additionalProperties: false
      type: object
      title: DeploymentFilter
      description: >-
        Filter for deployments. Only deployments matching all criteria will be
        returned.
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
    DeploymentFilterId:
      properties:
        any_:
          anyOf:
            - items:
                type: string
                format: uuid
              type: array
            - type: 'null'
          title: Any
          description: A list of deployment ids to include
        not_any_:
          anyOf:
            - items:
                type: string
                format: uuid
              type: array
            - type: 'null'
          title: Not Any
          description: A list of deployment ids to exclude
      additionalProperties: false
      type: object
      title: DeploymentFilterId
      description: Filter by `Deployment.id`.
    DeploymentFilterName:
      properties:
        any_:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          title: Any
          description: A list of deployment names to include
          examples:
            - - my-deployment-1
              - my-deployment-2
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
      title: DeploymentFilterName
      description: Filter by `Deployment.name`.
    DeploymentOrFlowNameFilter:
      properties:
        like_:
          anyOf:
            - type: string
            - type: 'null'
          title: Like
          description: >-
            A case-insensitive partial match on deployment or flow names. For
            example, passing 'example' might match deployments or flows with
            'example' in their names.
      additionalProperties: false
      type: object
      title: DeploymentOrFlowNameFilter
      description: >-
        Filter by `Deployment.name` or `Flow.name` with a single input string
        for ilike filtering.
    DeploymentFilterPaused:
      properties:
        eq_:
          anyOf:
            - type: boolean
            - type: 'null'
          title: Eq
          description: Only returns where deployment is/is not paused
      additionalProperties: false
      type: object
      title: DeploymentFilterPaused
      description: Filter by `Deployment.paused`.
    DeploymentFilterTags:
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
            A list of tags. Deployments will be returned only if their tags are
            a superset of the list
          examples:
            - - tag-1
              - tag-2
        any_:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          title: Any
          description: A list of tags to include
          examples:
            - - tag-1
              - tag-2
        is_null_:
          anyOf:
            - type: boolean
            - type: 'null'
          title: Is Null
          description: If true, only include deployments without tags
      additionalProperties: false
      type: object
      title: DeploymentFilterTags
      description: Filter by `Deployment.tags`.
    DeploymentFilterWorkQueueName:
      properties:
        any_:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          title: Any
          description: A list of work queue names to include
          examples:
            - - work_queue_1
              - work_queue_2
      additionalProperties: false
      type: object
      title: DeploymentFilterWorkQueueName
      description: Filter by `Deployment.work_queue_name`.
    DeploymentFilterConcurrencyLimit:
      properties:
        ge_:
          anyOf:
            - type: integer
            - type: 'null'
          title: Ge
          description: >-
            Only include deployments with a concurrency limit greater than or
            equal to this value
        le_:
          anyOf:
            - type: integer
            - type: 'null'
          title: Le
          description: >-
            Only include deployments with a concurrency limit less than or equal
            to this value
        is_null_:
          anyOf:
            - type: boolean
            - type: 'null'
          title: Is Null
          description: If true, only include deployments without a concurrency limit
      additionalProperties: false
      type: object
      title: DeploymentFilterConcurrencyLimit
      description: >-
        DEPRECATED: Prefer `Deployment.concurrency_limit_id` over
        `Deployment.concurrency_limit`.

````

Built with [Mintlify](https://mintlify.com).