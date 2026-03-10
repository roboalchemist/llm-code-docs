# Source: https://docs.aws.amazon.com/ec2/latest/devguide/llms.txt

# Amazon Elastic Compute Cloud Developer Guide

- [Using the AWS CLI](https://docs.aws.amazon.com/ec2/latest/devguide/ec2-aws-cli.html)
- [Using CloudFormation](https://docs.aws.amazon.com/ec2/latest/devguide/ec2-cloudformation.html)
- [Using an AWS SDK](https://docs.aws.amazon.com/ec2/latest/devguide/sdk-general-information-section.html)
- [Low-level API for Amazon EC2](https://docs.aws.amazon.com/ec2/latest/devguide/ec2-low-level-api.html)
- [Console-to-Code](https://docs.aws.amazon.com/ec2/latest/devguide/console-to-code.html)
- [Monitor API requests using CloudWatch](https://docs.aws.amazon.com/ec2/latest/devguide/monitor.html)

## [Programmatic access to Amazon EC2](https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-intro.html)

- [Service endpoints](https://docs.aws.amazon.com/ec2/latest/devguide/ec2-endpoints.html): List of service endpoints for Amazon EC2, including FIPS endpoints.
- [Eventual consistency](https://docs.aws.amazon.com/ec2/latest/devguide/eventual-consistency.html): Learn about the eventual consistency model for Amazon EC2.
- [Idempotency](https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html): Ensure that your API request is idempotent so that it complete only once.
- [API request throttling](https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-throttling.html): Learn how Amazon EC2 throttles API requests
- [Pagination](https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-pagination.html): Learn about pagination for the Amazon EC2 API.


## [Code examples](https://docs.aws.amazon.com/ec2/latest/devguide/service_code_examples.html)

### [Basics](https://docs.aws.amazon.com/ec2/latest/devguide/service_code_examples_basics.html)

The following code examples show how to use the basics of Amazon EC2 with AWS SDKs.

- [Hello Amazon EC2](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_Hello_section.html): Hello Amazon EC2
- [Learn the basics](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_Scenario_GetStartedInstances_section.html): Learn the basics of Amazon EC2 with an AWS SDK

### [Actions](https://docs.aws.amazon.com/ec2/latest/devguide/service_code_examples_actions.html)

The following code examples show how to use Amazon EC2 with AWS SDKs.

- [AcceptVpcPeeringConnection](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_AcceptVpcPeeringConnection_section.html): Use AcceptVpcPeeringConnection with a CLI
- [AllocateAddress](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_AllocateAddress_section.html): Use AllocateAddress with an AWS SDK or CLI
- [AllocateHosts](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_AllocateHosts_section.html): Use AllocateHosts with a CLI
- [AssignPrivateIpAddresses](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_AssignPrivateIpAddresses_section.html): Use AssignPrivateIpAddresses with a CLI
- [AssociateAddress](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_AssociateAddress_section.html): Use AssociateAddress with an AWS SDK or CLI
- [AssociateDhcpOptions](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_AssociateDhcpOptions_section.html): Use AssociateDhcpOptions with a CLI
- [AssociateRouteTable](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_AssociateRouteTable_section.html): Use AssociateRouteTable with a CLI
- [AttachInternetGateway](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_AttachInternetGateway_section.html): Use AttachInternetGateway with a CLI
- [AttachNetworkInterface](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_AttachNetworkInterface_section.html): Use AttachNetworkInterface with a CLI
- [AttachVolume](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_AttachVolume_section.html): Use AttachVolume with a CLI
- [AttachVpnGateway](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_AttachVpnGateway_section.html): Use AttachVpnGateway with a CLI
- [AuthorizeSecurityGroupEgress](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_AuthorizeSecurityGroupEgress_section.html): Use AuthorizeSecurityGroupEgress with a CLI
- [AuthorizeSecurityGroupIngress](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_AuthorizeSecurityGroupIngress_section.html): Use AuthorizeSecurityGroupIngress with an AWS SDK or CLI
- [CancelCapacityReservation](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_CancelCapacityReservation_section.html): Use CancelCapacityReservation with a CLI
- [CancelImportTask](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_CancelImportTask_section.html): Use CancelImportTask with a CLI
- [CancelSpotFleetRequests](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_CancelSpotFleetRequests_section.html): Use CancelSpotFleetRequests with a CLI
- [CancelSpotInstanceRequests](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_CancelSpotInstanceRequests_section.html): Use CancelSpotInstanceRequests with a CLI
- [ConfirmProductInstance](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_ConfirmProductInstance_section.html): Use ConfirmProductInstance with a CLI
- [CopyImage](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_CopyImage_section.html): Use CopyImage with a CLI
- [CopySnapshot](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_CopySnapshot_section.html): Use CopySnapshot with a CLI
- [CreateCapacityReservation](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_CreateCapacityReservation_section.html): Use CreateCapacityReservation with a CLI
- [CreateCustomerGateway](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_CreateCustomerGateway_section.html): Use CreateCustomerGateway with a CLI
- [CreateDhcpOptions](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_CreateDhcpOptions_section.html): Use CreateDhcpOptions with a CLI
- [CreateFlowLogs](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_CreateFlowLogs_section.html): Use CreateFlowLogs with a CLI
- [CreateImage](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_CreateImage_section.html): Use CreateImage with a CLI
- [CreateInstanceExportTask](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_CreateInstanceExportTask_section.html): Use CreateInstanceExportTask with a CLI
- [CreateInternetGateway](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_CreateInternetGateway_section.html): Use CreateInternetGateway with a CLI
- [CreateKeyPair](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_CreateKeyPair_section.html): Use CreateKeyPair with an AWS SDK or CLI
- [CreateLaunchTemplate](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_CreateLaunchTemplate_section.html): Use CreateLaunchTemplate with an AWS SDK or CLI
- [CreateNetworkAcl](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_CreateNetworkAcl_section.html): Use CreateNetworkAcl with a CLI
- [CreateNetworkAclEntry](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_CreateNetworkAclEntry_section.html): Use CreateNetworkAclEntry with a CLI
- [CreateNetworkInterface](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_CreateNetworkInterface_section.html): Use CreateNetworkInterface with a CLI
- [CreatePlacementGroup](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_CreatePlacementGroup_section.html): Use CreatePlacementGroup with a CLI
- [CreateRoute](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_CreateRoute_section.html): Use CreateRoute with a CLI
- [CreateRouteTable](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_CreateRouteTable_section.html): Use CreateRouteTable with an AWS SDK or CLI
- [CreateSecurityGroup](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_CreateSecurityGroup_section.html): Use CreateSecurityGroup with an AWS SDK or CLI
- [CreateSnapshot](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_CreateSnapshot_section.html): Use CreateSnapshot with a CLI
- [CreateSpotDatafeedSubscription](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_CreateSpotDatafeedSubscription_section.html): Use CreateSpotDatafeedSubscription with a CLI
- [CreateSubnet](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_CreateSubnet_section.html): Use CreateSubnet with an AWS SDK or CLI
- [CreateTags](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_CreateTags_section.html): Use CreateTags with an AWS SDK or CLI
- [CreateVolume](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_CreateVolume_section.html): Use CreateVolume with a CLI
- [CreateVpc](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_CreateVpc_section.html): Use CreateVpc with an AWS SDK or CLI
- [CreateVpcEndpoint](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_CreateVpcEndpoint_section.html): Use CreateVpcEndpoint with an AWS SDK or CLI
- [CreateVpnConnection](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_CreateVpnConnection_section.html): Use CreateVpnConnection with a CLI
- [CreateVpnConnectionRoute](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_CreateVpnConnectionRoute_section.html): Use CreateVpnConnectionRoute with a CLI
- [CreateVpnGateway](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_CreateVpnGateway_section.html): Use CreateVpnGateway with a CLI
- [DeleteCustomerGateway](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_DeleteCustomerGateway_section.html): Use DeleteCustomerGateway with a CLI
- [DeleteDhcpOptions](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_DeleteDhcpOptions_section.html): Use DeleteDhcpOptions with a CLI
- [DeleteFlowLogs](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_DeleteFlowLogs_section.html): Use DeleteFlowLogs with a CLI
- [DeleteInternetGateway](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_DeleteInternetGateway_section.html): Use DeleteInternetGateway with a CLI
- [DeleteKeyPair](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_DeleteKeyPair_section.html): Use DeleteKeyPair with an AWS SDK or CLI
- [DeleteLaunchTemplate](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_DeleteLaunchTemplate_section.html): Use DeleteLaunchTemplate with an AWS SDK or CLI
- [DeleteNetworkAcl](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_DeleteNetworkAcl_section.html): Use DeleteNetworkAcl with a CLI
- [DeleteNetworkAclEntry](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_DeleteNetworkAclEntry_section.html): Use DeleteNetworkAclEntry with a CLI
- [DeleteNetworkInterface](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_DeleteNetworkInterface_section.html): Use DeleteNetworkInterface with a CLI
- [DeletePlacementGroup](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_DeletePlacementGroup_section.html): Use DeletePlacementGroup with a CLI
- [DeleteRoute](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_DeleteRoute_section.html): Use DeleteRoute with a CLI
- [DeleteRouteTable](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_DeleteRouteTable_section.html): Use DeleteRouteTable with a CLI
- [DeleteSecurityGroup](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_DeleteSecurityGroup_section.html): Use DeleteSecurityGroup with an AWS SDK or CLI
- [DeleteSnapshot](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_DeleteSnapshot_section.html): Use DeleteSnapshot with an AWS SDK or CLI
- [DeleteSpotDatafeedSubscription](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_DeleteSpotDatafeedSubscription_section.html): Use DeleteSpotDatafeedSubscription with a CLI
- [DeleteSubnet](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_DeleteSubnet_section.html): Use DeleteSubnet with a CLI
- [DeleteTags](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_DeleteTags_section.html): Use DeleteTags with a CLI
- [DeleteVolume](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_DeleteVolume_section.html): Use DeleteVolume with a CLI
- [DeleteVpc](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_DeleteVpc_section.html): Use DeleteVpc with an AWS SDK or CLI
- [DeleteVpcEndpoints](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_DeleteVpcEndpoints_section.html): Use DeleteVpcEndpoints with an AWS SDK or CLI
- [DeleteVpnConnection](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_DeleteVpnConnection_section.html): Use DeleteVpnConnection with a CLI
- [DeleteVpnConnectionRoute](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_DeleteVpnConnectionRoute_section.html): Use DeleteVpnConnectionRoute with a CLI
- [DeleteVpnGateway](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_DeleteVpnGateway_section.html): Use DeleteVpnGateway with a CLI
- [DeregisterImage](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_DeregisterImage_section.html): Use DeregisterImage with a CLI
- [DescribeAccountAttributes](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_DescribeAccountAttributes_section.html): Use DescribeAccountAttributes with a CLI
- [DescribeAddresses](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_DescribeAddresses_section.html): Use DescribeAddresses with an AWS SDK or CLI
- [DescribeAvailabilityZones](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_DescribeAvailabilityZones_section.html): Use DescribeAvailabilityZones with an AWS SDK or CLI
- [DescribeBundleTasks](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_DescribeBundleTasks_section.html): Use DescribeBundleTasks with a CLI
- [DescribeCapacityReservations](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_DescribeCapacityReservations_section.html): Use DescribeCapacityReservations with a CLI
- [DescribeCustomerGateways](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_DescribeCustomerGateways_section.html): Use DescribeCustomerGateways with a CLI
- [DescribeDhcpOptions](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_DescribeDhcpOptions_section.html): Use DescribeDhcpOptions with a CLI
- [DescribeFlowLogs](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_DescribeFlowLogs_section.html): Use DescribeFlowLogs with a CLI
- [DescribeHostReservationOfferings](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_DescribeHostReservationOfferings_section.html): Use DescribeHostReservationOfferings with a CLI
- [DescribeHosts](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_DescribeHosts_section.html): Use DescribeHosts with a CLI
- [DescribeIamInstanceProfileAssociations](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_DescribeIamInstanceProfileAssociations_section.html): Use DescribeIamInstanceProfileAssociations with an AWS SDK or CLI
- [DescribeIdFormat](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_DescribeIdFormat_section.html): Use DescribeIdFormat with a CLI
- [DescribeIdentityIdFormat](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_DescribeIdentityIdFormat_section.html): Use DescribeIdentityIdFormat with a CLI
- [DescribeImageAttribute](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_DescribeImageAttribute_section.html): Use DescribeImageAttribute with a CLI
- [DescribeImages](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_DescribeImages_section.html): Use DescribeImages with an AWS SDK or CLI
- [DescribeImportImageTasks](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_DescribeImportImageTasks_section.html): Use DescribeImportImageTasks with a CLI
- [DescribeImportSnapshotTasks](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_DescribeImportSnapshotTasks_section.html): Use DescribeImportSnapshotTasks with a CLI
- [DescribeInstanceAttribute](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_DescribeInstanceAttribute_section.html): Use DescribeInstanceAttribute with a CLI
- [DescribeInstanceStatus](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_DescribeInstanceStatus_section.html): Use DescribeInstanceStatus with an AWS SDK or CLI
- [DescribeInstanceTypes](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_DescribeInstanceTypes_section.html): Use DescribeInstanceTypes with an AWS SDK or CLI
- [DescribeInstances](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_DescribeInstances_section.html): Use DescribeInstances with an AWS SDK or CLI
- [DescribeInternetGateways](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_DescribeInternetGateways_section.html): Use DescribeInternetGateways with a CLI
- [DescribeKeyPairs](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_DescribeKeyPairs_section.html): Use DescribeKeyPairs with an AWS SDK or CLI
- [DescribeNetworkAcls](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_DescribeNetworkAcls_section.html): Use DescribeNetworkAcls with a CLI
- [DescribeNetworkInterfaceAttribute](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_DescribeNetworkInterfaceAttribute_section.html): Use DescribeNetworkInterfaceAttribute with a CLI
- [DescribeNetworkInterfaces](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_DescribeNetworkInterfaces_section.html): Use DescribeNetworkInterfaces with a CLI
- [DescribePlacementGroups](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_DescribePlacementGroups_section.html): Use DescribePlacementGroups with a CLI
- [DescribePrefixLists](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_DescribePrefixLists_section.html): Use DescribePrefixLists with a CLI
- [DescribeRegions](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_DescribeRegions_section.html): Use DescribeRegions with an AWS SDK or CLI
- [DescribeRouteTables](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_DescribeRouteTables_section.html): Use DescribeRouteTables with an AWS SDK or CLI
- [DescribeScheduledInstanceAvailability](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_DescribeScheduledInstanceAvailability_section.html): Use DescribeScheduledInstanceAvailability with a CLI
- [DescribeScheduledInstances](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_DescribeScheduledInstances_section.html): Use DescribeScheduledInstances with a CLI
- [DescribeSecurityGroups](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_DescribeSecurityGroups_section.html): Use DescribeSecurityGroups with an AWS SDK or CLI
- [DescribeSnapshotAttribute](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_DescribeSnapshotAttribute_section.html): Use DescribeSnapshotAttribute with a CLI
- [DescribeSnapshots](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_DescribeSnapshots_section.html): Use DescribeSnapshots with an AWS SDK or CLI
- [DescribeSpotDatafeedSubscription](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_DescribeSpotDatafeedSubscription_section.html): Use DescribeSpotDatafeedSubscription with a CLI
- [DescribeSpotFleetInstances](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_DescribeSpotFleetInstances_section.html): Use DescribeSpotFleetInstances with a CLI
- [DescribeSpotFleetRequestHistory](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_DescribeSpotFleetRequestHistory_section.html): Use DescribeSpotFleetRequestHistory with a CLI
- [DescribeSpotFleetRequests](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_DescribeSpotFleetRequests_section.html): Use DescribeSpotFleetRequests with a CLI
- [DescribeSpotInstanceRequests](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_DescribeSpotInstanceRequests_section.html): Use DescribeSpotInstanceRequests with a CLI
- [DescribeSpotPriceHistory](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_DescribeSpotPriceHistory_section.html): Use DescribeSpotPriceHistory with a CLI
- [DescribeSubnets](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_DescribeSubnets_section.html): Use DescribeSubnets with an AWS SDK or CLI
- [DescribeTags](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_DescribeTags_section.html): Use DescribeTags with a CLI
- [DescribeVolumeAttribute](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_DescribeVolumeAttribute_section.html): Use DescribeVolumeAttribute with a CLI
- [DescribeVolumeStatus](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_DescribeVolumeStatus_section.html): Use DescribeVolumeStatus with a CLI
- [DescribeVolumes](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_DescribeVolumes_section.html): Use DescribeVolumes with a CLI
- [DescribeVpcAttribute](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_DescribeVpcAttribute_section.html): Use DescribeVpcAttribute with a CLI
- [DescribeVpcClassicLink](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_DescribeVpcClassicLink_section.html): Use DescribeVpcClassicLink with a CLI
- [DescribeVpcClassicLinkDnsSupport](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_DescribeVpcClassicLinkDnsSupport_section.html): Use DescribeVpcClassicLinkDnsSupport with a CLI
- [DescribeVpcEndpointServices](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_DescribeVpcEndpointServices_section.html): Use DescribeVpcEndpointServices with a CLI
- [DescribeVpcEndpoints](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_DescribeVpcEndpoints_section.html): Use DescribeVpcEndpoints with a CLI
- [DescribeVpcs](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_DescribeVpcs_section.html): Use DescribeVpcs with an AWS SDK or CLI
- [DescribeVpnConnections](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_DescribeVpnConnections_section.html): Use DescribeVpnConnections with a CLI
- [DescribeVpnGateways](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_DescribeVpnGateways_section.html): Use DescribeVpnGateways with a CLI
- [DetachInternetGateway](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_DetachInternetGateway_section.html): Use DetachInternetGateway with a CLI
- [DetachNetworkInterface](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_DetachNetworkInterface_section.html): Use DetachNetworkInterface with a CLI
- [DetachVolume](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_DetachVolume_section.html): Use DetachVolume with a CLI
- [DetachVpnGateway](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_DetachVpnGateway_section.html): Use DetachVpnGateway with a CLI
- [DisableVgwRoutePropagation](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_DisableVgwRoutePropagation_section.html): Use DisableVgwRoutePropagation with a CLI
- [DisableVpcClassicLink](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_DisableVpcClassicLink_section.html): Use DisableVpcClassicLink with a CLI
- [DisableVpcClassicLinkDnsSupport](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_DisableVpcClassicLinkDnsSupport_section.html): Use DisableVpcClassicLinkDnsSupport with a CLI
- [DisassociateAddress](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_DisassociateAddress_section.html): Use DisassociateAddress with an AWS SDK or CLI
- [DisassociateRouteTable](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_DisassociateRouteTable_section.html): Use DisassociateRouteTable with a CLI
- [EnableVgwRoutePropagation](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_EnableVgwRoutePropagation_section.html): Use EnableVgwRoutePropagation with a CLI
- [EnableVolumeIo](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_EnableVolumeIo_section.html): Use EnableVolumeIo with a CLI
- [EnableVpcClassicLink](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_EnableVpcClassicLink_section.html): Use EnableVpcClassicLink with a CLI
- [EnableVpcClassicLinkDnsSupport](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_EnableVpcClassicLinkDnsSupport_section.html): Use EnableVpcClassicLinkDnsSupport with a CLI
- [GetConsoleOutput](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_GetConsoleOutput_section.html): Use GetConsoleOutput with a CLI
- [GetHostReservationPurchasePreview](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_GetHostReservationPurchasePreview_section.html): Use GetHostReservationPurchasePreview with a CLI
- [GetPasswordData](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_GetPasswordData_section.html): Use GetPasswordData with an AWS SDK or CLI
- [ImportImage](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_ImportImage_section.html): Use ImportImage with a CLI
- [ImportKeyPair](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_ImportKeyPair_section.html): Use ImportKeyPair with a CLI
- [ImportSnapshot](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_ImportSnapshot_section.html): Use ImportSnapshot with a CLI
- [ModifyCapacityReservation](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_ModifyCapacityReservation_section.html): Use ModifyCapacityReservation with a CLI
- [ModifyHosts](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_ModifyHosts_section.html): Use ModifyHosts with a CLI
- [ModifyIdFormat](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_ModifyIdFormat_section.html): Use ModifyIdFormat with a CLI
- [ModifyImageAttribute](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_ModifyImageAttribute_section.html): Use ModifyImageAttribute with a CLI
- [ModifyInstanceAttribute](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_ModifyInstanceAttribute_section.html): Use ModifyInstanceAttribute with a CLI
- [ModifyInstanceCreditSpecification](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_ModifyInstanceCreditSpecification_section.html): Use ModifyInstanceCreditSpecification with a CLI
- [ModifyNetworkInterfaceAttribute](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_ModifyNetworkInterfaceAttribute_section.html): Use ModifyNetworkInterfaceAttribute with a CLI
- [ModifyReservedInstances](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_ModifyReservedInstances_section.html): Use ModifyReservedInstances with a CLI
- [ModifySnapshotAttribute](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_ModifySnapshotAttribute_section.html): Use ModifySnapshotAttribute with a CLI
- [ModifySpotFleetRequest](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_ModifySpotFleetRequest_section.html): Use ModifySpotFleetRequest with a CLI
- [ModifySubnetAttribute](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_ModifySubnetAttribute_section.html): Use ModifySubnetAttribute with a CLI
- [ModifyVolumeAttribute](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_ModifyVolumeAttribute_section.html): Use ModifyVolumeAttribute with a CLI
- [ModifyVpcAttribute](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_ModifyVpcAttribute_section.html): Use ModifyVpcAttribute with a CLI
- [MonitorInstances](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_MonitorInstances_section.html): Use MonitorInstances with an AWS SDK or CLI
- [MoveAddressToVpc](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_MoveAddressToVpc_section.html): Use MoveAddressToVpc with a CLI
- [PurchaseHostReservation](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_PurchaseHostReservation_section.html): Use PurchaseHostReservation with a CLI
- [PurchaseScheduledInstances](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_PurchaseScheduledInstances_section.html): Use PurchaseScheduledInstances with a CLI
- [RebootInstances](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_RebootInstances_section.html): Use RebootInstances with an AWS SDK or CLI
- [RegisterImage](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_RegisterImage_section.html): Use RegisterImage with a CLI
- [RejectVpcPeeringConnection](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_RejectVpcPeeringConnection_section.html): Use RejectVpcPeeringConnection with a CLI
- [ReleaseAddress](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_ReleaseAddress_section.html): Use ReleaseAddress with an AWS SDK or CLI
- [ReleaseHosts](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_ReleaseHosts_section.html): Use ReleaseHosts with a CLI
- [ReplaceIamInstanceProfileAssociation](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_ReplaceIamInstanceProfileAssociation_section.html): Use ReplaceIamInstanceProfileAssociation with an AWS SDK or CLI
- [ReplaceNetworkAclAssociation](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_ReplaceNetworkAclAssociation_section.html): Use ReplaceNetworkAclAssociation with a CLI
- [ReplaceNetworkAclEntry](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_ReplaceNetworkAclEntry_section.html): Use ReplaceNetworkAclEntry with a CLI
- [ReplaceRoute](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_ReplaceRoute_section.html): Use ReplaceRoute with a CLI
- [ReplaceRouteTableAssociation](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_ReplaceRouteTableAssociation_section.html): Use ReplaceRouteTableAssociation with a CLI
- [ReportInstanceStatus](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_ReportInstanceStatus_section.html): Use ReportInstanceStatus with a CLI
- [RequestSpotFleet](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_RequestSpotFleet_section.html): Use RequestSpotFleet with a CLI
- [RequestSpotInstances](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_RequestSpotInstances_section.html): Use RequestSpotInstances with a CLI
- [ResetImageAttribute](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_ResetImageAttribute_section.html): Use ResetImageAttribute with a CLI
- [ResetInstanceAttribute](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_ResetInstanceAttribute_section.html): Use ResetInstanceAttribute with a CLI
- [ResetNetworkInterfaceAttribute](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_ResetNetworkInterfaceAttribute_section.html): Use ResetNetworkInterfaceAttribute with a CLI
- [ResetSnapshotAttribute](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_ResetSnapshotAttribute_section.html): Use ResetSnapshotAttribute with a CLI
- [RevokeSecurityGroupEgress](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_RevokeSecurityGroupEgress_section.html): Use RevokeSecurityGroupEgress with a CLI
- [RevokeSecurityGroupIngress](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_RevokeSecurityGroupIngress_section.html): Use RevokeSecurityGroupIngress with a CLI
- [RunInstances](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_RunInstances_section.html): Use RunInstances with an AWS SDK or CLI
- [RunScheduledInstances](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_RunScheduledInstances_section.html): Use RunScheduledInstances with a CLI
- [StartInstances](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_StartInstances_section.html): Use StartInstances with an AWS SDK or CLI
- [StopInstances](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_StopInstances_section.html): Use StopInstances with an AWS SDK or CLI
- [TerminateInstances](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_TerminateInstances_section.html): Use TerminateInstances with an AWS SDK or CLI
- [UnassignPrivateIpAddresses](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_UnassignPrivateIpAddresses_section.html): Use UnassignPrivateIpAddresses with a CLI
- [UnmonitorInstances](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_UnmonitorInstances_section.html): Use UnmonitorInstances with an AWS SDK or CLI
- [UpdateSecurityGroupRuleDescriptionsIngress](https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_UpdateSecurityGroupRuleDescriptionsIngress_section.html): Use UpdateSecurityGroupRuleDescriptionsIngress with a CLI

### [Scenarios](https://docs.aws.amazon.com/ec2/latest/devguide/service_code_examples_scenarios.html)

The following code examples show how to use Amazon EC2 with AWS SDKs.

- [Build and manage a resilient service](https://docs.aws.amazon.com/ec2/latest/devguide/example_cross_ResilientService_section.html): Build and manage a resilient service using an AWS SDK
- [Create a VPC with private subnets and NAT gateways](https://docs.aws.amazon.com/ec2/latest/devguide/example_vpc_GettingStartedPrivate_section.html): Create a VPC with private subnets and NAT gateways using the CLI
- [Get started with Amazon VPC](https://docs.aws.amazon.com/ec2/latest/devguide/example_vpc_GettingStartedCLI_section.html): Get started using Amazon VPC using the CLI
- [Get started with Transit Gateway](https://docs.aws.amazon.com/ec2/latest/devguide/example_vpc_TransitGatewayGettingStarted_section.html): Get started with Transit Gateway using the CLI
- [Get started with VPC IPAM](https://docs.aws.amazon.com/ec2/latest/devguide/example_vpc_GettingStartedIpam_section.html): Get started using Amazon VPC IPAM using the CLI
