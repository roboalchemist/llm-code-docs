# Source: https://www.courier.com/docs/platform/automations/get-profile.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# GET Profile

> The GET Profile node fetches a user's profile using user_id (e.g., refs.data.user_id) and attaches it to the automation context, enabling access via refs.profile in subsequent steps.

## Overview

The GET Profile node fetches a user's Courier profile and attaches it to the automation run context. After this node runs, profile data is available via `refs.profile` in subsequent steps.

Set the user ID to a dynamic value from the data object, such as `refs.data.user_id`.

<Frame caption="GET Profile Node">
  <img src="https://mintcdn.com/courier-4f1f25dc/WNdu5qn7yJu4418-/assets/platform/automations/get-profile-node.png?fit=max&auto=format&n=WNdu5qn7yJu4418-&q=85&s=a32ec4020d914b988eed9eae6fd0b47f" alt="GET Profile Node" width="1894" height="858" data-path="assets/platform/automations/get-profile-node.png" />
</Frame>

### Ad Hoc Usage

Use the `get-profile` step in an [ad hoc automation](/platform/automations/steps) to load a user's profile before sending:

```json  theme={null}
{
  "automation": {
    "steps": [
      {
        "action": "get-profile",
        "user_id": "user_123",
        "merge_strategy": "none"
      },
      {
        "action": "send",
        "template": "order-update",
        "recipient": "user_123"
      }
    ]
  }
}
```

### Merge Strategy

After the `get-profile` step, the user's stored profile fields (email, phone, custom attributes) are available in the automation context. The `merge_strategy` field controls how fetched data combines with existing context data (defaults to `soft-merge`):

| Strategy     | Behavior                                                                            |
| ------------ | ----------------------------------------------------------------------------------- |
| `soft-merge` | Merge fetched fields into existing context; existing fields are preserved (default) |
| `replace`    | Replace the entire context path with fetched data                                   |
| `overwrite`  | Overwrite all properties from fetched data                                          |
| `none`       | Do not modify context if the path already has data                                  |

See [Fetch Data](/platform/automations/fetch-data) for more on merge strategies.
