# Source: https://infisical.com/docs/documentation/platform/webhooks.md

# Webhooks

> Learn the fundamentals of Infisical webhooks.

Webhooks can be used to trigger changes to your integrations when secrets are modified, providing smooth integration with other third-party applications.

<img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/webhooks.png" alt="webhooks" />

To create a webhook for a particular project, go to `Project Settings > Webhooks`.

Infisical supports two webhook types - General and Slack. If you need to integrate with Slack, use the Slack type with an [Incoming Webhook](https://api.slack.com/messaging/webhooks). When creating a webhook, you can specify an environment and folder path to trigger only specific integrations.

<img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/webhook-create.png" alt="webhook-create" />

## Secret Key Verification

A secret key is a way for users to verify that a webhook request was sent by Infisical and is intended for the correct integration.

When you provide a secret key, Infisical will sign the payload of the webhook request using the key and attach a header called `x-infisical-signature` to the request with a payload.

The header will be in the format `t=<timestamp>;<signature>`. You can then generate the signature yourself by generating a SHA256 hash of the payload with the secret key that you know.

If the signature in the header matches the signature that you generated, then you can be sure that the request was sent by Infisical and is intended for your integration. The timestamp in the header ensures that the request is not replayed.

### Webhook Payload Format

```json  theme={"dark"}
{
  "event": "secrets.modified",
  "project": {
    "workspaceId": "the workspace id",
    "environment": "project environment",
    "secretPath": "project folder path"
  },
  "timestamp": ""
}
```

```json  theme={"dark"}
{
  "event": "secrets.reminder-expired",
  "project": {
    "workspaceId": "the workspace id",
    "environment": "project environment",
    "secretPath": "project folder path",
    "secretName": "name of the secret",
    "secretId": "id of the secret",
    "reminderNote": "reminder note of the secret"
  },
  "timestamp": ""
}
```
