# Source: https://upstash.com/docs/workflow/rest/flow-control/get.md

# Source: https://upstash.com/docs/workflow/rest/dlq/get.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/string/get.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/json/get.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/string/get.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/json/get.md

# Source: https://upstash.com/docs/qstash/api/url-groups/get.md

# Source: https://upstash.com/docs/qstash/api/signingKeys/get.md

# Source: https://upstash.com/docs/qstash/api/schedules/get.md

# Source: https://upstash.com/docs/qstash/api/queues/get.md

# Source: https://upstash.com/docs/qstash/api/messages/get.md

# Source: https://upstash.com/docs/qstash/api/flow-control/get.md

# Source: https://upstash.com/docs/workflow/rest/flow-control/get.md

# Source: https://upstash.com/docs/workflow/rest/dlq/get.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/string/get.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/json/get.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/string/get.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/json/get.md

# Source: https://upstash.com/docs/qstash/api/url-groups/get.md

# Source: https://upstash.com/docs/qstash/api/signingKeys/get.md

# Source: https://upstash.com/docs/qstash/api/schedules/get.md

# Source: https://upstash.com/docs/qstash/api/queues/get.md

# Source: https://upstash.com/docs/qstash/api/messages/get.md

# Source: https://upstash.com/docs/qstash/api/flow-control/get.md

# Source: https://upstash.com/docs/workflow/rest/flow-control/get.md

# Source: https://upstash.com/docs/workflow/rest/dlq/get.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/string/get.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/json/get.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/string/get.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/json/get.md

# Source: https://upstash.com/docs/qstash/api/url-groups/get.md

# Source: https://upstash.com/docs/qstash/api/signingKeys/get.md

# Source: https://upstash.com/docs/qstash/api/schedules/get.md

# Source: https://upstash.com/docs/qstash/api/queues/get.md

# Source: https://upstash.com/docs/qstash/api/messages/get.md

# Source: https://upstash.com/docs/qstash/api/flow-control/get.md

# Source: https://upstash.com/docs/workflow/rest/flow-control/get.md

# Get Flow-Control

> Get Information on Flow-Control

## Request

<ParamField path="flowControlKey" type="string">
  The key of the flow control. See the [flow control](/workflow/features/flow-control) for more details.
</ParamField>

## Response

<ResponseField name="flowControlKey" type="string">
  The key of of the flow control.
</ResponseField>

<ResponseField name="waitListSize" type="integer">
  The number of messages in the wait list that waits for `parallelism` set in the flow control.
</ResponseField>

<RequestExample>
  ```sh  theme={"system"}
  curl -X GET https://qstash.upstash.io/v2/flowControl/YOUR_FLOW_CONTROL_KEY  -H "Authorization: Bearer <token>"
  ```
</RequestExample>
