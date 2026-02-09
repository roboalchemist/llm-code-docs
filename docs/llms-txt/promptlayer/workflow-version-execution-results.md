# Source: https://docs.promptlayer.com/reference/workflow-version-execution-results.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.promptlayer.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Agent Version Execution Results

Retrieve the execution results of a specific Agent version. You can include all output nodes by setting the `return_all_outputs` query parameter to `true`.

This endpoint returns a status code of `200` when the agent has finished execution. If the agent is still in the process of running, it will return a status code of `202`.

Please note that this feature was previously called "Workflows" and is now called "Agents". Some references to "Workflows" remain in our SDK and will be updated before the feature exits beta.


## OpenAPI

````yaml GET /workflow-version-execution-results
openapi: 3.1.0
info:
  title: FastAPI
  version: 0.1.0
servers: []
security: []
paths:
  /workflow-version-execution-results:
    get:
      tags:
        - workflow
      summary: Get Workflow Version Execution Results
      operationId: getWorkflowVersionExecutionResults
      parameters:
        - name: workflow_version_execution_id
          in: query
          required: true
          schema:
            type: integer
            format: int64
          description: >-
            The unique identifier of the workflow version execution whose
            results you want to retrieve.
        - name: return_all_outputs
          in: query
          required: false
          schema:
            type: boolean
            default: false
          description: >-
            When set to true, the response includes all output nodes' results.
            If omitted or set to false, only the main output is returned.
        - name: X-API-KEY
          in: header
          required: true
          schema:
            type: string
          description: Your API key for authentication.
      responses:
        '200':
          description: Successful response with execution results.
          content:
            application/json:
              schema:
                oneOf:
                  - type: object
                    additionalProperties:
                      type: object
                      properties:
                        status:
                          type: string
                          description: The status of the node execution.
                        value:
                          description: The output value of the node.
                        error_message:
                          type: string
                          nullable: true
                          description: Error message if the node failed.
                        raw_error_message:
                          type: string
                          nullable: true
                          description: Raw error message if the node failed.
                        is_output_node:
                          type: boolean
                          description: Whether this node is an output node.
                  - description: >-
                      The main output value of the workflow execution when
                      return_all_outputs is false.
        '400':
          description: Bad Request
        '401':
          description: Unauthorized
        '403':
          description: Forbidden
        '404':
          description: Not Found
      security:
        - ApiKeyAuth: []
components:
  securitySchemes:
    ApiKeyAuth:
      type: apiKey
      in: header
      name: X-API-KEY

````