# Source: https://upstash.com/docs/devops/terraform/data_sources/upstash_qstash_endpoint_data.md

> ## Documentation Index
> Fetch the complete documentation index at: https://upstash.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# upstash_qstash_endpoint_data

<RequestExample>
  ```hcl example.tf theme={"system"}
  data "upstash_qstash_endpoint_data" "exampleQStashEndpointData" {
    endpoint_id = resource.upstash_qstash_endpoint.exampleQStashEndpoint.endpoint_id
  }
  ```
</RequestExample>

## Schema

### Required

<ParamField query="topic_id" type="string" required>
  Topic Id that the endpoint is added to
</ParamField>

### Read-Only

<ResponseField name="endpoint_id" type="string">
  Unique QStash Endpoint ID
</ResponseField>

<ResponseField name="id" type="number">
  The ID of this resource.
</ResponseField>

<ResponseField name="url" type="string">
  Unique QStash Topic Name for Endpoint
</ResponseField>
