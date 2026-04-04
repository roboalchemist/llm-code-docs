# Source: https://docs.aws.amazon.com/gameliftstreams/latest/developerguide/llms.txt

# Amazon GameLift Streams Developer Guide

> Learn how to upload your game and create a stream group to manage streaming capacity in multiple geographical locations, how to integrate a web client and backend server with your game to start streaming sessions, and how to monitor streaming usage and optimize your streaming solution to lower streaming capacity costs.

- [What is Amazon GameLift Streams?](https://docs.aws.amazon.com/gameliftstreams/latest/developerguide/what-is-service.html)
- [Terms of use](https://docs.aws.amazon.com/gameliftstreams/latest/developerguide/terms-of-use.html)
- [Setting up](https://docs.aws.amazon.com/gameliftstreams/latest/developerguide/setting-up.html)
- [Launch checklist](https://docs.aws.amazon.com/gameliftstreams/latest/developerguide/gameliftstreams-application-launch-checklist.html)
- [Usage and bills](https://docs.aws.amazon.com/gameliftstreams/latest/developerguide/pricing.html)

## [Getting started](https://docs.aws.amazon.com/gameliftstreams/latest/developerguide/getting-started.html)

- [Choosing a configuration](https://docs.aws.amazon.com/gameliftstreams/latest/developerguide/choosing-configuration.html): Learn how to choose optimal runtime environments and configuration settings for your Amazon GameLift Streams applications.
- [Configuration options](https://docs.aws.amazon.com/gameliftstreams/latest/developerguide/configuration-options.html): Discover the available runtime environments, stream classes, and configuration options for Amazon GameLift Streams applications.
- [Your first stream](https://docs.aws.amazon.com/gameliftstreams/latest/developerguide/streaming-process.html): Learn how to create your first Amazon GameLift Streams application and test streaming with a step-by-step tutorial.


## [Managing your streams](https://docs.aws.amazon.com/gameliftstreams/latest/developerguide/manage-streams.html)

- [Applications](https://docs.aws.amazon.com/gameliftstreams/latest/developerguide/applications.html): Learn how to upload your application and create an application resource for streaming with Amazon GameLift Streams.
- [Stream groups](https://docs.aws.amazon.com/gameliftstreams/latest/developerguide/stream-groups.html): Learn how to manage and scale your game streaming resources efficiently using Amazon GameLift Streams stream groups.
- [Multi-application stream groups](https://docs.aws.amazon.com/gameliftstreams/latest/developerguide/multi-apps.html): Learn how to optimize resources by setting up multi-application stream groups to run multiple games efficiently in Amazon GameLift Streams.
- [Stream sessions](https://docs.aws.amazon.com/gameliftstreams/latest/developerguide/stream-sessions.html): Learn how to create and manage stream sessions to deliver interactive game experiences to your players using Amazon GameLift Streams.
- [Export stream session files](https://docs.aws.amazon.com/gameliftstreams/latest/developerguide/stream-sessions-export-files.html): Learn how to export and download files from your Amazon GameLift Streams sessions for debugging and analysis purposes.


## [Amazon GameLift Streams backend service and web client](https://docs.aws.amazon.com/gameliftstreams/latest/developerguide/sdk.html)

- [Supported browsers and input](https://docs.aws.amazon.com/gameliftstreams/latest/developerguide/sdk-browsers-input.html): Discover which browsers and input devices are supported for Amazon GameLift Streams client applications.
- [Required ports](https://docs.aws.amazon.com/gameliftstreams/latest/developerguide/required-ports.html): Learn about the network ports and firewall requirements needed for Amazon GameLift Streams connectivity.
- [Setting up a web server and client](https://docs.aws.amazon.com/gameliftstreams/latest/developerguide/setting-up-web-sdk.html): Learn how to set up a web server and client application using the Amazon GameLift Streams Web SDK and sample code.
- [Customize stream appearance](https://docs.aws.amazon.com/gameliftstreams/latest/developerguide/sdk-stream-appearance.html): Learn how to customize how an Amazon GameLift Streams stream appears to end-users by displaying a loading screen.
- [Locale preference](https://docs.aws.amazon.com/gameliftstreams/latest/developerguide/sdk-locale-support.html): Learn how to configure locale preferences for Amazon GameLift Streams to support location-specific information.
- [Mouse movement handling](https://docs.aws.amazon.com/gameliftstreams/latest/developerguide/sdk-mouse-movement.html): Learn how Amazon GameLift Streams handles mouse input and cursor management for optimal streaming performance.
- [Data channel communication](https://docs.aws.amazon.com/gameliftstreams/latest/developerguide/data-channels.html): Learn how to use data channels to enable secure communication between your Amazon GameLift Streams application and web clients.


## [Security](https://docs.aws.amazon.com/gameliftstreams/latest/developerguide/security.html)

- [Data protection](https://docs.aws.amazon.com/gameliftstreams/latest/developerguide/data-protection.html): Learn how the AWS shared responsibility model applies to data protection in Amazon GameLift Streams.

### [Identity and Access Management](https://docs.aws.amazon.com/gameliftstreams/latest/developerguide/security-iam.html)

How to authenticate requests and manage access to your Amazon GameLift Streams resources.

- [How Amazon GameLift Streams works with IAM](https://docs.aws.amazon.com/gameliftstreams/latest/developerguide/security_iam_service-with-iam.html): Learn how Amazon GameLift Streams integrates with AWS Identity and Access Management (IAM) for secure resource access.
- [Identity-based policy examples](https://docs.aws.amazon.com/gameliftstreams/latest/developerguide/security_iam_id-based-policy-examples.html): Discover identity-based policy examples to control access to Amazon GameLift Streams resources and actions.
- [Troubleshooting](https://docs.aws.amazon.com/gameliftstreams/latest/developerguide/security_iam_troubleshoot.html): Learn how to troubleshoot common identity and access issues with Amazon GameLift Streams and AWS Identity and Access Management.
- [Compliance validation](https://docs.aws.amazon.com/gameliftstreams/latest/developerguide/compliance-validation.html): Learn what AWS services are in scope of a specific compliance program.
- [Resilience](https://docs.aws.amazon.com/gameliftstreams/latest/developerguide/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and learn about specific Amazon GameLift Streams features for data resiliency.

### [Infrastructure Security](https://docs.aws.amazon.com/gameliftstreams/latest/developerguide/infrastructure-security.html)

Learn how to securely access Amazon GameLift Streams APIs using TLS encryption, proper cipher suites, and AWS authentication credentials.

- [Reuse and multi-tenancy](https://docs.aws.amazon.com/gameliftstreams/latest/developerguide/infrastructure-security-tenancy.html): Learn how Amazon GameLift Streams isolates user data throughout multi-tenancy and reuse of compute resources.
- [Interface VPC endpoints](https://docs.aws.amazon.com/gameliftstreams/latest/developerguide/infrastructure-security-vpc-endpoints.html): Learn how to use interface VPC endpoints to improve security when accessing Amazon GameLift Streams APIs privately.
- [Configuration and vulnerability analysis](https://docs.aws.amazon.com/gameliftstreams/latest/developerguide/vulnerability-analysis-management.html): Find best practices for regularly patching, updating, and securing the operating system and applications on your Amazon GameLift Streams instances.
- [Security best practices](https://docs.aws.amazon.com/gameliftstreams/latest/developerguide/security-best-practices.html): Learn how AWS architecture supports data redundancy, and learn about specific Amazon GameLift Streams features for data resiliency.


## [Monitoring Amazon GameLift Streams](https://docs.aws.amazon.com/gameliftstreams/latest/developerguide/monitoring-overview.html)

- [Monitor with CloudWatch](https://docs.aws.amazon.com/gameliftstreams/latest/developerguide/monitoring-cloudwatch.html): Learn about monitoring stream capacity, usage, and performance in Amazon GameLift Streams using Amazon CloudWatch Logs.
- [Logging API calls with CloudTrail](https://docs.aws.amazon.com/gameliftstreams/latest/developerguide/logging-using-cloudtrail.html): Learn about logging Amazon GameLift Streams API calls with AWS CloudTrail.
- [Real-time performance stats](https://docs.aws.amazon.com/gameliftstreams/latest/developerguide/realtime-performance-stats.html): Learn how to use performance stats to monitor your stream session's resource utilization.


## [Troubleshoot](https://docs.aws.amazon.com/gameliftstreams/latest/developerguide/troubleshoot.html)

### [Compatibility with Proton](https://docs.aws.amazon.com/gameliftstreams/latest/developerguide/troubleshoot-compatibility-wp.html)

Learn how to test compatibility of your game with the Proton runtime environment, and troubleshoot compatibility issues that you find.

- [Set up a local machine](https://docs.aws.amazon.com/gameliftstreams/latest/developerguide/troubleshoot-compatibility-setup-local.html): Set up a local Ubuntu environment to test and troubleshoot your Amazon GameLift Streams application's compatibility with Proton.
- [Set up a remote machine](https://docs.aws.amazon.com/gameliftstreams/latest/developerguide/troubleshoot-compatibility-setup-remote.html): Set up a remote environment using Amazon EC2 to troubleshoot your Amazon GameLift Streams application's compatibility with Proton.
- [Troubleshoot on Proton](https://docs.aws.amazon.com/gameliftstreams/latest/developerguide/troubleshoot-compatibility-wp-proton.html): Set up Proton on your machine to troubleshoot compatibility issues between your Amazon GameLift Streams application and Proton.
- [Profiling Unreal Engine performance](https://docs.aws.amazon.com/gameliftstreams/latest/developerguide/profiling-ue.html): Learn how to analyze your Unreal Engine game or application performance to help you identify areas to optimize, leading to smoother streaming in Amazon GameLift Streams.


## [Regions, quotas, and limitations](https://docs.aws.amazon.com/gameliftstreams/latest/developerguide/regions-quotas.html)

- [AWS Regions and streaming locations](https://docs.aws.amazon.com/gameliftstreams/latest/developerguide/regions-quotas-rande.html): Discover which AWS Regions and remote locations support Amazon GameLift Streams for your streaming deployments.
- [Supported locations by stream class](https://docs.aws.amazon.com/gameliftstreams/latest/developerguide/stream-class-locations.html): View which locations support each stream class for your Amazon GameLift Streams deployments.
- [Service quotas](https://docs.aws.amazon.com/gameliftstreams/latest/developerguide/quotas.html): Learn about Amazon GameLift Streams service quotas and limits that apply to your AWS account and streaming resources.
- [API rate limits](https://docs.aws.amazon.com/gameliftstreams/latest/developerguide/api-rate-limits.html): Understand the API rate limits that apply to Amazon GameLift Streams service requests from your AWS account.
- [Other limitations](https://docs.aws.amazon.com/gameliftstreams/latest/developerguide/other-limitations.html): Discover additional Amazon GameLift Streams limitations beyond standard quotas and API limits that may affect your streaming applications.
