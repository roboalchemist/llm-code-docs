# Source: https://docs.aws.amazon.com/vpc/latest/privatelink/llms.txt

# Amazon Virtual Private Cloud AWS PrivateLink

> Use AWS PrivateLink to connect your VPC to supported AWS services, services hosted by other AWS accounts, and supported AWS Marketplace partner services.

- [Get started](https://docs.aws.amazon.com/vpc/latest/privatelink/getting-started.html)
- [Access SaaS products](https://docs.aws.amazon.com/vpc/latest/privatelink/privatelink-access-saas.html)
- [CloudWatch metrics](https://docs.aws.amazon.com/vpc/latest/privatelink/privatelink-cloudwatch-metrics.html)
- [Quotas](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-limits-endpoints.html)
- [Document history](https://docs.aws.amazon.com/vpc/latest/privatelink/doc-history.html)

## [What is AWS PrivateLink?](https://docs.aws.amazon.com/vpc/latest/privatelink/what-is-privatelink.html)

- [Concepts](https://docs.aws.amazon.com/vpc/latest/privatelink/concepts.html): Use AWS PrivateLink to establish connectivity between the resources in your VPC private subnets and VPC endpoint services that are outside your VPC.


## [Access AWS services](https://docs.aws.amazon.com/vpc/latest/privatelink/privatelink-access-aws-services.html)

- [Services that integrate](https://docs.aws.amazon.com/vpc/latest/privatelink/aws-services-privatelink-support.html): Learn which AWS services integrate with AWS PrivateLink.
- [Cross-region enabled AWS services](https://docs.aws.amazon.com/vpc/latest/privatelink/aws-services-cross-region-privatelink-support.html): Learn which AWS services integrate with cross Region AWS PrivateLink.
- [Create an interface endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html): Learn how to create an interface VPC endpoint.
- [Configure an interface endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/interface-endpoints.html): Learn how to update the configuration of an interface VPC endpoint.
- [Receive alerts for interface endpoint events](https://docs.aws.amazon.com/vpc/latest/privatelink/manage-notifications-endpoint.html): Receive alerts for specific events related to your interface VPC endpoint.
- [Delete an interface endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/delete-interface-endpoint.html): Learn how to delete an interface VPC endpoint.

### [Gateway endpoints](https://docs.aws.amazon.com/vpc/latest/privatelink/gateway-endpoints.html)

Learn how to use gateway endpoints to connect to Amazon S3 and Amazon DynamoDB.

- [Endpoints for Amazon S3](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-s3.html): Use gateway endpoints to connect privately to Amazon S3.
- [Endpoints for DynamoDB](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-ddb.html): Use gateway endpoints to connect privately to Amazon DynamoDB.


## [Access virtual appliances](https://docs.aws.amazon.com/vpc/latest/privatelink/vpce-gateway-load-balancer.html)

- [Create a Gateway Load Balancer endpoint service](https://docs.aws.amazon.com/vpc/latest/privatelink/create-gateway-load-balancer-endpoint-service.html): Use AWS PrivateLink to establish secure, low-latency connections to virtual appliances.
- [Create a Gateway Load Balancer endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/gateway-load-balancer-endpoints.html): Learn how to create a Gateway Load Balancer endpoint.


## [Share your services](https://docs.aws.amazon.com/vpc/latest/privatelink/privatelink-share-your-services.html)

- [Create an endpoint service](https://docs.aws.amazon.com/vpc/latest/privatelink/create-endpoint-service.html): Learn how to create an endpoint service.
- [Configure an endpoint service](https://docs.aws.amazon.com/vpc/latest/privatelink/configure-endpoint-service.html): Learn how to update the configuration of an endpoint service.
- [Manage DNS names](https://docs.aws.amazon.com/vpc/latest/privatelink/manage-dns-names.html): Configure a private DNS name for your VPC endpoint service.
- [Receive alerts for endpoint service events](https://docs.aws.amazon.com/vpc/latest/privatelink/create-notification-endpoint-service.html): Receive alerts for specific events related to your VPC endpoint service.
- [Delete an endpoint service](https://docs.aws.amazon.com/vpc/latest/privatelink/delete-endpoint-service.html): Learn how to delete an endpoint service.


## [Access VPC resources](https://docs.aws.amazon.com/vpc/latest/privatelink/privatelink-access-resources.html)

- [Create a resource endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/use-resource-endpoint.html): Learn how to access a resource through a VPC endpoint of type resource.
- [Manage resource endpoints](https://docs.aws.amazon.com/vpc/latest/privatelink/manage-resource-endpoint.html): Learn how to manage a resource endpoint.

### [Resource configuration](https://docs.aws.amazon.com/vpc/latest/privatelink/resource-configuration.html)

Create and configure your resource configurations within VPC Lattice.

- [Create a resource configuration](https://docs.aws.amazon.com/vpc/latest/privatelink/create-resource-configuration.html): Create a VPC Lattice resource configuration.
- [Manage associations](https://docs.aws.amazon.com/vpc/latest/privatelink/resource-configuration-associations.html): Manage the resource configuration associations.

### [Resource gateway](https://docs.aws.amazon.com/vpc/latest/privatelink/resource-gateway.html)

Create and configure your resource gateway within VPC Lattice.

- [Create a resource gateway](https://docs.aws.amazon.com/vpc/latest/privatelink/create-resource-gateway.html): Create a VPC Lattice resource gateway.
- [Delete a resource gateway](https://docs.aws.amazon.com/vpc/latest/privatelink/delete-resource-gateway.html): You cannot delete a resource gateway as long as there are resource configurations associated with it.


## [Access service networks](https://docs.aws.amazon.com/vpc/latest/privatelink/privatelink-access-service-networks.html)

- [Create a service-network endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/access-with-service-network-endpoint.html): Learn how to access a service network using a service-network endpoint.
- [Manage service-network endpoints](https://docs.aws.amazon.com/vpc/latest/privatelink/manage-sn-endpoint.html): Learn how to manage a service-network endpoint.


## [Identity and access management](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-iam.html)

- [How AWS PrivateLink works with IAM](https://docs.aws.amazon.com/vpc/latest/privatelink/security_iam_service-with-iam.html): Learn which IAM features are available to use with AWS PrivateLink.
- [Identity-based policy examples](https://docs.aws.amazon.com/vpc/latest/privatelink/security_iam_id-based-policy-examples.html): Control the creation and configuration of VPC endpoints by users and roles.
- [Endpoint policies](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-access.html): Control which principals can perform which operations on a VPC endpoint.
- [AWS managed policies](https://docs.aws.amazon.com/vpc/latest/privatelink/security-iam-awsmanpol.html): Learn about AWS managed policies for AWS PrivateLink and recent changes to those policies.
