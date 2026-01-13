# Source: https://docs.datadoghq.com/tracing/guide/serverless_enable_aws_xray.md

---
title: Enable AWS X-Ray Tracing
description: Trace your Lambda functions with AWS X-Ray
breadcrumbs: Docs > APM > Tracing Guides > Enable AWS X-Ray Tracing
source_url: https://docs.datadoghq.com/guide/serverless_enable_aws_xray/index.html
---

# Enable AWS X-Ray Tracing

## Enable AWS X-Ray{% #enable-aws-x-ray %}

**Prerequisite:** [Install the AWS integration](https://docs.datadoghq.com/integrations/amazon_web_services/#setup).

1. Ensure the following permissions are present in the policy document for your AWS/Datadog Role:

```text
xray:BatchGetTraces,
xray:GetTraceSummaries
```

The `BatchGetTraces` permission is used to return the full traces. The `GetTraceSummaries` permission is used to get a list of summaries of recent traces.

[Enable the X-Ray integration within Datadog](https://app.datadoghq.com/account/settings#integrations/amazon_xray).

If you are using a Customer Master Key to encrypt traces, add the `kms:Decrypt` method to your policy where the Resource is the Customer Master Key used for X-Ray.

**Note:** Enabling the AWS X-Ray integration increases the amount of consumed Indexed Spans which can increase your bill.

### Enabling AWS X-Ray for your functions{% #enabling-aws-x-ray-for-your-functions %}

To get the most out of the AWS X-Ray integration:

- Enable it on your Lambda functions and API Gateways, either using the Serverless Framework plugin or manually; and
- Install the tracing libraries in your Lambda functions.

#### [Recommended] Datadog Serverless Framework plugin{% #recommended-datadog-serverless-framework-plugin %}

The [Datadog Serverless Framework plugin](https://github.com/DataDog/serverless-plugin-datadog) automatically enables X-Ray for your Lambda functions and API Gateway instances. The plugin also automatically adds the [Datadog Lambda Layer](https://docs.datadoghq.com/integrations/amazon_lambda/?tab=python#installing-and-using-the-datadog-layer) to all of your Node.js and Python functions.

[Get started with the Serverless Framework plugin](https://www.datadoghq.com/blog/serverless-framework-plugin) and [read the docs](https://github.com/DataDog/serverless-plugin-datadog).

Lastly, install and import the X-Ray client library in your Lambda function.

#### Manual setup{% #manual-setup %}

If you do not use the Serverless Framework to deploy your serverless application, follow these instructions for manual setup:

1. Navigate to the Lambda function in the AWS console you want to instrument. In the "Debugging and error handling" section, check the box to **Enable active tracing**. This turns on X-Ray for that function.
1. Navigate to the [API Gateway console](https://console.aws.amazon.com/apigateway/). Select your API and then the stage.
1. On the **Logs/Tracing** tab, select **Enable X-Ray Tracing**.
1. To make these changes take effect, go to **Resources** in the left navigation panel and select **Actions** and click **Deploy API**.

**Note:** The Datadog Lambda Layer and client libraries include the X-Ray SDK as a dependency, so you don't need to explicitly install it in your projects.

Lastly, install and import the X-Ray client library in your Lambda function.

#### Installing the X-Ray client libraries{% #installing-the-x-ray-client-libraries %}

The X-Ray client library offers insights into your HTTP requests to APIs and into calls to DynamoDB, S3, MySQL and PostgreSQL (self-hosted, Amazon RDS, and Amazon Aurora), SQS, and SNS.

Install the library, import it into your Lambda projects, and patch the services you wish to instrument.

{% tab title="Node.js" %}
Install the X-Ray tracing library:

```bash

npm install aws-xray-sdk

# for Yarn users
yarn add aws-xray-sdk
```

To instrument the AWS SDK:

```js
var AWSXRay = require('aws-xray-sdk-core');
var AWS = AWSXRay.captureAWS(require('aws-sdk'));
```

To instrument all downstream HTTP calls:

```js
var AWSXRay = require('aws-xray-sdk');
AWSXRay.captureHTTPsGlobal(require('http'));
var http = require('http');
```

To instrument PostgreSQL queries:

```js
var AWSXRay = require('aws-xray-sdk');
var pg = AWSXRay.capturePostgres(require('pg'));
var client = new pg.Client();
```

To instrument MySQL queries:

```js
var AWSXRay = require('aws-xray-sdk');
var mysql = AWSXRay.captureMySQL(require('mysql'));
//...
var connection = mysql.createConnection(config);
```

For further configuration, creating subsegments, and recording annotations, see the [X-Ray Node.js docs](https://docs.aws.amazon.com/en_pv/xray/latest/devguide/xray-sdk-nodejs.html).
{% /tab %}

{% tab title="Python" %}
Install the X-Ray tracing library:

```bash
pip install aws-xray-sdk
```

To patch [all libraries](https://docs.aws.amazon.com/en_pv/xray/latest/devguide/xray-sdk-python-patching.html) by default, add the following to the file containing your Lambda handlers:

```python
from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.core import patch_all
patch_all()
```

Note that tracing `aiohttp` requires [specific instrumentation](https://docs.aws.amazon.com/en_pv/xray/latest/devguide/xray-sdk-python-httpclients.html).

For further configuration, creating subsegments, and recording annotations, see the [X-Ray Python docs](https://docs.aws.amazon.com/en_pv/xray/latest/devguide/xray-sdk-python.html).
{% /tab %}

{% tab title="Go" %}
See:

- [X-Ray SDK for Go docs](https://docs.aws.amazon.com/en_pv/xray/latest/devguide/xray-sdk-go.html).

{% /tab %}

{% tab title="Ruby" %}
See:

- [X-Ray SDK for Ruby docs](https://docs.aws.amazon.com/en_pv/xray/latest/devguide/xray-sdk-ruby.html).

{% /tab %}

{% tab title="Java" %}
See:

- [X-Ray SDK for Java docs](https://docs.aws.amazon.com/en_pv/xray/latest/devguide/xray-sdk-java.html).

{% /tab %}

{% tab title=".NET" %}
See:

- [X-Ray SDK for .Net docs](https://docs.aws.amazon.com/en_pv/xray/latest/devguide/xray-sdk-dotnet.html).

{% /tab %}
