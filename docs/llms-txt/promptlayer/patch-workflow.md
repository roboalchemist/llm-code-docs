# Source: https://docs.promptlayer.com/reference/patch-workflow.md

# Update Agent (PATCH)

Partially update an Agent by creating a new version with merged changes. This endpoint allows you to modify specific nodes without resending the entire configuration.

The PATCH operation:

1. Fetches the specified base version (or latest if not specified)
2. Merges your node updates with existing nodes
3. Creates a new version with the merged configuration

Please note that this feature was previously called "Workflows" and is now called "Agents". Some references to "Workflows" remain in our SDK and will be updated before the feature exits beta.

## HTTP Request

`PATCH /rest/workflows/{workflow_id_or_name}`

## Path Parameters

* **workflow\_id\_or\_name** (string, required): The ID or name of the Agent to update.

## Request Body

The request body expects a JSON object with the following structure:

### Schema

```json  theme={null}
{
  "base_version": "integer (optional)",
  "commit_message": "string (optional)",
  "nodes": {
    "node_name": {
      "node_type": "string (optional)",
      "configuration": "object (optional)",
      "dependencies": ["string"] "(optional)",
      "is_output_node": "boolean (optional)"
    },
    "node_to_remove": null
  },
  "required_input_variables": {
    "variable_name": "type"
  },
  "edges": [...],
  "release_labels": ["string"]
}
```

### Parameters

#### Version Control

* **base\_version** (integer, optional): The version number to base changes on. Defaults to the latest version.
* **commit\_message** (string, optional): A message describing the changes.

#### Node Updates

The `nodes` object is keyed by node name:

* **Updating a node**: Provide the node name with an object containing the fields to update. Unspecified fields are preserved from the base version.
* **Removing a node**: Set the node name to `null`.
* **Adding a node**: Provide a node name that doesn't exist in the base version with `node_type` and `configuration` (required for new nodes). See [Node & Column Types](/features/evaluations/column-types) for available node types.

#### Other Fields

* **required\_input\_variables** (object, optional): If provided, replaces the input variables entirely.
* **edges** (array, optional): If provided, replaces edges entirely. If not provided, edges are copied from the base version (excluding edges referencing removed nodes).
* **release\_labels** (array of strings, optional): Labels to attach to the new version.

## Response

**Status Code**: 201 (Created)

```json  theme={null}
{
  "success": true,
  "message": "Workflow version created successfully",
  "workflow_id": 123,
  "workflow_name": "my-agent",
  "workflow_version_id": 789,
  "version_number": 3,
  "base_version": 2,
  "release_labels": ["staging"],
  "nodes": [
    {
      "id": "uuid",
      "name": "updated_node",
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

### Update a Single Node's Configuration

Update just the configuration of one node while preserving everything else:

```python  theme={null}
import requests

response = requests.patch(
    "https://api.promptlayer.com/rest/workflows/my-agent",
    headers={"X-API-KEY": "your-api-key"},
    json={
        "commit_message": "Updated prompt template version",
        "nodes": {
            "response_generator": {
                "configuration": {
                    "template": {
                        "prompt_name": "response-v2",
                        "label": "production"
                    }
                }
            }
        }
    }
)
```

### Add a New Node

Add a new node to an existing agent:

```python  theme={null}
response = requests.patch(
    "https://api.promptlayer.com/rest/workflows/my-agent",
    headers={"X-API-KEY": "your-api-key"},
    json={
        "commit_message": "Added logging node",
        "nodes": {
            "logger": {
                "node_type": "CODE_EXECUTION",
                "configuration": {
                    "code": "print(f'Processing: {input_data}')",
                    "language": "PYTHON"
                },
                "dependencies": ["input_data"],
                "is_output_node": False
            }
        }
    }
)
```

### Remove a Node

Remove a node from the agent:

```python  theme={null}
response = requests.patch(
    "https://api.promptlayer.com/rest/workflows/my-agent",
    headers={"X-API-KEY": "your-api-key"},
    json={
        "commit_message": "Removed deprecated node",
        "nodes": {
            "old_processor": None  # This removes the node
        }
    }
)
```

### Branch from a Specific Version

Create a new version based on an older version (not the latest):

```python  theme={null}
response = requests.patch(
    "https://api.promptlayer.com/rest/workflows/my-agent",
    headers={"X-API-KEY": "your-api-key"},
    json={
        "base_version": 5,  # Branch from version 5
        "commit_message": "Hotfix based on v5",
        "nodes": {
            "output": {
                "configuration": {
                    "value": {"type": "string", "value": "fixed"}
                }
            }
        }
    }
)
```

### Update Multiple Nodes at Once

```python  theme={null}
response = requests.patch(
    "https://api.promptlayer.com/rest/workflows/my-agent",
    headers={"X-API-KEY": "your-api-key"},
    json={
        "commit_message": "Major update",
        "nodes": {
            "node_a": {
                "configuration": {"value": {"type": "string", "value": "updated_a"}}
            },
            "node_b": {
                "dependencies": ["node_a", "new_input"]
            },
            "old_node": None,  # Remove this node
            "new_node": {      # Add this node
                "node_type": "VARIABLE",
                "configuration": {"value": {"type": "string", "value": "new"}},
                "dependencies": [],
                "is_output_node": False
            }
        },
        "required_input_variables": {
            "original_input": "string",
            "new_input": "string"
        },
        "release_labels": ["staging"]
    }
)
```

### Update and Deploy to Production

```python  theme={null}
response = requests.patch(
    "https://api.promptlayer.com/rest/workflows/123",
    headers={"X-API-KEY": "your-api-key"},
    json={
        "commit_message": "Production deploy",
        "nodes": {
            "response": {
                "configuration": {
                    "template": {"prompt_name": "prod-response", "label": "production"}
                }
            }
        },
        "release_labels": ["production"]  # Move production label to this version
    }
)
```

## Merge Behavior

| Field                        | Merge Behavior                                                 |
| ---------------------------- | -------------------------------------------------------------- |
| `nodes`                      | Merge by name - update matching, keep unmentioned, remove null |
| `nodes[name].configuration`  | Deep merge with existing config                                |
| `nodes[name].dependencies`   | Full replace (not merged)                                      |
| `nodes[name].is_output_node` | Update if specified                                            |
| `required_input_variables`   | Full replace if specified                                      |
| `edges`                      | Full replace if specified, otherwise copied from base          |
| `release_labels`             | Move labels to new version                                     |

## Error Responses

| Status Code | Error                                                   |
| ----------- | ------------------------------------------------------- |
| 400         | Validation error, no output nodes, invalid dependencies |
| 401         | Missing or invalid API key                              |
| 404         | Workflow not found, base version not found              |


## OpenAPI

````yaml PATCH /rest/workflows/{workflow_id_or_name}
openapi: 3.1.0
info:
  title: FastAPI
  version: 0.1.0
servers: []
security: []
paths:
  /rest/workflows/{workflow_id_or_name}:
    patch:
      tags:
        - workflow
      summary: Patch Workflow
      operationId: patchWorkflow
      parameters:
        - name: workflow_id_or_name
          in: path
          required: true
          schema:
            type: string
          description: The ID or name of the workflow to update.
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
              $ref: '#/components/schemas/PatchWorkflow'
      responses:
        '201':
          description: Workflow version created successfully
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
    PatchWorkflow:
      type: object
      properties:
        base_version:
          type: integer
          nullable: true
          description: >-
            The version number to base changes on. Defaults to the latest
            version.
        commit_message:
          type: string
          nullable: true
          description: A message describing the changes.
        nodes:
          type: object
          additionalProperties:
            oneOf:
              - $ref: '#/components/schemas/NodeUpdate'
              - type: 'null'
          nullable: true
          description: Node updates keyed by node name. Use null to remove a node.
        required_input_variables:
          type: object
          additionalProperties:
            type: string
          nullable: true
          description: If provided, replaces the input variables entirely.
        edges:
          type: array
          items:
            $ref: '#/components/schemas/Edge'
          nullable: true
          description: If provided, replaces edges entirely.
        release_labels:
          type: array
          items:
            type: string
          nullable: true
          description: Labels to attach to the new version.
      description: Request body for partially updating a workflow.
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
    NodeUpdate:
      type: object
      properties:
        node_type:
          type: string
          nullable: true
          description: The node type (required for new nodes).
        configuration:
          type: object
          nullable: true
          description: Node configuration to merge.
        dependencies:
          type: array
          items:
            type: string
          nullable: true
          description: Dependencies to replace.
        is_output_node:
          type: boolean
          nullable: true
          description: Whether this is an output node.
      description: Partial update for a single node.
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

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.promptlayer.com/llms.txt