# Source: https://docs.datadoghq.com/api/latest/workflow-automation

This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). (US1).
# Workflow Automation
Datadog Workflow Automation allows you to automate your end-to-end processes by connecting Datadog with the rest of your tech stack. Build workflows to auto-remediate your alerts, streamline your incident and security processes, and reduce manual toil. Workflow Automation supports over 1,000+ OOTB actions, including AWS, JIRA, ServiceNow, GitHub, and OpenAI. Learn more in our Workflow Automation docs [here](https://docs.datadoghq.com/service_management/workflows/).
## [Get an existing Workflow](https://docs.datadoghq.com/api/latest/workflow-automation/#get-an-existing-workflow)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/workflow-automation/#get-an-existing-workflow-v2)


GET https://api.ap1.datadoghq.com/api/v2/workflows/{workflow_id}https://api.ap2.datadoghq.com/api/v2/workflows/{workflow_id}https://api.datadoghq.eu/api/v2/workflows/{workflow_id}https://api.ddog-gov.com/api/v2/workflows/{workflow_id}https://api.datadoghq.com/api/v2/workflows/{workflow_id}https://api.us3.datadoghq.com/api/v2/workflows/{workflow_id}https://api.us5.datadoghq.com/api/v2/workflows/{workflow_id}
### Overview
Get a workflow by ID. This API requires a [registered application key](https://docs.datadoghq.com/api/latest/action-connection/#register-a-new-app-key). Alternatively, you can configure these permissions [in the UI](https://docs.datadoghq.com/account_management/api-app-keys/#actions-api-access). This endpoint requires the `workflows_read` permission.
### Arguments
#### Path Parameters
Name
Type
Description
workflow_id [_required_]
string
The ID of the workflow.
### Response
  * [200](https://docs.datadoghq.com/api/latest/workflow-automation/#GetWorkflow-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/workflow-automation/#GetWorkflow-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/workflow-automation/#GetWorkflow-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/workflow-automation/#GetWorkflow-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/workflow-automation/#GetWorkflow-429-v2)


Successfully got a workflow.
  * [Model](https://docs.datadoghq.com/api/latest/workflow-automation/)
  * [Example](https://docs.datadoghq.com/api/latest/workflow-automation/)


The response object after getting a workflow.
Field
Type
Description
data
object
Data related to the workflow.
attributes [_required_]
object
The definition of `WorkflowDataAttributes` object.
createdAt
date-time
When the workflow was created.
description
string
Description of the workflow.
name [_required_]
string
Name of the workflow.
published
boolean
Set the workflow to published or unpublished. Workflows in an unpublished state will only be executable via manual runs. Automatic triggers such as Schedule will not execute the workflow until it is published.
spec [_required_]
object
The spec defines what the workflow does.
annotations
[object]
A list of annotations used in the workflow. These are like sticky notes for your workflow!
display [_required_]
object
The definition of `AnnotationDisplay` object.
bounds
object
The definition of `AnnotationDisplayBounds` object.
height
double
The `bounds` `height`.
width
double
The `bounds` `width`.
x
double
The `bounds` `x`.
y
double
The `bounds` `y`.
id [_required_]
string
The `Annotation` `id`.
markdownTextAnnotation [_required_]
object
The definition of `AnnotationMarkdownTextAnnotation` object.
text
string
The `markdownTextAnnotation` `text`.
connectionEnvs
[object]
A list of connections or connection groups used in the workflow.
connectionGroups
[object]
The `ConnectionEnv` `connectionGroups`.
connectionGroupId [_required_]
string
The `ConnectionGroup` `connectionGroupId`.
label [_required_]
string
The `ConnectionGroup` `label`.
tags [_required_]
[string]
The `ConnectionGroup` `tags`.
connections
[object]
The `ConnectionEnv` `connections`.
connectionId [_required_]
string
The `Connection` `connectionId`.
label [_required_]
string
The `Connection` `label`.
env [_required_]
enum
The definition of `ConnectionEnvEnv` object. Allowed enum values: `default`
handle
string
Unique identifier used to trigger workflows automatically in Datadog.
inputSchema
object
A list of input parameters for the workflow. These can be used as dynamic runtime values in your workflow.
parameters
[object]
The `InputSchema` `parameters`.
defaultValue
The `InputSchemaParameters` `defaultValue`.
description
string
The `InputSchemaParameters` `description`.
label
string
The `InputSchemaParameters` `label`.
name [_required_]
string
The `InputSchemaParameters` `name`.
type [_required_]
enum
The definition of `InputSchemaParametersType` object. Allowed enum values: `STRING,NUMBER,BOOLEAN,OBJECT,ARRAY_STRING,ARRAY_NUMBER,ARRAY_BOOLEAN,ARRAY_OBJECT`
outputSchema
object
A list of output parameters for the workflow.
parameters
[object]
The `OutputSchema` `parameters`.
defaultValue
The `OutputSchemaParameters` `defaultValue`.
description
string
The `OutputSchemaParameters` `description`.
label
string
The `OutputSchemaParameters` `label`.
name [_required_]
string
The `OutputSchemaParameters` `name`.
type [_required_]
enum
The definition of `OutputSchemaParametersType` object. Allowed enum values: `STRING,NUMBER,BOOLEAN,OBJECT,ARRAY_STRING,ARRAY_NUMBER,ARRAY_BOOLEAN,ARRAY_OBJECT`
value
The `OutputSchemaParameters` `value`.
steps
[object]
A `Step` is a sub-component of a workflow. Each `Step` performs an action.
actionId [_required_]
string
The unique identifier of an action.
completionGate
object
Used to create conditions before running subsequent actions.
completionCondition [_required_]
object
The definition of `CompletionCondition` object.
operand1 [_required_]
The `CompletionCondition` `operand1`.
operand2
The `CompletionCondition` `operand2`.
operator [_required_]
enum
The definition of `CompletionConditionOperator` object. Allowed enum values: `OPERATOR_EQUAL,OPERATOR_NOT_EQUAL,OPERATOR_GREATER_THAN,OPERATOR_LESS_THAN,OPERATOR_GREATER_THAN_OR_EQUAL_TO,OPERATOR_LESS_THAN_OR_EQUAL_TO,OPERATOR_CONTAINS,OPERATOR_DOES_NOT_CONTAIN,OPERATOR_IS_NULL,OPERATOR_IS_NOT_NULL,OPERATOR_IS_EMPTY,OPERATOR_IS_NOT_EMPTY`
retryStrategy [_required_]
object
The definition of `RetryStrategy` object.
kind [_required_]
enum
The definition of `RetryStrategyKind` object. Allowed enum values: `RETRY_STRATEGY_LINEAR`
linear
object
The definition of `RetryStrategyLinear` object.
interval [_required_]
string
The `RetryStrategyLinear` `interval`. The expected format is the number of seconds ending with an s. For example, 1 day is 86400s
maxRetries [_required_]
double
The `RetryStrategyLinear` `maxRetries`.
connectionLabel
string
The unique identifier of a connection defined in the spec.
display
object
The definition of `StepDisplay` object.
bounds
object
The definition of `StepDisplayBounds` object.
x
double
The `bounds` `x`.
y
double
The `bounds` `y`.
errorHandlers
[object]
The `Step` `errorHandlers`.
fallbackStepName [_required_]
string
The `ErrorHandler` `fallbackStepName`.
retryStrategy [_required_]
object
The definition of `RetryStrategy` object.
kind [_required_]
enum
The definition of `RetryStrategyKind` object. Allowed enum values: `RETRY_STRATEGY_LINEAR`
linear
object
The definition of `RetryStrategyLinear` object.
interval [_required_]
string
The `RetryStrategyLinear` `interval`. The expected format is the number of seconds ending with an s. For example, 1 day is 86400s
maxRetries [_required_]
double
The `RetryStrategyLinear` `maxRetries`.
name [_required_]
string
Name of the step.
outboundEdges
[object]
A list of subsequent actions to run.
branchName [_required_]
string
The `OutboundEdge` `branchName`.
nextStepName [_required_]
string
The `OutboundEdge` `nextStepName`.
parameters
[object]
A list of inputs for an action.
name [_required_]
string
The `Parameter` `name`.
value [_required_]
The `Parameter` `value`.
readinessGate
object
Used to merge multiple branches into a single branch.
thresholdType [_required_]
enum
The definition of `ReadinessGateThresholdType` object. Allowed enum values: `ANY,ALL`
triggers
[ <oneOf>]
The list of triggers that activate this workflow. At least one trigger is required, and each trigger type may appear at most once.
Option 1
object
Schema for an API-based trigger.
apiTrigger [_required_]
object
Trigger a workflow from an API request. The workflow must be published.
rateLimit
object
Defines a rate limit for a trigger.
count
int64
The `TriggerRateLimit` `count`.
interval
string
The `TriggerRateLimit` `interval`. The expected format is the number of seconds ending with an s. For example, 1 day is 86400s
startStepNames
[string]
A list of steps that run first after a trigger fires.
Option 2
object
Schema for an App-based trigger.
appTrigger [_required_]
object
Trigger a workflow from an App.
startStepNames
[string]
A list of steps that run first after a trigger fires.
Option 3
object
Schema for a Case-based trigger.
caseTrigger [_required_]
object
Trigger a workflow from a Case. For automatic triggering a handle must be configured and the workflow must be published.
rateLimit
object
Defines a rate limit for a trigger.
count
int64
The `TriggerRateLimit` `count`.
interval
string
The `TriggerRateLimit` `interval`. The expected format is the number of seconds ending with an s. For example, 1 day is 86400s
startStepNames
[string]
A list of steps that run first after a trigger fires.
Option 4
object
Schema for a Change Event-based trigger.
changeEventTrigger [_required_]
object
Trigger a workflow from a Change Event.
startStepNames
[string]
A list of steps that run first after a trigger fires.
Option 5
object
Schema for a Database Monitoring-based trigger.
databaseMonitoringTrigger [_required_]
object
Trigger a workflow from Database Monitoring.
startStepNames
[string]
A list of steps that run first after a trigger fires.
Option 6
object
Schema for a Datastore-based trigger.
datastoreTrigger [_required_]
object
Trigger a workflow from a Datastore. For automatic triggering a handle must be configured and the workflow must be published.
rateLimit
object
Defines a rate limit for a trigger.
count
int64
The `TriggerRateLimit` `count`.
interval
string
The `TriggerRateLimit` `interval`. The expected format is the number of seconds ending with an s. For example, 1 day is 86400s
startStepNames
[string]
A list of steps that run first after a trigger fires.
Option 7
object
Schema for a Dashboard-based trigger.
dashboardTrigger [_required_]
object
Trigger a workflow from a Dashboard.
startStepNames
[string]
A list of steps that run first after a trigger fires.
Option 8
object
Schema for a GitHub webhook-based trigger.
githubWebhookTrigger [_required_]
object
Trigger a workflow from a GitHub webhook. To trigger a workflow from GitHub, you must set a `webhookSecret`. In your GitHub Webhook Settings, set the Payload URL to "base_url"/api/v2/workflows/"workflow_id"/webhook?orgId="org_id", select application/json for the content type, and be highly recommend enabling SSL verification for security. The workflow must be published.
rateLimit
object
Defines a rate limit for a trigger.
count
int64
The `TriggerRateLimit` `count`.
interval
string
The `TriggerRateLimit` `interval`. The expected format is the number of seconds ending with an s. For example, 1 day is 86400s
startStepNames
[string]
A list of steps that run first after a trigger fires.
Option 9
object
Schema for an Incident-based trigger.
incidentTrigger [_required_]
object
Trigger a workflow from an Incident. For automatic triggering a handle must be configured and the workflow must be published.
rateLimit
object
Defines a rate limit for a trigger.
count
int64
The `TriggerRateLimit` `count`.
interval
string
The `TriggerRateLimit` `interval`. The expected format is the number of seconds ending with an s. For example, 1 day is 86400s
startStepNames
[string]
A list of steps that run first after a trigger fires.
Option 10
object
Schema for a Monitor-based trigger.
monitorTrigger [_required_]
object
Trigger a workflow from a Monitor. For automatic triggering a handle must be configured and the workflow must be published.
rateLimit
object
Defines a rate limit for a trigger.
count
int64
The `TriggerRateLimit` `count`.
interval
string
The `TriggerRateLimit` `interval`. The expected format is the number of seconds ending with an s. For example, 1 day is 86400s
startStepNames
[string]
A list of steps that run first after a trigger fires.
Option 11
object
Schema for a Notebook-based trigger.
notebookTrigger [_required_]
object
Trigger a workflow from a Notebook.
startStepNames
[string]
A list of steps that run first after a trigger fires.
Option 12
object
Schema for a Schedule-based trigger.
scheduleTrigger [_required_]
object
Trigger a workflow from a Schedule. The workflow must be published.
rruleExpression [_required_]
string
Recurrence rule expression for scheduling.
startStepNames
[string]
A list of steps that run first after a trigger fires.
Option 13
object
Schema for a Security-based trigger.
securityTrigger [_required_]
object
Trigger a workflow from a Security Signal or Finding. For automatic triggering a handle must be configured and the workflow must be published.
rateLimit
object
Defines a rate limit for a trigger.
count
int64
The `TriggerRateLimit` `count`.
interval
string
The `TriggerRateLimit` `interval`. The expected format is the number of seconds ending with an s. For example, 1 day is 86400s
startStepNames
[string]
A list of steps that run first after a trigger fires.
Option 14
object
Schema for a Self Service-based trigger.
selfServiceTrigger [_required_]
object
Trigger a workflow from Self Service.
startStepNames
[string]
A list of steps that run first after a trigger fires.
Option 15
object
Schema for a Slack-based trigger.
slackTrigger [_required_]
object
Trigger a workflow from Slack. The workflow must be published.
startStepNames
[string]
A list of steps that run first after a trigger fires.
Option 16
object
Schema for a Software Catalog-based trigger.
softwareCatalogTrigger [_required_]
object
Trigger a workflow from Software Catalog.
startStepNames
[string]
A list of steps that run first after a trigger fires.
Option 17
object
Schema for a Workflow-based trigger.
startStepNames
[string]
A list of steps that run first after a trigger fires.
workflowTrigger [_required_]
object
Trigger a workflow from the Datadog UI. Only required if no other trigger exists.
tags
[string]
Tags of the workflow.
updatedAt
date-time
When the workflow was last updated.
webhookSecret
string
If a Webhook trigger is defined on this workflow, a webhookSecret is required and should be provided here.
id
string
The workflow identifier
relationships
object
The definition of `WorkflowDataRelationships` object.
creator
object
The definition of `WorkflowUserRelationship` object.
data
object
The definition of `WorkflowUserRelationshipData` object.
id [_required_]
string
The user identifier
type [_required_]
enum
The definition of `WorkflowUserRelationshipType` object. Allowed enum values: `users`
owner
object
The definition of `WorkflowUserRelationship` object.
data
object
The definition of `WorkflowUserRelationshipData` object.
id [_required_]
string
The user identifier
type [_required_]
enum
The definition of `WorkflowUserRelationshipType` object. Allowed enum values: `users`
type [_required_]
enum
The definition of `WorkflowDataType` object. Allowed enum values: `workflows`
```
{
  "data": {
    "attributes": {
      "createdAt": "2019-09-19T10:00:00.000Z",
      "description": "string",
      "name": "",
      "published": false,
      "spec": {
        "annotations": [
          {
            "display": {
              "bounds": {
                "height": "number",
                "width": "number",
                "x": "number",
                "y": "number"
              }
            },
            "id": "",
            "markdownTextAnnotation": {
              "text": "string"
            }
          }
        ],
        "connectionEnvs": [
          {
            "connectionGroups": [
              {
                "connectionGroupId": "",
                "label": "",
                "tags": [
                  ""
                ]
              }
            ],
            "connections": [
              {
                "connectionId": "",
                "label": ""
              }
            ],
            "env": "default"
          }
        ],
        "handle": "string",
        "inputSchema": {
          "parameters": [
            {
              "defaultValue": "undefined",
              "description": "string",
              "label": "string",
              "name": "",
              "type": "STRING"
            }
          ]
        },
        "outputSchema": {
          "parameters": [
            {
              "defaultValue": "undefined",
              "description": "string",
              "label": "string",
              "name": "",
              "type": "STRING",
              "value": "undefined"
            }
          ]
        },
        "steps": [
          {
            "actionId": "",
            "completionGate": {
              "completionCondition": {
                "operand1": "undefined",
                "operand2": "undefined",
                "operator": "OPERATOR_EQUAL"
              },
              "retryStrategy": {
                "kind": "RETRY_STRATEGY_LINEAR",
                "linear": {
                  "interval": "",
                  "maxRetries": 0
                }
              }
            },
            "connectionLabel": "string",
            "display": {
              "bounds": {
                "x": "number",
                "y": "number"
              }
            },
            "errorHandlers": [
              {
                "fallbackStepName": "",
                "retryStrategy": {
                  "kind": "RETRY_STRATEGY_LINEAR",
                  "linear": {
                    "interval": "",
                    "maxRetries": 0
                  }
                }
              }
            ],
            "name": "",
            "outboundEdges": [
              {
                "branchName": "",
                "nextStepName": ""
              }
            ],
            "parameters": [
              {
                "name": "",
                "value": "undefined"
              }
            ],
            "readinessGate": {
              "thresholdType": "ANY"
            }
          }
        ],
        "triggers": [
          {
            "apiTrigger": {
              "rateLimit": {
                "count": "integer",
                "interval": "string"
              }
            },
            "startStepNames": [
              ""
            ]
          }
        ]
      },
      "tags": [],
      "updatedAt": "2019-09-19T10:00:00.000Z",
      "webhookSecret": "string"
    },
    "id": "string",
    "relationships": {
      "creator": {
        "data": {
          "id": "",
          "type": "users"
        }
      },
      "owner": {
        "data": {
          "id": "",
          "type": "users"
        }
      }
    },
    "type": "workflows"
  }
}
```

Copy
Bad request
  * [Model](https://docs.datadoghq.com/api/latest/workflow-automation/)
  * [Example](https://docs.datadoghq.com/api/latest/workflow-automation/)


API error response.
Field
Type
Description
errors [_required_]
[object]
A list of errors.
detail
string
A human-readable explanation specific to this occurrence of the error.
meta
object
Non-standard meta-information about the error
source
object
References to the source of the error.
header
string
A string indicating the name of a single request header which caused the error.
parameter
string
A string indicating which URI query parameter caused the error.
pointer
string
A JSON pointer to the value in the request document that caused the error.
status
string
Status code of the response.
title
string
Short human-readable summary of the error.
```
{
  "errors": [
    {
      "detail": "Missing required attribute in body",
      "meta": {},
      "source": {
        "header": "Authorization",
        "parameter": "limit",
        "pointer": "/data/attributes/title"
      },
      "status": "400",
      "title": "Bad Request"
    }
  ]
}
```

Copy
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/workflow-automation/)
  * [Example](https://docs.datadoghq.com/api/latest/workflow-automation/)


API error response.
Field
Type
Description
errors [_required_]
[object]
A list of errors.
detail
string
A human-readable explanation specific to this occurrence of the error.
meta
object
Non-standard meta-information about the error
source
object
References to the source of the error.
header
string
A string indicating the name of a single request header which caused the error.
parameter
string
A string indicating which URI query parameter caused the error.
pointer
string
A JSON pointer to the value in the request document that caused the error.
status
string
Status code of the response.
title
string
Short human-readable summary of the error.
```
{
  "errors": [
    {
      "detail": "Missing required attribute in body",
      "meta": {},
      "source": {
        "header": "Authorization",
        "parameter": "limit",
        "pointer": "/data/attributes/title"
      },
      "status": "400",
      "title": "Bad Request"
    }
  ]
}
```

Copy
Not found
  * [Model](https://docs.datadoghq.com/api/latest/workflow-automation/)
  * [Example](https://docs.datadoghq.com/api/latest/workflow-automation/)


API error response.
Field
Type
Description
errors [_required_]
[object]
A list of errors.
detail
string
A human-readable explanation specific to this occurrence of the error.
meta
object
Non-standard meta-information about the error
source
object
References to the source of the error.
header
string
A string indicating the name of a single request header which caused the error.
parameter
string
A string indicating which URI query parameter caused the error.
pointer
string
A JSON pointer to the value in the request document that caused the error.
status
string
Status code of the response.
title
string
Short human-readable summary of the error.
```
{
  "errors": [
    {
      "detail": "Missing required attribute in body",
      "meta": {},
      "source": {
        "header": "Authorization",
        "parameter": "limit",
        "pointer": "/data/attributes/title"
      },
      "status": "400",
      "title": "Bad Request"
    }
  ]
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/workflow-automation/)
  * [Example](https://docs.datadoghq.com/api/latest/workflow-automation/)


API error response.
Field
Type
Description
errors [_required_]
[object]
A list of errors.
detail
string
A human-readable explanation specific to this occurrence of the error.
meta
object
Non-standard meta-information about the error
source
object
References to the source of the error.
header
string
A string indicating the name of a single request header which caused the error.
parameter
string
A string indicating which URI query parameter caused the error.
pointer
string
A JSON pointer to the value in the request document that caused the error.
status
string
Status code of the response.
title
string
Short human-readable summary of the error.
```
{
  "errors": [
    {
      "detail": "Missing required attribute in body",
      "meta": {},
      "source": {
        "header": "Authorization",
        "parameter": "limit",
        "pointer": "/data/attributes/title"
      },
      "status": "400",
      "title": "Bad Request"
    }
  ]
}
```

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/workflow-automation/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/workflow-automation/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/workflow-automation/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/workflow-automation/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/workflow-automation/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/workflow-automation/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/workflow-automation/?code-lang=typescript)


#####  Get an existing Workflow
Copy
```
                  # Path parameters  
export workflow_id="CHANGE_ME"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/workflows/${workflow_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get an existing Workflow
```
"""
Get an existing Workflow returns "Successfully got a workflow." response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.workflow_automation_api import WorkflowAutomationApi

# there is a valid "workflow" in the system
WORKFLOW_DATA_ID = environ["WORKFLOW_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = WorkflowAutomationApi(api_client)
    response = api_instance.get_workflow(
        workflow_id=WORKFLOW_DATA_ID,
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Get an existing Workflow
```
# Get an existing Workflow returns "Successfully got a workflow." response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::WorkflowAutomationAPI.new

# there is a valid "workflow" in the system
WORKFLOW_DATA_ID = ENV["WORKFLOW_DATA_ID"]
p api_instance.get_workflow(WORKFLOW_DATA_ID)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Get an existing Workflow
```
// Get an existing Workflow returns "Successfully got a workflow." response

package main

import (
	"context"
	"encoding/json"
	"fmt"
	"os"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
	// there is a valid "workflow" in the system
	WorkflowDataID := os.Getenv("WORKFLOW_DATA_ID")

	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewWorkflowAutomationApi(apiClient)
	resp, r, err := api.GetWorkflow(ctx, WorkflowDataID)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `WorkflowAutomationApi.GetWorkflow`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `WorkflowAutomationApi.GetWorkflow`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Get an existing Workflow
```
// Get an existing Workflow returns "Successfully got a workflow." response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.WorkflowAutomationApi;
import com.datadog.api.client.v2.model.GetWorkflowResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    WorkflowAutomationApi apiInstance = new WorkflowAutomationApi(defaultClient);

    // there is a valid "workflow" in the system
    String WORKFLOW_DATA_ID = System.getenv("WORKFLOW_DATA_ID");

    try {
      GetWorkflowResponse result = apiInstance.getWorkflow(WORKFLOW_DATA_ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkflowAutomationApi#getWorkflow");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"


```

#####  Get an existing Workflow
```
// Get an existing Workflow returns "Successfully got a workflow." response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_workflow_automation::WorkflowAutomationAPI;

#[tokio::main]
async fn main() {
    // there is a valid "workflow" in the system
    let workflow_data_id = std::env::var("WORKFLOW_DATA_ID").unwrap();
    let configuration = datadog::Configuration::new();
    let api = WorkflowAutomationAPI::with_config(configuration);
    let resp = api.get_workflow(workflow_data_id.clone()).await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run


```

#####  Get an existing Workflow
```
/**
 * Get an existing Workflow returns "Successfully got a workflow." response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.WorkflowAutomationApi(configuration);

// there is a valid "workflow" in the system
const WORKFLOW_DATA_ID = process.env.WORKFLOW_DATA_ID as string;

const params: v2.WorkflowAutomationApiGetWorkflowRequest = {
  workflowId: WORKFLOW_DATA_ID,
};

apiInstance
  .getWorkflow(params)
  .then((data: v2.GetWorkflowResponse) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"


```

* * *
## [Create a Workflow](https://docs.datadoghq.com/api/latest/workflow-automation/#create-a-workflow)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/workflow-automation/#create-a-workflow-v2)


POST https://api.ap1.datadoghq.com/api/v2/workflowshttps://api.ap2.datadoghq.com/api/v2/workflowshttps://api.datadoghq.eu/api/v2/workflowshttps://api.ddog-gov.com/api/v2/workflowshttps://api.datadoghq.com/api/v2/workflowshttps://api.us3.datadoghq.com/api/v2/workflowshttps://api.us5.datadoghq.com/api/v2/workflows
### Overview
Create a new workflow, returning the workflow ID. This API requires a [registered application key](https://docs.datadoghq.com/api/latest/action-connection/#register-a-new-app-key). Alternatively, you can configure these permissions [in the UI](https://docs.datadoghq.com/account_management/api-app-keys/#actions-api-access). This endpoint requires the `workflows_write` permission.
### Request
#### Body Data (required)
  * [Model](https://docs.datadoghq.com/api/latest/workflow-automation/)
  * [Example](https://docs.datadoghq.com/api/latest/workflow-automation/)


Field
Type
Description
data [_required_]
object
Data related to the workflow.
attributes [_required_]
object
The definition of `WorkflowDataAttributes` object.
createdAt
date-time
When the workflow was created.
description
string
Description of the workflow.
name [_required_]
string
Name of the workflow.
published
boolean
Set the workflow to published or unpublished. Workflows in an unpublished state will only be executable via manual runs. Automatic triggers such as Schedule will not execute the workflow until it is published.
spec [_required_]
object
The spec defines what the workflow does.
annotations
[object]
A list of annotations used in the workflow. These are like sticky notes for your workflow!
display [_required_]
object
The definition of `AnnotationDisplay` object.
bounds
object
The definition of `AnnotationDisplayBounds` object.
height
double
The `bounds` `height`.
width
double
The `bounds` `width`.
x
double
The `bounds` `x`.
y
double
The `bounds` `y`.
id [_required_]
string
The `Annotation` `id`.
markdownTextAnnotation [_required_]
object
The definition of `AnnotationMarkdownTextAnnotation` object.
text
string
The `markdownTextAnnotation` `text`.
connectionEnvs
[object]
A list of connections or connection groups used in the workflow.
connectionGroups
[object]
The `ConnectionEnv` `connectionGroups`.
connectionGroupId [_required_]
string
The `ConnectionGroup` `connectionGroupId`.
label [_required_]
string
The `ConnectionGroup` `label`.
tags [_required_]
[string]
The `ConnectionGroup` `tags`.
connections
[object]
The `ConnectionEnv` `connections`.
connectionId [_required_]
string
The `Connection` `connectionId`.
label [_required_]
string
The `Connection` `label`.
env [_required_]
enum
The definition of `ConnectionEnvEnv` object. Allowed enum values: `default`
handle
string
Unique identifier used to trigger workflows automatically in Datadog.
inputSchema
object
A list of input parameters for the workflow. These can be used as dynamic runtime values in your workflow.
parameters
[object]
The `InputSchema` `parameters`.
defaultValue
The `InputSchemaParameters` `defaultValue`.
description
string
The `InputSchemaParameters` `description`.
label
string
The `InputSchemaParameters` `label`.
name [_required_]
string
The `InputSchemaParameters` `name`.
type [_required_]
enum
The definition of `InputSchemaParametersType` object. Allowed enum values: `STRING,NUMBER,BOOLEAN,OBJECT,ARRAY_STRING,ARRAY_NUMBER,ARRAY_BOOLEAN,ARRAY_OBJECT`
outputSchema
object
A list of output parameters for the workflow.
parameters
[object]
The `OutputSchema` `parameters`.
defaultValue
The `OutputSchemaParameters` `defaultValue`.
description
string
The `OutputSchemaParameters` `description`.
label
string
The `OutputSchemaParameters` `label`.
name [_required_]
string
The `OutputSchemaParameters` `name`.
type [_required_]
enum
The definition of `OutputSchemaParametersType` object. Allowed enum values: `STRING,NUMBER,BOOLEAN,OBJECT,ARRAY_STRING,ARRAY_NUMBER,ARRAY_BOOLEAN,ARRAY_OBJECT`
value
The `OutputSchemaParameters` `value`.
steps
[object]
A `Step` is a sub-component of a workflow. Each `Step` performs an action.
actionId [_required_]
string
The unique identifier of an action.
completionGate
object
Used to create conditions before running subsequent actions.
completionCondition [_required_]
object
The definition of `CompletionCondition` object.
operand1 [_required_]
The `CompletionCondition` `operand1`.
operand2
The `CompletionCondition` `operand2`.
operator [_required_]
enum
The definition of `CompletionConditionOperator` object. Allowed enum values: `OPERATOR_EQUAL,OPERATOR_NOT_EQUAL,OPERATOR_GREATER_THAN,OPERATOR_LESS_THAN,OPERATOR_GREATER_THAN_OR_EQUAL_TO,OPERATOR_LESS_THAN_OR_EQUAL_TO,OPERATOR_CONTAINS,OPERATOR_DOES_NOT_CONTAIN,OPERATOR_IS_NULL,OPERATOR_IS_NOT_NULL,OPERATOR_IS_EMPTY,OPERATOR_IS_NOT_EMPTY`
retryStrategy [_required_]
object
The definition of `RetryStrategy` object.
kind [_required_]
enum
The definition of `RetryStrategyKind` object. Allowed enum values: `RETRY_STRATEGY_LINEAR`
linear
object
The definition of `RetryStrategyLinear` object.
interval [_required_]
string
The `RetryStrategyLinear` `interval`. The expected format is the number of seconds ending with an s. For example, 1 day is 86400s
maxRetries [_required_]
double
The `RetryStrategyLinear` `maxRetries`.
connectionLabel
string
The unique identifier of a connection defined in the spec.
display
object
The definition of `StepDisplay` object.
bounds
object
The definition of `StepDisplayBounds` object.
x
double
The `bounds` `x`.
y
double
The `bounds` `y`.
errorHandlers
[object]
The `Step` `errorHandlers`.
fallbackStepName [_required_]
string
The `ErrorHandler` `fallbackStepName`.
retryStrategy [_required_]
object
The definition of `RetryStrategy` object.
kind [_required_]
enum
The definition of `RetryStrategyKind` object. Allowed enum values: `RETRY_STRATEGY_LINEAR`
linear
object
The definition of `RetryStrategyLinear` object.
interval [_required_]
string
The `RetryStrategyLinear` `interval`. The expected format is the number of seconds ending with an s. For example, 1 day is 86400s
maxRetries [_required_]
double
The `RetryStrategyLinear` `maxRetries`.
name [_required_]
string
Name of the step.
outboundEdges
[object]
A list of subsequent actions to run.
branchName [_required_]
string
The `OutboundEdge` `branchName`.
nextStepName [_required_]
string
The `OutboundEdge` `nextStepName`.
parameters
[object]
A list of inputs for an action.
name [_required_]
string
The `Parameter` `name`.
value [_required_]
The `Parameter` `value`.
readinessGate
object
Used to merge multiple branches into a single branch.
thresholdType [_required_]
enum
The definition of `ReadinessGateThresholdType` object. Allowed enum values: `ANY,ALL`
triggers
[ <oneOf>]
The list of triggers that activate this workflow. At least one trigger is required, and each trigger type may appear at most once.
Option 1
object
Schema for an API-based trigger.
apiTrigger [_required_]
object
Trigger a workflow from an API request. The workflow must be published.
rateLimit
object
Defines a rate limit for a trigger.
count
int64
The `TriggerRateLimit` `count`.
interval
string
The `TriggerRateLimit` `interval`. The expected format is the number of seconds ending with an s. For example, 1 day is 86400s
startStepNames
[string]
A list of steps that run first after a trigger fires.
Option 2
object
Schema for an App-based trigger.
appTrigger [_required_]
object
Trigger a workflow from an App.
startStepNames
[string]
A list of steps that run first after a trigger fires.
Option 3
object
Schema for a Case-based trigger.
caseTrigger [_required_]
object
Trigger a workflow from a Case. For automatic triggering a handle must be configured and the workflow must be published.
rateLimit
object
Defines a rate limit for a trigger.
count
int64
The `TriggerRateLimit` `count`.
interval
string
The `TriggerRateLimit` `interval`. The expected format is the number of seconds ending with an s. For example, 1 day is 86400s
startStepNames
[string]
A list of steps that run first after a trigger fires.
Option 4
object
Schema for a Change Event-based trigger.
changeEventTrigger [_required_]
object
Trigger a workflow from a Change Event.
startStepNames
[string]
A list of steps that run first after a trigger fires.
Option 5
object
Schema for a Database Monitoring-based trigger.
databaseMonitoringTrigger [_required_]
object
Trigger a workflow from Database Monitoring.
startStepNames
[string]
A list of steps that run first after a trigger fires.
Option 6
object
Schema for a Datastore-based trigger.
datastoreTrigger [_required_]
object
Trigger a workflow from a Datastore. For automatic triggering a handle must be configured and the workflow must be published.
rateLimit
object
Defines a rate limit for a trigger.
count
int64
The `TriggerRateLimit` `count`.
interval
string
The `TriggerRateLimit` `interval`. The expected format is the number of seconds ending with an s. For example, 1 day is 86400s
startStepNames
[string]
A list of steps that run first after a trigger fires.
Option 7
object
Schema for a Dashboard-based trigger.
dashboardTrigger [_required_]
object
Trigger a workflow from a Dashboard.
startStepNames
[string]
A list of steps that run first after a trigger fires.
Option 8
object
Schema for a GitHub webhook-based trigger.
githubWebhookTrigger [_required_]
object
Trigger a workflow from a GitHub webhook. To trigger a workflow from GitHub, you must set a `webhookSecret`. In your GitHub Webhook Settings, set the Payload URL to "base_url"/api/v2/workflows/"workflow_id"/webhook?orgId="org_id", select application/json for the content type, and be highly recommend enabling SSL verification for security. The workflow must be published.
rateLimit
object
Defines a rate limit for a trigger.
count
int64
The `TriggerRateLimit` `count`.
interval
string
The `TriggerRateLimit` `interval`. The expected format is the number of seconds ending with an s. For example, 1 day is 86400s
startStepNames
[string]
A list of steps that run first after a trigger fires.
Option 9
object
Schema for an Incident-based trigger.
incidentTrigger [_required_]
object
Trigger a workflow from an Incident. For automatic triggering a handle must be configured and the workflow must be published.
rateLimit
object
Defines a rate limit for a trigger.
count
int64
The `TriggerRateLimit` `count`.
interval
string
The `TriggerRateLimit` `interval`. The expected format is the number of seconds ending with an s. For example, 1 day is 86400s
startStepNames
[string]
A list of steps that run first after a trigger fires.
Option 10
object
Schema for a Monitor-based trigger.
monitorTrigger [_required_]
object
Trigger a workflow from a Monitor. For automatic triggering a handle must be configured and the workflow must be published.
rateLimit
object
Defines a rate limit for a trigger.
count
int64
The `TriggerRateLimit` `count`.
interval
string
The `TriggerRateLimit` `interval`. The expected format is the number of seconds ending with an s. For example, 1 day is 86400s
startStepNames
[string]
A list of steps that run first after a trigger fires.
Option 11
object
Schema for a Notebook-based trigger.
notebookTrigger [_required_]
object
Trigger a workflow from a Notebook.
startStepNames
[string]
A list of steps that run first after a trigger fires.
Option 12
object
Schema for a Schedule-based trigger.
scheduleTrigger [_required_]
object
Trigger a workflow from a Schedule. The workflow must be published.
rruleExpression [_required_]
string
Recurrence rule expression for scheduling.
startStepNames
[string]
A list of steps that run first after a trigger fires.
Option 13
object
Schema for a Security-based trigger.
securityTrigger [_required_]
object
Trigger a workflow from a Security Signal or Finding. For automatic triggering a handle must be configured and the workflow must be published.
rateLimit
object
Defines a rate limit for a trigger.
count
int64
The `TriggerRateLimit` `count`.
interval
string
The `TriggerRateLimit` `interval`. The expected format is the number of seconds ending with an s. For example, 1 day is 86400s
startStepNames
[string]
A list of steps that run first after a trigger fires.
Option 14
object
Schema for a Self Service-based trigger.
selfServiceTrigger [_required_]
object
Trigger a workflow from Self Service.
startStepNames
[string]
A list of steps that run first after a trigger fires.
Option 15
object
Schema for a Slack-based trigger.
slackTrigger [_required_]
object
Trigger a workflow from Slack. The workflow must be published.
startStepNames
[string]
A list of steps that run first after a trigger fires.
Option 16
object
Schema for a Software Catalog-based trigger.
softwareCatalogTrigger [_required_]
object
Trigger a workflow from Software Catalog.
startStepNames
[string]
A list of steps that run first after a trigger fires.
Option 17
object
Schema for a Workflow-based trigger.
startStepNames
[string]
A list of steps that run first after a trigger fires.
workflowTrigger [_required_]
object
Trigger a workflow from the Datadog UI. Only required if no other trigger exists.
tags
[string]
Tags of the workflow.
updatedAt
date-time
When the workflow was last updated.
webhookSecret
string
If a Webhook trigger is defined on this workflow, a webhookSecret is required and should be provided here.
id
string
The workflow identifier
relationships
object
The definition of `WorkflowDataRelationships` object.
creator
object
The definition of `WorkflowUserRelationship` object.
data
object
The definition of `WorkflowUserRelationshipData` object.
id [_required_]
string
The user identifier
type [_required_]
enum
The definition of `WorkflowUserRelationshipType` object. Allowed enum values: `users`
owner
object
The definition of `WorkflowUserRelationship` object.
data
object
The definition of `WorkflowUserRelationshipData` object.
id [_required_]
string
The user identifier
type [_required_]
enum
The definition of `WorkflowUserRelationshipType` object. Allowed enum values: `users`
type [_required_]
enum
The definition of `WorkflowDataType` object. Allowed enum values: `workflows`
```
{
  "data": {
    "attributes": {
      "description": "A sample workflow.",
      "name": "Example Workflow",
      "published": true,
      "spec": {
        "connectionEnvs": [
          {
            "connections": [
              {
                "connectionId": "11111111-1111-1111-1111-111111111111",
                "label": "INTEGRATION_DATADOG"
              }
            ],
            "env": "default"
          }
        ],
        "inputSchema": {
          "parameters": [
            {
              "defaultValue": "default",
              "name": "input",
              "type": "STRING"
            }
          ]
        },
        "outputSchema": {
          "parameters": [
            {
              "name": "output",
              "type": "ARRAY_OBJECT",
              "value": "outputValue"
            }
          ]
        },
        "steps": [
          {
            "actionId": "com.datadoghq.dd.monitor.listMonitors",
            "connectionLabel": "INTEGRATION_DATADOG",
            "name": "Step1",
            "outboundEdges": [
              {
                "branchName": "main",
                "nextStepName": "Step2"
              }
            ],
            "parameters": [
              {
                "name": "tags",
                "value": "service:monitoring"
              }
            ]
          },
          {
            "actionId": "com.datadoghq.core.noop",
            "name": "Step2"
          }
        ],
        "triggers": [
          {
            "monitorTrigger": {
              "rateLimit": {
                "count": 1,
                "interval": "3600s"
              }
            },
            "startStepNames": [
              "Step1"
            ]
          },
          {
            "startStepNames": [
              "Step1"
            ],
            "githubWebhookTrigger": {}
          }
        ]
      },
      "tags": [
        "team:infra",
        "service:monitoring",
        "foo:bar"
      ]
    },
    "type": "workflows"
  }
}
```

Copy
### Response
  * [201](https://docs.datadoghq.com/api/latest/workflow-automation/#CreateWorkflow-201-v2)
  * [400](https://docs.datadoghq.com/api/latest/workflow-automation/#CreateWorkflow-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/workflow-automation/#CreateWorkflow-403-v2)
  * [429](https://docs.datadoghq.com/api/latest/workflow-automation/#CreateWorkflow-429-v2)


Successfully created a workflow.
  * [Model](https://docs.datadoghq.com/api/latest/workflow-automation/)
  * [Example](https://docs.datadoghq.com/api/latest/workflow-automation/)


The response object after creating a new workflow.
Field
Type
Description
data [_required_]
object
Data related to the workflow.
attributes [_required_]
object
The definition of `WorkflowDataAttributes` object.
createdAt
date-time
When the workflow was created.
description
string
Description of the workflow.
name [_required_]
string
Name of the workflow.
published
boolean
Set the workflow to published or unpublished. Workflows in an unpublished state will only be executable via manual runs. Automatic triggers such as Schedule will not execute the workflow until it is published.
spec [_required_]
object
The spec defines what the workflow does.
annotations
[object]
A list of annotations used in the workflow. These are like sticky notes for your workflow!
display [_required_]
object
The definition of `AnnotationDisplay` object.
bounds
object
The definition of `AnnotationDisplayBounds` object.
height
double
The `bounds` `height`.
width
double
The `bounds` `width`.
x
double
The `bounds` `x`.
y
double
The `bounds` `y`.
id [_required_]
string
The `Annotation` `id`.
markdownTextAnnotation [_required_]
object
The definition of `AnnotationMarkdownTextAnnotation` object.
text
string
The `markdownTextAnnotation` `text`.
connectionEnvs
[object]
A list of connections or connection groups used in the workflow.
connectionGroups
[object]
The `ConnectionEnv` `connectionGroups`.
connectionGroupId [_required_]
string
The `ConnectionGroup` `connectionGroupId`.
label [_required_]
string
The `ConnectionGroup` `label`.
tags [_required_]
[string]
The `ConnectionGroup` `tags`.
connections
[object]
The `ConnectionEnv` `connections`.
connectionId [_required_]
string
The `Connection` `connectionId`.
label [_required_]
string
The `Connection` `label`.
env [_required_]
enum
The definition of `ConnectionEnvEnv` object. Allowed enum values: `default`
handle
string
Unique identifier used to trigger workflows automatically in Datadog.
inputSchema
object
A list of input parameters for the workflow. These can be used as dynamic runtime values in your workflow.
parameters
[object]
The `InputSchema` `parameters`.
defaultValue
The `InputSchemaParameters` `defaultValue`.
description
string
The `InputSchemaParameters` `description`.
label
string
The `InputSchemaParameters` `label`.
name [_required_]
string
The `InputSchemaParameters` `name`.
type [_required_]
enum
The definition of `InputSchemaParametersType` object. Allowed enum values: `STRING,NUMBER,BOOLEAN,OBJECT,ARRAY_STRING,ARRAY_NUMBER,ARRAY_BOOLEAN,ARRAY_OBJECT`
outputSchema
object
A list of output parameters for the workflow.
parameters
[object]
The `OutputSchema` `parameters`.
defaultValue
The `OutputSchemaParameters` `defaultValue`.
description
string
The `OutputSchemaParameters` `description`.
label
string
The `OutputSchemaParameters` `label`.
name [_required_]
string
The `OutputSchemaParameters` `name`.
type [_required_]
enum
The definition of `OutputSchemaParametersType` object. Allowed enum values: `STRING,NUMBER,BOOLEAN,OBJECT,ARRAY_STRING,ARRAY_NUMBER,ARRAY_BOOLEAN,ARRAY_OBJECT`
value
The `OutputSchemaParameters` `value`.
steps
[object]
A `Step` is a sub-component of a workflow. Each `Step` performs an action.
actionId [_required_]
string
The unique identifier of an action.
completionGate
object
Used to create conditions before running subsequent actions.
completionCondition [_required_]
object
The definition of `CompletionCondition` object.
operand1 [_required_]
The `CompletionCondition` `operand1`.
operand2
The `CompletionCondition` `operand2`.
operator [_required_]
enum
The definition of `CompletionConditionOperator` object. Allowed enum values: `OPERATOR_EQUAL,OPERATOR_NOT_EQUAL,OPERATOR_GREATER_THAN,OPERATOR_LESS_THAN,OPERATOR_GREATER_THAN_OR_EQUAL_TO,OPERATOR_LESS_THAN_OR_EQUAL_TO,OPERATOR_CONTAINS,OPERATOR_DOES_NOT_CONTAIN,OPERATOR_IS_NULL,OPERATOR_IS_NOT_NULL,OPERATOR_IS_EMPTY,OPERATOR_IS_NOT_EMPTY`
retryStrategy [_required_]
object
The definition of `RetryStrategy` object.
kind [_required_]
enum
The definition of `RetryStrategyKind` object. Allowed enum values: `RETRY_STRATEGY_LINEAR`
linear
object
The definition of `RetryStrategyLinear` object.
interval [_required_]
string
The `RetryStrategyLinear` `interval`. The expected format is the number of seconds ending with an s. For example, 1 day is 86400s
maxRetries [_required_]
double
The `RetryStrategyLinear` `maxRetries`.
connectionLabel
string
The unique identifier of a connection defined in the spec.
display
object
The definition of `StepDisplay` object.
bounds
object
The definition of `StepDisplayBounds` object.
x
double
The `bounds` `x`.
y
double
The `bounds` `y`.
errorHandlers
[object]
The `Step` `errorHandlers`.
fallbackStepName [_required_]
string
The `ErrorHandler` `fallbackStepName`.
retryStrategy [_required_]
object
The definition of `RetryStrategy` object.
kind [_required_]
enum
The definition of `RetryStrategyKind` object. Allowed enum values: `RETRY_STRATEGY_LINEAR`
linear
object
The definition of `RetryStrategyLinear` object.
interval [_required_]
string
The `RetryStrategyLinear` `interval`. The expected format is the number of seconds ending with an s. For example, 1 day is 86400s
maxRetries [_required_]
double
The `RetryStrategyLinear` `maxRetries`.
name [_required_]
string
Name of the step.
outboundEdges
[object]
A list of subsequent actions to run.
branchName [_required_]
string
The `OutboundEdge` `branchName`.
nextStepName [_required_]
string
The `OutboundEdge` `nextStepName`.
parameters
[object]
A list of inputs for an action.
name [_required_]
string
The `Parameter` `name`.
value [_required_]
The `Parameter` `value`.
readinessGate
object
Used to merge multiple branches into a single branch.
thresholdType [_required_]
enum
The definition of `ReadinessGateThresholdType` object. Allowed enum values: `ANY,ALL`
triggers
[ <oneOf>]
The list of triggers that activate this workflow. At least one trigger is required, and each trigger type may appear at most once.
Option 1
object
Schema for an API-based trigger.
apiTrigger [_required_]
object
Trigger a workflow from an API request. The workflow must be published.
rateLimit
object
Defines a rate limit for a trigger.
count
int64
The `TriggerRateLimit` `count`.
interval
string
The `TriggerRateLimit` `interval`. The expected format is the number of seconds ending with an s. For example, 1 day is 86400s
startStepNames
[string]
A list of steps that run first after a trigger fires.
Option 2
object
Schema for an App-based trigger.
appTrigger [_required_]
object
Trigger a workflow from an App.
startStepNames
[string]
A list of steps that run first after a trigger fires.
Option 3
object
Schema for a Case-based trigger.
caseTrigger [_required_]
object
Trigger a workflow from a Case. For automatic triggering a handle must be configured and the workflow must be published.
rateLimit
object
Defines a rate limit for a trigger.
count
int64
The `TriggerRateLimit` `count`.
interval
string
The `TriggerRateLimit` `interval`. The expected format is the number of seconds ending with an s. For example, 1 day is 86400s
startStepNames
[string]
A list of steps that run first after a trigger fires.
Option 4
object
Schema for a Change Event-based trigger.
changeEventTrigger [_required_]
object
Trigger a workflow from a Change Event.
startStepNames
[string]
A list of steps that run first after a trigger fires.
Option 5
object
Schema for a Database Monitoring-based trigger.
databaseMonitoringTrigger [_required_]
object
Trigger a workflow from Database Monitoring.
startStepNames
[string]
A list of steps that run first after a trigger fires.
Option 6
object
Schema for a Datastore-based trigger.
datastoreTrigger [_required_]
object
Trigger a workflow from a Datastore. For automatic triggering a handle must be configured and the workflow must be published.
rateLimit
object
Defines a rate limit for a trigger.
count
int64
The `TriggerRateLimit` `count`.
interval
string
The `TriggerRateLimit` `interval`. The expected format is the number of seconds ending with an s. For example, 1 day is 86400s
startStepNames
[string]
A list of steps that run first after a trigger fires.
Option 7
object
Schema for a Dashboard-based trigger.
dashboardTrigger [_required_]
object
Trigger a workflow from a Dashboard.
startStepNames
[string]
A list of steps that run first after a trigger fires.
Option 8
object
Schema for a GitHub webhook-based trigger.
githubWebhookTrigger [_required_]
object
Trigger a workflow from a GitHub webhook. To trigger a workflow from GitHub, you must set a `webhookSecret`. In your GitHub Webhook Settings, set the Payload URL to "base_url"/api/v2/workflows/"workflow_id"/webhook?orgId="org_id", select application/json for the content type, and be highly recommend enabling SSL verification for security. The workflow must be published.
rateLimit
object
Defines a rate limit for a trigger.
count
int64
The `TriggerRateLimit` `count`.
interval
string
The `TriggerRateLimit` `interval`. The expected format is the number of seconds ending with an s. For example, 1 day is 86400s
startStepNames
[string]
A list of steps that run first after a trigger fires.
Option 9
object
Schema for an Incident-based trigger.
incidentTrigger [_required_]
object
Trigger a workflow from an Incident. For automatic triggering a handle must be configured and the workflow must be published.
rateLimit
object
Defines a rate limit for a trigger.
count
int64
The `TriggerRateLimit` `count`.
interval
string
The `TriggerRateLimit` `interval`. The expected format is the number of seconds ending with an s. For example, 1 day is 86400s
startStepNames
[string]
A list of steps that run first after a trigger fires.
Option 10
object
Schema for a Monitor-based trigger.
monitorTrigger [_required_]
object
Trigger a workflow from a Monitor. For automatic triggering a handle must be configured and the workflow must be published.
rateLimit
object
Defines a rate limit for a trigger.
count
int64
The `TriggerRateLimit` `count`.
interval
string
The `TriggerRateLimit` `interval`. The expected format is the number of seconds ending with an s. For example, 1 day is 86400s
startStepNames
[string]
A list of steps that run first after a trigger fires.
Option 11
object
Schema for a Notebook-based trigger.
notebookTrigger [_required_]
object
Trigger a workflow from a Notebook.
startStepNames
[string]
A list of steps that run first after a trigger fires.
Option 12
object
Schema for a Schedule-based trigger.
scheduleTrigger [_required_]
object
Trigger a workflow from a Schedule. The workflow must be published.
rruleExpression [_required_]
string
Recurrence rule expression for scheduling.
startStepNames
[string]
A list of steps that run first after a trigger fires.
Option 13
object
Schema for a Security-based trigger.
securityTrigger [_required_]
object
Trigger a workflow from a Security Signal or Finding. For automatic triggering a handle must be configured and the workflow must be published.
rateLimit
object
Defines a rate limit for a trigger.
count
int64
The `TriggerRateLimit` `count`.
interval
string
The `TriggerRateLimit` `interval`. The expected format is the number of seconds ending with an s. For example, 1 day is 86400s
startStepNames
[string]
A list of steps that run first after a trigger fires.
Option 14
object
Schema for a Self Service-based trigger.
selfServiceTrigger [_required_]
object
Trigger a workflow from Self Service.
startStepNames
[string]
A list of steps that run first after a trigger fires.
Option 15
object
Schema for a Slack-based trigger.
slackTrigger [_required_]
object
Trigger a workflow from Slack. The workflow must be published.
startStepNames
[string]
A list of steps that run first after a trigger fires.
Option 16
object
Schema for a Software Catalog-based trigger.
softwareCatalogTrigger [_required_]
object
Trigger a workflow from Software Catalog.
startStepNames
[string]
A list of steps that run first after a trigger fires.
Option 17
object
Schema for a Workflow-based trigger.
startStepNames
[string]
A list of steps that run first after a trigger fires.
workflowTrigger [_required_]
object
Trigger a workflow from the Datadog UI. Only required if no other trigger exists.
tags
[string]
Tags of the workflow.
updatedAt
date-time
When the workflow was last updated.
webhookSecret
string
If a Webhook trigger is defined on this workflow, a webhookSecret is required and should be provided here.
id
string
The workflow identifier
relationships
object
The definition of `WorkflowDataRelationships` object.
creator
object
The definition of `WorkflowUserRelationship` object.
data
object
The definition of `WorkflowUserRelationshipData` object.
id [_required_]
string
The user identifier
type [_required_]
enum
The definition of `WorkflowUserRelationshipType` object. Allowed enum values: `users`
owner
object
The definition of `WorkflowUserRelationship` object.
data
object
The definition of `WorkflowUserRelationshipData` object.
id [_required_]
string
The user identifier
type [_required_]
enum
The definition of `WorkflowUserRelationshipType` object. Allowed enum values: `users`
type [_required_]
enum
The definition of `WorkflowDataType` object. Allowed enum values: `workflows`
```
{
  "data": {
    "attributes": {
      "createdAt": "2019-09-19T10:00:00.000Z",
      "description": "string",
      "name": "",
      "published": false,
      "spec": {
        "annotations": [
          {
            "display": {
              "bounds": {
                "height": "number",
                "width": "number",
                "x": "number",
                "y": "number"
              }
            },
            "id": "",
            "markdownTextAnnotation": {
              "text": "string"
            }
          }
        ],
        "connectionEnvs": [
          {
            "connectionGroups": [
              {
                "connectionGroupId": "",
                "label": "",
                "tags": [
                  ""
                ]
              }
            ],
            "connections": [
              {
                "connectionId": "",
                "label": ""
              }
            ],
            "env": "default"
          }
        ],
        "handle": "string",
        "inputSchema": {
          "parameters": [
            {
              "defaultValue": "undefined",
              "description": "string",
              "label": "string",
              "name": "",
              "type": "STRING"
            }
          ]
        },
        "outputSchema": {
          "parameters": [
            {
              "defaultValue": "undefined",
              "description": "string",
              "label": "string",
              "name": "",
              "type": "STRING",
              "value": "undefined"
            }
          ]
        },
        "steps": [
          {
            "actionId": "",
            "completionGate": {
              "completionCondition": {
                "operand1": "undefined",
                "operand2": "undefined",
                "operator": "OPERATOR_EQUAL"
              },
              "retryStrategy": {
                "kind": "RETRY_STRATEGY_LINEAR",
                "linear": {
                  "interval": "",
                  "maxRetries": 0
                }
              }
            },
            "connectionLabel": "string",
            "display": {
              "bounds": {
                "x": "number",
                "y": "number"
              }
            },
            "errorHandlers": [
              {
                "fallbackStepName": "",
                "retryStrategy": {
                  "kind": "RETRY_STRATEGY_LINEAR",
                  "linear": {
                    "interval": "",
                    "maxRetries": 0
                  }
                }
              }
            ],
            "name": "",
            "outboundEdges": [
              {
                "branchName": "",
                "nextStepName": ""
              }
            ],
            "parameters": [
              {
                "name": "",
                "value": "undefined"
              }
            ],
            "readinessGate": {
              "thresholdType": "ANY"
            }
          }
        ],
        "triggers": [
          {
            "apiTrigger": {
              "rateLimit": {
                "count": "integer",
                "interval": "string"
              }
            },
            "startStepNames": [
              ""
            ]
          }
        ]
      },
      "tags": [],
      "updatedAt": "2019-09-19T10:00:00.000Z",
      "webhookSecret": "string"
    },
    "id": "string",
    "relationships": {
      "creator": {
        "data": {
          "id": "",
          "type": "users"
        }
      },
      "owner": {
        "data": {
          "id": "",
          "type": "users"
        }
      }
    },
    "type": "workflows"
  }
}
```

Copy
Bad request
  * [Model](https://docs.datadoghq.com/api/latest/workflow-automation/)
  * [Example](https://docs.datadoghq.com/api/latest/workflow-automation/)


API error response.
Field
Type
Description
errors [_required_]
[object]
A list of errors.
detail
string
A human-readable explanation specific to this occurrence of the error.
meta
object
Non-standard meta-information about the error
source
object
References to the source of the error.
header
string
A string indicating the name of a single request header which caused the error.
parameter
string
A string indicating which URI query parameter caused the error.
pointer
string
A JSON pointer to the value in the request document that caused the error.
status
string
Status code of the response.
title
string
Short human-readable summary of the error.
```
{
  "errors": [
    {
      "detail": "Missing required attribute in body",
      "meta": {},
      "source": {
        "header": "Authorization",
        "parameter": "limit",
        "pointer": "/data/attributes/title"
      },
      "status": "400",
      "title": "Bad Request"
    }
  ]
}
```

Copy
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/workflow-automation/)
  * [Example](https://docs.datadoghq.com/api/latest/workflow-automation/)


API error response.
Field
Type
Description
errors [_required_]
[object]
A list of errors.
detail
string
A human-readable explanation specific to this occurrence of the error.
meta
object
Non-standard meta-information about the error
source
object
References to the source of the error.
header
string
A string indicating the name of a single request header which caused the error.
parameter
string
A string indicating which URI query parameter caused the error.
pointer
string
A JSON pointer to the value in the request document that caused the error.
status
string
Status code of the response.
title
string
Short human-readable summary of the error.
```
{
  "errors": [
    {
      "detail": "Missing required attribute in body",
      "meta": {},
      "source": {
        "header": "Authorization",
        "parameter": "limit",
        "pointer": "/data/attributes/title"
      },
      "status": "400",
      "title": "Bad Request"
    }
  ]
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/workflow-automation/)
  * [Example](https://docs.datadoghq.com/api/latest/workflow-automation/)


API error response.
Field
Type
Description
errors [_required_]
[object]
A list of errors.
detail
string
A human-readable explanation specific to this occurrence of the error.
meta
object
Non-standard meta-information about the error
source
object
References to the source of the error.
header
string
A string indicating the name of a single request header which caused the error.
parameter
string
A string indicating which URI query parameter caused the error.
pointer
string
A JSON pointer to the value in the request document that caused the error.
status
string
Status code of the response.
title
string
Short human-readable summary of the error.
```
{
  "errors": [
    {
      "detail": "Missing required attribute in body",
      "meta": {},
      "source": {
        "header": "Authorization",
        "parameter": "limit",
        "pointer": "/data/attributes/title"
      },
      "status": "400",
      "title": "Bad Request"
    }
  ]
}
```

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/workflow-automation/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/workflow-automation/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/workflow-automation/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/workflow-automation/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/workflow-automation/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/workflow-automation/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/workflow-automation/?code-lang=typescript)


#####  Create a Workflow returns "Successfully created a workflow." response
Copy
```
                          # Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/workflows" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "description": "A sample workflow.",
      "name": "Example Workflow",
      "published": true,
      "spec": {
        "connectionEnvs": [
          {
            "connections": [
              {
                "connectionId": "11111111-1111-1111-1111-111111111111",
                "label": "INTEGRATION_DATADOG"
              }
            ],
            "env": "default"
          }
        ],
        "inputSchema": {
          "parameters": [
            {
              "defaultValue": "default",
              "name": "input",
              "type": "STRING"
            }
          ]
        },
        "outputSchema": {
          "parameters": [
            {
              "name": "output",
              "type": "ARRAY_OBJECT",
              "value": "outputValue"
            }
          ]
        },
        "steps": [
          {
            "actionId": "com.datadoghq.dd.monitor.listMonitors",
            "connectionLabel": "INTEGRATION_DATADOG",
            "name": "Step1",
            "outboundEdges": [
              {
                "branchName": "main",
                "nextStepName": "Step2"
              }
            ],
            "parameters": [
              {
                "name": "tags",
                "value": "service:monitoring"
              }
            ]
          },
          {
            "actionId": "com.datadoghq.core.noop",
            "name": "Step2"
          }
        ],
        "triggers": [
          {
            "monitorTrigger": {
              "rateLimit": {
                "count": 1,
                "interval": "3600s"
              }
            },
            "startStepNames": [
              "Step1"
            ]
          },
          {
            "startStepNames": [
              "Step1"
            ],
            "githubWebhookTrigger": {}
          }
        ]
      },
      "tags": [
        "team:infra",
        "service:monitoring",
        "foo:bar"
      ]
    },
    "type": "workflows"
  }
}
EOF  

                        
```

#####  Create a Workflow returns "Successfully created a workflow." response
```
// Create a Workflow returns "Successfully created a workflow." response

package main

import (
	"context"
	"encoding/json"
	"fmt"
	"os"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
	body := datadogV2.CreateWorkflowRequest{
		Data: datadogV2.WorkflowData{
			Attributes: datadogV2.WorkflowDataAttributes{
				Description: datadog.PtrString("A sample workflow."),
				Name:        "Example Workflow",
				Published:   datadog.PtrBool(true),
				Spec: datadogV2.Spec{
					ConnectionEnvs: []datadogV2.ConnectionEnv{
						{
							Connections: []datadogV2.Connection{
								{
									ConnectionId: "11111111-1111-1111-1111-111111111111",
									Label:        "INTEGRATION_DATADOG",
								},
							},
							Env: datadogV2.CONNECTIONENVENV_DEFAULT,
						},
					},
					InputSchema: &datadogV2.InputSchema{
						Parameters: []datadogV2.InputSchemaParameters{
							{
								DefaultValue: "default",
								Name:         "input",
								Type:         datadogV2.INPUTSCHEMAPARAMETERSTYPE_STRING,
							},
						},
					},
					OutputSchema: &datadogV2.OutputSchema{
						Parameters: []datadogV2.OutputSchemaParameters{
							{
								Name:  "output",
								Type:  datadogV2.OUTPUTSCHEMAPARAMETERSTYPE_ARRAY_OBJECT,
								Value: "outputValue",
							},
						},
					},
					Steps: []datadogV2.Step{
						{
							ActionId:        "com.datadoghq.dd.monitor.listMonitors",
							ConnectionLabel: datadog.PtrString("INTEGRATION_DATADOG"),
							Name:            "Step1",
							OutboundEdges: []datadogV2.OutboundEdge{
								{
									BranchName:   "main",
									NextStepName: "Step2",
								},
							},
							Parameters: []datadogV2.Parameter{
								{
									Name:  "tags",
									Value: "service:monitoring",
								},
							},
						},
						{
							ActionId: "com.datadoghq.core.noop",
							Name:     "Step2",
						},
					},
					Triggers: []datadogV2.Trigger{
						datadogV2.Trigger{
							MonitorTriggerWrapper: &datadogV2.MonitorTriggerWrapper{
								MonitorTrigger: datadogV2.MonitorTrigger{
									RateLimit: &datadogV2.TriggerRateLimit{
										Count:    datadog.PtrInt64(1),
										Interval: datadog.PtrString("3600s"),
									},
								},
								StartStepNames: []string{
									"Step1",
								},
							}},
						datadogV2.Trigger{
							GithubWebhookTriggerWrapper: &datadogV2.GithubWebhookTriggerWrapper{
								StartStepNames: []string{
									"Step1",
								},
								GithubWebhookTrigger: datadogV2.GithubWebhookTrigger{},
							}},
					},
				},
				Tags: []string{
					"team:infra",
					"service:monitoring",
					"foo:bar",
				},
			},
			Type: datadogV2.WORKFLOWDATATYPE_WORKFLOWS,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewWorkflowAutomationApi(apiClient)
	resp, r, err := api.CreateWorkflow(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `WorkflowAutomationApi.CreateWorkflow`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `WorkflowAutomationApi.CreateWorkflow`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Create a Workflow returns "Successfully created a workflow." response
```
// Create a Workflow returns "Successfully created a workflow." response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.WorkflowAutomationApi;
import com.datadog.api.client.v2.model.Connection;
import com.datadog.api.client.v2.model.ConnectionEnv;
import com.datadog.api.client.v2.model.ConnectionEnvEnv;
import com.datadog.api.client.v2.model.CreateWorkflowRequest;
import com.datadog.api.client.v2.model.CreateWorkflowResponse;
import com.datadog.api.client.v2.model.GithubWebhookTrigger;
import com.datadog.api.client.v2.model.GithubWebhookTriggerWrapper;
import com.datadog.api.client.v2.model.InputSchema;
import com.datadog.api.client.v2.model.InputSchemaParameters;
import com.datadog.api.client.v2.model.InputSchemaParametersType;
import com.datadog.api.client.v2.model.MonitorTrigger;
import com.datadog.api.client.v2.model.MonitorTriggerWrapper;
import com.datadog.api.client.v2.model.OutboundEdge;
import com.datadog.api.client.v2.model.OutputSchema;
import com.datadog.api.client.v2.model.OutputSchemaParameters;
import com.datadog.api.client.v2.model.OutputSchemaParametersType;
import com.datadog.api.client.v2.model.Parameter;
import com.datadog.api.client.v2.model.Spec;
import com.datadog.api.client.v2.model.Step;
import com.datadog.api.client.v2.model.Trigger;
import com.datadog.api.client.v2.model.TriggerRateLimit;
import com.datadog.api.client.v2.model.WorkflowData;
import com.datadog.api.client.v2.model.WorkflowDataAttributes;
import com.datadog.api.client.v2.model.WorkflowDataType;
import java.util.Arrays;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    WorkflowAutomationApi apiInstance = new WorkflowAutomationApi(defaultClient);

    CreateWorkflowRequest body =
        new CreateWorkflowRequest()
            .data(
                new WorkflowData()
                    .attributes(
                        new WorkflowDataAttributes()
                            .description("A sample workflow.")
                            .name("Example Workflow")
                            .published(true)
                            .spec(
                                new Spec()
                                    .connectionEnvs(
                                        Collections.singletonList(
                                            new ConnectionEnv()
                                                .connections(
                                                    Collections.singletonList(
                                                        new Connection()
                                                            .connectionId(
                                                                "11111111-1111-1111-1111-111111111111")
                                                            .label("INTEGRATION_DATADOG")))
                                                .env(ConnectionEnvEnv.DEFAULT)))
                                    .inputSchema(
                                        new InputSchema()
                                            .parameters(
                                                Collections.singletonList(
                                                    new InputSchemaParameters()
                                                        .defaultValue("default")
                                                        .name("input")
                                                        .type(InputSchemaParametersType.STRING))))
                                    .outputSchema(
                                        new OutputSchema()
                                            .parameters(
                                                Collections.singletonList(
                                                    new OutputSchemaParameters()
                                                        .name("output")
                                                        .type(
                                                            OutputSchemaParametersType.ARRAY_OBJECT)
                                                        .value("outputValue"))))
                                    .steps(
                                        Arrays.asList(
                                            new Step()
                                                .actionId("com.datadoghq.dd.monitor.listMonitors")
                                                .connectionLabel("INTEGRATION_DATADOG")
                                                .name("Step1")
                                                .outboundEdges(
                                                    Collections.singletonList(
                                                        new OutboundEdge()
                                                            .branchName("main")
                                                            .nextStepName("Step2")))
                                                .parameters(
                                                    Collections.singletonList(
                                                        new Parameter()
                                                            .name("tags")
                                                            .value("service:monitoring"))),
                                            new Step()
                                                .actionId("com.datadoghq.core.noop")
                                                .name("Step2")))
                                    .triggers(
                                        Arrays.asList(
                                            new Trigger(
                                                new MonitorTriggerWrapper()
                                                    .monitorTrigger(
                                                        new MonitorTrigger()
                                                            .rateLimit(
                                                                new TriggerRateLimit()
                                                                    .count(1L)
                                                                    .interval("3600s")))
                                                    .startStepNames(
                                                        Collections.singletonList("Step1"))),
                                            new Trigger(
                                                new GithubWebhookTriggerWrapper()
                                                    .startStepNames(
                                                        Collections.singletonList("Step1"))
                                                    .githubWebhookTrigger(
                                                        new GithubWebhookTrigger())))))
                            .tags(Arrays.asList("team:infra", "service:monitoring", "foo:bar")))
                    .type(WorkflowDataType.WORKFLOWS));

    try {
      CreateWorkflowResponse result = apiInstance.createWorkflow(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkflowAutomationApi#createWorkflow");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"


```

#####  Create a Workflow returns "Successfully created a workflow." response
```
"""
Create a Workflow returns "Successfully created a workflow." response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.workflow_automation_api import WorkflowAutomationApi
from datadog_api_client.v2.model.connection import Connection
from datadog_api_client.v2.model.connection_env import ConnectionEnv
from datadog_api_client.v2.model.connection_env_env import ConnectionEnvEnv
from datadog_api_client.v2.model.create_workflow_request import CreateWorkflowRequest
from datadog_api_client.v2.model.github_webhook_trigger import GithubWebhookTrigger
from datadog_api_client.v2.model.github_webhook_trigger_wrapper import GithubWebhookTriggerWrapper
from datadog_api_client.v2.model.input_schema import InputSchema
from datadog_api_client.v2.model.input_schema_parameters import InputSchemaParameters
from datadog_api_client.v2.model.input_schema_parameters_type import InputSchemaParametersType
from datadog_api_client.v2.model.monitor_trigger import MonitorTrigger
from datadog_api_client.v2.model.monitor_trigger_wrapper import MonitorTriggerWrapper
from datadog_api_client.v2.model.outbound_edge import OutboundEdge
from datadog_api_client.v2.model.output_schema import OutputSchema
from datadog_api_client.v2.model.output_schema_parameters import OutputSchemaParameters
from datadog_api_client.v2.model.output_schema_parameters_type import OutputSchemaParametersType
from datadog_api_client.v2.model.parameter import Parameter
from datadog_api_client.v2.model.spec import Spec
from datadog_api_client.v2.model.step import Step
from datadog_api_client.v2.model.trigger_rate_limit import TriggerRateLimit
from datadog_api_client.v2.model.workflow_data import WorkflowData
from datadog_api_client.v2.model.workflow_data_attributes import WorkflowDataAttributes
from datadog_api_client.v2.model.workflow_data_type import WorkflowDataType

body = CreateWorkflowRequest(
    data=WorkflowData(
        attributes=WorkflowDataAttributes(
            description="A sample workflow.",
            name="Example Workflow",
            published=True,
            spec=Spec(
                connection_envs=[
                    ConnectionEnv(
                        connections=[
                            Connection(
                                connection_id="11111111-1111-1111-1111-111111111111",
                                label="INTEGRATION_DATADOG",
                            ),
                        ],
                        env=ConnectionEnvEnv.DEFAULT,
                    ),
                ],
                input_schema=InputSchema(
                    parameters=[
                        InputSchemaParameters(
                            default_value="default",
                            name="input",
                            type=InputSchemaParametersType.STRING,
                        ),
                    ],
                ),
                output_schema=OutputSchema(
                    parameters=[
                        OutputSchemaParameters(
                            name="output",
                            type=OutputSchemaParametersType.ARRAY_OBJECT,
                            value="outputValue",
                        ),
                    ],
                ),
                steps=[
                    Step(
                        action_id="com.datadoghq.dd.monitor.listMonitors",
                        connection_label="INTEGRATION_DATADOG",
                        name="Step1",
                        outbound_edges=[
                            OutboundEdge(
                                branch_name="main",
                                next_step_name="Step2",
                            ),
                        ],
                        parameters=[
                            Parameter(
                                name="tags",
                                value="service:monitoring",
                            ),
                        ],
                    ),
                    Step(
                        action_id="com.datadoghq.core.noop",
                        name="Step2",
                    ),
                ],
                triggers=[
                    MonitorTriggerWrapper(
                        monitor_trigger=MonitorTrigger(
                            rate_limit=TriggerRateLimit(
                                count=1,
                                interval="3600s",
                            ),
                        ),
                        start_step_names=[
                            "Step1",
                        ],
                    ),
                    GithubWebhookTriggerWrapper(
                        start_step_names=[
                            "Step1",
                        ],
                        github_webhook_trigger=GithubWebhookTrigger(),
                    ),
                ],
            ),
            tags=[
                "team:infra",
                "service:monitoring",
                "foo:bar",
            ],
        ),
        type=WorkflowDataType.WORKFLOWS,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = WorkflowAutomationApi(api_client)
    response = api_instance.create_workflow(body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Create a Workflow returns "Successfully created a workflow." response
```
# Create a Workflow returns "Successfully created a workflow." response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::WorkflowAutomationAPI.new

body = DatadogAPIClient::V2::CreateWorkflowRequest.new({
  data: DatadogAPIClient::V2::WorkflowData.new({
    attributes: DatadogAPIClient::V2::WorkflowDataAttributes.new({
      description: "A sample workflow.",
      name: "Example Workflow",
      published: true,
      spec: DatadogAPIClient::V2::Spec.new({
        connection_envs: [
          DatadogAPIClient::V2::ConnectionEnv.new({
            connections: [
              DatadogAPIClient::V2::Connection.new({
                connection_id: "11111111-1111-1111-1111-111111111111",
                label: "INTEGRATION_DATADOG",
              }),
            ],
            env: DatadogAPIClient::V2::ConnectionEnvEnv::DEFAULT,
          }),
        ],
        input_schema: DatadogAPIClient::V2::InputSchema.new({
          parameters: [
            DatadogAPIClient::V2::InputSchemaParameters.new({
              default_value: "default",
              name: "input",
              type: DatadogAPIClient::V2::InputSchemaParametersType::STRING,
            }),
          ],
        }),
        output_schema: DatadogAPIClient::V2::OutputSchema.new({
          parameters: [
            DatadogAPIClient::V2::OutputSchemaParameters.new({
              name: "output",
              type: DatadogAPIClient::V2::OutputSchemaParametersType::ARRAY_OBJECT,
              value: "outputValue",
            }),
          ],
        }),
        steps: [
          DatadogAPIClient::V2::Step.new({
            action_id: "com.datadoghq.dd.monitor.listMonitors",
            connection_label: "INTEGRATION_DATADOG",
            name: "Step1",
            outbound_edges: [
              DatadogAPIClient::V2::OutboundEdge.new({
                branch_name: "main",
                next_step_name: "Step2",
              }),
            ],
            parameters: [
              DatadogAPIClient::V2::Parameter.new({
                name: "tags",
                value: "service:monitoring",
              }),
            ],
          }),
          DatadogAPIClient::V2::Step.new({
            action_id: "com.datadoghq.core.noop",
            name: "Step2",
          }),
        ],
        triggers: [
          DatadogAPIClient::V2::MonitorTriggerWrapper.new({
            monitor_trigger: DatadogAPIClient::V2::MonitorTrigger.new({
              rate_limit: DatadogAPIClient::V2::TriggerRateLimit.new({
                count: 1,
                interval: "3600s",
              }),
            }),
            start_step_names: [
              "Step1",
            ],
          }),
          DatadogAPIClient::V2::GithubWebhookTriggerWrapper.new({
            start_step_names: [
              "Step1",
            ],
            github_webhook_trigger: DatadogAPIClient::V2::GithubWebhookTrigger.new({}),
          }),
        ],
      }),
      tags: [
        "team:infra",
        "service:monitoring",
        "foo:bar",
      ],
    }),
    type: DatadogAPIClient::V2::WorkflowDataType::WORKFLOWS,
  }),
})
p api_instance.create_workflow(body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Create a Workflow returns "Successfully created a workflow." response
```
// Create a Workflow returns "Successfully created a workflow." response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_workflow_automation::WorkflowAutomationAPI;
use datadog_api_client::datadogV2::model::Connection;
use datadog_api_client::datadogV2::model::ConnectionEnv;
use datadog_api_client::datadogV2::model::ConnectionEnvEnv;
use datadog_api_client::datadogV2::model::CreateWorkflowRequest;
use datadog_api_client::datadogV2::model::GithubWebhookTrigger;
use datadog_api_client::datadogV2::model::GithubWebhookTriggerWrapper;
use datadog_api_client::datadogV2::model::InputSchema;
use datadog_api_client::datadogV2::model::InputSchemaParameters;
use datadog_api_client::datadogV2::model::InputSchemaParametersType;
use datadog_api_client::datadogV2::model::MonitorTrigger;
use datadog_api_client::datadogV2::model::MonitorTriggerWrapper;
use datadog_api_client::datadogV2::model::OutboundEdge;
use datadog_api_client::datadogV2::model::OutputSchema;
use datadog_api_client::datadogV2::model::OutputSchemaParameters;
use datadog_api_client::datadogV2::model::OutputSchemaParametersType;
use datadog_api_client::datadogV2::model::Parameter;
use datadog_api_client::datadogV2::model::Spec;
use datadog_api_client::datadogV2::model::Step;
use datadog_api_client::datadogV2::model::Trigger;
use datadog_api_client::datadogV2::model::TriggerRateLimit;
use datadog_api_client::datadogV2::model::WorkflowData;
use datadog_api_client::datadogV2::model::WorkflowDataAttributes;
use datadog_api_client::datadogV2::model::WorkflowDataType;
use serde_json::Value;

#[tokio::main]
async fn main() {
    let body = CreateWorkflowRequest::new(WorkflowData::new(
        WorkflowDataAttributes::new(
            "Example Workflow".to_string(),
            Spec::new()
                .connection_envs(vec![ConnectionEnv::new(ConnectionEnvEnv::DEFAULT)
                    .connections(vec![Connection::new(
                        "11111111-1111-1111-1111-111111111111".to_string(),
                        "INTEGRATION_DATADOG".to_string(),
                    )])])
                .input_schema(InputSchema::new().parameters(vec![
                                    InputSchemaParameters::new(
                                        "input".to_string(),
                                        InputSchemaParametersType::STRING,
                                    ).default_value(Value::from("default"))
                                ]))
                .output_schema(OutputSchema::new().parameters(vec![
                                    OutputSchemaParameters::new(
                                        "output".to_string(),
                                        OutputSchemaParametersType::ARRAY_OBJECT,
                                    ).value(Value::from("outputValue"))
                                ]))
                .steps(vec![
                    Step::new(
                        "com.datadoghq.dd.monitor.listMonitors".to_string(),
                        "Step1".to_string(),
                    )
                    .connection_label("INTEGRATION_DATADOG".to_string())
                    .outbound_edges(vec![OutboundEdge::new(
                        "main".to_string(),
                        "Step2".to_string(),
                    )])
                    .parameters(vec![Parameter::new(
                        "tags".to_string(),
                        Value::from("service:monitoring"),
                    )]),
                    Step::new("com.datadoghq.core.noop".to_string(), "Step2".to_string()),
                ])
                .triggers(vec![
                    Trigger::MonitorTriggerWrapper(Box::new(
                        MonitorTriggerWrapper::new(
                            MonitorTrigger::new().rate_limit(
                                TriggerRateLimit::new()
                                    .count(1)
                                    .interval("3600s".to_string()),
                            ),
                        )
                        .start_step_names(vec!["Step1".to_string()]),
                    )),
                    Trigger::GithubWebhookTriggerWrapper(Box::new(
                        GithubWebhookTriggerWrapper::new(GithubWebhookTrigger::new())
                            .start_step_names(vec!["Step1".to_string()]),
                    )),
                ]),
        )
        .description("A sample workflow.".to_string())
        .published(true)
        .tags(vec![
            "team:infra".to_string(),
            "service:monitoring".to_string(),
            "foo:bar".to_string(),
        ]),
        WorkflowDataType::WORKFLOWS,
    ));
    let configuration = datadog::Configuration::new();
    let api = WorkflowAutomationAPI::with_config(configuration);
    let resp = api.create_workflow(body).await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run


```

#####  Create a Workflow returns "Successfully created a workflow." response
```
/**
 * Create a Workflow returns "Successfully created a workflow." response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.WorkflowAutomationApi(configuration);

const params: v2.WorkflowAutomationApiCreateWorkflowRequest = {
  body: {
    data: {
      attributes: {
        description: "A sample workflow.",
        name: "Example Workflow",
        published: true,
        spec: {
          connectionEnvs: [
            {
              connections: [
                {
                  connectionId: "11111111-1111-1111-1111-111111111111",
                  label: "INTEGRATION_DATADOG",
                },
              ],
              env: "default",
            },
          ],
          inputSchema: {
            parameters: [
              {
                defaultValue: "default",
                name: "input",
                type: "STRING",
              },
            ],
          },
          outputSchema: {
            parameters: [
              {
                name: "output",
                type: "ARRAY_OBJECT",
                value: "outputValue",
              },
            ],
          },
          steps: [
            {
              actionId: "com.datadoghq.dd.monitor.listMonitors",
              connectionLabel: "INTEGRATION_DATADOG",
              name: "Step1",
              outboundEdges: [
                {
                  branchName: "main",
                  nextStepName: "Step2",
                },
              ],
              parameters: [
                {
                  name: "tags",
                  value: "service:monitoring",
                },
              ],
            },
            {
              actionId: "com.datadoghq.core.noop",
              name: "Step2",
            },
          ],
          triggers: [
            {
              monitorTrigger: {
                rateLimit: {
                  count: 1,
                  interval: "3600s",
                },
              },
              startStepNames: ["Step1"],
            },
            {
              startStepNames: ["Step1"],
              githubWebhookTrigger: {},
            },
          ],
        },
        tags: ["team:infra", "service:monitoring", "foo:bar"],
      },
      type: "workflows",
    },
  },
};

apiInstance
  .createWorkflow(params)
  .then((data: v2.CreateWorkflowResponse) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"


```

* * *
## [Update an existing Workflow](https://docs.datadoghq.com/api/latest/workflow-automation/#update-an-existing-workflow)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/workflow-automation/#update-an-existing-workflow-v2)


PATCH https://api.ap1.datadoghq.com/api/v2/workflows/{workflow_id}https://api.ap2.datadoghq.com/api/v2/workflows/{workflow_id}https://api.datadoghq.eu/api/v2/workflows/{workflow_id}https://api.ddog-gov.com/api/v2/workflows/{workflow_id}https://api.datadoghq.com/api/v2/workflows/{workflow_id}https://api.us3.datadoghq.com/api/v2/workflows/{workflow_id}https://api.us5.datadoghq.com/api/v2/workflows/{workflow_id}
### Overview
Update a workflow by ID. This API requires a [registered application key](https://docs.datadoghq.com/api/latest/action-connection/#register-a-new-app-key). Alternatively, you can configure these permissions [in the UI](https://docs.datadoghq.com/account_management/api-app-keys/#actions-api-access). This endpoint requires the `workflows_write` permission.
### Arguments
#### Path Parameters
Name
Type
Description
workflow_id [_required_]
string
The ID of the workflow.
### Request
#### Body Data (required)
  * [Model](https://docs.datadoghq.com/api/latest/workflow-automation/)
  * [Example](https://docs.datadoghq.com/api/latest/workflow-automation/)


Field
Type
Description
data [_required_]
object
Data related to the workflow being updated.
attributes [_required_]
object
The definition of `WorkflowDataUpdateAttributes` object.
createdAt
date-time
When the workflow was created.
description
string
Description of the workflow.
name
string
Name of the workflow.
published
boolean
Set the workflow to published or unpublished. Workflows in an unpublished state will only be executable via manual runs. Automatic triggers such as Schedule will not execute the workflow until it is published.
spec
object
The spec defines what the workflow does.
annotations
[object]
A list of annotations used in the workflow. These are like sticky notes for your workflow!
display [_required_]
object
The definition of `AnnotationDisplay` object.
bounds
object
The definition of `AnnotationDisplayBounds` object.
height
double
The `bounds` `height`.
width
double
The `bounds` `width`.
x
double
The `bounds` `x`.
y
double
The `bounds` `y`.
id [_required_]
string
The `Annotation` `id`.
markdownTextAnnotation [_required_]
object
The definition of `AnnotationMarkdownTextAnnotation` object.
text
string
The `markdownTextAnnotation` `text`.
connectionEnvs
[object]
A list of connections or connection groups used in the workflow.
connectionGroups
[object]
The `ConnectionEnv` `connectionGroups`.
connectionGroupId [_required_]
string
The `ConnectionGroup` `connectionGroupId`.
label [_required_]
string
The `ConnectionGroup` `label`.
tags [_required_]
[string]
The `ConnectionGroup` `tags`.
connections
[object]
The `ConnectionEnv` `connections`.
connectionId [_required_]
string
The `Connection` `connectionId`.
label [_required_]
string
The `Connection` `label`.
env [_required_]
enum
The definition of `ConnectionEnvEnv` object. Allowed enum values: `default`
handle
string
Unique identifier used to trigger workflows automatically in Datadog.
inputSchema
object
A list of input parameters for the workflow. These can be used as dynamic runtime values in your workflow.
parameters
[object]
The `InputSchema` `parameters`.
defaultValue
The `InputSchemaParameters` `defaultValue`.
description
string
The `InputSchemaParameters` `description`.
label
string
The `InputSchemaParameters` `label`.
name [_required_]
string
The `InputSchemaParameters` `name`.
type [_required_]
enum
The definition of `InputSchemaParametersType` object. Allowed enum values: `STRING,NUMBER,BOOLEAN,OBJECT,ARRAY_STRING,ARRAY_NUMBER,ARRAY_BOOLEAN,ARRAY_OBJECT`
outputSchema
object
A list of output parameters for the workflow.
parameters
[object]
The `OutputSchema` `parameters`.
defaultValue
The `OutputSchemaParameters` `defaultValue`.
description
string
The `OutputSchemaParameters` `description`.
label
string
The `OutputSchemaParameters` `label`.
name [_required_]
string
The `OutputSchemaParameters` `name`.
type [_required_]
enum
The definition of `OutputSchemaParametersType` object. Allowed enum values: `STRING,NUMBER,BOOLEAN,OBJECT,ARRAY_STRING,ARRAY_NUMBER,ARRAY_BOOLEAN,ARRAY_OBJECT`
value
The `OutputSchemaParameters` `value`.
steps
[object]
A `Step` is a sub-component of a workflow. Each `Step` performs an action.
actionId [_required_]
string
The unique identifier of an action.
completionGate
object
Used to create conditions before running subsequent actions.
completionCondition [_required_]
object
The definition of `CompletionCondition` object.
operand1 [_required_]
The `CompletionCondition` `operand1`.
operand2
The `CompletionCondition` `operand2`.
operator [_required_]
enum
The definition of `CompletionConditionOperator` object. Allowed enum values: `OPERATOR_EQUAL,OPERATOR_NOT_EQUAL,OPERATOR_GREATER_THAN,OPERATOR_LESS_THAN,OPERATOR_GREATER_THAN_OR_EQUAL_TO,OPERATOR_LESS_THAN_OR_EQUAL_TO,OPERATOR_CONTAINS,OPERATOR_DOES_NOT_CONTAIN,OPERATOR_IS_NULL,OPERATOR_IS_NOT_NULL,OPERATOR_IS_EMPTY,OPERATOR_IS_NOT_EMPTY`
retryStrategy [_required_]
object
The definition of `RetryStrategy` object.
kind [_required_]
enum
The definition of `RetryStrategyKind` object. Allowed enum values: `RETRY_STRATEGY_LINEAR`
linear
object
The definition of `RetryStrategyLinear` object.
interval [_required_]
string
The `RetryStrategyLinear` `interval`. The expected format is the number of seconds ending with an s. For example, 1 day is 86400s
maxRetries [_required_]
double
The `RetryStrategyLinear` `maxRetries`.
connectionLabel
string
The unique identifier of a connection defined in the spec.
display
object
The definition of `StepDisplay` object.
bounds
object
The definition of `StepDisplayBounds` object.
x
double
The `bounds` `x`.
y
double
The `bounds` `y`.
errorHandlers
[object]
The `Step` `errorHandlers`.
fallbackStepName [_required_]
string
The `ErrorHandler` `fallbackStepName`.
retryStrategy [_required_]
object
The definition of `RetryStrategy` object.
kind [_required_]
enum
The definition of `RetryStrategyKind` object. Allowed enum values: `RETRY_STRATEGY_LINEAR`
linear
object
The definition of `RetryStrategyLinear` object.
interval [_required_]
string
The `RetryStrategyLinear` `interval`. The expected format is the number of seconds ending with an s. For example, 1 day is 86400s
maxRetries [_required_]
double
The `RetryStrategyLinear` `maxRetries`.
name [_required_]
string
Name of the step.
outboundEdges
[object]
A list of subsequent actions to run.
branchName [_required_]
string
The `OutboundEdge` `branchName`.
nextStepName [_required_]
string
The `OutboundEdge` `nextStepName`.
parameters
[object]
A list of inputs for an action.
name [_required_]
string
The `Parameter` `name`.
value [_required_]
The `Parameter` `value`.
readinessGate
object
Used to merge multiple branches into a single branch.
thresholdType [_required_]
enum
The definition of `ReadinessGateThresholdType` object. Allowed enum values: `ANY,ALL`
triggers
[ <oneOf>]
The list of triggers that activate this workflow. At least one trigger is required, and each trigger type may appear at most once.
Option 1
object
Schema for an API-based trigger.
apiTrigger [_required_]
object
Trigger a workflow from an API request. The workflow must be published.
rateLimit
object
Defines a rate limit for a trigger.
count
int64
The `TriggerRateLimit` `count`.
interval
string
The `TriggerRateLimit` `interval`. The expected format is the number of seconds ending with an s. For example, 1 day is 86400s
startStepNames
[string]
A list of steps that run first after a trigger fires.
Option 2
object
Schema for an App-based trigger.
appTrigger [_required_]
object
Trigger a workflow from an App.
startStepNames
[string]
A list of steps that run first after a trigger fires.
Option 3
object
Schema for a Case-based trigger.
caseTrigger [_required_]
object
Trigger a workflow from a Case. For automatic triggering a handle must be configured and the workflow must be published.
rateLimit
object
Defines a rate limit for a trigger.
count
int64
The `TriggerRateLimit` `count`.
interval
string
The `TriggerRateLimit` `interval`. The expected format is the number of seconds ending with an s. For example, 1 day is 86400s
startStepNames
[string]
A list of steps that run first after a trigger fires.
Option 4
object
Schema for a Change Event-based trigger.
changeEventTrigger [_required_]
object
Trigger a workflow from a Change Event.
startStepNames
[string]
A list of steps that run first after a trigger fires.
Option 5
object
Schema for a Database Monitoring-based trigger.
databaseMonitoringTrigger [_required_]
object
Trigger a workflow from Database Monitoring.
startStepNames
[string]
A list of steps that run first after a trigger fires.
Option 6
object
Schema for a Datastore-based trigger.
datastoreTrigger [_required_]
object
Trigger a workflow from a Datastore. For automatic triggering a handle must be configured and the workflow must be published.
rateLimit
object
Defines a rate limit for a trigger.
count
int64
The `TriggerRateLimit` `count`.
interval
string
The `TriggerRateLimit` `interval`. The expected format is the number of seconds ending with an s. For example, 1 day is 86400s
startStepNames
[string]
A list of steps that run first after a trigger fires.
Option 7
object
Schema for a Dashboard-based trigger.
dashboardTrigger [_required_]
object
Trigger a workflow from a Dashboard.
startStepNames
[string]
A list of steps that run first after a trigger fires.
Option 8
object
Schema for a GitHub webhook-based trigger.
githubWebhookTrigger [_required_]
object
Trigger a workflow from a GitHub webhook. To trigger a workflow from GitHub, you must set a `webhookSecret`. In your GitHub Webhook Settings, set the Payload URL to "base_url"/api/v2/workflows/"workflow_id"/webhook?orgId="org_id", select application/json for the content type, and be highly recommend enabling SSL verification for security. The workflow must be published.
rateLimit
object
Defines a rate limit for a trigger.
count
int64
The `TriggerRateLimit` `count`.
interval
string
The `TriggerRateLimit` `interval`. The expected format is the number of seconds ending with an s. For example, 1 day is 86400s
startStepNames
[string]
A list of steps that run first after a trigger fires.
Option 9
object
Schema for an Incident-based trigger.
incidentTrigger [_required_]
object
Trigger a workflow from an Incident. For automatic triggering a handle must be configured and the workflow must be published.
rateLimit
object
Defines a rate limit for a trigger.
count
int64
The `TriggerRateLimit` `count`.
interval
string
The `TriggerRateLimit` `interval`. The expected format is the number of seconds ending with an s. For example, 1 day is 86400s
startStepNames
[string]
A list of steps that run first after a trigger fires.
Option 10
object
Schema for a Monitor-based trigger.
monitorTrigger [_required_]
object
Trigger a workflow from a Monitor. For automatic triggering a handle must be configured and the workflow must be published.
rateLimit
object
Defines a rate limit for a trigger.
count
int64
The `TriggerRateLimit` `count`.
interval
string
The `TriggerRateLimit` `interval`. The expected format is the number of seconds ending with an s. For example, 1 day is 86400s
startStepNames
[string]
A list of steps that run first after a trigger fires.
Option 11
object
Schema for a Notebook-based trigger.
notebookTrigger [_required_]
object
Trigger a workflow from a Notebook.
startStepNames
[string]
A list of steps that run first after a trigger fires.
Option 12
object
Schema for a Schedule-based trigger.
scheduleTrigger [_required_]
object
Trigger a workflow from a Schedule. The workflow must be published.
rruleExpression [_required_]
string
Recurrence rule expression for scheduling.
startStepNames
[string]
A list of steps that run first after a trigger fires.
Option 13
object
Schema for a Security-based trigger.
securityTrigger [_required_]
object
Trigger a workflow from a Security Signal or Finding. For automatic triggering a handle must be configured and the workflow must be published.
rateLimit
object
Defines a rate limit for a trigger.
count
int64
The `TriggerRateLimit` `count`.
interval
string
The `TriggerRateLimit` `interval`. The expected format is the number of seconds ending with an s. For example, 1 day is 86400s
startStepNames
[string]
A list of steps that run first after a trigger fires.
Option 14
object
Schema for a Self Service-based trigger.
selfServiceTrigger [_required_]
object
Trigger a workflow from Self Service.
startStepNames
[string]
A list of steps that run first after a trigger fires.
Option 15
object
Schema for a Slack-based trigger.
slackTrigger [_required_]
object
Trigger a workflow from Slack. The workflow must be published.
startStepNames
[string]
A list of steps that run first after a trigger fires.
Option 16
object
Schema for a Software Catalog-based trigger.
softwareCatalogTrigger [_required_]
object
Trigger a workflow from Software Catalog.
startStepNames
[string]
A list of steps that run first after a trigger fires.
Option 17
object
Schema for a Workflow-based trigger.
startStepNames
[string]
A list of steps that run first after a trigger fires.
workflowTrigger [_required_]
object
Trigger a workflow from the Datadog UI. Only required if no other trigger exists.
tags
[string]
Tags of the workflow.
updatedAt
date-time
When the workflow was last updated.
webhookSecret
string
If a Webhook trigger is defined on this workflow, a webhookSecret is required and should be provided here.
id
string
The workflow identifier
relationships
object
The definition of `WorkflowDataRelationships` object.
creator
object
The definition of `WorkflowUserRelationship` object.
data
object
The definition of `WorkflowUserRelationshipData` object.
id [_required_]
string
The user identifier
type [_required_]
enum
The definition of `WorkflowUserRelationshipType` object. Allowed enum values: `users`
owner
object
The definition of `WorkflowUserRelationship` object.
data
object
The definition of `WorkflowUserRelationshipData` object.
id [_required_]
string
The user identifier
type [_required_]
enum
The definition of `WorkflowUserRelationshipType` object. Allowed enum values: `users`
type [_required_]
enum
The definition of `WorkflowDataType` object. Allowed enum values: `workflows`
```
{
  "data": {
    "attributes": {
      "description": "A sample workflow.",
      "name": "Example Workflow",
      "published": true,
      "spec": {
        "connectionEnvs": [
          {
            "connections": [
              {
                "connectionId": "11111111-1111-1111-1111-111111111111",
                "label": "INTEGRATION_DATADOG"
              }
            ],
            "env": "default"
          }
        ],
        "inputSchema": {
          "parameters": [
            {
              "defaultValue": "default",
              "name": "input",
              "type": "STRING"
            }
          ]
        },
        "outputSchema": {
          "parameters": [
            {
              "name": "output",
              "type": "ARRAY_OBJECT",
              "value": "outputValue"
            }
          ]
        },
        "steps": [
          {
            "actionId": "com.datadoghq.dd.monitor.listMonitors",
            "connectionLabel": "INTEGRATION_DATADOG",
            "name": "Step1",
            "outboundEdges": [
              {
                "branchName": "main",
                "nextStepName": "Step2"
              }
            ],
            "parameters": [
              {
                "name": "tags",
                "value": "service:monitoring"
              }
            ]
          },
          {
            "actionId": "com.datadoghq.core.noop",
            "name": "Step2"
          }
        ],
        "triggers": [
          {
            "monitorTrigger": {
              "rateLimit": {
                "count": 1,
                "interval": "3600s"
              }
            },
            "startStepNames": [
              "Step1"
            ]
          },
          {
            "startStepNames": [
              "Step1"
            ],
            "githubWebhookTrigger": {}
          }
        ]
      },
      "tags": [
        "team:infra",
        "service:monitoring",
        "foo:bar"
      ]
    },
    "id": "22222222-2222-2222-2222-222222222222",
    "type": "workflows"
  }
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/workflow-automation/#UpdateWorkflow-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/workflow-automation/#UpdateWorkflow-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/workflow-automation/#UpdateWorkflow-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/workflow-automation/#UpdateWorkflow-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/workflow-automation/#UpdateWorkflow-429-v2)


Successfully updated a workflow.
  * [Model](https://docs.datadoghq.com/api/latest/workflow-automation/)
  * [Example](https://docs.datadoghq.com/api/latest/workflow-automation/)


The response object after updating a workflow.
Field
Type
Description
data
object
Data related to the workflow being updated.
attributes [_required_]
object
The definition of `WorkflowDataUpdateAttributes` object.
createdAt
date-time
When the workflow was created.
description
string
Description of the workflow.
name
string
Name of the workflow.
published
boolean
Set the workflow to published or unpublished. Workflows in an unpublished state will only be executable via manual runs. Automatic triggers such as Schedule will not execute the workflow until it is published.
spec
object
The spec defines what the workflow does.
annotations
[object]
A list of annotations used in the workflow. These are like sticky notes for your workflow!
display [_required_]
object
The definition of `AnnotationDisplay` object.
bounds
object
The definition of `AnnotationDisplayBounds` object.
height
double
The `bounds` `height`.
width
double
The `bounds` `width`.
x
double
The `bounds` `x`.
y
double
The `bounds` `y`.
id [_required_]
string
The `Annotation` `id`.
markdownTextAnnotation [_required_]
object
The definition of `AnnotationMarkdownTextAnnotation` object.
text
string
The `markdownTextAnnotation` `text`.
connectionEnvs
[object]
A list of connections or connection groups used in the workflow.
connectionGroups
[object]
The `ConnectionEnv` `connectionGroups`.
connectionGroupId [_required_]
string
The `ConnectionGroup` `connectionGroupId`.
label [_required_]
string
The `ConnectionGroup` `label`.
tags [_required_]
[string]
The `ConnectionGroup` `tags`.
connections
[object]
The `ConnectionEnv` `connections`.
connectionId [_required_]
string
The `Connection` `connectionId`.
label [_required_]
string
The `Connection` `label`.
env [_required_]
enum
The definition of `ConnectionEnvEnv` object. Allowed enum values: `default`
handle
string
Unique identifier used to trigger workflows automatically in Datadog.
inputSchema
object
A list of input parameters for the workflow. These can be used as dynamic runtime values in your workflow.
parameters
[object]
The `InputSchema` `parameters`.
defaultValue
The `InputSchemaParameters` `defaultValue`.
description
string
The `InputSchemaParameters` `description`.
label
string
The `InputSchemaParameters` `label`.
name [_required_]
string
The `InputSchemaParameters` `name`.
type [_required_]
enum
The definition of `InputSchemaParametersType` object. Allowed enum values: `STRING,NUMBER,BOOLEAN,OBJECT,ARRAY_STRING,ARRAY_NUMBER,ARRAY_BOOLEAN,ARRAY_OBJECT`
outputSchema
object
A list of output parameters for the workflow.
parameters
[object]
The `OutputSchema` `parameters`.
defaultValue
The `OutputSchemaParameters` `defaultValue`.
description
string
The `OutputSchemaParameters` `description`.
label
string
The `OutputSchemaParameters` `label`.
name [_required_]
string
The `OutputSchemaParameters` `name`.
type [_required_]
enum
The definition of `OutputSchemaParametersType` object. Allowed enum values: `STRING,NUMBER,BOOLEAN,OBJECT,ARRAY_STRING,ARRAY_NUMBER,ARRAY_BOOLEAN,ARRAY_OBJECT`
value
The `OutputSchemaParameters` `value`.
steps
[object]
A `Step` is a sub-component of a workflow. Each `Step` performs an action.
actionId [_required_]
string
The unique identifier of an action.
completionGate
object
Used to create conditions before running subsequent actions.
completionCondition [_required_]
object
The definition of `CompletionCondition` object.
operand1 [_required_]
The `CompletionCondition` `operand1`.
operand2
The `CompletionCondition` `operand2`.
operator [_required_]
enum
The definition of `CompletionConditionOperator` object. Allowed enum values: `OPERATOR_EQUAL,OPERATOR_NOT_EQUAL,OPERATOR_GREATER_THAN,OPERATOR_LESS_THAN,OPERATOR_GREATER_THAN_OR_EQUAL_TO,OPERATOR_LESS_THAN_OR_EQUAL_TO,OPERATOR_CONTAINS,OPERATOR_DOES_NOT_CONTAIN,OPERATOR_IS_NULL,OPERATOR_IS_NOT_NULL,OPERATOR_IS_EMPTY,OPERATOR_IS_NOT_EMPTY`
retryStrategy [_required_]
object
The definition of `RetryStrategy` object.
kind [_required_]
enum
The definition of `RetryStrategyKind` object. Allowed enum values: `RETRY_STRATEGY_LINEAR`
linear
object
The definition of `RetryStrategyLinear` object.
interval [_required_]
string
The `RetryStrategyLinear` `interval`. The expected format is the number of seconds ending with an s. For example, 1 day is 86400s
maxRetries [_required_]
double
The `RetryStrategyLinear` `maxRetries`.
connectionLabel
string
The unique identifier of a connection defined in the spec.
display
object
The definition of `StepDisplay` object.
bounds
object
The definition of `StepDisplayBounds` object.
x
double
The `bounds` `x`.
y
double
The `bounds` `y`.
errorHandlers
[object]
The `Step` `errorHandlers`.
fallbackStepName [_required_]
string
The `ErrorHandler` `fallbackStepName`.
retryStrategy [_required_]
object
The definition of `RetryStrategy` object.
kind [_required_]
enum
The definition of `RetryStrategyKind` object. Allowed enum values: `RETRY_STRATEGY_LINEAR`
linear
object
The definition of `RetryStrategyLinear` object.
interval [_required_]
string
The `RetryStrategyLinear` `interval`. The expected format is the number of seconds ending with an s. For example, 1 day is 86400s
maxRetries [_required_]
double
The `RetryStrategyLinear` `maxRetries`.
name [_required_]
string
Name of the step.
outboundEdges
[object]
A list of subsequent actions to run.
branchName [_required_]
string
The `OutboundEdge` `branchName`.
nextStepName [_required_]
string
The `OutboundEdge` `nextStepName`.
parameters
[object]
A list of inputs for an action.
name [_required_]
string
The `Parameter` `name`.
value [_required_]
The `Parameter` `value`.
readinessGate
object
Used to merge multiple branches into a single branch.
thresholdType [_required_]
enum
The definition of `ReadinessGateThresholdType` object. Allowed enum values: `ANY,ALL`
triggers
[ <oneOf>]
The list of triggers that activate this workflow. At least one trigger is required, and each trigger type may appear at most once.
Option 1
object
Schema for an API-based trigger.
apiTrigger [_required_]
object
Trigger a workflow from an API request. The workflow must be published.
rateLimit
object
Defines a rate limit for a trigger.
count
int64
The `TriggerRateLimit` `count`.
interval
string
The `TriggerRateLimit` `interval`. The expected format is the number of seconds ending with an s. For example, 1 day is 86400s
startStepNames
[string]
A list of steps that run first after a trigger fires.
Option 2
object
Schema for an App-based trigger.
appTrigger [_required_]
object
Trigger a workflow from an App.
startStepNames
[string]
A list of steps that run first after a trigger fires.
Option 3
object
Schema for a Case-based trigger.
caseTrigger [_required_]
object
Trigger a workflow from a Case. For automatic triggering a handle must be configured and the workflow must be published.
rateLimit
object
Defines a rate limit for a trigger.
count
int64
The `TriggerRateLimit` `count`.
interval
string
The `TriggerRateLimit` `interval`. The expected format is the number of seconds ending with an s. For example, 1 day is 86400s
startStepNames
[string]
A list of steps that run first after a trigger fires.
Option 4
object
Schema for a Change Event-based trigger.
changeEventTrigger [_required_]
object
Trigger a workflow from a Change Event.
startStepNames
[string]
A list of steps that run first after a trigger fires.
Option 5
object
Schema for a Database Monitoring-based trigger.
databaseMonitoringTrigger [_required_]
object
Trigger a workflow from Database Monitoring.
startStepNames
[string]
A list of steps that run first after a trigger fires.
Option 6
object
Schema for a Datastore-based trigger.
datastoreTrigger [_required_]
object
Trigger a workflow from a Datastore. For automatic triggering a handle must be configured and the workflow must be published.
rateLimit
object
Defines a rate limit for a trigger.
count
int64
The `TriggerRateLimit` `count`.
interval
string
The `TriggerRateLimit` `interval`. The expected format is the number of seconds ending with an s. For example, 1 day is 86400s
startStepNames
[string]
A list of steps that run first after a trigger fires.
Option 7
object
Schema for a Dashboard-based trigger.
dashboardTrigger [_required_]
object
Trigger a workflow from a Dashboard.
startStepNames
[string]
A list of steps that run first after a trigger fires.
Option 8
object
Schema for a GitHub webhook-based trigger.
githubWebhookTrigger [_required_]
object
Trigger a workflow from a GitHub webhook. To trigger a workflow from GitHub, you must set a `webhookSecret`. In your GitHub Webhook Settings, set the Payload URL to "base_url"/api/v2/workflows/"workflow_id"/webhook?orgId="org_id", select application/json for the content type, and be highly recommend enabling SSL verification for security. The workflow must be published.
rateLimit
object
Defines a rate limit for a trigger.
count
int64
The `TriggerRateLimit` `count`.
interval
string
The `TriggerRateLimit` `interval`. The expected format is the number of seconds ending with an s. For example, 1 day is 86400s
startStepNames
[string]
A list of steps that run first after a trigger fires.
Option 9
object
Schema for an Incident-based trigger.
incidentTrigger [_required_]
object
Trigger a workflow from an Incident. For automatic triggering a handle must be configured and the workflow must be published.
rateLimit
object
Defines a rate limit for a trigger.
count
int64
The `TriggerRateLimit` `count`.
interval
string
The `TriggerRateLimit` `interval`. The expected format is the number of seconds ending with an s. For example, 1 day is 86400s
startStepNames
[string]
A list of steps that run first after a trigger fires.
Option 10
object
Schema for a Monitor-based trigger.
monitorTrigger [_required_]
object
Trigger a workflow from a Monitor. For automatic triggering a handle must be configured and the workflow must be published.
rateLimit
object
Defines a rate limit for a trigger.
count
int64
The `TriggerRateLimit` `count`.
interval
string
The `TriggerRateLimit` `interval`. The expected format is the number of seconds ending with an s. For example, 1 day is 86400s
startStepNames
[string]
A list of steps that run first after a trigger fires.
Option 11
object
Schema for a Notebook-based trigger.
notebookTrigger [_required_]
object
Trigger a workflow from a Notebook.
startStepNames
[string]
A list of steps that run first after a trigger fires.
Option 12
object
Schema for a Schedule-based trigger.
scheduleTrigger [_required_]
object
Trigger a workflow from a Schedule. The workflow must be published.
rruleExpression [_required_]
string
Recurrence rule expression for scheduling.
startStepNames
[string]
A list of steps that run first after a trigger fires.
Option 13
object
Schema for a Security-based trigger.
securityTrigger [_required_]
object
Trigger a workflow from a Security Signal or Finding. For automatic triggering a handle must be configured and the workflow must be published.
rateLimit
object
Defines a rate limit for a trigger.
count
int64
The `TriggerRateLimit` `count`.
interval
string
The `TriggerRateLimit` `interval`. The expected format is the number of seconds ending with an s. For example, 1 day is 86400s
startStepNames
[string]
A list of steps that run first after a trigger fires.
Option 14
object
Schema for a Self Service-based trigger.
selfServiceTrigger [_required_]
object
Trigger a workflow from Self Service.
startStepNames
[string]
A list of steps that run first after a trigger fires.
Option 15
object
Schema for a Slack-based trigger.
slackTrigger [_required_]
object
Trigger a workflow from Slack. The workflow must be published.
startStepNames
[string]
A list of steps that run first after a trigger fires.
Option 16
object
Schema for a Software Catalog-based trigger.
softwareCatalogTrigger [_required_]
object
Trigger a workflow from Software Catalog.
startStepNames
[string]
A list of steps that run first after a trigger fires.
Option 17
object
Schema for a Workflow-based trigger.
startStepNames
[string]
A list of steps that run first after a trigger fires.
workflowTrigger [_required_]
object
Trigger a workflow from the Datadog UI. Only required if no other trigger exists.
tags
[string]
Tags of the workflow.
updatedAt
date-time
When the workflow was last updated.
webhookSecret
string
If a Webhook trigger is defined on this workflow, a webhookSecret is required and should be provided here.
id
string
The workflow identifier
relationships
object
The definition of `WorkflowDataRelationships` object.
creator
object
The definition of `WorkflowUserRelationship` object.
data
object
The definition of `WorkflowUserRelationshipData` object.
id [_required_]
string
The user identifier
type [_required_]
enum
The definition of `WorkflowUserRelationshipType` object. Allowed enum values: `users`
owner
object
The definition of `WorkflowUserRelationship` object.
data
object
The definition of `WorkflowUserRelationshipData` object.
id [_required_]
string
The user identifier
type [_required_]
enum
The definition of `WorkflowUserRelationshipType` object. Allowed enum values: `users`
type [_required_]
enum
The definition of `WorkflowDataType` object. Allowed enum values: `workflows`
```
{
  "data": {
    "attributes": {
      "createdAt": "2019-09-19T10:00:00.000Z",
      "description": "string",
      "name": "string",
      "published": false,
      "spec": {
        "annotations": [
          {
            "display": {
              "bounds": {
                "height": "number",
                "width": "number",
                "x": "number",
                "y": "number"
              }
            },
            "id": "",
            "markdownTextAnnotation": {
              "text": "string"
            }
          }
        ],
        "connectionEnvs": [
          {
            "connectionGroups": [
              {
                "connectionGroupId": "",
                "label": "",
                "tags": [
                  ""
                ]
              }
            ],
            "connections": [
              {
                "connectionId": "",
                "label": ""
              }
            ],
            "env": "default"
          }
        ],
        "handle": "string",
        "inputSchema": {
          "parameters": [
            {
              "defaultValue": "undefined",
              "description": "string",
              "label": "string",
              "name": "",
              "type": "STRING"
            }
          ]
        },
        "outputSchema": {
          "parameters": [
            {
              "defaultValue": "undefined",
              "description": "string",
              "label": "string",
              "name": "",
              "type": "STRING",
              "value": "undefined"
            }
          ]
        },
        "steps": [
          {
            "actionId": "",
            "completionGate": {
              "completionCondition": {
                "operand1": "undefined",
                "operand2": "undefined",
                "operator": "OPERATOR_EQUAL"
              },
              "retryStrategy": {
                "kind": "RETRY_STRATEGY_LINEAR",
                "linear": {
                  "interval": "",
                  "maxRetries": 0
                }
              }
            },
            "connectionLabel": "string",
            "display": {
              "bounds": {
                "x": "number",
                "y": "number"
              }
            },
            "errorHandlers": [
              {
                "fallbackStepName": "",
                "retryStrategy": {
                  "kind": "RETRY_STRATEGY_LINEAR",
                  "linear": {
                    "interval": "",
                    "maxRetries": 0
                  }
                }
              }
            ],
            "name": "",
            "outboundEdges": [
              {
                "branchName": "",
                "nextStepName": ""
              }
            ],
            "parameters": [
              {
                "name": "",
                "value": "undefined"
              }
            ],
            "readinessGate": {
              "thresholdType": "ANY"
            }
          }
        ],
        "triggers": [
          {
            "apiTrigger": {
              "rateLimit": {
                "count": "integer",
                "interval": "string"
              }
            },
            "startStepNames": [
              ""
            ]
          }
        ]
      },
      "tags": [],
      "updatedAt": "2019-09-19T10:00:00.000Z",
      "webhookSecret": "string"
    },
    "id": "string",
    "relationships": {
      "creator": {
        "data": {
          "id": "",
          "type": "users"
        }
      },
      "owner": {
        "data": {
          "id": "",
          "type": "users"
        }
      }
    },
    "type": "workflows"
  }
}
```

Copy
Bad request
  * [Model](https://docs.datadoghq.com/api/latest/workflow-automation/)
  * [Example](https://docs.datadoghq.com/api/latest/workflow-automation/)


API error response.
Field
Type
Description
errors [_required_]
[object]
A list of errors.
detail
string
A human-readable explanation specific to this occurrence of the error.
meta
object
Non-standard meta-information about the error
source
object
References to the source of the error.
header
string
A string indicating the name of a single request header which caused the error.
parameter
string
A string indicating which URI query parameter caused the error.
pointer
string
A JSON pointer to the value in the request document that caused the error.
status
string
Status code of the response.
title
string
Short human-readable summary of the error.
```
{
  "errors": [
    {
      "detail": "Missing required attribute in body",
      "meta": {},
      "source": {
        "header": "Authorization",
        "parameter": "limit",
        "pointer": "/data/attributes/title"
      },
      "status": "400",
      "title": "Bad Request"
    }
  ]
}
```

Copy
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/workflow-automation/)
  * [Example](https://docs.datadoghq.com/api/latest/workflow-automation/)


API error response.
Field
Type
Description
errors [_required_]
[object]
A list of errors.
detail
string
A human-readable explanation specific to this occurrence of the error.
meta
object
Non-standard meta-information about the error
source
object
References to the source of the error.
header
string
A string indicating the name of a single request header which caused the error.
parameter
string
A string indicating which URI query parameter caused the error.
pointer
string
A JSON pointer to the value in the request document that caused the error.
status
string
Status code of the response.
title
string
Short human-readable summary of the error.
```
{
  "errors": [
    {
      "detail": "Missing required attribute in body",
      "meta": {},
      "source": {
        "header": "Authorization",
        "parameter": "limit",
        "pointer": "/data/attributes/title"
      },
      "status": "400",
      "title": "Bad Request"
    }
  ]
}
```

Copy
Not found
  * [Model](https://docs.datadoghq.com/api/latest/workflow-automation/)
  * [Example](https://docs.datadoghq.com/api/latest/workflow-automation/)


API error response.
Field
Type
Description
errors [_required_]
[object]
A list of errors.
detail
string
A human-readable explanation specific to this occurrence of the error.
meta
object
Non-standard meta-information about the error
source
object
References to the source of the error.
header
string
A string indicating the name of a single request header which caused the error.
parameter
string
A string indicating which URI query parameter caused the error.
pointer
string
A JSON pointer to the value in the request document that caused the error.
status
string
Status code of the response.
title
string
Short human-readable summary of the error.
```
{
  "errors": [
    {
      "detail": "Missing required attribute in body",
      "meta": {},
      "source": {
        "header": "Authorization",
        "parameter": "limit",
        "pointer": "/data/attributes/title"
      },
      "status": "400",
      "title": "Bad Request"
    }
  ]
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/workflow-automation/)
  * [Example](https://docs.datadoghq.com/api/latest/workflow-automation/)


API error response.
Field
Type
Description
errors [_required_]
[object]
A list of errors.
detail
string
A human-readable explanation specific to this occurrence of the error.
meta
object
Non-standard meta-information about the error
source
object
References to the source of the error.
header
string
A string indicating the name of a single request header which caused the error.
parameter
string
A string indicating which URI query parameter caused the error.
pointer
string
A JSON pointer to the value in the request document that caused the error.
status
string
Status code of the response.
title
string
Short human-readable summary of the error.
```
{
  "errors": [
    {
      "detail": "Missing required attribute in body",
      "meta": {},
      "source": {
        "header": "Authorization",
        "parameter": "limit",
        "pointer": "/data/attributes/title"
      },
      "status": "400",
      "title": "Bad Request"
    }
  ]
}
```

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/workflow-automation/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/workflow-automation/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/workflow-automation/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/workflow-automation/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/workflow-automation/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/workflow-automation/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/workflow-automation/?code-lang=typescript)


#####  Update an existing Workflow returns "Successfully updated a workflow." response
Copy
```
                          # Path parameters  
export workflow_id="CHANGE_ME"  
# Curl command  
curl -X PATCH "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/workflows/${workflow_id}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "description": "A sample workflow.",
      "name": "Example Workflow",
      "published": true,
      "spec": {
        "connectionEnvs": [
          {
            "connections": [
              {
                "connectionId": "11111111-1111-1111-1111-111111111111",
                "label": "INTEGRATION_DATADOG"
              }
            ],
            "env": "default"
          }
        ],
        "inputSchema": {
          "parameters": [
            {
              "defaultValue": "default",
              "name": "input",
              "type": "STRING"
            }
          ]
        },
        "outputSchema": {
          "parameters": [
            {
              "name": "output",
              "type": "ARRAY_OBJECT",
              "value": "outputValue"
            }
          ]
        },
        "steps": [
          {
            "actionId": "com.datadoghq.dd.monitor.listMonitors",
            "connectionLabel": "INTEGRATION_DATADOG",
            "name": "Step1",
            "outboundEdges": [
              {
                "branchName": "main",
                "nextStepName": "Step2"
              }
            ],
            "parameters": [
              {
                "name": "tags",
                "value": "service:monitoring"
              }
            ]
          },
          {
            "actionId": "com.datadoghq.core.noop",
            "name": "Step2"
          }
        ],
        "triggers": [
          {
            "monitorTrigger": {
              "rateLimit": {
                "count": 1,
                "interval": "3600s"
              }
            },
            "startStepNames": [
              "Step1"
            ]
          },
          {
            "startStepNames": [
              "Step1"
            ],
            "githubWebhookTrigger": {}
          }
        ]
      },
      "tags": [
        "team:infra",
        "service:monitoring",
        "foo:bar"
      ]
    },
    "id": "22222222-2222-2222-2222-222222222222",
    "type": "workflows"
  }
}
EOF  

                        
```

#####  Update an existing Workflow returns "Successfully updated a workflow." response
```
// Update an existing Workflow returns "Successfully updated a workflow." response

package main

import (
	"context"
	"encoding/json"
	"fmt"
	"os"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
	// there is a valid "workflow" in the system
	WorkflowDataID := os.Getenv("WORKFLOW_DATA_ID")

	body := datadogV2.UpdateWorkflowRequest{
		Data: datadogV2.WorkflowDataUpdate{
			Attributes: datadogV2.WorkflowDataUpdateAttributes{
				Description: datadog.PtrString("A sample workflow."),
				Name:        datadog.PtrString("Example Workflow"),
				Published:   datadog.PtrBool(true),
				Spec: &datadogV2.Spec{
					ConnectionEnvs: []datadogV2.ConnectionEnv{
						{
							Connections: []datadogV2.Connection{
								{
									ConnectionId: "11111111-1111-1111-1111-111111111111",
									Label:        "INTEGRATION_DATADOG",
								},
							},
							Env: datadogV2.CONNECTIONENVENV_DEFAULT,
						},
					},
					InputSchema: &datadogV2.InputSchema{
						Parameters: []datadogV2.InputSchemaParameters{
							{
								DefaultValue: "default",
								Name:         "input",
								Type:         datadogV2.INPUTSCHEMAPARAMETERSTYPE_STRING,
							},
						},
					},
					OutputSchema: &datadogV2.OutputSchema{
						Parameters: []datadogV2.OutputSchemaParameters{
							{
								Name:  "output",
								Type:  datadogV2.OUTPUTSCHEMAPARAMETERSTYPE_ARRAY_OBJECT,
								Value: "outputValue",
							},
						},
					},
					Steps: []datadogV2.Step{
						{
							ActionId:        "com.datadoghq.dd.monitor.listMonitors",
							ConnectionLabel: datadog.PtrString("INTEGRATION_DATADOG"),
							Name:            "Step1",
							OutboundEdges: []datadogV2.OutboundEdge{
								{
									BranchName:   "main",
									NextStepName: "Step2",
								},
							},
							Parameters: []datadogV2.Parameter{
								{
									Name:  "tags",
									Value: "service:monitoring",
								},
							},
						},
						{
							ActionId: "com.datadoghq.core.noop",
							Name:     "Step2",
						},
					},
					Triggers: []datadogV2.Trigger{
						datadogV2.Trigger{
							MonitorTriggerWrapper: &datadogV2.MonitorTriggerWrapper{
								MonitorTrigger: datadogV2.MonitorTrigger{
									RateLimit: &datadogV2.TriggerRateLimit{
										Count:    datadog.PtrInt64(1),
										Interval: datadog.PtrString("3600s"),
									},
								},
								StartStepNames: []string{
									"Step1",
								},
							}},
						datadogV2.Trigger{
							GithubWebhookTriggerWrapper: &datadogV2.GithubWebhookTriggerWrapper{
								StartStepNames: []string{
									"Step1",
								},
								GithubWebhookTrigger: datadogV2.GithubWebhookTrigger{},
							}},
					},
				},
				Tags: []string{
					"team:infra",
					"service:monitoring",
					"foo:bar",
				},
			},
			Id:   datadog.PtrString("22222222-2222-2222-2222-222222222222"),
			Type: datadogV2.WORKFLOWDATATYPE_WORKFLOWS,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewWorkflowAutomationApi(apiClient)
	resp, r, err := api.UpdateWorkflow(ctx, WorkflowDataID, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `WorkflowAutomationApi.UpdateWorkflow`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `WorkflowAutomationApi.UpdateWorkflow`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Update an existing Workflow returns "Successfully updated a workflow." response
```
// Update an existing Workflow returns "Successfully updated a workflow." response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.WorkflowAutomationApi;
import com.datadog.api.client.v2.model.Connection;
import com.datadog.api.client.v2.model.ConnectionEnv;
import com.datadog.api.client.v2.model.ConnectionEnvEnv;
import com.datadog.api.client.v2.model.GithubWebhookTrigger;
import com.datadog.api.client.v2.model.GithubWebhookTriggerWrapper;
import com.datadog.api.client.v2.model.InputSchema;
import com.datadog.api.client.v2.model.InputSchemaParameters;
import com.datadog.api.client.v2.model.InputSchemaParametersType;
import com.datadog.api.client.v2.model.MonitorTrigger;
import com.datadog.api.client.v2.model.MonitorTriggerWrapper;
import com.datadog.api.client.v2.model.OutboundEdge;
import com.datadog.api.client.v2.model.OutputSchema;
import com.datadog.api.client.v2.model.OutputSchemaParameters;
import com.datadog.api.client.v2.model.OutputSchemaParametersType;
import com.datadog.api.client.v2.model.Parameter;
import com.datadog.api.client.v2.model.Spec;
import com.datadog.api.client.v2.model.Step;
import com.datadog.api.client.v2.model.Trigger;
import com.datadog.api.client.v2.model.TriggerRateLimit;
import com.datadog.api.client.v2.model.UpdateWorkflowRequest;
import com.datadog.api.client.v2.model.UpdateWorkflowResponse;
import com.datadog.api.client.v2.model.WorkflowDataType;
import com.datadog.api.client.v2.model.WorkflowDataUpdate;
import com.datadog.api.client.v2.model.WorkflowDataUpdateAttributes;
import java.util.Arrays;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    WorkflowAutomationApi apiInstance = new WorkflowAutomationApi(defaultClient);

    // there is a valid "workflow" in the system
    String WORKFLOW_DATA_ID = System.getenv("WORKFLOW_DATA_ID");

    UpdateWorkflowRequest body =
        new UpdateWorkflowRequest()
            .data(
                new WorkflowDataUpdate()
                    .attributes(
                        new WorkflowDataUpdateAttributes()
                            .description("A sample workflow.")
                            .name("Example Workflow")
                            .published(true)
                            .spec(
                                new Spec()
                                    .connectionEnvs(
                                        Collections.singletonList(
                                            new ConnectionEnv()
                                                .connections(
                                                    Collections.singletonList(
                                                        new Connection()
                                                            .connectionId(
                                                                "11111111-1111-1111-1111-111111111111")
                                                            .label("INTEGRATION_DATADOG")))
                                                .env(ConnectionEnvEnv.DEFAULT)))
                                    .inputSchema(
                                        new InputSchema()
                                            .parameters(
                                                Collections.singletonList(
                                                    new InputSchemaParameters()
                                                        .defaultValue("default")
                                                        .name("input")
                                                        .type(InputSchemaParametersType.STRING))))
                                    .outputSchema(
                                        new OutputSchema()
                                            .parameters(
                                                Collections.singletonList(
                                                    new OutputSchemaParameters()
                                                        .name("output")
                                                        .type(
                                                            OutputSchemaParametersType.ARRAY_OBJECT)
                                                        .value("outputValue"))))
                                    .steps(
                                        Arrays.asList(
                                            new Step()
                                                .actionId("com.datadoghq.dd.monitor.listMonitors")
                                                .connectionLabel("INTEGRATION_DATADOG")
                                                .name("Step1")
                                                .outboundEdges(
                                                    Collections.singletonList(
                                                        new OutboundEdge()
                                                            .branchName("main")
                                                            .nextStepName("Step2")))
                                                .parameters(
                                                    Collections.singletonList(
                                                        new Parameter()
                                                            .name("tags")
                                                            .value("service:monitoring"))),
                                            new Step()
                                                .actionId("com.datadoghq.core.noop")
                                                .name("Step2")))
                                    .triggers(
                                        Arrays.asList(
                                            new Trigger(
                                                new MonitorTriggerWrapper()
                                                    .monitorTrigger(
                                                        new MonitorTrigger()
                                                            .rateLimit(
                                                                new TriggerRateLimit()
                                                                    .count(1L)
                                                                    .interval("3600s")))
                                                    .startStepNames(
                                                        Collections.singletonList("Step1"))),
                                            new Trigger(
                                                new GithubWebhookTriggerWrapper()
                                                    .startStepNames(
                                                        Collections.singletonList("Step1"))
                                                    .githubWebhookTrigger(
                                                        new GithubWebhookTrigger())))))
                            .tags(Arrays.asList("team:infra", "service:monitoring", "foo:bar")))
                    .id("22222222-2222-2222-2222-222222222222")
                    .type(WorkflowDataType.WORKFLOWS));

    try {
      UpdateWorkflowResponse result = apiInstance.updateWorkflow(WORKFLOW_DATA_ID, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkflowAutomationApi#updateWorkflow");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"


```

#####  Update an existing Workflow returns "Successfully updated a workflow." response
```
"""
Update an existing Workflow returns "Successfully updated a workflow." response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.workflow_automation_api import WorkflowAutomationApi
from datadog_api_client.v2.model.connection import Connection
from datadog_api_client.v2.model.connection_env import ConnectionEnv
from datadog_api_client.v2.model.connection_env_env import ConnectionEnvEnv
from datadog_api_client.v2.model.github_webhook_trigger import GithubWebhookTrigger
from datadog_api_client.v2.model.github_webhook_trigger_wrapper import GithubWebhookTriggerWrapper
from datadog_api_client.v2.model.input_schema import InputSchema
from datadog_api_client.v2.model.input_schema_parameters import InputSchemaParameters
from datadog_api_client.v2.model.input_schema_parameters_type import InputSchemaParametersType
from datadog_api_client.v2.model.monitor_trigger import MonitorTrigger
from datadog_api_client.v2.model.monitor_trigger_wrapper import MonitorTriggerWrapper
from datadog_api_client.v2.model.outbound_edge import OutboundEdge
from datadog_api_client.v2.model.output_schema import OutputSchema
from datadog_api_client.v2.model.output_schema_parameters import OutputSchemaParameters
from datadog_api_client.v2.model.output_schema_parameters_type import OutputSchemaParametersType
from datadog_api_client.v2.model.parameter import Parameter
from datadog_api_client.v2.model.spec import Spec
from datadog_api_client.v2.model.step import Step
from datadog_api_client.v2.model.trigger_rate_limit import TriggerRateLimit
from datadog_api_client.v2.model.update_workflow_request import UpdateWorkflowRequest
from datadog_api_client.v2.model.workflow_data_type import WorkflowDataType
from datadog_api_client.v2.model.workflow_data_update import WorkflowDataUpdate
from datadog_api_client.v2.model.workflow_data_update_attributes import WorkflowDataUpdateAttributes

# there is a valid "workflow" in the system
WORKFLOW_DATA_ID = environ["WORKFLOW_DATA_ID"]

body = UpdateWorkflowRequest(
    data=WorkflowDataUpdate(
        attributes=WorkflowDataUpdateAttributes(
            description="A sample workflow.",
            name="Example Workflow",
            published=True,
            spec=Spec(
                connection_envs=[
                    ConnectionEnv(
                        connections=[
                            Connection(
                                connection_id="11111111-1111-1111-1111-111111111111",
                                label="INTEGRATION_DATADOG",
                            ),
                        ],
                        env=ConnectionEnvEnv.DEFAULT,
                    ),
                ],
                input_schema=InputSchema(
                    parameters=[
                        InputSchemaParameters(
                            default_value="default",
                            name="input",
                            type=InputSchemaParametersType.STRING,
                        ),
                    ],
                ),
                output_schema=OutputSchema(
                    parameters=[
                        OutputSchemaParameters(
                            name="output",
                            type=OutputSchemaParametersType.ARRAY_OBJECT,
                            value="outputValue",
                        ),
                    ],
                ),
                steps=[
                    Step(
                        action_id="com.datadoghq.dd.monitor.listMonitors",
                        connection_label="INTEGRATION_DATADOG",
                        name="Step1",
                        outbound_edges=[
                            OutboundEdge(
                                branch_name="main",
                                next_step_name="Step2",
                            ),
                        ],
                        parameters=[
                            Parameter(
                                name="tags",
                                value="service:monitoring",
                            ),
                        ],
                    ),
                    Step(
                        action_id="com.datadoghq.core.noop",
                        name="Step2",
                    ),
                ],
                triggers=[
                    MonitorTriggerWrapper(
                        monitor_trigger=MonitorTrigger(
                            rate_limit=TriggerRateLimit(
                                count=1,
                                interval="3600s",
                            ),
                        ),
                        start_step_names=[
                            "Step1",
                        ],
                    ),
                    GithubWebhookTriggerWrapper(
                        start_step_names=[
                            "Step1",
                        ],
                        github_webhook_trigger=GithubWebhookTrigger(),
                    ),
                ],
            ),
            tags=[
                "team:infra",
                "service:monitoring",
                "foo:bar",
            ],
        ),
        id="22222222-2222-2222-2222-222222222222",
        type=WorkflowDataType.WORKFLOWS,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = WorkflowAutomationApi(api_client)
    response = api_instance.update_workflow(workflow_id=WORKFLOW_DATA_ID, body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Update an existing Workflow returns "Successfully updated a workflow." response
```
# Update an existing Workflow returns "Successfully updated a workflow." response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::WorkflowAutomationAPI.new

# there is a valid "workflow" in the system
WORKFLOW_DATA_ID = ENV["WORKFLOW_DATA_ID"]

body = DatadogAPIClient::V2::UpdateWorkflowRequest.new({
  data: DatadogAPIClient::V2::WorkflowDataUpdate.new({
    attributes: DatadogAPIClient::V2::WorkflowDataUpdateAttributes.new({
      description: "A sample workflow.",
      name: "Example Workflow",
      published: true,
      spec: DatadogAPIClient::V2::Spec.new({
        connection_envs: [
          DatadogAPIClient::V2::ConnectionEnv.new({
            connections: [
              DatadogAPIClient::V2::Connection.new({
                connection_id: "11111111-1111-1111-1111-111111111111",
                label: "INTEGRATION_DATADOG",
              }),
            ],
            env: DatadogAPIClient::V2::ConnectionEnvEnv::DEFAULT,
          }),
        ],
        input_schema: DatadogAPIClient::V2::InputSchema.new({
          parameters: [
            DatadogAPIClient::V2::InputSchemaParameters.new({
              default_value: "default",
              name: "input",
              type: DatadogAPIClient::V2::InputSchemaParametersType::STRING,
            }),
          ],
        }),
        output_schema: DatadogAPIClient::V2::OutputSchema.new({
          parameters: [
            DatadogAPIClient::V2::OutputSchemaParameters.new({
              name: "output",
              type: DatadogAPIClient::V2::OutputSchemaParametersType::ARRAY_OBJECT,
              value: "outputValue",
            }),
          ],
        }),
        steps: [
          DatadogAPIClient::V2::Step.new({
            action_id: "com.datadoghq.dd.monitor.listMonitors",
            connection_label: "INTEGRATION_DATADOG",
            name: "Step1",
            outbound_edges: [
              DatadogAPIClient::V2::OutboundEdge.new({
                branch_name: "main",
                next_step_name: "Step2",
              }),
            ],
            parameters: [
              DatadogAPIClient::V2::Parameter.new({
                name: "tags",
                value: "service:monitoring",
              }),
            ],
          }),
          DatadogAPIClient::V2::Step.new({
            action_id: "com.datadoghq.core.noop",
            name: "Step2",
          }),
        ],
        triggers: [
          DatadogAPIClient::V2::MonitorTriggerWrapper.new({
            monitor_trigger: DatadogAPIClient::V2::MonitorTrigger.new({
              rate_limit: DatadogAPIClient::V2::TriggerRateLimit.new({
                count: 1,
                interval: "3600s",
              }),
            }),
            start_step_names: [
              "Step1",
            ],
          }),
          DatadogAPIClient::V2::GithubWebhookTriggerWrapper.new({
            start_step_names: [
              "Step1",
            ],
            github_webhook_trigger: DatadogAPIClient::V2::GithubWebhookTrigger.new({}),
          }),
        ],
      }),
      tags: [
        "team:infra",
        "service:monitoring",
        "foo:bar",
      ],
    }),
    id: "22222222-2222-2222-2222-222222222222",
    type: DatadogAPIClient::V2::WorkflowDataType::WORKFLOWS,
  }),
})
p api_instance.update_workflow(WORKFLOW_DATA_ID, body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Update an existing Workflow returns "Successfully updated a workflow." response
```
// Update an existing Workflow returns "Successfully updated a workflow." response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_workflow_automation::WorkflowAutomationAPI;
use datadog_api_client::datadogV2::model::Connection;
use datadog_api_client::datadogV2::model::ConnectionEnv;
use datadog_api_client::datadogV2::model::ConnectionEnvEnv;
use datadog_api_client::datadogV2::model::GithubWebhookTrigger;
use datadog_api_client::datadogV2::model::GithubWebhookTriggerWrapper;
use datadog_api_client::datadogV2::model::InputSchema;
use datadog_api_client::datadogV2::model::InputSchemaParameters;
use datadog_api_client::datadogV2::model::InputSchemaParametersType;
use datadog_api_client::datadogV2::model::MonitorTrigger;
use datadog_api_client::datadogV2::model::MonitorTriggerWrapper;
use datadog_api_client::datadogV2::model::OutboundEdge;
use datadog_api_client::datadogV2::model::OutputSchema;
use datadog_api_client::datadogV2::model::OutputSchemaParameters;
use datadog_api_client::datadogV2::model::OutputSchemaParametersType;
use datadog_api_client::datadogV2::model::Parameter;
use datadog_api_client::datadogV2::model::Spec;
use datadog_api_client::datadogV2::model::Step;
use datadog_api_client::datadogV2::model::Trigger;
use datadog_api_client::datadogV2::model::TriggerRateLimit;
use datadog_api_client::datadogV2::model::UpdateWorkflowRequest;
use datadog_api_client::datadogV2::model::WorkflowDataType;
use datadog_api_client::datadogV2::model::WorkflowDataUpdate;
use datadog_api_client::datadogV2::model::WorkflowDataUpdateAttributes;
use serde_json::Value;

#[tokio::main]
async fn main() {
    // there is a valid "workflow" in the system
    let workflow_data_id = std::env::var("WORKFLOW_DATA_ID").unwrap();
    let body = UpdateWorkflowRequest::new(
        WorkflowDataUpdate::new(
            WorkflowDataUpdateAttributes::new()
                .description("A sample workflow.".to_string())
                .name("Example Workflow".to_string())
                .published(true)
                .spec(
                    Spec::new()
                        .connection_envs(vec![ConnectionEnv::new(ConnectionEnvEnv::DEFAULT)
                            .connections(vec![Connection::new(
                                "11111111-1111-1111-1111-111111111111".to_string(),
                                "INTEGRATION_DATADOG".to_string(),
                            )])])
                        .input_schema(InputSchema::new().parameters(vec![
                                        InputSchemaParameters::new(
                                            "input".to_string(),
                                            InputSchemaParametersType::STRING,
                                        ).default_value(Value::from("default"))
                                    ]))
                        .output_schema(OutputSchema::new().parameters(vec![
                                        OutputSchemaParameters::new(
                                            "output".to_string(),
                                            OutputSchemaParametersType::ARRAY_OBJECT,
                                        ).value(Value::from("outputValue"))
                                    ]))
                        .steps(vec![
                            Step::new(
                                "com.datadoghq.dd.monitor.listMonitors".to_string(),
                                "Step1".to_string(),
                            )
                            .connection_label("INTEGRATION_DATADOG".to_string())
                            .outbound_edges(vec![OutboundEdge::new(
                                "main".to_string(),
                                "Step2".to_string(),
                            )])
                            .parameters(vec![Parameter::new(
                                "tags".to_string(),
                                Value::from("service:monitoring"),
                            )]),
                            Step::new("com.datadoghq.core.noop".to_string(), "Step2".to_string()),
                        ])
                        .triggers(vec![
                            Trigger::MonitorTriggerWrapper(Box::new(
                                MonitorTriggerWrapper::new(
                                    MonitorTrigger::new().rate_limit(
                                        TriggerRateLimit::new()
                                            .count(1)
                                            .interval("3600s".to_string()),
                                    ),
                                )
                                .start_step_names(vec!["Step1".to_string()]),
                            )),
                            Trigger::GithubWebhookTriggerWrapper(Box::new(
                                GithubWebhookTriggerWrapper::new(GithubWebhookTrigger::new())
                                    .start_step_names(vec!["Step1".to_string()]),
                            )),
                        ]),
                )
                .tags(vec![
                    "team:infra".to_string(),
                    "service:monitoring".to_string(),
                    "foo:bar".to_string(),
                ]),
            WorkflowDataType::WORKFLOWS,
        )
        .id("22222222-2222-2222-2222-222222222222".to_string()),
    );
    let configuration = datadog::Configuration::new();
    let api = WorkflowAutomationAPI::with_config(configuration);
    let resp = api.update_workflow(workflow_data_id.clone(), body).await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run


```

#####  Update an existing Workflow returns "Successfully updated a workflow." response
```
/**
 * Update an existing Workflow returns "Successfully updated a workflow." response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.WorkflowAutomationApi(configuration);

// there is a valid "workflow" in the system
const WORKFLOW_DATA_ID = process.env.WORKFLOW_DATA_ID as string;

const params: v2.WorkflowAutomationApiUpdateWorkflowRequest = {
  body: {
    data: {
      attributes: {
        description: "A sample workflow.",
        name: "Example Workflow",
        published: true,
        spec: {
          connectionEnvs: [
            {
              connections: [
                {
                  connectionId: "11111111-1111-1111-1111-111111111111",
                  label: "INTEGRATION_DATADOG",
                },
              ],
              env: "default",
            },
          ],
          inputSchema: {
            parameters: [
              {
                defaultValue: "default",
                name: "input",
                type: "STRING",
              },
            ],
          },
          outputSchema: {
            parameters: [
              {
                name: "output",
                type: "ARRAY_OBJECT",
                value: "outputValue",
              },
            ],
          },
          steps: [
            {
              actionId: "com.datadoghq.dd.monitor.listMonitors",
              connectionLabel: "INTEGRATION_DATADOG",
              name: "Step1",
              outboundEdges: [
                {
                  branchName: "main",
                  nextStepName: "Step2",
                },
              ],
              parameters: [
                {
                  name: "tags",
                  value: "service:monitoring",
                },
              ],
            },
            {
              actionId: "com.datadoghq.core.noop",
              name: "Step2",
            },
          ],
          triggers: [
            {
              monitorTrigger: {
                rateLimit: {
                  count: 1,
                  interval: "3600s",
                },
              },
              startStepNames: ["Step1"],
            },
            {
              startStepNames: ["Step1"],
              githubWebhookTrigger: {},
            },
          ],
        },
        tags: ["team:infra", "service:monitoring", "foo:bar"],
      },
      id: "22222222-2222-2222-2222-222222222222",
      type: "workflows",
    },
  },
  workflowId: WORKFLOW_DATA_ID,
};

apiInstance
  .updateWorkflow(params)
  .then((data: v2.UpdateWorkflowResponse) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"


```

* * *
## [Delete an existing Workflow](https://docs.datadoghq.com/api/latest/workflow-automation/#delete-an-existing-workflow)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/workflow-automation/#delete-an-existing-workflow-v2)


DELETE https://api.ap1.datadoghq.com/api/v2/workflows/{workflow_id}https://api.ap2.datadoghq.com/api/v2/workflows/{workflow_id}https://api.datadoghq.eu/api/v2/workflows/{workflow_id}https://api.ddog-gov.com/api/v2/workflows/{workflow_id}https://api.datadoghq.com/api/v2/workflows/{workflow_id}https://api.us3.datadoghq.com/api/v2/workflows/{workflow_id}https://api.us5.datadoghq.com/api/v2/workflows/{workflow_id}
### Overview
Delete a workflow by ID. This API requires a [registered application key](https://docs.datadoghq.com/api/latest/action-connection/#register-a-new-app-key). Alternatively, you can configure these permissions [in the UI](https://docs.datadoghq.com/account_management/api-app-keys/#actions-api-access). This endpoint requires the `workflows_write` permission.
### Arguments
#### Path Parameters
Name
Type
Description
workflow_id [_required_]
string
The ID of the workflow.
### Response
  * [204](https://docs.datadoghq.com/api/latest/workflow-automation/#DeleteWorkflow-204-v2)
  * [403](https://docs.datadoghq.com/api/latest/workflow-automation/#DeleteWorkflow-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/workflow-automation/#DeleteWorkflow-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/workflow-automation/#DeleteWorkflow-429-v2)


Successfully deleted a workflow.
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/workflow-automation/)
  * [Example](https://docs.datadoghq.com/api/latest/workflow-automation/)


API error response.
Field
Type
Description
errors [_required_]
[object]
A list of errors.
detail
string
A human-readable explanation specific to this occurrence of the error.
meta
object
Non-standard meta-information about the error
source
object
References to the source of the error.
header
string
A string indicating the name of a single request header which caused the error.
parameter
string
A string indicating which URI query parameter caused the error.
pointer
string
A JSON pointer to the value in the request document that caused the error.
status
string
Status code of the response.
title
string
Short human-readable summary of the error.
```
{
  "errors": [
    {
      "detail": "Missing required attribute in body",
      "meta": {},
      "source": {
        "header": "Authorization",
        "parameter": "limit",
        "pointer": "/data/attributes/title"
      },
      "status": "400",
      "title": "Bad Request"
    }
  ]
}
```

Copy
Not found
  * [Model](https://docs.datadoghq.com/api/latest/workflow-automation/)
  * [Example](https://docs.datadoghq.com/api/latest/workflow-automation/)


API error response.
Field
Type
Description
errors [_required_]
[object]
A list of errors.
detail
string
A human-readable explanation specific to this occurrence of the error.
meta
object
Non-standard meta-information about the error
source
object
References to the source of the error.
header
string
A string indicating the name of a single request header which caused the error.
parameter
string
A string indicating which URI query parameter caused the error.
pointer
string
A JSON pointer to the value in the request document that caused the error.
status
string
Status code of the response.
title
string
Short human-readable summary of the error.
```
{
  "errors": [
    {
      "detail": "Missing required attribute in body",
      "meta": {},
      "source": {
        "header": "Authorization",
        "parameter": "limit",
        "pointer": "/data/attributes/title"
      },
      "status": "400",
      "title": "Bad Request"
    }
  ]
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/workflow-automation/)
  * [Example](https://docs.datadoghq.com/api/latest/workflow-automation/)


API error response.
Field
Type
Description
errors [_required_]
[object]
A list of errors.
detail
string
A human-readable explanation specific to this occurrence of the error.
meta
object
Non-standard meta-information about the error
source
object
References to the source of the error.
header
string
A string indicating the name of a single request header which caused the error.
parameter
string
A string indicating which URI query parameter caused the error.
pointer
string
A JSON pointer to the value in the request document that caused the error.
status
string
Status code of the response.
title
string
Short human-readable summary of the error.
```
{
  "errors": [
    {
      "detail": "Missing required attribute in body",
      "meta": {},
      "source": {
        "header": "Authorization",
        "parameter": "limit",
        "pointer": "/data/attributes/title"
      },
      "status": "400",
      "title": "Bad Request"
    }
  ]
}
```

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/workflow-automation/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/workflow-automation/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/workflow-automation/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/workflow-automation/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/workflow-automation/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/workflow-automation/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/workflow-automation/?code-lang=typescript)


#####  Delete an existing Workflow
Copy
```
                  # Path parameters  
export workflow_id="CHANGE_ME"  
# Curl command  
curl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/workflows/${workflow_id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Delete an existing Workflow
```
"""
Delete an existing Workflow returns "Successfully deleted a workflow." response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.workflow_automation_api import WorkflowAutomationApi

# there is a valid "workflow" in the system
WORKFLOW_DATA_ID = environ["WORKFLOW_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = WorkflowAutomationApi(api_client)
    api_instance.delete_workflow(
        workflow_id=WORKFLOW_DATA_ID,
    )

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Delete an existing Workflow
```
# Delete an existing Workflow returns "Successfully deleted a workflow." response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::WorkflowAutomationAPI.new

# there is a valid "workflow" in the system
WORKFLOW_DATA_ID = ENV["WORKFLOW_DATA_ID"]
api_instance.delete_workflow(WORKFLOW_DATA_ID)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Delete an existing Workflow
```
// Delete an existing Workflow returns "Successfully deleted a workflow." response

package main

import (
	"context"
	"fmt"
	"os"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
	// there is a valid "workflow" in the system
	WorkflowDataID := os.Getenv("WORKFLOW_DATA_ID")

	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewWorkflowAutomationApi(apiClient)
	r, err := api.DeleteWorkflow(ctx, WorkflowDataID)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `WorkflowAutomationApi.DeleteWorkflow`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Delete an existing Workflow
```
// Delete an existing Workflow returns "Successfully deleted a workflow." response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.WorkflowAutomationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    WorkflowAutomationApi apiInstance = new WorkflowAutomationApi(defaultClient);

    // there is a valid "workflow" in the system
    String WORKFLOW_DATA_ID = System.getenv("WORKFLOW_DATA_ID");

    try {
      apiInstance.deleteWorkflow(WORKFLOW_DATA_ID);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkflowAutomationApi#deleteWorkflow");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"


```

#####  Delete an existing Workflow
```
// Delete an existing Workflow returns "Successfully deleted a workflow." response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_workflow_automation::WorkflowAutomationAPI;

#[tokio::main]
async fn main() {
    // there is a valid "workflow" in the system
    let workflow_data_id = std::env::var("WORKFLOW_DATA_ID").unwrap();
    let configuration = datadog::Configuration::new();
    let api = WorkflowAutomationAPI::with_config(configuration);
    let resp = api.delete_workflow(workflow_data_id.clone()).await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run


```

#####  Delete an existing Workflow
```
/**
 * Delete an existing Workflow returns "Successfully deleted a workflow." response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.WorkflowAutomationApi(configuration);

// there is a valid "workflow" in the system
const WORKFLOW_DATA_ID = process.env.WORKFLOW_DATA_ID as string;

const params: v2.WorkflowAutomationApiDeleteWorkflowRequest = {
  workflowId: WORKFLOW_DATA_ID,
};

apiInstance
  .deleteWorkflow(params)
  .then((data: any) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"


```

* * *
## [List workflow instances](https://docs.datadoghq.com/api/latest/workflow-automation/#list-workflow-instances)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/workflow-automation/#list-workflow-instances-v2)


GET https://api.ap1.datadoghq.com/api/v2/workflows/{workflow_id}/instanceshttps://api.ap2.datadoghq.com/api/v2/workflows/{workflow_id}/instanceshttps://api.datadoghq.eu/api/v2/workflows/{workflow_id}/instanceshttps://api.ddog-gov.com/api/v2/workflows/{workflow_id}/instanceshttps://api.datadoghq.com/api/v2/workflows/{workflow_id}/instanceshttps://api.us3.datadoghq.com/api/v2/workflows/{workflow_id}/instanceshttps://api.us5.datadoghq.com/api/v2/workflows/{workflow_id}/instances
### Overview
List all instances of a given workflow. This API requires a [registered application key](https://docs.datadoghq.com/api/latest/action-connection/#register-a-new-app-key). Alternatively, you can configure these permissions [in the UI](https://docs.datadoghq.com/account_management/api-app-keys/#actions-api-access). This endpoint requires the `workflows_read` permission.
OAuth apps require the `workflows_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#workflow-automation) to access this endpoint.
### Arguments
#### Path Parameters
Name
Type
Description
workflow_id [_required_]
string
The ID of the workflow.
#### Query Strings
Name
Type
Description
page[size]
integer
Size for a given page. The maximum allowed value is 100.
page[number]
integer
Specific page number to return.
### Response
  * [200](https://docs.datadoghq.com/api/latest/workflow-automation/#ListWorkflowInstances-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/workflow-automation/#ListWorkflowInstances-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/workflow-automation/#ListWorkflowInstances-403-v2)
  * [429](https://docs.datadoghq.com/api/latest/workflow-automation/#ListWorkflowInstances-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/workflow-automation/)
  * [Example](https://docs.datadoghq.com/api/latest/workflow-automation/)


Response returned when listing workflow instances.
Expand All
Field
Type
Description
<any-key>
```
{
  "data": [
    {
      "id": "string"
    }
  ],
  "meta": {
    "page": {
      "totalCount": "integer"
    }
  }
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/workflow-automation/)
  * [Example](https://docs.datadoghq.com/api/latest/workflow-automation/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/workflow-automation/)
  * [Example](https://docs.datadoghq.com/api/latest/workflow-automation/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/workflow-automation/)
  * [Example](https://docs.datadoghq.com/api/latest/workflow-automation/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/workflow-automation/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/workflow-automation/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/workflow-automation/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/workflow-automation/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/workflow-automation/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/workflow-automation/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/workflow-automation/?code-lang=typescript)


#####  List workflow instances
Copy
```
                  # Path parameters  
export workflow_id="CHANGE_ME"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/workflows/${workflow_id}/instances" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  List workflow instances
```
"""
List workflow instances returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.workflow_automation_api import WorkflowAutomationApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = WorkflowAutomationApi(api_client)
    response = api_instance.list_workflow_instances(
        workflow_id="ccf73164-1998-4785-a7a3-8d06c7e5f558",
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  List workflow instances
```
# List workflow instances returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::WorkflowAutomationAPI.new
p api_instance.list_workflow_instances("ccf73164-1998-4785-a7a3-8d06c7e5f558")

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  List workflow instances
```
// List workflow instances returns "OK" response

package main

import (
	"context"
	"encoding/json"
	"fmt"
	"os"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewWorkflowAutomationApi(apiClient)
	resp, r, err := api.ListWorkflowInstances(ctx, "ccf73164-1998-4785-a7a3-8d06c7e5f558", *datadogV2.NewListWorkflowInstancesOptionalParameters())

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `WorkflowAutomationApi.ListWorkflowInstances`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `WorkflowAutomationApi.ListWorkflowInstances`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  List workflow instances
```
// List workflow instances returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.WorkflowAutomationApi;
import com.datadog.api.client.v2.model.WorkflowListInstancesResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    WorkflowAutomationApi apiInstance = new WorkflowAutomationApi(defaultClient);

    try {
      WorkflowListInstancesResponse result =
          apiInstance.listWorkflowInstances("ccf73164-1998-4785-a7a3-8d06c7e5f558");
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkflowAutomationApi#listWorkflowInstances");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"


```

#####  List workflow instances
```
// List workflow instances returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_workflow_automation::ListWorkflowInstancesOptionalParams;
use datadog_api_client::datadogV2::api_workflow_automation::WorkflowAutomationAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = WorkflowAutomationAPI::with_config(configuration);
    let resp = api
        .list_workflow_instances(
            "ccf73164-1998-4785-a7a3-8d06c7e5f558".to_string(),
            ListWorkflowInstancesOptionalParams::default(),
        )
        .await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run


```

#####  List workflow instances
```
/**
 * List workflow instances returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.WorkflowAutomationApi(configuration);

const params: v2.WorkflowAutomationApiListWorkflowInstancesRequest = {
  workflowId: "ccf73164-1998-4785-a7a3-8d06c7e5f558",
};

apiInstance
  .listWorkflowInstances(params)
  .then((data: v2.WorkflowListInstancesResponse) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"


```

* * *
## [Execute a workflow](https://docs.datadoghq.com/api/latest/workflow-automation/#execute-a-workflow)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/workflow-automation/#execute-a-workflow-v2)


POST https://api.ap1.datadoghq.com/api/v2/workflows/{workflow_id}/instanceshttps://api.ap2.datadoghq.com/api/v2/workflows/{workflow_id}/instanceshttps://api.datadoghq.eu/api/v2/workflows/{workflow_id}/instanceshttps://api.ddog-gov.com/api/v2/workflows/{workflow_id}/instanceshttps://api.datadoghq.com/api/v2/workflows/{workflow_id}/instanceshttps://api.us3.datadoghq.com/api/v2/workflows/{workflow_id}/instanceshttps://api.us5.datadoghq.com/api/v2/workflows/{workflow_id}/instances
### Overview
Execute the given workflow. This API requires a [registered application key](https://docs.datadoghq.com/api/latest/action-connection/#register-a-new-app-key). Alternatively, you can configure these permissions [in the UI](https://docs.datadoghq.com/account_management/api-app-keys/#actions-api-access). This endpoint requires the `workflows_run` permission.
OAuth apps require the `workflows_run` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#workflow-automation) to access this endpoint.
### Arguments
#### Path Parameters
Name
Type
Description
workflow_id [_required_]
string
The ID of the workflow.
### Request
#### Body Data (required)
  * [Model](https://docs.datadoghq.com/api/latest/workflow-automation/)
  * [Example](https://docs.datadoghq.com/api/latest/workflow-automation/)


Field
Type
Description
meta
object
Additional information for creating a workflow instance.
payload
object
The input parameters to the workflow.
```
{
  "meta": {
    "payload": {
      "input": "value"
    }
  }
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/workflow-automation/#CreateWorkflowInstance-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/workflow-automation/#CreateWorkflowInstance-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/workflow-automation/#CreateWorkflowInstance-403-v2)
  * [429](https://docs.datadoghq.com/api/latest/workflow-automation/#CreateWorkflowInstance-429-v2)


Created
  * [Model](https://docs.datadoghq.com/api/latest/workflow-automation/)
  * [Example](https://docs.datadoghq.com/api/latest/workflow-automation/)


Response returned upon successful workflow instance creation.
Expand All
Field
Type
Description
<any-key>
```
{
  "data": {
    "id": "string"
  }
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/workflow-automation/)
  * [Example](https://docs.datadoghq.com/api/latest/workflow-automation/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/workflow-automation/)
  * [Example](https://docs.datadoghq.com/api/latest/workflow-automation/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/workflow-automation/)
  * [Example](https://docs.datadoghq.com/api/latest/workflow-automation/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/workflow-automation/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/workflow-automation/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/workflow-automation/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/workflow-automation/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/workflow-automation/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/workflow-automation/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/workflow-automation/?code-lang=typescript)


#####  Execute a workflow returns "Created" response
Copy
```
                          # Path parameters  
export workflow_id="CHANGE_ME"  
# Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/workflows/${workflow_id}/instances" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "meta": {
    "payload": {
      "input": "value"
    }
  }
}
EOF  

                        
```

#####  Execute a workflow returns "Created" response
```
// Execute a workflow returns "Created" response

package main

import (
	"context"
	"encoding/json"
	"fmt"
	"os"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
	body := datadogV2.WorkflowInstanceCreateRequest{
		Meta: &datadogV2.WorkflowInstanceCreateMeta{
			Payload: map[string]interface{}{
				"input": "value",
			},
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewWorkflowAutomationApi(apiClient)
	resp, r, err := api.CreateWorkflowInstance(ctx, "ccf73164-1998-4785-a7a3-8d06c7e5f558", body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `WorkflowAutomationApi.CreateWorkflowInstance`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `WorkflowAutomationApi.CreateWorkflowInstance`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Execute a workflow returns "Created" response
```
// Execute a workflow returns "Created" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.WorkflowAutomationApi;
import com.datadog.api.client.v2.model.WorkflowInstanceCreateMeta;
import com.datadog.api.client.v2.model.WorkflowInstanceCreateRequest;
import com.datadog.api.client.v2.model.WorkflowInstanceCreateResponse;
import java.util.Map;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    WorkflowAutomationApi apiInstance = new WorkflowAutomationApi(defaultClient);

    WorkflowInstanceCreateRequest body =
        new WorkflowInstanceCreateRequest()
            .meta(
                new WorkflowInstanceCreateMeta()
                    .payload(Map.ofEntries(Map.entry("input", "value"))));

    try {
      WorkflowInstanceCreateResponse result =
          apiInstance.createWorkflowInstance("ccf73164-1998-4785-a7a3-8d06c7e5f558", body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkflowAutomationApi#createWorkflowInstance");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"


```

#####  Execute a workflow returns "Created" response
```
"""
Execute a workflow returns "Created" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.workflow_automation_api import WorkflowAutomationApi
from datadog_api_client.v2.model.workflow_instance_create_meta import WorkflowInstanceCreateMeta
from datadog_api_client.v2.model.workflow_instance_create_request import WorkflowInstanceCreateRequest

body = WorkflowInstanceCreateRequest(
    meta=WorkflowInstanceCreateMeta(
        payload=dict([("input", "value")]),
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = WorkflowAutomationApi(api_client)
    response = api_instance.create_workflow_instance(workflow_id="ccf73164-1998-4785-a7a3-8d06c7e5f558", body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Execute a workflow returns "Created" response
```
# Execute a workflow returns "Created" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::WorkflowAutomationAPI.new

body = DatadogAPIClient::V2::WorkflowInstanceCreateRequest.new({
  meta: DatadogAPIClient::V2::WorkflowInstanceCreateMeta.new({
    payload: {
      "input": "value",
    },
  }),
})
p api_instance.create_workflow_instance("ccf73164-1998-4785-a7a3-8d06c7e5f558", body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Execute a workflow returns "Created" response
```
// Execute a workflow returns "Created" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_workflow_automation::WorkflowAutomationAPI;
use datadog_api_client::datadogV2::model::WorkflowInstanceCreateMeta;
use datadog_api_client::datadogV2::model::WorkflowInstanceCreateRequest;
use serde_json::Value;
use std::collections::BTreeMap;

#[tokio::main]
async fn main() {
    let body =
        WorkflowInstanceCreateRequest::new().meta(WorkflowInstanceCreateMeta::new().payload(
            BTreeMap::from([("input".to_string(), Value::from("value"))]),
        ));
    let configuration = datadog::Configuration::new();
    let api = WorkflowAutomationAPI::with_config(configuration);
    let resp = api
        .create_workflow_instance("ccf73164-1998-4785-a7a3-8d06c7e5f558".to_string(), body)
        .await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run


```

#####  Execute a workflow returns "Created" response
```
/**
 * Execute a workflow returns "Created" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.WorkflowAutomationApi(configuration);

const params: v2.WorkflowAutomationApiCreateWorkflowInstanceRequest = {
  body: {
    meta: {
      payload: {
        input: "value",
      },
    },
  },
  workflowId: "ccf73164-1998-4785-a7a3-8d06c7e5f558",
};

apiInstance
  .createWorkflowInstance(params)
  .then((data: v2.WorkflowInstanceCreateResponse) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"


```

* * *
## [Get a workflow instance](https://docs.datadoghq.com/api/latest/workflow-automation/#get-a-workflow-instance)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/workflow-automation/#get-a-workflow-instance-v2)


GET https://api.ap1.datadoghq.com/api/v2/workflows/{workflow_id}/instances/{instance_id}https://api.ap2.datadoghq.com/api/v2/workflows/{workflow_id}/instances/{instance_id}https://api.datadoghq.eu/api/v2/workflows/{workflow_id}/instances/{instance_id}https://api.ddog-gov.com/api/v2/workflows/{workflow_id}/instances/{instance_id}https://api.datadoghq.com/api/v2/workflows/{workflow_id}/instances/{instance_id}https://api.us3.datadoghq.com/api/v2/workflows/{workflow_id}/instances/{instance_id}https://api.us5.datadoghq.com/api/v2/workflows/{workflow_id}/instances/{instance_id}
### Overview
Get a specific execution of a given workflow. This API requires a [registered application key](https://docs.datadoghq.com/api/latest/action-connection/#register-a-new-app-key). Alternatively, you can configure these permissions [in the UI](https://docs.datadoghq.com/account_management/api-app-keys/#actions-api-access). This endpoint requires the `workflows_read` permission.
OAuth apps require the `workflows_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#workflow-automation) to access this endpoint.
### Arguments
#### Path Parameters
Name
Type
Description
workflow_id [_required_]
string
The ID of the workflow.
instance_id [_required_]
string
The ID of the workflow instance.
### Response
  * [200](https://docs.datadoghq.com/api/latest/workflow-automation/#GetWorkflowInstance-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/workflow-automation/#GetWorkflowInstance-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/workflow-automation/#GetWorkflowInstance-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/workflow-automation/#GetWorkflowInstance-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/workflow-automation/#GetWorkflowInstance-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/workflow-automation/)
  * [Example](https://docs.datadoghq.com/api/latest/workflow-automation/)


The state of the given workflow instance.
Expand All
Field
Type
Description
<any-key>
```
{
  "data": {
    "attributes": {
      "id": "string"
    }
  }
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/workflow-automation/)
  * [Example](https://docs.datadoghq.com/api/latest/workflow-automation/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/workflow-automation/)
  * [Example](https://docs.datadoghq.com/api/latest/workflow-automation/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Not Found
  * [Model](https://docs.datadoghq.com/api/latest/workflow-automation/)
  * [Example](https://docs.datadoghq.com/api/latest/workflow-automation/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/workflow-automation/)
  * [Example](https://docs.datadoghq.com/api/latest/workflow-automation/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/workflow-automation/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/workflow-automation/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/workflow-automation/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/workflow-automation/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/workflow-automation/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/workflow-automation/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/workflow-automation/?code-lang=typescript)


#####  Get a workflow instance
Copy
```
                  # Path parameters  
export workflow_id="CHANGE_ME"  
export instance_id="CHANGE_ME"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/workflows/${workflow_id}/instances/${instance_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get a workflow instance
```
"""
Get a workflow instance returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.workflow_automation_api import WorkflowAutomationApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = WorkflowAutomationApi(api_client)
    response = api_instance.get_workflow_instance(
        workflow_id="ccf73164-1998-4785-a7a3-8d06c7e5f558",
        instance_id="305a472b-71ab-4ce8-8f8d-75db635627b5",
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Get a workflow instance
```
# Get a workflow instance returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::WorkflowAutomationAPI.new
p api_instance.get_workflow_instance("ccf73164-1998-4785-a7a3-8d06c7e5f558", "305a472b-71ab-4ce8-8f8d-75db635627b5")

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get a workflow instance
```
// Get a workflow instance returns "OK" response

package main

import (
	"context"
	"encoding/json"
	"fmt"
	"os"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewWorkflowAutomationApi(apiClient)
	resp, r, err := api.GetWorkflowInstance(ctx, "ccf73164-1998-4785-a7a3-8d06c7e5f558", "305a472b-71ab-4ce8-8f8d-75db635627b5")

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `WorkflowAutomationApi.GetWorkflowInstance`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `WorkflowAutomationApi.GetWorkflowInstance`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Get a workflow instance
```
// Get a workflow instance returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.WorkflowAutomationApi;
import com.datadog.api.client.v2.model.WorklflowGetInstanceResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    WorkflowAutomationApi apiInstance = new WorkflowAutomationApi(defaultClient);

    try {
      WorklflowGetInstanceResponse result =
          apiInstance.getWorkflowInstance(
              "ccf73164-1998-4785-a7a3-8d06c7e5f558", "305a472b-71ab-4ce8-8f8d-75db635627b5");
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkflowAutomationApi#getWorkflowInstance");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"


```

#####  Get a workflow instance
```
// Get a workflow instance returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_workflow_automation::WorkflowAutomationAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = WorkflowAutomationAPI::with_config(configuration);
    let resp = api
        .get_workflow_instance(
            "ccf73164-1998-4785-a7a3-8d06c7e5f558".to_string(),
            "305a472b-71ab-4ce8-8f8d-75db635627b5".to_string(),
        )
        .await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run


```

#####  Get a workflow instance
```
/**
 * Get a workflow instance returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.WorkflowAutomationApi(configuration);

const params: v2.WorkflowAutomationApiGetWorkflowInstanceRequest = {
  workflowId: "ccf73164-1998-4785-a7a3-8d06c7e5f558",
  instanceId: "305a472b-71ab-4ce8-8f8d-75db635627b5",
};

apiInstance
  .getWorkflowInstance(params)
  .then((data: v2.WorklflowGetInstanceResponse) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"


```

* * *
## [Cancel a workflow instance](https://docs.datadoghq.com/api/latest/workflow-automation/#cancel-a-workflow-instance)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/workflow-automation/#cancel-a-workflow-instance-v2)


PUT https://api.ap1.datadoghq.com/api/v2/workflows/{workflow_id}/instances/{instance_id}/cancelhttps://api.ap2.datadoghq.com/api/v2/workflows/{workflow_id}/instances/{instance_id}/cancelhttps://api.datadoghq.eu/api/v2/workflows/{workflow_id}/instances/{instance_id}/cancelhttps://api.ddog-gov.com/api/v2/workflows/{workflow_id}/instances/{instance_id}/cancelhttps://api.datadoghq.com/api/v2/workflows/{workflow_id}/instances/{instance_id}/cancelhttps://api.us3.datadoghq.com/api/v2/workflows/{workflow_id}/instances/{instance_id}/cancelhttps://api.us5.datadoghq.com/api/v2/workflows/{workflow_id}/instances/{instance_id}/cancel
### Overview
Cancels a specific execution of a given workflow. This API requires a [registered application key](https://docs.datadoghq.com/api/latest/action-connection/#register-a-new-app-key). Alternatively, you can configure these permissions [in the UI](https://docs.datadoghq.com/account_management/api-app-keys/#actions-api-access). This endpoint requires the `workflows_run` permission.
### Arguments
#### Path Parameters
Name
Type
Description
workflow_id [_required_]
string
The ID of the workflow.
instance_id [_required_]
string
The ID of the workflow instance.
### Response
  * [200](https://docs.datadoghq.com/api/latest/workflow-automation/#CancelWorkflowInstance-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/workflow-automation/#CancelWorkflowInstance-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/workflow-automation/#CancelWorkflowInstance-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/workflow-automation/#CancelWorkflowInstance-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/workflow-automation/#CancelWorkflowInstance-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/workflow-automation/)
  * [Example](https://docs.datadoghq.com/api/latest/workflow-automation/)


Information about the canceled instance.
Field
Type
Description
data
object
Data about the canceled instance.
id
string
The id of the canceled instance
```
{
  "data": {
    "id": "string"
  }
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/workflow-automation/)
  * [Example](https://docs.datadoghq.com/api/latest/workflow-automation/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/workflow-automation/)
  * [Example](https://docs.datadoghq.com/api/latest/workflow-automation/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Not Found
  * [Model](https://docs.datadoghq.com/api/latest/workflow-automation/)
  * [Example](https://docs.datadoghq.com/api/latest/workflow-automation/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/workflow-automation/)
  * [Example](https://docs.datadoghq.com/api/latest/workflow-automation/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/workflow-automation/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/workflow-automation/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/workflow-automation/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/workflow-automation/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/workflow-automation/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/workflow-automation/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/workflow-automation/?code-lang=typescript)


#####  Cancel a workflow instance
Copy
```
                  # Path parameters  
export workflow_id="CHANGE_ME"  
export instance_id="CHANGE_ME"  
# Curl command  
curl -X PUT "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/workflows/${workflow_id}/instances/${instance_id}/cancel" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Cancel a workflow instance
```
"""
Cancel a workflow instance returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.workflow_automation_api import WorkflowAutomationApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = WorkflowAutomationApi(api_client)
    response = api_instance.cancel_workflow_instance(
        workflow_id="ccf73164-1998-4785-a7a3-8d06c7e5f558",
        instance_id="305a472b-71ab-4ce8-8f8d-75db635627b5",
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Cancel a workflow instance
```
# Cancel a workflow instance returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::WorkflowAutomationAPI.new
p api_instance.cancel_workflow_instance("ccf73164-1998-4785-a7a3-8d06c7e5f558", "305a472b-71ab-4ce8-8f8d-75db635627b5")

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Cancel a workflow instance
```
// Cancel a workflow instance returns "OK" response

package main

import (
	"context"
	"encoding/json"
	"fmt"
	"os"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewWorkflowAutomationApi(apiClient)
	resp, r, err := api.CancelWorkflowInstance(ctx, "ccf73164-1998-4785-a7a3-8d06c7e5f558", "305a472b-71ab-4ce8-8f8d-75db635627b5")

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `WorkflowAutomationApi.CancelWorkflowInstance`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `WorkflowAutomationApi.CancelWorkflowInstance`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Cancel a workflow instance
```
// Cancel a workflow instance returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.WorkflowAutomationApi;
import com.datadog.api.client.v2.model.WorklflowCancelInstanceResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    WorkflowAutomationApi apiInstance = new WorkflowAutomationApi(defaultClient);

    try {
      WorklflowCancelInstanceResponse result =
          apiInstance.cancelWorkflowInstance(
              "ccf73164-1998-4785-a7a3-8d06c7e5f558", "305a472b-71ab-4ce8-8f8d-75db635627b5");
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkflowAutomationApi#cancelWorkflowInstance");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"


```

#####  Cancel a workflow instance
```
// Cancel a workflow instance returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_workflow_automation::WorkflowAutomationAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = WorkflowAutomationAPI::with_config(configuration);
    let resp = api
        .cancel_workflow_instance(
            "ccf73164-1998-4785-a7a3-8d06c7e5f558".to_string(),
            "305a472b-71ab-4ce8-8f8d-75db635627b5".to_string(),
        )
        .await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run


```

#####  Cancel a workflow instance
```
/**
 * Cancel a workflow instance returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.WorkflowAutomationApi(configuration);

const params: v2.WorkflowAutomationApiCancelWorkflowInstanceRequest = {
  workflowId: "ccf73164-1998-4785-a7a3-8d06c7e5f558",
  instanceId: "305a472b-71ab-4ce8-8f8d-75db635627b5",
};

apiInstance
  .cancelWorkflowInstance(params)
  .then((data: v2.WorklflowCancelInstanceResponse) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"


```

* * *
![](https://id.rlcdn.com/464526.gif)![](https://t.co/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=c170ef65-c699-4085-ab5f-57d16f444c4e&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=2b7ae509-6303-4b07-ab71-0d71cc38deaa&pt=Workflow%20Automation&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fworkflow-automation%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=c170ef65-c699-4085-ab5f-57d16f444c4e&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=2b7ae509-6303-4b07-ab71-0d71cc38deaa&pt=Workflow%20Automation&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fworkflow-automation%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)
![](https://bat.bing.com/action/0?ti=4061438&Ver=2&mid=0074867a-4ad3-42f6-82ac-ab542a1198d2&bo=2&sid=e9375cd0f0bd11f08bcff787fa0fba6f&vid=e9375d80f0bd11f0b5075ff6ae9d9677&vids=0&msclkid=N&pi=918639831&lg=en-US&sw=1080&sh=600&sc=24&tl=Workflow%20Automation&p=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fworkflow-automation%2F&r=&lt=10501&evt=pageLoad&sv=2&asc=G&cdb=AQAS&rn=438524)
