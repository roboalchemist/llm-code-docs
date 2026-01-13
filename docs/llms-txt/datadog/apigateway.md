# Source: https://docs.datadoghq.com/tracing/trace_collection/proxy_setup/apigateway.md

---
title: Instrumenting Amazon API Gateway
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > APM > Application Instrumentation > Tracing a Proxy > Instrumenting
  Amazon API Gateway
source_url: https://docs.datadoghq.com/trace_collection/proxy_setup/apigateway/index.html
---

# Instrumenting Amazon API Gateway

{% callout %}
##### Tracing for Amazon API Gateway is in Preview

This feature is in Preview.
{% /callout %}

Datadog APM can create **inferred spans** for requests that pass through Amazon API Gateway to container- or EC2-hosted services. The spans power end-to-end traces, service maps, and sampling based on the gateway itself.

{% alert level="warning" %}
If your API Gateway integrates with AWS Lambda, do not follow the instructions on this page. [Datadog Lambda layers](https://docs.datadoghq.com/serverless/aws_lambda/installation/) already emit inferred API Gateway spans; adding the proxy headers described here can create duplicate or conflicting traces.
{% /alert %}

### Prerequisites{% #prerequisites %}

- Amazon API Gateway is deployed as a [REST API](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-rest-api.html) (v1) or [HTTP API](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api.html) (v2).

**Note**: If using HTTP API (v2), `context.requestTimeEpoch` provides second-level granularity, unlike REST APIs (v1) which provide millisecond precision. This means span duration is approximate.

- `DD_TRACE_INFERRED_PROXY_SERVICES_ENABLED` is set in the application container:

  ```shell
    export DD_TRACE_INFERRED_PROXY_SERVICES_ENABLED=true
    
```



Alternatively, enable it through the Datadog ECS Fargate CDK construct:

  ```typescript
    new DatadogECSFargate(this, 'Datadog', {
      apm: { isEnabled: true, traceInferredProxyServices: true },
    });
    
  ```



Or you can enable it through the Datadog ECS Fargate Terraform module:

  ```typescript
    module "ecs_fargate_task" { 
      dd_apm = {
        enabled = true,
        trace_inferred_proxy_services = true
      }
    }
    
  ```



- Your underlying application is running a supported web framework.

- Your application tracer meets the minimum version.

#### Supported versions and web frameworks{% #supported-versions-and-web-frameworks %}

| Runtime | Datadog Tracer    | Tracer version                                                                                                                                     | Frameworks                                                                                                                                                                                  |
| ------- | ----------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Node.js | `dd-trace-js`     | v[4.50.0](https://github.com/DataDog/dd-trace-js/releases/tag/v4.50.0)+ or v[5.26.0](https://github.com/DataDog/dd-trace-js/releases/tag/v5.26.0)+ | express, fastify, hapi, koa, microgateway-core, next, paperplane, restify, router, apollo                                                                                                   |
| Go      | `dd-trace-go`     | v[1.72.1](https://github.com/DataDog/dd-trace-go/releases/tag/v1.72.1)+                                                                            | chi, httptreemux, echo, go-restful, fiber, gin, gorilla mux, httprouter, fasthttp, goji                                                                                                     |
| Python  | `dd-trace-py`     | v[3.1.0](https://github.com/DataDog/dd-trace-py/releases/tag/v3.1.0)+                                                                              | aiohttp, asgi, bottle, cherrypy, django, djangorestframework, falcon, fastapi, flask, molten, pyramid, sanic, starlette, tornado, wsgi                                                      |
| PHP     | `dd-trace-php`    | v[1.8.0](https://github.com/DataDog/dd-trace-php/releases/tag/1.8.0)+                                                                              | CakePHP, CodeIgniter, Drupal, FuelPHP, Laminas, Laravel, Lumen, Magento, Neos Flow, Phalcon, Roadrunner, Slim, Symfony, WordPress, Zend Framework                                           |
| .NET    | `dd-trace-dotnet` | v[3.15.0](https://github.com/DataDog/dd-trace-dotnet/releases/tag/v3.15.0)+                                                                        | ASP.NET, ASP.NET Core                                                                                                                                                                       |
| Java    | `dd-trace-java`   | v[1.56.0](https://github.com/DataDog/dd-trace-java/releases/tag/v1.56.0)+                                                                          | akka-http, axway-api, azure-functions, finatra, grizzly, jetty, liberty, micronaut, netty, pekko-http, play, ratpack, restlet, servlet, spring-web, spray, synapse, tomcat, undertow, vertx |

## Setup{% #setup %}

{% tab title="REST API (v1)" %}
To create inferred spans, API Gateway must pass the following headers to your backend services:

| Header                       | Value                                                       |
| ---------------------------- | ----------------------------------------------------------- |
| `x-dd-proxy`                 | `'aws-apigateway'`**Note**: Single quotes must be included. |
| `x-dd-proxy-request-time-ms` | `context.requestTimeEpoch`                                  |
| `x-dd-proxy-domain-name`     | `context.domainName`                                        |
| `x-dd-proxy-httpmethod`      | `context.httpMethod`                                        |
| `x-dd-proxy-path`            | `context.path`                                              |
| `x-dd-proxy-stage`           | `context.stage`                                             |

To pass in the required headers, you can use the AWS CDK or AWS Console:

{% collapsible-section #id-for-anchoring %}
#### AWS CDK

Add the headers under `requestParameters` and use `$context` variables:

```gdscript3
import { DatadogAPIGatewayRequestParameters } from "datadog-cdk-constructs-v2";

// Datadog integration definition
const ddIntegration = new apigateway.Integration({
  type: apigateway.IntegrationType.HTTP_PROXY,
  integrationHttpMethod: "ANY",
  options: {
    connectionType: apigateway.ConnectionType.INTERNET,
    requestParameters: DatadogAPIGatewayRequestParameters,
  },
  uri: `http://${loadBalancer.loadBalancerDnsName}`,
});

const api = new apigateway.RestApi(this, "MyApi", {
  restApiName: "my-api-gateway",
  deployOptions: { stageName: "prod" },
  defaultIntegration: ddIntegration, // Datadog instrumentation applied here
});
```

{% /collapsible-section %}

{% collapsible-section #id-for-anchoring %}
#### AWS Console

1. In the AWS Management Console, navigate to API Gateway and go to your API's **Resources** page.

1. Go to **Integration request** and click **Edit**.

1. Under **Edit integration request**, go to **URL request headers parameters**. Click **Add request header parameter**.

{% image
   source="https://datadog-docs.imgix.net/images/tracing/trace_collection/apigateway/console_headers.718ed8507ca5680f20ce36bf85842769.png?auto=format"
   alt="Your HTTP headers for your API in API Gateway, after you have added all six header parameters." /%}

{% /collapsible-section %}

{% /tab %}

{% tab title="HTTP API (v2)" %}
To create inferred spans, API Gateway must pass the following headers to your backend services:

| Header                       | Value                            |
| ---------------------------- | -------------------------------- |
| `x-dd-proxy`                 | `aws-apigateway`                 |
| `x-dd-proxy-request-time-ms` | `${context.requestTimeEpoch}000` |
| `x-dd-proxy-domain-name`     | `$context.domainName`            |
| `x-dd-proxy-httpmethod`      | `$context.httpMethod`            |
| `x-dd-proxy-path`            | `$context.path`                  |
| `x-dd-proxy-stage`           | `$context.stage`                 |

**Note**: `context.requestTimeEpoch` returns a timestamp in seconds in v2 APIs. Datadog expects milliseconds, so you must multiply it by 1000 by appending `000`.

Attach the parameter mapping that injects the headers:

```typescript
   import { DatadogAPIGatewayV2ParameterMapping }
     from 'datadog-cdk-constructs-v2';

   const ddIntegration = new apigatewayv2_integrations.HttpUrlIntegration(
     'HttpUrlIntegration',
     'https://example.com',
     { parameterMapping: DatadogAPIGatewayV2ParameterMapping },
   );

   new apigatewayv2.HttpApi(this, 'HttpApi', {
     apiName: 'my-http-api',
     routes: [{
       path: '/{proxy+}',
       methods: [apigatewayv2.HttpMethod.ANY],
       integration: ddIntegration,
     }],
   });
```

{% /tab %}

## Update sampling rules{% #update-sampling-rules %}

Head-based sampling still applies when using API Gateway tracing. Because the inferred span becomes the new trace root, update your rules so the service value matches the API Gateway service name shown in Datadog.

For example, if the original sampling rule is:

```shell
# before: sampled upstream service
DD_TRACE_SAMPLING_RULES='[{"service":"pythonapp","sample_rate":0.5}]'
```

Update the rule in one of the following ways:

1. Change the `service` value to match your API Gateway's name as it appears in Datadog:

   ```shell
      # option 1: sample the gateway root span
      DD_TRACE_SAMPLING_RULES='[{"service":"my-api-gateway","sample_rate":0.5}]'
      
```

1. Remove the `service` key to apply the rule to all root spans:

   ```shell
      # option 2: apply to all roots
      DD_TRACE_SAMPLING_RULES='[{"sample_rate":0.5}]'
      
```

## Further Reading{% #further-reading %}

- [Tutorial - Enabling Tracing for a Go Application on Amazon ECS with Fargate](https://docs.datadoghq.com/tracing/guide/tutorial-enable-go-aws-ecs-fargate/)
- [Amazon ECS on AWS Fargate](https://docs.datadoghq.com/integrations/ecs_fargate/)
- [Amazon EKS on AWS Fargate](https://docs.datadoghq.com/integrations/eks_fargate)
