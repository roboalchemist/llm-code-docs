# Source: https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/llms.txt

# AWS SDK for JavaScript Developer Guide for SDK Version 3

> Guide to help developers use AWS services with browser scripts and Node.js.

- [What's the AWS SDK for JavaScript?](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/welcome.html)
- [Set up the SDK for JavaScript](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/setting-up.html)
- [Document history](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/doc-history.html)

## [Get started](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/getting-started.html)

- [SDK authentication with AWS](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/getting-your-credentials.html): You must establish how your code authenticates with AWS when developing with AWS services.
- [Get started with Node.js](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/getting-started-nodejs.html): Create a simple Node.js app with the AWS SDK for JavaScript.
- [Get started in the browser](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/getting-started-browser.html): Create a simple browser-based app with the AWS SDK for JavaScript.
- [Getting started in React Native](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/getting-started-react-native.html): Create a simple browser-based app with the AWS SDK for JavaScript.


## [Configure the SDK for JavaScript](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/configuring-the-jssdk.html)

- [Configuration per service](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/global-config-object.html): You can configure the SDK by passing configuration information to a service object.
- [Set the AWS Region](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/setting-region.html): An AWS Region is a named set of AWS resources in the same geographical area.

### [Set credentials](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/setting-credentials.html)

AWS uses credentials to identify who is calling services and whether access to the requested resources is allowed.

### [Set credentials in Node.js](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/setting-credentials-node.html)

We recommend that new users who are developing locally and are not given a method of authentication by their employer to set up AWS IAM Identity Center.

- [Credentials for Amazon EC2 from IAM roles](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/loading-node-credentials-iam.html): If you run your Node.js application on an Amazon EC2 instance, you can leverage IAM roles for Amazon EC2 to automatically provide credentials to the instance.
- [Credentials for a Node.js Lambda function](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/loading-node-credentials-lambda.html): When you create an AWS Lambda function, you must create a special IAM role that has permission to execute the function.

### [Set credentials in a web browser](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/setting-credentials-browser.html)

There are several ways to supply your credentials to the SDK from browser scripts.

- [Using Amazon Cognito Identity](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/loading-browser-credentials-cognito.html): The recommended way to obtain AWS credentials for your browser scripts is to use the Amazon Cognito Identity credentials client CognitoIdentityClient.

### [Node.js considerations](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/node-js-considerations.html)

Configure the SDK for JavaScript for Node.js.

- [Configure maxSockets in Node.js](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/node-configuring-maxsockets.html): Configure maxSockets in Node.js.
- [Reuse connections with keep-alive in Node.js](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/node-reusing-connections.html): The default Node.js HTTP/HTTPS agent creates a new TCP connection for every new request.
- [Configure proxies for Node.js](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/node-configuring-proxies.html): Install and use a third-party HTTP agent proxy.
- [Register certificate bundles in Node.js](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/node-registering-certs.html): Include a specified set of certificates in your Node.js application.

### [Browser Script Considerations](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/browser-js-considerations.html)

Build and configure the SDK for JavaScript for browsers, using the SDK builder, the CLI, or browserify.

- [Build the SDK for Browsers](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/building-sdk-for-browsers.html): Links to additional information of use to users of the SDK for JavaScript.
- [Cross-origin resource sharing (CORS)](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/cors.html): CORS considerations for users of the SDK for JavaScript.
- [Bundle with webpack](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/webpack.html): Bundle web applications using webpack with the SDK for JavaScript.


## [Work with AWS services](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/working-with-services.html)

- [Create and call service objects](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/creating-and-calling-service-objects.html): Create and call service objects using the SDK for JavaScript.

### [Call services asynchronously](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/calling-services-asynchronously.html)

All requests made through the SDK are asynchronous.

- [Manage asynchronous calls](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/making-asynchronous-calls.html): For example, the home page of an e-commerce website lets returning customers sign in.
- [Use async/await](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/using-async-await.html): Rather than using promises, you should consider using async/await.
- [Use promises](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/using-promises.html): Use JavaScript promises for asynchronous calls with the AWS SDK for JavaScript.
- [Use a callback function](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/using-a-callback-function.html): Use a callback function for asynchronous calls with the SDK for JavaScript.
- [Create service client requests](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/the-request-object.html): Describes creating requests for service clients in the AWS SDK for JavaScript.
- [Handle service client responses](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/the-response-object.html): Describes handling responses from service clients in the AWS SDK for JavaScript.
- [Work with JSON](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/working-with-json.html): Work with JSON in the AWS SDK for JavaScript.
- [Logging AWS SDK for JavaScript Calls](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/logging-sdk-calls.html): The AWS SDK for JavaScript is instrumented with a built-in logger so you can log API calls you make with the SDK for JavaScript.
- [Use AWS account-based endpoints with DynamoDB](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/ddb-account-based-endpoints-v3.html): DynamoDB offers AWS account-based endpoints that can improve performance by using your AWS account ID to streamline request routing.
- [Amazon S3 Checksums](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/s3-checksums.html): Learn how to use Amazon S3 checksums with the AWS SDK for JavaScript.

### [Code examples subset with guidance](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/sdk-code-samples.html)

Examples of how to access various services using the AWS SDK for JavaScript.

- [JavaScript ES6/CommonJS syntax](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/sdk-example-javascript-syntax.html): The AWS SDK for JavaScript code examples are written in ECMAScript 6 (ES6).

### [AWS Elemental MediaConvert examples](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/emc-examples.html)

Examples that show how to use the MediaConvert client class.

- [Creating and managing jobs](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/emc-examples-jobs.html): Example that shows how to create and manage conversion jobs in AWS Elemental MediaConvert.
- [Using job templates](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/emc-examples-templates.html): JavaScript code example that applies to Node.js execution
- [AWS Lambda examples](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/lambda-examples.html): Reference to tutorial that shows how to use the Lambda client class.
- [Amazon Lex examples](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/lex-examples.html): Reference to tutorial that shows how to use the Lex Runtime Service client class.
- [Amazon Polly examples](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/polly-examples.html): JavaScript code example that applies to Node.js execution

### [Amazon Redshift examples](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/redshift-examples.html)

Examples that show how to use the Amazon Redshift client class.

- [Amazon Redshift examples](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/redshift-examples-section.html): In this example, a series of Node.js modules are used to create, modify, describe the parameters of, and then delete Amazon Redshift clusters using the following methods of the Redshift client class:

### [Amazon SES examples](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/ses-examples.html)

Examples that show how to use the Amazon SES client class.

- [Managing identities](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/ses-examples-managing-identities.html): JavaScript code example that applies to Node.js execution
- [Working with email templates](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/ses-examples-creating-template.html): JavaScript code example that applies to Node.js execution
- [Sending email using Amazon SES](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/ses-examples-sending-email.html): JavaScript code example that applies to Node.js execution

### [Amazon SNS Examples](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/sns-examples.html)

Examples that show how to use the Amazon SNS client class.

- [Managing Topics](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/sns-examples-managing-topics.html): JavaScript code example that applies to Node.js execution
- [Publishing Messages to a Topic](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/sns-examples-publishing-messages.html): JavaScript code example that applies to Node.js execution
- [Managing Subscriptions](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/sns-examples-subscribing-unsubscribing-topics.html): JavaScript code example that applies to Node.js execution
- [Sending SMS Messages](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/sns-examples-sending-sms.html): JavaScript code example that applies to Node.js execution

### [Amazon Transcribe examples](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/Transcribe-examples.html)

Examples that show how to use the Amazon Transcribe client class.

- [Amazon Transcribe examples](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/transcribe-examples-section.html): In this example, a series of Node.js modules are used to create,list, and delete transcription jobs using the following methods of the TranscribeService client class:
- [Amazon Transcribe medical examples](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/transcribe-medical-examples-section.html): In this example, a series of Node.js modules are used to create,list, and delete medical transcription jobs using the following methods of the TranscribeService client class:
- [Cross-service: Setting up Node.js on an Amazon EC2 instance](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/setting-up-node-on-ec2-instance.html): A common scenario for using Node.js with the SDK for JavaScript is to set up and run a Node.js web application on an Amazon Elastic Compute Cloud (Amazon EC2) instance.
- [Cross-service: Amazon API Gateway and Lambda](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/api-gateway-invoking-lambda-example.html): You can invoke a Lambda function by using Amazon API Gateway, which is an AWS service for creating, publishing, maintaining, monitoring, and securing REST, HTTP, and WebSocket APIs at scale.
- [Cross-service: Scheduled Lambda events](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/scheduled-events-invoking-lambda-example.html): You can create a scheduled event that invokes an AWS Lambda function by using an Amazon CloudWatch Event.
- [Cross-service: Amazon Lex example](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/lex-bot-example.html): You can create an Amazon Lex chatbot within a web application to engage your web site visitors.


## [Code examples](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/javascript_code_examples.html)

- [API Gateway](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/javascript_api-gateway_code_examples.html): Code examples that show how to use AWS SDK for JavaScript (v3) with API Gateway.
- [Aurora](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/javascript_aurora_code_examples.html): Code examples that show how to use AWS SDK for JavaScript (v3) with Aurora.
- [Auto Scaling](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/javascript_auto-scaling_code_examples.html): Code examples that show how to use AWS SDK for JavaScript (v3) with Auto Scaling.
- [Amazon Bedrock](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/javascript_bedrock_code_examples.html): Code examples that show how to use AWS SDK for JavaScript (v3) with Amazon Bedrock.
- [Amazon Bedrock Runtime](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/javascript_bedrock-runtime_code_examples.html): Code examples that show how to use AWS SDK for JavaScript (v3) with Amazon Bedrock Runtime.
- [Amazon Bedrock Agents](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/javascript_bedrock-agent_code_examples.html): Code examples that show how to use AWS SDK for JavaScript (v3) with Amazon Bedrock Agents.
- [Amazon Bedrock Agents Runtime](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/javascript_bedrock-agent-runtime_code_examples.html): Code examples that show how to use AWS SDK for JavaScript (v3) with Amazon Bedrock Agents Runtime.
- [CloudWatch](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/javascript_cloudwatch_code_examples.html): Code examples that show how to use AWS SDK for JavaScript (v3) with CloudWatch.
- [CloudWatch Events](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/javascript_cloudwatch-events_code_examples.html): Code examples that show how to use AWS SDK for JavaScript (v3) with CloudWatch Events.
- [CloudWatch Logs](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/javascript_cloudwatch-logs_code_examples.html): Code examples that show how to use AWS SDK for JavaScript (v3) with CloudWatch Logs.
- [CodeBuild](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/javascript_codebuild_code_examples.html): Code examples that show how to use AWS SDK for JavaScript (v3) with CodeBuild.
- [Amazon Cognito Identity](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/javascript_cognito-identity_code_examples.html): Code examples that show how to use AWS SDK for JavaScript (v3) with Amazon Cognito Identity.
- [Amazon Cognito Identity Provider](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/javascript_cognito-identity-provider_code_examples.html): Code examples that show how to use AWS SDK for JavaScript (v3) with Amazon Cognito Identity Provider.
- [Amazon Comprehend](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/javascript_comprehend_code_examples.html): Code examples that show how to use AWS SDK for JavaScript (v3) with Amazon Comprehend.
- [Amazon DocumentDB](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/javascript_docdb_code_examples.html): Code examples that show how to use AWS SDK for JavaScript (v3) with Amazon DocumentDB.
- [DynamoDB](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/javascript_dynamodb_code_examples.html): Code examples that show how to use AWS SDK for JavaScript (v3) with DynamoDB.
- [Amazon EC2](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/javascript_ec2_code_examples.html): Code examples that show how to use AWS SDK for JavaScript (v3) with Amazon EC2.
- [Elastic Load Balancing - Version 2](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/javascript_elastic-load-balancing-v2_code_examples.html): Code examples that show how to use AWS SDK for JavaScript (v3) with Elastic Load Balancing - Version 2.
- [AWS Entity Resolution](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/javascript_entityresolution_code_examples.html): Code examples that show how to use AWS SDK for JavaScript (v3) with AWS Entity Resolution.
- [EventBridge](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/javascript_eventbridge_code_examples.html): Code examples that show how to use AWS SDK for JavaScript (v3) with EventBridge.
- [Amazon Glacier](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/javascript_glacier_code_examples.html): Code examples that show how to use AWS SDK for JavaScript (v3) with Amazon Glacier.
- [AWS Glue](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/javascript_glue_code_examples.html): Code examples that show how to use AWS SDK for JavaScript (v3) with AWS Glue.
- [HealthImaging](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/javascript_medical-imaging_code_examples.html): Code examples that show how to use AWS SDK for JavaScript (v3) with HealthImaging.
- [IAM](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/javascript_iam_code_examples.html): Code examples that show how to use AWS SDK for JavaScript (v3) with IAM.
- [AWS IoT SiteWise](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/javascript_iotsitewise_code_examples.html): Code examples that show how to use AWS SDK for JavaScript (v3) with AWS IoT SiteWise.
- [Kinesis](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/javascript_kinesis_code_examples.html): Code examples that show how to use AWS SDK for JavaScript (v3) with Kinesis.
- [Lambda](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/javascript_lambda_code_examples.html): Code examples that show how to use AWS SDK for JavaScript (v3) with Lambda.
- [Amazon Lex](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/javascript_lex_code_examples.html): Code examples that show how to use AWS SDK for JavaScript (v3) with Amazon Lex.
- [Amazon Location](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/javascript_location_code_examples.html): Code examples that show how to use AWS SDK for JavaScript (v3) with Amazon Location.
- [Amazon MSK](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/javascript_kafka_code_examples.html): Code examples that show how to use AWS SDK for JavaScript (v3) with Amazon MSK.
- [Amazon Personalize](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/javascript_personalize_code_examples.html): Code examples that show how to use AWS SDK for JavaScript (v3) with Amazon Personalize.
- [Amazon Personalize Events](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/javascript_personalize-events_code_examples.html): Code examples that show how to use AWS SDK for JavaScript (v3) with Amazon Personalize Events.
- [Amazon Personalize Runtime](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/javascript_personalize-runtime_code_examples.html): Code examples that show how to use AWS SDK for JavaScript (v3) with Amazon Personalize Runtime.
- [Amazon Pinpoint](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/javascript_pinpoint_code_examples.html): Code examples that show how to use AWS SDK for JavaScript (v3) with Amazon Pinpoint.
- [Amazon Polly](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/javascript_polly_code_examples.html): Code examples that show how to use AWS SDK for JavaScript (v3) with Amazon Polly.
- [Amazon RDS](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/javascript_rds_code_examples.html): Code examples that show how to use AWS SDK for JavaScript (v3) with Amazon RDS.
- [Amazon RDS Data Service](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/javascript_rds-data_code_examples.html): Code examples that show how to use AWS SDK for JavaScript (v3) with Amazon RDS Data Service.
- [Amazon Redshift](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/javascript_redshift_code_examples.html): Code examples that show how to use AWS SDK for JavaScript (v3) with Amazon Redshift.
- [Amazon Rekognition](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/javascript_rekognition_code_examples.html): Code examples that show how to use AWS SDK for JavaScript (v3) with Amazon Rekognition.
- [Amazon S3](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/javascript_s3_code_examples.html): Code examples that show how to use AWS SDK for JavaScript (v3) with Amazon S3.
- [SageMaker AI](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/javascript_sagemaker_code_examples.html): Code examples that show how to use AWS SDK for JavaScript (v3) with SageMaker AI.
- [Secrets Manager](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/javascript_secrets-manager_code_examples.html): Code examples that show how to use AWS SDK for JavaScript (v3) with Secrets Manager.
- [Amazon SES](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/javascript_ses_code_examples.html): Code examples that show how to use AWS SDK for JavaScript (v3) with Amazon SES.
- [Amazon SNS](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/javascript_sns_code_examples.html): Code examples that show how to use AWS SDK for JavaScript (v3) with Amazon SNS.
- [Amazon SQS](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/javascript_sqs_code_examples.html): Code examples that show how to use AWS SDK for JavaScript (v3) with Amazon SQS.
- [Step Functions](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/javascript_sfn_code_examples.html): Code examples that show how to use AWS SDK for JavaScript (v3) with Step Functions.
- [AWS STS](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/javascript_sts_code_examples.html): Code examples that show how to use AWS SDK for JavaScript (v3) with AWS STS.
- [Support](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/javascript_support_code_examples.html): Code examples that show how to use AWS SDK for JavaScript (v3) with Support.
- [Systems Manager](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/javascript_ssm_code_examples.html): Code examples that show how to use AWS SDK for JavaScript (v3) with Systems Manager.
- [Amazon Textract](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/javascript_textract_code_examples.html): Code examples that show how to use AWS SDK for JavaScript (v3) with Amazon Textract.
- [Amazon Transcribe](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/javascript_transcribe_code_examples.html): Code examples that show how to use AWS SDK for JavaScript (v3) with Amazon Transcribe.
- [Amazon Translate](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/javascript_translate_code_examples.html): Code examples that show how to use AWS SDK for JavaScript (v3) with Amazon Translate.


## [Security](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/security.html)

- [Data protection](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/data-protection.html): Learn how the AWS shared responsibility model applies to data protection in this AWS product or service.
- [Identity and Access Management](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/security-iam.html): How to authenticate requests and manage access to your AWS resources.
- [Compliance Validation](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/compliance-validation.html): Provides information about compliance validation for this AWS product or service.
- [Resilience](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/disaster-recovery-resiliency.html): Provides information about resilience for this AWS Product or Service.
- [Infrastructure Security](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/infrastructure-security.html): Provides information about infrastructure security for this AWS product or service.
- [Enforce a minimum TLS version](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/enforcing-tls.html): How to verify and configure the version of TLS used by the SDK for JavaScript.


## [Migrate to v3](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/migrating.html)

### [What's different between the v2 and v3](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/migrate-whats-different.html)

What's different between the AWS SDK for JavaScript v2 and v3.

- [Client constructors](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/migrate-client-constructors.html): This list is indexed by v2 config parameters.
- [Credential providers](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/migrate-credential-providers.html): In v2, the SDK for JavaScript provides a list of credential providers to choose from, as well as a credentials provider chain, available by default on Node.js, that tries to load the AWS credentials from all the most common providers.
- [Amazon S3 considerations](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/migrate-s3.html)
- [DynamoDB document client](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/migrate-dynamodb-doc-client.html)
- [Waiters and signers](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/migrate-waiters-signers.html): This page describes the usage of waiters and signers in the AWS SDK for JavaScript v3.
- [Notes on specific service clients](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/migrate-service-client-notes.html)
- [Supplemental documentation](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/migrate-supp-docs.html): The following table includes links to supplemental documentation that will help you use and understand the AWS SDK for JavaScript (v3).
