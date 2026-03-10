# Source: https://docs.aws.amazon.com/cloud-map/latest/dg/llms.txt

# AWS Cloud Map Developer Guide

> AWS Cloud Map is a fully managed service that you can use to create and maintain a map of the backend services and resources that your applications depend on.

- [What Is AWS Cloud Map?](https://docs.aws.amazon.com/cloud-map/latest/dg/what-is-cloud-map.html)
- [Document history](https://docs.aws.amazon.com/cloud-map/latest/dg/doc-history.html)

## [Get started](https://docs.aws.amazon.com/cloud-map/latest/dg/tutorials.html)

- [Set up](https://docs.aws.amazon.com/cloud-map/latest/dg/setting-up-cloud-map.html): Learn how to set up to use AWS Cloud Map.
- [Use AWS Cloud Map with DNS queries and API calls](https://docs.aws.amazon.com/cloud-map/latest/dg/tutorial-private-namespace.html): Tutorial for setting up AWS Cloud Map namespace for service discovery using DNS queries.
- [Use AWS Cloud Map service discovery with DNS queries and API calls using the AWS CLI](https://docs.aws.amazon.com/cloud-map/latest/dg/tutorial-private-namespace-cli.html): Tutorial for setting up AWS Cloud Map namespace for service discovery using DNS queries and API calls using the AWS CLI.
- [Use AWS Cloud Map with custom attributes](https://docs.aws.amazon.com/cloud-map/latest/dg/tutorial-microservices.html): Tutorial for setting up AWS Cloud Map service discovery using custom attributes.
- [Use AWS Cloud Map service discovery with custom attributes using the AWS CLI](https://docs.aws.amazon.com/cloud-map/latest/dg/tutorial-microservices-cli.html): Tutorial for setting up AWS Cloud Map service discovery using custom attributes using the AWS CLI.


## [Namespaces](https://docs.aws.amazon.com/cloud-map/latest/dg/working-with-namespaces.html)

- [Creating a namespace](https://docs.aws.amazon.com/cloud-map/latest/dg/creating-namespaces.html): Learn how to create a namespace using the CLI, console, and SDK for Python
- [Listing namespaces](https://docs.aws.amazon.com/cloud-map/latest/dg/listing-namespaces.html): Learn how to view a list of your AWS Cloud Map namespaces.
- [Deleting a namespace](https://docs.aws.amazon.com/cloud-map/latest/dg/deleting-namespaces.html): Learn how to delete an AWS Cloud Map namespace.

### [Shared namespaces](https://docs.aws.amazon.com/cloud-map/latest/dg/sharing-namespaces.html)

Learn about cross-account sharing of AWS Cloud Map namespaces.

- [Sharing an AWS Cloud Map namespace](https://docs.aws.amazon.com/cloud-map/latest/dg/sharing-share.html): When you share an AWS Cloud Map namespace that you own with other AWS accounts (consumers), you enable these accounts to discover the up-to-date network locations of services in the namespace without the need for temporary credentials.
- [Stop sharing a AWS Cloud Map namespace](https://docs.aws.amazon.com/cloud-map/latest/dg/sharing-unshare.html): When a namespace is no longer shared, the namespace and any services and instances associated with it can no longer be accessed by consumer AWS accounts.
- [Identifying a shared AWS Cloud Map namespace](https://docs.aws.amazon.com/cloud-map/latest/dg/sharing-identify.html): Owners and consumers can identify shared namespaces using the AWS Cloud Map console and AWS CLI.


## [Services](https://docs.aws.amazon.com/cloud-map/latest/dg/working-with-services.html)

- [Health check configuration](https://docs.aws.amazon.com/cloud-map/latest/dg/services-health-checks.html): Learn about health checks for AWS Cloud Map services.
- [DNS configuration](https://docs.aws.amazon.com/cloud-map/latest/dg/services-route53.html): Learn about DNS configurations for AWS Cloud Map services.
- [Creating a service](https://docs.aws.amazon.com/cloud-map/latest/dg/creating-services.html): Learn how to create an AWS Cloud Map service.
- [Updating a service](https://docs.aws.amazon.com/cloud-map/latest/dg/editing-services.html): Learn how to update a AWS Cloud Map service using the AWS Management Console, AWS CLI, and SDK for Python.
- [Listing services in a namespace](https://docs.aws.amazon.com/cloud-map/latest/dg/listing-services.html): Learn how to view a list of AWS Cloud Map services in a namespace.
- [Deleting a service](https://docs.aws.amazon.com/cloud-map/latest/dg/deleting-services.html): Learn how to delete a AWS Cloud Map service using the AWS Management Console, AWS CLI, and SDK for Python.


## [Service instances](https://docs.aws.amazon.com/cloud-map/latest/dg/working-with-instances.html)

- [Registering a service instance](https://docs.aws.amazon.com/cloud-map/latest/dg/registering-instances.html): Learn how to register a service instance using the AWS CLI, AWS Management Console, and SDK for Python.
- [Listing service instances](https://docs.aws.amazon.com/cloud-map/latest/dg/listing-instances.html): Learn how to view a list of AWS Cloud Map instances in a service.
- [Updating a service instance](https://docs.aws.amazon.com/cloud-map/latest/dg/updating-instances.html): Learn how to update AWS Cloud Map service instances.
- [Deregistering a service instance](https://docs.aws.amazon.com/cloud-map/latest/dg/deregistering-instances.html): Learn how to deregister service instances using the AWS Management Console, AWS CLI, and SDK for Python.


## [Security](https://docs.aws.amazon.com/cloud-map/latest/dg/security.html)

### [Identity and Access Management](https://docs.aws.amazon.com/cloud-map/latest/dg/security-iam.html)

How to authenticate requests and manage access to your AWS Cloud Map resources.

- [How AWS Cloud Map works with IAM](https://docs.aws.amazon.com/cloud-map/latest/dg/security_iam_service-with-iam.html): Before you use IAM to manage access to AWS Cloud Map, learn what IAM features are available to use with AWS Cloud Map.
- [Identity-based policy examples](https://docs.aws.amazon.com/cloud-map/latest/dg/security_iam_id-based-policy-examples.html): By default, users and roles don't have permission to create or modify AWS Cloud Map resources.
- [AWS managed policies](https://docs.aws.amazon.com/cloud-map/latest/dg/security-iam-awsmanpol.html): Learn about AWS managed policies for AWS Cloud Map and recent changes to those policies.
- [AWS Cloud Map API permissions reference](https://docs.aws.amazon.com/cloud-map/latest/dg/cloud-map-api-permissions-ref.html): Learn about AWS Cloud Map API permissions.
- [Troubleshooting](https://docs.aws.amazon.com/cloud-map/latest/dg/security_iam_troubleshoot.html): Learn about how to troubleshoot identity and access for AWS Cloud Map.
- [Compliance Validation](https://docs.aws.amazon.com/cloud-map/latest/dg/cloud-map-compliance.html): Learn what AWS services are in scope of a specific compliance program.
- [Resilience](https://docs.aws.amazon.com/cloud-map/latest/dg/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and learn about specific AWS Cloud Map features for data resiliency.

### [Infrastructure Security](https://docs.aws.amazon.com/cloud-map/latest/dg/infrastructure-security.html)

Learn how AWS Cloud Map isolates service traffic.

- [AWS PrivateLink](https://docs.aws.amazon.com/cloud-map/latest/dg/vpc-interface-endpoints.html): You can use an AWS PrivateLink to create a private connection between your VPC and AWS Cloud Map.


## [Monitoring](https://docs.aws.amazon.com/cloud-map/latest/dg/monitoring-overview.html)

- [Log AWS Cloud Map API calls using AWS CloudTrail](https://docs.aws.amazon.com/cloud-map/latest/dg/logging-using-cloudtrail.html): Learn about logging AWS Cloud Map with AWS CloudTrail.


## [Tagging your resources](https://docs.aws.amazon.com/cloud-map/latest/dg/using-tags.html)

- [Updating tags for AWS Cloud Map resources](https://docs.aws.amazon.com/cloud-map/latest/dg/tag-resources-api-sdk.html): Learn how to update tags to AWS Cloud Map resources


## [Service quotas](https://docs.aws.amazon.com/cloud-map/latest/dg/cloud-map-limits.html)

- [Managing your service quotas](https://docs.aws.amazon.com/cloud-map/latest/dg/service-quotas-manage.html): Learn how to manage AWS Cloud Map service quotas using the AWS Management Console and the AWS CLI
- [Handle DiscoverInstances API request throttling](https://docs.aws.amazon.com/cloud-map/latest/dg/throttling.html): Learn about handling AWS Cloud Map API request throttling.
