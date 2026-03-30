# Source: https://docs.aws.amazon.com/directconnect/latest/UserGuide/llms.txt

# AWS Direct Connect User Guide

> Direct Connect links your internal network to an Direct Connect location over fiber-optic cable. One end of the cable is connected to your router and the other to an Direct Connect router. With this connection in place, you can create virtual interfaces directly to the AWS cloud (for example, to Amazon EC2 and Amazon S3), bypassing Internet service providers in your network path.

- [Direct Connect maintenance](https://docs.aws.amazon.com/directconnect/latest/UserGuide/dx-maintenance.html)
- [Cross connects](https://docs.aws.amazon.com/directconnect/latest/UserGuide/Colocation.html)
- [Tag resources](https://docs.aws.amazon.com/directconnect/latest/UserGuide/using-tags.html)
- [Use the AWS CLI](https://docs.aws.amazon.com/directconnect/latest/UserGuide/using-cli.html)
- [Log API calls](https://docs.aws.amazon.com/directconnect/latest/UserGuide/logging_dc_api_calls.html)
- [Direct Connect quotas](https://docs.aws.amazon.com/directconnect/latest/UserGuide/limits.html)
- [Document history](https://docs.aws.amazon.com/directconnect/latest/UserGuide/AboutThisGuide.html)

## [What is Direct Connect?](https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html)

- [Access to remote AWS Regions](https://docs.aws.amazon.com/directconnect/latest/UserGuide/remote_regions.html): Access public and private resources in a remote Region.

### [Routing policies and BGP communities](https://docs.aws.amazon.com/directconnect/latest/UserGuide/routing-and-bgp.html)

Understand the routing policies and BGP communities that are supported by Direct Connect.

- [Long ASN support](https://docs.aws.amazon.com/directconnect/latest/UserGuide/long-asn-support.html): Support for long ASNs (4-byte) allows you to configure long Autonomous System Numbers (ASNs) as part of the parameters of the BGP session established between the AWS network device and your network device.
- [Private virtual interface routing example](https://docs.aws.amazon.com/directconnect/latest/UserGuide/private-transit-vif-example.html): This shows an example of a Direct Connect private virtual interface routing.


## [Connection options](https://docs.aws.amazon.com/directconnect/latest/UserGuide/connection_options.html)

### [AWS Direct Connect Resiliency Toolkit](https://docs.aws.amazon.com/directconnect/latest/UserGuide/resiliency_toolkit.html)

Use the AWS Direct Connect Resiliency Toolkit to configure, test, and monitor your connectivity to AWS.

- [Configure maximum resiliency](https://docs.aws.amazon.com/directconnect/latest/UserGuide/max-resiliency-set-up.html): Use the AWS Direct Connect Resiliency Toolkit to configure maximum resiliency in Direct Connect.
- [Configure high resiliency](https://docs.aws.amazon.com/directconnect/latest/UserGuide/high-resiliency-set-up.html): Use the AWS Direct Connect Resiliency Toolkit to configure high resiliency in Direct Connect.
- [Configure development and test resiliency](https://docs.aws.amazon.com/directconnect/latest/UserGuide/devtest-resiliency-set-up.html): Use the AWS Direct Connect Resiliency Toolkit for development and test resiliency.

### [Direct Connect failover test](https://docs.aws.amazon.com/directconnect/latest/UserGuide/resiliency_failover.html)

Use the Direct Connect failover test to verify that your configuration meets your resiliency requirements.

- [Start a virtual interface failover test](https://docs.aws.amazon.com/directconnect/latest/UserGuide/start_failover_test.html): Use the AWS Direct Connect Resiliency Toolkit to start a virtual interface failover test.
- [View a virtual interface failover test history](https://docs.aws.amazon.com/directconnect/latest/UserGuide/view_failover_test.html): Use the AWS Direct Connect Resiliency Toolkit to view the failover test history for a virtual interface.
- [Stop a virtual interface failover test](https://docs.aws.amazon.com/directconnect/latest/UserGuide/stop_failover_test.html): Use the AWS Direct Connect Resiliency Toolkit to stop a virtual interface failover test.

### [Classic connection](https://docs.aws.amazon.com/directconnect/latest/UserGuide/classic_connection.html)

Use the AWS Direct Connect Resiliency Toolkit to configure, test, and monitor your connectivity to AWS.

- [Configure a Classic connection](https://docs.aws.amazon.com/directconnect/latest/UserGuide/toolkit-classic.html): Configure a Classic connection in Direct Connect.


## [MAC security (MACsec)](https://docs.aws.amazon.com/directconnect/latest/UserGuide/MACsec.html)

- [Get started with MACsec on a dedicated connection](https://docs.aws.amazon.com/directconnect/latest/UserGuide/create-macsec-dedicated.html): Learn how to use MACsec on a dedicated Direct Connect connection.


## [Dedicated and hosted connections](https://docs.aws.amazon.com/directconnect/latest/UserGuide/WorkingWithConnections.html)

### [Dedicated connections](https://docs.aws.amazon.com/directconnect/latest/UserGuide/dedicated_connection.html)

Create a Direct Connect dedicated connection.

- [Create a connection using the Connection wizard](https://docs.aws.amazon.com/directconnect/latest/UserGuide/create-connection.html): Create a Direct Connect dedicated connection using the Connection wizard.
- [Download the LOA-CFA](https://docs.aws.amazon.com/directconnect/latest/UserGuide/download-loa-cfa.html): Download the Letter of Authorization and Connecting Facility Assignment (LOA-CFA) that allows you to establish a cross connect to an AWS colocation.
- [Associate a MACsec CKN/CAK with a connection](https://docs.aws.amazon.com/directconnect/latest/UserGuide/associate-key-connection.html): Create an association between a connection and a MACsec key.
- [Remove the association between a MACsec secret key and a connection](https://docs.aws.amazon.com/directconnect/latest/UserGuide/disassociate-key-connection.html): Remove an association between a connection and a MACsec key.

### [Hosted connections](https://docs.aws.amazon.com/directconnect/latest/UserGuide/hosted_connection.html)

Learn about Direct Connect hosted connections.

- [Accept a hosted connection](https://docs.aws.amazon.com/directconnect/latest/UserGuide/accept-hosted-connection.html): Accept a hosted connection provisioned by an AWS Direct Connect Partner.
- [Delete a connection](https://docs.aws.amazon.com/directconnect/latest/UserGuide/deleteconnection.html): Delete a connection to stop all port hour charges.
- [Update a connection](https://docs.aws.amazon.com/directconnect/latest/UserGuide/updateconnection.html): Update the connection name, add a tag, or remove a tag.
- [View connection details](https://docs.aws.amazon.com/directconnect/latest/UserGuide/viewdetails.html): View information about your connection.


## [Virtual interfaces and hosted virtual interfaces](https://docs.aws.amazon.com/directconnect/latest/UserGuide/WorkingWithVirtualInterfaces.html)

### [Virtual interfaces](https://docs.aws.amazon.com/directconnect/latest/UserGuide/create-vif.html)

Create a public, private, or transit virtual interface in Direct Connect.

- [Create a public virtual interface](https://docs.aws.amazon.com/directconnect/latest/UserGuide/create-public-vif.html): Create a Direct Connect public virtual interface.
- [Create a private virtual interface](https://docs.aws.amazon.com/directconnect/latest/UserGuide/create-private-vif.html): Provision a private virtual interface to a virtual private gateway in the same region as your Direct Connect connection.
- [Create a transit virtual interface to the Direct Connect gateway](https://docs.aws.amazon.com/directconnect/latest/UserGuide/create-transit-vif-dx.html): Create a transit virtual interface to a Direct Connect gateway.
- [Download the router configuration file](https://docs.aws.amazon.com/directconnect/latest/UserGuide/vif-router-config.html): Download the Direct Connect router configuration in order to use a virtual interface.

### [Hosted virtual interfaces](https://docs.aws.amazon.com/directconnect/latest/UserGuide/hosted-vif.html)

Learn about using Direct Connect hosted connections with multiple accounts.

- [Create a hosted private virtual interface](https://docs.aws.amazon.com/directconnect/latest/UserGuide/create-hosted-private-vif.html): Create a hosted private virtual interface in Direct Connect.
- [Create a hosted public virtual interface](https://docs.aws.amazon.com/directconnect/latest/UserGuide/create-hosted-public-vif.html): Create a hosted public virtual interface in Direct Connect.
- [Create a hosted transit virtual interface](https://docs.aws.amazon.com/directconnect/latest/UserGuide/create-hosted-transit-vif.html): Create a hosted transit virtual interface in Direct Connect.
- [View virtual interface details](https://docs.aws.amazon.com/directconnect/latest/UserGuide/viewvifdetails.html): View the current status of your Direct Connect virtual interface.
- [Add a BGP peer](https://docs.aws.amazon.com/directconnect/latest/UserGuide/add-peer-to-vif.html): Add an IPv4 or IPv6 BGP peering session to your Direct Connect virtual interface.
- [Delete a BGP peer](https://docs.aws.amazon.com/directconnect/latest/UserGuide/delete-bgp-peer-vif.html): Delete a BGP peer in Direct Connect.
- [Set the MTU of a private virtual interface](https://docs.aws.amazon.com/directconnect/latest/UserGuide/interface-set-mtu.html): Set the maximum transmission units (MTU) of a private virtual interface in Direct Connect.
- [Add or remove virtual interface tags](https://docs.aws.amazon.com/directconnect/latest/UserGuide/modify-tags-vif.html): Add or remove virtual interface tags in Direct Connect.
- [Delete a virtual interface](https://docs.aws.amazon.com/directconnect/latest/UserGuide/deletevif.html): Delete a Direct Connect virtual interface.
- [Accept a hosted virtual interface](https://docs.aws.amazon.com/directconnect/latest/UserGuide/accepthostedvirtualinterface.html): Accept a Direct Connect hosted virtual interface.
- [Migrate a virtual interface](https://docs.aws.amazon.com/directconnect/latest/UserGuide/migratevirtualinterface.html): Migrate a virtual interface to a new Direct Connect connection or LAG.


## [Link aggregation groups (LAGs)](https://docs.aws.amazon.com/directconnect/latest/UserGuide/lags.html)

- [Create a LAG](https://docs.aws.amazon.com/directconnect/latest/UserGuide/create-lag.html): Create a LAG from existing connections, or with new connections, in Direct Connect.
- [View LAG details](https://docs.aws.amazon.com/directconnect/latest/UserGuide/view-lag.html): View Direct Connect LAG details.
- [Update a LAG](https://docs.aws.amazon.com/directconnect/latest/UserGuide/update-lag.html): Update the name or the minimum operational connections threshold for your LAG, or add or remove a tag, in Direct Connect.
- [Associate a connection with a LAG](https://docs.aws.amazon.com/directconnect/latest/UserGuide/associate-connection-with-lag.html): Associate a connection with a LAG in Direct Connect.
- [Disassociate a connection from a LAG](https://docs.aws.amazon.com/directconnect/latest/UserGuide/disassociate-connection-from-lag.html): Disassociate a connection from a LAG in Direct Connect.
- [Associate a MACsec CKN/CAK with a LAG](https://docs.aws.amazon.com/directconnect/latest/UserGuide/associate-key-lag.html): Create an association between a LAG and a MACsec key in Direct Connect.
- [Remove the association between a MACsec secret key and a LAG](https://docs.aws.amazon.com/directconnect/latest/UserGuide/disassociate-key-lag.html): Remove an association between a LAG and a MACsec key in Direct Connect.
- [Delete a LAG](https://docs.aws.amazon.com/directconnect/latest/UserGuide/delete-lag.html): Delete a LAG.


## [Gateways](https://docs.aws.amazon.com/directconnect/latest/UserGuide/direct-connect-gateways.html)

### [Direct Connect gateways](https://docs.aws.amazon.com/directconnect/latest/UserGuide/direct-connect-gateways-intro.html)

Use a Direct Connect gateway to connect VPCs when you have either a virtual private gateway or multiple VPCs in the same Region.

- [Create a Direct Connect gateway](https://docs.aws.amazon.com/directconnect/latest/UserGuide/create-direct-connect-gateway.html): Create a Direct Connect gateway.
- [Migrate from a virtual private gateway to a Direct Connect gateway](https://docs.aws.amazon.com/directconnect/latest/UserGuide/migrate-to-direct-connect-gateway.html): Migrate from a virtual private gateway to a Direct Connect gateway.
- [Delete a Direct Connect gateway](https://docs.aws.amazon.com/directconnect/latest/UserGuide/delete-direct-connect-gateway.html): Delete a Direct Connect gateway.

### [Virtual private gateway associations](https://docs.aws.amazon.com/directconnect/latest/UserGuide/virtualgateways.html)

Use a Direct Connect gateway to connect over a private virtual interface to one or more VPCs in any account that are located in the same or different Regions.

- [Create a virtual private gateway](https://docs.aws.amazon.com/directconnect/latest/UserGuide/create-virtual-private-gateway.html): Create a virtual private gateway in Direct Connect.
- [Associate or disassociate virtual private gateways](https://docs.aws.amazon.com/directconnect/latest/UserGuide/associate-vgw-with-direct-connect-gateway.html): Associate or disassociate virtual private gateways in Direct Connect.
- [Create a private virtual interface to the Direct Connect gateway](https://docs.aws.amazon.com/directconnect/latest/UserGuide/create-private-vif-for-gateway.html): Create a private virtual interface to the Direct Connect gateway.
- [Associate a virtual private gateway across accounts](https://docs.aws.amazon.com/directconnect/latest/UserGuide/multi-account-associate-vgw.html): Associate a virtual private gateway across accounts in Direct Connect.

### [Transit gateway associations](https://docs.aws.amazon.com/directconnect/latest/UserGuide/direct-connect-transit-gateways.html)

Connect an Direct Connect gateway and a transit gateway to have a single connection from your VPCs or VPNs to your Direct Connect connection.

- [Associate or disassociate a transit gateway with Direct Connect.](https://docs.aws.amazon.com/directconnect/latest/UserGuide/associate-tgw-with-direct-connect-gateway.html): Associate or disassociate a transit gateway in Direct Connect.
- [Create a transit virtual interface to the Direct Connect gateway](https://docs.aws.amazon.com/directconnect/latest/UserGuide/create-transit-vif-for-gateway.html): Create a transit virtual interface to a Direct Connect gateway.
- [Create a transit gateway association proposal](https://docs.aws.amazon.com/directconnect/latest/UserGuide/multi-account-tgw-create-proposal.html): Create a transit gateway association proposal in Direct Connect.
- [Accept or reject a transit gateway association proposal](https://docs.aws.amazon.com/directconnect/latest/UserGuide/multi-account-tgw-accept-reject-proposal.html): Accept or reject a transit gateway association proposal in Direct Connect.
- [Update the allowed prefixes for a transit gateway association](https://docs.aws.amazon.com/directconnect/latest/UserGuide/multi-account-tgw-update-proposal-routes.html): Update the allowed prefixes for a transit gateway association in Direct Connect.
- [Delete a transit gateway association proposal](https://docs.aws.amazon.com/directconnect/latest/UserGuide/multi-account-tgw-delete-proposal.html): Delete a transit gateway association proposal in Direct Connect.

### [Cloud WAN core network associations](https://docs.aws.amazon.com/directconnect/latest/UserGuide/direct-connect-cloud-wan.html)

Connect a Direct Connect gateway to a Cloud WAN core network to create and manage a single connection to a Cloud WAN core network.

- [Verify a Direct Connect gateway association](https://docs.aws.amazon.com/directconnect/latest/UserGuide/edit-cloudwan-with-direct-connect-gateway.html): Verify that a Direct Connect gateway is associated with a Cloud WAN core network.
- [Allowed prefixes interactions](https://docs.aws.amazon.com/directconnect/latest/UserGuide/allowed-to-prefixes.html): Learn how allowed prefixes interact with transit gateways and virtual private gateways in Direct Connect.


## [Security](https://docs.aws.amazon.com/directconnect/latest/UserGuide/security.html)

### [Data protection](https://docs.aws.amazon.com/directconnect/latest/UserGuide/data-protection.html)

Configure AWS Direct Connect to meet your security and compliance objectives, and learn how to use other AWS services that help you to secure your Direct Connect resources.

- [Internetwork traffic privacy](https://docs.aws.amazon.com/directconnect/latest/UserGuide/encryption-at-rest.html): Learn how AWS Direct Connect isolates service traffic.
- [Encryption](https://docs.aws.amazon.com/directconnect/latest/UserGuide/encryption-in-transit.html): Learn how AWS Direct Connect encrypts data in transit.

### [Identity and Access Management](https://docs.aws.amazon.com/directconnect/latest/UserGuide/security-iam.html)

How to authenticate requests and manage access to your Direct Connect resources.

- [How Direct Connect works with IAM](https://docs.aws.amazon.com/directconnect/latest/UserGuide/security_iam_service-with-iam.html): Learn how Direct Connectworks with IAM

### [Identity-based policy examples for Direct Connect](https://docs.aws.amazon.com/directconnect/latest/UserGuide/security_iam_id-based-policy-examples.html)

This section shows examples of identity-based policies for Direct Connect.

- [Tag-based condition keys](https://docs.aws.amazon.com/directconnect/latest/UserGuide/security_iam_resource-based-policy-examples.html): Used tag-based condition keys in Direct Connect.
- [Service-linked roles](https://docs.aws.amazon.com/directconnect/latest/UserGuide/using-service-linked-roles.html): Learn how to use service-linked roles to give Direct Connect access to resources in your AWS account.
- [AWS managed policies](https://docs.aws.amazon.com/directconnect/latest/UserGuide/security-iam-awsmanpol.html): Learn about AWS managed policies for Direct Connect and recent changes to those policies.
- [Troubleshooting](https://docs.aws.amazon.com/directconnect/latest/UserGuide/security_iam_troubleshoot.html): Troubleshoot identity and access issues in Direct Connect.
- [Logging and monitoring](https://docs.aws.amazon.com/directconnect/latest/UserGuide/dc-incident-response.html): Use automated monitoring and logging tools to watch your Direct Connect connections.
- [Compliance validation](https://docs.aws.amazon.com/directconnect/latest/UserGuide/DirectConnect-compliance.html): Learn what AWS services are in scope of a specific compliance program.
- [Resilience in Direct Connect](https://docs.aws.amazon.com/directconnect/latest/UserGuide/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and learn about specific AWS Direct Connect features for data resiliency.
- [Infrastructure security](https://docs.aws.amazon.com/directconnect/latest/UserGuide/infrastructure-security.html): Learn how AWS Direct Connect isolates service traffic.


## [Monitor Direct Connect resources](https://docs.aws.amazon.com/directconnect/latest/UserGuide/monitoring-overview.html)

### [Monitor with Amazon CloudWatch](https://docs.aws.amazon.com/directconnect/latest/UserGuide/monitoring-cloudwatch.html)

Monitor your physical Direct Connect connections and virtual interfaces with CloudWatch.

- [View Direct Connect CloudWatch metrics](https://docs.aws.amazon.com/directconnect/latest/UserGuide/viewing-metrics.html): View Direct Connect CloudWatch metrics.
- [Create alarms to monitor connections](https://docs.aws.amazon.com/directconnect/latest/UserGuide/creating-alarms.html): Create CloudWatch alarms to monitor Direct Connect connections.


## [Troubleshooting](https://docs.aws.amazon.com/directconnect/latest/UserGuide/Troubleshooting.html)

- [Layer 1 (physical) issues](https://docs.aws.amazon.com/directconnect/latest/UserGuide/ts_layer_1.html): If you or your network provider are having difficulty establishing physical connectivity to an Direct Connect device, use the following steps to troubleshoot the issue.
- [Layer 2 (data link) issues](https://docs.aws.amazon.com/directconnect/latest/UserGuide/ts-layer-2.html): If your Direct Connect physical connection is up but your virtual interface is down, use the following steps to troubleshoot the issue.
- [Layer 3/4 (Network/Transport) issues](https://docs.aws.amazon.com/directconnect/latest/UserGuide/ts-layer-3.html): Consider a situation where your Direct Connect physical connection is up and you can ping the Amazon peer IP address.
- [Long ASN issues](https://docs.aws.amazon.com/directconnect/latest/UserGuide/ts-long-asn.html): If you are experiencing issues with long ASN configurations, use the following steps to troubleshoot:
- [Routing issues](https://docs.aws.amazon.com/directconnect/latest/UserGuide/ts-routing.html): Consider a situation where your virtual interface is up and you've established a BGP peering session.
