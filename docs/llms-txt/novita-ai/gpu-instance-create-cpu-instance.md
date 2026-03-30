# Source: https://novita.ai/docs/api-reference/gpu-instance-create-cpu-instance.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Create CPU Instance

## Request Headers

<ParamField header="Content-Type" type="string" required={true}>
  Enum: `application/json`
</ParamField>

<ParamField header="Authorization" type="string" required={true}>
  Bearer authentication format, for example: Bearer \{\{API Key}}.
</ParamField>

## Request Body

<ParamField body="name" type="string" required={false}>
  CPU instance name. String, length limit: 0-255 characters.
</ParamField>

<ParamField body="productId" type="string" required={true}>
  Product ID for deploying the instance. You can query this via the [List CPU Products API](/api-reference/gpu-instance-list-cpu-products). String, length limit: 1-255 characters.
</ParamField>

<ParamField body="imageUrl" type="string" required={true}>
  Container image URL. String, length limit: 1-500 characters.
</ParamField>

<ParamField body="imageAuth" type="string" required={false}>
  Image repository authentication. Format: username:password. Required for private images; not required for public images or platform images. String, length limit: 0-10239 characters.
</ParamField>

<ParamField body="imageAuthId" type="string" required={false}>
  Image repository authentication ID.
</ParamField>

<ParamField body="ports" type="string" required={false}>
  Ports exposed by the instance. String, e.g.: 80/http, 3306/tcp. Supported port range: 1-65535, except for 2222, 2223, 2224 which are reserved for internal use. Supported port types: tcp, http. The total number of ports used by ports + tools must not exceed 15.
</ParamField>

<ParamField body="envs" type="object[]" required={false}>
  Instance environment variables. Array, up to 100 environment variables.

  <Expandable title="properties" defaultOpen={false}>
    <ParamField body="key" type="string" required={false}>
      Environment variable name. String, length limit: 0-511 characters.
    </ParamField>

    <ParamField body="value" type="string" required={false}>
      Environment variable value. String, length limit: 0-4095 characters.
    </ParamField>
  </Expandable>
</ParamField>

<ParamField body="tools" type="object[]" required={false}>
  Enable official image support tools. Array. Currently, some official images only include Jupyter. The total number of ports used by ports + tools must not exceed 15.

  <Expandable title="properties" defaultOpen={false}>
    <ParamField body="name" type="string" required={false}>
      Tool name. Valid value: Jupyter.
    </ParamField>

    <ParamField body="port" type="string" required={false}>
      Port used by the tool. Supported port range: 1-65535, except for 2222, 2223, 2224 which are reserved for internal use.
    </ParamField>

    <ParamField body="type" type="string" required={false}>
      Port type used by the tool. Valid values: tcp, http.
    </ParamField>
  </Expandable>
</ParamField>

<ParamField body="command" type="string" required={false}>
  Container startup command. This setting will override the Docker image's CMD. String, length limit: 0-2047 characters.
</ParamField>

<ParamField body="entrypoint" type="string" required={false}>
  Container startup entrypoint. This setting will override the Docker image's ENTRYPOINT. String, length limit: 0-2047 characters.
</ParamField>

<ParamField body="clusterId" type="string" required={false}>
  Specify the cluster ID to create the instance in. If left empty, the instance will be created in a random cluster. String, length limit: 0-255 characters.
</ParamField>

<ParamField body="localStorageMountPoint" type="string" required={false}>
  Mount point for local storage. Default: "/workspace". String, length limit: 1-4095 characters.
</ParamField>

<ParamField body="networkStorages" type="object[]" required={false}>
  Cloud storage mount configuration. Array, up to 30 cloud storages can be mounted.

  <Expandable title="properties" defaultOpen={false}>
    <ParamField body="Id" type="string" required={false}>
      Cloud storage ID.
    </ParamField>

    <ParamField body="mountPoint" type="string" required={false}>
      Mount point for cloud storage. Default: "/network". String, length limit: 1-4095 characters.
    </ParamField>
  </Expandable>
</ParamField>

<ParamField body="networkId" type="string" required={false}>
  VPC network ID. Leave empty if not using a VPC network.
</ParamField>

<ParamField body="kind" type="string" required={true}>
  Instance type. Valid values: cpu, gpu. Must be set to cpu.
</ParamField>

## Response

<ResponseField name="id" type="string" required={false}>
  Created instance ID.
</ResponseField>


Built with [Mintlify](https://mintlify.com).