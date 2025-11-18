# Source: https://upstash.com/docs/devops/terraform/resources/upstash_qstash_endpoint.md

# upstash_qstash_endpoint

> Create and manage QStash endpoints.

<RequestExample>
  ```hcl example.tf theme={"system"}
  resource "upstash_qstash_endpoint" "exampleQStashEndpoint" {
    url      = "https://***.***"
    topic_id = resource.upstash_qstash_topic.exampleQstashTopic.topic_id
  }
  ```
</RequestExample>

## Schema

### Required

<ParamField query="topic_id" type="string" required>
  Topic ID that the endpoint is added to
</ParamField>

<ParamField query="url" type="string" required>
  URL of the endpoint
</ParamField>

### Read-Only

<ResponseField name="endpoint_id" type="string">
  Unique QStash endpoint ID
</ResponseField>

<ResponseField name="id" type="string">
  The ID of this resource.
</ResponseField>

<ResponseField name="topic_name" type="string">
  Unique QStash topic name for endpoint
</ResponseField>
