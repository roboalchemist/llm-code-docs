# Source: https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/llms.txt

# AWS Serverless Application Model Developer Guide

> Introduces you to AWS SAM, and shows you how to use AWS SAM to define, test, and deploy serverless applications.

- [How to use AWS SAM](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/chapter-using-sam.html)
- [Document history](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/doc-history.html)

## [What is AWS SAM?](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/what-is-sam.html)

- [How it works](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/what-is-sam-overview.html): Describes how you can use the AWS Serverless Application Model (AWS SAM) to build serverless applications.
- [Serverless concepts](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/what-is-concepts.html): Overview of basic serverless concepts that you should know before using the AWS Serverless Application Model.
- [Infrastructure as Code](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/what-is-iac.html): Learn how Infrastructure as Code (IaC) helps you automate the deployment and management of your AWS resources, and how AWS SAM fits within the AWS IaC ecosystem.


## [Getting started](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-getting-started.html)

- [Prerequisites](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/prerequisites.html): Prerequisites required before installing the AWS SAMÂ CLI.

### [Install the AWS SAMÂ CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html)

This section describes how to install the AWS SAMÂ CLI on macOS, Windows, and Linux.

- [Optional: Verify the AWS SAMÂ CLI installer](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/reference-sam-cli-install-verify.html): Verify the integrity of the AWS SAMÂ CLI package installer.
- [Hello World Tutorial](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-getting-started-hello-world.html): Learn how to use AWS SAM to deploy a basic Hello World application to the AWS Cloud.
- [Converting from Lambda](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/convert-lambda-to-sam.html): Learn how to convert existing Lambda functions to AWS SAM applications.


## [AWS SAMÂ CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/using-sam-cli.html)

- [Configuring the AWS SAMÂ CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/using-sam-cli-configure.html): Configure credentials, basic settings, and project settings for the AWS SAMÂ CLI.
- [Core commands](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/using-sam-cli-corecommands.html): Use AWS SAMÂ CLI core commands to create, build, test, deploy, and sync your serverless application..
- [Local testing with AWS SAMÂ CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/using-sam-cli-local-testing.html): Learn how to use the AWS SAMÂ CLI for local testing of your serverless applications.


## [AWS SAM template](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-specification.html)

### [Template anatomy](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-specification-template-anatomy.html)

Learn about the format of an AWS SAM template file and how it differs from an CloudFormation template file.

- [Globals](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-specification-template-anatomy-globals.html): Learn about the Globals section of an AWS SAM template.

### [Resources and properties](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-specification-resources-and-properties.html)

This section contains details of AWS SAM resource and property types.

### [AWS::Serverless::Api](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-resource-api.html)

This section contains details of the AWS SAM resource and property type AWS::Serverless::Api.

### [ApiAuth](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-property-api-apiauth.html)

This section contains ApiAuth details of the AWS SAM resource and property type AWS::Serverless::Api.

- [ApiUsagePlan](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-property-api-apiusageplan.html): This section contains ApiUsagePlan details related to ApiAuth for the AWS SAM resource and property type AWS::Serverless::Api.

### [CognitoAuthorizer](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-property-api-cognitoauthorizer.html)

This section contains CognitoAuthorizer details related to ApiAuth for the AWS SAM resource and property type AWS::Serverless::Api.

- [CognitoAuthorizationIdentity](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-property-api-cognitoauthorizationidentity.html): This property can be used to specify an IdentitySource in an incoming request for an authorizer.

### [LambdaRequestAuthorizer](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-property-api-lambdarequestauthorizer.html)

This section contains LambdaRequestAuthorizer details related to ApiAuth for the AWS SAM resource and property type AWS::Serverless::Api.

- [LambdaRequestAuthorizationIdentity](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-property-api-lambdarequestauthorizationidentity.html): This property can be used to specify an IdentitySource in an incoming request for an authorizer.

### [LambdaTokenAuthorizer](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-property-api-lambdatokenauthorizer.html)

This section contains LambdaTokenAuthorizer details related to ApiAuth for the AWS SAM resource and property type AWS::Serverless::Api.

- [LambdaTokenAuthorizationIdentity](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-property-api-lambdatokenauthorizationidentity.html): This section contains LambdaTokenAuthorizationIdentity details related to ApiAuth for the AWS SAM resource and property type AWS::Serverless::Api.
- [ResourcePolicyStatement](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-property-api-resourcepolicystatement.html): This section contains ResourcePolicyStatement details related to ApiAuth for the AWS SAM resource and property type AWS::Serverless::Api.
- [ApiDefinition](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-property-api-apidefinition.html): An OpenAPI document defining the API.
- [CorsConfiguration](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-property-api-corsconfiguration.html): Manage cross-origin resource sharing (CORS) for your API Gateway APIs.

### [DomainConfiguration](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-property-api-domainconfiguration.html)

Configures a custom domain for an API.

- [DomainAccessAssociation](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-property-api-domainaccessassociation.html): Configures domain access association for an API.
- [Route53Configuration](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-property-api-route53configuration.html): Configures the Route53 record sets for an API.
- [EndpointConfiguration](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-property-api-endpointconfiguration.html): The endpoint type of a REST API.

### [AWS::Serverless::Application](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-resource-application.html)

This section contains details related to the AWS SAM resource and property type AWS::Serverless::Application.

- [ApplicationLocationObject](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-property-application-applicationlocationobject.html): This section contains ApplicationLocationObject details related to the AWS SAM resource and property type AWS::Serverless::Application.

### [AWS::Serverless::CapacityProvider](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-resource-capacityprovider.html)

This section contains details related to the AWS SAM resource and property type AWS::Serverless::CapacityProvider.

- [VpcConfig](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-property-capacityprovider-vpcconfig.html): This section contains VpcConfig details related to the AWS SAM resource and property type AWS::Serverless::CapacityProvider.
- [InstanceRequirements](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-property-capacityprovider-instancerequirements.html): This section contains InstanceRequirements details related to the AWS SAM resource and property type AWS::Serverless::CapacityProvider.
- [ScalingConfig](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-property-capacityprovider-scalingconfig.html): This section contains ScalingConfig details related to the AWS SAM resource and property type AWS::Serverless::CapacityProvider.

### [AWS::Serverless::Connector](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-resource-connector.html)

This section contains details related to the AWS SAM resource and property type AWS::Serverless::Connector.

- [ResourceReference](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-property-connector-resourcereference.html): This section contains ResourceReference details related to the AWS SAM resource and property type AWS::Serverless::Connector.
- [SourceReference](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-property-connector-sourcereference.html): This section contains SourceReference details related to the AWS SAM resource and property type AWS::Serverless::Connector.

### [AWS::Serverless::Function](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-resource-function.html)

This section contains details related to the AWS SAM resource and property type AWS::Serverless::Function.

- [DeadLetterQueue](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-property-function-deadletterqueue.html): This section contains DeadLetterQueue details related to the AWS SAM resource and property type AWS::Serverless::Function.

### [DeploymentPreference](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-property-function-deploymentpreference.html)

This section contains DeploymentPreference details related to the AWS SAM resource and property type AWS::Serverless::Function.

- [Hooks](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-property-function-hooks.html): This section contains Hooks details related to the AWS SAM resource and property type AWS::Serverless::Function.
- [DurableConfig](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-property-function-durableconfig.html): This section contains DurableConfig details related to the AWS SAM resource and property type AWS::Serverless::Function.

### [EventInvokeConfiguration](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-property-function-eventinvokeconfiguration.html)

This section contains EventInvokeConfiguration details related to the AWS SAM resource and property type AWS::Serverless::Function.

### [EventInvokeDestinationConfiguration](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-property-function-eventinvokedestinationconfiguration.html)

This section contains EventInvokeDestinationConfiguration details related to the AWS SAM resource and property type AWS::Serverless::Function.

- [OnFailure](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-property-function-onfailure.html): This section describes a destination for events that failed processing for EventInvokeDestinationConfiguration, which is used for the AWS SAM resource and property type AWS::Serverless::Function.
- [OnSuccess](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-property-function-onsuccess.html): This section describes a destination for events that processed successfully for EventInvokeDestinationConfiguration, which is used for the AWS SAM resource and property type AWS::Serverless::Function.

### [EventSource](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-property-function-eventsource.html)

This section contains EventSource details related to the AWS SAM resource and property type AWS::Serverless::Function.

- [AlexaSkill](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-property-function-alexaskill.html): This section contains EventSource details related to AlexaSkill for the AWS SAM resource and property type AWS::Serverless::Function.

### [Api](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-property-function-api.html)

This section contains EventSource details related to Api for the AWS SAM resource and property type AWS::Serverless::Function.

### [ApiFunctionAuth](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-property-function-apifunctionauth.html)

This section contains EventSource details related to Api for the AWS SAM resource and property type AWS::Serverless::Function.

- [ResourcePolicyStatement](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-property-function-resourcepolicystatement.html): This section contains EventSource details related to Api for the AWS SAM resource and property type AWS::Serverless::Function.
- [RequestModel](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-property-function-requestmodel.html): This section contains EventSource details related to Api for the AWS SAM resource and property type AWS::Serverless::Function.
- [RequestParameter](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-property-function-requestparameter.html): This section contains EventSource details related to Api for the AWS SAM resource and property type AWS::Serverless::Function.
- [CloudWatchEvent](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-property-function-cloudwatchevent.html): This section contains CloudWatchEvent details related to EventSource for the AWS SAM resource and property type AWS::Serverless::Function.
- [CloudWatchLogs](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-property-function-cloudwatchlogs.html): This section contains CloudWatchLogs details related to Api for the AWS SAM resource and property type AWS::Serverless::Function.
- [Cognito](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-property-function-cognito.html): This section contains Cognito details related to EventSource for the AWS SAM resource and property type AWS::Serverless::Function.
- [DocumentDB](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-property-function-documentdb.html): This section contains DocumentDB details related to EventSource for the AWS SAM resource and property type AWS::Serverless::Function.
- [DynamoDB](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-property-function-dynamodb.html): This section contains DynamoDB details related to EventSource for the AWS SAM resource and property type AWS::Serverless::Function.

### [EventBridgeRule](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-property-function-eventbridgerule.html)

This section contains EventBridgeRule details related to EventSource for the AWS SAM resource and property type AWS::Serverless::Function.

- [DeadLetterConfig](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-property-function-deadletterconfig.html): This section contains DeadLetterConfig details related to EventBridgeRule for the AWS SAM resource and property type AWS::Serverless::Function.
- [Target](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-property-function-target.html): This section contains Target details related to EventBridgeRule for the AWS SAM resource and property type AWS::Serverless::Function.

### [HttpApi](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-property-function-httpapi.html)

This section contains HttpApi details related to EventSource for the AWS SAM resource and property type AWS::Serverless::Function.

- [HttpApiFunctionAuth](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-property-function-httpapifunctionauth.html): This section contains HttpApiFunctionAuth details related to EventSource for the AWS SAM resource and property type AWS::Serverless::Function.
- [IoTRule](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-property-function-iotrule.html): This section contains IoTRule details related to EventSource for the AWS SAM resource and property type AWS::Serverless::Function.
- [Kinesis](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-property-function-kinesis.html): This section contains Kinesis details related to EventSource for the AWS SAM resource and property type AWS::Serverless::Function.
- [MQ](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-property-function-mq.html): This section contains MQ details related to EventSource for the AWS SAM resource and property type AWS::Serverless::Function.
- [MSK](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-property-function-msk.html): This section contains MSK details related to EventSource for the AWS SAM resource and property type AWS::Serverless::Function.
- [S3](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-property-function-s3.html): This section contains S3 details related to EventSource for the AWS SAM resource and property type AWS::Serverless::Function.

### [Schedule](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-property-function-schedule.html)

The object describing a Schedule event source type, which sets your serverless function as the target of an Amazon EventBridge rule that triggers on a schedule.

- [DeadLetterConfig](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-property-function-scheduledeadletterconfig.html): The object used to specify the Amazon Simple Queue Service (Amazon SQS) queue where EventBridge sends events after a failed target invocation.
- [ScheduleV2](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-property-function-schedulev2.html): The object describing a ScheduleV2 event source type, which sets your serverless function as the target of an Amazon EventBridge Scheduler event that triggers on a schedule.
- [SelfManagedKafka](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-property-function-selfmanagedkafka.html): The object describing a SelfManagedKafka event source type.

### [SNS](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-property-function-sns.html)

This section contains SNS details related to EventSource for the AWS SAM resource and property type AWS::Serverless::Function.

- [SqsSubscriptionObject](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-property-function-sqssubscriptionobject.html): This section contains SQS details related to EventSource for the AWS SAM resource and property type AWS::Serverless::Function.
- [SQS](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-property-function-sqs.html): This section contains SQS details related to EventSource for the AWS SAM resource and property type AWS::Serverless::Function.
- [FunctionCode](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-property-function-functioncode.html): The deployment package for a Lambda function.
- [FunctionUrlConfig](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-property-function-functionurlconfig.html): Configure a Lambda function URL using the FunctionUrlConfig property of the AWS::Serverless::Function resource in an AWS SAM template.
- [CapacityProviderConfig](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-property-function-capacityproviderconfig.html): This section contains CapacityProviderConfig details related to the AWS SAM resource and property type AWS::Serverless::Function.
- [FunctionScalingConfig](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-property-function-functionscalingconfig.html): This section contains FunctionScalingConfig details related to the AWS SAM resource and property type AWS::Serverless::Function.

### [AWS::Serverless::GraphQLApi](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-resource-graphqlapi.html)

This section contains details related to the AWS SAM resource and property type AWS::Serverless::GraphQLApi.

- [ApiKeys](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-property-graphqlapi-apikeys.html): Use AWS SAM to create a unique key that can be used to perform GraphQL operations requiring an API key.

### [Auth](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-property-graphqlapi-auth.html)

Use AWS SAM to configure authorization for your GraphQL API.

- [AuthProvider](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-property-graphqlapi-auth-authprovider.html): Use AWS SAM to configure optional authorization configuration for your additional GraphQL API authorization types.

### [DataSource](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-property-graphqlapi-datasource.html)

Use AWS SAM to configure a data source that your GraphQL API resolver can connect to.

- [DynamoDb](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-property-graphqlapi-datasource-dynamodb.html): Use AWS SAM to configure an Amazon DynamoDB table as a data source for your GraphQL API resolver.
- [Lambda](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-property-graphqlapi-datasource-lambda.html): Use AWS SAM to configure an AWS Lambda function as a data source for your GraphQL API resolver.

### [Function](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-property-graphqlapi-function.html)

Use AWS SAM to configure functions in GraphQL APIs to perform certain operations.

- [Runtime](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-property-graphqlapi-function-runtime.html): Use AWS SAM to configure an AWS Lambda function as a data source for your GraphQL API resolver.

### [Resolver](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-property-graphqlapi-resolver.html)

Use AWS SAM to configure resolvers for the fields of your GraphQL API.

- [Runtime](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-property-graphqlapi-resolver-runtime.html): Use AWS SAM to configure an AWS Lambda function as a data source for your GraphQL API resolver.

### [AWS::Serverless::HttpApi](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-resource-httpapi.html)

This section contains details related to the AWS SAM resource and property type AWS::Serverless::HttpApi.

### [HttpApiAuth](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-property-httpapi-httpapiauth.html)

This section contains HttpApiAuth details for the AWS SAM resource and property type AWS::Serverless::HttpApi.

### [LambdaAuthorizer](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-property-httpapi-lambdaauthorizer.html)

This section contains LambdaAuthorizer details related to HttpApiAuth for the AWS SAM resource and property type AWS::Serverless::HttpApi.

- [LambdaAuthorizationIdentity](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-property-httpapi-lambdaauthorizationidentity.html): This section contains LambdaAuthorizationIdentity details related to HttpApiAuth for the AWS SAM resource and property type AWS::Serverless::HttpApi.
- [OAuth2Authorizer](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-property-httpapi-oauth2authorizer.html): This section contains OAuth2Authorizer details related to HttpApiAuth for the AWS SAM resource and property type AWS::Serverless::HttpApi.
- [HttpApiCorsConfiguration](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-property-httpapi-httpapicorsconfiguration.html): This section contains HttpApiCorsConfiguration details related to HttpApiAuth for the AWS SAM resource and property type AWS::Serverless::HttpApi.
- [HttpApiDefinition](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-property-httpapi-httpapidefinition.html): This section contains HttpApiDefinition details related to HttpApiAuth for the AWS SAM resource and property type AWS::Serverless::HttpApi.

### [HttpApiDomainConfiguration](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-property-httpapi-httpapidomainconfiguration.html)

Configures a custom domain for an API.

- [Route53Configuration](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-property-httpapi-route53configuration.html): Configures the Route53 record sets for an API.

### [AWS::Serverless::LayerVersion](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-resource-layerversion.html)

This section contains details related to the AWS SAM resource and property type AWS::Serverless::LayerVersion.

- [LayerContent](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-property-layerversion-layercontent.html): This section contains LayerContent details related to the AWS SAM resource and property type AWS::Serverless::LayerVersion.

### [AWS::Serverless::SimpleTable](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-resource-simpletable.html)

This section contains details related to the AWS SAM resource and property type AWS::Serverless::SimpleTable.

- [PrimaryKeyObject](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-property-simpletable-primarykeyobject.html): This section contains PrimaryKeyObject details related to the AWS SAM resource and property type AWS::Serverless::SimpleTable.
- [ProvisionedThroughputObject](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-property-simpletable-provisionedthroughputobject.html): This section contains ProvisionedThroughput details related to the AWS SAM resource and property type AWS::Serverless::SimpleTable.

### [AWS::Serverless::StateMachine](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-resource-statemachine.html)

This section contains details related to the AWS SAM resource and property type AWS::Serverless::StateMachine.

### [EventSource](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-property-statemachine-statemachineeventsource.html)

This section contains EventSource details related to the AWS SAM resource and property type AWS::Serverless::StateMachine.

### [Api](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-property-statemachine-statemachineapi.html)

This section contains Api details related to the AWS SAM resource and property type AWS::Serverless::StateMachine.

### [ApiStateMachineAuth](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-property-statemachine-apistatemachineauth.html)

This section contains API authorization details related to the AWS SAM resource and property type AWS::Serverless::StateMachine.

- [ResourcePolicyStatement](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-property-statemachine-resourcepolicystatement.html): This section contains ResourcePolicyStatement details related to the AWS SAM resource and property type AWS::Serverless::StateMachine.
- [CloudWatchEvent](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-property-statemachine-statemachinecloudwatchevent.html): This section contains CloudWatchEvent details related to the AWS SAM resource and property type AWS::Serverless::StateMachine.

### [EventBridgeRule](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-property-statemachine-statemachineeventbridgerule.html)

This section contains EventBridgeRule details related to the AWS SAM resource and property type AWS::Serverless::StateMachine.

- [DeadLetterConfig](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-property-statemachine-statemachinedeadletterconfig.html): This section contains DeadLetterConfig details related to EventBridgeRule for the AWS SAM resource and property type AWS::Serverless::StateMachine.
- [Target](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-property-statemachine-statemachinetarget.html): This section contains Target details related to EventBridgeRule for the AWS SAM resource and property type AWS::Serverless::StateMachine.

### [Schedule](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-property-statemachine-statemachineschedule.html)

This section contains Schedule details related to EventBridgeRule for the AWS SAM resource and property type AWS::Serverless::StateMachine.

- [DeadLetterConfig](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-property-statemachine-statemachinescheduledeadletterconfig.html): This section contains DeadLetterConfig details related to EventBridgeRule for the AWS SAM resource and property type AWS::Serverless::StateMachine.
- [Target](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-property-statemachine-statemachinescheduletarget.html): This section contains Target details related to EventBridgeRule for the AWS SAM resource and property type AWS::Serverless::StateMachine.
- [ScheduleV2](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-property-statemachine-statemachineschedulev2.html): This section contains ScheduleV2 details related to EventBridgeRule for the AWS SAM resource and property type AWS::Serverless::StateMachine.

### [Generated resources](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-specification-generated-resources.html)

This section lists the CloudFormation resources that AWS Serverless Application Model (AWS SAM) generates when AWS SAM template files are processed.

- [AWS::Serverless::Api](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-specification-generated-resources-api.html): This section lists the CloudFormation resources that AWS Serverless Application Model (AWS SAM) generates when AWS SAM AWS::Serverless::Api is specified.
- [AWS::Serverless::Application](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-specification-generated-resources-application.html): This section lists the CloudFormation resources that AWS Serverless Application Model (AWS SAM) generates when AWS SAM AWS::Serverless::Application is specified.
- [AWS::Serverless::CapacityProvider](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-specification-generated-resources-capacityprovider.html): This section lists the CloudFormation resources that AWS Serverless Application Model (AWS SAM) generates when AWS SAM AWS::Serverless::CapacityProvider is specified.
- [AWS::Serverless::Connector](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-specification-generated-resources-connector.html): Learn which CloudFormation resources AWS SAM generates when you specify the AWS::Serverless::Connector resource in an AWS SAM template.
- [AWS::Serverless::Function](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-specification-generated-resources-function.html): This section lists the CloudFormation resources that AWS Serverless Application Model (AWS SAM) generates when AWS SAM AWS::Serverless::Function is specified.
- [AWS::Serverless::GraphQLApi](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-specification-generated-resources-graphqlapi.html): This section lists the CloudFormation resources that AWS Serverless Application Model (AWS SAM) generates when AWS SAM AWS::Serverless::GraphQLApi is specified.
- [AWS::Serverless::HttpApi](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-specification-generated-resources-httpapi.html): This section lists the CloudFormation resources that AWS Serverless Application Model (AWS SAM) generates when AWS SAM AWS::Serverless::HttpApi is specified.
- [AWS::Serverless::LayerVersion](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-specification-generated-resources-layerversion.html): This section lists the CloudFormation resources that AWS Serverless Application Model (AWS SAM) generates when AWS SAM AWS::Serverless::LayerVersion is specified.
- [AWS::Serverless::SimpleTable](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-specification-generated-resources-simpletable.html): This section lists the CloudFormation resources that AWS Serverless Application Model (AWS SAM) generates when AWS SAM AWS::Serverless::SimpleTable is specified.
- [AWS::Serverless::StateMachine](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-specification-generated-resources-statemachine.html): This section lists the CloudFormation resources that AWS Serverless Application Model (AWS SAM) generates when AWS SAM AWS::Serverless::StateMachine is specified.
- [Supported resource attributes](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-specification-resource-attributes.html): This section contains details about the resource attributes that are supported by AWS SAM resources.
- [API Gateway extensions](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-specification-api-gateway-extensions.html): This section contains details about API Gateway extensions supported by AWS SAM.
- [Intrinsic functions](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-specification-intrinsic-functions.html): This section contains information about intrinsic functions.


## [Example applications](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-example-applications.html)

- [Process DynamoDB events](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-example-ddb.html): This is an example application that's configured with DynamoDB as an event source, and a Lambda function that logs data that was passed in through the event message.
- [Process Amazon S3 events](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-example-s3.html): This is an example application that's configured with Amazon S3 as an event source, and a Lambda function that invokes APIs for Amazon S3, Amazon Rekognition, and DynamoDB.


## [Develop your application](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/chapter-create-application.html)

- [Create your application](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/using-sam-cli-init.html): Use the AWS SAMÂ CLI sam init command to initialize a new serverless application.

### [Define your infrastructure](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-authoring.html)

Using AWS SAM, configure your infrastructure and define the resources of your application primarily with the AWS SAM template.

- [Define application resources](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/authoring-define-resources.html): Define your application's resources in your AWS SAM template.

### [Set up access](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-permissions.html)

Set up and manage access and permissions of your resources in your AWS SAM template

### [AWS SAM connectors](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/managing-permissions-connectors.html)

Manage permissions between serverless application resources using AWS SAM connectors

- [Define permissions](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/connector-usage-define.html): In AWS SAM, Read and Write permissions can be provisioned within a single connector:
- [More ways to define resources](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/connector-usage-other-properties.html): For both source and destination resources, when defined within the same template, use the Id property.
- [Single source multiple connectors](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/connector-usage-single-source.html): Within a source resource, you can define multiple connectors, each with a different destination resource.
- [Multi-destination connectors](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/connector-usage-multi-destination.html): Within a source resource, you can define a single connector with multiple destination resources.
- [Resource attributes](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/connector-usage-resource-attributes.html): Resource attributes can be defined for resources to specify additional behaviors and relationships.

### [AWS SAMÂ policy templates](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-policy-templates.html)

This section contains the full list of supported policy templates.

- [Policy template list](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-policy-template-list.html): The following are the available policy templates, along with the permissions that are applied to each one.
- [CloudFormation](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-permissions-cloudformation.html): Use IAM to control who can access which AWS resources in your serverless application.

### [Control API access](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-controlling-access-to-apis.html)

To ensure your serverless application is secure, use the AWS SAM template to control access to API Gateway APIs.

- [Lambda authorizer examples](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-controlling-access-to-apis-lambda-authorizer.html): The AWS::Serverless::Api resource type supports two types of Lambda authorizers: TOKEN authorizers and REQUEST authorizers.
- [IAM permission example](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-controlling-access-to-apis-permissions.html): You can control access to your APIs by defining IAM permissions within your AWS SAM template.
- [Amazon Cognito user pool example](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-controlling-access-to-apis-cognito-user-pool.html): You can control access to your APIs by defining Amazon Cognito user pools within your AWS SAM template.
- [API key example](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-controlling-access-to-apis-keys.html): You can control access to your APIs by requiring API keys within your AWS SAM template.
- [Resource policy example](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-controlling-access-to-apis-resource-policies.html): You can control access to your APIs by attaching a resource policy within your AWS SAM template.
- [OAuth 2.0/JWT authorizer example](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-controlling-access-to-apis-oauth2-authorizer.html): You can control access to your APIs using JWTs as part of OpenID Connect (OIDC) and OAuth 2.0 frameworks.
- [Customized response example](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-controlling-access-to-apis-customize-response.html): You can customize some API Gateway error responses by defining response headers within your AWS SAM template.
- [Increase efficiency with layers](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-layers.html): Include layers in your serverless application, and learn how layers are downloaded and cached on your local host when running and debugging your serverless application locally.
- [Reuse code](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-template-nested-applications.html): Use nested applications to reuse common code, functionality, resources, and configurations in separate AWS SAM templates
- [Manage time-based events](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/using-eventbridge-scheduler.html): Schedule events in your AWS SAM templates using EventBridge Scheduler.
- [Orchestrating applications](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-step-functions-in-sam.html): Learn how to use AWS Step Functions with AWS SAM to orchestrate AWS Lambda functions and other AWS resources to form complex and robust workflows.
- [Set up code signing](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/authoring-codesigning.html): Use code signing with your AWS SAM application so that only trusted code is deployed.
- [Validate AWS SAM template files](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-using-validate.html): Use the content on this page to validate AWS SAM template files.

### [Build your application](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-building.html)

You can use AWS SAM to your build applications and customized versions of your applications, functions, layers, or custom runtimes.

- [Intro to sam build](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/using-sam-cli-build.html): Use the AWS SAMÂ CLI sam build command to prepare your serverless application for subsequent steps in your development workflow, such as local testing or deploying to the AWS Cloud.
- [Default build](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-using-build.html): Use the sam build command to build an AWS SAM serverless application as a .zip file archive or a container image.

### [Customize your build](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/building-lambda-functions.html)

Use the sam build command to customize your build for specific Lambda functions or layers.

- [Node.js functions with esbuild](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-using-build-typescript.html): Use the sam build command to build an AWS SAM serverless application that uses TypeScript as a .zip file archive or a container image.
- [Building .NET Native AOT functions](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/build-dotnet7.html): Building .NET applications with AWS SAM.
- [Rust functions with Cargo Lambda](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/building-rust.html): Use AWS SAM to build serverless applications containing Rust Lambda functions.
- [Python functions with uv](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/building-python-uv.html): Use AWS SAM to build serverless applications containing Python Lambda functions with uv as the package manager.
- [Functions with custom runtimes](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/building-custom-runtimes.html): Build custom runtimes required for your Lambda function.
- [Lambda layers](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/building-layers.html): Use the sam build command to build a custom layer.


## [Test your application](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-test-and-debug.html)

### [Intro to sam local](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/using-sam-cli-local.html)

Use the AWS SAMÂ CLI sam local command to test your serverless applications locally.

- [Intro to sam local generate-event](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/using-sam-cli-local-generate-event.html): Use the AWS SAMÂ CLI sam local generate-event subcommand to generate event payloads for supported AWS services.
- [Intro to sam local invoke](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/using-sam-cli-local-invoke.html): Use the AWS SAMÂ CLI sam local invoke subcommand to initiate a one-time invocation of an AWS Lambda function locally.
- [Intro to sam local start-api](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/using-sam-cli-local-start-api.html): Use the AWS SAMÂ CLIsam local start-api subcommand to run your Lambda functions locally and test through a local HTTP server host.
- [Intro to sam local start-lambda](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/using-sam-cli-local-start-lambda.html): Use the AWS SAMÂ CLI sam local start-api subcommand to run your Lambda functions locally and test through a local HTTP server host.
- [Locally invoke functions](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-using-invoke.html): Invoke a Lambda function locally using the sam local invoke AWS SAMÂ CLI command.
- [Locally run API Gateway](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-using-start-api.html): Start a local instance of API Gateway using the sam local start-api AWS SAM CLI command.
- [Test with sam remote test-event](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/using-sam-cli-remote-test-event.html): Use the AWS SAMÂ CLI sam remote test-event command to access and manage shareable test events for your Lambda functions.
- [Test with sam remote invoke](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/using-sam-cli-remote-invoke.html): Use the AWS SAMÂ CLI sam remote invoke command to interact with your Lambda functions in the AWS Cloud.
- [Automate integration tests](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-using-automated-tests.html): Test your code locally using automated integration testing.
- [Generate sample payloads](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-using-generate-event.html): Describes how to test your Lambda functions by generating sample payloads.
- [Test and debug durable functions](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/test-and-debug-durable-functions.html): Learn how to test and debug durable functions locally using AWS SAM CLI.


## [Debug your application](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/debug-application.html)

- [Locally debug functions](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-using-debugging.html): You can use AWS SAM with a variety of AWS toolkits and debuggers to test and debug your serverless applications locally.
- [Pass multiple runtime arguments](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-using-debugging-additional-arguments.html): You may choose to pass additional runtime arguments with AWS SAM to inspect issues and troubleshoot variables more effectively.
- [Validate with cfn-lint](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/validate-cfn-lint.html): Validate your AWS SAM applications with CloudFormation Linter


## [Deploy your application and resources](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-deploying.html)

- [Intro to sam deploy](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/using-sam-cli-deploy.html): Use the AWS SAMÂ CLI sam deploy command to deploy your serverless application to the AWS Cloud.
- [Deployment options](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/deploying-options.html): With AWS SAM, you deploy your serverless application manually and you can automate deployment when you use AWS SAM with a continuous integration and continuous deployment (CI/CD) system.

### [Deploy with CI/CD systems and pipelines](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/deploying-cicd-overview.html)

With AWS SAM, you can automate deployment when you use AWS SAM with a continuous integration and continuous deployment (CI/CD) system.

- [How AWS SAM uploads local files](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/deploy-upload-local-files.html): Use the AWS SAMÂ CLI to automatically upload local files at deployment.

### [Generate a starter pipeline](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-generating-example-ci-cd.html)

You can use AWS SAM to generate starter pipeline configuration for a number of popular CI/CD systems.

- [AWS CodePipeline](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-generating-example-ci-cd-codepipeline.html): You can use AWS SAM to generate starter pipeline configuration for AWS CodePipeline
- [Jenkins, GitLab CI/CD, GitHub Actions, Bitbucket Pipelines](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-generating-example-ci-cd-others.html): You can use AWS SAM to generate starter pipeline configuration for Jenkins, GitLab CI/CD, GitHub Actions, or Bitbucket Pipelines.
- [Customize starter pipelines](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-customizing-starter-pipelines.html): CI/CD administrators can customize starter pipeline templates that AWS SAM uses to create starter pipeline configurations for developers.

### [Automate your deployments](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-deploying-modify-pipeline.html)

You can automate the deployment of your application using pipelines, AWS SAM, and a CI/CD system.

- [AWS CodePipeline](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/deploying-using-codepipeline.html): Configure your CodePipeline to deploy AWS SAM applications.
- [Bitbucket Pipelines](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/deploying-using-bitbucket.html): Configure your Bitbucket Pipeline to deploy AWS SAM applications.
- [Jenkins](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/deploying-using-jenkins.html): Configure your Jenkins pipeline to deploy AWS SAM applications.
- [GitLab CI/CD](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/deploying-using-gitlab.html): Configure your GitLab CI/CD pipeline to deploy AWS SAM applications.
- [GitHub Actions](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/deploying-using-github.html): Configure your GitHub pipeline to deploy AWS SAM applications.
- [Use OIDC authentication](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/deploying-with-oidc.html): Use OpenID Connect (OIDC) with supported CI/CD platforms to set up user authentication with AWS SAM pipelines.
- [Intro to sam sync](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/using-sam-cli-sync.html): Use the AWS SAMÂ CLI sam sync command to sync local application changes to the AWS Cloud.


## [Monitor your application](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-monitoring.html)

- [Application Insights](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/monitor-app-insights.html): Monitor your AWS SAM serverless applications with CloudWatch Application Insights.
- [Working with logs](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-logging.html): Work with logs to simplify troubleshooting and keep records.


## [AWS SAM reference](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-reference.html)

### [AWS SAMÂ CLI commands](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-command-reference.html)

This section is the full AWS SAMÂ CLI command reference.

- [sam build](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-cli-command-reference-sam-build.html): Build an AWS SAM application using the sam build command from the AWS SAM CLI.
- [sam delete](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-cli-command-reference-sam-delete.html): To delete an AWS SAM application, use the sam delete command from the AWS SAM CLI.
- [sam deploy](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-cli-command-reference-sam-deploy.html): Options for the AWS SAMÂ CLI sam deploy command.
- [sam init](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-cli-command-reference-sam-init.html): This page provides reference information for the AWS Serverless Application Model Command Line Interface (AWS SAMÂ CLI) sam init command.

### [sam list](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-cli-command-reference-sam-list.html)

Reference documentation for the AWS SAMÂ CLI sam list command.

- [sam list endpoints](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-cli-command-reference-sam-list-endpoints.html): Reference documentation for the AWS SAMÂ CLI sam list endpoints subcommand.
- [sam list resources](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-cli-command-reference-sam-list-resources.html): Reference documentation for the AWS SAMÂ CLI sam list resources command.
- [sam list stack-outputs](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-cli-command-reference-sam-list-stack-outputs.html): Reference documentation for the AWS SAMÂ CLI sam list stack-outputs command.

### [sam local callback](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-cli-command-reference-sam-local-callback.html)

Reference documentation for the AWS SAMÂ CLI sam local callback command.

- [sam local callback succeed](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-cli-command-reference-sam-local-callback-succeed.html): Send a success callback to a durable function execution using the AWS Serverless Application Model Command Line Interface (AWS SAMÂ CLI).
- [sam local callback fail](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-cli-command-reference-sam-local-callback-fail.html): Send a failure callback to a durable function execution using the AWS Serverless Application Model Command Line Interface (AWS SAMÂ CLI).
- [sam local callback heartbeat](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-cli-command-reference-sam-local-callback-heartbeat.html): Send a heartbeat callback to a durable function execution using the AWS Serverless Application Model Command Line Interface (AWS SAMÂ CLI).

### [sam local execution](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-cli-command-reference-sam-local-execution.html)

Reference documentation for the AWS SAMÂ CLI sam local execution command.

- [sam local execution get](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-cli-command-reference-sam-local-execution-get.html): Get details of a durable function execution using the AWS Serverless Application Model Command Line Interface (AWS SAMÂ CLI).
- [sam local execution history](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-cli-command-reference-sam-local-execution-history.html): Get execution history of a durable function execution using the AWS Serverless Application Model Command Line Interface (AWS SAMÂ CLI).
- [sam local execution stop](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-cli-command-reference-sam-local-execution-stop.html): Stop a durable function execution using the AWS Serverless Application Model Command Line Interface (AWS SAMÂ CLI).
- [sam local generate-event](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-cli-command-reference-sam-local-generate-event.html): Options for the AWS Serverless Application Model Command Line Interface (AWS SAMÂ CLI) sam local generate-event subcommand.
- [sam local invoke](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-cli-command-reference-sam-local-invoke.html): Options for the AWS Serverless Application Model Command Line Interface (AWS SAMÂ CLI) sam local invoke subcommand.
- [sam local start-api](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-cli-command-reference-sam-local-start-api.html): Options for the AWS Serverless Application Model Command Line Interface (AWS SAMÂ CLI) sam local start-api subcommand.
- [sam local start-lambda](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-cli-command-reference-sam-local-start-lambda.html): Options for the AWS Serverless Application Model Command Line Interface (AWS SAMÂ CLI) sam local start-lambda subcommand.
- [sam logs](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-cli-command-reference-sam-logs.html): Fetches logs that are generated by your Lambda function.
- [sam package](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-cli-command-reference-sam-package.html): To package an AWS SAM application, use the sam package command from the AWS SAM CLI.
- [sam pipeline bootstrap](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-cli-command-reference-sam-pipeline-bootstrap.html): To set up infrastructure resources needed to deploying your AWS SAM application with a CI/CD system, use the sam pipeline bootstrap command from the AWS SAMÂ CLI.
- [sam pipeline init](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-cli-command-reference-sam-pipeline-init.html): To generate a pipeline configuration to deploy your AWS SAM application with a CI/CD system, use the sam pipeline init command from the AWS SAM CLI.
- [sam publish](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-cli-command-reference-sam-publish.html): Publish an AWS SAM application to the AWS Serverless Application Repository using the sam publish command from the AWS SAMÂ CLI.

### [sam remote callback](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-cli-command-reference-sam-remote-callback.html)

Reference documentation for the AWS SAMÂ CLI sam remote callback command.

- [sam remote callback succeed](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-cli-command-reference-sam-remote-callback-succeed.html): Send a callback success to a remote durable function execution using the AWS Serverless Application Model Command Line Interface (AWS SAMÂ CLI).
- [sam remote callback fail](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-cli-command-reference-sam-remote-callback-fail.html): Send a callback failure to a remote durable function execution using the AWS Serverless Application Model Command Line Interface (AWS SAMÂ CLI).
- [sam remote callback heartbeat](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-cli-command-reference-sam-remote-callback-heartbeat.html): Send a callback heartbeat to a remote durable function execution using the AWS Serverless Application Model Command Line Interface (AWS SAMÂ CLI).

### [sam remote execution](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-cli-command-reference-sam-remote-execution.html)

Reference documentation for the AWS SAMÂ CLI sam remote execution command.

- [sam remote execution get](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-cli-command-reference-sam-remote-execution-get.html): Get details of a durable execution using the AWS Serverless Application Model Command Line Interface (AWS SAMÂ CLI).
- [sam remote execution history](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-cli-command-reference-sam-remote-execution-history.html): Get execution history of a durable function execution using the AWS Serverless Application Model Command Line Interface (AWS SAMÂ CLI).
- [sam remote execution stop](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-cli-command-reference-sam-remote-execution-stop.html): Stop a durable function execution using the AWS Serverless Application Model Command Line Interface (AWS SAMÂ CLI).
- [sam remote invoke](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-cli-command-reference-remote-invoke.html): Options for the AWS SAMÂ CLI sam remote invoke command.

### [sam remote test-event](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-cli-command-reference-remote-test-event.html)

Reference information for the AWS SAM CLI sam remote test-event command.

- [sam remote test-event delete](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-cli-command-reference-remote-test-event-delete.html): Reference information for the AWS SAM CLI sam remote test-event delete subcommand.
- [sam remote test-event get](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-cli-command-reference-remote-test-event-get.html): Reference information for the AWS SAM CLI sam remote test-event get subcommand.
- [sam remote test-event list](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-cli-command-reference-remote-test-event-list.html): Reference information for the AWS SAM CLI sam remote test-event list subcommand.
- [sam remote test-event put](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-cli-command-reference-remote-test-event-put.html): Reference information for the AWS SAM CLI sam remote test-event put subcommand.
- [sam sync](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-cli-command-reference-sam-sync.html): To sync your local serverless application changes to the AWS Cloud, use the sam sync command from the AWS SAMÂ CLI.
- [sam traces](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-cli-command-reference-sam-traces.html): Use the sam traces command get AWS X-Ray tracing information about your serverless application.
- [sam validate](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-cli-command-reference-sam-validate.html): Verifies whether an AWS SAM template file is valid.

### [AWS SAMÂ CLI management](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/reference-sam-cli.html)

Reference information for the AWS SAMÂ CLI.

- [AWS SAMÂ CLI configuration file](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-config.html): Learn about the AWS SAMÂ CLI configuration file.
- [Managing AWS SAMÂ CLI versions](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/manage-sam-cli-versions.html): This section describes how to upgrade and uninstall the AWS SAMÂ CLI on macOS, Windows, and Linux.
- [Setting up AWS credentials](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-getting-started-set-up-credentials.html): Provides instructions for setting up AWS credentials.
- [AWS SAMÂ CLI telemetry](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-telemetry.html): Learn about using telemetry in the AWS SAMÂ CLI.
- [Troubleshooting](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-cli-troubleshooting.html): Get troubleshooting guidance for the AWS SAMÂ CLI.
- [Connector reference](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/reference-sam-connector.html): This reference provides important information regarding the AWS SAM connector resource type.
- [Installing Docker](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-docker.html): Instructions about installing Docker for use with the AWS SAMÂ CLI.
- [Installing Finch](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-finch.html): Instructions about installing Finch for use with the AWS SAMCLI.
- [Image repositories](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-image-repositories.html): Reference table of image repositories available for building.
- [Deploying gradually](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/automating-updates-to-serverless-apps.html): Use CodeDeploy to gradually deploy your AWS SAM applications.
- [Important notes](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/important-notes.html): This section includes important notes and known issues for AWS SAM.


## [Terraform support](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/terraform-support.html)

- [Getting started](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/gs-terraform-support.html): Get started with Terraform support for the AWS SAMÂ CLI.
- [Using AWS SAMÂ CLI with Terraform](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/using-samcli-terraform.html): Use the AWS SAMÂ CLI with Terraform to perform local debugging and testing on your Lambda functions.
- [Using AWS SAMÂ CLI with Serverless.tf](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/using-samcli-serverlesstf.html): Using the AWS SAMÂ CLI with Serverless.tf for local debugging and testing.

### [Terraform reference](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/terraform-reference.html)

This section provides reference information for using the AWS SAMÂ CLI with Terraform for local debugging and testing.

- [sam metadata](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/terraform-sam-metadata.html): Reference documentation on the sam metadata resource when using the AWS SAMÂ CLI with Terraform for local debugging and testing.


## [Publishing for others to use](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-template-publishing-applications.html)

- [Metadata section properties](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-template-publishing-applications-metadata-properties.html): Use a metadata key to specify application information that you want published to the AWS Serverless Application Repository.
