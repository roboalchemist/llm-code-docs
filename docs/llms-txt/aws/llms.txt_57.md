# Source: https://docs.aws.amazon.com/Route53/latest/APIReference/llms.txt

# Amazon RouteÂ 53 API Reference

> Amazon RouteÂ 53 is a highly available and scalable Domain Name System (DNS) web service.

- [Welcome](https://docs.aws.amazon.com/Route53/latest/APIReference/Welcome.html)
- [Amazon RouteÂ 53 API actions by function](https://docs.aws.amazon.com/Route53/latest/APIReference/API-actions-by-function.html)
- [Traffic Policy Document Format](https://docs.aws.amazon.com/Route53/latest/APIReference/api-policies-traffic-policy-document-format.html)
- [Common Parameters](https://docs.aws.amazon.com/Route53/latest/APIReference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/Route53/latest/APIReference/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/Route53/latest/APIReference/API_Operations.html)

### [Amazon RouteÂ 53](https://docs.aws.amazon.com/Route53/latest/APIReference/API_Operations_Amazon_Route_53.html)

The following actions are supported by Amazon RouteÂ 53:

- [ActivateKeySigningKey](https://docs.aws.amazon.com/Route53/latest/APIReference/API_ActivateKeySigningKey.html): Activates a key-signing key (KSK) so that it can be used for signing by DNSSEC.
- [AssociateVPCWithHostedZone](https://docs.aws.amazon.com/Route53/latest/APIReference/API_AssociateVPCWithHostedZone.html): Associates an Amazon VPC with a private hosted zone.
- [ChangeCidrCollection](https://docs.aws.amazon.com/Route53/latest/APIReference/API_ChangeCidrCollection.html): Creates, changes, or deletes CIDR blocks within a collection.
- [ChangeResourceRecordSets](https://docs.aws.amazon.com/Route53/latest/APIReference/API_ChangeResourceRecordSets.html): Creates, changes, or deletes a resource record set, which contains authoritative DNS information for a specified domain name or subdomain name.
- [ChangeTagsForResource](https://docs.aws.amazon.com/Route53/latest/APIReference/API_ChangeTagsForResource.html): Adds, edits, or deletes tags for a health check or a hosted zone.
- [CreateCidrCollection](https://docs.aws.amazon.com/Route53/latest/APIReference/API_CreateCidrCollection.html): Creates a CIDR collection in the current AWS account.
- [CreateHealthCheck](https://docs.aws.amazon.com/Route53/latest/APIReference/API_CreateHealthCheck.html): Creates a new health check.
- [CreateHostedZone](https://docs.aws.amazon.com/Route53/latest/APIReference/API_CreateHostedZone.html): Creates a new public or private hosted zone.
- [CreateKeySigningKey](https://docs.aws.amazon.com/Route53/latest/APIReference/API_CreateKeySigningKey.html): Creates a new key-signing key (KSK) associated with a hosted zone.
- [CreateQueryLoggingConfig](https://docs.aws.amazon.com/Route53/latest/APIReference/API_CreateQueryLoggingConfig.html): Creates a configuration for DNS query logging.
- [CreateReusableDelegationSet](https://docs.aws.amazon.com/Route53/latest/APIReference/API_CreateReusableDelegationSet.html): Creates a delegation set (a group of four name servers) that can be reused by multiple hosted zones that were created by the same AWS account.
- [CreateTrafficPolicy](https://docs.aws.amazon.com/Route53/latest/APIReference/API_CreateTrafficPolicy.html): Creates a traffic policy, which you use to create multiple DNS resource record sets for one domain name (such as example.com) or one subdomain name (such as www.example.com).
- [CreateTrafficPolicyInstance](https://docs.aws.amazon.com/Route53/latest/APIReference/API_CreateTrafficPolicyInstance.html): Creates resource record sets in a specified hosted zone based on the settings in a specified traffic policy version.
- [CreateTrafficPolicyVersion](https://docs.aws.amazon.com/Route53/latest/APIReference/API_CreateTrafficPolicyVersion.html): Creates a new version of an existing traffic policy.
- [CreateVPCAssociationAuthorization](https://docs.aws.amazon.com/Route53/latest/APIReference/API_CreateVPCAssociationAuthorization.html): Authorizes the AWS account that created a specified VPC to submit an AssociateVPCWithHostedZone request to associate the VPC with a specified hosted zone that was created by a different account.
- [DeactivateKeySigningKey](https://docs.aws.amazon.com/Route53/latest/APIReference/API_DeactivateKeySigningKey.html): Deactivates a key-signing key (KSK) so that it will not be used for signing by DNSSEC.
- [DeleteCidrCollection](https://docs.aws.amazon.com/Route53/latest/APIReference/API_DeleteCidrCollection.html): Deletes a CIDR collection in the current AWS account.
- [DeleteHealthCheck](https://docs.aws.amazon.com/Route53/latest/APIReference/API_DeleteHealthCheck.html): Deletes a health check.
- [DeleteHostedZone](https://docs.aws.amazon.com/Route53/latest/APIReference/API_DeleteHostedZone.html): Deletes a hosted zone.
- [DeleteKeySigningKey](https://docs.aws.amazon.com/Route53/latest/APIReference/API_DeleteKeySigningKey.html): Deletes a key-signing key (KSK).
- [DeleteQueryLoggingConfig](https://docs.aws.amazon.com/Route53/latest/APIReference/API_DeleteQueryLoggingConfig.html): Deletes a configuration for DNS query logging.
- [DeleteReusableDelegationSet](https://docs.aws.amazon.com/Route53/latest/APIReference/API_DeleteReusableDelegationSet.html): Deletes a reusable delegation set.
- [DeleteTrafficPolicy](https://docs.aws.amazon.com/Route53/latest/APIReference/API_DeleteTrafficPolicy.html): Deletes a traffic policy.
- [DeleteTrafficPolicyInstance](https://docs.aws.amazon.com/Route53/latest/APIReference/API_DeleteTrafficPolicyInstance.html): Deletes a traffic policy instance and all of the resource record sets that Amazon Route 53 created when you created the instance.
- [DeleteVPCAssociationAuthorization](https://docs.aws.amazon.com/Route53/latest/APIReference/API_DeleteVPCAssociationAuthorization.html): Removes authorization to submit an AssociateVPCWithHostedZone request to associate a specified VPC with a hosted zone that was created by a different account.
- [DisableHostedZoneDNSSEC](https://docs.aws.amazon.com/Route53/latest/APIReference/API_DisableHostedZoneDNSSEC.html): Disables DNSSEC signing in a specific hosted zone.
- [DisassociateVPCFromHostedZone](https://docs.aws.amazon.com/Route53/latest/APIReference/API_DisassociateVPCFromHostedZone.html): Disassociates an Amazon Virtual Private Cloud (Amazon VPC) from an Amazon Route 53 private hosted zone.
- [EnableHostedZoneDNSSEC](https://docs.aws.amazon.com/Route53/latest/APIReference/API_EnableHostedZoneDNSSEC.html): Enables DNSSEC signing in a specific hosted zone.
- [GetAccountLimit](https://docs.aws.amazon.com/Route53/latest/APIReference/API_GetAccountLimit.html): Gets the specified limit for the current account, for example, the maximum number of health checks that you can create using the account.
- [GetChange](https://docs.aws.amazon.com/Route53/latest/APIReference/API_GetChange.html): Returns the current status of a change batch request.
- [GetCheckerIpRanges](https://docs.aws.amazon.com/Route53/latest/APIReference/API_GetCheckerIpRanges.html): Route 53 does not perform authorization for this API because it retrieves information that is already available to the public.
- [GetDNSSEC](https://docs.aws.amazon.com/Route53/latest/APIReference/API_GetDNSSEC.html): Returns information about DNSSEC for a specific hosted zone, including the key-signing keys (KSKs) in the hosted zone.
- [GetGeoLocation](https://docs.aws.amazon.com/Route53/latest/APIReference/API_GetGeoLocation.html): Gets information about whether a specified geographic location is supported for Amazon Route 53 geolocation resource record sets.
- [GetHealthCheck](https://docs.aws.amazon.com/Route53/latest/APIReference/API_GetHealthCheck.html): Gets information about a specified health check.
- [GetHealthCheckCount](https://docs.aws.amazon.com/Route53/latest/APIReference/API_GetHealthCheckCount.html): Retrieves the number of health checks that are associated with the current AWS account.
- [GetHealthCheckLastFailureReason](https://docs.aws.amazon.com/Route53/latest/APIReference/API_GetHealthCheckLastFailureReason.html): Gets the reason that a specified health check failed most recently.
- [GetHealthCheckStatus](https://docs.aws.amazon.com/Route53/latest/APIReference/API_GetHealthCheckStatus.html): Gets status of a specified health check.
- [GetHostedZone](https://docs.aws.amazon.com/Route53/latest/APIReference/API_GetHostedZone.html): Gets information about a specified hosted zone including the four name servers assigned to the hosted zone.
- [GetHostedZoneCount](https://docs.aws.amazon.com/Route53/latest/APIReference/API_GetHostedZoneCount.html): Retrieves the number of hosted zones that are associated with the current AWS account.
- [GetHostedZoneLimit](https://docs.aws.amazon.com/Route53/latest/APIReference/API_GetHostedZoneLimit.html): Gets the specified limit for a specified hosted zone, for example, the maximum number of records that you can create in the hosted zone.
- [GetQueryLoggingConfig](https://docs.aws.amazon.com/Route53/latest/APIReference/API_GetQueryLoggingConfig.html): Gets information about a specified configuration for DNS query logging.
- [GetReusableDelegationSet](https://docs.aws.amazon.com/Route53/latest/APIReference/API_GetReusableDelegationSet.html): Retrieves information about a specified reusable delegation set, including the four name servers that are assigned to the delegation set.
- [GetReusableDelegationSetLimit](https://docs.aws.amazon.com/Route53/latest/APIReference/API_GetReusableDelegationSetLimit.html): Gets the maximum number of hosted zones that you can associate with the specified reusable delegation set.
- [GetTrafficPolicy](https://docs.aws.amazon.com/Route53/latest/APIReference/API_GetTrafficPolicy.html): Gets information about a specific traffic policy version.
- [GetTrafficPolicyInstance](https://docs.aws.amazon.com/Route53/latest/APIReference/API_GetTrafficPolicyInstance.html): Gets information about a specified traffic policy instance.
- [GetTrafficPolicyInstanceCount](https://docs.aws.amazon.com/Route53/latest/APIReference/API_GetTrafficPolicyInstanceCount.html): Gets the number of traffic policy instances that are associated with the current AWS account.
- [ListCidrBlocks](https://docs.aws.amazon.com/Route53/latest/APIReference/API_ListCidrBlocks.html): Returns a paginated list of location objects and their CIDR blocks.
- [ListCidrCollections](https://docs.aws.amazon.com/Route53/latest/APIReference/API_ListCidrCollections.html): Returns a paginated list of CIDR collections in the AWS account (metadata only).
- [ListCidrLocations](https://docs.aws.amazon.com/Route53/latest/APIReference/API_ListCidrLocations.html): Returns a paginated list of CIDR locations for the given collection (metadata only, does not include CIDR blocks).
- [ListGeoLocations](https://docs.aws.amazon.com/Route53/latest/APIReference/API_ListGeoLocations.html): Retrieves a list of supported geographic locations.
- [ListHealthChecks](https://docs.aws.amazon.com/Route53/latest/APIReference/API_ListHealthChecks.html): Retrieve a list of the health checks that are associated with the current AWS account.
- [ListHostedZones](https://docs.aws.amazon.com/Route53/latest/APIReference/API_ListHostedZones.html): Retrieves a list of the public and private hosted zones that are associated with the current AWS account.
- [ListHostedZonesByName](https://docs.aws.amazon.com/Route53/latest/APIReference/API_ListHostedZonesByName.html): Retrieves a list of your hosted zones in lexicographic order.
- [ListHostedZonesByVPC](https://docs.aws.amazon.com/Route53/latest/APIReference/API_ListHostedZonesByVPC.html): Lists all the private hosted zones that a specified VPC is associated with, regardless of which AWS account or AWS service owns the hosted zones.
- [ListQueryLoggingConfigs](https://docs.aws.amazon.com/Route53/latest/APIReference/API_ListQueryLoggingConfigs.html): Lists the configurations for DNS query logging that are associated with the current AWS account or the configuration that is associated with a specified hosted zone.
- [ListResourceRecordSets](https://docs.aws.amazon.com/Route53/latest/APIReference/API_ListResourceRecordSets.html): Lists the resource record sets in a specified hosted zone.
- [ListReusableDelegationSets](https://docs.aws.amazon.com/Route53/latest/APIReference/API_ListReusableDelegationSets.html): Retrieves a list of the reusable delegation sets that are associated with the current AWS account.
- [ListTagsForResource](https://docs.aws.amazon.com/Route53/latest/APIReference/API_ListTagsForResource.html): Lists tags for one health check or hosted zone.
- [ListTagsForResources](https://docs.aws.amazon.com/Route53/latest/APIReference/API_ListTagsForResources.html): Lists tags for up to 10 health checks or hosted zones.
- [ListTrafficPolicies](https://docs.aws.amazon.com/Route53/latest/APIReference/API_ListTrafficPolicies.html): Gets information about the latest version for every traffic policy that is associated with the current AWS account.
- [ListTrafficPolicyInstances](https://docs.aws.amazon.com/Route53/latest/APIReference/API_ListTrafficPolicyInstances.html): Gets information about the traffic policy instances that you created by using the current AWS account.
- [ListTrafficPolicyInstancesByHostedZone](https://docs.aws.amazon.com/Route53/latest/APIReference/API_ListTrafficPolicyInstancesByHostedZone.html): Gets information about the traffic policy instances that you created in a specified hosted zone.
- [ListTrafficPolicyInstancesByPolicy](https://docs.aws.amazon.com/Route53/latest/APIReference/API_ListTrafficPolicyInstancesByPolicy.html): Gets information about the traffic policy instances that you created by using a specify traffic policy version.
- [ListTrafficPolicyVersions](https://docs.aws.amazon.com/Route53/latest/APIReference/API_ListTrafficPolicyVersions.html): Gets information about all of the versions for a specified traffic policy.
- [ListVPCAssociationAuthorizations](https://docs.aws.amazon.com/Route53/latest/APIReference/API_ListVPCAssociationAuthorizations.html): Gets a list of the VPCs that were created by other accounts and that can be associated with a specified hosted zone because you've submitted one or more CreateVPCAssociationAuthorization requests.
- [TestDNSAnswer](https://docs.aws.amazon.com/Route53/latest/APIReference/API_TestDNSAnswer.html): Gets the value that Amazon Route 53 returns in response to a DNS request for a specified record name and type.
- [UpdateHealthCheck](https://docs.aws.amazon.com/Route53/latest/APIReference/API_UpdateHealthCheck.html): Updates an existing health check.
- [UpdateHostedZoneComment](https://docs.aws.amazon.com/Route53/latest/APIReference/API_UpdateHostedZoneComment.html): Updates the comment for a specified hosted zone.
- [UpdateHostedZoneFeatures](https://docs.aws.amazon.com/Route53/latest/APIReference/API_UpdateHostedZoneFeatures.html): Updates the features configuration for a hosted zone.
- [UpdateTrafficPolicyComment](https://docs.aws.amazon.com/Route53/latest/APIReference/API_UpdateTrafficPolicyComment.html): Updates the comment for a specified traffic policy version.
- [UpdateTrafficPolicyInstance](https://docs.aws.amazon.com/Route53/latest/APIReference/API_UpdateTrafficPolicyInstance.html)

### [Amazon RouteÂ 53 domain registration](https://docs.aws.amazon.com/Route53/latest/APIReference/API_Operations_Amazon_Route_53_Domains.html)

The following actions are supported by Amazon RouteÂ 53 domain registration:

- [AcceptDomainTransferFromAnotherAwsAccount](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_AcceptDomainTransferFromAnotherAwsAccount.html): Accepts the transfer of a domain from another AWS account to the currentAWS account.
- [AssociateDelegationSignerToDomain](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_AssociateDelegationSignerToDomain.html): Creates a delegation signer (DS) record in the registry zone for this domain name.
- [CancelDomainTransferToAnotherAwsAccount](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_CancelDomainTransferToAnotherAwsAccount.html): Cancels the transfer of a domain from the current AWS account to another AWS account.
- [CheckDomainAvailability](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_CheckDomainAvailability.html): This operation checks the availability of one domain name.
- [CheckDomainTransferability](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_CheckDomainTransferability.html): Checks whether a domain name can be transferred to Amazon Route 53.
- [DeleteDomain](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_DeleteDomain.html): This operation deletes the specified domain.
- [DeleteTagsForDomain](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_DeleteTagsForDomain.html): This operation deletes the specified tags for a domain.
- [DisableDomainAutoRenew](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_DisableDomainAutoRenew.html): This operation disables automatic renewal of domain registration for the specified domain.
- [DisableDomainTransferLock](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_DisableDomainTransferLock.html): This operation removes the transfer lock on the domain (specifically the clientTransferProhibited status) to allow domain transfers.
- [DisassociateDelegationSignerFromDomain](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_DisassociateDelegationSignerFromDomain.html): Deletes a delegation signer (DS) record in the registry zone for this domain name.
- [EnableDomainAutoRenew](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_EnableDomainAutoRenew.html): This operation configures Amazon Route 53 to automatically renew the specified domain before the domain registration expires.
- [EnableDomainTransferLock](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_EnableDomainTransferLock.html): This operation sets the transfer lock on the domain (specifically the clientTransferProhibited status) to prevent domain transfers.
- [GetContactReachabilityStatus](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_GetContactReachabilityStatus.html): For operations that require confirmation that the email address for the registrant contact is valid, such as registering a new domain, this operation returns information about whether the registrant contact has responded.
- [GetDomainDetail](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_GetDomainDetail.html): This operation returns detailed information about a specified domain that is associated with the current AWS account.
- [GetDomainSuggestions](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_GetDomainSuggestions.html): The GetDomainSuggestions operation returns a list of suggested domain names.
- [GetOperationDetail](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_GetOperationDetail.html): This operation returns the current status of an operation that is not completed.
- [ListDomains](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_ListDomains.html): This operation returns all the domain names registered with Amazon Route 53 for the current AWS account if no filtering conditions are used.
- [ListOperations](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_ListOperations.html): Returns information about all of the operations that return an operation ID and that have ever been performed on domains that were registered by the current account.
- [ListPrices](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_ListPrices.html): Lists the following prices for either all the TLDs supported by RouteÂ 53, or the specified TLD:
- [ListTagsForDomain](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_ListTagsForDomain.html): This operation returns all of the tags that are associated with the specified domain.
- [PushDomain](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_PushDomain.html): Moves a domain from AWS to another registrar.
- [RegisterDomain](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_RegisterDomain.html): This operation registers a domain.
- [RejectDomainTransferFromAnotherAwsAccount](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_RejectDomainTransferFromAnotherAwsAccount.html): Rejects the transfer of a domain from another AWS account to the current AWS account.
- [RenewDomain](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_RenewDomain.html): This operation renews a domain for the specified number of years.
- [ResendContactReachabilityEmail](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_ResendContactReachabilityEmail.html): For operations that require confirmation that the email address for the registrant contact is valid, such as registering a new domain, this operation resends the confirmation email to the current email address for the registrant contact.
- [ResendOperationAuthorization](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_ResendOperationAuthorization.html): Resend the form of authorization email for this operation.
- [RetrieveDomainAuthCode](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_RetrieveDomainAuthCode.html): This operation returns the authorization code for the domain.
- [TransferDomain](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_TransferDomain.html): Transfers a domain from another registrar to Amazon Route 53.
- [TransferDomainToAnotherAwsAccount](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_TransferDomainToAnotherAwsAccount.html): Transfers a domain from the current AWS account to another AWS account.
- [UpdateDomainContact](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_UpdateDomainContact.html): This operation updates the contact information for a particular domain.
- [UpdateDomainContactPrivacy](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_UpdateDomainContactPrivacy.html): This operation updates the specified domain contact's privacy setting.
- [UpdateDomainNameservers](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_UpdateDomainNameservers.html): This operation replaces the current set of name servers for the domain with the specified set of name servers.
- [UpdateTagsForDomain](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_UpdateTagsForDomain.html): This operation adds or updates tags for a specified domain.
- [ViewBilling](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_ViewBilling.html): Returns all the domain-related billing records for the current AWS account for a specified period

### [Amazon Route 53 Global Resolver](https://docs.aws.amazon.com/Route53/latest/APIReference/API_Operations_Amazon_Route_53_Global_Resolver.html)

The following actions are supported by Amazon Route 53 Global Resolver:

- [AssociateHostedZone](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_AssociateHostedZone.html): Associates a Route 53 private hosted zone with a Route 53 Global Resolver resource.
- [BatchCreateFirewallRule](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_BatchCreateFirewallRule.html): Creates multiple DNS firewall rules in a single operation.
- [BatchDeleteFirewallRule](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_BatchDeleteFirewallRule.html): Deletes multiple DNS firewall rules in a single operation.
- [BatchUpdateFirewallRule](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_BatchUpdateFirewallRule.html): Updates multiple DNS firewall rules in a single operation.
- [CreateAccessSource](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_CreateAccessSource.html): Creates an access source for a DNS view.
- [CreateAccessToken](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_CreateAccessToken.html): Creates an access token for a DNS view.
- [CreateDNSView](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_CreateDNSView.html): Creates a DNS view within a Route 53 Global Resolver.
- [CreateFirewallDomainList](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_CreateFirewallDomainList.html): Creates a firewall domain list.
- [CreateFirewallRule](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_CreateFirewallRule.html): Creates a DNS firewall rule.
- [CreateGlobalResolver](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_CreateGlobalResolver.html): Creates a new Route 53 Global Resolver instance.
- [DeleteAccessSource](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_DeleteAccessSource.html): Deletes an access source.
- [DeleteAccessToken](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_DeleteAccessToken.html): Deletes an access token.
- [DeleteDNSView](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_DeleteDNSView.html): Deletes a DNS view.
- [DeleteFirewallDomainList](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_DeleteFirewallDomainList.html): Deletes a firewall domain list.
- [DeleteFirewallRule](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_DeleteFirewallRule.html): Deletes a DNS firewall rule.
- [DeleteGlobalResolver](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_DeleteGlobalResolver.html): Deletes a Route 53 Global Resolver instance.
- [DisableDNSView](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_DisableDNSView.html): Disables a DNS view, preventing it from serving DNS queries.
- [DisassociateHostedZone](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_DisassociateHostedZone.html): Disassociates a Route 53 private hosted zone from a Route 53 Global Resolver resource.
- [EnableDNSView](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_EnableDNSView.html): Enables a disabled DNS view, allowing it to serve DNS queries again.
- [GetAccessSource](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_GetAccessSource.html): Retrieves information about an access source.
- [GetAccessToken](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_GetAccessToken.html): Retrieves information about an access token.
- [GetDNSView](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_GetDNSView.html): Retrieves information about a DNS view.
- [GetFirewallDomainList](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_GetFirewallDomainList.html): Retrieves information about a firewall domain list.
- [GetFirewallRule](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_GetFirewallRule.html): Retrieves information about a DNS firewall rule.
- [GetGlobalResolver](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_GetGlobalResolver.html): Retrieves information about a Route 53 Global Resolver instance.
- [GetHostedZoneAssociation](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_GetHostedZoneAssociation.html): Retrieves information about a hosted zone association.
- [GetManagedFirewallDomainList](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_GetManagedFirewallDomainList.html): Retrieves information about an AWS-managed firewall domain list.
- [ImportFirewallDomains](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_ImportFirewallDomains.html): Imports a list of domains from an Amazon S3 file into a firewall domain list.
- [ListAccessSources](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_ListAccessSources.html): Lists all access sources with pagination support.
- [ListAccessTokens](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_ListAccessTokens.html): Lists all access tokens for a DNS view with pagination support.
- [ListDNSViews](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_ListDNSViews.html): Lists all DNS views for a Route 53 Global Resolver with pagination support.
- [ListFirewallDomainLists](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_ListFirewallDomainLists.html): Lists all firewall domain lists for a Route 53 Global Resolver with pagination support.
- [ListFirewallDomains](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_ListFirewallDomains.html): Lists all the domains in DNS Firewall domain list you have created.
- [ListFirewallRules](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_ListFirewallRules.html): Lists all DNS firewall rules for a DNS view with pagination support.
- [ListGlobalResolvers](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_ListGlobalResolvers.html): Lists all Route 53 Global Resolver instances in your account with pagination support.
- [ListHostedZoneAssociations](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_ListHostedZoneAssociations.html): Lists all hosted zone associations for a Route 53 Global Resolver resource with pagination support.
- [ListManagedFirewallDomainLists](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_ListManagedFirewallDomainLists.html): Returns a paginated list of the AWS Managed DNS Lists and the categories for DNS Firewall.
- [ListTagsForResource](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_ListTagsForResource.html): Lists the tags associated with a Route 53 Global Resolver resource.
- [TagResource](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_TagResource.html): Adds or updates tags for a Route 53 Global Resolver resource.
- [UntagResource](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_UntagResource.html): Removes tags from a Route 53 Global Resolver resource.
- [UpdateAccessSource](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_UpdateAccessSource.html): Updates the configuration of an access source.
- [UpdateAccessToken](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_UpdateAccessToken.html): Updates the configuration of an access token.
- [UpdateDNSView](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_UpdateDNSView.html): Updates the configuration of a DNS view.
- [UpdateFirewallDomains](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_UpdateFirewallDomains.html): Updates a DNS Firewall domain list from an array of specified domains.
- [UpdateFirewallRule](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_UpdateFirewallRule.html): Updates the configuration of a DNS firewall rule.
- [UpdateGlobalResolver](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_UpdateGlobalResolver.html): Updates the configuration of a Route 53 Global Resolver instance.
- [UpdateHostedZoneAssociation](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_UpdateHostedZoneAssociation.html): Updates the configuration of a hosted zone association.

### [Route 53 Profiles](https://docs.aws.amazon.com/Route53/latest/APIReference/API_Operations_Route_53_Profiles.html)

The following actions are supported by Route 53 Profiles:

- [AssociateProfile](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53profiles_AssociateProfile.html): Associates a Route 53 Profiles profile with a VPC.
- [AssociateResourceToProfile](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53profiles_AssociateResourceToProfile.html): Associates a DNS resource configuration to a Route 53 Profile.
- [CreateProfile](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53profiles_CreateProfile.html): Creates an empty Route 53 Profile.
- [DeleteProfile](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53profiles_DeleteProfile.html): Deletes the specified Route 53 Profile.
- [DisassociateProfile](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53profiles_DisassociateProfile.html): Dissociates a specified Route 53 Profile from the specified VPC.
- [DisassociateResourceFromProfile](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53profiles_DisassociateResourceFromProfile.html): Dissoaciated a specified resource, from the Route 53 Profile.
- [GetProfile](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53profiles_GetProfile.html): Returns information about a specified Route 53 Profile, such as whether whether the Profile is shared, and the current status of the Profile.
- [GetProfileAssociation](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53profiles_GetProfileAssociation.html): Retrieves a Route 53 Profile association for a VPC.
- [GetProfileResourceAssociation](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53profiles_GetProfileResourceAssociation.html): Returns information about a specified Route 53 Profile resource association.
- [ListProfileAssociations](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53profiles_ListProfileAssociations.html): Lists all the VPCs that the specified Route 53 Profile is associated with.
- [ListProfileResourceAssociations](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53profiles_ListProfileResourceAssociations.html): Lists all the resource associations for the specified Route 53 Profile.
- [ListProfiles](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53profiles_ListProfiles.html): Lists all the Route 53 Profiles associated with your AWS account.
- [ListTagsForResource](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53profiles_ListTagsForResource.html): Lists the tags that you associated with the specified resource.
- [TagResource](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53profiles_TagResource.html): Adds one or more tags to a specified resource.
- [UntagResource](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53profiles_UntagResource.html): Removes one or more tags from a specified resource.
- [UpdateProfileResourceAssociation](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53profiles_UpdateProfileResourceAssociation.html): Updates the specified Route 53 Profile resourse association.

### [Amazon RouteÂ 53 Resolver](https://docs.aws.amazon.com/Route53/latest/APIReference/API_Operations_Amazon_Route_53_Resolver.html)

The following actions are supported by Amazon RouteÂ 53 Resolver:

- [AssociateFirewallRuleGroup](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_AssociateFirewallRuleGroup.html): Associates a with a VPC, to provide DNS filtering for the VPC.
- [AssociateResolverEndpointIpAddress](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_AssociateResolverEndpointIpAddress.html): Adds IP addresses to an inbound or an outbound Resolver endpoint.
- [AssociateResolverQueryLogConfig](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_AssociateResolverQueryLogConfig.html): Associates an Amazon VPC with a specified query logging configuration.
- [AssociateResolverRule](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_AssociateResolverRule.html): Associates a Resolver rule with a VPC.
- [CreateFirewallDomainList](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_CreateFirewallDomainList.html): Creates an empty firewall domain list for use in DNS Firewall rules.
- [CreateFirewallRule](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_CreateFirewallRule.html): Creates a single DNS Firewall rule in the specified rule group, using the specified domain list.
- [CreateFirewallRuleGroup](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_CreateFirewallRuleGroup.html): Creates an empty DNS Firewall rule group for filtering DNS network traffic in a VPC.
- [CreateOutpostResolver](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_CreateOutpostResolver.html): Creates a Amazon RouteÂ 53 Resolver on an Outpost.
- [CreateResolverEndpoint](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_CreateResolverEndpoint.html): Creates a Resolver endpoint.
- [CreateResolverQueryLogConfig](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_CreateResolverQueryLogConfig.html): Creates a Resolver query logging configuration, which defines where you want Resolver to save DNS query logs that originate in your VPCs.
- [CreateResolverRule](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_CreateResolverRule.html): For DNS queries that originate in your VPCs, specifies which Resolver endpoint the queries pass through, one domain name that you want to forward to your network, and the IP addresses of the DNS resolvers in your network.
- [DeleteFirewallDomainList](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_DeleteFirewallDomainList.html): Deletes the specified domain list.
- [DeleteFirewallRule](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_DeleteFirewallRule.html): Deletes the specified firewall rule.
- [DeleteFirewallRuleGroup](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_DeleteFirewallRuleGroup.html): Deletes the specified firewall rule group.
- [DeleteOutpostResolver](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_DeleteOutpostResolver.html): Deletes a Resolver on the Outpost.
- [DeleteResolverEndpoint](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_DeleteResolverEndpoint.html): Deletes a Resolver endpoint.
- [DeleteResolverQueryLogConfig](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_DeleteResolverQueryLogConfig.html): Deletes a query logging configuration.
- [DeleteResolverRule](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_DeleteResolverRule.html): Deletes a Resolver rule.
- [DisassociateFirewallRuleGroup](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_DisassociateFirewallRuleGroup.html): Disassociates a from a VPC, to remove DNS filtering from the VPC.
- [DisassociateResolverEndpointIpAddress](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_DisassociateResolverEndpointIpAddress.html): Removes IP addresses from an inbound or an outbound Resolver endpoint.
- [DisassociateResolverQueryLogConfig](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_DisassociateResolverQueryLogConfig.html): Disassociates a VPC from a query logging configuration.
- [DisassociateResolverRule](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_DisassociateResolverRule.html): Removes the association between a specified Resolver rule and a specified VPC.
- [GetFirewallConfig](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_GetFirewallConfig.html): Retrieves the configuration of the firewall behavior provided by DNS Firewall for a single VPC from Amazon Virtual Private Cloud (Amazon VPC).
- [GetFirewallDomainList](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_GetFirewallDomainList.html): Retrieves the specified firewall domain list.
- [GetFirewallRuleGroup](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_GetFirewallRuleGroup.html): Retrieves the specified firewall rule group.
- [GetFirewallRuleGroupAssociation](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_GetFirewallRuleGroupAssociation.html): Retrieves a firewall rule group association, which enables DNS filtering for a VPC with one rule group.
- [GetFirewallRuleGroupPolicy](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_GetFirewallRuleGroupPolicy.html): Returns the AWS Identity and Access Management (AWS IAM) policy for sharing the specified rule group.
- [GetOutpostResolver](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_GetOutpostResolver.html): Gets information about a specified Resolver on the Outpost, such as its instance count and type, name, and the current status of the Resolver.
- [GetResolverConfig](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_GetResolverConfig.html): Retrieves the behavior configuration of RouteÂ 53 Resolver behavior for a single VPC from Amazon Virtual Private Cloud.
- [GetResolverDnssecConfig](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_GetResolverDnssecConfig.html): Gets DNSSEC validation information for a specified resource.
- [GetResolverEndpoint](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_GetResolverEndpoint.html): Gets information about a specified Resolver endpoint, such as whether it's an inbound or an outbound Resolver endpoint, and the current status of the endpoint.
- [GetResolverQueryLogConfig](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_GetResolverQueryLogConfig.html): Gets information about a specified Resolver query logging configuration, such as the number of VPCs that the configuration is logging queries for and the location that logs are sent to.
- [GetResolverQueryLogConfigAssociation](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_GetResolverQueryLogConfigAssociation.html): Gets information about a specified association between a Resolver query logging configuration and an Amazon VPC.
- [GetResolverQueryLogConfigPolicy](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_GetResolverQueryLogConfigPolicy.html): Gets information about a query logging policy.
- [GetResolverRule](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_GetResolverRule.html): Gets information about a specified Resolver rule, such as the domain name that the rule forwards DNS queries for and the ID of the outbound Resolver endpoint that the rule is associated with.
- [GetResolverRuleAssociation](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_GetResolverRuleAssociation.html): Gets information about an association between a specified Resolver rule and a VPC.
- [GetResolverRulePolicy](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_GetResolverRulePolicy.html): Gets information about the Resolver rule policy for a specified rule.
- [ImportFirewallDomains](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_ImportFirewallDomains.html): Imports domain names from a file into a domain list, for use in a DNS firewall rule group.
- [ListFirewallConfigs](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_ListFirewallConfigs.html): Retrieves the firewall configurations that you have defined.
- [ListFirewallDomainLists](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_ListFirewallDomainLists.html): Retrieves the firewall domain lists that you have defined.
- [ListFirewallDomains](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_ListFirewallDomains.html): Retrieves the domains that you have defined for the specified firewall domain list.
- [ListFirewallRuleGroupAssociations](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_ListFirewallRuleGroupAssociations.html): Retrieves the firewall rule group associations that you have defined.
- [ListFirewallRuleGroups](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_ListFirewallRuleGroups.html): Retrieves the minimal high-level information for the rule groups that you have defined.
- [ListFirewallRules](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_ListFirewallRules.html): Retrieves the firewall rules that you have defined for the specified firewall rule group.
- [ListOutpostResolvers](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_ListOutpostResolvers.html): Lists all the Resolvers on Outposts that were created using the current AWS account.
- [ListResolverConfigs](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_ListResolverConfigs.html): Retrieves the Resolver configurations that you have defined.
- [ListResolverDnssecConfigs](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_ListResolverDnssecConfigs.html): Lists the configurations for DNSSEC validation that are associated with the current AWS account.
- [ListResolverEndpointIpAddresses](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_ListResolverEndpointIpAddresses.html): Gets the IP addresses for a specified Resolver endpoint.
- [ListResolverEndpoints](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_ListResolverEndpoints.html): Lists all the Resolver endpoints that were created using the current AWS account.
- [ListResolverQueryLogConfigAssociations](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_ListResolverQueryLogConfigAssociations.html): Lists information about associations between Amazon VPCs and query logging configurations.
- [ListResolverQueryLogConfigs](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_ListResolverQueryLogConfigs.html): Lists information about the specified query logging configurations.
- [ListResolverRuleAssociations](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_ListResolverRuleAssociations.html): Lists the associations that were created between Resolver rules and VPCs using the current AWS account.
- [ListResolverRules](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_ListResolverRules.html): Lists the Resolver rules that were created using the current AWS account.
- [ListTagsForResource](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_ListTagsForResource.html): Lists the tags that you associated with the specified resource.
- [PutFirewallRuleGroupPolicy](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_PutFirewallRuleGroupPolicy.html): Attaches an AWS Identity and Access Management (AWS IAM) policy for sharing the rule group.
- [PutResolverQueryLogConfigPolicy](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_PutResolverQueryLogConfigPolicy.html): Specifies an AWS account that you want to share a query logging configuration with, the query logging configuration that you want to share, and the operations that you want the account to be able to perform on the configuration.
- [PutResolverRulePolicy](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_PutResolverRulePolicy.html): Specifies an AWS rule that you want to share with another account, the account that you want to share the rule with, and the operations that you want the account to be able to perform on the rule.
- [TagResource](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_TagResource.html): Adds one or more tags to a specified resource.
- [UntagResource](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_UntagResource.html): Removes one or more tags from a specified resource.
- [UpdateFirewallConfig](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_UpdateFirewallConfig.html): Updates the configuration of the firewall behavior provided by DNS Firewall for a single VPC from Amazon Virtual Private Cloud (Amazon VPC).
- [UpdateFirewallDomains](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_UpdateFirewallDomains.html): Updates the firewall domain list from an array of domain specifications.
- [UpdateFirewallRule](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_UpdateFirewallRule.html): Updates the specified firewall rule.
- [UpdateFirewallRuleGroupAssociation](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_UpdateFirewallRuleGroupAssociation.html): Changes the association of a with a VPC.
- [UpdateOutpostResolver](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_UpdateOutpostResolver.html): You can use UpdateOutpostResolver to update the instance count, type, or name of a Resolver on an Outpost.
- [UpdateResolverConfig](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_UpdateResolverConfig.html): Updates the behavior configuration of Amazon RouteÂ 53 Resolver behavior for a single VPC from Amazon Virtual Private Cloud.
- [UpdateResolverDnssecConfig](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_UpdateResolverDnssecConfig.html): Updates an existing DNSSEC validation configuration.
- [UpdateResolverEndpoint](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_UpdateResolverEndpoint.html): Updates the name, or endpoint type for an inbound or an outbound Resolver endpoint.
- [UpdateResolverRule](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_UpdateResolverRule.html): Updates settings for a specified Resolver rule.


## [Making API Requests](https://docs.aws.amazon.com/Route53/latest/APIReference/requests.html)

### [Making API Requests for Hosted Zones, Resource Record Sets, and Health Checks](https://docs.aws.amazon.com/Route53/latest/APIReference/requests-rest.html)

Describes how to make REST requests to the Route 53 control API, which you use to create and manage your hosted zones, resource record sets, health checks, and tags.

- [REST Requests](https://docs.aws.amazon.com/Route53/latest/APIReference/requests-rest-overview.html): Describes the structure of a Route 53 REST request.
- [REST Responses](https://docs.aws.amazon.com/Route53/latest/APIReference/requests-rest-responses.html): Describes the REST responses that return special information specific to Route 53.

### [Making API Requests for Domain Registration and for RouteÂ 53 Resolver](https://docs.aws.amazon.com/Route53/latest/APIReference/requests-rpc.html)

Describes how to make requests to the Amazon Route 53 control API to manage domain registration and Route 53 Resolver.

- [RPC Requests](https://docs.aws.amazon.com/Route53/latest/APIReference/requests-rpc-overview.html): Describes the structure of a Route 53 RPC request.
- [RPC Responses](https://docs.aws.amazon.com/Route53/latest/APIReference/requests-rpc-responses.html): Describes the RPC responses that return special information specific to Route 53.
- [Signing Amazon RouteÂ 53 API Requests](https://docs.aws.amazon.com/Route53/latest/APIReference/requests-authentication.html): Requests must be signed using an access key ID and a secret access key.


## [Data Types](https://docs.aws.amazon.com/Route53/latest/APIReference/API_Types.html)

### [Amazon RouteÂ 53](https://docs.aws.amazon.com/Route53/latest/APIReference/API_Types_Amazon_Route_53.html)

The following data types are supported by Amazon RouteÂ 53:

- [AccountLimit](https://docs.aws.amazon.com/Route53/latest/APIReference/API_AccountLimit.html): A complex type that contains the type of limit that you specified in the request and the current value for that limit.
- [AlarmIdentifier](https://docs.aws.amazon.com/Route53/latest/APIReference/API_AlarmIdentifier.html): A complex type that identifies the CloudWatch alarm that you want Amazon Route 53 health checkers to use to determine whether the specified health check is healthy.
- [AliasTarget](https://docs.aws.amazon.com/Route53/latest/APIReference/API_AliasTarget.html): Alias resource record sets only: Information about the AWS resource, such as a CloudFront distribution or an Amazon S3 bucket, that you want to route traffic to.
- [Change](https://docs.aws.amazon.com/Route53/latest/APIReference/API_Change.html): The information for each resource record set that you want to change.
- [ChangeBatch](https://docs.aws.amazon.com/Route53/latest/APIReference/API_ChangeBatch.html): The information for a change request.
- [ChangeInfo](https://docs.aws.amazon.com/Route53/latest/APIReference/API_ChangeInfo.html): A complex type that describes change information about changes made to your hosted zone.
- [CidrBlockSummary](https://docs.aws.amazon.com/Route53/latest/APIReference/API_CidrBlockSummary.html): A complex type that lists the CIDR blocks.
- [CidrCollection](https://docs.aws.amazon.com/Route53/latest/APIReference/API_CidrCollection.html): A complex type that identifies a CIDR collection.
- [CidrCollectionChange](https://docs.aws.amazon.com/Route53/latest/APIReference/API_CidrCollectionChange.html): A complex type that contains information about the CIDR collection change.
- [CidrRoutingConfig](https://docs.aws.amazon.com/Route53/latest/APIReference/API_CidrRoutingConfig.html): The object that is specified in resource record set object when you are linking a resource record set to a CIDR location.
- [CloudWatchAlarmConfiguration](https://docs.aws.amazon.com/Route53/latest/APIReference/API_CloudWatchAlarmConfiguration.html): A complex type that contains information about the CloudWatch alarm that Amazon Route 53 is monitoring for this health check.
- [CollectionSummary](https://docs.aws.amazon.com/Route53/latest/APIReference/API_CollectionSummary.html): A complex type that is an entry in an CidrCollection array.
- [Coordinates](https://docs.aws.amazon.com/Route53/latest/APIReference/API_Coordinates.html): A complex type that lists the coordinates for a geoproximity resource record.
- [DelegationSet](https://docs.aws.amazon.com/Route53/latest/APIReference/API_DelegationSet.html): A complex type that lists the name servers in a delegation set, as well as the CallerReference and the ID for the delegation set.
- [Dimension](https://docs.aws.amazon.com/Route53/latest/APIReference/API_Dimension.html): For the metric that the CloudWatch alarm is associated with, a complex type that contains information about one dimension.
- [DNSSECStatus](https://docs.aws.amazon.com/Route53/latest/APIReference/API_DNSSECStatus.html): A string representing the status of DNSSEC signing.
- [GeoLocation](https://docs.aws.amazon.com/Route53/latest/APIReference/API_GeoLocation.html): A complex type that contains information about a geographic location.
- [GeoLocationDetails](https://docs.aws.amazon.com/Route53/latest/APIReference/API_GeoLocationDetails.html): A complex type that contains the codes and full continent, country, and subdivision names for the specified geolocation code.
- [GeoProximityLocation](https://docs.aws.amazon.com/Route53/latest/APIReference/API_GeoProximityLocation.html): (Resource record sets only): A complex type that lets you specify where your resources are located.
- [HealthCheck](https://docs.aws.amazon.com/Route53/latest/APIReference/API_HealthCheck.html): A complex type that contains information about one health check that is associated with the current AWS account.
- [HealthCheckConfig](https://docs.aws.amazon.com/Route53/latest/APIReference/API_HealthCheckConfig.html): A complex type that contains information about the health check.
- [HealthCheckObservation](https://docs.aws.amazon.com/Route53/latest/APIReference/API_HealthCheckObservation.html): A complex type that contains the last failure reason as reported by one Amazon Route 53 health checker.
- [HostedZone](https://docs.aws.amazon.com/Route53/latest/APIReference/API_HostedZone.html): A complex type that contains general information about the hosted zone.
- [HostedZoneConfig](https://docs.aws.amazon.com/Route53/latest/APIReference/API_HostedZoneConfig.html): A complex type that contains an optional comment about your hosted zone.
- [HostedZoneFailureReasons](https://docs.aws.amazon.com/Route53/latest/APIReference/API_HostedZoneFailureReasons.html): Contains information about why certain features failed to be enabled or configured for the hosted zone.
- [HostedZoneFeatures](https://docs.aws.amazon.com/Route53/latest/APIReference/API_HostedZoneFeatures.html): Represents the features configuration for a hosted zone, including the status of various features and any associated failure reasons.
- [HostedZoneLimit](https://docs.aws.amazon.com/Route53/latest/APIReference/API_HostedZoneLimit.html): A complex type that contains the type of limit that you specified in the request and the current value for that limit.
- [HostedZoneOwner](https://docs.aws.amazon.com/Route53/latest/APIReference/API_HostedZoneOwner.html): A complex type that identifies a hosted zone that a specified Amazon VPC is associated with and the owner of the hosted zone.
- [HostedZoneSummary](https://docs.aws.amazon.com/Route53/latest/APIReference/API_HostedZoneSummary.html): In the response to a ListHostedZonesByVPC request, the HostedZoneSummaries element contains one HostedZoneSummary element for each hosted zone that the specified Amazon VPC is associated with.
- [KeySigningKey](https://docs.aws.amazon.com/Route53/latest/APIReference/API_KeySigningKey.html): A key-signing key (KSK) is a complex type that represents a public/private key pair.
- [LinkedService](https://docs.aws.amazon.com/Route53/latest/APIReference/API_LinkedService.html): If a health check or hosted zone was created by another service, LinkedService is a complex type that describes the service that created the resource.
- [LocationSummary](https://docs.aws.amazon.com/Route53/latest/APIReference/API_LocationSummary.html): A complex type that contains information about the CIDR location.
- [QueryLoggingConfig](https://docs.aws.amazon.com/Route53/latest/APIReference/API_QueryLoggingConfig.html): A complex type that contains information about a configuration for DNS query logging.
- [ResourceRecord](https://docs.aws.amazon.com/Route53/latest/APIReference/API_ResourceRecord.html): Information specific to the resource record.
- [ResourceRecordSet](https://docs.aws.amazon.com/Route53/latest/APIReference/API_ResourceRecordSet.html): Information about the resource record set to create or delete.
- [ResourceTagSet](https://docs.aws.amazon.com/Route53/latest/APIReference/API_ResourceTagSet.html): A complex type containing a resource and its associated tags.
- [ReusableDelegationSetLimit](https://docs.aws.amazon.com/Route53/latest/APIReference/API_ReusableDelegationSetLimit.html): A complex type that contains the type of limit that you specified in the request and the current value for that limit.
- [StatusReport](https://docs.aws.amazon.com/Route53/latest/APIReference/API_StatusReport.html): A complex type that contains the status that one Amazon Route 53 health checker reports and the time of the health check.
- [Tag](https://docs.aws.amazon.com/Route53/latest/APIReference/API_Tag.html): A complex type that contains information about a tag that you want to add or edit for the specified health check or hosted zone.
- [TrafficPolicy](https://docs.aws.amazon.com/Route53/latest/APIReference/API_TrafficPolicy.html): A complex type that contains settings for a traffic policy.
- [TrafficPolicyInstance](https://docs.aws.amazon.com/Route53/latest/APIReference/API_TrafficPolicyInstance.html): A complex type that contains settings for the new traffic policy instance.
- [TrafficPolicySummary](https://docs.aws.amazon.com/Route53/latest/APIReference/API_TrafficPolicySummary.html): A complex type that contains information about the latest version of one traffic policy that is associated with the current AWS account.
- [VPC](https://docs.aws.amazon.com/Route53/latest/APIReference/API_VPC.html): (Private hosted zones only) A complex type that contains information about an Amazon VPC.

### [Amazon RouteÂ 53 domain registration](https://docs.aws.amazon.com/Route53/latest/APIReference/API_Types_Amazon_Route_53_Domains.html)

The following data types are supported by Amazon RouteÂ 53 domain registration:

- [BillingRecord](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_BillingRecord.html): Information for one billing record.
- [Consent](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_Consent.html): Customer's consent for the owner change request.
- [ContactDetail](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_ContactDetail.html): ContactDetail includes the following elements.
- [DnssecKey](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_DnssecKey.html): Information about the DNSSEC key.
- [DnssecSigningAttributes](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_DnssecSigningAttributes.html): Information about a delegation signer (DS) record that was created in the registry by AssociateDelegationSignerToDomain.
- [DomainPrice](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_DomainPrice.html): Information about the domain price associated with a TLD.
- [DomainSuggestion](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_DomainSuggestion.html): Information about one suggested domain name.
- [DomainSummary](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_DomainSummary.html): Summary information about one domain.
- [DomainTransferability](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_DomainTransferability.html): A complex type that contains information about whether the specified domain can be transferred to Route 53.
- [ExtraParam](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_ExtraParam.html): ExtraParam includes the following elements.
- [FilterCondition](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_FilterCondition.html): Information for the filtering of a list of domains returned by ListDomains.
- [Nameserver](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_Nameserver.html): Name server includes the following elements.
- [OperationSummary](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_OperationSummary.html): OperationSummary includes the following elements.
- [PriceWithCurrency](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_PriceWithCurrency.html): Currency-specific price information.
- [SortCondition](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_SortCondition.html): Information for sorting a list of domains.
- [Tag](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_Tag.html): Each tag includes the following elements.

### [Amazon Route 53 Global Resolver](https://docs.aws.amazon.com/Route53/latest/APIReference/API_Types_Amazon_Route_53_Global_Resolver.html)

The following data types are supported by Amazon Route 53 Global Resolver:

- [AccessSourcesItem](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_AccessSourcesItem.html): Summary information about an access source.
- [AccessTokenItem](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_AccessTokenItem.html): Summary information about a token.
- [BatchCreateFirewallRuleInputItem](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_BatchCreateFirewallRuleInputItem.html): Information about a DNS Firewall rule to create in a batch operation.
- [BatchCreateFirewallRuleOutputItem](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_BatchCreateFirewallRuleOutputItem.html): Information about the result of creating a DNS Firewall rule in a batch operation.
- [BatchCreateFirewallRuleResult](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_BatchCreateFirewallRuleResult.html): The result of creating a firewall rule in a batch operation.
- [BatchDeleteFirewallRuleInputItem](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_BatchDeleteFirewallRuleInputItem.html): Information about a DNS Firewall rule to delete in a batch operation.
- [BatchDeleteFirewallRuleOutputItem](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_BatchDeleteFirewallRuleOutputItem.html): The result of deleting a firewall rule in a batch operation.
- [BatchDeleteFirewallRuleResult](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_BatchDeleteFirewallRuleResult.html): Information about a firewall rule that was deleted in a batch operation.
- [BatchUpdateFirewallRuleInputItem](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_BatchUpdateFirewallRuleInputItem.html): Information for updating a firewall rule in a batch operation.
- [BatchUpdateFirewallRuleOutputItem](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_BatchUpdateFirewallRuleOutputItem.html): The result of updating a firewall rule in a batch operation.
- [BatchUpdateFirewallRuleResult](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_BatchUpdateFirewallRuleResult.html): Information about a firewall rule that was updated in a batch operation.
- [DNSViewSummary](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_DNSViewSummary.html): Summary information about a DNS view.
- [FirewallDomainListsItem](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_FirewallDomainListsItem.html): Summary information about a firewall domain list.
- [FirewallRulesItem](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_FirewallRulesItem.html): Summary information about a firewall rule.
- [GlobalResolversItem](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_GlobalResolversItem.html): Summary information about a global resolver.
- [HostedZoneAssociationSummary](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_HostedZoneAssociationSummary.html): Summary information about a hosted zone association.
- [ManagedFirewallDomainListsItem](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_ManagedFirewallDomainListsItem.html): Summary information about a managed firewall domain list.
- [ValidationExceptionField](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_ValidationExceptionField.html): Information about a field that failed validation.

### [Route 53 Profiles](https://docs.aws.amazon.com/Route53/latest/APIReference/API_Types_Route_53_Profiles.html)

The following data types are supported by Route 53 Profiles:

- [Profile](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53profiles_Profile.html): A complex type that includes settings for a Route 53 Profile.
- [ProfileAssociation](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53profiles_ProfileAssociation.html): An association between a Route 53 Profile and a VPC.
- [ProfileResourceAssociation](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53profiles_ProfileResourceAssociation.html): The association between a Route 53 Profile and resources.
- [ProfileSummary](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53profiles_ProfileSummary.html): Summary information about a Route 53 Profile.
- [Tag](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53profiles_Tag.html): Tag for the Profile.

### [Amazon RouteÂ 53 Resolver](https://docs.aws.amazon.com/Route53/latest/APIReference/API_Types_Amazon_Route_53_Resolver.html)

The following data types are supported by Amazon RouteÂ 53 Resolver:

- [Filter](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_Filter.html): For Resolver list operations (ListResolverEndpoints, ListResolverRules, ListResolverRuleAssociations, ListResolverQueryLogConfigs, ListResolverQueryLogConfigAssociations), and ListResolverDnssecConfigs), an optional specification to return a subset of objects.
- [FirewallConfig](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_FirewallConfig.html): Configuration of the firewall behavior provided by DNS Firewall for a single VPC from Amazon Virtual Private Cloud (Amazon VPC).
- [FirewallDomainList](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_FirewallDomainList.html): High-level information about a list of firewall domains for use in a .
- [FirewallDomainListMetadata](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_FirewallDomainListMetadata.html): Minimal high-level information for a firewall domain list.
- [FirewallRule](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_FirewallRule.html): A single firewall rule in a rule group.
- [FirewallRuleGroup](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_FirewallRuleGroup.html): High-level information for a firewall rule group.
- [FirewallRuleGroupAssociation](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_FirewallRuleGroupAssociation.html): An association between a firewall rule group and a VPC, which enables DNS filtering for the VPC.
- [FirewallRuleGroupMetadata](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_FirewallRuleGroupMetadata.html): Minimal high-level information for a firewall rule group.
- [IpAddressRequest](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_IpAddressRequest.html): In a CreateResolverEndpoint request, the IP address that DNS queries originate from (for outbound endpoints) or that you forward DNS queries to (for inbound endpoints).
- [IpAddressResponse](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_IpAddressResponse.html): In the response to a GetResolverEndpoint request, information about the IP addresses that the Resolver endpoint uses for DNS queries.
- [IpAddressUpdate](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_IpAddressUpdate.html): In an UpdateResolverEndpoint request, information about an IP address to update.
- [OutpostResolver](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_OutpostResolver.html): A complex type that contains settings for an existing Resolver on an Outpost.
- [ResolverConfig](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_ResolverConfig.html): A complex type that contains information about a Resolver configuration for a VPC.
- [ResolverDnssecConfig](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_ResolverDnssecConfig.html): A complex type that contains information about a configuration for DNSSEC validation.
- [ResolverEndpoint](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_ResolverEndpoint.html): In the response to a CreateResolverEndpoint, DeleteResolverEndpoint, GetResolverEndpoint, Updates the name, or ResolverEndpointType for an endpoint, or UpdateResolverEndpoint request, a complex type that contains settings for an existing inbound or outbound Resolver endpoint.
- [ResolverQueryLogConfig](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_ResolverQueryLogConfig.html): In the response to a CreateResolverQueryLogConfig, DeleteResolverQueryLogConfig, GetResolverQueryLogConfig, or ListResolverQueryLogConfigs request, a complex type that contains settings for one query logging configuration.
- [ResolverQueryLogConfigAssociation](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_ResolverQueryLogConfigAssociation.html): In the response to an AssociateResolverQueryLogConfig, DisassociateResolverQueryLogConfig, GetResolverQueryLogConfigAssociation, or ListResolverQueryLogConfigAssociations, request, a complex type that contains settings for a specified association between an Amazon VPC and a query logging configuration.
- [ResolverRule](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_ResolverRule.html): For queries that originate in your VPC, detailed information about a Resolver rule, which specifies how to route DNS queries out of the VPC.
- [ResolverRuleAssociation](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_ResolverRuleAssociation.html): In the response to an AssociateResolverRule, DisassociateResolverRule, or ListResolverRuleAssociations request, provides information about an association between a Resolver rule and a VPC.
- [ResolverRuleConfig](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_ResolverRuleConfig.html): In an UpdateResolverRule request, information about the changes that you want to make.
- [Tag](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_Tag.html): One tag that you want to add to the specified resource.
- [TargetAddress](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_TargetAddress.html): In a CreateResolverRule request, an array of the IPs that you want to forward DNS queries to.
- [UpdateIpAddress](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_UpdateIpAddress.html): Provides information about the IP address type in response to UpdateResolverEndpoint.
