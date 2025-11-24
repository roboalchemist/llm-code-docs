# Source: https://docs.zapier.com/powered-by-zapier/zap-creation/selecting-an-action.md

# Selecting an Action

> An Action is an operation that can be performed against a third-party API; such as a `READ` or a `WRITE`.

<Note>
  [Action Schema](/powered-by-zapier/api-reference/common-types/action)
</Note>

Once you've [selected an app](/powered-by-zapier/api-reference/apps/get-apps-\[v2]), we can fetch the list of available actions for a selected App by making a request to the [`/actions` endpoint](/powered-by-zapier/api-reference/actions/get-actions):

```js  theme={null}
// GET /actions?app=4b3920d6-1d5a-4071-b837-9383dc511b80&action_type=READ
{
  "data": [
    {
      "type": "action",
      "id": "core:853266",
      "action_type": "READ",
      "title": "New Lead",
      "description": "Triggers when a new lead is added to SuperExampleCRM",
      "is_instant": true
    },
    {
      "type": "action",
      "id": "uag:1f188536-6dd0-4172-8414-2b90914ddee9",
      "action_type": "READ",
      "title": "New Deal",
      "description": "Triggers when a new deal is added to SuperExampleCRM",
      "is_instant": false
    }
  ]
}
```

<Info>
  As an example, `READ` and `WRITE` map to *Trigger* and *Action* respectively
  In the Zapier ecosystem.{" "}
</Info>

Our user can then select one of these Actions that they wish to use as the Trigger for their Zap. The `id` field is accepted in several other endpoints.

<Tip>
  Looking to focus your experience to just a few actions? Check out [Hardcoding
  an Action](/powered-by-zapier/zap-creation/hardcoding-an-action).
</Tip>
