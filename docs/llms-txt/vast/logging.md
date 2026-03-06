# Source: https://docs.vast.ai/documentation/serverless/logging.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.vast.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Endpoint and Worker Logs

> Learn how to access Vast serverless logs

<script
  type="application/ld+json"
  dangerouslySetInnerHTML={{
__html: JSON.stringify({
  "@context": "https://schema.org",
  "@type": "TechArticle",
  "headline": "Vast.ai Endpoint and Worker Logs",
  "description": "Learn how to access endpoint and worker logs in Vast.ai serverless, including where to find them and how to retain them for debugging.",
  "author": {
    "@type": "Organization",
    "name": "Vast.ai"
  },
  "articleSection": "Serverless Documentation",
  "keywords": ["endpoint logs", "worker logs", "serverless", "vast.ai", "debugging", "CLI", "UI"]
})
}}
/>

Endpoint and worker logs provide real-time visibility into the behavior of your serverless infrastructure. These logs are primarily intended for debugging issues with endpoints, workergroups, and individual workers.

## Endpoint Logs

Endpoint logs are available under the **"All Workergroups"** tab in the Serverless endpoint, within the Vast console UI.

<Frame caption="Endpoint Log">
    <img src="https://mintcdn.com/vastai-80aa3a82/HhcLrgFHfoqC6U00/images/endpoint-log.webp?fit=max&auto=format&n=HhcLrgFHfoqC6U00&q=85&s=9f265707a2ca86afd1aef979d36c2f11" alt="Endpoint Log" data-og-width="2311" width="2311" data-og-height="1214" height="1214" data-path="images/endpoint-log.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/vastai-80aa3a82/HhcLrgFHfoqC6U00/images/endpoint-log.webp?w=280&fit=max&auto=format&n=HhcLrgFHfoqC6U00&q=85&s=d9d623e2d99e7237cfc5a4ae726be46d 280w, https://mintcdn.com/vastai-80aa3a82/HhcLrgFHfoqC6U00/images/endpoint-log.webp?w=560&fit=max&auto=format&n=HhcLrgFHfoqC6U00&q=85&s=8d11daebae20bd848fdd7224dd73d45a 560w, https://mintcdn.com/vastai-80aa3a82/HhcLrgFHfoqC6U00/images/endpoint-log.webp?w=840&fit=max&auto=format&n=HhcLrgFHfoqC6U00&q=85&s=21ff49d08db2d26dea8c000cd51778a8 840w, https://mintcdn.com/vastai-80aa3a82/HhcLrgFHfoqC6U00/images/endpoint-log.webp?w=1100&fit=max&auto=format&n=HhcLrgFHfoqC6U00&q=85&s=c68cd06dd623604c3f68b3d2dce1ff46 1100w, https://mintcdn.com/vastai-80aa3a82/HhcLrgFHfoqC6U00/images/endpoint-log.webp?w=1650&fit=max&auto=format&n=HhcLrgFHfoqC6U00&q=85&s=27361a29514f4f233feb56d389f987e7 1650w, https://mintcdn.com/vastai-80aa3a82/HhcLrgFHfoqC6U00/images/endpoint-log.webp?w=2500&fit=max&auto=format&n=HhcLrgFHfoqC6U00&q=85&s=77964f2fb0d81919c4f5cef272462e11 2500w" />
</Frame>

These logs include low-level details about scaling decisions made by the serverless engine. They are useful for understanding how the system responds to traffic and workload changes, and include:

* Summarized performance for all workers and workergroups
* Measured and estimated performance and worker load
* Marketplace offer details used in worker recruitment

## Worker Logs

Worker logs are accessible on a per-worker basis. To view worker logs, navigate to the serverless endpoint in question and click on this icon next to the worker.

<Frame caption="Worker Log">
    <img src="https://mintcdn.com/vastai-80aa3a82/i_2h4PucC2hksc2Z/images/worker-log.webp?fit=max&auto=format&n=i_2h4PucC2hksc2Z&q=85&s=c23a399b722c512c2f2fb6903204d33f" alt="Worker Log" data-og-width="4308" width="4308" data-og-height="771" height="771" data-path="images/worker-log.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/vastai-80aa3a82/i_2h4PucC2hksc2Z/images/worker-log.webp?w=280&fit=max&auto=format&n=i_2h4PucC2hksc2Z&q=85&s=e6e25ffbfd455528e1f14852b37b73a0 280w, https://mintcdn.com/vastai-80aa3a82/i_2h4PucC2hksc2Z/images/worker-log.webp?w=560&fit=max&auto=format&n=i_2h4PucC2hksc2Z&q=85&s=7493e2b5695e4d78254d2d496ecf7326 560w, https://mintcdn.com/vastai-80aa3a82/i_2h4PucC2hksc2Z/images/worker-log.webp?w=840&fit=max&auto=format&n=i_2h4PucC2hksc2Z&q=85&s=c423cfe6eabfbc7b5ba708651f407b5f 840w, https://mintcdn.com/vastai-80aa3a82/i_2h4PucC2hksc2Z/images/worker-log.webp?w=1100&fit=max&auto=format&n=i_2h4PucC2hksc2Z&q=85&s=eb0a33ca9b94087b5b73be4e4e9d40c1 1100w, https://mintcdn.com/vastai-80aa3a82/i_2h4PucC2hksc2Z/images/worker-log.webp?w=1650&fit=max&auto=format&n=i_2h4PucC2hksc2Z&q=85&s=d32c4b37ff44f25fa6a0c5fc080bcc73 1650w, https://mintcdn.com/vastai-80aa3a82/i_2h4PucC2hksc2Z/images/worker-log.webp?w=2500&fit=max&auto=format&n=i_2h4PucC2hksc2Z&q=85&s=8dea4789da2549c2ecc821165b9eee4f 2500w" />
</Frame>

Worker logs provide detailed runtime output for individual workers, helping you debug model loading, request handling, container behavior, and other worker-specific events.

## Log Characteristics and Retention

* Logs are **streaming outputs**, typically only a few seconds behind real-time.
* Logs are **not permanently maintained** and are intended for near real-time debugging of issues.
* Users who need longer retention should **periodically download logs** to store them externally.

## Accessing Logs Through the CLI

In addition to accessing these logs through the UI, you can use the vastai CLI to check endpoint and worker group logs at different log levels (level 0 is the highest detail, level 3 the lowest).

## Endpoint logs

```cli CLI Command theme={null}
vastai get endpt-logs <endpoint_id> --level (0-3)
```

## Workergroup logs

```cli CLI Command theme={null}
vastai get wrkgrp-logs <worker_group_id> --level (0-3)
```
