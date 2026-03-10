# Source: https://docs.aws.amazon.com/vpc-lattice/latest/ug/llms.txt

# Amazon VPC Lattice User Guide

- [What is Amazon VPC Lattice?](https://docs.aws.amazon.com/vpc-lattice/latest/ug/what-is-vpc-lattice.html)
- [How VPC Lattice works](https://docs.aws.amazon.com/vpc-lattice/latest/ug/how-it-works.html)
- [Share VPC Lattice entities](https://docs.aws.amazon.com/vpc-lattice/latest/ug/sharing.html)
- [Quotas](https://docs.aws.amazon.com/vpc-lattice/latest/ug/quotas.html)
- [Document history](https://docs.aws.amazon.com/vpc-lattice/latest/ug/doc-history.html)

## [Service networks](https://docs.aws.amazon.com/vpc-lattice/latest/ug/service-networks.html)

- [Create a service network](https://docs.aws.amazon.com/vpc-lattice/latest/ug/create-service-network.html): Create a VPC Lattice service network.
- [Manage associations](https://docs.aws.amazon.com/vpc-lattice/latest/ug/service-network-associations.html): Associate a VPC Lattice service, a VPC, or a resource configuration with a VPC Lattice service network.
- [Edit access settings](https://docs.aws.amazon.com/vpc-lattice/latest/ug/service-network-access.html): Configure client access to a VPC Lattice service network.
- [Edit monitoring details](https://docs.aws.amazon.com/vpc-lattice/latest/ug/service-network-monitoring.html): Configure access logs for a VPC Lattice service network.
- [Manage tags](https://docs.aws.amazon.com/vpc-lattice/latest/ug/service-network-tags.html): Add or remove tags for a VPC Lattice service network.
- [Delete a service network](https://docs.aws.amazon.com/vpc-lattice/latest/ug/delete-service-network.html): Delete a VPC Lattice service network.


## [Services](https://docs.aws.amazon.com/vpc-lattice/latest/ug/services.html)

- [Manage associations](https://docs.aws.amazon.com/vpc-lattice/latest/ug/service-associations.html): Associate a VPC Lattice service with a VPC Lattice service network.
- [Edit access settings](https://docs.aws.amazon.com/vpc-lattice/latest/ug/service-access.html): Configure client access to a VPC Lattice service.
- [Edit monitoring details](https://docs.aws.amazon.com/vpc-lattice/latest/ug/service-monitoring.html): Configure access logs for a VPC Lattice service.
- [Manage tags](https://docs.aws.amazon.com/vpc-lattice/latest/ug/service-tags.html): Add or remove tags for a VPC Lattice service.
- [Configure a custom domain name](https://docs.aws.amazon.com/vpc-lattice/latest/ug/service-custom-domain-name.html): Provide a domain name for your VPC Lattice service that is easy for users to remember.
- [BYOC](https://docs.aws.amazon.com/vpc-lattice/latest/ug/service-byoc.html): Learn about the requirements for certificates used with VPC Lattice custom domain names.
- [Delete a service](https://docs.aws.amazon.com/vpc-lattice/latest/ug/delete-service.html): Delete a VPC Lattice service.


## [Target groups](https://docs.aws.amazon.com/vpc-lattice/latest/ug/target-groups.html)

- [Create a target group](https://docs.aws.amazon.com/vpc-lattice/latest/ug/create-target-group.html): Create a target group for your service in VPC Lattice.
- [Register targets](https://docs.aws.amazon.com/vpc-lattice/latest/ug/register-targets.html): Learn how to add or remove targets from a target group for Amazon VPC Lattice.
- [Configure health checks](https://docs.aws.amazon.com/vpc-lattice/latest/ug/target-group-health-checks.html): Specify the health check settings for your target groups in VPC Lattice.
- [HTTP targets](https://docs.aws.amazon.com/vpc-lattice/latest/ug/http-targets.html): Understand the HTTP header fields that VPC Lattice adds to HTTP traffic.
- [Lambda functions as targets](https://docs.aws.amazon.com/vpc-lattice/latest/ug/lambda-functions.html): Register a Lambda function as a target with a service in VPC Lattice.
- [Application Load Balancers as targets](https://docs.aws.amazon.com/vpc-lattice/latest/ug/alb-target.html): Register an Application Load Balancer as the target of a VPC Lattice service.
- [Update tags](https://docs.aws.amazon.com/vpc-lattice/latest/ug/target-group-tags.html): Update the tags for your target groups in VPC Lattice.
- [Delete a target group](https://docs.aws.amazon.com/vpc-lattice/latest/ug/delete-target-group.html): Delete a target group for your service in VPC Lattice.


## [Listeners](https://docs.aws.amazon.com/vpc-lattice/latest/ug/listeners.html)

- [HTTP listeners](https://docs.aws.amazon.com/vpc-lattice/latest/ug/http-listeners.html): Add an HTTP listener for your service in VPC Lattice.
- [HTTPS listeners](https://docs.aws.amazon.com/vpc-lattice/latest/ug/https-listeners.html): Describes HTTPS listeners for your service in VPC Lattice.
- [TLS listeners](https://docs.aws.amazon.com/vpc-lattice/latest/ug/tls-listeners.html): Learn how to configure listeners for your VPC Lattice. service
- [Listener rules](https://docs.aws.amazon.com/vpc-lattice/latest/ug/listener-rules.html): Learn how to configure the rules that your VPC Lattice service uses to route requests.
- [Delete a listener](https://docs.aws.amazon.com/vpc-lattice/latest/ug/delete-listener.html): Delete a listener for your service in VPC Lattice.


## [VPC resources](https://docs.aws.amazon.com/vpc-lattice/latest/ug/vpc-resources.html)

### [Resource gateways](https://docs.aws.amazon.com/vpc-lattice/latest/ug/resource-gateway.html)

Create and configure a resource gateway within your VPC Lattice.

- [Create a resource gateway](https://docs.aws.amazon.com/vpc-lattice/latest/ug/create-resource-gateway.html): Create a VPC Lattice resource gateway.
- [Delete a resource gateway](https://docs.aws.amazon.com/vpc-lattice/latest/ug/delete-resource-gateway.html): You cannot delete a resource gateway as long as there are resource configurations associated with it.

### [Resource configurations](https://docs.aws.amazon.com/vpc-lattice/latest/ug/resource-configuration.html)

Create and configure your resource configurations within VPC Lattice.

- [Create and verify a domain](https://docs.aws.amazon.com/vpc-lattice/latest/ug/create-and-verify.html): Learn how to create a verify a custom domain name for VPC Lattice resource configurations.
- [Create a resource configuration](https://docs.aws.amazon.com/vpc-lattice/latest/ug/create-resource-configuration.html): Create a VPC Lattice resource configuration.
- [Manage associations](https://docs.aws.amazon.com/vpc-lattice/latest/ug/resource-configuration-associations.html): Manage the resource configuration associations.


## [VPC Lattice for Oracle Database@AWS](https://docs.aws.amazon.com/vpc-lattice/latest/ug/vpc-lattice-oci.html)

- [Oracle Cloud Infrastructure (OCI) Managed Backup to Amazon S3](https://docs.aws.amazon.com/vpc-lattice/latest/ug/vpc-lattice-oci-managed-backup.html): Use VPC Lattice, Oracle Database@AWS, and Amazon S3
- [Amazon S3 access](https://docs.aws.amazon.com/vpc-lattice/latest/ug/vpc-lattice-oci-s3-access.html): Use VPC Lattice, Oracle Database@AWS, and Amazon S3
- [Zero-ETL for Amazon Redshift](https://docs.aws.amazon.com/vpc-lattice/latest/ug/vpc-lattice-oci-zero-etl.html): Use VPC Lattice, Oracle Database@AWS, and Zero-ETL
- [Access and share VPC Lattice entities](https://docs.aws.amazon.com/vpc-lattice/latest/ug/vpc-lattice-oci-entities.html): Use VPC Lattice, Oracle Database@AWS, and other resources


## [Security](https://docs.aws.amazon.com/vpc-lattice/latest/ug/security.html)

### [Manage access to services](https://docs.aws.amazon.com/vpc-lattice/latest/ug/access-management-overview.html)

Manage access to your VPC Lattice services.

- [Auth policies](https://docs.aws.amazon.com/vpc-lattice/latest/ug/auth-policies.html): Control access to your VPC Lattice resources by using auth policies.
- [Security groups](https://docs.aws.amazon.com/vpc-lattice/latest/ug/security-groups.html): Control access to your resources by adding security groups to the VPC association that links a VPC to a service network.
- [Network ACLs](https://docs.aws.amazon.com/vpc-lattice/latest/ug/network-acls.html): Use network access control lists on your subnets to control traffic to and from VPC Lattice.
- [Authenticated requests](https://docs.aws.amazon.com/vpc-lattice/latest/ug/sigv4-authenticated-requests.html): Learn how to use Signature Version 4 (SIGv4) for authenticated requests to VPC Lattice.
- [Data protection](https://docs.aws.amazon.com/vpc-lattice/latest/ug/data-protection.html): Learn how the AWS shared responsibility model applies to data protection in VPC Lattice.

### [Identity and access management](https://docs.aws.amazon.com/vpc-lattice/latest/ug/security-iam.html)

In VPC Lattice, use IAM identity-based policies to control who can perform essential actions.

- [How Amazon VPC Lattice works with IAM](https://docs.aws.amazon.com/vpc-lattice/latest/ug/security_iam_service-with-iam.html): Understand about the IAM features that VPC Lattice supports.
- [API permissions](https://docs.aws.amazon.com/vpc-lattice/latest/ug/additional-api-permissions.html): Describes the permissions in VPC Lattice that you must grant IAM users to call specific API actions.
- [Identity-based policies](https://docs.aws.amazon.com/vpc-lattice/latest/ug/security_iam_id-based-policies.html): Learn how to use identity-based policies to grant users and roles access to VPC Lattice.
- [Using service-linked roles](https://docs.aws.amazon.com/vpc-lattice/latest/ug/using-service-linked-roles.html): Describes how to give VPC Lattice access to resources in your account by using service-linked roles.
- [AWS managed policies](https://docs.aws.amazon.com/vpc-lattice/latest/ug/managed-policies.html): Learn about VPC Lattice updates to AWS managed policies.
- [Compliance validation](https://docs.aws.amazon.com/vpc-lattice/latest/ug/compliance-validation.html): Learn what AWS services are in scope of a specific compliance program.
- [Privately access Lattice APIs](https://docs.aws.amazon.com/vpc-lattice/latest/ug/vpc-interface-endpoints.html): You can use an interface VPC endpoint to create a private connection between your VPC and Amazon VPC Lattice without requiring access over the internet or through a NAT device, a VPN connection, or an Direct Connect connection.
- [Resilience](https://docs.aws.amazon.com/vpc-lattice/latest/ug/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and learn about specific VPC Lattice features for data resiliency.
- [Infrastructure security](https://docs.aws.amazon.com/vpc-lattice/latest/ug/infrastructure-security.html): Learn how Amazon VPC Lattice isolates service traffic.


## [Monitoring](https://docs.aws.amazon.com/vpc-lattice/latest/ug/monitoring-overview.html)

- [CloudWatch metrics](https://docs.aws.amazon.com/vpc-lattice/latest/ug/monitoring-cloudwatch.html): Learn about the metrics that VPC Lattice sends to Amazon CloudWatch.
- [Access logs](https://docs.aws.amazon.com/vpc-lattice/latest/ug/monitoring-access-logs.html): Create an access log to capture information about IP traffic going to and from your service network.
- [CloudTrail logs](https://docs.aws.amazon.com/vpc-lattice/latest/ug/monitoring-cloudtrail.html): Capture detailed information about the calls made to VPC Lattice using AWS CloudTrail.
