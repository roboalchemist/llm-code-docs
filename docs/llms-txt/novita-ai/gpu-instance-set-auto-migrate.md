# Source: https://novita.ai/docs/api-reference/gpu-instance-set-auto-migrate.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Set Auto Migrate Strategy

## Request Headers

<ParamField header="Content-Type" type="string" required={true}>
  Enum: `application/json`
</ParamField>

<ParamField header="Authorization" type="string" required={true}>
  Bearer authentication format, for example: Bearer \{\{API Key}}.
</ParamField>

## Request Body

<ParamField body="instanceId" type="string" required={true}>
  Instance ID.
</ParamField>

<ParamField body="autoMigrateOpen" type="boolean" required={true}>
  Enable/disable automatic instance migration.
</ParamField>

<ParamField body="autoMigrateSystemDisk" type="boolean" required={true}>
  Enable/disable automatic system disk migration during instance migration.
</ParamField>


Built with [Mintlify](https://mintlify.com).