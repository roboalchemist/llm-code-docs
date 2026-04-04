# Source: https://checklyhq.com/docs/resolve/traces/export/grafana-tempo.md

> ## Documentation Index
> Fetch the complete documentation index at: https://checklyhq.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Exporting Traces to Grafana Tempo

> Learn how to export traces from Checkly to Grafana Tempo.

You can connect the Traces export to Grafana using the OpenTelemetry Integration and Grafana Tempo.

1. Make sure that you have Tempo running on your Grafana Cloud Instance at `yourOrganization.grafana.net`. Find it at **Connections > Search for Tempo > Check if Tempo Data source is marked as installed**.

2. In Grafana Cloud (`grafana.com/orgs/yourOrganization`), head over to **Connections** > **Add new connection** > **OpenTelemetry (OTLP)**.
   <img src="https://mintcdn.com/checkly-422f444a/WJFfxOuqqqZjE4cw/images/docs/images/otel/export-traces/grafana-cloud-opentelemetry.png?fit=max&auto=format&n=WJFfxOuqqqZjE4cw&q=85&s=0e23420c2f7911b4db66884b075a25f0" alt="Add an OTLP connection in Grafana Cloud" width="1309" height="865" data-path="images/docs/images/otel/export-traces/grafana-cloud-opentelemetry.png" />

3. Copy the endpoint URL and append `v1/traces` to it.
   <img src="https://mintcdn.com/checkly-422f444a/WJFfxOuqqqZjE4cw/images/docs/images/otel/export-traces/grafana-otlp-endpoint-config.png?fit=max&auto=format&n=WJFfxOuqqqZjE4cw&q=85&s=16212932d6f73e3c5719e1298c897c3b" alt="Grafana OTLP endpoint" width="1054" height="737" data-path="images/docs/images/otel/export-traces/grafana-otlp-endpoint-config.png" />
   It should be similar to:`https://otlp-gateway-prod-eu-west-2.grafana.net/otlp/v1/traces`.

4. Generate an OTLP Token, and copy both the Instance ID and the OTLP Token as well.
   <img src="https://mintcdn.com/checkly-422f444a/WJFfxOuqqqZjE4cw/images/docs/images/otel/export-traces/create-otlp-token-grafana.png?fit=max&auto=format&n=WJFfxOuqqqZjE4cw&q=85&s=4442363568fd2e278f9243a50d4cf86a" alt="Generate an OTLP token" width="740" height="439" data-path="images/docs/images/otel/export-traces/create-otlp-token-grafana.png" />

5. Head back to the [Traces Settings page](https://app.checklyhq.com/settings/account/traces) on Checkly.

* Enable exporting traces and add the endpoint URL from step 3.
* and in the **Headers** section, specify the HTTP Header:  `Authorization` and `Basic instance:token`, where `instance:token` is base64 encoded.
  You can use an online tool like [base64encode.net](https://www.base64encode.net/)
  to encode your instance and token.
  <img src="https://mintcdn.com/checkly-422f444a/WJFfxOuqqqZjE4cw/images/docs/images/otel/export-traces/export-traces-to-grafana-config.png?fit=max&auto=format&n=WJFfxOuqqqZjE4cw&q=85&s=dac659ad7cc55d1de12b7bd20b619c23" alt="Export Traces configuration" width="990" height="490" data-path="images/docs/images/otel/export-traces/export-traces-to-grafana-config.png" />

2. Back in your Grafana Cloud Instance (for example danube.grafana.net), head over to "Explore", select the *Tempo* source that is named `grafanacloud-yourOrganization-traces`:
   <img src="https://mintcdn.com/checkly-422f444a/WJFfxOuqqqZjE4cw/images/docs/images/otel/export-traces/grafana-cloud-tempo-source.png?fit=max&auto=format&n=WJFfxOuqqqZjE4cw&q=85&s=242e517a2fb85a84b4cb9d89b46cd1c5" alt="Select Tempo traces data source" width="2270" height="286" data-path="images/docs/images/otel/export-traces/grafana-cloud-tempo-source.png" />

   Now, click **Search** to see the table of Traces received. The ones exported by Checkly, have `checkly` in the service column.
   <img src="https://mintcdn.com/checkly-422f444a/WJFfxOuqqqZjE4cw/images/docs/images/otel/export-traces/grafana-explore-checkly-traces.png?fit=max&auto=format&n=WJFfxOuqqqZjE4cw&q=85&s=1e06e3a798ae4305e883010c35a1feac" alt="See Checkly Traces in Grafana" width="2984" height="1544" data-path="images/docs/images/otel/export-traces/grafana-explore-checkly-traces.png" />

Find more the details in the [Grafana OpenTelemetry documentation](https://grafana.com/docs/grafana-cloud/send-data/otlp/send-data-otlp/?pg=traces\&plcmt=hero-btn-2#before-you-begin).


Built with [Mintlify](https://mintlify.com).