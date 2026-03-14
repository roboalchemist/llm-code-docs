# Source: https://novita.ai/docs/api-reference/gpu-instance-migrate-instance.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Migrate Instance

## API Description

When migrating an instance, any new data on the system disk and local disk will not be preserved.

## Request Headers

<ParamField header="Content-Type" type="string" required={true}>
  Enum: `application/json`
</ParamField>

<ParamField header="Authorization" type="string" required={true}>
  Bearer authentication format, for example: Bearer \{\{API Key}}.
</ParamField>

## Request Body

<ParamField body="instanceId" type="string" required={true}>
  The ID of the instance to be migrated.
</ParamField>


Built with [Mintlify](https://mintlify.com).