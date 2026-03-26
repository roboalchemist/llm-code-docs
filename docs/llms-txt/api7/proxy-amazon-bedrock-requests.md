# Source: https://docs.api7.ai/apisix/how-to-guide/ai-gateway/proxy-amazon-bedrock-requests.md

# Proxy Amazon Bedrock Requests

[Amazon Bedrock](https://aws.amazon.com/bedrock/) is a fully managed service that offers a wide range of high-performing [foundation models (FMs)](https://aws.amazon.com/what-is/foundation-models/) from leading AI companies such as Anthropic, AI21 Labs, Cohere, Meta, Mistral AI, Stability AI, and Amazon. These models are made available through Bedrock in a single API, empowering organizations to build cutting-edge AI solutions with ease.

This guide will walk you through the process of integrating APISIX with Amazon Bedrock. You will be setting up a [Lambda function](https://aws.amazon.com/pm/lambda) on AWS to interact with [Claude 3 Opus model on Bedrock](https://aws.amazon.com/bedrock/claude/), configuring the necessary Identity and access management (IAM) permissions, and creating an APISIX route to the function URL using the [`aws-lambda`](https://docs.api7.ai/hub/aws-lambda.md) plugin, which implements [AWS Signature Version 4](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html).

![architecture diagram](https://static.api7.ai/uploads/2024/04/24/hcpEI780_bedrock.png)

## Prerequisite(s)[â](#prerequisites "Direct link to Prerequisite(s)")

* Have an AWS account and log in as an IAM user.
* Install [Docker](https://docs.docker.com/get-docker/).
* Install [cURL](https://curl.se/) to send requests to the services for validation.
* Follow the [Getting Started Tutorial](https://docs.api7.ai/apisix/getting-started/.md) to start a new APISIX instance in Docker or on Kubernetes.

## Select Foundation Models (FMs)[â](#select-foundation-models-fms "Direct link to Select Foundation Models (FMs)")

Log into your **AWS console**, go to the Amazon Bedrock service, and request access for one or more models you would like to integrate with:

![request model access](https://static.api7.ai/uploads/2024/04/23/XEhGkZVA_manage-mode-access.png)

The following document will use Anthropic Claude 3 Opus model as an example. Note that not all models are available in all regions. At the time of writing, Anthropic Claude 3 Opus is only available in `us-west-2`. See [model regions](https://docs.aws.amazon.com/bedrock/latest/userguide/models-regions.html) for reference and adjust your AWS account region as needed.

## Create IAM Access Keys[â](#create-iam-access-keys "Direct link to Create IAM Access Keys")

Go to **AWS Identity and Access Management (IAM)** and select the user account you would like to use for integration:

![select IAM user](https://static.api7.ai/uploads/2024/04/23/8AToZtz9_select-iam-user.png)

In the **security credentials** tab, select **create access key**:

![create access keys](https://static.api7.ai/uploads/2024/04/23/1K9FiWb4_create-access-key.png)

Select **application running outside AWS** as the use case:

![select use case](https://static.api7.ai/uploads/2024/04/23/Fa4jdK5H_iam-user-use-case.png)

Continue the credential creation and note down the access key and secret access key:

![save access keys](https://static.api7.ai/uploads/2024/04/23/zGCyqp20_save-access-key.png)

## Create Lambda Function[â](#create-lambda-function "Direct link to Create Lambda Function")

Go to AWS **Lambda** and create a new function with Node.js runtime. You can also choose other runtime and write your own code.

### Develop Function Code[â](#develop-function-code "Direct link to Develop Function Code")

Paste the following code into the Lambda function:

```
import { BedrockRuntimeClient, InvokeModelCommand } from "@aws-sdk/client-bedrock-runtime";

// replace with your model information
const aws_region = "us-west-2";
const model_id = "anthropic.claude-3-opus-20240229-v1:0"
const anthropic_version = "bedrock-2023-05-31"

// create a bedrock client in the selected region
const bedrockClient = new BedrockRuntimeClient({ region: aws_region });

export const handler = async (event) => {
    // get model prompt from model_input in the request body
    const requestBody = JSON.parse(event.body);
    const model_input = requestBody.model_input;
    // put together model parameters
    const params = {
        modelId: model_id,
        contentType: "application/json",
        accept: "application/json",
        body: JSON.stringify({
            anthropic_version: anthropic_version,
            max_tokens: 2048,
            messages: [{
                role: "user",
                content: `${model_input}`
            }]
        })
    }
    // attempt sending requests to bedrock
    const cmd = new InvokeModelCommand(params);
    try {
        const resp = await bedrockClient.send(cmd);
        const textDecoder = new TextDecoder("utf-8");
        const resp_body = JSON.parse(textDecoder.decode(resp.body));
        return resp_body.content[0].text;
    } catch (err) {
        console.error("Error invoking Bedrock:", err);
        throw err;
    }
};
```

This function accepts a model prompt from a user input `model_input` in the request body.

### Configure Function Permission[â](#configure-function-permission "Direct link to Configure Function Permission")

In this step, you will attach the needed permission to the Lambda function so that it can invoke Bedrock models.

Go to the **Configuration** tab of the Lambda function and under **Permissions**, click on the role name to open the IAM page for the function:

![configure lambda function permission](https://static.api7.ai/uploads/2024/04/23/WnnOFaHR_lambda-function-permission.png)

Click on the **Add permissions** dropdown and select **Create incline policy**:

![create incline policy](https://static.api7.ai/uploads/2024/04/23/Tk5lQxkk_add-inline-policy.png)

Add the following policy to the **policy editor** and save:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "bedrock:InvokeModel"
      ],
      "Resource": "*"
    }
  ]
}
```

This allows the Lambda function to invoke Bedrock models only without provisioning the full permissions.

### Adjust Function Timeouts[â](#adjust-function-timeouts "Direct link to Adjust Function Timeouts")

By default, Lambda function times out in 3 seconds, and it is sometimes it is not sufficient time for model to process user requests and respond back.

To increase the timeout value, go to the **Configuration** tab of the Lambda function and under **General configuration**, edit the timeout to a larger value, such as 30 seconds:

![adjust timeout value](https://static.api7.ai/uploads/2024/04/23/HVizFIh0_adjust-function-timeout.png)

### Create Function URL[â](#create-function-url "Direct link to Create Function URL")

To integrate with the Lambda function, the function should have a public URL. Go to the **Configuration** tab of the Lambda function and under **Function URL**, create a function URL:

![create function URL](https://static.api7.ai/uploads/2024/04/23/3fF90ws2_function-url.png)

## Configure APISIX[â](#configure-apisix "Direct link to Configure APISIX")

Create a route in APISIX and configure the `aws-lambda` plugin:

* Admin API
* ADC

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT -d '
{
  "id": "aws-bedrock",
  "uri": "/bedrock-claude",
  "plugins": {
    "aws-lambda": {
      "function_uri": "https://jbihqn4bfwewf4nfrz6typjmcvjh40iuamw.lambda-url.us-west-2.on.aws/",
      "authorization": {
        "iam": {
          "accesskey": "AKIAIOSFODNN7EXAMPLE",
          "secretkey": "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",
          "aws_region": "us-west-2",
          "service": "lambda"
        }
      },
      "timeout": 30000,
      "ssl_verify": false
    }
  }
}'
```

â¶ Replace with your Lambda function URL.

â· Replace with your IAM access key.

â¸ Replace with your IAM secret access key.

â¹ Set to the AWS region of your Lambda function.

âº Set to the service receiving the request.

â» Configure timeout in milliseconds.

adc.yaml

```
services:
  - name: Amazon Bedrock Service
    routes:
      - uris:
          - /bedrock-claude
        name: bedrock-claude
        plugins:
          aws-lambda:
            function_uri: 'https://jbihqn4bfwewf4nfrz6typjmcvjh40iuamw.lambda-url.us-west-2.on.aws/'
            authorization:
              iam:
                accesskey: AKIAIOSFODNN7EXAMPLE
                secretkey: 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
                aws_region: us-west-2
                service: lambda
            timeout: 30000
            ssl_verify: false
```

â¶ Replace with your Lambda function URL.

â· Replace with your IAM access key.

â¸ Replace with your IAM secret access key.

â¹ Set to the AWS region of your Lambda function.

âº Set to the service receiving the request.

â» Configure timeout in milliseconds.

Synchronize the configuration to APISIX:

```
adc sync -f adc.yaml
```

## Verify[â](#verify "Direct link to Verify")

Send a request to the route with a prompt in the request body:

```
curl -i "http://127.0.0.1:9080/bedrock-claude" -X POST \
  -H "Content-Type: application/json" \
  -d '{"model_input": "Write a 50 word introduction of Frida Khalo"}'
```

You should receive an `HTTP/1.1 200 OK` response with the model output:

```
Frida Kahlo (1907-1954) was a Mexican artist known for her striking self-portraits and vivid expressions of pain, resilience, and identity. Despite facing numerous challenges, including a devastating bus accident and a turbulent marriage to fellow artist Diego Rivera, Kahlo's unique style and powerful imagery have made her an iconic figure in art history.
```

## Next Steps[â](#next-steps "Direct link to Next Steps")

You have now learned how to integrate APISIX with Amazon Bedrock FMs.

If you would like to proxy streamed responses from Amazon Bedrock, you can use the [proxy-buffering](https://docs.api7.ai/hub/proxy-buffering.md) plugin to disable NGINX's `proxy_buffering` directive to avoid server-sent events (SSE) being buffered.

Additionally, you can integrate more capabilities that APISIX offers, such as [rate limiting](https://docs.api7.ai/apisix/how-to-guide/traffic-management/rate-limiting.md) and [caching](https://docs.api7.ai/hub/proxy-cache.md), to regulate API usage and improve user experience.
