# Source: https://upstash.com/docs/workflow/rest/flow-control/list.md

# Source: https://upstash.com/docs/workflow/rest/dlq/list.md

# Source: https://upstash.com/docs/workflow/basics/client/dlq/list.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/functions/list.md

# Source: https://upstash.com/docs/workflow/rest/flow-control/list.md

# Source: https://upstash.com/docs/workflow/rest/dlq/list.md

# Source: https://upstash.com/docs/workflow/basics/client/dlq/list.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/functions/list.md

# Source: https://upstash.com/docs/workflow/rest/flow-control/list.md

# Source: https://upstash.com/docs/workflow/rest/dlq/list.md

# Source: https://upstash.com/docs/workflow/basics/client/dlq/list.md

# Source: https://upstash.com/docs/qstash/api/url-groups/list.md

# Source: https://upstash.com/docs/qstash/api/schedules/list.md

# Source: https://upstash.com/docs/qstash/api/queues/list.md

# Source: https://upstash.com/docs/qstash/api/logs/list.md

# Source: https://upstash.com/docs/qstash/api/flow-control/list.md

# Source: https://upstash.com/docs/qstash/api/events/list.md

# Source: https://upstash.com/docs/workflow/rest/flow-control/list.md

# Source: https://upstash.com/docs/workflow/rest/dlq/list.md

# Source: https://upstash.com/docs/workflow/basics/client/dlq/list.md

# Source: https://upstash.com/docs/qstash/api/url-groups/list.md

# Source: https://upstash.com/docs/qstash/api/schedules/list.md

# Source: https://upstash.com/docs/qstash/api/queues/list.md

# Source: https://upstash.com/docs/qstash/api/logs/list.md

# Source: https://upstash.com/docs/qstash/api/flow-control/list.md

# Source: https://upstash.com/docs/qstash/api/events/list.md

# Source: https://upstash.com/docs/workflow/rest/flow-control/list.md

# Source: https://upstash.com/docs/workflow/rest/dlq/list.md

# Source: https://upstash.com/docs/workflow/basics/client/dlq/list.md

# Source: https://upstash.com/docs/qstash/api/url-groups/list.md

# Source: https://upstash.com/docs/qstash/api/schedules/list.md

# Source: https://upstash.com/docs/qstash/api/queues/list.md

# Source: https://upstash.com/docs/qstash/api/logs/list.md

# Source: https://upstash.com/docs/qstash/api/flow-control/list.md

# Source: https://upstash.com/docs/qstash/api/events/list.md

# Source: https://upstash.com/docs/workflow/rest/flow-control/list.md

# List Flow-Control Keys

> List All Flow Control Keys

## Response

<ResponseField name="flowControls" type="Array">
  <Expandable>
    <ResponseField name="flowControlKey" type="string">
      The key of the flow control. See the [flow control](/workflow/features/flow-control) for more details.
    </ResponseField>

    <ResponseField name="waitListSize" type="integer">
      The number of messages in the wait list that waits for `parallelism` set in the flow control.
    </ResponseField>
  </Expandable>
</ResponseField>

<RequestExample>
  ```sh  theme={"system"}
  curl -X GET https://qstash.upstash.io/v2/flowControl/  -H "Authorization: Bearer <token>"
  ```
</RequestExample>
