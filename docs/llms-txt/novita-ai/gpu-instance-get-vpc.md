# Source: https://novita.ai/docs/api-reference/gpu-instance-get-vpc.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get VPC Network

## Request Headers

<ParamField header="Content-Type" type="string" required={true}>
  Enum: `application/json`
</ParamField>

<ParamField header="Authorization" type="string" required={true}>
  Bearer authentication format, for example: Bearer \{\{API Key}}.
</ParamField>

## Query Parameters

<ParamField query="networkId" type="string" required={true}>
  Cluster ID. String, length limit: 1-255 characters. Only one is supported.
</ParamField>

## Response

<ResponseField name="network" type="object[]" required={true}>
  VPC network information.

  <Expandable title="properties" defaultOpen={true}>
    <ResponseField name="Id" type="string" required={true}>
      VPC network ID.
    </ResponseField>

    <ResponseField name="user" type="string" required={true}>
      User account ID.
    </ResponseField>

    <ResponseField name="name" type="string" required={true}>
      VPC network name.
    </ResponseField>

    <ResponseField name="state" type="object[]" required={true}>
      VPC network status.

      <Expandable title="properties" defaultOpen={true}>
        <ResponseField name="state" type="string" required={true}>
          VPC network status. Possible values:

          * creating: Being created.
          * ready: Successfully created.
        </ResponseField>

        <ResponseField name="error" type="string" required={false}>
          Error message if VPC network creation fails or the network is unavailable.
        </ResponseField>
      </Expandable>
    </ResponseField>

    <ResponseField name="segment" type="string" required={true}>
      VPC network segment.
    </ResponseField>

    <ResponseField name="clusterId" type="string" required={true}>
      Cluster ID.
    </ResponseField>

    <ResponseField name="Addresses" type="object[]" required={true}>
      Instance information under the VPC network.

      <Expandable title="properties" defaultOpen={true}>
        <ResponseField name="Id" type="string" required={true}>
          Instance ID.
        </ResponseField>

        <ResponseField name="Ip" type="string" required={true}>
          Instance IP address.
        </ResponseField>
      </Expandable>
    </ResponseField>

    <ResponseField name="createTime" type="string" required={true}>
      VPC network creation time. Format: Unix timestamp.
    </ResponseField>
  </Expandable>
</ResponseField>


Built with [Mintlify](https://mintlify.com).