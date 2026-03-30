# Source: https://novita.ai/docs/api-reference/gpu-instance-restart-instance.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Restart Instance

**This API is used to restart a specific GPU instance.**

## Request Headers

<ParamField header="Content-Type" type="string" required={true}>
  Enum: `application/json`
</ParamField>

<ParamField header="Authorization" type="string" required={true}>
  Bearer authentication format, for example: Bearer \{\{API Key}}.
</ParamField>

## Request Body

<ParamField body="instanceId" type="string" required={true}>
  ID of the instance to be restarted.
</ParamField>


Built with [Mintlify](https://mintlify.com).