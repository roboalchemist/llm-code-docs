# Source: https://novita.ai/docs/guides/gpu-instance-save-image.md

# Source: https://novita.ai/docs/api-reference/gpu-instance-save-image.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Save Instance Image

## Request Headers

<ParamField header="Content-Type" type="string" required={true}>
  Enum: `application/json`
</ParamField>

<ParamField header="Authorization" type="string" required={true}>
  Bearer authentication format, for example: Bearer \{\{API Key}}.
</ParamField>

## Request Body

<ParamField body="instanceId" type="string" required={true}>
  Instance ID. String, length: 1-255 characters.
</ParamField>

<ParamField body="image" type="string" required={true}>
  Target image address, including registry/repository:tag. String, length: 1-4095 characters.
</ParamField>

<ParamField body="registryAuthId" type="string" required={false}>
  Container registry authentication ID. Not required for public registries or platform-provided registries. Required for third-party private registries.
</ParamField>

## Response

<ResponseField name="jobId" type="string" required={true}>
  Image save job ID. Use this ID to check status and logs in the Console under Job Management.
</ResponseField>


Built with [Mintlify](https://mintlify.com).