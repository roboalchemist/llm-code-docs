# Source: https://docs.knock.app/mapi-reference/channels/schemas/push_channel_settings.md

### PushChannelSettings

Push channel settings. Only used as configuration as part of a workflow channel step.

#### Attributes

- **token_deregistration** (boolean) - Whether to deregister a push-token when a push send hard bounces. This is to prevent the same token from being used for future pushes.

#### Example

```json
{
  "token_deregistration": true
}
```

