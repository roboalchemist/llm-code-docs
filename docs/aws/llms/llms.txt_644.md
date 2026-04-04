# Source: https://docs.aws.amazon.com/panorama/latest/dev/llms.txt

# AWS Panorama Developer Guide

> Provides a conceptual overview of AWS Panorama and detailed instructions for using its features.

- [Samples](https://docs.aws.amazon.com/panorama/latest/dev/panorama-samples.html)
- [Troubleshooting](https://docs.aws.amazon.com/panorama/latest/dev/panorama-troubleshooting.html)
- [Releases](https://docs.aws.amazon.com/panorama/latest/dev/panorama-releases.html)

## [What is AWS Panorama?](https://docs.aws.amazon.com/panorama/latest/dev/panorama-welcome.html)

- [AWS Panorama end of support](https://docs.aws.amazon.com/panorama/latest/dev/panorama-end-of-support.html): Information about the end of support for AWS Panorama.


## [Getting started](https://docs.aws.amazon.com/panorama/latest/dev/panorama-gettingstarted.html)

- [Concepts](https://docs.aws.amazon.com/panorama/latest/dev/gettingstarted-concepts.html): Learn about AWS Panorama concepts.
- [Setting up](https://docs.aws.amazon.com/panorama/latest/dev/gettingstarted-setup.html): Set up the AWS Panorama Appliance with the AWS Panorama console.
- [Deploying an application](https://docs.aws.amazon.com/panorama/latest/dev/gettingstarted-deploy.html): Deploy a sample application to the AWS Panorama Appliance.
- [Developing applications](https://docs.aws.amazon.com/panorama/latest/dev/gettingstarted-sample.html): Learn about the AWS Panorama sample application's implementation and features.
- [Supported models and cameras](https://docs.aws.amazon.com/panorama/latest/dev/gettingstarted-compatibility.html): Learn about the model frameworks and cameras that AWS Panorama supports.
- [Appliance specifications](https://docs.aws.amazon.com/panorama/latest/dev/gettingstarted-hardware.html): Learn about the AWS Panorama Appliance hardware.
- [Quotas](https://docs.aws.amazon.com/panorama/latest/dev/gettingstarted-quotas.html): Service quotas limit the resources that you can create in each Region.


## [Permissions](https://docs.aws.amazon.com/panorama/latest/dev/panorama-permissions.html)

- [User policies](https://docs.aws.amazon.com/panorama/latest/dev/permissions-user.html): Grant IAM users, groups, and roles permission to use AWS Panorama.
- [Service roles](https://docs.aws.amazon.com/panorama/latest/dev/permissions-services.html): Learn about services that integrate with AWS Panorama.
- [Application role](https://docs.aws.amazon.com/panorama/latest/dev/permissions-application.html): Use an IAM role to grant AWS permissions to a AWS Panorama application.


## [Appliance](https://docs.aws.amazon.com/panorama/latest/dev/panorama-appliance.html)

- [Managing](https://docs.aws.amazon.com/panorama/latest/dev/appliance-manage.html): You use the AWS Panorama console to configure, upgrade or deregister the AWS Panorama Appliance and other compatible devices.
- [Network setup](https://docs.aws.amazon.com/panorama/latest/dev/appliance-network.html): Connect the AWS Panorama Appliance to your network.
- [Cameras](https://docs.aws.amazon.com/panorama/latest/dev/appliance-cameras.html): To register video streams as data sources for your application, use the AWS Panorama console.
- [Applications](https://docs.aws.amazon.com/panorama/latest/dev/appliance-applications.html): An application is a combination of code, models, and configuration.
- [Buttons and lights](https://docs.aws.amazon.com/panorama/latest/dev/appliance-buttons.html): The AWS Panorama Appliance has two LED lights above the power button that indicate the device status and network connectivity.


## [Managing applications](https://docs.aws.amazon.com/panorama/latest/dev/panorama-applications.html)

- [Deploy](https://docs.aws.amazon.com/panorama/latest/dev/applications-deploy.html): Automate application deployments with the AWS CLI.
- [Manage](https://docs.aws.amazon.com/panorama/latest/dev/applications-manage.html): Use the AWS Panorama console to manage deployed applications.
- [Packages](https://docs.aws.amazon.com/panorama/latest/dev/applications-packages.html): Configure node packages and assets prior to deployment.
- [Application manifest](https://docs.aws.amazon.com/panorama/latest/dev/applications-manifest.html): Define your AWS Panorama application in a graph-based configuration file.
- [Nodes](https://docs.aws.amazon.com/panorama/latest/dev/applications-nodes.html): Define and connect nodes in an application manifest.
- [Parameters](https://docs.aws.amazon.com/panorama/latest/dev/applications-manifest-parameters.html): Configure applications at deploy time with parameters.
- [Overrides](https://docs.aws.amazon.com/panorama/latest/dev/applications-overrides.html): Override application manifest settings at deploy time.


## [Building applications](https://docs.aws.amazon.com/panorama/latest/dev/panorama-development.html)

- [Models](https://docs.aws.amazon.com/panorama/latest/dev/applications-models.html): A computer vision model is a software program that is trained to detect objects in images.
- [Build an image](https://docs.aws.amazon.com/panorama/latest/dev/applications-image.html): Create an application container image with a Dockerfile.
- [AWS SDK](https://docs.aws.amazon.com/panorama/latest/dev/applications-awssdk.html): You can use the AWS SDK for Python (Boto) to call AWS services from your application code.
- [Application SDK](https://docs.aws.amazon.com/panorama/latest/dev/applications-panoramasdk.html): The AWS Panorama Application SDK is a Python library for developing AWS Panorama applications.
- [Running multiple threads](https://docs.aws.amazon.com/panorama/latest/dev/applications-threading.html): Run additional threads to perform background tasks in parallel.
- [Serving inbound traffic](https://docs.aws.amazon.com/panorama/latest/dev/applications-ports.html): Open ports on the AWS Panorama Appliance for monitoring or debugging.
- [Using the GPU](https://docs.aws.amazon.com/panorama/latest/dev/applications-gpuaccess.html): Configure an application to use GPU-accelerated libraries or machine learning models in application code.
- [Tutorial â Windows development environment](https://docs.aws.amazon.com/panorama/latest/dev/applications-devenvwindows.html): Set up a development environment for building AWS Panorama applications in Windows.


## [The AWS Panorama API](https://docs.aws.amazon.com/panorama/latest/dev/panorama-api.html)

- [Automate device registration](https://docs.aws.amazon.com/panorama/latest/dev/api-provision.html): Register devices with the AWS Panorama API.
- [Manage appliance](https://docs.aws.amazon.com/panorama/latest/dev/api-appliance.html): Automate appliance management workflows with the AWS Panorama API.
- [Automate application deployment](https://docs.aws.amazon.com/panorama/latest/dev/api-deploy.html): Deploy applications with the AWS Panorama API.
- [Manage applications](https://docs.aws.amazon.com/panorama/latest/dev/api-applications.html): Monitor and manage application instances and nodes.
- [Using VPC endpoints](https://docs.aws.amazon.com/panorama/latest/dev/api-endpoints.html): Use a VPC endpoint to connect to AWS Panorama


## [Monitoring](https://docs.aws.amazon.com/panorama/latest/dev/panorama-monitoring.html)

- [AWS Panorama console](https://docs.aws.amazon.com/panorama/latest/dev/monitoring-console.html): Monitor AWS Panorama applications in the AWS Management Console.
- [Logs](https://docs.aws.amazon.com/panorama/latest/dev/monitoring-logging.html): Use CloudWatch Logs to monitor and troubleshoot AWS Panorama applications.
- [CloudWatch metrics](https://docs.aws.amazon.com/panorama/latest/dev/monitoring-metrics.html): Monitor appliances with CloudWatch metrics.


## [Security](https://docs.aws.amazon.com/panorama/latest/dev/panorama-security.html)

- [Security features](https://docs.aws.amazon.com/panorama/latest/dev/security-features.html): To protect your applications, models, and hardware against malicious code and other exploits, the AWS Panorama Appliance implements an extensive set of security features.
- [Best practices](https://docs.aws.amazon.com/panorama/latest/dev/security-bestpractices.html): Keep in mind the following best practices when using the AWS Panorama appliance.
- [Data protection](https://docs.aws.amazon.com/panorama/latest/dev/security-dataprotection.html): Learn how the AWS shared responsibility model applies to data protection in AWS Panorama.

### [Identity and access management](https://docs.aws.amazon.com/panorama/latest/dev/security-iam.html)

How to authenticate requests and manage access your AWS Panorama resources.

- [How AWS Panorama works with IAM](https://docs.aws.amazon.com/panorama/latest/dev/security_iam_service-with-iam.html): Before you use IAM to manage access to AWS Panorama, you should understand what IAM features are available to use with AWS Panorama.
- [Identity-based policy examples](https://docs.aws.amazon.com/panorama/latest/dev/security_iam_id-based-policy-examples.html): By default, IAM users and roles don't have permission to create or modify AWS Panorama resources.
- [AWS managed policies](https://docs.aws.amazon.com/panorama/latest/dev/security-iam-awsmanpol.html): Learn about AWS managed policies for Amazon Lookout for Metrics.
- [Using service-linked roles](https://docs.aws.amazon.com/panorama/latest/dev/using-service-linked-roles.html): How to use service-linked roles to give AWS Panorama access to resources in your AWS account.
- [Cross-service confused deputy prevention](https://docs.aws.amazon.com/panorama/latest/dev/security-iam-trustpolicies.html): The confused deputy problem is a security issue where an entity that doesn't have permission to perform an action can coerce a more-privileged entity to perform the action.
- [Troubleshooting](https://docs.aws.amazon.com/panorama/latest/dev/security_iam_troubleshoot.html): Use the following information to help you diagnose and fix common issues that you might encounter when working with AWS Panorama and IAM.
- [Compliance validation](https://docs.aws.amazon.com/panorama/latest/dev/security-compliance.html): Learn what AWS services are in scope of a specific compliance program.
- [Infrastructure security](https://docs.aws.amazon.com/panorama/latest/dev/security-infrastructure.html): Learn how AWS Panorama isolates service traffic.
- [Runtime environment](https://docs.aws.amazon.com/panorama/latest/dev/security-runtime.html): Security considerations for software running on the AWS Panorama Appliance.
