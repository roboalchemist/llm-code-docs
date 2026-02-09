# Source: https://upstash.com/docs/workflow/features/dlq.md

# Source: https://upstash.com/docs/qstash/sdks/ts/examples/dlq.md

# Source: https://upstash.com/docs/qstash/sdks/py/examples/dlq.md

# Source: https://upstash.com/docs/qstash/features/dlq.md

> ## Documentation Index
> Fetch the complete documentation index at: https://upstash.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Dead Letter Queues

At times, your API may fail to process a request. This could be due to a bug in your code, a temporary issue with a third-party service, or even network issues.
QStash automatically retries messages that fail due to a temporary issue but eventually stops and moves the message to a dead letter queue to be handled manually.

Read more about retries [here](/qstash/features/retry).

## How to Use the Dead Letter Queue

You can manually republish messages from the dead letter queue in the console.

<Frame>
  <img src="https://mintcdn.com/upstash/pqZtv0gXFMQuy8rU/img/qstash-dlq/dlq.png?fit=max&auto=format&n=pqZtv0gXFMQuy8rU&q=85&s=1db8b3071c6c2c5081b72b3af8ae308c" data-og-width="1766" width="1766" data-og-height="754" height="754" data-path="img/qstash-dlq/dlq.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/pqZtv0gXFMQuy8rU/img/qstash-dlq/dlq.png?w=280&fit=max&auto=format&n=pqZtv0gXFMQuy8rU&q=85&s=61d0988d24307fa3cd18e92bbdc8ea3c 280w, https://mintcdn.com/upstash/pqZtv0gXFMQuy8rU/img/qstash-dlq/dlq.png?w=560&fit=max&auto=format&n=pqZtv0gXFMQuy8rU&q=85&s=29e07e23a9bd232736824d2e7c1987ae 560w, https://mintcdn.com/upstash/pqZtv0gXFMQuy8rU/img/qstash-dlq/dlq.png?w=840&fit=max&auto=format&n=pqZtv0gXFMQuy8rU&q=85&s=7bcd4f12dad7d2b087dec72e8df6773e 840w, https://mintcdn.com/upstash/pqZtv0gXFMQuy8rU/img/qstash-dlq/dlq.png?w=1100&fit=max&auto=format&n=pqZtv0gXFMQuy8rU&q=85&s=aabf97d59621bd4e4ff30dd0752f6f49 1100w, https://mintcdn.com/upstash/pqZtv0gXFMQuy8rU/img/qstash-dlq/dlq.png?w=1650&fit=max&auto=format&n=pqZtv0gXFMQuy8rU&q=85&s=5d733a24f42737e1abdb415f88d9cb36 1650w, https://mintcdn.com/upstash/pqZtv0gXFMQuy8rU/img/qstash-dlq/dlq.png?w=2500&fit=max&auto=format&n=pqZtv0gXFMQuy8rU&q=85&s=d142326784affec2a50f680cd44bc6d9 2500w" />
</Frame>

1. **Retry** - Republish the message and remove it from the dead letter queue. Republished messages are just like any other message and will be retried automatically if they fail.
2. **Delete** - Delete the message from the dead letter queue.

## Limitations

Dead letter queues are subject only to a retention period that depends on your plan. Messages are deleted when their retention period expires. See the “Max DLQ Retention” row on the [QStash Pricing](https://upstash.com/pricing/qstash) page.
