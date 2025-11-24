# Source: https://docs.hypermode.com/dgraph/admin/traces.md

# Traces

<Info>
  We're overhauling Dgraph's docs to make them clearer and more approachable. If
  you notice any issues during this transition or have suggestions, please
  [let us know](https://github.com/hypermodeinc/docs/issues).
</Info>

Dgraph is integrated with [OpenCensus](https://opencensus.io/zpages/) to collect
distributed traces from the Dgraph cluster.

Trace data is always collected within Dgraph. You can adjust the trace sampling
rate for Dgraph queries using the `--trace`
[superflag's](/dgraph/cli/command-reference) `ratio` option when running Dgraph
Alpha nodes. By default, `--trace ratio` is set to 0.01 to trace 1% of queries.

## Examining traces with zPages

The most basic way to view traces is with the integrated trace pages.

OpenCensus's [zPages](https://opencensus.io/zpages/) are accessible via the Zero
or Alpha HTTP port at `/z/tracez`.

## Examining traces with Jaeger

Jaeger collects distributed traces and provides a UI to view and query traces
across different services. This provides the necessary observability to
understand what's happening in the system.

Dgraph can be configured to send traces directly to a Jaeger collector with the
`trace` superflag's `jaeger` option. For example, if the Jaeger collector is
running on `http://localhost:14268`, then pass this option to the Dgraph Zero
and Dgraph Alpha instances as `--trace jaeger=http://localhost:14268`.

See
[Jaeger's Getting Started docs](https://www.jaegertracing.io/docs/getting-started/)
to get up and running with Jaeger.

### Setting up multiple Dgraph clusters with Jaeger

Jaeger allows you to examine traces from multiple Dgraph clusters. To do this,
use the `--collector.tags` on a Jaeger collector to set custom trace tags. For
example, run one collector with `--collector.tags env=qa` and then another
collector with `--collector.tags env=dev`. In Dgraph, set the `--trace jaeger`
option in the Dgraph QA cluster to the first collector and set this option in
the Dgraph development cluster to the second collector. You can run multiple
Jaeger collector components for the same single Jaeger backend. This is still a
single Jaeger installation but with different collectors customizing the tags
per environment.

Once you have this configured, you can filter by tags in the Jaeger UI. Filter
traces by tags matching `env=dev`:

<img src="https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/jaeger-ui.png?fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=b52505ffe7a14a0941bcf0f57490c960" alt="Jaeger UI" width="345" height="426" data-path="images/dgraph/jaeger-ui.png" srcset="https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/jaeger-ui.png?w=280&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=aac7f5994b4b580e9b08eb0a010d98b1 280w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/jaeger-ui.png?w=560&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=4a25ce1ce5ea7fb4bcc9589b7bd61916 560w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/jaeger-ui.png?w=840&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=e0ce50e14fcba2116a8f790968d7e9a4 840w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/jaeger-ui.png?w=1100&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=4aa77053dcca3dee892de6ef5c459270 1100w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/jaeger-ui.png?w=1650&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=7933e17eec6881192a2302acbf508e7b 1650w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/jaeger-ui.png?w=2500&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=3b8de207065028989787024c9149d813 2500w" data-optimize="true" data-opv="2" />

Every trace has your custom tags set under the “Process” section of each span:

<img src="https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/jaeger-server-query.png?fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=ac84d8275e7778e8787beb70f7393bad" alt="Jaeger Query" width="527" height="168" data-path="images/dgraph/jaeger-server-query.png" srcset="https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/jaeger-server-query.png?w=280&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=d15395db89a00244b320720dc36a58cd 280w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/jaeger-server-query.png?w=560&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=9738a5ed8604757786c1b85d35e05bda 560w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/jaeger-server-query.png?w=840&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=86f139ec4f1274f315d60913370398d6 840w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/jaeger-server-query.png?w=1100&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=18d25be9226f7c02be6d704cfd611612 1100w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/jaeger-server-query.png?w=1650&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=6e215303505af628f42e29c2327dc54d 1650w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/jaeger-server-query.png?w=2500&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=b8cae7fdd1696144a0fd064cf48e79fa 2500w" data-optimize="true" data-opv="2" />

Filter traces by tags matching `env=qa`:

<img src="https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/jaeger-json.png?fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=ec704f99027a2b55dd2bbd4ea7f7cf10" alt="Jaeger JSON" width="345" height="355" data-path="images/dgraph/jaeger-json.png" srcset="https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/jaeger-json.png?w=280&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=d3b80e08cb1e8e9122003398d91ad30a 280w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/jaeger-json.png?w=560&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=1d773839bdcae374b31162e2dbdf7d8c 560w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/jaeger-json.png?w=840&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=9fef9792a4a98e5cbaad688cf8c53b96 840w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/jaeger-json.png?w=1100&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=a4370a6a1b72525207f6e8bec9fc029e 1100w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/jaeger-json.png?w=1650&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=27ea96fc240bc072fecced0871c66b0d 1650w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/jaeger-json.png?w=2500&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=353f4bdd85d552473eaf57e90ac9619b 2500w" data-optimize="true" data-opv="2" />

<img src="https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/jaeger-server-query-2.png?fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=03473ecc8cc9e3b3f903dc86a6dfd376" alt="Jaeger Query Result" width="516" height="163" data-path="images/dgraph/jaeger-server-query-2.png" srcset="https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/jaeger-server-query-2.png?w=280&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=655469d345a3b1f4c78a49418f800c49 280w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/jaeger-server-query-2.png?w=560&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=4270415463a05479768acc049a822816 560w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/jaeger-server-query-2.png?w=840&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=544a9d41750c98cad6696a69d6cb4e3f 840w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/jaeger-server-query-2.png?w=1100&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=7c38dc0d4e9f96f5b62a0be6f26b8297 1100w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/jaeger-server-query-2.png?w=1650&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=63ed55e4ed28041c6e673e0544f1841d 1650w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/jaeger-server-query-2.png?w=2500&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=f417747c7755b355c69b7bdd5dbb24df 2500w" data-optimize="true" data-opv="2" />

To learn more about Jaeger, see
[Jaeger's Deployment Guide](https://www.jaegertracing.io/docs/deployment/).
