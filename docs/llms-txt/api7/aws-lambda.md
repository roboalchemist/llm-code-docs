# Source: https://docs.api7.ai/hub/aws-lambda.md

# aws-lambda

The `aws-lambda` plugin eases the integration of APISIX with [AWS Lambda](https://aws.amazon.com/lambda/) and [Amazon API gateway](https://aws.amazon.com/api-gateway/) to proxy for other AWS services.

The plugin supports authentication and authorization with AWS via IAM user credentials and API gateway's API key.

## Examples[â](#examples "Direct link to Examples")

The examples below demonstrate how you can configure `aws-lambda` for different scenarios.

To follow along the examples, please first log into your AWS console and create a Lambda function with any runtime. You do not need to customize the function and by default, the function should return `Hello from Lambda!` when called.

### Invoke Lambda Function Securely using IAM Access Keys[â](#invoke-lambda-function-securely-using-iam-access-keys "Direct link to Invoke Lambda Function Securely using IAM Access Keys")

The following example demonstrates how you can integrate APISIX with the Lambda function and configure IAM access keys for authorization. The `aws-lambda` plugin implements [AWS Signature Version 4](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html) for IAM access keys. You will be first creating IAM access keys and the Lambda function URL on AWS console.

For IAM access keys, go to **AWS Identity and Access Management (IAM)** and click into the user you would like to use for integration.

Next, in the **security credentials** tab, select **create access key**:

![create access keys](https://static.api7.ai/uploads/2024/04/23/1K9FiWb4_create-access-key.png)

Select **application running outside AWS** as the use case:

![select use case](https://static.api7.ai/uploads/2024/04/23/Fa4jdK5H_iam-user-use-case.png)

Continue the credential creation and note down the access key and secret access key:

![save access keys](https://static.api7.ai/uploads/2024/04/23/zGCyqp20_save-access-key.png)

To create the Lambda function URL, go to the **Configuration** tab of the Lambda function and under **Function URL**, create a function URL:

![create function URL](https://static.api7.ai/uploads/2024/04/23/3fF90ws2_function-url.png)

Finally, create a route in APISIX with your function URL and IAM access keys:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "aws-lambda-route",
    "uri": "/aws-lambda",
    "plugins": {
      "aws-lambda": {
        "function_uri": "https://jbihqn4bfwewfrz6typjmcvjh40iuamw.lambda-url.us-west-2.on.aws/",
        "authorization": {
          "iam": {
            "accesskey": "AKIARK7HKSJVWCOIIMW6",
            "secretkey": "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",
            "aws_region": "us-west-2",
            "service": "lambda"
          }
        },
        "ssl_verify": false
      }
    }
  }'
```

â¶ replace with your Lambda function URL

â· replace with your IAM access key

â¸ replace with your IAM secret access key

â¹ replace with the AWS region of your Lambda function

âº set to `lambda` when integrating with Lambda function

Send a request to the route:

```
curl -i "http://127.0.0.1:9080/aws-lambda"
```

You should receive an `HTTP/1.1 200 OK` response with the following message:

```
"Hello from Lambda!"
```

### Integrate with Amazon API Gateway Securely with API Key[â](#integrate-with-amazon-api-gateway-securely-with-api-key "Direct link to Integrate with Amazon API Gateway Securely with API Key")

The following example demonstrates how you can integrate APISIX with Amazon API gateway and configure the gateway to trigger the execution of Lambda function.

To configure an API gateway as a Lambda trigger, go to your Lambda function and select **Add trigger**:

![add trigger for lambda function](https://static.api7.ai/uploads/2024/04/25/UjI9bLDQ_add-trigger.png)

Next, select **API Gateway** as the trigger and **REST API** as the API type, and finish adding the trigger:

![select REST to be the API type and secure the API with API key](https://static.api7.ai/uploads/2024/04/25/4Bp9r3UP_rest-api-key.png)

<br />

info

The Amazon API gateway supports two types of RESTful APIs: HTTP APIs and REST APIs. Only REST APIs offer API key and IAM as security measures.

You should now be redirected back to the Lambda interface. To find the API key and gateway API endpoint, go to the **Configuration** tab of the Lambda function and under **Triggers**, you can find the details of the API gateway:

![API gateway endpoint and API key](https://static.api7.ai/uploads/2024/04/25/6bjpeNIb_api-gateway-info.png)

Finally, create a route in APISIX with your gateway endpoint and API key:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "aws-lambda-route",
    "uri": "/aws-lambda",
    "plugins": {
      "aws-lambda": {
        "function_uri": "https://xwbs1bjiy3.execute-api.us-west-2.amazonaws.com/default/api7-docs",
        "authorization": {
          "apikey": "hpr8KdMxlR37p0Sq8aIhi28cq2thilcF5wziOsvJ"
        },
        "ssl_verify":false
      }
    }
  }'
```

Send a request to the route:

```
curl -i "http://127.0.0.1:9080/aws-lambda"
```

You should receive an `HTTP/1.1 200 OK` response with the following message:

```
"Hello from Lambda!"
```

If your API key is invalid, you should receive an `HTTP/1.1 403 Forbidden` response.

### Forward Requests to Amazon API Gateway Sub-Paths[â](#forward-requests-to-amazon-api-gateway-sub-paths "Direct link to Forward Requests to Amazon API Gateway Sub-Paths")

The following example demonstrates how you can forward requests to a sub-path of the Amazon API gateway API and configure the API to trigger the execution of Lambda function.

Please follow the [previous example](#integrate-with-amazon-api-gateway-securely-with-api-key) to set up an API gateway first.

To create a sub-path, go to the **Configuration** tab of the Lambda function and under **Triggers**, click into the API gateway:

![click into the API gateway](https://static.api7.ai/uploads/2024/04/26/5Twffgyr_click-into-adjusted.png)

Next, select **Create resource** to create a sub-path:

![create resource](https://static.api7.ai/uploads/2024/04/26/hXlnuVwk_create-resource.png)

Enter the sub-path information and complete creation:

![complete resource creation](https://static.api7.ai/uploads/2024/04/26/7t1yiWjl_create-resource-2.png)

Once redirected back to the main gateway console, you should see the newly created path. Select **Create method** to configure HTTP methods for the path and the associated action:

![click on create method](https://static.api7.ai/uploads/2024/04/26/3rZZJy3e_create-method.png)

Select the allowed HTTP method in the dropdown. For the purpose of demonstration, this example continues to use the same Lambda function as the triggered action when the path is requested:

![create method and lambda function](https://static.api7.ai/uploads/2024/04/26/vni7yS2q_create%20method%202.png)

Finish the method creation. Once redirected back to the main gateway console, click on **Deploy API** to deploy the path and method changes:

![deploy changes to API gateway](https://static.api7.ai/uploads/2024/04/26/2vrqnVPB_deploy-api.png)

Finally, create a route in APISIX with your gateway endpoint and API key:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "aws-lambda-route",
    "uri": "/aws-lambda/*",
    "plugins": {
      "aws-lambda": {
        "function_uri": "https://xwbs1bjiy3.execute-api.us-west-2.amazonaws.com/default",
        "authorization": {
          "apikey": "hpr8KdMxlR37p0Sq8aIhi28cq2thilcF5wziOsvJ"
        },
        "ssl_verify":false
      }
    }
  }'
```

â¶ match all sub-paths of `/aws-lambda/`

â· the sub-paths matched by the wildcard `*` will be appended to the end of the `function_uri`

Send a request to the route:

```
curl -i "http://127.0.0.1:9080/aws-lambda/api7-docs"
```

APISIX will forward the request to `https://xwbs1bjiy3.execute-api.us-west-2.amazonaws.com/default/api7-docs` and you should receive an `HTTP/1.1 200 OK` response with the following message:

```
"Hello from Lambda!"
```

If your API key is invalid or if the requested path is not associated with any method, you should receive an `HTTP/1.1 403 Forbidden` response.
