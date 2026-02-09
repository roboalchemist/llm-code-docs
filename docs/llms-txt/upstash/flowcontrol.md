# Source: https://upstash.com/docs/qstash/features/flowcontrol.md

> ## Documentation Index
> Fetch the complete documentation index at: https://upstash.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Flow Control

FlowControl enables you to limit the number of messages sent to your endpoint via delaying the delivery.
There are two limits that you can set with the FlowControl feature: [Rate](#rate-limit) and [Parallelism](#parallelism-limit).
And if needed both parameters can be [combined](#rate-and-parallelism-together).

For the `FlowControl`, you need to choose a key first. This key is used to count the number of calls made to your endpoint.

There are not limits to number of keys you can use.

<Warning>
  The rate/parallelism limits are not applied per `url`, they are applied per `Flow-Control-Key`.
</Warning>

<Warning>
  Keep in mind that rate/period and parallelism info are kept on each publish separately. That means
  if you change the rate/period or parallelism on a new publish, the old fired ones will not be affected. They will keep their flowControl config.
  During the period that old `publishes` has not delivered but there are also the `publishes` with the new rates, QStash will effectively allow
  the highest rate/period or highest parallelism. Eventually(after the old publishes are delivered), the new rate/period and parallelism will be used.
</Warning>

## Rate and Period Parameters

The `rate` parameter specifies the maximum number of calls allowed within a given period. The `period` parameter allows you to specify the time window over which the rate limit is enforced. By default, the period is set to 1 second, but you can adjust it to control how frequently calls are allowed. For example, you can set a rate of 10 calls per minute as follows:

<CodeGroup>
  ```typescript TypeScript theme={"system"}
  const client = new Client({ token: "<QSTASH_TOKEN>" });

  await client.publishJSON({
      url: "https://example.com",
      body: { hello: "world" },
      flowControl: { key: "USER_GIVEN_KEY", rate: 10, period: "1m" },
  });
  ```

  ```bash cURL theme={"system"}
  curl -XPOST -H 'Authorization: Bearer XXX' \
              -H "Content-type: application/json" \
              -H "Upstash-Flow-Control-Key:USER_GIVEN_KEY"  \
              -H "Upstash-Flow-Control-Value:rate=10,period=1m" \
             'https://qstash.upstash.io/v2/publish/https://example.com' \
              -d '{"message":"Hello, World!"}'
  ```
</CodeGroup>

## Parallelism Limit

The parallelism limit is the number of calls that can be active at the same time.
Active means that the call is made to your endpoint and the response is not received yet.

You can set the parallelism limit to 10 calls active at the same time as follows:

<CodeGroup>
  ```typescript TypeScript theme={"system"}
  const client = new Client({ token: "<QSTASH_TOKEN>" });

  await client.publishJSON({
      url: "https://example.com",
      body: { hello: "world" },
      flowControl: { key: "USER_GIVEN_KEY", parallelism: 10 },
  });
  ```

  ```bash cURL theme={"system"}
  curl -XPOST -H 'Authorization: Bearer XXX' \
              -H "Content-type: application/json" \
              -H "Upstash-Flow-Control-Key:USER_GIVEN_KEY"  \
              -H "Upstash-Flow-Control-Value:parallelism=10" \
             'https://qstash.upstash.io/v2/publish/https://example.com' \ 
              -d '{"message":"Hello, World!"}'
  ```
</CodeGroup>

You can also use the Rest API to get information how many messages waiting for parallelism limit.
See the [API documentation](/qstash/api/flow-control/get) for more details.

## Rate, Parallelism, and Period Together

All three parameters can be combined. For example, with a rate of 10 per minute, parallelism of 20, and a period of 1 minute, QStash will trigger 10 calls in the first minute and another 10 in the next. Since none of them will have finished, the system will wait until one completes before triggering another.

<CodeGroup>
  ```typescript TypeScript theme={"system"}
  const client = new Client({ token: "<QSTASH_TOKEN>" });

  await client.publishJSON({
      url: "https://example.com",
      body: { hello: "world" },
      flowControl: { key: "USER_GIVEN_KEY", rate: 10, parallelism: 20, period: "1m" },
  });
  ```

  ```bash cURL theme={"system"}
  curl -XPOST -H 'Authorization: Bearer XXX' \
              -H "Content-type: application/json" \
              -H "Upstash-Flow-Control-Key:USER_GIVEN_KEY"  \
              -H "Upstash-Flow-Control-Value:rate=10,parallelism=20,period=1m" \
             'https://qstash.upstash.io/v2/publish/https://example.com' \
              -d '{"message":"Hello, World!"}'
  ```
</CodeGroup>

## Monitor

You can monitor wait list size of your flow control key's from the console `FlowControl` tab.

<Frame>
  <img src="https://mintcdn.com/upstash/l4MDSLdJz3ZGZA7P/img/qstash/flowcontrol.png?fit=max&auto=format&n=l4MDSLdJz3ZGZA7P&q=85&s=db5e5b7c27ecb7544a0b8f8b507c8fa1" data-og-width="2096" width="2096" data-og-height="742" height="742" data-path="img/qstash/flowcontrol.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/l4MDSLdJz3ZGZA7P/img/qstash/flowcontrol.png?w=280&fit=max&auto=format&n=l4MDSLdJz3ZGZA7P&q=85&s=199d2c52e7026c76844cea2bd7567353 280w, https://mintcdn.com/upstash/l4MDSLdJz3ZGZA7P/img/qstash/flowcontrol.png?w=560&fit=max&auto=format&n=l4MDSLdJz3ZGZA7P&q=85&s=13b8527108acf683db323ba6ccd7a159 560w, https://mintcdn.com/upstash/l4MDSLdJz3ZGZA7P/img/qstash/flowcontrol.png?w=840&fit=max&auto=format&n=l4MDSLdJz3ZGZA7P&q=85&s=465c0081b3daae785f3bbf9c09bb230c 840w, https://mintcdn.com/upstash/l4MDSLdJz3ZGZA7P/img/qstash/flowcontrol.png?w=1100&fit=max&auto=format&n=l4MDSLdJz3ZGZA7P&q=85&s=5ac4b509b8c4965327a9897838327954 1100w, https://mintcdn.com/upstash/l4MDSLdJz3ZGZA7P/img/qstash/flowcontrol.png?w=1650&fit=max&auto=format&n=l4MDSLdJz3ZGZA7P&q=85&s=9a2e227175179517625160bda083caf9 1650w, https://mintcdn.com/upstash/l4MDSLdJz3ZGZA7P/img/qstash/flowcontrol.png?w=2500&fit=max&auto=format&n=l4MDSLdJz3ZGZA7P&q=85&s=3aea93b2f317bcc6c0302ef675aa1cb9 2500w" />
</Frame>

Also you can get the same info using the REST API.

* [List All Flow Control Keys](/qstash/api/flow-control/list).
* [Single Flow Control Key](/qstash/api/flow-control/get).
