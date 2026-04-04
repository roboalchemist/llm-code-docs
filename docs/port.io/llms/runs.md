# Source: https://docs.port.io/workflows/runs.md

# Interact with workflow runs

When a workflow is executed, it creates a **workflow run** that tracks the execution progress. Each node in the workflow creates a **node run** that captures its status, logs, and output.

## Viewing workflow runs[â](#viewing-workflow-runs "Direct link to Viewing workflow runs")

### From the Workflows page[â](#from-the-workflows-page "Direct link to From the Workflows page")

1. Navigate to the [Workflows page](https://app.getport.io/settings/workflows)
2. Click on a workflow to view its details
3. The **Runs** tab shows all executions of that workflow

### From entity pages[â](#from-entity-pages "Direct link to From entity pages")

Workflow runs associated with an entity appear in the entity's activity feed and can be accessed from the entity page.

## Run structure[â](#run-structure "Direct link to Run structure")

A workflow run contains:

| Field         | Description                                                                |
| ------------- | -------------------------------------------------------------------------- |
| `identifier`  | Unique run identifier (format: `wfr_xxxx`)                                 |
| `status`      | Current status: `IN_PROGRESS` or `COMPLETED`                               |
| `result`      | Final result: `SUCCESS`, `FAILED`, or `CANCELLED` (null while in progress) |
| `nodeRuns`    | Array of node run objects                                                  |
| `variables`   | Runtime variables including outputs                                        |
| `workflow`    | Object containing `identifier` and `version` of the workflow               |
| `createdAt`   | When the run started                                                       |
| `updatedAt`   | When the run was last updated                                              |
| `completedAt` | When the run finished (null while in progress)                             |
| `createdBy`   | User or system that triggered the run                                      |

### Node run structure[â](#node-run-structure "Direct link to Node run structure")

Each node run contains:

| Field         | Description                                                                |
| ------------- | -------------------------------------------------------------------------- |
| `identifier`  | Unique node run identifier (format: `wfnr_xxxx`)                           |
| `node`        | Object containing `identifier` of the node                                 |
| `status`      | Current status: `IN_PROGRESS` or `COMPLETED`                               |
| `result`      | Final result: `SUCCESS`, `FAILED`, or `CANCELLED` (null while in progress) |
| `output`      | Output data from the node                                                  |
| `createdAt`   | When the node started                                                      |
| `updatedAt`   | When the node was last updated                                             |
| `completedAt` | When the node finished (null while in progress)                            |

## Updating node runs[â](#updating-node-runs "Direct link to Updating node runs")

External systems can update node run status and add logs using Port's API. This is useful when:

* Using asynchronous webhooks
* Processing Kafka messages
* Running long-running operations

### Update node run status[â](#update-node-run-status "Direct link to Update node run status")

```
curl -X PATCH "https://api.port.io/v1/workflows/runs/{workflow_run_id}/nodes/{node_run_id}" \
  -H "Authorization: Bearer {token}" \
  -H "Content-Type: application/json" \
  -d '{
    "status": "COMPLETED",
    "result": "SUCCESS",
    "output": {
      "resourceId": "abc123",
      "deploymentUrl": "https://my-app.example.com"
    }
  }'
```

### Request body[â](#request-body "Direct link to Request body")

| Field    | Type     | Description                                                            |
| -------- | -------- | ---------------------------------------------------------------------- |
| `status` | `string` | `IN_PROGRESS` or `COMPLETED`                                           |
| `result` | `string` | Required if status is `COMPLETED`: `SUCCESS`, `FAILED`, or `CANCELLED` |
| `output` | `object` | Output data to make available to subsequent nodes                      |

### Adding logs[â](#adding-logs "Direct link to Adding logs")

Use the dedicated logs endpoint to add log entries to a node run:

```
curl -X POST "https://api.port.io/v1/workflows/nodes/runs/{node_run_identifier}/logs" \
  -H "Authorization: Bearer {token}" \
  -H "Content-Type: application/json" \
  -d '{
    "logs": [
      {
        "level": "INFO",
        "message": "Starting deployment to production"
      },
      {
        "level": "INFO",
        "message": "Deployment completed successfully"
      }
    ]
  }'
```

### Log entry structure[â](#log-entry-structure "Direct link to Log entry structure")

| Field     | Type     | Description                                    |
| --------- | -------- | ---------------------------------------------- |
| `level`   | `string` | Log level: `DEBUG`, `INFO`, `WARN`, or `ERROR` |
| `message` | `string` | The log message                                |

Log levels: `DEBUG`, `INFO`, `WARN`, `ERROR`

## Run outputs[â](#run-outputs "Direct link to Run outputs")

Node outputs are stored in the workflow run's `variables.outputs` and can be referenced by subsequent nodes.

For webhook nodes (without custom `variables`), the output includes the full response:

```
{
  "outputs": {
    "create_resource": {
      "response": {
        "data": {
          "resourceId": "abc123",
          "resourceUrl": "https://..."
        }
      }
    }
  }
}
```

Reference in subsequent nodes:

```
{
  "body": {
    "resourceId": "{{ .outputs.create_resource.response.data.resourceId }}"
  }
}
```

If you define custom `variables` on a node, only those variables are stored as outputs (see [Data flow](/workflows/build-workflows/data-flow.md#variables)).

## Configure visibility for action runs[â](#configure-visibility-for-action-runs "Direct link to Configure visibility for action runs")

By default, all organization members can view workflow runs. You can restrict this access using the `allowAnyoneToViewRuns` property in the workflow definition:

* **When enabled (default):** All organization members can view the workflow's runs.
* **When disabled:** Admins can view all runs, while members can only view the runs they executed.

This ensures that sensitive operational data remains accessible only to authorized users while maintaining transparency where appropriate.

**Example workflow definition with restricted visibility:**

```
{
  "identifier": "my_workflow",
  "allowAnyoneToViewRuns": false,
  // ...
}
```

## Example[â](#example "Direct link to Example")

**External processing**

Here's an example of how an external system might process a webhook action:

**Python example (click to expand)**

```
import requests

def process_webhook(webhook_data):
    """Process a webhook and report back to Port"""
    
    workflow_run_id = webhook_data['context']['workflowRunId']
    node_run_id = webhook_data['context']['nodeRunId']
    
    # Log the start
    add_node_run_logs(node_run_id, [{
        "level": "INFO",
        "message": "Processing started"
    }])
    
    try:
        # Do the actual work
        result = perform_operation(webhook_data['payload'])
        
        # Log success
        add_node_run_logs(node_run_id, [{
            "level": "INFO",
            "message": f"Operation completed: {result}"
        }])
        
        # Report success
        update_node_run(workflow_run_id, node_run_id, {
            "status": "COMPLETED",
            "result": "SUCCESS",
            "output": result
        })
    except Exception as e:
        # Log and report failure
        add_node_run_logs(node_run_id, [{
            "level": "ERROR",
            "message": f"Operation failed: {str(e)}"
        }])
        
        update_node_run(workflow_run_id, node_run_id, {
            "status": "COMPLETED",
            "result": "FAILED"
        })

def add_node_run_logs(node_run_id, logs):
    """Add logs to a node run via Port API"""
    response = requests.post(
        f"https://api.port.io/v1/workflows/nodes/runs/{node_run_id}/logs",
        headers={
            "Authorization": f"Bearer {get_port_token()}",
            "Content-Type": "application/json"
        },
        json={"logs": logs}
    )
    response.raise_for_status()

def update_node_run(workflow_run_id, node_run_id, data):
    """Update a node run via Port API"""
    response = requests.patch(
        f"https://api.port.io/v1/workflows/runs/{workflow_run_id}/nodes/{node_run_id}",
        headers={
            "Authorization": f"Bearer {get_port_token()}",
            "Content-Type": "application/json"
        },
        json=data
    )
    response.raise_for_status()
```

## Limitations[â](#limitations "Direct link to Limitations")

The following run features are not yet available in workflows (Beta):

* **Re-run workflow**: Ability to re-run a workflow from the UI.
* **Partial re-run**: Re-run from a specific node.
* **Cancel in-progress run**: Cancel a running workflow.
