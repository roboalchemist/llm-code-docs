# Source: https://learn.microsoft.com/en-us/power-automate/developer/desktop-flow-public-apis

Title: Work with desktop flows using code - Power Automate

URL Source: https://learn.microsoft.com/en-us/power-automate/developer/desktop-flow-public-apis

Published Time: Fri, 10 Oct 2025 05:19:20 GMT

Markdown Content:
Developers can add [desktop flows](https://learn.microsoft.com/en-us/power-automate/desktop-flows/introduction) functionality to their applications, including programmatically triggering and canceling desktop flows. These capabilities are offered as part of the Microsoft Dataverse platform.

1. Knowledge of [Dataverse Web API](https://learn.microsoft.com/en-us/power-apps/developer/data-platform/webapi/perform-operations-web-api), [authentication with Dataverse](https://learn.microsoft.com/en-us/power-apps/developer/data-platform/authentication) and [using OAuth with Dataverse](https://learn.microsoft.com/en-us/power-apps/developer/data-platform/authenticate-oauth).
2. Knowledge of Dataverse environment and organization notions, and [how to retrieve the organization URL](https://learn.microsoft.com/en-us/power-apps/developer/data-platform/webapi/discover-url-organization-web-api) manually or programmatically.
3. Knowledge of [desktop flows notions](https://learn.microsoft.com/en-us/power-automate/desktop-flows/run-pad-flow) and of what [connections are and how to create them](https://learn.microsoft.com/en-us/power-automate/desktop-flows/install#setup-desktop-flows-connections-and-machine-credentials).

Important

In this article, you must replace all squared brackets [...] in URLs and input/output data with values specific to your scenario.

All desktop flows scripts are in Dataverse as part of the [workflow entity](https://learn.microsoft.com/en-us/power-apps/developer/data-platform/reference/entities/workflow).

Filter the list of workflows based on the category to identify desktop flows.

```
Authorization: Bearer eyJ0eXAiOi...
Accept: application/json

GET https://[Organization URI]/api/data/v9.2/workflows?$filter=category+eq+6&$select=name,workflowid&$orderby=name HTTP/1.1
```

```
{
    "@odata.context": "https://[Organization URI]/api/data/v9.2/$metadata#workflows(name,workflowid)",
    "value": [
        {
            "@odata.etag": "W1069462",
            "name": "Desktop flow 1",
            "workflowid": "f091ffab-58bb-4630-a115-659453d56f59",
        },
        {
            "@odata.etag": "W1028555",
            "name": "Desktop flow 2",
            "workflowid": "eafba1a2-e8d4-4efa-b549-11d4dfd9a3d1",
        }
    ]
}
```

If you need to retrieve the flow schema for inputs and/or outputs, you can use the clientData field for the target workflow.

```
Authorization: Bearer eyJ0eXAiOi...
Accept: application/json

GET https://[Organization URI]/api/data/v9.2/workflows([Workflow Id])/inputs/$value HTTP/1.1
```

```
{
    "schema": {
        "properties": {
            "inputText": {
                "default": "",
                "description": "",
                "format": null,
                "title": "inputText",
                "type": "string",
                "value": ""
            },
            "inputInteger": {
                "default": "",
                "description": "",
                "format": null,
                "title": "inputInteger",
                "type": "number",
                "value": "0"
            }
        },
        "type": "object"
    }
}
```

```
Authorization: Bearer eyJ0eXAiOi...
Accept: application/json

GET https://[Organization URI]/api/data/v9.2/workflows([Workflow Id])/outputs/$value HTTP/1.1
```

```
{
    "schema": {
        "properties": {
            "outputText": {
                "default": "",
                "description": "",
                "format": null,
                "title": "outputText",
                "type": "string",
                "value": null
            },
            "outputInteger": {
                "default": "",
                "description": "",
                "format": null,
                "title": "outputInteger",
                "type": "number",
                "value": null
            }
        },
        "type": "object"
    }
}
```

Dataverse stores all desktop flow runs in the [flowsession entity](https://learn.microsoft.com/en-us/power-apps/developer/data-platform/reference/entities/flowsession).

```
Authorization: Bearer eyJ0eXAiOi...
Accept: application/json

GET https://[Organization URI]/api/data/v9.2/flowsessions([Flow session ID])?$select=statuscode,statecode,startedon,completedon HTTP/1.1
```

```
{
    "@odata.context": "https://[Organization URI]/api/data/v9.2/$metadata#flowsessions(statuscode,statecode,startedon,completedon)/$entity",
    "@odata.etag": "W1276122",
    "statuscode": 8,
    "statecode": 0,
    "startedon": "2022-06-16T12:54:40Z",
    "completedon": "2022-06-16T12:57:46Z",
}
```

If the desktop flow has outputs, you can query the outputs field to retrieve them.

```
Authorization: Bearer eyJ0eXAiOi...
Accept: application/json

GET https://[Organization URI]/api/data/v9.2/flowsessions([Flow session ID])/outputs/$value HTTP/1.1
```

```
{
    "Output1": "My output value"
}
```

By using Dataverse, you can add the functionality of triggering a desktop flow through your application. To implement this functionality, you need to use the [RunDesktopFlow action](https://learn.microsoft.com/en-us/dynamics365/customer-engagement/web-api/rundesktopflow).

To call the action, you'll need the following information.

* The `ID` of the desktop flow that you want to run. You can get this ID via the API as the [List available desktop flows](https://learn.microsoft.com/en-us/power-automate/developer/desktop-flow-public-apis#list-available-desktop-flows) section outlines earlier in this article.

Tip

Alternatively, you can retrieve the ID manually from the desktop flow details URL in Power Automate. The URL format is: `https://make.powerautomate.com/manage/environments/[Environment ID]/uiflows/[Desktop Flow ID]/details`.

For more information, see [Manage desktop flows](https://learn.microsoft.com/en-us/power-automate/desktop-flows/manage).

* The `name` of the desktop flow connection (targeting a machine/machine group) to use to run your flow. The name can be retrieved from the URL of the same connection page in Power Automate. The URL format is:

`https://make.powerautomate.com/manage/environments/[Environment ID]/connections?apiName=shared_uiflow&connectionName=[Connection Name]`.

Tip

Alternatively, you can use a connection reference's logical name as the input of the connection instead of the connection name (usage example described below). The connection references are stored in the Dataverse table connectionreference and can be listed programmatically in the same way as desktop flows detailed in the [List available desktop flows](https://learn.microsoft.com/en-us/power-automate/developer/desktop-flow-public-apis#list-available-desktop-flows) section.

For more information, see [Use a connection reference in a solution](https://learn.microsoft.com/en-us/power-apps/maker/data-platform/create-connection-reference) and [connectionreference table/entity reference](https://learn.microsoft.com/en-us/power-apps/developer/data-platform/reference/entities/connectionreference).

```
Authorization: Bearer eyJ0eXAiOi...
Accept: application/json

POST https://[Organization URI]/api/data/v9.2/workflows([Workflow ID])/Microsoft.Dynamics.CRM.RunDesktopFlow HTTP/1.1  
{
    "runMode": "attended",
    "runPriority": "normal",
    "connectionName": "[Connection Name]",
    "timeout": 7200,
    "inputs": "{\"Input1\":\"Value\", \"Input2\":\"Value\"}"
}
```

```
Authorization: Bearer eyJ0eXAiOi...
Accept: application/json

POST https://[Organization URI]/api/data/v9.2/workflows([Workflow ID])/Microsoft.Dynamics.CRM.RunDesktopFlow HTTP/1.1  
{
    "runMode": "attended",
    "runPriority": "normal",
    "connectionName": "[Connection Reference Logical Name]",
    "connectionType": 2,
    "timeout": 7200,
    "inputs": "{\"Input1\":\"Value\", \"Input2\":\"Value\"}"
}
```

```
{
    "@odata.context": "https://[Organization URI]/api/data/v9.2/$metadata#Microsoft.Dynamics.CRM.RunDesktopFlowResponse",
    "flowsessionId": "d9687093-d0c0-ec11-983e-0022480b428a"
}
```

The inputs of the script are viewable in the run details page on the Power Automate portal (in Preview).

Warning

When using the API, there are some limitations to be aware of:

* Triggering a desktop flow run with an account having "User" privileges will work. However, canceling the run and querying the status needs "Owner" privileges.

* Dataverse impersonation isn't supported.

* The input field content size is limited to 2 MB.

An optional parameter "callbackUrl" is available in the body of the [RunDesktopFlow action](https://learn.microsoft.com/en-us/dynamics365/customer-engagement/web-api/rundesktopflow). You can use it if you want to be notified of your script completion. A POST request will be sent to the provided URL when the script is complete.

```
User-Agent: EnterpriseConnectors/1.0
Content-type: application/json; charset=utf-8
x-ms-workflow-id: [Workflow ID]
x-ms-run-id: [Flow session ID]

POST [yourCallbackURL]
```

```
{
    "statuscode": 4,
    "statecode": 0,
    "startedon": "2022-09-05T08:04:11Z",
    "completedon": "2022-09-05T08:04:41Z",
    "flowsessionid": "d9687093-d0c0-ec11-983e-0022480b428a"
}
```

If no callback URL parameter is provided, the flow session status should be polled from Dataverse (refers to [Get the status of a desktop flow run](https://learn.microsoft.com/en-us/power-automate/developer/desktop-flow-public-apis#get-the-status-of-a-desktop-flow-run)).

Note

* You can still use the status polling as a fallback mechanism even if you provide a callback URL parameter.
* Your callback endpoint operation should be idempotent.
* The POST request will be retried three times with one second interval if your endpoint responds with a Server Error response (code 500 and above) or a "Request Timeout" response (code 408).

Requirements for the callback URL parameter

* Your server must have the current [TLS and cipher suites](https://learn.microsoft.com/en-us/power-platform/admin/server-cipher-tls-requirements).
* Only the HTTPS protocol is allowed.
* Access to localhost (loopback) isn't permitted.
* IP addresses can't be used. You must use a named web address that requires DNS name resolution.
* Your server must allow connections from [Power Platform and Dynamics 365 services IP address values specified under the AzureCloud service tag](https://learn.microsoft.com/en-us/power-platform/admin/online-requirements#ip-addresses-required).

Tip

As the callback call isn't authenticated, some precautions should be taken

* Check the flow session Id validity when the callback notification is received. Dataverse is the source of truth.
* Implement a rate limit strategy on your server side.
* Try to limit the callback URL sharing between several organizations.

Similar to the [Trigger](https://learn.microsoft.com/en-us/power-automate/developer/desktop-flow-public-apis#trigger-a-desktop-flow-run) functionality, you can also cancel a queued/running desktop flow. To cancel a desktop flow, use the [CancelDesktopFlowRun action](https://learn.microsoft.com/en-us/dynamics365/customer-engagement/web-api/canceldesktopflowrun).

```
Authorization: Bearer eyJ0eXAiOi...
Accept: application/json

POST https://[Organization URI]/api/data/v9.2/flowsessions(d9687093-d0c0-ec11-983e-0022480b428a)/Microsoft.Dynamics.CRM.CancelDesktopFlowRun HTTP/1.1
```

```
HTTP/1.1 204 No Content
```

When an error occurs, the response has a different format that matches Dataverse error messages. The http error code and the message should provide enough information to understand the issue.

```
HTTP/1.1 403 Forbidden

{
    "error": {
        "code": "0x80040220",
        "message": " Principal user (Id=526..., type=8) is missing prvReadworkflow privilege (Id=88...*)”
    }
}
```

* We currently support up to 70 desktop flows runs per minute for every connection.
