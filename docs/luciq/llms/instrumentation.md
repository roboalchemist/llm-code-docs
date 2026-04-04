# Source: https://docs.luciq.ai/product-guides-and-integrations/product-guides/application-performance-monitoring/instrumentation.md

# Instrumentation

### Spans

Spans allow you to better understand the root causes of the latencies that occur during your app’s launch and screen loading. This section provides a detailed breakdown of the duration of the platform life cycle stages, network calls, and more information during the app launch and screen loading.

<figure><img src="https://files.readme.io/b582643a66a8296181c6f6d61017c7c099bdb239a32c93efc0e4ddd173726700-ios-apm-instrumentation-1.png" alt=""><figcaption></figcaption></figure>

#### Spans Table Breakdown

|                  |                                                                                                                                                                                            |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Span Name        | This shows the stage or request name to identify its source.                                                                                                                               |
| P50              | This is the 50th percentile, which is the maximum latency that 50% of all the occurrences have in the selected time period and is shown in ms.                                             |
| P95              | This is the 95th percentile, which is the maximum latency that 95% of all the occurrences have in the selected time period and is shown in ms.                                             |
| P50 & P95 Change | This shows the change rate of P50 & P95 durations in comparison to the last period based on the selected date filter.                                                                      |
| Average Calls    | This shows how many times the span happened per single occurrence to understand its redundancy better. To get the overall duration of this span, multiply the Average Call by the P50/P95. |
| Frequency        | This is how many times the span happened per all occurrences of the specified metric.                                                                                                      |

#### Supported Span Types

These are the currently supported Span Types:

* View Loading.
* Network.
* App Initialization.
* Database Queries.

#### Database Queries

You'll be able to see the Database queries that happen during your app launch or screen loading with all its details in the spans table and occurrences view.

<figure><img src="https://files.readme.io/828e441ec01ab724572ccb43c911fe593c4b6513be1bb0dc67b36f740150b008-ios-apm-instrumentation-3.png" alt=""><figcaption></figcaption></figure>

### Spans Table in Network Metric

To help you have a better understanding of what's causing the bulk delays inside your network calls, either from the Client, Server, or Network sides, you'll be able to see a detailed breakdown of the latencies caused by the stages/operations that were made to send the network request and receive its response from the server on aggregation and occurrence levels inside the network metric.

You can read more about the Spans table in Network Metric [here](https://docs.luciq.ai/product-guides-and-integrations/product-guides/application-performance-monitoring/network).

{% hint style="info" %}
If you are using the `EndAppLaunch` or `EndScreenLoading` APIs, Luciq captures the duration from the start of the app launch or screen loading up until the call of any of the APIs.
{% endhint %}
