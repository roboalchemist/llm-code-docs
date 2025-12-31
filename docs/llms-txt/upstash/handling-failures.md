# Source: https://upstash.com/docs/qstash/howto/handling-failures.md

# Handling Failures

Sometimes, endpoints fail due to various reasons such as network issues or server issues.
In such cases, QStash offers a few options to handle these failures.

## Failure Callbacks

When publishing a message, you can provide a failure callback that will be called if the message fails to be published.
You can read more about callbacks [here](/qstash/features/callbacks).

With the failure callback, you can add custom logic such as logging the failure or sending an alert to the team.
Once you handle the failure, you can [delete it from the dead letter queue](/qstash/api/dlq/deleteMessage).

<CodeGroup>
  ```bash cURL theme={"system"}
  curl -X POST \
    https://qstash.upstash.io/v2/publish/<DESTINATION_URL> \
    -H 'Content-Type: application/json' \
    -H 'Authorization: Bearer <QSTASH_TOKEN>' \
    -H 'Upstash-Failure-Callback: <CALLBACK_URL>' \
    -d '{ "hello": "world" }'
  ```

  ```typescript Typescript theme={"system"}
  import { Client } from "@upstash/qstash";

  const client = new Client({ token: "<QSTASH_TOKEN>" });
  const res = await client.publishJSON({
    url: "https://my-api...",
    body: { hello: "world" },
    failureCallback: "https://my-callback...",
  });
  ```

  ```python Python theme={"system"}
  from qstash import QStash

  client = QStash("<QSTASH_TOKEN>")
  client.message.publish_json(
      url="https://my-api...",
      body={
          "hello": "world",
      },
      failure_callback="https://my-callback...",
  )
  ```
</CodeGroup>

## Dead Letter Queue

If you don't want to handle the failure immediately, you can use the dead letter queue (DLQ) to store the failed messages.
You can read more about the dead letter queue [here](/qstash/features/dlq).

Failed messages are automatically moved to the dead letter queue upon failure, and can be retried from the console or
the API by [retrieving the message](/qstash/api/dlq/getMessage) then [publishing it](/qstash/api/publish).

<Frame>
  <img src="https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/dlq-console.png?fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=19f34bc4484b4d6b8542e4d0a439409a" alt="DLQ from console" data-og-width="2064" width="2064" data-og-height="1302" height="1302" data-path="img/qstash/dlq-console.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/dlq-console.png?w=280&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=b64d919c6f58b24416bf0c2abba5f197 280w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/dlq-console.png?w=560&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=5049e7623f66b16e8517545a7c2780db 560w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/dlq-console.png?w=840&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=5c6ae4279cd00f1c77e16449e01ed3e4 840w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/dlq-console.png?w=1100&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=47fccebcd8c9f50452799d5857d20aac 1100w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/dlq-console.png?w=1650&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=1dadf8ad6af4713f9e900a28d5cd5c45 1650w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/dlq-console.png?w=2500&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=2ede823dab238e7043f605df32a9aa6f 2500w" />
</Frame>
