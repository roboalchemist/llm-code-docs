# Source: https://novita.ai/docs/guides/gpu-instance-upgrade-instance.md

# Source: https://novita.ai/docs/api-reference/gpu-instance-upgrade-instance.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Upgrade Instance

## API Description

When upgrading an instance, all parameters must be provided in full.

## Request Headers

<ParamField header="Content-Type" type="string" required={true}>
  Enum: `application/json`
</ParamField>

<ParamField header="Authorization" type="string" required={true}>
  Bearer authentication format, for example: Bearer \{\{API Key}}.
</ParamField>

## Request Body

<ParamField body="instanceId" type="string" required={true}>
  The ID of the instance to be upgraded.
</ParamField>

<ParamField body="imageUrl" type="string" required={true}>
  Container image URL. String, length limit: 1-500 characters.
</ParamField>

<ParamField body="imageAuthId" type="string" required={false}>
  Image registry authentication ID.
</ParamField>

<ParamField body="envs" type="object[]" required={true}>
  Instance environment variables. Up to 100 environment variable pairs can be created.

  <Expandable title="properties" defaultOpen={false}>
    <ParamField body="key" type="string" required={false}>
      Environment variable name. String, length limit: 0-511 characters.
    </ParamField>

    <ParamField body="value" type="string" required={false}>
      Environment variable value. String, length limit: 0-4095 characters.
    </ParamField>
  </Expandable>
</ParamField>

<ParamField body="command" type="string" required={true}>
  Container startup command. String, length limit: 0-2047 characters.
</ParamField>

<ParamField body="entrypoint" type="string" required={true}>
  Container startup entrypoint. This setting will override the Docker image's ENTRYPOINT. String, length limit: 0-2047 characters.
</ParamField>

<ParamField body="save" type="boolean" required={true}>
  Whether to retain data from the previous instance. Boolean, values: true or false.
</ParamField>

<ParamField body="networkVolume" type="object" required={true}>
  Configure cloud storage (type: network). Each instance supports mounting up to 30 cloud storage volumes. To remove all cloud storage mounts, set volumeMounts to an empty array: \[].

  <Expandable title="properties" defaultOpen={false}>
    <ParamField body="volumeMounts" type="object[]" required={true}>
      Cloud storage mount information.

      <Expandable title="properties" defaultOpen={true}>
        <ParamField body="type" type="string" required={true}>
          Storage type. Must be set to network.
        </ParamField>

        <ParamField body="id" type="string" required={true}>
          Cloud storage ID.
        </ParamField>

        <ParamField body="mountPath" type="string" required={true}>
          Mount path for the cloud storage. Default: "/network". String, length limit: 1-4095 characters.
        </ParamField>
      </Expandable>
    </ParamField>
  </Expandable>
</ParamField>


Built with [Mintlify](https://mintlify.com).