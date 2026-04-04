# Source: https://docs.aws.amazon.com/apigateway/latest/developerguide/llms.txt

# Amazon API Gateway Developer Guide

> Build, deploy, maintain and call cloud-based APIs using Amazon API Gateway with this Developer Guide.

- [Prerequisites](https://docs.aws.amazon.com/apigateway/latest/developerguide/setting-up.html)
- [Get started](https://docs.aws.amazon.com/apigateway/latest/developerguide/getting-started.html)
- [API Gateway ARNs](https://docs.aws.amazon.com/apigateway/latest/developerguide/arn-format-reference.html)
- [API references](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-ref.html)
- [Document history](https://docs.aws.amazon.com/apigateway/latest/developerguide/history.html)

## [What is Amazon API Gateway?](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html)

- [API Gateway use cases](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-overview-developer-experience.html): The following use cases section presents an overview of the different types of API Gateway APIs and the different kinds of developers who use API Gateway.
- [API Gateway concepts](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-basic-concept.html): Defines API Gateway basic concepts.
- [Choose between REST APIs and HTTP APIs](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-vs-rest.html): Learn the differences between REST APIs and HTTP APIs.
- [Get started with the REST API console](https://docs.aws.amazon.com/apigateway/latest/developerguide/getting-started-rest-new-console.html): Get started with the API Gateway REST API console.


## [Tutorials and workshops](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-tutorials.html)

### [REST API tutorials](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-rest-tutorials.html)

Use hands-on tutorials to learn about Amazon API Gateway REST APIs.

### [Choose a Lambda integration tutorial](https://docs.aws.amazon.com/apigateway/latest/developerguide/getting-started-with-lambda-integration.html)

Learn how to create and test an API to expose a Lambda function with the Lambda integration using the API Gateway console.

- [Tutorial: Create a REST API with a Lambda proxy integration](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-create-api-as-simple-proxy-for-lambda.html): Learn how to build and test an API with Lambda proxy integration using the API Gateway console.
- [Tutorial: Create a REST API with a Lambda non-proxy integration](https://docs.aws.amazon.com/apigateway/latest/developerguide/getting-started-lambda-non-proxy-integration.html): Learn how to create and test an API method to expose a Lambda function with the Lambda custom integration using the API Gateway console.
- [Tutorial: Create a REST API with a cross-account Lambda proxy integration](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-cross-account-lambda-integrations.html): Learn how to build and test an API with cross-account Lambda proxy integration using the API Gateway console.
- [Tutorial: Create a REST API by importing an example](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-create-api-from-example.html): Learn how to create an API in API Gateway with the help of an example.

### [Choose an HTTP integration tutorial](https://docs.aws.amazon.com/apigateway/latest/developerguide/getting-started-http-integrations.html)

Learn how to create an API with HTTP proxy integration or HTTP non-proxy integration.

- [Tutorial: Create a REST API with an HTTP proxy integration](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-create-api-as-simple-proxy-for-http.html): Build and test an API with HTTP proxy integration using the API Gateway console.
- [Tutorial: Create a REST API with an HTTP non-proxy integration](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-create-api-step-by-step.html): Learn how to create an API Gateway API with the HTTP custom integration using the API Gateway console.
- [Tutorial: Create a REST API with a private integration](https://docs.aws.amazon.com/apigateway/latest/developerguide/getting-started-with-private-integration.html): Create a private integration
- [Tutorial: Create a REST API with an AWS integration](https://docs.aws.amazon.com/apigateway/latest/developerguide/getting-started-aws-proxy.html): Learn how to integrate API Gateway with an AWS service proxy.

### [Tutorial: Create a calculator REST API with three integrations](https://docs.aws.amazon.com/apigateway/latest/developerguide/integrating-api-with-aws-services-lambda.html)

Learn two ways to configure a REST API in Amazon API Gateway as a service proxy for AWS Lambda.

- [OpenAPI definitions of a sample API for a Lambda function](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-as-lambda-proxy-export-swagger-with-extensions.html)

### [Tutorial: Create a REST API as an Amazon S3 proxy](https://docs.aws.amazon.com/apigateway/latest/developerguide/integrating-api-with-aws-services-s3.html)

Learn how to create and configure a REST API in API Gateway as an Amazon S3 proxy.

- [OpenAPI definitions of a sample API as an Amazon S3 proxy](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-as-s3-proxy-export-swagger-with-extensions.html): The following OpenAPI definitions describes an API that works as an Amazon S3 proxy.
- [Call the API using a REST API client](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-as-s3-proxy-test-using-postman.html): To provide an end-to-end tutorial, we now show how to call the API using Postman, which supports the AWS IAM authorization.

### [Tutorial: Create a REST API as an Amazon Kinesis proxy](https://docs.aws.amazon.com/apigateway/latest/developerguide/integrating-api-with-aws-services-kinesis.html)

Learn how to create and configure a REST API in API Gateway as an AWS proxy for Kinesis.

- [OpenAPI definitions of a sample API as a Kinesis proxy](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-as-kinesis-proxy-export-swagger-with-extensions.html): A sample API as a Kinesis proxy in OpenAPI Specification.
- [Tutorial: Create a REST API using AWS SDKs or the AWS CLI](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-create-api-cli-sdk.html): Create and test an edge-optimized API using an AWS SDKs or the AWS CLI
- [Tutorial: Create a private REST API](https://docs.aws.amazon.com/apigateway/latest/developerguide/private-api-tutorial.html): Learn to create a private REST API in API Gateway that is only accessible from within an Amazon VPC.

### [HTTP API tutorials](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-http-tutorials.html)

Provide hands-on tutorials to learn about Amazon API Gateway HTTP APIs.

- [Tutorial: Build a CRUD HTTP API with Lambda and DynamoDB](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-dynamo-db.html): Learn to create an Amazon API Gateway HTTP API that invokes an AWS Lambda function to create, update, or delete data in Amazon DynamoDB.
- [Tutorial: Create an HTTP API with a private integration to Amazon ECS](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-private-integration.html): Learn to create an Amazon API Gateway HTTP API that uses a VPC link to integrate with an Amazon ECS service in an Amazon VPC.

### [WebSocket API tutorials](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-websocket-tutorials.html)

Provide hands-on tutorials to learn about Amazon API Gateway WebSocket APIs.

- [Tutorial: Create a WebSocket chat app](https://docs.aws.amazon.com/apigateway/latest/developerguide/websocket-api-chat-app.html): Learn to create a serverless chat application that uses an API Gateway WebSocket API.
- [Tutorial: Create a WebSocket API with an AWS integration](https://docs.aws.amazon.com/apigateway/latest/developerguide/websocket-api-step-functions-tutorial.html): Learn to create a serverless application that uses an API Gateway WebSocket API and Step Functions.


## [API Gateway REST APIs](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-rest-api.html)

### [Develop](https://docs.aws.amazon.com/apigateway/latest/developerguide/rest-api-develop.html)

Learn about developing REST APIs.

### [API Gateway endpoint types](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-api-endpoint-types.html)

Learn about the supported API endpoint types in API Gateway.

- [Change a public or private API endpoint type](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-api-migration.html): Learn how to change the type of API from edge-optimized to Regional, from Regional to edge-optimized, or from public to private or private to regional.

### [Security policies](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-security-policies.html)

Learn how to configure security policies for your REST APIs

- [Supported security policies](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-security-policies-list.html): All supported security policies for API Gateway REST APIs and custom domain names.
- [How to change a security policy](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-security-policies-update.html): How to update your security policy.

### [IP address types for REST APIs in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-ip-address-type.html)

Learn about changing the IP address type

- [Change the IP address type of a REST API](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-ip-address-type-change.html): You can change the IP address type by updating the APIâs configuration.

### [Methods](https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-method-settings.html)

Learn how to set up a REST API Gateway API method as a frontend programming interface for the client to access the integrated backend.

- [Set up method request](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-method-settings-method-request.html): Setting up a method request involves performing the following tasks, after creating a RestApi resource:
- [Set up method response](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-method-settings-method-response.html): An API method response encapsulates the output of an API method request that the client will receive.
- [Set up method using the console](https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-set-up-method-using-console.html): When you create a method using the REST API console, you configure both the integration request and the method request.

### [Access control](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-control-access-to-api.html)

Learn how to control and manage access to a REST API in Amazon API Gateway.

### [Use API Gateway resource policies](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-resource-policies.html)

Learn how to use resource policies to control access to your Amazon API Gateway resources.

- [Access policy language overview for Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-control-access-policy-language-overview.html): Learn the access policy language overview of Amazon API Gateway.
- [How resource policies affect authorization workflow](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-authorization-flow.html): Understand how resource policies work with other authorization mechanisms to control access to your Amazon API Gateway resources.
- [API Gateway resource policy examples](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-resource-policies-examples.html): Learn example API Gateway resource policies.
- [Create and attach an API Gateway resource policy to an API](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-resource-policies-create-attach.html): Learn how to attach a resource policy to your REST API.
- [AWS condition keys that can be used in API Gateway resource policies](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-resource-policies-aws-condition-keys.html): Learn condition keys that can be used in API Gateway resource policies.

### [Use IAM permissions](https://docs.aws.amazon.com/apigateway/latest/developerguide/permissions.html)

Learn how to provide access permissions to users for Amazon API Gateway actions and resources.

- [Control access for invoking an API](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-control-access-using-iam-policies-to-invoke-api.html): In this section, you learn about the permissions model for controlling access to your API using IAM permissions.
- [IAM policy examples for API execution permissions](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-iam-policy-examples-for-api-execution.html): For permissions model and other background information, see .
- [Use VPC endpoint policies for private APIs](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-vpc-endpoint-policies.html): Learn how to create endpoint policies for VPC endpoints in Amazon API Gateway.
- [Using tags to control access to a REST API](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-control-access-tags.html): Learn how to enable and configure attribute-based access control of an API in Amazon API Gateway.

### [Use Lambda authorizers](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-use-lambda-authorizer.html)

Enable an Amazon API Gateway Lambda authorizer to authenticate API requests.

- [Configure a Lambda authorizer](https://docs.aws.amazon.com/apigateway/latest/developerguide/configure-api-gateway-lambda-authorization.html): Learn how to configure an API Gateway Lambda authorizer in the API Gateway console and using the AWS CLI.
- [Input to a Lambda authorizer](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-lambda-authorizer-input.html): Learn the format of input to a Lambda authorizer
- [Output from an API Gateway Lambda authorizer](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-lambda-authorizer-output.html): Learn about the output from an API Gateway Lambda authorizer.
- [Call an API with Lambda authorizers](https://docs.aws.amazon.com/apigateway/latest/developerguide/call-api-with-api-gateway-lambda-authorization.html): Learn how to invoke an API Gateway API Lambda authorizer.
- [Configure a cross-account Lambda authorizer](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-lambda-authorizer-cross-account-lambda-authorizer.html): Learn how to configure a cross-account API Gateway Lambda authorizer.
- [Control access based on an identityâs attributes with Verified Permissions](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-lambda-authorizer-verified-permissions.html): Create a Lambda authorizer using Verified Permissions.

### [Use Amazon Cognito user pool as authorizer for a REST API](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-integrate-with-cognito.html)

Learn how to use an Amazon Cognito user pool to authorize calling an API method.

- [Create an Amazon Cognito user pool for a REST API](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-create-cognito-user-pool.html): Learn how to create an Amazon Cognito user pool for a REST API.
- [Integrate a REST API with an Amazon Cognito user pool](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-enable-cognito-user-pool.html): Learn how to integrate a REST API with an Amazon Cognito user pool.
- [Call a REST API integrated with a user pool](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-invoke-api-integrated-with-cognito-user-pool.html): Learn how to call a REST API integrated with an Amazon Cognito user pool
- [Configure cross-account Amazon Cognito authorizer for a REST API](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-cross-account-cognito-authorizer.html): Learn how to configure a cross-account API Gateway Amazon Cognito authorizer.
- [Create an Amazon Cognito authorizer for a REST API using CloudFormation](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-cognito-authorizer-cfn.html): Learn how to create an Amazon Cognito authorizer for a REST API using CloudFormation

### [Integrations](https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-integration-settings.html)

Learn how to configure an integration request and integration response of a method with a backend.

### [Integration request](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-integration-settings-integration-request.html)

Learn how to set up an integration request in API Gateway.

- [Basic tasks of an API integration request](https://docs.aws.amazon.com/apigateway/latest/developerguide/integration-request-basic-setup.html): An integration request is an HTTP request that API Gateway submits to the backend, passing along the client-submitted request data, and transforming the data, if necessary.
- [Choose an API integration type](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-api-integration-types.html): Learn about the supported API integration types in API Gateway.
- [Set up proxy integrations with a proxy resource](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-set-up-simple-proxy.html): Learn about the proxy resource and the proxy integration in API Gateway.
- [Set up integration request using the console](https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-method-settings-console.html): Learn how to set up an API integration request using the API Gateway console.
- [Integration response](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-integration-settings-integration-response.html): Learn how to set up an integration response in API Gateway

### [Lambda integration](https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-integrations.html)

Learn how to configure Lambda integrations in API Gateway.

### [Lambda proxy integrations](https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html)

Learn how to configure a Lambda proxy integration request and integration response in API Gateway.

- [Set up Lambda proxy integration for API Gateway using the AWS CLI](https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integration-using-cli.html): In this section, we show how to set up an API with the Lambda proxy integration using the AWS CLI.
- [Set up a proxy resource with Lambda proxy integration with an OpenAPI definition](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-set-up-lambda-proxy-integration-on-proxy-resource.html): To set up a proxy resource with the Lambda proxy integration type, create an API resource with a greedy path parameter (for example, /parent/{proxy+}) and integrate this resource with a Lambda function backend (for example, arn:aws:lambda:us-west-2:123456789012:function:SimpleLambda4ProxyResource) on the ANY method.
- [Set up Lambda custom integrations](https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-custom-integrations.html): Learn how to configure a Lambda custom integration request and integration response in API Gateway.
- [Set up asynchronous invocation of the backend Lambda function](https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-integration-async.html): Learn about Lambda asynchronous invocation in Lambda integrations.
- [Handle Lambda errors in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/handle-errors-in-lambda-integration.html): How to handle Lambda errors in API Gateway.
- [HTTP integration](https://docs.aws.amazon.com/apigateway/latest/developerguide/setup-http-integrations.html): Learn how to configure HTTP integrations in API Gateway.

### [Stream the integration response for your proxy integrations](https://docs.aws.amazon.com/apigateway/latest/developerguide/response-transfer-mode.html)

Learn how to set the response transfer mode for your proxy integrations

- [Set up an HTTP proxy integration with payload response streaming](https://docs.aws.amazon.com/apigateway/latest/developerguide/response-streaming-http.html): Learn how to set the response transfer mode for a new HTTP proxy integration

### [Set up a Lambda proxy integration with payload response streaming](https://docs.aws.amazon.com/apigateway/latest/developerguide/response-transfer-mode-lambda.html)

Learn how to set the response transfer mode for a new Lambda proxy integration

- [Configure a Lambda proxy integration with payload response streaming](https://docs.aws.amazon.com/apigateway/latest/developerguide/response-streaming-lambda-configure.html): Learn how to create a Lambda proxy integration with response streaming.
- [Troubleshoot issues with response streaming](https://docs.aws.amazon.com/apigateway/latest/developerguide/response-streaming-troubleshoot.html): Learn how to troubleshoot the response transfer mode for your integrations

### [Private integration](https://docs.aws.amazon.com/apigateway/latest/developerguide/private-integration.html)

Learn how to set up private integrations for a REST API.

- [VPC links V2](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-vpc-links-v2.html): Learn about working with VPC links for private integrations.
- [Set up a private integration](https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-private-integration.html): Learn how to set up private integrations for a REST API.

### [Private integration using VPC links V1 (legacy)](https://docs.aws.amazon.com/apigateway/latest/developerguide/vpc-links-v1.html)

- [Set up a Network Load Balancer for private integrations (legacy)](https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-nlb-for-vpclink-using-console.html): Learn how to set up a Network Load Balancer for private integrations.
- [Grant permissions for API Gateway to create a VPC link (legacy)](https://docs.aws.amazon.com/apigateway/latest/developerguide/grant-permissions-to-create-vpclink.html): Learn how to grant permissions to create a VPC link.
- [Set up an API with private integrations using AWS CLI (legacy)](https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-api-with-vpclink-cli.html): Learn how to set up an API Gateway API with private integrations.
- [API Gateway accounts used for private integrations (legacy)](https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-api-with-vpclink-accounts.html): Learn how to set up an API Gateway API with private integrations.

### [Mock integration](https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-mock-integration.html)

Learn how to configure mock integration for a method in API Gateway.

- [Enable mock integration using the API Gateway console](https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-mock-integration-console.html): You must have a method available in API Gateway.

### [Request validation](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-method-request-validation.html)

Describes how to turn on request validation on methods for API Gateway.

- [Data models for REST APIs](https://docs.aws.amazon.com/apigateway/latest/developerguide/models-mappings-models.html): Learn about what a data model is for API Gateway.
- [Set up basic request validation in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-request-validation-set-up.html): Learn how to set up basic request validation in API Gateway.
- [AWS CloudFormation template of a sample API with basic request validation](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-request-validation-sample-cloudformation.html): CloudFormation example of request validation

### [Data transformations](https://docs.aws.amazon.com/apigateway/latest/developerguide/rest-api-data-transformations.html)

Learn how to set up request data mappings in integration request and how to set response data mappings in integration response.

### [Parameter mapping](https://docs.aws.amazon.com/apigateway/latest/developerguide/rest-api-parameter-mapping.html)

How to map parameters in API Gateway.

- [Parameter mapping examples](https://docs.aws.amazon.com/apigateway/latest/developerguide/request-response-data-mappings.html): Set up data mappings from an API method request to the method response parameters in Amazon API Gateway.
- [Parameter mapping source reference](https://docs.aws.amazon.com/apigateway/latest/developerguide/rest-api-parameter-mapping-sources.html): Reference for parameter mapping

### [Mapping template transformations](https://docs.aws.amazon.com/apigateway/latest/developerguide/models-mappings.html)

In Amazon API Gateway, pass an API request response payload between your API methods and the backend HTTP, AWS Lambda or AWS integrations.

- [Method request behavior for payloads without mapping templates](https://docs.aws.amazon.com/apigateway/latest/developerguide/integration-passthrough-behaviors.html): How you can configure method request behavior for payloads without mapping templates in API Gateway
- [Additional mapping template example](https://docs.aws.amazon.com/apigateway/latest/developerguide/example-photos.html): Additional example for data mapping template transformations.
- [Override your API's request and response parameters and status codes](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-override-request-response-parameters.html): Learn about mapping template overrides for your API's request and response parameters and status codes.
- [Tutorial: Modify the integration request and response for integrations to AWS services](https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-data-transformations-in-api-gateway.html): Learn how to set up a data transformation in API Gateway.
- [Examples using variables for mapping template transformations](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-mapping-variable-examples.html): Example using context, input, and util variables.
- [Variables for data transformations](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-mapping-template-reference.html): Reference for variables and functions used in data transformations

### [Gateway responses](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-gatewayResponse-definition.html)

Learn how to set up gateway responses to customize error responses.

- [Set up a gateway response for a REST API using the API Gateway console](https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-gateway-response-using-the-console.html): Learn how to set up a gateway response for a REST API.
- [Set up a gateway response using the API Gateway REST API](https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-gateway-response-using-the-api.html): Learn how to set up a gateway response for a REST API.
- [Set up gateway response customization in OpenAPI](https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-gateway-responses-in-swagger.html): You can use the x-amazon-apigateway-gateway-responses extension at the API root level to customize gateway responses in OpenAPI.
- [Gateway response types for API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/supported-gateway-response-types.html): Learn about the gateway response types.

### [CORS](https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-cors.html)

Learn what cross-origin resource sharing (CORS) is, whether you want to enable it, and how to enable CORS methods in API Gateway.

- [Enable CORS using the console](https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-cors-console.html): Learn how to enable CORS on a resource using the API Gateway console.
- [Enable CORS using OpenAPI definition](https://docs.aws.amazon.com/apigateway/latest/developerguide/enable-cors-for-resource-using-swagger-importer-tool.html): Learn how to enable CORS on a resource using an OpenAPI definition.
- [Test CORS for an API Gateway API](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-test-cors.html): Learn how to test CORS.

### [Binary media types](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-payload-encodings.html)

Set up content encoding conversion in API Gateway to support binary media types.

- [Content type conversions in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-payload-encodings-workflow.html): Convert content types in API Gateway.
- [Enabling binary support using the API Gateway console](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-payload-encodings-configure-with-console.html): Enable binary support in the API Gateway console.
- [Enabling binary support using the API Gateway REST API](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-payload-encodings-configure-with-control-service-api.html): Enable binary support using the API Gateway REST API.
- [Import and export content encodings for API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-payload-encodings-import-and-export.html): Import and export content encodings using an API Gateway extension to the API's OpenAPI definition file.
- [Return binary media from a Lambda proxy integration in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/lambda-proxy-binary-media.html): Example code to return binary media and text data from an AWS Lambda proxy integration.
- [Access binary files in Amazon S3 through an API Gateway API](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-content-encodings-examples-image-s3.html): Examples showing how to access binary files in Amazon S3 using an API Gateway API.
- [Access binary files in Lambda using an API Gateway API](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-content-encodings-examples-image-lambda.html): Example showing how to access binary files in Lambda using an API Gateway API.

### [Invoke](https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-call-api.html)

Learn how to call a deployed REST API in Amazon API Gateway.

- [Use the console to test a REST API method](https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-test-method.html): Learn how to test a method in API Gateway.
- [Use a Java SDK generated by API Gateway for a REST API](https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-call-apigateway-generated-java-sdk.html): In this section, we outline the steps to use a Java SDK generated by API Gateway for a REST API, by using the Simple Calculator API as an example.
- [Use an Android SDK generated by API Gateway for a REST API](https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-generate-sdk-android.html): How to use an Android SDK that you generated by using API Gateway.
- [Use a JavaScript SDK generated by API Gateway for a REST API](https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-generate-sdk-javascript.html): How to use a JavaScript SDK that you generated by API Gateway.
- [Use a Ruby SDK generated by API Gateway for a REST API](https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-call-sdk-ruby.html): How to use a Ruby SDK generated by API Gateway.
- [Use iOS SDK generated by API Gateway for a REST API in Objective-C or Swift](https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-generate-sdk-ios.html): How to use an iOS SDK that you generated by using API Gateway.

### [OpenAPI](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-import-api.html)

Learn how to import an API into API Gateway with an OpenAPI definition file.

- [Import an edge-optimized API](https://docs.aws.amazon.com/apigateway/latest/developerguide/import-edge-optimized-api.html): Learn how to import an edge-optimized API into API Gateway
- [Import a Regional API](https://docs.aws.amazon.com/apigateway/latest/developerguide/import-export-api-endpoints.html): Learn how to import the OpenAPI defintion of a Regional API.
- [Import an OpenAPI file to update an existing API definition](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-import-api-update.html): You can import API definitions only to update an existing API, without changing its endpoint configuration, as well as stages and stage variables, or references to API keys.
- [Set the OpenAPI basePath property](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-import-api-basePath.html): In OpenAPI 2.0, you can use the basePath property to provide one or more path parts that precede each path defined in the paths property.
- [AWS variables](https://docs.aws.amazon.com/apigateway/latest/developerguide/import-api-aws-variables.html): You can use the following AWS variables in OpenAPI definitions.
- [Errors and warnings from importing your API into API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-import-api-errors-warnings.html): When you import your external definition file into API Gateway, API Gateway might generate warnings and errors.
- [Export a REST API](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-export-api.html): Export an existing REST API from API Gateway to OpenAPI and other API definition files.

### [Publish](https://docs.aws.amazon.com/apigateway/latest/developerguide/rest-api-publish.html)

Learn about publishing REST APIs.

### [Deploy REST APIs](https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-deploy-api.html)

Learn how to deploy a REST API in Amazon API Gateway.

- [Create a deployment](https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-deployments.html): Learn how to set up and manage API deployments in Amazon API Gateway.

### [Set up a stage](https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-stages.html)

Learn how to set up and manage stages in Amazon API Gateway.

- [Add a stage to an Amazon Bedrock AgentCore Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/mcp-server.html): Use an AgentCore Gateway to expose your REST API into a Model Context Protocol (MCP)-compatible tool.
- [Delete a stage](https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-delete-stage.html): Learn how to delete a stage in API Gateway.
- [Set up tags](https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-tags.html): Learn how to set up and manage tags in Amazon API Gateway.

### [Use stage variables](https://docs.aws.amazon.com/apigateway/latest/developerguide/stage-variables.html)

Learn how to work with stage variables in Amazon API Gateway.

- [Set up stage variables for REST APIs in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-set-stage-variables-aws-console.html): Learn how to work with stage variables in Amazon API Gateway.
- [Stage variables reference](https://docs.aws.amazon.com/apigateway/latest/developerguide/aws-api-gateway-stage-variables-reference.html): Learn about the stage variable reference for REST APIs.

### [Set up a canary release deployment](https://docs.aws.amazon.com/apigateway/latest/developerguide/canary-release.html)

Learn how to set up a canary release deployment to test API updates in Amazon API Gateway.

- [Create a canary release deployment](https://docs.aws.amazon.com/apigateway/latest/developerguide/create-canary-deployment.html): You create a canary release deployment when deploying the API with canary settings as an additional input to the deployment creation operation.
- [Update a canary release](https://docs.aws.amazon.com/apigateway/latest/developerguide/update-canary-deployment.html): After a canary release is deployed, you may want to adjust the percentage of the canary traffic or enable or disable the use of a stage cache to optimize the test performance.
- [Promote a canary release](https://docs.aws.amazon.com/apigateway/latest/developerguide/promote-canary-deployment.html): When you promote a canary release, the canary release replaces the current stage settings.
- [Turn off a canary release](https://docs.aws.amazon.com/apigateway/latest/developerguide/delete-canary-deployment.html): To turn off a canary release deployment is to set the canarySettings to null to remove it from the stage.
- [Redeploy a REST API](https://docs.aws.amazon.com/apigateway/latest/developerguide/updating-api.html): Update a REST API in Amazon API Gateway.

### [Custom domain names](https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-custom-domains.html)

Learn how to set up a custom domain name for a REST API in API Gateway.

- [Get certificates ready in AWS Certificate Manager](https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-specify-certificate-for-custom-domain-name.html): Before setting up a custom domain name for an API, you must have an SSL/TLS certificate ready in AWS Certificate Manager.
- [Set up a Regional custom domain name](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-regional-api-custom-domain-create.html): Learn how to create and maintain a custom domain name for an API Gateway Regional API endpoint.
- [Set up an edge-optimized custom domain name in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-edge-optimized-custom-domain-name.html): Learn how to create an edge-optimized custom domain name.
- [Migrate custom domain names](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-regional-api-custom-domain-migrate.html): Learn how to migrate a custom domain name between a Regional API endpoint and an edge-optimized API endpoint.

### [Send traffic to your APIs through your custom domain name in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/rest-api-routing-mode.html)

Learn about the different ways you can send traffic to your APIs through your custom domain name in API Gateway.

- [Set the routing mode for your custom domain name](https://docs.aws.amazon.com/apigateway/latest/developerguide/set-routing-mode.html): How to set the routing mode for custom domain names.

### [Routing rules](https://docs.aws.amazon.com/apigateway/latest/developerguide/rest-api-routing-rules.html)

Learn about REST API routing rules.

- [Examples of how API Gateway evaluates routing rules](https://docs.aws.amazon.com/apigateway/latest/developerguide/rest-api-routing-rules-examples.html): Examples of how API Gateway evaluates routing rules
- [How to use routing rules](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-routing-rules-use.html): How to create and update the priority of a routing rule.
- [Recreate an API mapping using routing rules](https://docs.aws.amazon.com/apigateway/latest/developerguide/rest-api-routing-rules-recreate-api-mapping.html): Recreate an API mapping using routing rules
- [Troubleshooting issues with routing rules](https://docs.aws.amazon.com/apigateway/latest/developerguide/rest-api-routing-rules-troubleshoot.html): How to troubleshoot your routing rules
- [API mappings](https://docs.aws.amazon.com/apigateway/latest/developerguide/rest-api-mappings.html): Learn about REST API mappings for custom domain names.
- [IP address types for custom domain names in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/rest-custom-domain-ip-address-type.html): Learn about changing the IP address type for custom domain names
- [Choose a security policy](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-custom-domain-tls-version.html): Learn how to choose a security policy for your custom domain.
- [Disable the default endpoint](https://docs.aws.amazon.com/apigateway/latest/developerguide/rest-api-disable-default-endpoint.html): Learn how to disable the default endpoint for a REST API in API Gateway.
- [DNS failover](https://docs.aws.amazon.com/apigateway/latest/developerguide/dns-failover.html): Learn to configure DNS failover for a multi-Region API Gateway architecture.

### [Optimize](https://docs.aws.amazon.com/apigateway/latest/developerguide/rest-api-optimize.html)

Learn about optimizing REST APIs.

- [Cache settings](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-caching.html): Learn how to enable Amazon API Gateway caching to enhance your API's performance.

### [Content encoding](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-gzip-compression-decompression.html)

In API Gateway, learn how to enable GZIP compression of a response payload and decompression of a request payload.

- [Enable payload compression for an API in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-enable-compression.html): Learn how to enable and disable compression for an API by using the API Gateway console, the AWS CLI, and the API Gateway REST API.
- [Call a method with a compressed payload](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-make-request-with-compressed-payload.html): Learn how to make an API request with a compressed payload.
- [Receive a response with a compressed payload](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-receive-response-with-compressed-payload.html): Learn how to receive an API response with a compressed payload.

### [Distribute](https://docs.aws.amazon.com/apigateway/latest/developerguide/rest-api-distribute.html)

Learn about distributing REST APIs.

### [Usage plans](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-api-usage-plans.html)

Learn how to create, configure, and optimize API usage plans in Amazon API Gateway.

- [Choose an API key source in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-api-key-source.html): Learn about choosing a key source for your API key
- [API Gateway API key file format](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-key-file-format.html): See the API key file format for an API Gateway usage plan.
- [Set up API keys for REST APIs in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-setup-api-keys.html): Learn how to set up API keys.
- [Set up usage plans for REST APIs in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-create-usage-plans.html): Create, configure, and test usage plans.
- [Maintain a usage plan for REST APIs in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-usage-plan-manage-usage.html): Maintaining a usage plan involves monitoring the used and remaining quotas over a given time period and, if needed, extending the remaining quotas by a specified amount.
- [Create and configure API keys and usage plans with CloudFormation](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-key-usage-plan-cfn.html): Learn how to create, configure, and test API keys and usage plans with CloudFormation.
- [Configure a method to use API keys with an OpenAPI definition](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-key-usage-plan-oas.html): You can use an OpenAPI definition to require API keys on a method.
- [Test usage plans for REST APIs in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-usage-plan-test-with-postman.html): Learn how to test a usage plan with the API Gateway CLI and REST API.
- [Call a method using an API key](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-api-key-call.html): Depending on the API key source type you choose, use one of the following procedures to use header-sourced API keys or authorizer-returned API keys in method invocation:

### [API documentation](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-documenting-api.html)

Learn how to provide documentation support for an API Gateway REST API.

- [Representation of API documentation in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-documenting-api-content-representation.html): Describes representation of API documentation in API Gateway.
- [Document an API using the API Gateway console](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-documenting-api-quick-start-with-console.html): Use the API Gateway console to document an API.
- [Publish API documentation using the API Gateway console](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-documenting-api-with-console.html): Use the API Gateway console to publish API documentation.
- [Document an API using the API Gateway REST API](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-documenting-api-quick-start-with-restapi.html): Use the API Gateway REST API to document an API.
- [Publish API documentation using the API Gateway REST API](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-documenting-api-quick-start-publishing.html): Get a documentation snapshot and associate it with an API stage in API Gateway.
- [Import API documentation](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-documenting-api-quick-start-import-export.html): Import documentation parts from OpenAPI to an API using API Gateway.
- [Control access to API documentation in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-documenting-api-content-provision-and-consumption.html): Control access to your API documentation.

### [SDK generation](https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-generate-sdk.html)

Learn how to generate a language-specific and platform-specific SDK for an API you created in API Gateway.

- [Simple calculator Lambda function](https://docs.aws.amazon.com/apigateway/latest/developerguide/simple-calc-nodejs-lambda-function.html): Demonstrates a simple calculator Lambda function.
- [Simple calculator API in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/simple-calc-lambda-api.html): Demonstrates a simple calculator API in API Gateway.
- [Simple calculator API OpenAPI definition](https://docs.aws.amazon.com/apigateway/latest/developerguide/simple-calc-lambda-api-swagger-definition.html): Demonstrates a simple calculator API OpenAPI definition.
- [Generate the Java SDK of an API in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/generate-java-sdk-of-an-api.html): The following procedure shows how to generate the Java SDK of an API in API Gateway.
- [Generate the Android SDK of an API in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/generate-android-sdk-of-an-api.html): Learn how to generate the Android SDK of an API.
- [Generate the iOS SDK of an API in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/generate-ios-sdk-of-an-api.html): Learn how to generate the iOS SDK of an API.
- [Generate the JavaScript SDK of a REST API in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/generate-javascript-sdk-of-an-api.html): Learn how to generate the JavaScript SDK of an API.
- [Generate the Ruby SDK of an API in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/generate-ruby-sdk-of-an-api.html): Learn how to generate the Ruby SDK of an API.
- [Generate SDKs for an API using AWS CLI commands in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-generate-sdk-cli.html): Learn how to generate the SDKs for an API using AWS CLI commands.
- [Sell your APIs as SaaS](https://docs.aws.amazon.com/apigateway/latest/developerguide/sell-api-as-saas-on-aws-marketplace.html): Learn how to sell your APIs as a Software as a Service (SaaS) product through AWS Marketplace.

### [Protect](https://docs.aws.amazon.com/apigateway/latest/developerguide/rest-api-protect.html)

Learn about protecting REST APIs.

- [Mutual TLS](https://docs.aws.amazon.com/apigateway/latest/developerguide/rest-api-mutual-tls.html): Learn about configuring mutual TLS authentication for a REST API.

### [Client certificates](https://docs.aws.amazon.com/apigateway/latest/developerguide/getting-started-client-side-ssl-authentication.html)

Learn how to enable backend SSL authentication of an API using the API Gateway console.

- [Supported certificate authorities for HTTP and HTTP proxy integration](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-supported-certificate-authorities-for-http-endpoints.html): Learn how to enable client-side SSL Authentication of an API using API Gateway console.
- [AWS WAF](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-control-access-aws-waf.html): Learn how to configure AWS WAF to protect your Amazon API Gateway APIs.
- [Throttling](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-request-throttling.html): Understand and change API request throttling limits on an account level, stage level, and method level.

### [Private REST APIs](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-private-apis.html)

Provides an overview of API Gateway private APIs.

- [Create a private API](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-private-api-create.html): Learn how to create a private REST API

### [Custom domain names for private APIs](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-private-custom-domains.html)

Provides an overview of API Gateway custom domain names for private APIs.

- [API providers and API consumers](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-private-custom-domains-associations.html): Provides an overview of API Gateway private custom domains providers and consumers.
- [Tutorial: Create and invoke a custom domain name for private APIs](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-private-custom-domains-tutorial.html): Shows how to create a private custom domain name in your own account

### [Working with cross-account private custom domain names](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-private-custom-domains-other-accounts.html)

Work with a private custom domain name in another AWS account.

- [API provider: Share your private custom domain name using AWS RAM](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-private-custom-domains-provider-share.html): Shows how provide access to API consumers in other accounts using AWS RAM.
- [API provider: Stop sharing a private custom domain name using AWS RAM](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-private-custom-domains-provider-stop-sharing.html): Shows how deny access to API consumers in other accounts using AWS RAM.
- [API provider: Share your private custom domain name using the API Gateway AWS CLI](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-private-custom-domains-provider-share-cli.html): Shows how provide access to API consumers in other accounts using the API Gateway AWS CLI.
- [API consumer: Associate your VPC endpoint with a private custom domain name shared with you](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-private-custom-domains-consumer-create.html): Create an association with a private custom domain name in another AWS account.
- [API consumer: Delete your domain name access association with a private custom domain name](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-private-custom-domains-consumer-delete-domain-name-access-association.html): Delete an association with a private custom domain name in another AWS account.
- [Create a custom domain name for private APIs using CloudFormation](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-private-custom-domains-cfn.html): CloudFormation example of a private custom domain name
- [Invoke a private API](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-private-api-test-invoke-url.html): Learn how to specify the base invoke URL of a private API.

### [Monitor](https://docs.aws.amazon.com/apigateway/latest/developerguide/rest-api-monitor.html)

Learn about monitoring REST APIs.

### [CloudWatch metrics](https://docs.aws.amazon.com/apigateway/latest/developerguide/monitoring-cloudwatch.html)

Learn how to monitor your REST API API with CloudWatch metrics.

- [Amazon API Gateway dimensions and metrics](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-metrics-and-dimensions.html): The metrics and dimensions that API Gateway sends to Amazon CloudWatch are listed below.
- [View metrics with the API dashboard](https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-api-dashboard.html): Learn how to view CloudWatch metrics of a deployed API using the API Dashboard in the API Gateway Console.
- [View metrics in the CloudWatch console](https://docs.aws.amazon.com/apigateway/latest/developerguide/metrics_dimensions_view_in_cloud_watch.html): Metrics are grouped first by the service namespace, and then by the various dimension combinations within each namespace.
- [View log event in the CloudWatch console](https://docs.aws.amazon.com/apigateway/latest/developerguide/view-cloudwatch-log-events-in-cloudwatch-console.html): The following section explains the necessary prerequisites and how to view API Gateway log events in the CloudWatch console.
- [Monitoring tools in AWS for API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/monitoring_automated_manual.html): Configure AWS tools to monitor API Gateway.
- [CloudWatch logs](https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-logging.html): Learn how to set up CloudWatch logging in Amazon API Gateway.
- [Firehose](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-logging-to-kinesis.html): Learn how to use Amazon Data Firehose as a destination for access logging.
- [Variables for access logging for API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-variables-for-access-logging.html): Reference for variables access logging, etc.

### [X-Ray](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-xray.html)

Learn how to use AWS X-Ray to trace API invocation.

- [Set up AWS X-Ray](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-enabling-xray.html): Learn how to enable AWS X-Ray in Amazon API Gateway.
- [Use AWS X-Ray service maps and trace views](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-using-xray-maps.html): Learn how to use AWS X-Ray service maps and trace views in Amazon API Gateway.
- [Configure AWS X-Ray sampling rules](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-configuring-xray-sampling-rules.html): Learn how to configure AWS X-Ray sampling rules.
- [X-Ray traces](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-understanding-xray-traces.html): Learn how to understand AWS X-Ray traces.


## [API Gateway portals](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-portals.html)

### [Portal product](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-portals-portal-product.html)

Learn about what a portal product is.

- [Create a portal product](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-portals-create-portal-product.html): Learn how to create a portal product
- [Create a product REST endpoint](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-portals-create-product-rest-endpoint.html): Learn how to create a portal product
- [Create a product page](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-portals-create-product-page.html): Learn how to create a portal product
- [Update a portal product](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-portals-update-portal-product.html): Learn how to update a portal product
- [Update a product REST endpoint](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-portals-update-product-endpoint.html): Learn how to update a product endpoint
- [Update product page](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-portals-update-product-page.html): Learn how to update a product page

### [Share portal products](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-portals-share-resources.html)

Learn how to share a product

- [Share your portal product with a portal owner](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-portals-share-products.html): Learn how to share a product
- [Add a shared portal product to your portal](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-portals-use-shared-products.html): Learn how to share a product
- [Enable try it for a product REST endpoint in your portal](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-portals-try-it.html): Learn how to try a product in your portal
- [Delete a portal product](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-portals-delete-product.html): Learn how to delete a portal product
- [Create a portal](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-portals-create-portal.html): Learn how to create a portal
- [Update a portal](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-portals-update-portal.html): Learn how to update your portal
- [Preview a portal](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-portals-prview-portal.html): Learn how to preview your portal
- [Publish a portal](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-portals-publish-portal.html): Learn how to create a product
- [Use a portal](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-portals-use-portal.html): Learn how to use an API portal
- [Disable a portal](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-portals-disable-portal.html): Learn how to disable an API portal
- [Delete a portal](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-portals-delete-portal.html): Learn how to delete an API portal


## [API Gateway HTTP APIs](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api.html)

### [Develop](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop.html)

Learn about developing HTTP APIs.

- [Routes](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop-routes.html): Learn about developing HTTP API routes.
- [IP address types for HTTP APIs in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-ip-address-type.html): Learn about changing the IP address type

### [Access control](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-access-control.html)

Learn how to control access to an HTTP API.

- [Lambda authorizers](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-lambda-authorizer.html): Learn about AWS Lambda authorizers for Amazon API Gateway HTTP APIs.
- [JWT authorizers](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-jwt-authorizer.html): Learn about JWT authorization for HTTP APIs.
- [IAM authorization](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-access-control-iam.html): Learn about IAM authorization for Amazon API Gateway HTTP APIs.

### [Integrations](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop-integrations.html)

Learn about developing HTTP API integrations.

- [AWS Lambda integrations](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop-integrations-lambda.html): Learn about developing HTTP API AWS Lambda integrations.
- [HTTP integrations](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop-integrations-http.html): Learn about developing HTTP API HTTP proxy integrations.

### [AWS service integrations](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop-integrations-aws-services.html)

Learn about developing HTTP API AWS service integrations.

- [AWS service integrations reference](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop-integrations-aws-services-reference.html): Learn about the required and optional parameters for HTTP API AWS service integrations.
- [Private integrations](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop-integrations-private.html): Learn about developing HTTP API private integrations.
- [CORS](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-cors.html): Learn how to configure CORS for an HTTP API.
- [Parameter mapping](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-parameter-mapping.html): Learn how to set up parameter mapping to modify API requests and responses for Amazon API Gateway HTTP APIs.

### [OpenAPI](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-open-api.html)

Learn about importing OpenAPI definitions for HTTP APIs.

- [Export](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-export.html): Learn about exporting an OpenAPI 3.0 definition of an API Gateway HTTP API.

### [Publish](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-publish.html)

Learn about publishing HTTP APIs.

### [Stages](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-stages.html)

Learn about HTTP API stages.

- [Use stage variables for HTTP APIs in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-stages.stage-variables.html): Learn about HTTP API stages in API Gateway.
- [API Gateway stage variables reference for HTTP APIs in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-stages.stage-variables-reference.html): Learn about the HTTP API stages variable reference.
- [Security policy for HTTP APIs in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-ciphers.html): Learn about the security policy for your HTTP APIs.

### [Custom domain names](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-custom-domain-names.html)

Learn how to set up a custom domain name for an HTTP API in API Gateway.

- [API mappings](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-mappings.html): Learn about HTTP API API mappings for custom domain names.
- [Disable the default endpoint](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-disable-default-endpoint.html): Learn how to disable the default endpoint for an HTTP API in API Gateway.
- [IP address types for custom domain names for HTTP APIs](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-custom-domain-names-ip-address-type.html): Learn about changing the IP address type

### [Protect](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-protect.html)

Learn about protecting HTTP APIs by throttling requests and enabling mutual TLS authentication.

- [Throttling](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-throttling.html): Learn about protecting HTTP APIs by throttling requests.
- [Mutual TLS](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-mutual-tls.html): Learn about configuring mutual TLS authentication for an HTTP API.

### [Monitor](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-monitor.html)

Learn about monitoring HTTP APIs.

- [Metrics](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-metrics.html): Learn about metrics for HTTP APIs.

### [Logging](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-logging.html)

Learn how to configure logging for an HTTP API.

- [Logging variables](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-logging-variables.html): Learn about the access logging variables for HTTP APIs.

### [Troubleshooting](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-troubleshooting.html)

Learn about troubleshooting for HTTP APIs.

- [Lambda integrations](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-troubleshooting-lambda.html): Learn about troubleshooting Lambda integrations for HTTP APIs.
- [JWT authorizers](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-troubleshooting-jwt.html): Learn about troubleshooting JWT authorizers for HTTP APIs.


## [API Gateway WebSocket APIs](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api.html)

### [Overview of WebSocket APIs](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-overview.html)

Learn about WebSocket APIs

- [Manage connected users and client apps](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-route-keys-connect-disconnect.html): Learn about how to manage connected users and client apps for WebSocket APIs.
- [Invoke your backend integration](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-routes-integrations.html): Learn about invoking your backend integration.
- [WebSocket selection expressions](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-selection-expressions.html): Learn about WebSocket selection expressions

### [Develop](https://docs.aws.amazon.com/apigateway/latest/developerguide/websocket-api-develop.html)

Learn about developing WebSocket APIs.

- [Create and configure](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-create-empty-api.html): Learn how to create a WebSocket API.
- [IP address types for WebSocket APIs in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/websocket-api-ip-address-type.html): Learn about changing the IP address type

### [Routes](https://docs.aws.amazon.com/apigateway/latest/developerguide/websocket-api-develop-routes.html)

Learn about developing WebSocket API routes.

- [Set up WebSocket API route responses](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-route-response.html): Learn how to set up a route response for a WebSocket API.
- [Subprotocol support](https://docs.aws.amazon.com/apigateway/latest/developerguide/websocket-connect-route-subprotocol.html): Learn how to configure a WebSocket API $connect route that requires that clients use a supported subprotocol.

### [Access control](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-control-access.html)

Learn how to control access to a WebSocket API.

- [Control access to WebSocket APIs with IAM authorization](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-control-access-iam.html): Learn how to use IAM authorization for a WebSocket API
- [Control access to WebSocket APIs with AWS Lambda REQUEST authorizers](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-lambda-auth.html): Learn how to create a Lambda authorizer function.

### [Integrations](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-integrations.html)

Learn how to add integrations to a WebSocket API.

- [Integration request](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-integration-requests.html): Setting up an integration request involves the following:
- [Integration responses](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-integration-responses.html): The following section provides a brief overview of integration responses for WebSocket API and how to set up an integration response for a WebSocket API.
- [Request validation](https://docs.aws.amazon.com/apigateway/latest/developerguide/websocket-api-request-validation.html): Learn how to validate requests for WebSocket APIs.

### [Data transformations](https://docs.aws.amazon.com/apigateway/latest/developerguide/websocket-api-data-transformations.html)

Learn how to set up request and response data transformations for WebSocket APIs.

- [Data mapping](https://docs.aws.amazon.com/apigateway/latest/developerguide/websocket-api-data-mapping.html): Learn how to set up data mapping for WebSocket APIs.
- [WebSocket mapping template reference](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-mapping-template-reference.html): Learn about the mapping template reference for API Gateway for WebSocket APIs.
- [Binary media types](https://docs.aws.amazon.com/apigateway/latest/developerguide/websocket-api-develop-binary-media-types.html): Learn about working with binary media types for WebSocket APIs.

### [Invoke](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-how-to-call-websocket-api.html)

Learn how to invoke a WebSocket API.

- [Use wscat to connect to a WebSocket API and send messages to it](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-how-to-call-websocket-api-wscat.html): Learn how to use wscat to connect to a WebSocket API.
- [Use @connections commands in your backend service](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-how-to-call-websocket-api-connections.html): Learn how to use @connections commands in your backend service for a WebSocket API.

### [Publish](https://docs.aws.amazon.com/apigateway/latest/developerguide/websocket-api-publish.html)

Learn about publishing WebSocket APIs.

- [Stages](https://docs.aws.amazon.com/apigateway/latest/developerguide/websocket-api-stages.html): Learn about WebSocket API stages.
- [Deploy a WebSocket API](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-set-up-websocket-deployment.html): Learn how to set up and manage WebSocket API deployments in Amazon API Gateway.
- [Security policy for WebSocket APIs in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/websocket-api-ciphers.html): Learn about the security policy for WebSocket APIs.

### [Custom domain names](https://docs.aws.amazon.com/apigateway/latest/developerguide/websocket-api-custom-domain-names.html)

Learn how to set up a custom domain name for a WebSocket API in API Gateway.

- [API mappings](https://docs.aws.amazon.com/apigateway/latest/developerguide/websocket-api-mappings.html): Learn about WebSocket API mappings for custom domain names.
- [IP address types for custom domain names for WebSocket APIs](https://docs.aws.amazon.com/apigateway/latest/developerguide/websocket-api-custom-domain-names-ip-address-type.html): Learn about changing the IP address type
- [Disable the default endpoint](https://docs.aws.amazon.com/apigateway/latest/developerguide/websocket-api-disable-default-endpoint.html): Learn how to disable the default endpoint for an WebSocket API in API Gateway.
- [Protect](https://docs.aws.amazon.com/apigateway/latest/developerguide/websocket-api-protect.html): Learn about protecting WebSocket APIs by throttling requests.

### [Monitor](https://docs.aws.amazon.com/apigateway/latest/developerguide/websocket-api-monitor.html)

Learn about monitoring WebSocket APIs.

- [Metrics](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-logging.html): Learn about monitoring WebSocket API with CloudWatch metrics
- [Logging](https://docs.aws.amazon.com/apigateway/latest/developerguide/websocket-api-logging.html): Learn how to configure logging for a WebSocket API.


## [OpenAPI extensions](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-swagger-extensions.html)

- [x-amazon-apigateway-any-method](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-swagger-extensions-any-method.html): Specifies the OpenAPI Operation Object for the API Gateway catch-all ANY method in an OpenAPI Path Item Object.
- [x-amazon-apigateway-cors](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-swagger-extensions-cors-configuration.html): Specifies the cross-origin resource sharing (CORS) configuration for an HTTP API.
- [x-amazon-apigateway-api-key-source](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-swagger-extensions-api-key-source.html): Specify the source to receive an API key to throttle API methods that require a key.
- [x-amazon-apigateway-auth](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-swagger-extensions-auth.html): Defines an authorization type to be applied for authorization of method invocations in API Gateway.
- [x-amazon-apigateway-authorizer](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-swagger-extensions-authorizer.html): Defines a Lambda authorizer, Amazon Cognito user pool, or JWT authorizer to be applied for authorization of method invocations in API Gateway.
- [x-amazon-apigateway-authtype](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-swagger-extensions-authtype.html): For REST APIs, this extension can be used to define a custom type of a Lambda authorizer.
- [x-amazon-apigateway-binary-media-type](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-swagger-extensions-binary-media-types.html): Specifies the list of binary media types to be supported by API Gateway, such as application/octet-stream and image/jpeg.
- [x-amazon-apigateway-documentation](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-swagger-extensions-documentation.html): Defines the documentation parts to be imported into API Gateway.
- [x-amazon-apigateway-endpoint-access-mode](https://docs.aws.amazon.com/apigateway/latest/developerguide/openapi-extensions-endpoint-access-mode.html): Specifies a the endpoint access mode for a REST API or custom domain name.
- [x-amazon-apigateway-endpoint-configuration](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-swagger-extensions-endpoint-configuration.html): Specifies details of the endpoint configuration for an API.
- [x-amazon-apigateway-gateway-responses](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-swagger-extensions-gateway-responses.html): Defines the gateway responses for an API as a string-to-GatewayResponse map of key-value pairs.
- [x-amazon-apigateway-gateway-responses.gatewayResponse](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-swagger-extensions-gateway-responses.gatewayResponse.html): Defines a gateway response of a given response type, including the status code, any applicable response parameters, or response templates.
- [x-amazon-apigateway-gateway-responses.responseParameters](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-swagger-extensions-gateway-responses.responseParameters.html): Defines a string-to-string map of key-value pairs to generate gateway response parameters from the incoming request parameters or using literal strings.
- [x-amazon-apigateway-gateway-responses.responseTemplates](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-swagger-extensions-gateway-responses.responseTemplates.html): Defines GatewayResponse mapping templates, as a string-to-string map of key-value pairs, for a given gateway response.
- [x-amazon-apigateway-importexport-version](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-extensions-importexport-version.html): Specifies the version of the API Gateway import and export algorithm for HTTP APIs.
- [x-amazon-apigateway-integration](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-swagger-extensions-integration.html): Specifies details of the backend integration used for this method.
- [x-amazon-apigateway-integrations](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-extensions-integrations.html): Defines a collection of integrations.
- [x-amazon-apigateway-integration.requestTemplates](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-swagger-extensions-integration-requestTemplates.html): Specifies mapping templates for a request payload of the specified MIME types.
- [x-amazon-apigateway-integration.requestParameters](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-swagger-extensions-integration-requestParameters.html): For REST APIs, specifies mappings from named method request parameters to integration request parameters.
- [x-amazon-apigateway-integration.responses](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-swagger-extensions-integration-responses.html): Defines the method's responses and specifies parameter mappings or payload mappings from integration responses to method responses.
- [x-amazon-apigateway-integration.response](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-swagger-extensions-integration-response.html): Defines a response and specifies parameter mappings or payload mappings from the integration response to the method response.
- [x-amazon-apigateway-integration.responseTemplates](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-swagger-extensions-integration-responseTemplates.html): Specifies mapping templates for a response payload of the specified MIME types.
- [x-amazon-apigateway-integration.responseParameters](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-swagger-extensions-integration-responseParameters.html): Specifies mappings from integration method response parameters to method response parameters.
- [x-amazon-apigateway-integration.tlsConfig](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-extensions-integration-tls-config.html): Specifies the TLS configuration for an integration.
- [x-amazon-apigateway-minimum-compression-size](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-openapi-minimum-compression-size.html): Specifies the minimum compression size for a REST API.
- [x-amazon-apigateway-policy](https://docs.aws.amazon.com/apigateway/latest/developerguide/openapi-extensions-policy.html): Specifies a resource policy for a REST API.
- [x-amazon-apigateway-request-validator](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-swagger-extensions-request-validator.html): Specifies a request validator, by referencing a request_validator_name of the map, to enable request validation on the containing API or a method.
- [x-amazon-apigateway-request-validators](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-swagger-extensions-request-validators.html): Defines the supported request validators for the containing API as a map between a validator name and the associated request validation rules.
- [x-amazon-apigateway-request-validators.requestValidator](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-swagger-extensions-request-validators.requestValidator.html): Specifies the validation rules of a request validator as part of the map definition.
- [x-amazon-apigateway-security-policy](https://docs.aws.amazon.com/apigateway/latest/developerguide/openapi-extensions-security-policy.html): Specifies a security policy for a REST API.
- [x-amazon-apigateway-tag-value](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-openapi-extensions-x-amazon-apigateway-tag-value.html): Specifies the value of an AWS tag for an HTTP API.


## [Security](https://docs.aws.amazon.com/apigateway/latest/developerguide/security.html)

### [Data protection](https://docs.aws.amazon.com/apigateway/latest/developerguide/data-protection.html)

Learn how the AWS shared responsibility model applies to data protection in Amazon API Gateway.

- [Data encryption](https://docs.aws.amazon.com/apigateway/latest/developerguide/data-protection-encryption.html): Learn how the AWS shared responsibility model applies to data encryption in Amazon API Gateway.
- [Internetwork traffic privacy](https://docs.aws.amazon.com/apigateway/latest/developerguide/security-traffic-privacy.html): Learn how Amazon API Gateway supports internetwork traffic privacy.

### [Identity and access management](https://docs.aws.amazon.com/apigateway/latest/developerguide/security-iam.html)

How to authenticate requests and manage access your API Gateway resources.

- [How Amazon API Gateway works with IAM](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html): Before you use IAM to manage access to API Gateway, you should understand what IAM features are available to use with API Gateway.
- [Identity-based policy examples](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_id-based-policy-examples.html): By default, IAM users and roles don't have permission to create or modify API Gateway resources.
- [Resource-based policy examples](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_resource-based-policy-examples.html): For resource-based policy examples, see .
- [Troubleshooting](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_troubleshoot.html): Use the following information to help you diagnose and fix common issues that you might encounter when working with API Gateway and IAM.
- [Using service-linked roles](https://docs.aws.amazon.com/apigateway/latest/developerguide/using-service-linked-roles.html): How to use service-linked roles to give API Gateway access to resources in your AWS account.

### [Logging and monitoring](https://docs.aws.amazon.com/apigateway/latest/developerguide/security-monitoring.html)

Tools in API Gateway for monitoring resources and responding to incidents.

- [Working with CloudTrail](https://docs.aws.amazon.com/apigateway/latest/developerguide/cloudtrail.html): Learn about logging Amazon API Gateway with AWS CloudTrail.
- [Working with AWS Config](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-config.html): Learn how to monitor API configuration using AWS Config.
- [Compliance validation](https://docs.aws.amazon.com/apigateway/latest/developerguide/compliance-validation.html): Learn what AWS services are in scope of a specific compliance program.
- [Resilience](https://docs.aws.amazon.com/apigateway/latest/developerguide/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and learn about specific Amazon API Gateway features for data resiliency.
- [Infrastructure security](https://docs.aws.amazon.com/apigateway/latest/developerguide/infrastructure-security.html): Learn how Amazon API Gateway isolates service traffic.
- [Configuration and vulnerability analysis](https://docs.aws.amazon.com/apigateway/latest/developerguide/vulnerability-analysis.html): Learn how the AWS shared responsibility model applies to vulnerability analysis in Amazon API Gateway.
- [Best practices](https://docs.aws.amazon.com/apigateway/latest/developerguide/security-best-practices.html): Learn security best practices for Amazon API Gateway.


## [Tagging](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-tagging.html)

- [API Gateway resources that can be tagged](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-tagging-supported-resources.html): Tags can be set on the following HTTP API or WebSocket API resources in the Amazon API Gateway V2 API:
- [Attribute-based access control](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-tagging-iam-policy.html): Conditions in AWS Identity and Access Management policies are part of the syntax that you use to specify permissions to API Gateway resources.


## [Quotas and important notes](https://docs.aws.amazon.com/apigateway/latest/developerguide/limits.html)

- [REST API quotas](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-execution-service-limits-table.html): Quotas for configuring and running a REST API
- [HTTP API quotas](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-quotas.html): Learn about quotas for an HTTP API.
- [Portal quotas](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-portal-quotas.html): Quotas for a portal
- [WebSocket API quotas](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-execution-service-websocket-limits-table.html): Learn about quotas for a WebSocket API.
- [Important notes](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-known-issues.html): The following section details notes that might impact your use of API Gateway.
