# Source: https://docs.promptlayer.com/reference/create-workflow.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.promptlayer.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Create Agent

Create a new Agent or a new version of an existing Agent programmatically. This endpoint allows you to define the complete agent configuration including nodes, edges (conditional connections), input variables, and release labels.

Please note that this feature was previously called "Workflows" and is now called "Agents". Some references to "Workflows" remain in our SDK and will be updated before the feature exits beta.

## HTTP Request

`POST /rest/workflows`

## Request Body

The request body expects a JSON object with the following structure:

### Schema

```json  theme={null}
{
  "name": "string (optional, for new agents)",
  "workflow_id": "integer (optional, for new version of existing agent)",
  "workflow_name": "string (optional, for new version of existing agent)",
  "folder_id": "integer (optional)",
  "commit_message": "string (optional)",
  "nodes": [
    {
      "name": "string (required)",
      "node_type": "string (required)",
      "configuration": "object (required)",
      "dependencies": ["string"],
      "is_output_node": "boolean"
    }
  ],
  "required_input_variables": {
    "variable_name": "type"
  },
  "edges": [
    {
      "source_node_name": "string",
      "target_node_name": "string",
      "is_and": "boolean",
      "conditionals": [
        {
          "position": "integer",
          "operator": "string",
          "left_config": "object",
          "right_config": "object"
        }
      ]
    }
  ],
  "release_labels": ["string"]
}
```

### Parameters

#### Agent Identification

* **name** (string, optional): The name for a new agent. If not provided, a name will be auto-generated. Cannot be used with `workflow_id` or `workflow_name`.
* **workflow\_id** (integer, optional): The ID of an existing agent to create a new version for.
* **workflow\_name** (string, optional): The name of an existing agent to create a new version for.
* **folder\_id** (integer, optional): The folder ID to place the agent in.

#### Version Details

* **commit\_message** (string, optional): A message describing the changes in this version.

#### Nodes

Each node represents a step in the agent workflow:

* **name** (string, required): Unique name for the node within this agent.
* **node\_type** (string, required): The type of node. See [Node Types](#node-types) below.
* **configuration** (object, required): Node-specific configuration.
* **dependencies** (array of strings, optional): Names of nodes or input variables this node depends on.
* **is\_output\_node** (boolean, required): Whether this node is an output node. At least one node must be an output node.

#### Input Variables

* **required\_input\_variables** (object, optional): A mapping of variable names to their types (e.g., `{"user_query": "string"}`).

#### Edges (Conditional Connections)

Edges define conditional branching between nodes:

* **source\_node\_name** (string, required): The source node name.
* **target\_node\_name** (string, required): The target node name (must have source in its dependencies).
* **is\_and** (boolean, required): Whether multiple conditionals use AND logic (true) or OR logic (false).
* **conditionals** (array, required): At least one conditional:
  * **position** (integer): Order of evaluation.
  * **operator** (string): One of `=`, `!=`, `<`, `>`, `<=`, `>=`, `in`, `not_in`, `is_null`, `is_not_null`.
  * **left\_config** (object): Left side of comparison.
  * **right\_config** (object): Right side of comparison.

#### Release Labels

* **release\_labels** (array of strings, optional): Labels to attach to this version (e.g., `["production", "staging"]`).

## Node Types

Agents use the same node types as evaluation pipelines. For the complete list of supported node types and their detailed configuration options, see the [Node & Column Types](/features/evaluations/column-types) documentation.

Common node types include:

| Node Type            | Description                                                                                          |
| -------------------- | ---------------------------------------------------------------------------------------------------- |
| `VARIABLE`           | Static value                                                                                         |
| `CODE_EXECUTION`     | Run Python or JavaScript code                                                                        |
| `PROMPT_TEMPLATE`    | Call an LLM with a prompt template                                                                   |
| `ENDPOINT`           | Make an HTTP request                                                                                 |
| `FOR_LOOP`           | Iterate over a collection ([details](/features/evaluations/column-types#for-loop-for_loop))          |
| `WHILE_LOOP`         | Execute until condition is met ([details](/features/evaluations/column-types#while-loop-while_loop)) |
| `COMPARE`            | Compare two values                                                                                   |
| `CONTAINS`           | Check if string contains value                                                                       |
| `LLM_ASSERTION`      | LLM-based evaluation                                                                                 |
| `AI_DATA_EXTRACTION` | Extract structured data                                                                              |
| `CODING_AGENT`       | Claude Code sandbox                                                                                  |

## Response

**Status Code**: 201 (Created)

```json  theme={null}
{
  "success": true,
  "message": "Workflow created successfully",
  "workflow_id": 123,
  "workflow_name": "my-agent",
  "workflow_version_id": 456,
  "version_number": 1,
  "release_labels": ["production"],
  "nodes": [
    {
      "id": "uuid",
      "name": "output_node",
      "node_type": "VARIABLE",
      "is_output_node": true
    }
  ],
  "required_input_variables": {
    "user_input": "string"
  }
}
```

## Examples

### Create a Simple Agent

```python  theme={null}
import requests

response = requests.post(
    "https://api.promptlayer.com/rest/workflows",
    headers={"X-API-KEY": "your-api-key"},
    json={
        "name": "greeting-agent",
        "commit_message": "Initial version",
        "nodes": [
            {
                "name": "greeting",
                "node_type": "VARIABLE",
                "is_output_node": True,
                "configuration": {
                    "value": {"type": "string", "value": "Hello, World!"}
                },
                "dependencies": []
            }
        ],
        "release_labels": ["production"]
    }
)
```

### Create an Agent with Multiple Nodes

```python  theme={null}
response = requests.post(
    "https://api.promptlayer.com/rest/workflows",
    headers={"X-API-KEY": "your-api-key"},
    json={
        "name": "classifier-agent",
        "nodes": [
            {
                "name": "classify",
                "node_type": "PROMPT_TEMPLATE",
                "is_output_node": False,
                "configuration": {
                    "template": {
                        "prompt_name": "intent-classifier",
                        "label": "production"
                    }
                },
                "dependencies": ["user_message"]
            },
            {
                "name": "is_urgent",
                "node_type": "CONTAINS",
                "is_output_node": False,
                "configuration": {
                    "source": "classify",
                    "value": "urgent"
                },
                "dependencies": ["classify"]
            },
            {
                "name": "response",
                "node_type": "PROMPT_TEMPLATE",
                "is_output_node": True,
                "configuration": {
                    "template": {
                        "prompt_name": "response-generator",
                        "label": "production"
                    }
                },
                "dependencies": ["classify", "is_urgent", "user_message"]
            }
        ],
        "required_input_variables": {
            "user_message": "string"
        }
    }
)
```

### Create an Agent with Conditional Edges

```python  theme={null}
response = requests.post(
    "https://api.promptlayer.com/rest/workflows",
    headers={"X-API-KEY": "your-api-key"},
    json={
        "name": "routing-agent",
        "nodes": [
            {
                "name": "router",
                "node_type": "PROMPT_TEMPLATE",
                "is_output_node": False,
                "configuration": {"template": {"prompt_name": "router"}},
                "dependencies": ["query"]
            },
            {
                "name": "sales_handler",
                "node_type": "PROMPT_TEMPLATE",
                "is_output_node": True,
                "configuration": {"template": {"prompt_name": "sales-response"}},
                "dependencies": ["router", "query"]
            },
            {
                "name": "support_handler",
                "node_type": "PROMPT_TEMPLATE",
                "is_output_node": True,
                "configuration": {"template": {"prompt_name": "support-response"}},
                "dependencies": ["router", "query"]
            }
        ],
        "required_input_variables": {"query": "string"},
        "edges": [
            {
                "source_node_name": "router",
                "target_node_name": "sales_handler",
                "is_and": True,
                "conditionals": [{
                    "position": 0,
                    "operator": "=",
                    "left_config": {"type": "source", "source": {"name": "router"}},
                    "right_config": {"type": "static_value", "static_value": "sales"}
                }]
            },
            {
                "source_node_name": "router",
                "target_node_name": "support_handler",
                "is_and": True,
                "conditionals": [{
                    "position": 0,
                    "operator": "=",
                    "left_config": {"type": "source", "source": {"name": "router"}},
                    "right_config": {"type": "static_value", "static_value": "support"}
                }]
            }
        ]
    }
)
```

### Create a New Version of an Existing Agent

```python  theme={null}
# By workflow ID
response = requests.post(
    "https://api.promptlayer.com/rest/workflows",
    headers={"X-API-KEY": "your-api-key"},
    json={
        "workflow_id": 123,
        "commit_message": "Updated configuration",
        "nodes": [...],
        "release_labels": ["staging"]
    }
)

# By workflow name
response = requests.post(
    "https://api.promptlayer.com/rest/workflows",
    headers={"X-API-KEY": "your-api-key"},
    json={
        "workflow_name": "my-agent",
        "commit_message": "v2 updates",
        "nodes": [...],
        "release_labels": ["production"]
    }
)
```

## Error Responses

| Status Code | Error                                                          |
| ----------- | -------------------------------------------------------------- |
| 400         | Invalid request body, duplicate name, validation errors        |
| 401         | Missing or invalid API key                                     |
| 404         | Workflow not found (when using workflow\_id or workflow\_name) |


## OpenAPI

````yaml POST /rest/workflows
openapi: 3.1.0
info:
  title: FastAPI
  version: 0.1.0
servers: []
security: []
paths:
  /rest/workflows:
    post:
      tags:
        - workflow
      summary: Create Workflow
      operationId: createWorkflow
      parameters:
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
              $ref: '#/components/schemas/CreateWorkflow'
      responses:
        '201':
          description: Workflow created successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CreateWorkflowResponse'
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
    CreateWorkflow:
      type: object
      properties:
        name:
          type: string
          minLength: 1
          maxLength: 255
          nullable: true
          description: >-
            The name for a new workflow. If not provided, a name will be
            auto-generated.
        workflow_id:
          type: integer
          nullable: true
          description: The ID of an existing workflow to create a new version for.
        workflow_name:
          type: string
          nullable: true
          description: The name of an existing workflow to create a new version for.
        folder_id:
          type: integer
          nullable: true
          description: The folder ID to place the workflow in.
        commit_message:
          type: string
          nullable: true
          description: A message describing the changes in this version.
        nodes:
          type: array
          items:
            $ref: '#/components/schemas/WorkflowNode'
          description: The nodes in the workflow.
        required_input_variables:
          type: object
          additionalProperties:
            type: string
          description: A mapping of variable names to their types.
        edges:
          type: array
          items:
            $ref: '#/components/schemas/Edge'
          nullable: true
          description: Conditional edges between nodes.
        release_labels:
          type: array
          items:
            type: string
          nullable: true
          description: Labels to attach to this version.
      required:
        - nodes
      description: Request body for creating a new workflow or workflow version.
    CreateWorkflowResponse:
      type: object
      properties:
        success:
          type: boolean
          description: Indicates if the request was successful.
        workflow_id:
          type: integer
          description: The ID of the workflow.
        workflow_name:
          type: string
          description: The name of the workflow.
        workflow_version_id:
          type: integer
          description: The ID of the created workflow version.
        version_number:
          type: integer
          description: The version number.
        base_version:
          type: integer
          nullable: true
          description: The base version this was created from (PATCH only).
        release_labels:
          type: array
          items:
            type: string
          nullable: true
          description: Labels attached to this version.
        nodes:
          type: array
          items:
            type: object
            properties:
              id:
                type: string
              name:
                type: string
              node_type:
                type: string
              is_output_node:
                type: boolean
          description: Summary of nodes in the workflow.
        required_input_variables:
          type: object
          additionalProperties:
            type: string
          description: Required input variables for the workflow.
      required:
        - success
        - workflow_id
        - workflow_name
        - workflow_version_id
        - version_number
      description: Response after creating or patching a workflow.
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
    WorkflowNode:
      type: object
      properties:
        name:
          type: string
          minLength: 1
          maxLength: 255
          description: Unique name for the node within this workflow.
        node_type:
          type: string
          description: >-
            The type of node. Common types include VARIABLE, CODE_EXECUTION,
            PROMPT_TEMPLATE, ENDPOINT, COMPARE, CONTAINS, LLM_ASSERTION,
            AI_DATA_EXTRACTION, CODING_AGENT. See Node & Column Types
            documentation for the complete list.
        configuration:
          type: object
          description: Node-specific configuration.
        dependencies:
          type: array
          items:
            type: string
          description: Names of nodes or input variables this node depends on.
        is_output_node:
          type: boolean
          description: Whether this node is an output node.
      required:
        - name
        - node_type
        - configuration
        - is_output_node
    Edge:
      type: object
      properties:
        source_node_name:
          type: string
          description: The source node name.
        target_node_name:
          type: string
          description: The target node name.
        is_and:
          type: boolean
          description: >-
            Whether multiple conditionals use AND logic (true) or OR logic
            (false).
        conditionals:
          type: array
          items:
            $ref: '#/components/schemas/EdgeConditional'
          minItems: 1
          description: At least one conditional.
      required:
        - source_node_name
        - target_node_name
        - is_and
        - conditionals
    EdgeConditional:
      type: object
      properties:
        position:
          type: integer
          minimum: 0
          description: Order of evaluation.
        operator:
          type: string
          enum:
            - '='
            - '!='
            - <
            - '>'
            - <=
            - '>='
            - in
            - not_in
            - is_null
            - is_not_null
          description: Comparison operator.
        left_config:
          type: object
          description: Left side of comparison. Can be static_value or source.
        right_config:
          type: object
          description: Right side of comparison. Can be static_value or source.
      required:
        - position
        - operator
        - left_config
        - right_config

````