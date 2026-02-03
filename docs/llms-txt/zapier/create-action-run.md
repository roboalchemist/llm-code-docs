# Source: https://docs.zapier.com/powered-by-zapier/running-actions/create-action-run.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.zapier.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Creating Action Runs

## Prerequisites

Before you begin, make sure:

* You have access to a **public Zapier integration**.
* You’ve [registered your app and authenticated](/powered-by-zapier/authentication/methods/user-access-token) to use the API.
* You have at least one **action** configured in your integration, with required fields and sample data tested in the Zapier UI or via the API.

***

To trigger an action, make a `POST` request to [/v2/action-runs/](/powered-by-zapier/api-reference/actions/create-an-action-run)

<Warning>
  **Important:** Before every action run, for the `action` attribute on your request body you should retreive a new/unique `id` from the [Get Actions](/powered-by-zapier/api-reference/actions/get-actions) endpoint for the action that you'd like to execute. This ensures that the action run can be uniquely tracked, that it can be properly debugged, and that attributions are properly reported.

  **Note:** *The `id` attribute will be unique for every lookup on the [Get Actions](/powered-by-zapier/api-reference/actions/get-actions) endpoint, and the `key` attribute will be the action's consistent developer-provided identifier.*
</Warning>

### Request Example

```http  theme={null}
POST https://api.zapier.com/v2/action-runs/
Authorization: Bearer YOUR_ACCESS_TOKEN
Content-Type: application/json

{
  "action": "core:89sg4uhs5g85gh53hso59hs399hgs59",
  "authentication": "UHsi8e6K",
  "input": {
    "email": "user@example.com",
    "message": "Hello from Powered by Zapier!"
  }
}
```

### Parameters

| Field            | Type   | Description                                             |
| ---------------- | ------ | ------------------------------------------------------- |
| `action`         | string | The unique identifier of the action you want to run.    |
| `authentication` | string | The authentication id needed to run this action.        |
| `input`          | object | Key-value pairs of input fields required by the action. |

### Response Example

```json  theme={null}
{
  "data": {
    "type": "run",
    "id": "arun_abc123"
  }
}
```

You can use this run's `id` to poll for the run’s status and result.
