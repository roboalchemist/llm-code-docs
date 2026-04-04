# Source: https://novita.ai/docs/api-reference/gpu-instance-create-instance.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Create GPU Instance

## Request Headers

<ParamField header="Content-Type" type="string" required={true}>
  Enum: `application/json`
</ParamField>

<ParamField header="Authorization" type="string" required={true}>
  Bearer authentication format, for example: Bearer \{\{API Key}}.
</ParamField>

## Request Body

<ParamField body="name" type="string" required={false}>
  Instance name. String, length limit: 0-255 characters.
</ParamField>

<ParamField body="productId" type="string" required={true}>
  GPU product ID. String, length limit: 1-255 characters. You can query this via the [List GPU Products API](/api-reference/gpu-instance-list-products).
</ParamField>

<ParamField body="gpuNum" type="integer" required={true}>
  Number of GPUs. Integer, valid range: \[1, 8].
</ParamField>

<ParamField body="rootfsSize" type="integer" required={true}>
  Root filesystem size. Integer, valid range: \[10, 6144]. If the minimum value is less than 10 GB, the system will default to 10 GB. The maximum value is dynamically limited by available storage resources and can be queried via the product list API.
</ParamField>

<ParamField body="imageUrl" type="string" required={true}>
  Image URL. String, length limit: 1-500 characters.
</ParamField>

<ParamField body="imageAuth" type="string" required={false}>
  Image authentication (username:password). String, length limit: 0-10239 characters.
</ParamField>

<ParamField body="imageAuthId" type="string" required={false}>
  Image repository authentication ID.
</ParamField>

<ParamField body="ports" type="string" required={false}>
  Instance open ports, e.g.: 80/http, 3306/tcp. Supported port range: \[1-65535], except for 2222, 2223, 2224 which are reserved for internal use. Supported port types: \[tcp, http]. The total number of ports used by ports + tools must not exceed 15.
</ParamField>

<ParamField body="envs" type="object[]" required={false}>
  Instance environment variables. Up to 100 environment variables can be created.

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
  Enable official image support tools. Currently, some official images only include Jupyter. The total number of ports used by ports + tools must not exceed 15.

  <Expandable title="properties" defaultOpen={false}>
    <ParamField body="name" type="string" required={false}>
      Tool name. Valid values: \[Jupyter].
    </ParamField>

    <ParamField body="port" type="string" required={false}>
      Port used by the tool. Supported port range: \[1-65535], except for 2222, 2223, 2224 which are reserved for internal use.
    </ParamField>

    <ParamField body="type" type="string" required={false}>
      Port type used by the tool. Supported types: \[tcp, http].
    </ParamField>
  </Expandable>
</ParamField>

<ParamField body="command" type="string" required={false}>
  Instance startup command. String, length limit: 0-2047 characters.
</ParamField>

<ParamField body="entrypoint" type="string" required={false}>
  Instance startup entrypoint. This setting will override the Docker image's ENTRYPOINT. String, length limit: 0-2047 characters.
</ParamField>

<ParamField body="clusterId" type="string" required={false}>
  Specify the cluster ID to create the instance in. If left empty, the instance will be created in a random cluster.
</ParamField>

<ParamField body="networkStorages" type="object[]" required={false}>
  Cloud storage mount configuration. Up to 30 cloud storages can be mounted.

  <Expandable title="properties" defaultOpen={false}>
    <ParamField body="Id" type="string" required={false}>
      Network storage ID.
    </ParamField>

    <ParamField body="mountPoint" type="string" required={false}>
      Network storage mount path. Default: "/network". String, length limit: 1-4095 characters.
    </ParamField>
  </Expandable>
</ParamField>

<ParamField body="networkId" type="string" required={false}>
  VPC network ID. Leave empty if not using a VPC network.
</ParamField>

<ParamField body="kind" type="string" required={true}>
  Instance type. Valid values: \[gpu, cpu].
</ParamField>

<ParamField body="month" type="integer" required={false}>
  Number of months for subscription instance. Set to 0 to create a pay-as-you-go instance. Integer, value must be greater than or equal to 0.
</ParamField>

<ParamField body="billingMode" type="string" required={false}>
  Instance billing mode. Valid values: `onDemand`, `monthly`, `spot`. <br />
  Default: `onDemand`.<br />
  Note: If month > 0 is set, `monthly` billing mode will be enforced.

  * `onDemand`: Pay-as-you-go billing
  * `monthly`: Monthly subscription billing
  * `spot`: Spot instance billing
</ParamField>

<ParamField body="autoRenew" type="boolean" required={false}>
  Whether to automatically renew. Boolean, default value: false.<br />
  Note: This parameter is only effective when monthly billing is enabled.
</ParamField>

<ParamField body="autoRenewMonth" type="integer" required={false}>
  Number of months to automatically renew. Integer, valid range: \[1, 12].<br />
  Note: This parameter is only effective when monthly billing is enabled and auto renew is enabled.
</ParamField>

<ParamField body="minCudaVersion" type="string" required={false}>
  Minimum CUDA version supported for instance creation. Must be specified in the format: 11.8, 12.4, etc. String, length limit: 0-255 characters.
</ParamField>

## Response

<ResponseField name="id" type="string" required={false}>
  Created instance ID.
</ResponseField>


Built with [Mintlify](https://mintlify.com).