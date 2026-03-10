# Source: https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/llms.txt

# AWS SDK for JavaScript Developer Guide for SDK v2

> Guide to help developers use AWS services with browser scripts and Node.js.

- [What Is the AWS SDK for JavaScript?](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/welcome.html)
- [API Reference and Changelog](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/aws-jsdk-reference.html)
- [Migrate to v3](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/migrate.html)
- [Additional Resources](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/resources.html)
- [Document History](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/doc-history.html)

## [Getting Started](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/getting-started.html)

- [Getting Started in a Browser Script](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/getting-started-browser.html): Create a simple browser-based app with the SDK for JavaScript.
- [Getting Started in Node.js](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/getting-started-nodejs.html): Create a simple Node.js app with the SDK for JavaScript.


## [Setting Up the SDK for JavaScript](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/setting-up.html)

### [Prerequisites](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/jssdk-prerequisites.html)

Before you use the AWS SDK for JavaScript, determine whether your code needs to run in Node.js or web browsers.

- [Setting Up an AWS Node.js Environment](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/setting-up-node.html): To set up an AWS Node.js environment in which you can run your application, use any of the following methods:
- [Web Browsers Supported](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/browsers-supported.html): The SDK for JavaScript supports all modern web browsers, including these minimum versions:
- [Installing the SDK](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/installing-jssdk.html): Learn about installing AWS SDK for JavaScript, a JavaScript API for Amazon Web Services, in both web browsers and in Node.js.
- [Loading the SDK](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/loading-the-jssdk.html): How you load the SDK for JavaScript depends on whether you are loading it to run in a web browser or in Node.js.
- [Upgrading From Version 1](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/upgrading-from-v1.html): Upgrade the SDK for JavaScript from version 1 to version 2.


## [Configuring the SDK for JavaScript](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/configuring-the-jssdk.html)

- [Using the Global Configuration Object](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/global-config-object.html): There are two ways to configure the SDK:
- [Setting the AWS Region](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/setting-region.html): A Region is a named set of AWS resources in the same geographical area.
- [Specifying Custom Endpoints](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/specifying-endpoints.html): Calls to API methods in the SDK for JavaScript are made to service endpoint URIs.
- [SDK authentication with AWS](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/getting-your-credentials.html): You must establish how your code authenticates with AWS when developing with AWS services.

### [Setting Credentials](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/setting-credentials.html)

AWS uses credentials to identify who is calling services and whether access to the requested resources is allowed.

### [Setting Credentials in Node.js](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/setting-credentials-node.html)

There are several ways in Node.js to supply your credentials to the SDK.

- [Credentials for Amazon EC2 from IAM Roles](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/loading-node-credentials-iam.html): If you run your Node.js application on an Amazon EC2 instance, you can leverage IAM roles for Amazon EC2 to automatically provide credentials to the instance.
- [Credentials for a Node.js Lambda Function](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/loading-node-credentials-lambda.html): When you create an AWS Lambda function, you must create a special IAM role that has permission to execute the function.
- [Credentials from the Shared Credentials File](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/loading-node-credentials-shared.html): You can keep your AWS credentials data in a shared file used by SDKs and the command line interface.
- [Credentials from Environment Variables](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/loading-node-credentials-environment.html): The SDK automatically detects AWS credentials set as variables in your environment and uses them for SDK requests, eliminating the need to manage credentials in your application.
- [Credentials from JSON File](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/loading-node-credentials-json-file.html): You can load configuration and credentials from a JSON document on disk using AWS.config.loadFromPath.
- [Credentials using a Configured Credential Process](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/loading-node-credentials-configured-credential-process.html): You can source credentials by using a method that isn't built into the SDK.

### [Setting Credentials in a Web Browser](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/setting-credentials-browser.html)

There are several ways to supply your credentials to the SDK from browser scripts.

- [Using Amazon Cognito Identity](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/loading-browser-credentials-cognito.html): The recommended way to obtain AWS credentials for your browser scripts is to use the Amazon Cognito Identity credentials object, AWS.CognitoIdentityCredentials.
- [Using Web Federated Identity](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/loading-browser-credentials-federated-id.html): You can directly configure individual identity providers to access AWS resources using web identity federation.
- [Web Federated Identity Examples](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/config-web-identity-examples.html): Here are a few examples of using web federated identity to obtain credentials in browser JavaScript.
- [Locking API Versions](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/locking-api-versions.html): Specify an API version to lock the version that you use in your application.

### [Node.js Considerations](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/node-js-considerations.html)

Configure the SDK for JavaScript for Node.js.

- [Configuring maxSockets in Node.js](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/node-configuring-maxsockets.html): Configure maxSockets in Node.js.
- [Reusing Connections with Keep-Alive in Node.js](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/node-reusing-connections.html): By default, the default Node.js HTTP/HTTPS agent creates a new TCP connection for every new request.
- [Configuring Proxies for Node.js](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/node-configuring-proxies.html): Install and use a third-party HTTP agent proxy.
- [Registering Certificate Bundles in Node.js](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/node-registering-certs.html): Include a specified set of certificates in your Node.js application.

### [Browser Script Considerations](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/browser-js-considerations.html)

Build and configure the SDK for JavaScript for browsers, using the SDK builder, the CLI, or browserify.

- [Building the SDK for Browsers](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/building-sdk-for-browsers.html): Links to additional information of use to users of the SDK for JavaScript.
- [Cross-Origin Resource Sharing (CORS)](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/cors.html): CORS considerations for users of the SDK for JavaScript.
- [Bundling with Webpack](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/webpack.html): Bundle web applications using webpack with the SDK for JavaScript.


## [Working with Services](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/working-with-services.html)

- [Creating and Calling Service Objects](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/creating-and-calling-service-objects.html): Create and call service objects using the SDK for JavaScript.
- [Logging AWS SDK for JavaScript Calls](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/logging-sdk-calls.html): The AWS SDK for JavaScript is instrumented with a built-in logger so you can log API calls you make with the SDK for JavaScript.

### [Calling Services Asychronously](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/calling-services-asynchronously.html)

All requests made through the SDK are asynchronous.

- [Managing Asychronous Calls](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/making-asynchronous-calls.html): For example, the home page of an e-commerce website lets returning customers sign in.
- [Using a Callback Function](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/using-a-callback-function.html): Use a callback function for asynchronous calls with the SDK for JavaScript.
- [Using a Request Object Event Listener](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/using-a-response-event-handler.html): Use a request object event listener for asynchronous calls with the SDK for JavaScript.
- [Using async/await](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/using-async-await.html): You can use the async/await pattern in your calls to the AWS SDK for JavaScript.
- [Using Promises](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/using-promises.html): Use JavaScript promises for asynchronous calls with the SDK for JavaScript.
- [Using the Response Object](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/the-response-object.html): Use the Response object to access the content of a response in the SDK for JavaScript.
- [Working with JSON](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/working-with-json.html): Work with JSON in the SDK for JavaScript.
- [Retries](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/retry-strategy.html): Describes the retry strategy of the SDK for JavaScript v2.


## [SDK for JavaScript Code Examples](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/sdk-code-samples.html)

### [Amazon CloudWatch Examples](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/cloudwatch-examples.html)

Examples that show how to use the CloudWatch client class.

- [Creating Alarms in Amazon CloudWatch](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/cloudwatch-examples-creating-alarms.html): JavaScript code example that applies to Node.js execution
- [Using Alarm Actions in Amazon CloudWatch](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/cloudwatch-examples-using-alarm-actions.html): JavaScript code example that applies to Node.js execution
- [Getting Metrics from Amazon CloudWatch](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/cloudwatch-examples-getting-metrics.html): JavaScript code example that applies to Node.js execution
- [Sending Events to Amazon CloudWatch Events](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/cloudwatch-examples-sending-events.html): JavaScript code example that applies to Node.js execution
- [Using Subscription Filters in Amazon CloudWatch Logs](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/cloudwatch-examples-subscriptions.html): JavaScript code example that applies to Node.js execution

### [Amazon DynamoDB Examples](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/dynamodb-examples.html)

Examples that show how to use the DynamoDB client classes.

- [Creating and Using Tables in DynamoDB](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/dynamodb-examples-using-tables.html): Example that shows how to create a table in DynamoDB using the service object.
- [Reading and Writing A Single Item in DynamoDB](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/dynamodb-example-table-read-write.html): Example that shows how to read and write a single item using the DynamoDB service object.
- [Reading and Writing Items in Batch in DynamoDB](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/dynamodb-example-table-read-write-batch.html): Example that shows how to read and write batches of items using the DynamoDB service object.
- [Querying and Scanning a DynamoDB Table](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/dynamodb-example-query-scan.html): Example that shows how to query and scan tables in DynamoDB using the SDK for JavaScript.
- [Using the DynamoDB Document Client](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/dynamodb-example-document-client.html): Example that shows how to use the DynamoDB document client in the SDK for JavaScript.

### [Amazon EC2 Examples](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/ec2-examples.html)

Examples that show how to use the Amazon EC2 client class.

- [Creating an Amazon EC2 Instance](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/ec2-example-creating-an-instance.html): Example that shows how to create an Amazon EC2 instance using the service object.
- [Managing Amazon EC2 Instances](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/ec2-example-managing-instances.html): JavaScript code example that applies to Node.js execution
- [Working with Amazon EC2 Key Pairs](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/ec2-example-key-pairs.html): JavaScript code example that applies to Node.js execution
- [Using Regions and Availability Zones with Amazon EC2](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/ec2-example-regions-availability-zones.html): JavaScript code example that applies to Node.js execution
- [Working with Security Groups in Amazon EC2](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/ec2-example-security-groups.html): JavaScript code example that applies to Node.js execution
- [Using Elastic IP Addresses in Amazon EC2](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/ec2-example-elastic-ip-addresses.html): JavaScript code example that applies to Node.js execution

### [MediaConvert Examples](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/emc-examples.html)

Examples that show how to use the MediaConvert client class.

- [Creating and Managing Jobs](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/emc-examples-jobs.html): Example that shows how to create and manage conversion jobs in MediaConvert.
- [Using Job Templates](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/emc-examples-templates.html): JavaScript code example that applies to Node.js execution

### [AWS IAM Examples](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/iam-examples.html)

Examples that show how to use the IAM client class.

- [Managing IAM Users](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/iam-examples-managing-users.html): JavaScript code example that applies to Node.js execution
- [Working with IAM Policies](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/iam-examples-policies.html): JavaScript code example that applies to Node.js execution
- [Managing IAM Access Keys](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/iam-examples-managing-access-keys.html): JavaScript code example that applies to Node.js execution
- [Working with IAM Server Certificates](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/iam-examples-server-certificates.html): JavaScript code example that applies to Node.js execution
- [Managing IAM Account Aliases](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/iam-examples-account-aliases.html): JavaScript code example that applies to Node.js execution

### [Amazon Kinesis Example](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/kinesis-examples.html)

Examples that show how to use the Kinesis client class.

### [Capturing Web Page Scroll Progress with Amazon Kinesis](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/kinesis-examples-capturing-page-scrolling.html)

JavaScript code example that applies to browser execution

- [Capturing Web Page Scroll Progress Code](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/kinesis-examples-capturing-page-scrolling-full.html): Here is the browser script code for the Kinesis capturing web page scroll progress example.

### [Amazon S3 Examples](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/s3-examples.html)

Examples that show how to use the Amazon S3 client class.

### [Amazon S3 Browser Examples](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/s3-browser-examples.html)

The following topics show two examples of how the AWS SDK for JavaScript can be used in the browser to interact with Amazon S3 buckets.

### [Viewing Photos in an Amazon S3 Bucket from a Browser](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/s3-example-photos-view.html)

Example browser script that shows how to view photos in Amazon S3 buckets.

- [Viewing Photos in an Amazon S3 Bucket: Full Code](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/s3-example-photos-view-full.html): This section contains the full HTML and JavaScript code for the example in which photos in an Amazon S3 bucket can be viewed.

### [Uploading Photos to Amazon S3 from a Browser](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/s3-example-photo-album.html)

Example browser script that shows how to view and manipulate photo albums and photos in Amazon S3 buckets.

- [Uploading Photos to Amazon S3: Full Code](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/s3-example-photo-album-full.html): This section contains the full HTML and JavaScript code for the example in which photos are uploaded to an Amazon S3 photo album.

### [Amazon S3 Node.js Examples](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/s3-node-examples.html)

The following topics show examples of how the AWS SDK for JavaScript can be used to interact with Amazon S3 buckets using Node.js.

- [Creating and Using Amazon S3 Buckets](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/s3-example-creating-buckets.html): Example Node.js modules that show how to create and use Amazon S3 buckets.
- [Configuring Amazon S3 Buckets](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/s3-example-configuring-buckets.html): Example Node.js modules that show how to configure Amazon S3 buckets.
- [Managing Amazon S3 Bucket Access Permissions](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/s3-example-access-permissions.html): Example Node.js modules that show how to manage Amazon S3 bucket access permissions.
- [Working with Amazon S3 Bucket Policies](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/s3-example-bucket-policies.html): Example Node.js modules that show how to work with Amazon S3 bucket policies.
- [Using an Amazon S3 Bucket as a Static Web Host](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/s3-example-static-web-host.html): Example Node.js modules that show how to set up an Amazon S3 bucket as a static web host.

### [Amazon SES Examples](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/ses-examples.html)

Examples that show how to use the Amazon SES client class.

- [Managing Identities](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/ses-examples-managing-identities.html): JavaScript code example that applies to Node.js execution
- [Working with Email Templates](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/ses-examples-creating-template.html): JavaScript code example that applies to Node.js execution
- [Sending Email Using Amazon SES](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/ses-examples-sending-email.html): JavaScript code example that applies to Node.js execution
- [Using IP Address Filters](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/ses-examples-ip-filters.html): JavaScript code example that applies to Node.js execution
- [Using Receipt Rules](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/ses-examples-receipt-rules.html): JavaScript code example that applies to Node.js execution

### [Amazon SNS Examples](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/sns-examples.html)

Examples that show how to use the Amazon SNS client class.

- [Managing Topics](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/sns-examples-managing-topics.html): JavaScript code example that applies to Node.js execution
- [Publishing Messages to a Topic](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/sns-examples-publishing-messages.html): JavaScript code example that applies to Node.js execution
- [Managing Subscriptions](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/sns-examples-subscribing-unubscribing-topics.html): JavaScript code example that applies to Node.js execution
- [Sending SMS Messages](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/sns-examples-sending-sms.html): JavaScript code example that applies to Node.js execution

### [Amazon SQS Examples](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/sqs-examples.html)

Examples that show how to use the Amazon SQS client class.

- [Using Queues in Amazon SQS](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/sqs-examples-using-queues.html): JavaScript code example that applies to Node.js execution
- [Sending and Receiving Messages in Amazon SQS](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/sqs-examples-send-receive-messages.html): JavaScript code example that applies to Node.js execution
- [Managing Visibility Timeout in Amazon SQS](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/sqs-examples-managing-visibility-timeout.html): JavaScript code example that applies to Node.js execution
- [Enabling Long Polling in Amazon SQS](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/sqs-examples-enable-long-polling.html): JavaScript code example that applies to Node.js execution
- [Using Dead Letter Queues in Amazon SQS](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/sqs-examples-dead-letter-queues.html): JavaScript code example that applies to Node.js execution


## [Tutorials](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/tutorials.html)

- [Tutorial: Setting Up Node.js on an Amazon EC2 Instance](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/setting-up-node-on-ec2-instance.html): A common scenario for using Node.js with the SDK for JavaScript is to set up and run a Node.js web application on an Amazon Elastic Compute Cloud (Amazon EC2) instance.


## [Security](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/security.html)

- [Data protection](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/data-protection.html): Learn how the AWS shared responsibility model applies to data protection in this AWS product or service.
- [Identity and Access Management](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/security-iam.html): How to authenticate requests and manage access to your AWS resources.
- [Compliance Validation](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/compliance-validation.html): Provides information about compliance validation for this AWS product or service.
- [Resilience](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/disaster-recovery-resiliency.html): Provides information about resilience for this AWS Product or Service.
- [Infrastructure Security](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/infrastructure-security.html): Provides information about infrastructure security for this AWS product or service.
- [Enforcing a minimum version of TLS](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/enforcing-tls.html): How to verify and configure the version of TLS used by the SDK for JavaScript.
