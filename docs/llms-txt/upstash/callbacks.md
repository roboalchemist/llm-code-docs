# Source: https://upstash.com/docs/qstash/features/callbacks.md

# Callbacks

All serverless function providers have a maximum execution time for each
function. Usually you can extend this time by paying more, but it's still
limited. QStash provides a way to go around this problem by using callbacks.

## What is a callback?

A callback allows you to call a long running function without having to wait for
its response. Instead of waiting for the request to finish, you can add a
callback url to your published message and when the request finishes, we will
call your callback URL with the response.

<img className="block h-32 dark:hidden" src="https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/callbacks.png?fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=9f0250ec6be5fab7f0725ca9414f3625" data-og-width="1952" width="1952" data-og-height="472" height="472" data-path="img/qstash/callbacks.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/callbacks.png?w=280&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=a32bb193cbff8a0990c757242ee8697d 280w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/callbacks.png?w=560&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=79f97f7832a197bbd6ca1658b67ce2fb 560w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/callbacks.png?w=840&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=d520b1a4e7778180056e5b5582b563b2 840w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/callbacks.png?w=1100&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=fad37f01afe4c1541754d060b9f9ece4 1100w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/callbacks.png?w=1650&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=fd84f5d263fb7b41d7806694dc740f41 1650w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/callbacks.png?w=2500&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=aee3cf71eb58efd7bbc0e21f2df41b03 2500w" />

<img className="hidden h-40 dark:block" src="https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/callback_dark.png?fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=c8ff0fd52e8896e529a79a776d69ff7a" data-og-width="2234" width="2234" data-og-height="725" height="725" data-path="img/qstash/callback_dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/callback_dark.png?w=280&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=c778a32a111846209dd953c0d41d5266 280w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/callback_dark.png?w=560&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=26b194dab1855728225776b631d5bee3 560w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/callback_dark.png?w=840&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=9767654e2a9d70b5320a442b11eb2710 840w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/callback_dark.png?w=1100&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=008355a069975305e80db9201aebf87c 1100w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/callback_dark.png?w=1650&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=b38d815bfa5003644179436b6ec7915c 1650w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/callback_dark.png?w=2500&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=b3219b39dac8894ba457e200eb32eac3 2500w" />

1. You publish a message to QStash using the `/v2/publish` endpoint
2. QStash will enqueue the message and deliver it to the destination
3. QStash waits for the response from the destination
4. When the response is ready, QStash calls your callback URL with the response

Callbacks publish a new message with the response to the callback URL. Messages
created by callbacks are charged as any other message.

## How do I use Callbacks?

You can add a callback url in the `Upstash-Callback` header when publishing a
message. The value must be a valid URL.

<CodeGroup>
  ```bash cURL theme={"system"}
  curl -X POST \
    https://qstash.upstash.io/v2/publish/https://my-api... \
    -H 'Content-Type: application/json' \
    -H 'Authorization: Bearer <QSTASH_TOKEN>' \
    -H 'Upstash-Callback: <CALLBACK_URL>' \
    -d '{ "hello": "world" }'
  ```

  ```typescript Typescript theme={"system"}
  import { Client } from "@upstash/qstash";

  const client = new Client({ token: "<QSTASH_TOKEN>" });
  const res = await client.publishJSON({
    url: "https://my-api...",
    body: { hello: "world" },
    callback: "https://my-callback...",
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
      callback="https://my-callback...",
  )
  ```
</CodeGroup>

The callback body sent to you will be a JSON object with the following fields:

```json  theme={"system"}
{
  "status": 200,
  "header": { "key": ["value"] },         // Response header
  "body": "YmFzZTY0IGVuY29kZWQgcm9keQ==", // base64 encoded response body
  "retried": 2,                           // How many times we retried to deliver the original message
  "maxRetries": 3,                        // Number of retries before the message assumed to be failed to delivered.
  "sourceMessageId": "msg_xxx",           // The ID of the message that triggered the callback
  "topicName": "myTopic",                 // The name of the URL Group (topic) if the request was part of a URL Group
  "endpointName": "myEndpoint",           // The endpoint name if the endpoint is given a name within a topic
  "url": "http://myurl.com",              // The destination url of the message that triggered the callback
  "method": "GET",                        // The http method of the message that triggered the callback
  "sourceHeader": { "key": "value" },     // The http header of the message that triggered the callback
  "sourceBody": "YmFzZTY0kZWQgcm9keQ==",  // The base64 encoded body of the message that triggered the callback
  "notBefore": "1701198458025",           // The unix timestamp of the message that triggered the callback is/will be delivered in milliseconds
  "createdAt": "1701198447054",           // The unix timestamp of the message that triggered the callback is created in milliseconds
  "scheduleId": "scd_xxx",                // The scheduleId of the message if the message is triggered by a schedule
  "callerIP": "178.247.74.179"            // The IP address where the message that triggered the callback is published from
}
```

In Next.js you could use the following code to handle the callback:

```js  theme={"system"}
// pages/api/callback.js

import { verifySignature } from "@upstash/qstash/nextjs";

function handler(req, res) {
  // responses from qstash are base64-encoded
  const decoded = atob(req.body.body);
  console.log(decoded);

  return res.status(200).end();
}

export default verifySignature(handler);

export const config = {
  api: {
    bodyParser: false,
  },
};
```

We may truncate the response body if it exceeds your plan limits. You can check
your `Max Message Size` in the
[console](https://console.upstash.com/qstash?tab=details).

Make sure you verify the authenticity of the callback request made to your API
by
[verifying the signature](/qstash/features/security/#request-signing-optional).

# What is a Failure-Callback?

Failure callbacks are similar to callbacks but they are called only when all the retries are exhausted and still
the message can not be delivered to the given endpoint.

This is designed to be an serverless alternative to [List messages to DLQ](/qstash/api/dlq/listMessages).

You can add a failure callback URL in the `Upstash-Failure-Callback` header when publishing a
message. The value must be a valid URL.

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

The callback body sent to you will be a JSON object with the following fields:

```json  theme={"system"}
{
  "status": 400,
  "header": { "key": ["value"] },         // Response header
  "body": "YmFzZTY0IGVuY29kZWQgcm9keQ==", // base64 encoded response body
  "retried": 3,                           // How many times we retried to deliver the original message
  "maxRetries": 3,                        // Number of retries before the message assumed to be failed to delivered.
  "dlqId": "1725323658779-0",             // Dead Letter Queue id. This can be used to retrieve/remove the related message from DLQ.
  "sourceMessageId": "msg_xxx",           // The ID of the message that triggered the callback
  "topicName": "myTopic",                 // The name of the URL Group (topic) if the request was part of a topic
  "endpointName": "myEndpoint",           // The endpoint name if the endpoint is given a name within a topic
  "url": "http://myurl.com",              // The destination url of the message that triggered the callback
  "method": "GET",                        // The http method of the message that triggered the callback
  "sourceHeader": { "key": "value" },     // The http header of the message that triggered the callback
  "sourceBody": "YmFzZTY0kZWQgcm9keQ==",  // The base64 encoded body of the message that triggered the callback
  "notBefore": "1701198458025",           // The unix timestamp of the message that triggered the callback is/will be delivered in milliseconds
  "createdAt": "1701198447054",           // The unix timestamp of the message that triggered the callback is created in milliseconds
  "scheduleId": "scd_xxx",                // The scheduleId of the message if the message is triggered by a schedule
  "callerIP": "178.247.74.179"            // The IP address where the message that triggered the callback is published from
}
```

You can also use a callback and failureCallback together!

## Configuring Callbacks

Publishes/enqueues for callbacks can also be configured with the same HTTP headers that are used to configure direct publishes/enqueues.

<Tip> You can refer to headers that are used to configure `publishes` [here](/qstash/api/publish) and for `enqueues`
[here](/qstash/api/enqueue) </Tip>

Instead of the `Upstash` prefix for headers, the `Upstash-Callback`/`Upstash-Failure-Callback` prefix can be used to configure callbacks as follows:

```
Upstash-Callback-Timeout 
Upstash-Callback-Retries
Upstash-Callback-Delay 
Upstash-Callback-Method 
Upstash-Failure-Callback-Timeout 
Upstash-Failure-Callback-Retries
Upstash-Failure-Callback-Delay
Upstash-Failure-Callback-Method
```

You can also forward headers to your callback endpoints as follows:

```
Upstash-Callback-Forward-MyCustomHeader 
Upstash-Failure-Callback-Forward-MyCustomHeader  
```
