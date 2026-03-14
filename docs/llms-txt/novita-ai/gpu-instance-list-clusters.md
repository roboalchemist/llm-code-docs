# Source: https://novita.ai/docs/api-reference/gpu-instance-list-clusters.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# List Clusters

## Request Headers

<ParamField header="Content-Type" type="string" required={true}>
  Enum: `application/json`
</ParamField>

<ParamField header="Authorization" type="string" required={true}>
  Bearer authentication format, for example: Bearer \{\{API Key}}.
</ParamField>

## Response

<ResponseField name="data" type="object[]" required={true}>
  <Expandable title="properties" defaultOpen={true}>
    <ResponseField name="id" type="string" required={true}>
      Cluster ID.
    </ResponseField>

    <ResponseField name="name" type="string" required={true}>
      Cluster name.
    </ResponseField>

    <ResponseField name="availableGpuType" type="[string]" required={true}>
      Supported GPU types in the cluster.
    </ResponseField>

    <ResponseField name="supportNetworkStorage" type="boolean" required={true}>
      Whether the cluster supports creating cloud storage.
    </ResponseField>

    <ResponseField name="supportInstanceNetwork" type="boolean" required={true}>
      Whether the cluster supports creating VPC networks.
    </ResponseField>
  </Expandable>
</ResponseField>


Built with [Mintlify](https://mintlify.com).