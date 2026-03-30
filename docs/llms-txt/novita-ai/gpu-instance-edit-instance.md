# Source: https://novita.ai/docs/guides/gpu-instance-edit-instance.md

# Source: https://novita.ai/docs/api-reference/gpu-instance-edit-instance.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Edit Instance

## Request Headers

<ParamField header="Content-Type" type="string" required={true}>
  Enum: `application/json`
</ParamField>

<ParamField header="Authorization" type="string" required={true}>
  Bearer authentication format, for example: Bearer \{\{API Key}}.
</ParamField>

## Request Body

<ParamField body="instanceId" type="string" required={true}>
  ID of the instance to edit.
</ParamField>

<ParamField body="ports" type="object[]" required={false}>
  Ports to be exposed by the instance. The total number of ports used by ports + tools must not exceed 15.

  <Expandable title="properties" defaultOpen={false}>
    <ParamField body="port" type="integer" required={false}>
      Port number. Supported port range: 1-65535, except for 2222, 2223, and 2224 which are reserved for internal use.
    </ParamField>

    <ParamField body="type" type="string" required={false}>
      Protocol type. Supported values: `tcp`, `http`.
    </ParamField>
  </Expandable>
</ParamField>

<ParamField body="expandRootDisk" type="integer" required={false}>
  Size to expand the root disk, in GB. Integer, value must be >= 0. Set to 0 if no expansion is needed.
</ParamField>


Built with [Mintlify](https://mintlify.com).