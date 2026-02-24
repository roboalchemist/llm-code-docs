# Source: https://docs.datadoghq.com/serverless.md

---
title: Serverless
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Serverless
---

# Serverless

{% alert level="info" %}
Make sure to check out discussions going on in the [\#serverless](https://datadoghq.slack.com/archives/CFDPB83M4) channel in the [Datadog Slack community](https://chat.datadoghq.com/).
{% /alert %}

{% callout %}
##### Join an enablement webinar session

Learn how serverless monitoring enables your teams to stay agile and focus their time on building revenue-generating applications while reducing operational overhead.

[SIGN UP](https://www.datadoghq.com/technical-enablement/sessions/?tags.topics-0=Serverless)
{% /callout %}

[Datadog Serverless Monitoring](http://app.datadoghq.com/functions) provides full visibility into all of the managed services that power your serverless applications by bringing together real-time metrics, logs and traces from your serverless compute as well as related fully-managed APIs, queues, streams and data stores.

Datadog provides solutions for monitoring AWS Lambda, Azure App Service, Azure Container Apps, and Google Cloud Run.

### AWS Lambda{% #aws-lambda %}

[Serverless Monitoring for AWS Lambda](https://docs.datadoghq.com/serverless/aws_lambda) enables you to correlate high-level metrics from AWS resources with those of Lambda functions, so you can quickly spot issues and start your investigation.

[Enhanced Lambda metrics](https://docs.datadoghq.com/serverless/enhanced_lambda_metrics), which appear in Datadog with the prefix `aws.lambda.enhanced`, are available at second granularity and in near real time. You can use enhanced Lambda metrics for alerts or SLOs on cold starts, estimated AWS costs, timeouts, out-of-memory errors, and memory usage across all of your Lambda functions.

You can send [custom metrics](https://docs.datadoghq.com/serverless/custom_metrics) from a Lambda function by generating metrics from logs and traces, using the Datadog Lambda Extension, or using the Datadog Forwarder Lambda.

With [Distributed Tracing](https://docs.datadoghq.com/serverless/distributed_tracing), you can connect your serverless traces to metrics for a context-rich picture of your application's performance. The Datadog Python, Node.js, Ruby, Go, Java, and .NET tracing libraries support distributed tracing for AWS Lambda.

[Deployment Tracking](https://docs.datadoghq.com/serverless/deployment_tracking) helps you to correlate serverless code, configuration, and deployment changes with metrics, traces, and logs from your functions for real-time insight into how these changes may affect the health and performance of your applications.

### AWS Step Functions{% #aws-step-functions %}

AWS Step Functions is a serverless orchestration service that lets developers create and manage multi-step application workflows in AWS.

Monitor metrics and logs from the [AWS Step Functions Integration](https://docs.datadoghq.com/integrations/amazon_step_functions) to view cloud-native telemetry within the Serverless app view.

Identify bugs and bottlenecks with [execution traces](https://docs.datadoghq.com/serverless/step_functions/installation). Traces for step functions can be generated from Step Function logs and provide granular execution information, including the state machine execution path, inputs and outputs for each step, and step execution length.

Enhanced Step Function metrics, which appear in Datadog with the prefix `aws.states.enhanced`, are available at second granularity and generated directly within Datadog.

### Azure App Service{% #azure-app-service %}

The [Datadog extension for Azure App Service](https://docs.datadoghq.com/serverless/azure_app_service/#overview) provides tracing capabilities for Azure Web Apps.

Use the [Azure App Service view](https://app.datadoghq.com/functions?cloud=azure&config_serverless-azure-app=true&group=service) to:

- Quickly identify apps with high latency or errors

- Track the utilization of your Web Apps, Function Apps, and App Service Plans

- Get insights into the costs of your App Service Plans by visualizing the number of active instances and seeing which are running apps that are submitting traces or logs to Datadog

- Map the apps running on your App Service Plans to identify apps that may be impacting costs or performance

The Datadog extension for Azure App Service provides tracing capabilities for Azure Web Apps. For more information about setting up tracing in Azure, see [Azure App Service](https://docs.datadoghq.com/serverless/azure_app_service/#overview).

### Azure Container Apps{% #azure-container-apps %}

Azure Container Apps is a fully managed serverless platform for deploying and scaling container-based applications. Datadog provides monitoring and log collection for Container Apps through the [Azure integration](https://docs.datadoghq.com/integrations/azure/#log-collection).

Datadog also provides a solution for [instrumenting your Container Apps applications](https://docs.datadoghq.com/serverless/azure_container_apps) with a purpose-built Agent to enable tracing, custom metrics, and direct log collection.

### Google Cloud Run{% #google-cloud-run %}

Google Cloud Run is a lightweight, event-based, asynchronous compute solution that allows you to create small, single-purpose functions. To monitor serverless functions running on Google Cloud Platform, enable the [Google Cloud Platform integration](https://docs.datadoghq.com/integrations/google_cloud_platform/).

Datadog also provides a solution for [instrumenting your Cloud Run applications](https://docs.datadoghq.com/serverless/google_cloud_run) with a purpose-built Agent to enable tracing, custom metrics, and direct log collection.

## Further Reading{% #further-reading %}

- [Check out the latest Serverless releases! (App login required).](https://app.datadoghq.com/release-notes?category=Serverless)
- [The State of Serverless](https://www.datadoghq.com/state-of-serverless)
- [Installing Serverless monitoring](https://docs.datadoghq.com/serverless/installation/)
- [Monitor Azure Container Apps with Datadog](https://www.datadoghq.com/blog/azure-container-apps/)
- [Join an interactive session to learn more about serverless monitoring](https://dtdg.co/fe)
