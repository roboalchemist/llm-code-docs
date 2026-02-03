# Source: https://upstash.com/docs/workflow/getstarted.md

# Source: https://upstash.com/docs/vector/overall/getstarted.md

# Source: https://upstash.com/docs/search/overall/getstarted.md

# Source: https://upstash.com/docs/redis/sdks/ts/getstarted.md

# Source: https://upstash.com/docs/redis/overall/getstarted.md

# Source: https://upstash.com/docs/qstash/overall/getstarted.md

> ## Documentation Index
> Fetch the complete documentation index at: https://upstash.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Getting Started

QStash is a **serverless messaging and scheduling solution**. It fits easily into your existing workflow and allows you to build reliable systems without managing infrastructure.

Instead of calling an endpoint directly, QStash acts as a middleman between you and an API to guarantee delivery, perform automatic retries on failure, and more.

<Frame>
  <img src="https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/qstash-benefits.png?fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=a49cf2890891033348a5493f7c299762" data-og-width="1920" width="1920" data-og-height="1080" height="1080" data-path="img/qstash/qstash-benefits.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/qstash-benefits.png?w=280&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=4d44a587b83b5b388afa187f97eb7fa3 280w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/qstash-benefits.png?w=560&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=e81daccf4cbbc98af3ce1a941dfeea32 560w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/qstash-benefits.png?w=840&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=8bb628a3e84bdd997685a3e33d49db16 840w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/qstash-benefits.png?w=1100&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=5924aa1542968662d0300c025baff453 1100w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/qstash-benefits.png?w=1650&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=4a6eb0397de0769fab6c4fbff8e2be50 1650w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/qstash-benefits.png?w=2500&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=b3060b417eb7928821a5a4149bdc3ee7 2500w" />
</Frame>

<Tip href="/workflow/getstarted">
  We have a new SDK called [Upstash Workflow](/workflow/getstarted).

  **Upstash Workflow SDK** is **QStash** simplified for your complex applications

  * Skip the details of preparing a complex dependent endpoints.
  * Focus on the essential parts.
  * Enjoy automatic retries and delivery guarantees.
  * Avoid platform-specific timeouts.

  Check out [Upstash Workflow Getting Started](/workflow/getstarted) for more.
</Tip>

## Quick Start

Check out these Quick Start guides to get started with QStash in your application.

<CardGroup cols={2}>
  <Card title="Next.js" icon="node-js" href="/qstash/quickstarts/vercel-nextjs">
    Build a Next application that uses QStash to start a long-running job on your platform
  </Card>

  <Card title="Python" icon="python" href="/qstash/quickstarts/python-vercel">
    Build a Python application that uses QStash to schedule a daily job that clean up a database
  </Card>
</CardGroup>

Or continue reading to learn how to send your first message!

## Send your first message

<Check>
  **Prerequisite**

  You need an Upstash account before publishing messages, create one
  [here](https://console.upstash.com).
</Check>

### Public API

Make sure you have a publicly available HTTP API that you want to send your
messages to. If you don't, you can use something like
[requestcatcher.com](https://requestcatcher.com/), [webhook.site](https://webhook.site/) or
[webhook-test.com](https://webhook-test.com/) to try it out.

For example, you can use this URL to test your messages: [https://firstqstashmessage.requestcatcher.com](https://firstqstashmessage.requestcatcher.com)

### Get your token

Go to the [Upstash Console](https://console.upstash.com/qstash) and copy the
`QSTASH_TOKEN`.

<Frame>
  <img src="https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/rest_token.png?fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=b0bda5d8c30d60c36bcaaf49accce9b1" data-og-width="1090" width="1090" data-og-height="402" height="402" data-path="img/qstash/rest_token.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/rest_token.png?w=280&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=ad32156275de5c4b5c17f8351d03dfd7 280w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/rest_token.png?w=560&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=2b05f661b26af08e75cb7bd29b94530a 560w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/rest_token.png?w=840&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=c7b6ff4e398e7adff1f6901c991f4c92 840w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/rest_token.png?w=1100&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=c8b639fac03f93107b378b3699c55803 1100w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/rest_token.png?w=1650&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=18008b9741588917fd62e0efe903be95 1650w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/rest_token.png?w=2500&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=245f6b9806e7b523b8a4a2ace3dad5c2 2500w" />
</Frame>

### Publish a message

A message can be any shape or form: json, xml, binary, anything, that can be
transmitted in the http request body. We do not impose any restrictions other
than a size limit of 1 MB (which can be customized at your request).

In addition to the request body itself, you can also send HTTP headers. Learn
more about this in the [message publishing section](/qstash/howto/publishing).

<CodeGroup>
  ```bash cURL theme={"system"}
  curl -XPOST \
      -H 'Authorization: Bearer <QSTASH_TOKEN>' \
      -H "Content-type: application/json" \
      -d '{ "hello": "world" }' \
      'https://qstash.upstash.io/v2/publish/https://<your-api-url>'
  ```

  ```bash cURL RequestCatcher theme={"system"}
  curl -XPOST \
      -H 'Authorization: Bearer <QSTASH_TOKEN>' \
      -H "Content-type: application/json" \
      -d '{ "hello": "world" }' \
      'https://qstash.upstash.io/v2/publish/https://firstqstashmessage.requestcatcher.com/test'
  ```
</CodeGroup>

Don't worry, we have SDKs for different languages so you don't
have to make these requests manually.

### Check Response

You should receive a response with a unique message ID.

<Frame>
  <img src="https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/reqcatcher.png?fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=f68c3043856bf77c5e55786a54d57cd7" data-og-width="1456" width="1456" data-og-height="580" height="580" data-path="img/qstash/reqcatcher.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/reqcatcher.png?w=280&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=84c76a371ea1a6af224a61c7897176e4 280w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/reqcatcher.png?w=560&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=337d1aa2277b60b314a69122ba24bfa0 560w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/reqcatcher.png?w=840&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=f8d5a20e4e1a735bb579791f474d891b 840w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/reqcatcher.png?w=1100&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=2fcbc86f518555b08b306ff0d4c64045 1100w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/reqcatcher.png?w=1650&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=f5f8791bc3df089e26bac1e742505b9c 1650w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/reqcatcher.png?w=2500&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=26a972e97932d8f03f8183da39996063 2500w" />
</Frame>

### Check Message Status

Head over to [Upstash Console](https://console.upstash.com/qstash) and go to the
`Logs` tab where you can see your message activities.

<Frame>
  <img src="https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/log.png?fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=beb5fcdfa587a89b438d2db22938f6df" data-og-width="2026" width="2026" data-og-height="660" height="660" data-path="img/qstash/log.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/log.png?w=280&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=acfc44f8f71fec5480334c50076ba5f6 280w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/log.png?w=560&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=46be420ad548bc8d1549ac4eb572ad46 560w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/log.png?w=840&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=506308270b92f95e63fb412cb14835ca 840w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/log.png?w=1100&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=b51df20dcd9047a2f1c8043db306e1b1 1100w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/log.png?w=1650&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=5482ee85fa85b78af2d8eab873024a00 1650w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/log.png?w=2500&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=3800e49a97e6c19fcdadef691c25dcd9 2500w" />
</Frame>

Learn more about different states [here](/qstash/howto/debug-logs).

## Features and Use Cases

<CardGroup cols={2}>
  <Card title="Background Jobs" icon="share-all" href="/qstash/features/background-jobs">
    Run long-running tasks in the background, without blocking your application
  </Card>

  <Card title="Schedules" icon="calendar-days" href="/qstash/features/schedules">
    Schedule messages to be delivered at a time in the future
  </Card>

  <Card title="Fan out" icon="arrows-maximize" href="/qstash/features/url-groups">
    Publish messages to multiple endpoints, in parallel, using URL Groups
  </Card>

  <Card title="FIFO" icon="right-left" href="/qstash/features/queues#ordered-delivery">
    Enqueue messages to be delivered one by one in the order they have enqueued.
  </Card>

  <Card title="Flow Control" icon="arrows-up-to-line" href="/qstash/features/flowcontrol">
    Custom rate per second and parallelism limits to avoid overflowing your endpoint.
  </Card>

  <Card title="Callbacks" icon="phone" href="/qstash/features/callbacks">
    Get a response delivered to your API when a message is delivered
  </Card>

  <Card title="Retry Failed Jobs" icon="repeat" href="/qstash/features/dlq">
    Use a Dead Letter Queue to have full control over failed messages
  </Card>

  <Card title="Deduplication" icon="copy" href="/qstash/features/deduplication">
    Prevent duplicate messages from being delivered
  </Card>

  <Card title="LLM Integrations" icon="shapes" href="/qstash/integrations/llm">
    Publish, enqueue, or batch chat completion requests using large language models with QStash
    features.
  </Card>
</CardGroup>
