# Source: https://docs.promptlayer.com/reference/run-workflow.md

# Run Agent

Initiate the execution of a specific Agent by its name. You can specify input variables, metadata, and choose which version of the Agent to run.

Please note that this feature was previously called "Workflows" and is now called "Agents". Some references to "Workflows" remain in our SDK and will be updated before the feature exits beta.

## HTTP Request

`POST /workflows/{workflow_name}/run`

## Path Parameters

* **workflow\_name** (string, required): The name of the Agent you wish to execute.

## Request Body

The request body expects a JSON object with the following structure:

### Schema

```json  theme={null}
{
  "workflow_label_name": "string (optional)",
  "workflow_version_number": "integer (optional)",
  "metadata": {
    "string": "string"
  },
  "input_variables": {
    "string": "any"
  },
  "return_all_outputs": "boolean (default: false)",
  "callback_url": "string (optional)"
}
```

### Parameters

* **workflow\_label\_name** (string, optional): The label of the specific Agent version to run.
* **workflow\_version\_number** (integer, optional): The version number of the Agent to run.
* **metadata** (object, optional): Additional metadata to attach to the execution.
* **input\_variables** (object, optional): Input variables for the Agent execution.
* **return\_all\_outputs** (boolean, optional, default: false): Whether to return all node outputs or just the final output.
* **callback\_url** (string, optional): An HTTP URL where execution results will be POSTed when the Agent completes. When provided, the API returns HTTP 202 (Accepted) immediately and sends results to this URL asynchronously. Ideal for long-running agents and webhook-based integrations.

## Response

**Status Code**: 201 (Created) or 202 (Accepted) if `callback_url` is provided

When a `callback_url` is provided, PromptLayer will POST the following to your callback URL when the agent completes:

```json  theme={null}
{
  "workflow_version_execution_id": "integer",
  "final_output": {
    "Node Name": {
      "status": "SUCCESS | FAILURE",
      "value": "any",
      "error_message": "string | null",
      "raw_error_message": "string | null",
      "is_output_node": "boolean"
    }
  }
}
```

The `final_output` structure matches the response from the [GET /workflow-version-execution-results](/reference/workflow-version-execution-results) endpoint.


## OpenAPI

````yaml POST /workflows/{workflow_name}/run
openapi: 3.1.0
info:
  title: FastAPI
  version: 0.1.0
servers: []
security: []
paths:
  /workflows/{workflow_name}/run:
    post:
      tags:
        - workflow
      summary: Run Workflow
      operationId: runWorkflow
      parameters:
        - name: workflow_name
          in: path
          required: true
          schema:
            type: string
          description: The name of the workflow to execute.
        - name: X-API-KEY
          in: header
          required: true
          schema:
            type: string
          description: Your API key for authentication.
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/RunWorkflow'
      responses:
        '201':
          description: Workflow execution created successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/RunWorkflowResponse'
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
        '401':
          description: Unauthorized
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
        '404':
          description: Not Found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
components:
  schemas:
    RunWorkflow:
      type: object
      properties:
        workflow_label_name:
          type: string
          nullable: true
          description: Specify a workflow label name to run a specific labeled version.
        workflow_version_number:
          type: integer
          nullable: true
          description: Specify a workflow version number to run a specific version.
        metadata:
          type: object
          additionalProperties:
            type: string
          nullable: true
          description: A dictionary of metadata key-value pairs.
        input_variables:
          type: object
          additionalProperties: true
          default: {}
          description: A dictionary of input variables required by the workflow.
        return_all_outputs:
          type: boolean
          default: false
          description: >-
            If set to `true`, all outputs from the workflow execution will be
            returned.
      required: []
      description: Parameters to run a workflow.
    RunWorkflowResponse:
      type: object
      properties:
        success:
          type: boolean
          description: Indicates if the request was successful.
        message:
          type: string
          description: A message describing the result.
        warning:
          type: string
          nullable: true
          description: Any warnings about missing input variables.
        workflow_version_execution_id:
          type: integer
          description: The ID of the created workflow execution.
      required:
        - success
        - message
        - workflow_version_execution_id
      description: Response after initiating a workflow execution.
    ErrorResponse:
      type: object
      properties:
        success:
          type: boolean
          default: false
          description: Indicates that the request failed.
        error:
          type: string
          description: Error message explaining why the request failed.
      required:
        - success
        - error
      description: Error response format.

````

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.promptlayer.com/llms.txt