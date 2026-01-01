---
---
title: AWS Lambda Container Image
description: "Learn how to set up Sentry with a Container Image."
---

The Python AWS Lambda Container Image is deprecated.

Please instrument your AWS Lambda function in one of the following ways instead:

- **Without touching your code:**
    This method can be instrumented from the Sentry product by those who have access to the AWS infrastructure and doesn't require that you make any direct updates to the code. See the [AWS Lambda guide](/organization/integrations/cloud-monitoring/aws-lambda/).
- **By adding the Sentry Lambda Layer to your function manually:**
    While this is a quick way to add Sentry to your AWS Lambda function, it gives you limited configuration possibilities with environment vars. See AWS Lambda Layer.
- **By manually adding Sentry to your function code:**
    This method requires that you install the Sentry SDK into your AWS Lambda function packages. While it takes more effort to set up, it gives you full control of your setup and manual instrumentation. See AWS Lambda manual instrumentation.

As an alternative setup method, you can add Sentry to your [Container Image](https://docs.aws.amazon.com/lambda/latest/dg/images-create.html). To import Sentry's Layer Image, add the following to your Dockerfile:

```docker {tabTitle: Dockerfile}
COPY --from=public.ecr.aws/sentry/sentry-python-serverless-sdk: /opt/ /opt
```

Replace `VERSION` with a specific version number (for example, 6). You can see a complete list of available versions in Sentry's [Amazon ECR repository](https://gallery.ecr.aws/sentry/sentry-python-serverless-sdk).

## Function Configuration

Set your image’s CMD value to the Sentry Handler:

```docker {tabTitle: Dockerfile}
CMD ["sentry_sdk.integrations.init_serverless_sdk.sentry_lambda_handler"]
```

Next, set the following environment variables in AWS:

- Set `SENTRY_INITIAL_HANDLER` to the path of your function handler
- Set `SENTRY_DSN` to your Sentry DSN
- Set `SENTRY_TRACES_SAMPLE_RATE` to your preferred [sampling rate](/platforms/python/configuration/sampling/#sampling-transaction-events) for transactions

Alternatively, you can also set the environment variables in your Dockerfile. Values set in AWS override the values in a Dockerfile if both are provided.

```docker {tabTitle: Dockerfile}
ENV SENTRY_INITIAL_HANDLER=""
ENV SENTRY_DSN="___PUBLIC_DSN___"
ENV SENTRY_TRACES_SAMPLE_RATE="1.0"
```
