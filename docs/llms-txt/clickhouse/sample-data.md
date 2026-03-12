# Source: https://clickhouse.ferndocs.com/click-stack/use-cases/observability/clickstack/getting-started/sample-data.md

---
slug: /use-cases/observability/clickstack/getting-started/sample-data
title: 'Sample Logs, Traces and Metrics'
sidebar_position: 0
pagination_prev: null
pagination_next: null
description: >-
  Getting started with ClickStack and a sample dataset with logs, sessions,
  traces and metrics
doc_type: guide
keywords:

- clickstack
- example data
- sample dataset
- logs
- observability

---

The following example assumes you have started ClickStack using the [instructions for the all-in-one image](/use-cases/observability/clickstack/getting-started) and connected to the [local ClickHouse instance](/use-cases/observability/clickstack/getting-started#complete-connection-credentials) or a [ClickHouse Cloud instance](/use-cases/observability/clickstack/getting-started#create-a-cloud-connection).

<Note title="HyperDX in ClickHouse Cloud">
This sample dataset can also be used with HyperDX in ClickHouse Cloud, with only minor adjustments to the flow as noted. If using HyperDX in ClickHouse Cloud, users will require an Open Telemetry collector to be running locally as described in the [getting started guide for this deployment model](/use-cases/observability/clickstack/deployment/hyperdx-clickhouse-cloud).
</Note>

<Steps>

## Navigate to the HyperDX UI [#navigate-to-the-hyperdx-ui]

Visit [http://localhost:8080](http://localhost:8080) to access the HyperDX UI if deploying locally. If using HyperDX in ClickHouse Cloud, select your service and `HyperDX` from the left menu.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/922d0d3fd2706b8e445d01dd59a64cf5aea5bc3693dd78e22937ea83794172ce/images/use-cases/observability/hyperdx.png" alt="HyperDX UI"/>

## Copy ingestion API key [#copy-ingestion-api-key]

<Note title="HyperDX in ClickHouse Cloud">
This step is not required if using HyperDX in ClickHouse Cloud, where ingestion key support is not currently supported.
</Note>

Navigate to [`Team Settings`](http://localhost:8080/team) and copy the `Ingestion API Key` from the `API Keys` section. This API key ensures data ingestion through the OpenTelemetry collector is secure.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/960820e8a6d33058d00b27f8d0f4c69ffdbc7e19466ea47c0fdf2af873647e8d/images/use-cases/observability/copy_api_key.png" alt="Copy API key"/>

## Download sample data [#download-sample-data]

In order to populate the UI with sample data, download the following file:

[Sample data](https://storage.googleapis.com/hyperdx/sample.tar.gz)

```shell
# curl
curl -O https://storage.googleapis.com/hyperdx/sample.tar.gz
# or
# wget https://storage.googleapis.com/hyperdx/sample.tar.gz
```

This file contains example logs, metrics, and traces from our public [OpenTelemetry demo](https://github.com/ClickHouse/opentelemetry-demo) - a simple e-commerce store with microservices. Copy this file to a directory of your choosing.

## Load sample data [#load-sample-data]

To load this data, we simply send it to the HTTP endpoint of the deployed OpenTelemetry (OTel) collector.

First, export the API key copied above.

<Note title="HyperDX in ClickHouse Cloud">
This step is not required if using HyperDX in ClickHouse Cloud, where ingestion key support is not currently supported.
</Note>

```shell
# export API key
export CLICKSTACK_API_KEY=<YOUR_INGESTION_API_KEY>
```

Run the following command to send the data to the OTel collector:

```shell
for filename in $(tar -tf sample.tar.gz); do
  endpoint="http://localhost:4318/v1/${filename%.json}"
  echo "loading ${filename%.json}"
  tar -xOf sample.tar.gz "$filename" | while read -r line; do
    printf '%s\n' "$line" | curl -s -o /dev/null -X POST "$endpoint" \
    -H "Content-Type: application/json" \
    -H "authorization: ${CLICKSTACK_API_KEY}" \
    --data-binary @-
  done
done
```

This simulates OTLP log, trace, and metric sources sending data to the OTel collector. In production, these sources may be language clients or even other OTel collectors.

Returning to the `Search` view, you should see that data has started to load (adjust the time frame to the `Last 1 hour` if the data does not render):

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/98bb4ee425a2fd371e91e4a8b142ce21e1637f6bda6d5a90ff34935c035e1601/images/use-cases/observability/hyperdx-10.png" alt="HyperDX search"/>

Data loading will take a few minutes. Allow for the load to be completed before progressing to the next steps.

## Explore sessions [#explore-sessions]

Suppose we have reports that our users are experiencing issues paying for goods. We can view their experience using HyperDX's session replay capabilities.

Select [`Client Sessions`](http://localhost:8080/sessions?from=1747312320000&to=1747312920000&sessionSource=l1324572572) from the left menu.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/bcb59dca92b32b13a06090fb7d3f70610ffdca7517e8b259895ffc8785d6b635/images/use-cases/observability/hyperdx-11.png" alt="Sessions"/>

This view allows us to see front-end sessions for our e-commerce store. Sessions remain Anonymous until users check out and try to complete a purchase.

Note that some sessions with emails have an associated error, potentially confirming reports of failed transactions.

Select a trace with a failure and associated email. The subsequent view allows us to replay the user's session and review their issue. Press play to watch the session.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/b547ff6a096eb6a013dec8b24ba1d9f6bfea5162d31320e50a3d6df0c5891620/images/use-cases/observability/hyperdx-12.png" alt="Session replay"/>

The replay shows the user navigating the site, adding items to their cart. Feel free to skip to later in the session where they attempt to complete a payment.

<Tip>
Any errors are annotated on the timeline in red.
</Tip>

The user was unable to place the order, with no obvious error. Scroll to the bottom of the left panel, containing the network and console events from the user's browser. You will notice a 500 error was thrown on making a `/api/checkout` call.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/59a47a2a9cafbd43d52e0b9dcc58743b30b35b8ccfd69831cef726818b00af00/images/use-cases/observability/hyperdx-13.png" alt="Error in session"/>

Select this `500` error. Neither the `Overview` nor `Column Values` indicate the source of the issue, other than the fact the error is unexpected, causing an `Internal Error`.

## Explore traces [#explore-traces]

Navigate to the `Trace` tab to see the full distributed trace.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/57264dc8f9dfc8b3d38c0f5195843119fa3b74cea380f56a35743bdba9f7c53f/images/use-cases/observability/hyperdx-14.png" alt="Session trace"/>

Scroll down the trace to see the origin of the error - the `checkout` service span. Select the `Payment` service span.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/5639b29e0bd2c6164d1b5569c9bccd074575c5cbdeb2ad0c0a604fe26db0daba/images/use-cases/observability/hyperdx-15.png" alt="Span"/>

Select the tab `Column Values` and scroll down. We can see the issue is associated with a cache being full.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/7bbc94c66c93a045f737e2d465969c04572a175c7256f4aa5913422a05ad2e0a/images/use-cases/observability/hyperdx-16.png" alt="Column values"/>

Scrolling up and returning to the trace, we can see logs are correlated with the span, thanks to our earlier configuration. These provide further context.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/f0730f34f99a0129205bf01e6b3e10931c548991a8796509d2dbda085b8e2913/images/use-cases/observability/hyperdx-17.png" alt="Correlated log"/>

We've established that a cache is getting filled in the payment service, which is preventing payments from completing.

## Explore logs [#explore-logs]

For further details, we can return to the [`Search` view](http://localhost:8080/search):

Select `Logs` from the sources and apply a filter to the `payment` service.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/a75090ff47c833d2ecb5dd7563958edd34a86219ebfbf70c7dcca5a46065a0c6/images/use-cases/observability/hyperdx-18.png" alt="Logs"/>

We can see that while the issue is recent, the number of impacted payments is high. Furthermore, a cache related to the visa payments appears to be causing issues.

## Chart metrics [#chart-metrics]

While an error has clearly been introduced in the code, we can use metrics to confirm the cache size. Navigate to the `Chart Explorer` view.

Select `Metrics` as the data source. Complete the chart builder to plot the `Maximum` of `visa_validation_cache.size (Gauge)` and press the play button. The cache was clearly increasing before reaching a maximum size, after which errors were generated.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/5be7d4b667a51d74fe9336fe3d3439ea7fb67983b62c57e0a973bad0c2494dc8/images/use-cases/observability/hyperdx-19.png" alt="Metrics"/>

</Steps>
