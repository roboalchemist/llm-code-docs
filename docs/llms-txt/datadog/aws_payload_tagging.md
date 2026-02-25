# Source: https://docs.datadoghq.com/tracing/guide/aws_payload_tagging.md

---
title: Capture Requests and Responses From AWS Services
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > APM > Tracing Guides > Capture Requests and Responses From AWS Services
---

# Capture Requests and Responses From AWS Services

## Overview{% #overview %}

AWS Payload Extraction captures request and response data exchanged between your application and AWS services. This feature attaches the extracted information as tags to your traces, enabling you to view the data in dashboards and use it for alerting.

## Requirements{% #requirements %}

The following tracer versions and AWS SDK packages are supported:

| Language | Version            | Instrumented AWS SDK Packages  |
| -------- | ------------------ | ------------------------------ |
| Node.js  | 5.25.0+ or 4.49.0+ | `@aws-sdk/*` (AWS SDK v3)      |
| Java     | 1.42.1+            | `aws-sdk-v2`                   |
| Python   | 2.17.0+            | `botocore` (including `boto3`) |

## How it works{% #how-it-works %}

AWS Payload Extraction extracts key-value pairs from hierarchical request and response bodies, converting them into dot-separated tags. For example:

Input JSON:

```json
{
  "Message": {
    "foo.bar": "baz",
    "Arr": ["a", "b"]
  }
}
```

Generated tags:

```text
aws.request.body.Message.foo\.bar: baz
aws.request.body.Message.Arr.0: a
aws.request.body.Message.Arr.1: b
```

The tracers are configured to match JSON data nested inside JSON documents, which is a common pattern with SQS payloads.

## General configuration{% #general-configuration %}

### Enable AWS Payload Extraction{% #enable-aws-payload-extraction %}

To enable AWS Payload Extraction, set these environment variables:

```sh
# Parse requests
DD_TRACE_CLOUD_REQUEST_PAYLOAD_TAGGING=all

# Parse responses
DD_TRACE_CLOUD_RESPONSE_PAYLOAD_TAGGING=all
```

You can choose to parse:

- Only request bodies
- Only response bodies
- Both request and response bodies

The value `all` indicates that the entire body is used to generate tags. See Protect sensitive information for more configuration options.

### Protect sensitive information{% #protect-sensitive-information %}

It's expected that many of these payloads contain *personally identifiable information* (PII).

To protect sensitive information, the tracers replace common PII fields with `'redacted'` (such as phone numbers in SNS). **Note**: You can't disable the default redactions.

You can specify additional fields to redact using [JSONPath](https://jsonpath.com/) syntax in the environment variables. For example:

```sh
DD_TRACE_CLOUD_REQUEST_PAYLOAD_TAGGING=$.Metadata.UserId,$.Attributes.0.Pass
```

This example:

- Redacts the `UserId` field within the `Metadata` object
- Redacts the `Pass` field in the first element of the `Attributes` array
- Applies default redactions
- Processes request bodies only

{% alert level="info" %}
Redaction rules apply across all services and cannot be configured per service.
{% /alert %}

### Control payload extraction depth{% #control-payload-extraction-depth %}

Control the maximum depth of payload extraction with:

```sh
DD_TRACE_CLOUD_PAYLOAD_TAGGING_MAX_DEPTH=10
```

The default value is `10`. Nodes beyond this depth are ignored during tag generation. The main reason to modify this value is to adjust performance.

### Disable AWS Payload Extraction{% #disable-aws-payload-extraction %}

Setting these variables to an empty string or omitting them disables the feature:

```sh
DD_TRACE_CLOUD_REQUEST_PAYLOAD_TAGGING=""
DD_TRACE_CLOUD_RESPONSE_PAYLOAD_TAGGING=""
```

## Language-specific configuration{% #language-specific-configuration %}

Each tracer implementation provides additional configuration options specific to that language.

{% tab title="Node.js" %}
### Supported services{% #supported-services %}

The following services are supported by default:

- SNS
- SQS
- Kinesis
- S3
- EventBridge
- DynamoDB

{% alert level="info" %}
To request support for additional services, open a feature request with the [Datadog Support](https://docs.datadoghq.com/help/) team.
{% /alert %}

### Default redaction rules{% #default-redaction-rules %}

The Node.js tracer applies redaction rules on a per-service basis. For example:

- The `$.Endpoint` field is redacted only for SNS service requests.
- Other tracers redact this field across all services.

{% /tab %}

{% tab title="Python" %}
### Supported services{% #supported-services %}

The following services are supported by default:

- SNS
- SQS
- Kinesis
- S3
- EventBridge
- DynamoDB

#### Configure services{% #configure-services %}

To enable tag extraction for additional services, use this environment variable:

```sh
# Default values
DD_TRACE_CLOUD_PAYLOAD_TAGGING_SERVICES=s3,sns,sqs,kinesis,eventbridge
```

Add services by appending to the comma-separated list. For example, to add support for AWS Amplify:

```sh
DD_TRACE_CLOUD_PAYLOAD_TAGGING_SERVICES=s3,sns,sqs,kinesis,eventbridge,dynamodb,amplify
```

{% alert level="danger" %}
Added services do not include default redactions. Test your application in staging to identify and configure necessary redactions.
{% /alert %}

#### Service naming{% #service-naming %}

Service names are case-sensitive and use lowercase. To find valid service names:

1. Visit the [Boto3 Available Services](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/index.html) page.
1. Click the service name you want to use.
1. Use the service name from the `boto3.client()` call.

### Configure the number of extracted tags{% #configure-the-number-of-extracted-tags %}

Control the maximum number of extracted tags with:

```sh
# Default value
DD_TRACE_CLOUD_PAYLOAD_TAGGING_MAX_TAGS=758
```

{% alert level="danger" %}
The default value (758) is the maximum the Datadog Agent can accept. Increasing this value is not recommended.
{% /alert %}

{% /tab %}

{% tab title="Java" %}
### Supported services{% #supported-services %}

The following services are supported:

- SNS
- SQS
- Kinesis
- S3
- EventBridge
- API Gateway

#### Configure services{% #configure-services %}

To enable tag extraction for additional services, use this environment variable:

```sh
# Default values
DD_TRACE_CLOUD_PAYLOAD_TAGGING_SERVICES=ApiGateway,ApiGatewayV2,EventBridge,Sqs,Sns,S3,Kinesis
```

{% alert level="danger" %}
Added services do not include default redactions. Test your application in staging to identify and configure necessary redactions.
{% /alert %}

#### Service naming{% #service-naming %}

Service names are case-sensitive and use PascalCase. To find a service name:

1. Generate a trace that includes the AWS service.
1. Find the service span.
1. Look for the `aws_service` field.

For example:

- For AWS SSO, the resource name is `Sso.GetRoleCredentials`.
- The `aws_service` field shows `Sso`.
- Use `Sso` in your configuration.

### Configure the number of extracted tags{% #configure-the-number-of-extracted-tags %}

Control the maximum number of extracted tags with:

```sh
DD_TRACE_CLOUD_PAYLOAD_TAGGING_MAX_TAGS=758
```

{% alert level="danger" %}
The default value (758) is the maximum the Datadog Agent can accept. Increasing this value is not recommended.
{% /alert %}

{% /tab %}

## Best practices{% #best-practices %}

- Different tracers use different JSONPath implementations, so test your queries with each tracer individually.
- Always verify redaction behavior in a Staging environment before enabling in Production.

## Further reading{% #further-reading %}

- [Learn about Datadog APM tracing](https://docs.datadoghq.com/tracing/)
- [APM Terminology and Overview](https://docs.datadoghq.com/tracing/glossary/)
