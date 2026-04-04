# Source: https://docs.aws.amazon.com/cloud-map/latest/api/llms.txt

# AWS Cloud Map API Reference

> With AWS Cloud Map, you can configure public DNS, private DNS, or HTTP namespaces that your microservice applications run in. When an instance becomes available, you can call the AWS Cloud Map API to register the instance with AWS Cloud Map. For public or private DNS namespaces, AWS Cloud Map automatically creates DNS records and an optional health check. Clients that submit public or private DNS queries, or HTTP requests, for the service receive an answer that contains up to eight healthy records.

- [Welcome](https://docs.aws.amazon.com/cloud-map/latest/api/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/cloud-map/latest/api/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/cloud-map/latest/api/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/cloud-map/latest/api/API_Operations.html)

- [CreateHttpNamespace](https://docs.aws.amazon.com/cloud-map/latest/api/API_CreateHttpNamespace.html): Creates an HTTP namespace.
- [CreatePrivateDnsNamespace](https://docs.aws.amazon.com/cloud-map/latest/api/API_CreatePrivateDnsNamespace.html): Creates a private namespace based on DNS, which is visible only inside a specified Amazon VPC.
- [CreatePublicDnsNamespace](https://docs.aws.amazon.com/cloud-map/latest/api/API_CreatePublicDnsNamespace.html): Creates a public namespace based on DNS, which is visible on the internet.
- [CreateService](https://docs.aws.amazon.com/cloud-map/latest/api/API_CreateService.html): Creates a service.
- [DeleteNamespace](https://docs.aws.amazon.com/cloud-map/latest/api/API_DeleteNamespace.html): Deletes a namespace from the current account.
- [DeleteService](https://docs.aws.amazon.com/cloud-map/latest/api/API_DeleteService.html): Deletes a specified service and all associated service attributes.
- [DeleteServiceAttributes](https://docs.aws.amazon.com/cloud-map/latest/api/API_DeleteServiceAttributes.html): Deletes specific attributes associated with a service.
- [DeregisterInstance](https://docs.aws.amazon.com/cloud-map/latest/api/API_DeregisterInstance.html): Deletes the Amazon RouteÂ 53 DNS records and health check, if any, that AWS Cloud Map created for the specified instance.
- [DiscoverInstances](https://docs.aws.amazon.com/cloud-map/latest/api/API_DiscoverInstances.html): Discovers registered instances for a specified namespace and service.
- [DiscoverInstancesRevision](https://docs.aws.amazon.com/cloud-map/latest/api/API_DiscoverInstancesRevision.html): Discovers the increasing revision associated with an instance.
- [GetInstance](https://docs.aws.amazon.com/cloud-map/latest/api/API_GetInstance.html): Gets information about a specified instance.
- [GetInstancesHealthStatus](https://docs.aws.amazon.com/cloud-map/latest/api/API_GetInstancesHealthStatus.html): Gets the current health status (Healthy, Unhealthy, or Unknown) of one or more instances that are associated with a specified service.
- [GetNamespace](https://docs.aws.amazon.com/cloud-map/latest/api/API_GetNamespace.html): Gets information about a namespace.
- [GetOperation](https://docs.aws.amazon.com/cloud-map/latest/api/API_GetOperation.html): Gets information about any operation that returns an operation ID in the response, such as a CreateHttpNamespace request.
- [GetService](https://docs.aws.amazon.com/cloud-map/latest/api/API_GetService.html): Gets the settings for a specified service.
- [GetServiceAttributes](https://docs.aws.amazon.com/cloud-map/latest/api/API_GetServiceAttributes.html): Returns the attributes associated with a specified service.
- [ListInstances](https://docs.aws.amazon.com/cloud-map/latest/api/API_ListInstances.html): Lists summary information about the instances that you registered by using a specified service.
- [ListNamespaces](https://docs.aws.amazon.com/cloud-map/latest/api/API_ListNamespaces.html): Lists summary information about the namespaces that were created by the current AWS account and shared with the current AWS account.
- [ListOperations](https://docs.aws.amazon.com/cloud-map/latest/api/API_ListOperations.html): Lists operations that match the criteria that you specify.
- [ListServices](https://docs.aws.amazon.com/cloud-map/latest/api/API_ListServices.html): Lists summary information for all the services that are associated with one or more namespaces.
- [ListTagsForResource](https://docs.aws.amazon.com/cloud-map/latest/api/API_ListTagsForResource.html): Lists tags for the specified resource.
- [RegisterInstance](https://docs.aws.amazon.com/cloud-map/latest/api/API_RegisterInstance.html): Creates or updates one or more records and, optionally, creates a health check based on the settings in a specified service.
- [TagResource](https://docs.aws.amazon.com/cloud-map/latest/api/API_TagResource.html): Adds one or more tags to the specified resource.
- [UntagResource](https://docs.aws.amazon.com/cloud-map/latest/api/API_UntagResource.html): Removes one or more tags from the specified resource.
- [UpdateHttpNamespace](https://docs.aws.amazon.com/cloud-map/latest/api/API_UpdateHttpNamespace.html): Updates an HTTP namespace.
- [UpdateInstanceCustomHealthStatus](https://docs.aws.amazon.com/cloud-map/latest/api/API_UpdateInstanceCustomHealthStatus.html): Submits a request to change the health status of a custom health check to healthy or unhealthy.
- [UpdatePrivateDnsNamespace](https://docs.aws.amazon.com/cloud-map/latest/api/API_UpdatePrivateDnsNamespace.html): Updates a private DNS namespace.
- [UpdatePublicDnsNamespace](https://docs.aws.amazon.com/cloud-map/latest/api/API_UpdatePublicDnsNamespace.html): Updates a public DNS namespace.
- [UpdateService](https://docs.aws.amazon.com/cloud-map/latest/api/API_UpdateService.html): Submits a request to perform the following operations:
- [UpdateServiceAttributes](https://docs.aws.amazon.com/cloud-map/latest/api/API_UpdateServiceAttributes.html): Submits a request to update a specified service to add service-level attributes.


## [Data Types](https://docs.aws.amazon.com/cloud-map/latest/api/API_Types.html)

- [DnsConfig](https://docs.aws.amazon.com/cloud-map/latest/api/API_DnsConfig.html): A complex type that contains information about the Amazon RouteÂ 53 DNS records that you want AWS Cloud Map to create when you register an instance.
- [DnsConfigChange](https://docs.aws.amazon.com/cloud-map/latest/api/API_DnsConfigChange.html): A complex type that contains information about changes to the RouteÂ 53 DNS records that AWS Cloud Map creates when you register an instance.
- [DnsProperties](https://docs.aws.amazon.com/cloud-map/latest/api/API_DnsProperties.html): A complex type that contains the ID for the RouteÂ 53 hosted zone that AWS Cloud Map creates when you create a namespace.
- [DnsRecord](https://docs.aws.amazon.com/cloud-map/latest/api/API_DnsRecord.html): A complex type that contains information about the RouteÂ 53 DNS records that you want AWS Cloud Map to create when you register an instance.
- [HealthCheckConfig](https://docs.aws.amazon.com/cloud-map/latest/api/API_HealthCheckConfig.html): Public DNS and HTTP namespaces only.
- [HealthCheckCustomConfig](https://docs.aws.amazon.com/cloud-map/latest/api/API_HealthCheckCustomConfig.html): A complex type that contains information about an optional custom health check.
- [HttpInstanceSummary](https://docs.aws.amazon.com/cloud-map/latest/api/API_HttpInstanceSummary.html): In a response to a DiscoverInstances request, HttpInstanceSummary contains information about one instance that matches the values that you specified in the request.
- [HttpNamespaceChange](https://docs.aws.amazon.com/cloud-map/latest/api/API_HttpNamespaceChange.html): Updated properties for the HTTP namespace.
- [HttpProperties](https://docs.aws.amazon.com/cloud-map/latest/api/API_HttpProperties.html): A complex type that contains the name of an HTTP namespace.
- [Instance](https://docs.aws.amazon.com/cloud-map/latest/api/API_Instance.html): A complex type that contains information about an instance that AWS Cloud Map creates when you submit a RegisterInstance request.
- [InstanceSummary](https://docs.aws.amazon.com/cloud-map/latest/api/API_InstanceSummary.html): A complex type that contains information about the instances that you registered by using a specified service.
- [Namespace](https://docs.aws.amazon.com/cloud-map/latest/api/API_Namespace.html): A complex type that contains information about a specified namespace.
- [NamespaceFilter](https://docs.aws.amazon.com/cloud-map/latest/api/API_NamespaceFilter.html): A complex type that identifies the namespaces that you want to list.
- [NamespaceProperties](https://docs.aws.amazon.com/cloud-map/latest/api/API_NamespaceProperties.html): A complex type that contains information that's specific to the namespace type.
- [NamespaceSummary](https://docs.aws.amazon.com/cloud-map/latest/api/API_NamespaceSummary.html): A complex type that contains information about a namespace.
- [Operation](https://docs.aws.amazon.com/cloud-map/latest/api/API_Operation.html): A complex type that contains information about a specified operation.
- [OperationFilter](https://docs.aws.amazon.com/cloud-map/latest/api/API_OperationFilter.html): A complex type that lets you select the operations that you want to list.
- [OperationSummary](https://docs.aws.amazon.com/cloud-map/latest/api/API_OperationSummary.html): A complex type that contains information about an operation that matches the criteria that you specified in a ListOperations request.
- [PrivateDnsNamespaceChange](https://docs.aws.amazon.com/cloud-map/latest/api/API_PrivateDnsNamespaceChange.html): Updated properties for the private DNS namespace.
- [PrivateDnsNamespaceProperties](https://docs.aws.amazon.com/cloud-map/latest/api/API_PrivateDnsNamespaceProperties.html): DNS properties for the private DNS namespace.
- [PrivateDnsNamespacePropertiesChange](https://docs.aws.amazon.com/cloud-map/latest/api/API_PrivateDnsNamespacePropertiesChange.html): Updated properties for the private DNS namespace.
- [PrivateDnsPropertiesMutable](https://docs.aws.amazon.com/cloud-map/latest/api/API_PrivateDnsPropertiesMutable.html): DNS properties for the private DNS namespace.
- [PrivateDnsPropertiesMutableChange](https://docs.aws.amazon.com/cloud-map/latest/api/API_PrivateDnsPropertiesMutableChange.html): Updated DNS properties for the private DNS namespace.
- [PublicDnsNamespaceChange](https://docs.aws.amazon.com/cloud-map/latest/api/API_PublicDnsNamespaceChange.html): Updated properties for the public DNS namespace.
- [PublicDnsNamespaceProperties](https://docs.aws.amazon.com/cloud-map/latest/api/API_PublicDnsNamespaceProperties.html): DNS properties for the public DNS namespace.
- [PublicDnsNamespacePropertiesChange](https://docs.aws.amazon.com/cloud-map/latest/api/API_PublicDnsNamespacePropertiesChange.html): Updated properties for the public DNS namespace.
- [PublicDnsPropertiesMutable](https://docs.aws.amazon.com/cloud-map/latest/api/API_PublicDnsPropertiesMutable.html): DNS properties for the public DNS namespace.
- [PublicDnsPropertiesMutableChange](https://docs.aws.amazon.com/cloud-map/latest/api/API_PublicDnsPropertiesMutableChange.html): Updated DNS properties for the public DNS namespace.
- [Service](https://docs.aws.amazon.com/cloud-map/latest/api/API_Service.html): A complex type that contains information about the specified service.
- [ServiceAttributes](https://docs.aws.amazon.com/cloud-map/latest/api/API_ServiceAttributes.html): A complex type that contains information about attributes associated with a specific service.
- [ServiceChange](https://docs.aws.amazon.com/cloud-map/latest/api/API_ServiceChange.html): A complex type that contains changes to an existing service.
- [ServiceFilter](https://docs.aws.amazon.com/cloud-map/latest/api/API_ServiceFilter.html): A complex type that lets you specify the namespaces that you want to list services for.
- [ServiceSummary](https://docs.aws.amazon.com/cloud-map/latest/api/API_ServiceSummary.html): A complex type that contains information about a specified service.
- [SOA](https://docs.aws.amazon.com/cloud-map/latest/api/API_SOA.html): Start of Authority (SOA) properties for a public or private DNS namespace.
- [SOAChange](https://docs.aws.amazon.com/cloud-map/latest/api/API_SOAChange.html): Updated Start of Authority (SOA) properties for a public or private DNS namespace.
- [Tag](https://docs.aws.amazon.com/cloud-map/latest/api/API_Tag.html): A custom key-value pair that's associated with a resource.
