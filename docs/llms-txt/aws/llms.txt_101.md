# Source: https://docs.aws.amazon.com/apprunner/latest/dg/llms.txt

# AWS App Runner Developer Guide

> Provides a conceptual overview of AWS App Runner, detailed feature descriptions, and instructions on how to use the service and deploy web applications.

- [What is AWS App Runner?](https://docs.aws.amazon.com/apprunner/latest/dg/what-is-apprunner.html)
- [Setting up](https://docs.aws.amazon.com/apprunner/latest/dg/setting-up.html)
- [Getting started](https://docs.aws.amazon.com/apprunner/latest/dg/getting-started.html)
- [Architecture and concepts](https://docs.aws.amazon.com/apprunner/latest/dg/architecture.html)
- [Image-based service](https://docs.aws.amazon.com/apprunner/latest/dg/service-source-image.html)
- [Developing for App Runner](https://docs.aws.amazon.com/apprunner/latest/dg/develop.html)
- [App Runner console](https://docs.aws.amazon.com/apprunner/latest/dg/console.html)
- [AWS Glossary](https://docs.aws.amazon.com/apprunner/latest/dg/glossary.html)

## [Code-based service](https://docs.aws.amazon.com/apprunner/latest/dg/service-source-code.html)

### [Python platform](https://docs.aws.amazon.com/apprunner/latest/dg/service-source-code-python.html)

Learn about the Python platform that AWS App Runner provides for building and running Python-based web applications.

- [Release information](https://docs.aws.amazon.com/apprunner/latest/dg/service-source-code-python-releases.html)

### [Node.js platform](https://docs.aws.amazon.com/apprunner/latest/dg/service-source-code-nodejs.html)

Learn about the Node.js platform that AWS App Runner provides for building and running Node.js-based web applications.

- [Release information](https://docs.aws.amazon.com/apprunner/latest/dg/service-source-code-nodejs-releases.html)

### [Java platform](https://docs.aws.amazon.com/apprunner/latest/dg/service-source-code-java.html)

Learn about the Java platform that AWS App Runner provides for building and running Java-based web applications.

- [Release information](https://docs.aws.amazon.com/apprunner/latest/dg/service-source-code-java-releases.html): This topic lists the full details for the Java runtime versions that App Runner supports.

### [.NET platform](https://docs.aws.amazon.com/apprunner/latest/dg/service-source-code-net6.html)

Learn about the .NET platform that AWS App Runner provides for building and running .NET-based web applications.

- [Release information](https://docs.aws.amazon.com/apprunner/latest/dg/service-source-code-dotnet-releases.html)

### [PHP platform](https://docs.aws.amazon.com/apprunner/latest/dg/service-source-code-php.html)

Learn about the PHP platform that AWS App Runner provides for building and running PHP-based web applications.

- [Release information](https://docs.aws.amazon.com/apprunner/latest/dg/service-source-code-php-releases.html)

### [Ruby platform](https://docs.aws.amazon.com/apprunner/latest/dg/service-source-code-ruby.html)

Learn about the Ruby platform that AWS App Runner provides for building and running Ruby-based web applications.

- [Release information](https://docs.aws.amazon.com/apprunner/latest/dg/service-source-code-ruby-releases.html)

### [Go platform](https://docs.aws.amazon.com/apprunner/latest/dg/service-source-code-go1.html)

Learn about the Go platform that AWS App Runner provides for building and running Go-based web applications.

- [Release information](https://docs.aws.amazon.com/apprunner/latest/dg/service-source-code-go-releases.html)


## [Managing your service](https://docs.aws.amazon.com/apprunner/latest/dg/manage.html)

- [Creation](https://docs.aws.amazon.com/apprunner/latest/dg/manage-create.html): Create a new AWS App Runner service from your container image or source code.
- [Rebuild failed service](https://docs.aws.amazon.com/apprunner/latest/dg/manage-rebuild.html): Rebuild a failed AWS App Runner service.
- [Deployment](https://docs.aws.amazon.com/apprunner/latest/dg/manage-deploy.html): Deploy a new version of your application source image or source code to your AWS App Runner service.

### [Configuration](https://docs.aws.amazon.com/apprunner/latest/dg/manage-configure.html)

Set and change configuration settings and options of your AWS App Runner service.

- [Observability configuration](https://docs.aws.amazon.com/apprunner/latest/dg/manage-configure-observability.html): Configure observability settings, for example, tracing, for your AWS App Runner service.
- [Configuration resources](https://docs.aws.amazon.com/apprunner/latest/dg/manage-configure-resources.html): Configure settings for your AWS App Runner service using separate sharable resources.
- [Health check configuration](https://docs.aws.amazon.com/apprunner/latest/dg/manage-configure-healthcheck.html): Configuring health check options for your AWS App Runner service.
- [Connections](https://docs.aws.amazon.com/apprunner/latest/dg/manage-connections.html): Manage connections of AWS App Runner services to private source repositories.
- [Auto scaling](https://docs.aws.amazon.com/apprunner/latest/dg/manage-autoscaling.html): Configure the automatic scaling settings of your AWS App Runner service.

### [Custom domain names](https://docs.aws.amazon.com/apprunner/latest/dg/manage-custom-domains.html)

Link custom domain names that you own to the web application in your AWS App Runner service to associate them with CNAMEs of your service.

- [Configure an Amazon RouteÂ 53 alias record](https://docs.aws.amazon.com/apprunner/latest/dg/manage-custom-domains-route53.html): Guidance on how to create Amazon RouteÂ 53 record to route traffic to your App Runner service.
- [Pausing / resuming](https://docs.aws.amazon.com/apprunner/latest/dg/manage-pause.html): Pause and resume your AWS App Runner service to temporarily make it inactive and unavailable.
- [Deletion](https://docs.aws.amazon.com/apprunner/latest/dg/manage-delete.html): Delete your AWS App Runner service to remove the running service, free up resources, and delete your data.


## [Reference Environment variables](https://docs.aws.amazon.com/apprunner/latest/dg/env-variable.html)

- [Manage environment variables](https://docs.aws.amazon.com/apprunner/latest/dg/env-variable-manage.html): Manage the environment variables for your App Runner service.


## [Networking](https://docs.aws.amazon.com/apprunner/latest/dg/network.html)

- [Terminology](https://docs.aws.amazon.com/apprunner/latest/dg/network-terms.html): Enable your AWS App Runner service to access applications that run in a private VPC from Amazon Virtual Private Cloud (Amazon VPC).

### [Incoming traffic](https://docs.aws.amazon.com/apprunner/latest/dg/network-incoming.html)

Set up your AWS App Runner service to receive incoming traffic from private or public endpoints.

### [Enable Private endpoint](https://docs.aws.amazon.com/apprunner/latest/dg/network-pl.html)

Enable your AWS App Runner service to create a private connection between your App Runner service and Amazon VPC.

- [Manage Private endpoints](https://docs.aws.amazon.com/apprunner/latest/dg/network-pl-manage.html): Enable your AWS App Runner service to create a private connection between your App Runner service and Amazon VPC.
- [Enable IPv6 for App Runner's endpoints](https://docs.aws.amazon.com/apprunner/latest/dg/network-dual-stack.html): Enable dual stack for your AWS App Runner service.
- [Outgoing traffic](https://docs.aws.amazon.com/apprunner/latest/dg/network-vpc.html): Enable your AWS App Runner service to access applications that run in a private VPC from Amazon Virtual Private Cloud (Amazon VPC).


## [Observability](https://docs.aws.amazon.com/apprunner/latest/dg/monitor.html)

- [Activity](https://docs.aws.amazon.com/apprunner/latest/dg/monitor-activity.html): Track your AWS App Runner service activity by viewing service operations.
- [Logs (CloudWatch Logs)](https://docs.aws.amazon.com/apprunner/latest/dg/monitor-cwl.html): Get insights into your AWS App Runner service by looking at deployment and service logs in the App Runner console and in Amazon CloudWatch Logs.
- [Metrics (CloudWatch)](https://docs.aws.amazon.com/apprunner/latest/dg/monitor-cw.html): Get insights into your AWS App Runner service by viewing metrics in the App Runner console and in Amazon CloudWatch.
- [Event handling (EventBridge)](https://docs.aws.amazon.com/apprunner/latest/dg/monitor-ev.html): Handle events related to your AWS App Runner service by defining rules with event patterns and target actions in Amazon EventBridge.
- [API actions (CloudTrail)](https://docs.aws.amazon.com/apprunner/latest/dg/monitor-ct.html): Learn about logging App Runner with AWS CloudTrail.
- [Tracing (X-Ray)](https://docs.aws.amazon.com/apprunner/latest/dg/monitor-xray.html): Trace requests into your application and downstream AWS and other web service calls using AWS X-Ray to gain insights and identify issues and opportunities for code optimization.


## [AWS WAF web ACL](https://docs.aws.amazon.com/apprunner/latest/dg/waf.html)

- [Manage web ACLs](https://docs.aws.amazon.com/apprunner/latest/dg/waf-manage.html): Manage the environment variables for your App Runner service.


## [App Runner configuration file](https://docs.aws.amazon.com/apprunner/latest/dg/config-file.html)

- [Examples](https://docs.aws.amazon.com/apprunner/latest/dg/config-file-examples.html): See complete examples of AWS App Runner configuration files, with all sections and keys, for managed runtimes.
- [Reference](https://docs.aws.amazon.com/apprunner/latest/dg/config-file-ref.html): Learn the syntax and semantics of an AWS App Runner configuration file, and specify the build and runtime behavior of your service.


## [App Runner API](https://docs.aws.amazon.com/apprunner/latest/dg/api.html)

- [Using AWS CloudShell](https://docs.aws.amazon.com/apprunner/latest/dg/api-cshell.html): Learn about how you can use AWS CloudShell to work with AWS App Runner.


## [Troubleshooting](https://docs.aws.amazon.com/apprunner/latest/dg/troubleshooting.html)

- [Failed to create service](https://docs.aws.amazon.com/apprunner/latest/dg/troubleshooting-create-failure.html): Troubleshooting steps for when you create a new AWS App Runner service from your container image or source code and fails to create.
- [Custom domain names](https://docs.aws.amazon.com/apprunner/latest/dg/manage-custom-domain-troubleshoot.html): Lists steps to troubleshoot and resolve the errors encountered while creating a custom domain.
- [Request routing error](https://docs.aws.amazon.com/apprunner/latest/dg/request-route-404-troubleshoot.html): Lists steps to troubleshoot and resolve the errors encountered sending HTTP/HTTPS traffic your App Runner service endpoints.
- [Connection fails to Amazon RDS or downstream service](https://docs.aws.amazon.com/apprunner/latest/dg/troubleshooting.vpc-outbound-connect-failure.html): Troubleshooting steps for when your service fails to connect to to Amazon RDS or downstream service.
- [When there are not enough IP addresses for launching or scaling](https://docs.aws.amazon.com/apprunner/latest/dg/troubleshooting-not-enough-ips.html): When there are not enough IP addresses for launching or scaling


## [Security](https://docs.aws.amazon.com/apprunner/latest/dg/security.html)

### [Data protection](https://docs.aws.amazon.com/apprunner/latest/dg/security-data-protection.html)

Learn how the AWS shared responsibility model applies to data protection in AWS App Runner.

- [Data encryption](https://docs.aws.amazon.com/apprunner/latest/dg/security-data-protection-encryption.html): Learn about data encryption in AWS App Runner.
- [Internetwork privacy](https://docs.aws.amazon.com/apprunner/latest/dg/security-data-protection-internetwork.html): Learn about internetwork traffic privacy in AWS App Runner.

### [Identity and access management](https://docs.aws.amazon.com/apprunner/latest/dg/security-iam.html)

How to authenticate requests and manage access your App Runner resources.

- [App Runner and IAM](https://docs.aws.amazon.com/apprunner/latest/dg/security_iam_service-with-iam.html): Before you use IAM to manage access to AWS App Runner, you should understand what IAM features are available to use with App Runner.
- [Identity-based policy examples](https://docs.aws.amazon.com/apprunner/latest/dg/security_iam_id-based-policy-examples.html): By default, IAM users and roles don't have permission to create or modify AWS App Runner resources.

### [Using service-linked roles](https://docs.aws.amazon.com/apprunner/latest/dg/security-iam-slr.html)

How to use service-linked roles to give App Runner access to resources in your AWS account.

- [Management role](https://docs.aws.amazon.com/apprunner/latest/dg/using-service-linked-roles-management.html): How to use service-linked roles to give App Runner access to resources in your AWS account.
- [Networking role](https://docs.aws.amazon.com/apprunner/latest/dg/using-service-linked-roles-networking.html): How to use service-linked roles to give App Runner access to resources in your AWS account.
- [AWS managed policies](https://docs.aws.amazon.com/apprunner/latest/dg/security-iam-awsmanpol.html): Learn about AWS managed policies for App Runner and recent changes to those policies.
- [Troubleshooting](https://docs.aws.amazon.com/apprunner/latest/dg/security_iam_troubleshoot.html): Use the following information to help you diagnose and fix common issues that you might encounter when working with AWS App Runner and IAM.
- [Logging and monitoring](https://docs.aws.amazon.com/apprunner/latest/dg/security-monitoring.html): Monitor your AWS App Runner service by viewing metrics, reading logs, and tracking service action calls.
- [Compliance validation](https://docs.aws.amazon.com/apprunner/latest/dg/security-compliance.html): Learn what AWS services are in scope of a specific compliance program.
- [Resilience](https://docs.aws.amazon.com/apprunner/latest/dg/security-resilience.html): Learn how AWS architecture supports data redundancy, and learn about specific AWS App Runner features for data resiliency.
- [Infrastructure security](https://docs.aws.amazon.com/apprunner/latest/dg/security-infrastructure.html): Learn how AWS App Runner isolates service traffic.
- [VPC endpoints](https://docs.aws.amazon.com/apprunner/latest/dg/security-vpce.html): Configure interface VPC endpoints to privately connect your VPC to AWS App Runner services, other supported AWS services, and VPC endpoint services powered by AWS PrivateLink.
- [Shared responsibility model](https://docs.aws.amazon.com/apprunner/latest/dg/security-shared-responsibility.html): AWS App Runner and our customers share responsibility for platform management and updates to maintain secure and compliant environments for customer applications.
- [Security best practices](https://docs.aws.amazon.com/apprunner/latest/dg/security-best-practices.html): Follow these security best practices to improve reliability, security, availability, and performance of your AWS App Runner solutions.
