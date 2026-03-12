# Source: https://docs.port.io/actions-and-automations/setup-backend/webhook/port-execution-agent/installation-methods/docker.md

# Docker

This page we will walk you through the installation of the Port execution agent using docker.

## Installation[â](#installation "Direct link to Installation")

**Remember to replace the placeholders for `<PORT_CLIENT_ID>`, `<PORT_CLIENT_SECRET>`, `<PORT_ORG_ID>` and `<KAFKA_CONSUMER_GROUP_ID>`.**

```
docker run \
  -e PORT_CLIENT_ID=<PORT_CLIENT_ID> \
  -e PORT_CLIENT_SECRET=<PORT_CLIENT_SECRET> \
  -e PORT_API_BASE_URL="https://api.port.io" \
  -e PORT_ORG_ID=<PORT_ORG_ID> \
  -e KAFKA_CONSUMER_GROUP_ID=<KAFKA_CONSUMER_GROUP_ID> \
  -e STREAMER_NAME=KAFKA \
  -e KAFKA_CONSUMER_SECURITY_PROTOCOL=SASL_SSL \
  -e KAFKA_CONSUMER_AUTHENTICATION_MECHANISM=SCRAM-SHA-512 \
  -e KAFKA_CONSUMER_AUTO_OFFSET_RESET=largest \
  ghcr.io/port-labs/port-agent:latest
```

## Next Steps[â](#next-steps "Direct link to Next Steps")

* Refer to the [usage guide](/actions-and-automations/setup-backend/webhook/port-execution-agent/usage.md) to set up a self-service action that sends a webhook.
* Customize the [payload mapping](/actions-and-automations/setup-backend/webhook/port-execution-agent/control-the-payload.md?installationMethod=docker) to control the payload sent to the target.
