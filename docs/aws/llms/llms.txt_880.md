# Source: https://docs.aws.amazon.com/xray/latest/devguide/llms.txt

# AWS X-Ray Developer Guide

> Use AWS X-Ray to monitor the components and services that make up your cloud applications. AWS X-Ray provides a detailed trace map and latency information for each connection that your application makes to AWS services and external web APIs.

- [What is AWS X-Ray?](https://docs.aws.amazon.com/xray/latest/devguide/aws-xray.html)
- [Getting started](https://docs.aws.amazon.com/xray/latest/devguide/xray-gettingstarted.html)
- [Concepts](https://docs.aws.amazon.com/xray/latest/devguide/xray-concepts.html)
- [Instrumenting your application](https://docs.aws.amazon.com/xray/latest/devguide/xray-instrumenting-your-app.html)
- [Transaction Search](https://docs.aws.amazon.com/xray/latest/devguide/xray-transactionsearch.html)
- [OpenTelemetry Protocol (OTLP) Endpoint](https://docs.aws.amazon.com/xray/latest/devguide/xray-opentelemetry.html)
- [X-Ray SDK and Daemon Support timeline](https://docs.aws.amazon.com/xray/latest/devguide/xray-sdk-daemon-timeline.html)
- [Creating X-Ray resources with CloudFormation](https://docs.aws.amazon.com/xray/latest/devguide/creating-resources-with-cloudformation.html)
- [Tagging](https://docs.aws.amazon.com/xray/latest/devguide/xray-tagging.html)
- [Troubleshooting](https://docs.aws.amazon.com/xray/latest/devguide/xray-troubleshooting.html)
- [Document History](https://docs.aws.amazon.com/xray/latest/devguide/document-history.html)

## [Choosing an interface](https://docs.aws.amazon.com/xray/latest/devguide/aws-xray-interface.html)

- [Use an SDK](https://docs.aws.amazon.com/xray/latest/devguide/aws-xray-interface-sdk.html)

### [Use a console](https://docs.aws.amazon.com/xray/latest/devguide/aws-xray-interface-console.html)

Use a console if you want a graphical user interface (GUI) that requires minimal coding.

- [Trace map](https://docs.aws.amazon.com/xray/latest/devguide/xray-console-servicemap.html): View the X-Ray trace map to identify services where errors are occurring, connections with high latency, or traces for requests that were unsuccessful.
- [Traces](https://docs.aws.amazon.com/xray/latest/devguide/xray-console-traces.html): Learn how to view X-Ray traces and trace details in the X-Ray console.
- [Filter expressions](https://docs.aws.amazon.com/xray/latest/devguide/xray-console-filters.html): Use filter expressions to find traces that have performance issues or that relate to specific requests.
- [Cross-account tracing](https://docs.aws.amazon.com/xray/latest/devguide/xray-console-crossaccount.html): Configure and view cross-account tracing in AWS X-Ray.
- [Tracing event-driven applications](https://docs.aws.amazon.com/xray/latest/devguide/xray-tracelinking.html): AWS X-Ray supports tracing event-driven applications using Amazon SQS and AWS Lambda.
- [Histograms](https://docs.aws.amazon.com/xray/latest/devguide/xray-console-histograms.html): Use the trace map in the X-Ray console to view histograms showing an edge for a metric, and zoom in to see individual traces for a specific time period.
- [Insights](https://docs.aws.amazon.com/xray/latest/devguide/xray-console-insights.html): Use AWS X-Ray to identify emergent issues in your applications as they happen.
- [Analytics](https://docs.aws.amazon.com/xray/latest/devguide/xray-console-analytics.html): Use the AWS X-Ray Analytics console to understand and debug request-serving applications.
- [Groups](https://docs.aws.amazon.com/xray/latest/devguide/xray-console-groups.html): Configure and manage groups in AWS X-Ray.
- [Sampling](https://docs.aws.amazon.com/xray/latest/devguide/xray-console-sampling.html): Configure AWS X-Ray to manage sampling rules.
- [Adaptive sampling](https://docs.aws.amazon.com/xray/latest/devguide/xray-adaptive-sampling.html): Configure AWS X-Ray to manage adaptive sampling rules.
- [Console deep linking](https://docs.aws.amazon.com/xray/latest/devguide/xray-console-deeplinks.html): Create deep links to filtered trace maps and trace lists in the AWS X-Ray console.

### [Use the X-Ray API](https://docs.aws.amazon.com/xray/latest/devguide/xray-api.html)

If the X-Ray SDK doesnât support your programming language, you can use either the X-Ray APIs directly or the AWS Command Line Interface (AWS CLI) to call X-Ray API commands.

- [Tutorial](https://docs.aws.amazon.com/xray/latest/devguide/xray-api-tutorial.html): The AWS CLI lets your access the X-Ray service directly and use the same APIs that the X-Ray console uses to retrieve the service graph and raw traces data.
- [Sending data](https://docs.aws.amazon.com/xray/latest/devguide/xray-api-sendingdata.html): Upload trace data with the AWS X-Ray API.
- [Getting data](https://docs.aws.amazon.com/xray/latest/devguide/xray-api-gettingdata.html): Retrieve service graphs and traces with the AWS X-Ray API.
- [Configuration](https://docs.aws.amazon.com/xray/latest/devguide/xray-api-configuration.html): Configure sampling and encryption settings with the AWS X-Ray API.
- [Sampling](https://docs.aws.amazon.com/xray/latest/devguide/xray-api-sampling.html): Use sampling rules with the AWS X-Ray API.
- [Segment documents](https://docs.aws.amazon.com/xray/latest/devguide/xray-api-segmentdocuments.html): Generate segment documents to send tracing information directly to X-Ray without using an SDK.


## [Security](https://docs.aws.amazon.com/xray/latest/devguide/security.html)

- [Data protection](https://docs.aws.amazon.com/xray/latest/devguide/xray-console-encryption.html): Configure X-Ray to use a AWS KMS key for encryption.

### [Identity and access management](https://docs.aws.amazon.com/xray/latest/devguide/security-iam.html)

How to authenticate requests and manage access your X-Ray resources.

- [How AWS X-Ray works with IAM](https://docs.aws.amazon.com/xray/latest/devguide/security_iam_service-with-iam.html): Before you use IAM to manage access to X-Ray, you should understand what IAM features are available to use with X-Ray.
- [Identity-based policy examples](https://docs.aws.amazon.com/xray/latest/devguide/security_iam_id-based-policy-examples.html): By default, users and roles don't have permission to create or modify X-Ray resources.
- [Troubleshooting](https://docs.aws.amazon.com/xray/latest/devguide/security_iam_troubleshoot.html): Use the following information to help you diagnose and fix common issues that you might encounter when working with X-Ray and IAM.
- [Logging and monitoring](https://docs.aws.amazon.com/xray/latest/devguide/security-logging-monitoring.html): Learn about logging and monitoring in AWS X-Ray.
- [Compliance validation](https://docs.aws.amazon.com/xray/latest/devguide/compliance-validation.html): Learn what AWS services are in scope of a specific compliance program.
- [Resilience](https://docs.aws.amazon.com/xray/latest/devguide/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and learn about specific AWS X-Ray features for data resiliency.
- [Infrastructure security](https://docs.aws.amazon.com/xray/latest/devguide/infrastructure-security.html): Learn how AWS X-Ray isolates service traffic.
- [VPC endpoints](https://docs.aws.amazon.com/xray/latest/devguide/xray-security-vpc-endpoint.html): Explains how to use AWS X-Ray with VPC endpoints.
- [Cross-service confused deputy prevention](https://docs.aws.amazon.com/xray/latest/devguide/cross-service-confused-deputy-prevention.html): The confused deputy problem is a security issue where an entity that doesn't have permission to perform an action can coerce a more-privileged entity to perform the action.


## [Sample application](https://docs.aws.amazon.com/xray/latest/devguide/xray-scorekeep.html)

- [Scorekeep tutorial](https://docs.aws.amazon.com/xray/latest/devguide/scorekeep-tutorial.html): Learn how to use AWS X-Ray by launching a sample Java application.
- [AWS SDK clients](https://docs.aws.amazon.com/xray/latest/devguide/scorekeep-sdkclients.html)
- [Custom subsegments](https://docs.aws.amazon.com/xray/latest/devguide/scorekeep-subsegments.html)
- [Annotations and metadata](https://docs.aws.amazon.com/xray/latest/devguide/scorekeep-annotations.html)
- [HTTP clients](https://docs.aws.amazon.com/xray/latest/devguide/scorekeep-httpclient.html)
- [SQL clients](https://docs.aws.amazon.com/xray/latest/devguide/scorekeep-postgresql.html)
- [AWS Lambda functions](https://docs.aws.amazon.com/xray/latest/devguide/scorekeep-lambda.html)
- [Instrumenting startup code](https://docs.aws.amazon.com/xray/latest/devguide/scorekeep-startup.html)
- [Instrumenting scripts](https://docs.aws.amazon.com/xray/latest/devguide/scorekeep-scripts.html)
- [Instrumenting web clients](https://docs.aws.amazon.com/xray/latest/devguide/scorekeep-client.html)
- [Worker threads](https://docs.aws.amazon.com/xray/latest/devguide/scorekeep-workerthreads.html)


## [X-Ray daemon](https://docs.aws.amazon.com/xray/latest/devguide/xray-daemon.html)

- [Configuration](https://docs.aws.amazon.com/xray/latest/devguide/xray-daemon-configuration.html): Use command line options or a configuration file to configure the X-Ray daemon.
- [Run the daemon locally](https://docs.aws.amazon.com/xray/latest/devguide/xray-daemon-local.html): Run the X-Ray daemon locally on Linux, MacOS, Windows, or in a Docker container.
- [On Elastic Beanstalk](https://docs.aws.amazon.com/xray/latest/devguide/xray-daemon-beanstalk.html): Use a configuration file to run the X-Ray daemon on your Elastic Beanstalk environment's Amazon EC2 instances.
- [On Amazon EC2](https://docs.aws.amazon.com/xray/latest/devguide/xray-daemon-ec2.html): Use a user data script to run the X-Ray Daemon on your Amazon EC2 instances.
- [On Amazon ECS](https://docs.aws.amazon.com/xray/latest/devguide/xray-daemon-ecs.html): Use a Docker image to run the X-Ray daemon on your Amazon ECS clusters.


## [Integrating with AWS services](https://docs.aws.amazon.com/xray/latest/devguide/xray-services.html)

- [Amazon Bedrock AgentCore](https://docs.aws.amazon.com/xray/latest/devguide/xray-services-agentcore.html): Use AWS X-Ray to view end-to-end requests when using Amazon Bedrock AgentCore events.
- [Amazon EC2](https://docs.aws.amazon.com/xray/latest/devguide/xray-services-ec2.html): Use an Amazon EC2 user data script to run the AWS X-Ray daemon on your application instances.
- [Amazon SNS](https://docs.aws.amazon.com/xray/latest/devguide/xray-services-sns.html): Use AWS X-Ray to trace messages sent they travel through your Amazon SNS topics.
- [Amazon SQS](https://docs.aws.amazon.com/xray/latest/devguide/xray-services-sqs.html): Enable AWS X-Ray to trace messages passed through Amazon SQS batches.
- [Amazon S3](https://docs.aws.amazon.com/xray/latest/devguide/xray-services-s3.html): Use AWS X-Ray to view end-to-end requests when using Amazon S3 events.
- [AWS Distro for OpenTelemetry](https://docs.aws.amazon.com/xray/latest/devguide/xray-services-adot.html): Collect metrics and traces using the AWS Distro for OpenTelemetry to send to X-Ray and other monitoring solutions.
- [AWS Config](https://docs.aws.amazon.com/xray/latest/devguide/xray-api-config.html): Integrate with AWS Config to record configuration changes made to the X-Ray encryption resource.
- [AWS AppSync](https://docs.aws.amazon.com/xray/latest/devguide/xray-services-appsync.html): Enable active tracing and sampling for AWS AppSync requests.
- [API Gateway](https://docs.aws.amazon.com/xray/latest/devguide/xray-services-apigateway.html): Use Amazon API Gateway to sample and record incoming requests.
- [App Mesh](https://docs.aws.amazon.com/xray/latest/devguide/xray-services-appmesh.html): Use an Amazon EC2 user data script to run the AWS X-Ray daemon on your application instances.
- [App Runner](https://docs.aws.amazon.com/xray/latest/devguide/xray-services-app-runner.html): Enable tracing for containerized applications with App Runner and X-Ray.
- [CloudTrail](https://docs.aws.amazon.com/xray/latest/devguide/xray-api-cloudtrail.html): Learn about logging AWS X-Ray with AWS CloudTrail.

### [CloudWatch](https://docs.aws.amazon.com/xray/latest/devguide/xray-services-cloudwatch.html)

Integrate Amazon CloudWatch with X-Ray

- [CloudWatch RUM](https://docs.aws.amazon.com/xray/latest/devguide/xray-services-RUM.html): Use CloudWatch RUM to trace user sessions with AWS X-Ray.
- [CloudWatch Synthetics](https://docs.aws.amazon.com/xray/latest/devguide/xray-services-cloudwatch-synthetics.html): Debug and triage Amazon CloudWatch Synthetics canaries using AWS X-Ray
- [Elastic Beanstalk](https://docs.aws.amazon.com/xray/latest/devguide/xray-services-beanstalk.html): Use AWS Elastic Beanstalk to run the AWS X-Ray daemon on your application instances.
- [Elastic Load Balancing](https://docs.aws.amazon.com/xray/latest/devguide/xray-services-elb.html): Use Elastic Load Balancing to tag incoming requests for use with AWS X-Ray.
- [EventBridge](https://docs.aws.amazon.com/xray/latest/devguide/xray-services-eventbridge.html): Enable AWS X-Ray to trace events passed through EventBridge.
- [Lambda](https://docs.aws.amazon.com/xray/latest/devguide/xray-services-lambda.html): Use X-Ray to trace AWS Lambda functions.
- [Step Functions](https://docs.aws.amazon.com/xray/latest/devguide/xray-services-stepfunctions.html): Use AWS X-Ray to trace and analyze requests for Step Functions.


## [Working with Go](https://docs.aws.amazon.com/xray/latest/devguide/xray-go.html)

- [AWS Distro for OpenTelemetry Go](https://docs.aws.amazon.com/xray/latest/devguide/xray-go-opentel-sdk.html): Use the AWS Distro for OpenTelemetry to instrument Go applications.

### [X-Ray SDK for Go](https://docs.aws.amazon.com/xray/latest/devguide/xray-sdk-go.html)

Use the X-Ray SDK for Go to instrument Go applications.

- [Configuration](https://docs.aws.amazon.com/xray/latest/devguide/xray-sdk-go-configuration.html): Configure the X-Ray SDK for Go module with service plugins, sampling rules, and log settings.
- [Incoming requests](https://docs.aws.amazon.com/xray/latest/devguide/xray-sdk-go-handler.html): Use xray.Handler in your application with the X-Ray SDK for Go to trace incoming requests.
- [AWS SDK clients](https://docs.aws.amazon.com/xray/latest/devguide/xray-sdk-go-awssdkclients.html): Instrument AWS SDK clients with the X-Ray SDK for Go to trace downstream calls to AWS services and resources.
- [Outgoing HTTP calls](https://docs.aws.amazon.com/xray/latest/devguide/xray-sdk-go-httpclients.html): Instrument HTTP clients with the X-Ray SDK for Go to trace calls to downstream web APIs.
- [SQL queries](https://docs.aws.amazon.com/xray/latest/devguide/xray-sdk-go-sqlclients.html): Instrument PostgreSQL and MySQL database connections with the X-Ray SDK for Go to trace SQL queries.
- [Custom subsegments](https://docs.aws.amazon.com/xray/latest/devguide/xray-sdk-go-subsegments.html): Create additional subsegments with the X-Ray SDK for Go to trace functions or sections of code.
- [Annotations and metadata](https://docs.aws.amazon.com/xray/latest/devguide/xray-sdk-go-segment.html): Add annotations and metadata to segments that the X-Ray SDK for Go records for your application.


## [Working with Java](https://docs.aws.amazon.com/xray/latest/devguide/xray-java.html)

- [AWS Distro for OpenTelemetry Java](https://docs.aws.amazon.com/xray/latest/devguide/xray-java-opentel-sdk.html): Use the AWS Distro for OpenTelemetry to instrument Java applications.

### [X-Ray SDK for Java](https://docs.aws.amazon.com/xray/latest/devguide/xray-sdk-java.html)

Use the X-Ray SDK for Java to instrument Java applications.

- [Auto-instrumentation agent](https://docs.aws.amazon.com/xray/latest/devguide/aws-x-ray-auto-instrumentation-agent-for-java.html): Use the AWS X-Ray auto-instrumentation agent for Java.
- [Configuration](https://docs.aws.amazon.com/xray/latest/devguide/xray-sdk-java-configuration.html): Configure the X-Ray SDK for Java module with service plugins, sampling rules, and log settings.
- [Incoming requests](https://docs.aws.amazon.com/xray/latest/devguide/xray-sdk-java-filters.html): Add a filter to your application with the X-Ray SDK for Java to trace incoming requests.
- [AWS SDK clients](https://docs.aws.amazon.com/xray/latest/devguide/xray-sdk-java-awssdkclients.html): Instrument AWS SDK for Java clients with the X-Ray SDK for Java to trace downstream calls to AWS services and resources.
- [Outgoing HTTP calls](https://docs.aws.amazon.com/xray/latest/devguide/xray-sdk-java-httpclients.html): Instrument HTTP clients with the X-Ray SDK for Java to trace calls to downstream web APIs.
- [SQL queries](https://docs.aws.amazon.com/xray/latest/devguide/xray-sdk-java-sqlclients.html): Instrument PostgreSQL and MySQL database connections with the X-Ray SDK for Java to trace SQL queries.
- [Custom subsegments](https://docs.aws.amazon.com/xray/latest/devguide/xray-sdk-java-subsegments.html): Create additional subsegments with the X-Ray SDK for Java to trace functions or sections of code.
- [Annotations and metadata](https://docs.aws.amazon.com/xray/latest/devguide/xray-sdk-java-segment.html): Add annotations and metadata to segments that the X-Ray SDK for Java records for your application.
- [Multithreading](https://docs.aws.amazon.com/xray/latest/devguide/xray-sdk-java-multithreading.html): Considerations for instrumenting multithreaded applications with AWS X-Ray.
- [AOP with Spring](https://docs.aws.amazon.com/xray/latest/devguide/xray-sdk-java-aop-spring.html): Instrument your application with AOP in Spring and the X-Ray SDK for Java.


## [Working with Node.js](https://docs.aws.amazon.com/xray/latest/devguide/xray-nodejs.html)

- [AWS Distro for OpenTelemetry JavaScript](https://docs.aws.amazon.com/xray/latest/devguide/xray-js-opentel-sdk.html): Use the AWS Distro for OpenTelemetry to instrument JavaScript applications.

### [X-Ray SDK for Node.js](https://docs.aws.amazon.com/xray/latest/devguide/xray-sdk-nodejs.html)

Instrument your Node.js application with the X-Ray SDK for Node.js to trace incoming requests and the downstream calls that your application makes in response.

- [Configuration](https://docs.aws.amazon.com/xray/latest/devguide/xray-sdk-nodejs-configuration.html): Configure the X-Ray SDK for Node.js module with service plugins and sampling rules.
- [Incoming requests](https://docs.aws.amazon.com/xray/latest/devguide/xray-sdk-nodejs-middleware.html): Add middleware to your application with the X-Ray SDK for Node.js to trace incoming requests.
- [AWS SDK clients](https://docs.aws.amazon.com/xray/latest/devguide/xray-sdk-nodejs-awssdkclients.html): Instrument AWS SDK for JavaScript in Node.js clients with the X-Ray SDK for Node.js to trace downstream calls to AWS services and resources.
- [Outgoing HTTP calls](https://docs.aws.amazon.com/xray/latest/devguide/xray-sdk-nodejs-httpclients.html): Instrument HTTP clients with the X-Ray SDK for Node.js to trace calls to downstream web APIs.
- [SQL queries](https://docs.aws.amazon.com/xray/latest/devguide/xray-sdk-nodejs-sqlclients.html): Instrument PostgreSQL and MySQL database connections with the X-Ray SDK for Node.js to trace SQL queries.
- [Custom subsegments](https://docs.aws.amazon.com/xray/latest/devguide/xray-sdk-nodejs-subsegments.html): Create additional subsegments with the X-Ray SDK for Node.js to trace functions or sections of code.
- [Annotations and metadata](https://docs.aws.amazon.com/xray/latest/devguide/xray-sdk-nodejs-segment.html): Add annotations and metadata to segments that the X-Ray SDK for Node.js records for your application.


## [Working with Python](https://docs.aws.amazon.com/xray/latest/devguide/xray-python.html)

- [AWS Distro for OpenTelemetry Python](https://docs.aws.amazon.com/xray/latest/devguide/xray-python-opentel-sdk.html): Use the AWS Distro for OpenTelemetry to instrument Python applications.

### [X-Ray SDK for Python](https://docs.aws.amazon.com/xray/latest/devguide/xray-sdk-python.html)

Use the X-Ray SDK for Python to instrument Python applications.

- [Configuration](https://docs.aws.amazon.com/xray/latest/devguide/xray-sdk-python-configuration.html): Configure the X-Ray SDK for Python module with service plugins, sampling rules, and log settings.
- [Incoming requests](https://docs.aws.amazon.com/xray/latest/devguide/xray-sdk-python-middleware.html): Add a filter to your application with the X-Ray SDK for Python to trace incoming requests.
- [Patching libraries](https://docs.aws.amazon.com/xray/latest/devguide/xray-sdk-python-patching.html): Instrument libraries with the X-Ray SDK for Python to trace downstream calls to AWS services, SQL databases, and other APIs.
- [AWS SDK clients](https://docs.aws.amazon.com/xray/latest/devguide/xray-sdk-python-awssdkclients.html): Instrument AWS SDK for Java clients with the X-Ray SDK for Python to trace downstream calls to AWS services and resources.
- [Outgoing HTTP calls](https://docs.aws.amazon.com/xray/latest/devguide/xray-sdk-python-httpclients.html): Instrument HTTP clients with the X-Ray SDK for Python to trace calls to downstream web APIs.
- [Custom subsegments](https://docs.aws.amazon.com/xray/latest/devguide/xray-sdk-python-subsegments.html): Create additional subsegments with the X-Ray SDK for Python to trace functions or sections of code.
- [Annotations and metadata](https://docs.aws.amazon.com/xray/latest/devguide/xray-sdk-python-segment.html): Add annotations and metadata to segments that the X-Ray SDK for Python records for your application.
- [Instrument serverless applications](https://docs.aws.amazon.com/xray/latest/devguide/xray-sdk-python-serverless.html): AWS X-Ray SDK for Python supports instrumenting web frameworks deployed in serverless applications.


## [Working with .NET](https://docs.aws.amazon.com/xray/latest/devguide/xray-dotnet.html)

- [AWS Distro for OpenTelemetry .NET](https://docs.aws.amazon.com/xray/latest/devguide/xray-dotnet-opentel-sdk.html): Use the AWS Distro for OpenTelemetry to instrument .NET applications.

### [X-Ray SDK for .NET](https://docs.aws.amazon.com/xray/latest/devguide/xray-sdk-dotnet.html)

Use the X-Ray SDK for .NET to instrument your application code and send trace data to AWS X-Ray.

- [Configuration](https://docs.aws.amazon.com/xray/latest/devguide/xray-sdk-dotnet-configuration.html): Configure the X-Ray SDK for .NET module with service plugins and sampling rules.
- [Incoming requests](https://docs.aws.amazon.com/xray/latest/devguide/xray-sdk-dotnet-messagehandler.html): Add a message handler to your application with the X-Ray SDK for .NET to trace incoming requests.
- [AWS SDK clients](https://docs.aws.amazon.com/xray/latest/devguide/xray-sdk-dotnet-sdkclients.html): Instrument AWS SDK for .NET clients with the X-Ray SDK for .NET to trace downstream calls to AWS services and resources.
- [Outgoing HTTP calls](https://docs.aws.amazon.com/xray/latest/devguide/xray-sdk-dotnet-httpclients.html): Instrument HTTP clients with the X-Ray SDK for .NET to trace calls to downstream web APIs.
- [SQL queries](https://docs.aws.amazon.com/xray/latest/devguide/xray-sdk-dotnet-sqlqueries.html): Instrument database connections with the X-Ray SDK for .NET to trace SQL queries.
- [Custom subsegments](https://docs.aws.amazon.com/xray/latest/devguide/xray-sdk-dotnet-subsegments.html): Create additional subsegments with the X-Ray SDK for .NET to trace functions or sections of code.
- [Annotations and metadata](https://docs.aws.amazon.com/xray/latest/devguide/xray-sdk-dotnet-segment.html): Add annotations and metadata to segments that the X-Ray SDK for .NET records for your application.


## [Working with Ruby](https://docs.aws.amazon.com/xray/latest/devguide/xray-ruby.html)

- [AWS Distro for OpenTelemetry Ruby](https://docs.aws.amazon.com/xray/latest/devguide/xray-ruby-opentel-sdk.html): Use the AWS Distro for OpenTelemetry to instrument Ruby applications.

### [X-Ray SDK for Ruby](https://docs.aws.amazon.com/xray/latest/devguide/xray-sdk-ruby.html)

Use the X-Ray SDK to instrument Ruby applications.

- [Configuration](https://docs.aws.amazon.com/xray/latest/devguide/xray-sdk-ruby-configuration.html): Configure the X-Ray SDK for Ruby module with service plugins, sampling rules, and log settings.
- [Incoming requests](https://docs.aws.amazon.com/xray/latest/devguide/xray-sdk-ruby-middleware.html): Add a filter to your application with the X-Ray SDK for Ruby to trace incoming requests.
- [Patching libraries](https://docs.aws.amazon.com/xray/latest/devguide/xray-sdk-ruby-patching.html): Instrument libraries with the X-Ray SDK for Ruby to trace downstream calls to AWS services, SQL databases, and other APIs.
- [AWS SDK clients](https://docs.aws.amazon.com/xray/latest/devguide/xray-sdk-ruby-awssdkclients.html): Instrument AWS SDK for Java clients with the X-Ray SDK for Ruby to trace downstream calls to AWS services and resources.
- [Custom subsegments](https://docs.aws.amazon.com/xray/latest/devguide/xray-sdk-ruby-subsegments.html): Create additional subsegments with the X-Ray SDK to trace functions or sections of code.
- [Annotations and metadata](https://docs.aws.amazon.com/xray/latest/devguide/xray-sdk-ruby-segment.html): Add annotations and metadata to segments that the X-Ray SDK for Ruby records for your application.


## [Migrating from X-Ray instrumentation to OpenTelemetry instrumentation](https://docs.aws.amazon.com/xray/latest/devguide/xray-sdk-migration.html)

- [Migrating to OpenTelemetry Java](https://docs.aws.amazon.com/xray/latest/devguide/xray-migration-opentelemetry.html): This section provides guidance on migrating from the X-Ray SDK to the OpenTelemetry SDK for Java applications.
- [Migrate to OpenTelemetry Go](https://docs.aws.amazon.com/xray/latest/devguide/manual-instrumentation-go.html): Learn how to manually instrument your Go applications using the OpenTelemetry SDK as a replacement for X-Ray SDK instrumentation.
- [Migrate to OpenTelemetry Node.js](https://docs.aws.amazon.com/xray/latest/devguide/migrate-xray-to-opentelemetry-nodejs.html): This section explains how to migrate your Node.js applications from X-Ray SDK to OpenTelemetry.
- [Migrate to OpenTelemetry .NET](https://docs.aws.amazon.com/xray/latest/devguide/introduction-dotnet.html): This section provides guidance on migrating from X-Ray SDK to OpenTelemetry for .NET applications, including both zero-code automatic instrumentation and manual instrumentation approaches.
- [Migrate to OpenTelemetry Python](https://docs.aws.amazon.com/xray/latest/devguide/migrate-xray-to-opentelemetry-python.html): This chapter provides guidance on migrating from X-Ray SDK to OpenTelemetry for Python applications, including both zero-code automatic instrumentation and manual instrumentation approaches.
- [Migrate to OpenTelemetry Ruby](https://docs.aws.amazon.com/xray/latest/devguide/migrate-xray-to-opentelemetry-ruby.html): This section provides guidance on migrating from X-Ray SDK to OpenTelemetry for Ruby applications, focusing on the manual instrumentation approach.
