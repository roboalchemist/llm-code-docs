# Source: https://clickhouse.ferndocs.com/click-stack/use-cases/observability/clickstack/getting-started/remote-demo-data.md

---
slug: /use-cases/observability/clickstack/getting-started/remote-demo-data
title: Remote Demo Dataset
sidebar_position: 2
pagination_prev: null
pagination_next: null
description: Getting started with ClickStack and a remote demo dataset
doc_type: guide
keywords:

- clickstack
- example data
- sample dataset
- logs
- observability

---

**The following guide assumes you have deployed ClickStack using the [instructions for the all-in-one image](/use-cases/observability/clickstack/getting-started), or [Local Mode Only](/use-cases/observability/clickstack/deployment/local-mode-only) and completed initial user creation. Alternatively, users can skip all local setup and simply connect to our ClickStack hosted demo [play-clickstack.clickhouse.com](https://play-clickstack.clickhouse.com) which uses this dataset.**

This guide uses a sample dataset hosted on the public ClickHouse playground at [sql.clickhouse.com](https://sql.clickhpouse.com), which you can connect to from your local ClickStack deployment.

<Warning title="Not supported with HyperDX in ClickHouse Cloud">
Remote databases are not supported when HyperDX is hosted in ClickHouse Cloud. This dataset is therefore not supported.
</Warning>

It contains approximately 40 hours of data captured from the ClickHouse version of the official OpenTelemetry (OTel) demo. The data is replayed nightly with timestamps adjusted to the current time window, allowing users to explore system behavior using HyperDX's integrated logs, traces, and metrics.

<Note title="Data variations">
Because the dataset is replayed from midnight each day, the exact visualizations may vary depending on when you explore the demo.
</Note>

## Demo scenario [#demo-scenario]

In this demo, we investigate an incident involving an e-commerce website that sells telescopes and related accessories.

The customer support team has reported that users are experiencing issues completing payments at checkout. The issue has been escalated to the Site Reliability Engineering (SRE) team for investigation.

Using HyperDX, the SRE team will analyze logs, traces, and metrics to diagnose and resolve the issue—then review session data to confirm whether their conclusions align with actual user behavior.

## Open Telemetry Demo [#otel-demo]

This demo uses a [ClickStack maintained fork](https://github.com/ClickHouse/opentelemetry-demo) of the official OpenTelemetry demo.

### Demo Architecture [#demo-architecture]

The demo is composed of microservices written in different programming languages that talk to each other over gRPC and HTTP and a load generator that uses Locust to fake user traffic. The original source code for this demo has been modified to use [ClickStack instrumentation](/use-cases/observability/clickstack/sdks).

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/5d11f76dcda59e1d67227a70d2f06ba9f4a5a21110aef0d664bccfde03a47166/images/use-cases/observability/hyperdx-demo/architecture.png" alt="Architecture"/>

_Credit: https://opentelemetry.io/docs/demo/architecture/_

Further details on the demo can be found in:

- [OpenTelemetry documentation](https://opentelemetry.io/docs/demo/)
- [ClickStack maintained fork](https://github.com/ClickHouse/opentelemetry-demo)

## Demo steps [#demo-steps]

**We have instrumented this demo with [ClickStack SDKs](/use-cases/observability/clickstack/sdks), deploying the services in Kubernetes, from which metrics and logs have also been collected.**

<Steps>

### Connect to the demo server [#connect-to-the-demo-server]

<Note title="Local-Only mode">
This step can be skipped if you clicked `Connect to Demo Server` when deploying in Local Mode. If using this mode, sources will be prefixed with `Demo_` e.g. `Demo_Logs`
</Note>

Navigate to `Team Settings` and click `Edit` for the `Local Connection`:

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/fc6dcaa6bda2e186dc33f09ce8194221fcf3b0cd9ea064c73c8a5c85c9f5f952/images/use-cases/observability/edit_connection.png" alt="Edit Connection"/>

Rename the connection to `Demo` and complete the subsequent form with the following connection details for the demo server:

- `Connection Name`: `Demo`
- `Host`: `https://sql-clickhouse.clickhouse.com`
- `Username`: `otel_demo`
- `Password`: Leave empty

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/f2520c5695cd2082897606e35c78d0f957096302952be8ba39d85582795a8ff9/images/use-cases/observability/hyperdx-demo/edit_demo_connection.png" alt="Edit Demo Connection"/>

### Modify the sources [#modify-sources]

<Note title="Local-Only mode">
This step can be skipped if you clicked `Connect to Demo Server` when deploying in Local Mode. If using this mode, sources will be prefixed with `Demo_` e.g. `Demo_Logs`
</Note>

Scroll up to `Sources` and modify each of the sources - `Logs`, `Traces`, `Metrics`, and `Sessions` - to use the `otel_v2` database.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/a19dc79a97dcea6e1cf1d6265017ac249ed8d77cd5b77921ff14fcc95e1dc589/images/use-cases/observability/hyperdx-demo/edit_demo_source.png" alt="Edit Demo Source"/>

<Note>
You may need to reload the page to ensure the full list of databases is listed in each source.
</Note>

### Adjust the time frame [#adjust-the-timeframe]

Adjust the time to show all data from the previous `1 day` using the time picker in the top right.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/7d846fc21407aace605c665d3087f15ad90e6e8c9428acb3e059289262f23b20/images/use-cases/observability/hyperdx-demo/step_2.png" alt="Step 2"/>

You may a small difference in the number of errors in the overview bar chart, with a small increase in red in several consecutive bars.

<Note>
The location of the bars will differ depending on when you query the dataset.
</Note>

### Filter to errors [#filter-to-errors]

To highlight occurrences of errors, use the `SeverityText` filter and select `error` to display only error-level entries.

The error should be more apparent:

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/80ad88811a920b1b38c3b8cc197024b39ab383c86097b6dbd618ce4bfa8ed4dc/images/use-cases/observability/hyperdx-demo/step_3.png" alt="Step 3"/>

### Identify the error patterns [#identify-error-patterns]

With HyperDX's Clustering feature, you can automatically identify errors and group them into meaningful patterns. This accelerates user analysis when dealing with large volumes of log and traces. To use it, select `Event Patterns` from the `Analysis Mode` menu on the left panel.

The error clusters reveal issues related to failed payments, including a named pattern `Failed to place order`. Additional clusters also indicate problems charging cards and caches being full.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/cdc8e386cdb54171a9664c8ef499ca1eec743ff9b5613a67e94e5b2bfa5d93d2/images/use-cases/observability/hyperdx-demo/step_4.png" alt="Step 4"/>

Note that these error clusters likely originate from different services.

### Explore an error pattern [#explore-error-pattern]

Click the most obvious error clusters which correlates with our reported issue of users being able to complete payments: `Failed to place order`.

This will display a list of all occurrences of this error which are associated with the `frontend` service:

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/9f6abe4090fab8770d42e500bf1763452f846f427a3da6eb272bbd6c356ea15d/images/use-cases/observability/hyperdx-demo/step_5.png" alt="Step 5"/>

Select any of the resulting errors. The logs metadata will be shown in detail. Scrolling through both the `Overview` and `Column Values` suggests an issue with the charging cards due to a cache:

`failed to charge card: could not charge the card: rpc error: code = Unknown desc = Visa cache full: cannot add new item.`

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/098f41f1c6dd06df46182507da7513f8bd9ad48b6e55db1516fe85523f0ebaea/images/use-cases/observability/hyperdx-demo/step_6.png" alt="Step 6"/>

### Explore the infrastructure [#explore-the-infrastructure]

We've identified a cache-related error that's likely causing payment failures. We still need to identify where this issue is originating from in our microservice architecture.

Given the cache issue, it makes sense to investigate the underlying infrastructure - potentially we have memory problem in the associated pods? In ClickStack, logs and metrics are unified and displayed in context, making it easier to uncover the root cause quickly.

Select the `Infrastructure` tab to view the metrics associated with the underlying pods for the `frontend` service and widen the timespan to `1d`:

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/573c8cae79c7779c11e77499c217fb7e024eaf48ed020596d283b295fe53a06a/images/use-cases/observability/hyperdx-demo/step_7.png" alt="Step 7"/>

The issue does not seem to infrastructure related - no metrics have appreciably changed over the time period: either before or after the error. Close the infrastructure tab.

### Explore a trace [#explore-a-trace]

In ClickStack, traces are also automatically correlated with both logs and metrics. Let's explore the trace linked to our selected log to identify the service responsible.

Select `Trace` to visualize the associated trace. Scrolling down through the subsequent view we can see how HyperDX is able to visualize the distributed trace across the microservices, connecting the spans in each service. A payment clearly involves multiple microservices, including those that performance checkout and currency conversions.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/9c4e0b04c2d5b63028843f70966ec0c85a9819de8ee7e8f0b492d6af91ecbac0/images/use-cases/observability/hyperdx-demo/step_8.png" alt="Step 8"/>

By scrolling to the bottom of the view we can see that the `payment` service is causing the error, which in turn propagates back up the call chain.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/dfe87fa63ac794432c322d36a3b1bb2f3787c8d02c5b5890e1e85af9994a562a/images/use-cases/observability/hyperdx-demo/step_9.png" alt="Step 9"/>

### Searching traces [#searching-traces]

We have established users are failing to complete purchases due to a cache issue in the payment service. Let's explore the traces for this service in more detail to see if we can learn more about the root cause.

Switch to the main Search view by selecting `Search`. Switch the data source for `Traces` and select the `Results table` view. **Ensure the timespan is still over the last day.**

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/5a027c2b4015826f90a1dc946052a65a977ea49ddac14d5c4450d1b9ee5b1b1d/images/use-cases/observability/hyperdx-demo/step_10.png" alt="Step 10"/>

This view shows all traces in the last day. We know the issue originates in our payment service, so apply the `payment` filter to the `ServiceName`.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/b284e91d41a34a4eac56297a51f24c9c9b824ca93871af674f2076dc6ee03810/images/use-cases/observability/hyperdx-demo/step_11.png" alt="Step 11"/>

If we apply event clustering to the traces by selecting `Event Patterns`, we can immediately see our cache issue with the `payment` service.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/53b6749b226ab9b97fda1278658c8e7d014068e7c4500bc1b3f9ce8648d479d4/images/use-cases/observability/hyperdx-demo/step_12.png" alt="Step 12"/>

### Explore infrastructure for a trace [#explore-infrastructure-for-a-trace]

Switch to the results view by clicking on `Results table`. Filter to errors using the `StatusCode` filter and `Error` value.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/b252d1d1731743e200c0dc1fb196d0b1704d722a39087236e2a0b79ac676c6ce/images/use-cases/observability/hyperdx-demo/step_13.png" alt="Step 13"/>

Select a `Error: Visa cache full: cannot add new item.` error, switch to the `Infrastructure` tab and widen the timespan to `1d`.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/c8651b0555c179d08ab07a7130669058ab8aebc1acab8f11d433043d0e63a78a/images/use-cases/observability/hyperdx-demo/step_14.png" alt="Step 14"/>

By correlating traces with metrics we can see that memory and CPU increased with the `payment` service, before collapsing to `0` (we can attribute this to a pod restart) - suggesting the cache issue caused resource issues. We can expect this has impacted payment completion times.

### Event deltas for faster resolution [#event-deltas-for-faster-resolution]

Event Deltas help surface anomalies by attributing changes in performance or error rates to specific subsets of data—making it easier to quickly pinpoint the root cause.

While we know that the `payment` service has a cache issue, causing an increase in resource consumption, we haven't fully identified the root cause.

Return to the result table view and select the time period containing the errors to limit the data. Ensure you select several hours to the left of the errors and after if possible (the issue may still be occurring):

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/881df864fd8f9895788e8d093969c8143c760b989d195a7ba3ccdad55e9ec28e/images/use-cases/observability/hyperdx-demo/step_15.png" alt="Step 15"/>

Remove the errors filter and select `Event Deltas` from the left `Analysis Mode` menu.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/6429ccb920aa11b338da49a168c4c0540b80a0c5f58e3d7960374bc798968474/images/use-cases/observability/hyperdx-demo/step_16.png" alt="Step 16"/>

The top panel shows the distribution of timings, with colors indicating event density (number of spans). The subset of events outside of the main concentration are typically those worth investigating.

If we select the events with a duration greater than `200ms`, and apply the filter `Filter by selection`, we can limit our analysis to slower events:

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/410d6cfd51222ce0a6a8e6954603437299a6bc7d55d4e2e7b0bc5f60b8055591/images/use-cases/observability/hyperdx-demo/step_17.png" alt="Step 17"/>

With analysis performed on the subset of data, we can see most performance spikes are associated with `visa` transactions.

### Using charts for more context [#using-charts-for-more-context]

In ClickStack, we can chart any numeric value from logs, traces, or metrics for greater context.

We have established:

- Our issue resides with the payment service
- A cache is full
- This caused increases in resource consumption
- The issue prevented visa payments from completing - or at least causing them to take a long time to complete.

<br/>

Select `Chart Explorer` from the left menu. Complete the following values to chart the time taken for payments to complete by chart type:

- `Data Source`: `Traces`
- `Metric`: `Maximum`
- `SQL Column`: `Duration`
- `Where`: `ServiceName: payment`
- `Timespan`: `Last 1 day`

<br/>

Clicking `▶️` will show how the performance of payments degraded over time.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/8a73c5852acc34eedf97def45bd1dcfd0530ae2ceb74d55aa4a53db5b78f9c2e/images/use-cases/observability/hyperdx-demo/step_18.png" alt="Step 18"/>

If we set `Group By` to `SpanAttributes['app.payment.card_type']` (just type `card` for autocomplete) we can see how the performance of the service degraded for Visa transactions relative to Mastercard:

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/b742203606097a4b485810268e2981de6a2338917decd531bc160638eefc0319/images/use-cases/observability/hyperdx-demo/step_19.png" alt="Step 19"/>

Note than once the error occurs responses return in `0s`.

### Exploring metrics more context [#exploring-metrics-for-more-context]

Finally, let's plot the cache size as a metric to see how it behaved over time, thus giving us more context.

Complete the following values:

- `Data Source`: `Metrics`
- `Metric`: `Maximum`
- `SQL Column`: `visa_validation_cache.size (gauge)` (just type `cache` for autocomplete)
- `Where`: `ServiceName: payment`
- `Group By`: `<empty>`

We can see how the cache size increased over a 4-5 hr period (likely after a software deployment) before reaching a maximum size of `100,000`. From the `Sample Matched Events` we can see our errors correlate with the cache reaching this limit and, after which it is recorded as having a size of `0` with responses also returning in `0s`.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/c6ac1b29fa3766ef620a32af70af832b653a74590bb5cdd6edb35154860512de/images/use-cases/observability/hyperdx-demo/step_20.png" alt="Step 20"/>

In summary, by exploring logs, traces and finally metrics we have concluded:

- Our issue resides with the payment service
- A change in service behavior, likely due to a deployment, resulted in a slow increase of a visa cache over a 4-5 hr period - reaching a maximum size of `100,000`.
- This caused increases in resource consumption as the cache grew in size - likely due to a poor implementation
- As the cache grew, the performance of Visa payments degraded
- On reaching the maximum size, the cache rejected payments and reported itself as size `0`.

### Using sessions [#using-sessions]

Sessions allow us to replay the user experience, offering a visual account of how an error occurred from the user's perspective. While not typically used to diagnose root causes, they are valuable for confirming issues reported to customer support and can serve as a starting point for deeper investigation.

In HyperDX, sessions are linked to traces and logs, providing a complete view of the underlying cause.

For example, if the support team provides the email of a user who encountered a payment issue `Braulio.Roberts23@hotmail.com` - it's often more effective to begin with their session rather than directly searching logs or traces.

Navigate to the `Client Sessions` tab from the left menu before ensuring the data source is set to `Sessions` and the time period is set to the `Last 1 day`:

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/3b2ec1ce6bb6c9921caf07d9d674296dab0cb6bc7568fc8748ced9baa55c54d8/images/use-cases/observability/hyperdx-demo/step_21.png" alt="Step 21"/>

Search for `SpanAttributes.userEmail: Braulio` to find our customer's session. Selecting the session will show the browser events and associated spans for the customer's session on the left, with the user's browser experience re-rendered to the right:

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/52e4dee3e54ae5109872f38847b6b9b62497dd1ea127b619f64367c7aa81acf0/images/use-cases/observability/hyperdx-demo/step_22.png" alt="Step 22"/>

### Replaying sessions [#replaying-sessions]

Sessions can be replayed by pressing the ▶️ button. Switching between `Highlighted` and `All Events` allows varying degrees of span granularity, with the former highlighting key events and errors.

If we scroll to the bottom of the spans we can see a `500` error associated with `/api/checkout`. Selecting the ▶️ button for this specific span moves the replay to this point in the session, allowing us to confirm the customer's experience - payment seems to simply not work with no error rendered.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/77ae9b1475b8bb50fb8f2bc565f974171834eb6fb3bc5437e49642b2e5257790/images/use-cases/observability/hyperdx-demo/step_23.png" alt="Step 23"/>

Selecting the span we can confirm this was caused by an internal error. By clicking the `Trace` tab and scrolling though the connected spans, we are able to confirm the customer indeed was a victim of our cache issue.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/6840f19d36ff8f3f87c3ff60449039b2422866f4158f370983e364b45065f8a4/images/use-cases/observability/hyperdx-demo/step_24.png" alt="Step 24"/>

</Steps>

This demo walks through a real-world incident involving failed payments in an e-commerce app, showing how ClickStack helps uncover root causes through unified logs, traces, metrics, and session replays - explore our [other getting started guides](/use-cases/observability/clickstack/sample-datasets) to dive deeper into specific features.
