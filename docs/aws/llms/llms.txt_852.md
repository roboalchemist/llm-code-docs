# Source: https://docs.aws.amazon.com/vpn/latest/s2svpn/llms.txt

# AWS Site-to-Site VPN User Guide

> Describes key concepts of AWS Site-to-Site VPN and provides instructions for using the features of Site-to-Site VPN.

- [What is AWS Site-to-Site VPN?](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html)
- [Get started with Site-to-Site VPN](https://docs.aws.amazon.com/vpn/latest/s2svpn/SetUpVPNConnections.html)
- [Quotas](https://docs.aws.amazon.com/vpn/latest/s2svpn/vpn-limits.html)
- [Document history](https://docs.aws.amazon.com/vpn/latest/s2svpn/WhatsNew.html)

## [How Site-to-Site VPN works](https://docs.aws.amazon.com/vpn/latest/s2svpn/how_it_works.html)

### [VPN tunnel options](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPNTunnels.html)

Learn about the different tunnel options for your Site-to-Site VPN connection.

- [Configure tunnel options](https://docs.aws.amazon.com/vpn/latest/s2svpn/tunnel-configure.html): Learn about the different tunnel options for your Site-to-Site VPN connection.
- [VPN tunnel authentication options](https://docs.aws.amazon.com/vpn/latest/s2svpn/vpn-tunnel-authentication-options.html): Explore VPN tunnel authentication options, detailing pre-shared keys and private certificate methods for Site-to-Site VPN VPNs.
- [VPN tunnel initiation options](https://docs.aws.amazon.com/vpn/latest/s2svpn/initiate-vpn-tunnels.html): Learn the options for the Internet Key Exchange (IKE) negotiation process when initiating Site-to-Site VPN tunnels.

### [Endpoint replacements](https://docs.aws.amazon.com/vpn/latest/s2svpn/endpoint-replacements.html)

Learn how your tunnel endpoints are affected during tunnel updates or modifications to your Site-to-Site VPN connection.

### [Tunnel endpoint lifecycle](https://docs.aws.amazon.com/vpn/latest/s2svpn/tunnel-endpoint-lifecycle.html)

Learn how to control the schedule of tunnel endpoint replacements for your Site-to-Site VPN connection.

- [Enable tunnel endpoint lifecycle control](https://docs.aws.amazon.com/vpn/latest/s2svpn/enable-elc.html): Enable tunnel endpoint lifecycle control for a Site-to-Site VPN connection.
- [Verify if tunnel endpoint lifecycle control is enabled](https://docs.aws.amazon.com/vpn/latest/s2svpn/view-elc-status.html): Verify tunnel endpoint lifecycle control for a Site-to-Site VPN connection.
- [Check for available updates](https://docs.aws.amazon.com/vpn/latest/s2svpn/view-elc-updates.html): Check for available Site-to-Site VPN tunnel updates.
- [Accept a maintenance update](https://docs.aws.amazon.com/vpn/latest/s2svpn/accept-update.html): Accept a tunnel maintenance update for a Site-to-Site VPN connection.
- [Turn tunnel endpoint lifecycle control off](https://docs.aws.amazon.com/vpn/latest/s2svpn/turn-elc-off.html): Turn off endpoint lifecycle control for a Site-to-Site VPN connection.
- [Customer gateway options](https://docs.aws.amazon.com/vpn/latest/s2svpn/cgw-options.html): Learn about the options you can configure for your customer gateway.
- [Accelerated VPN connections](https://docs.aws.amazon.com/vpn/latest/s2svpn/accelerated-vpn.html): Understand the key concepts, benefits, behavior, and requirements for accelerated Site-to-Site VPN connections.

### [Site-to-Site VPN routing options](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPNRoutingTypes.html)

Information about static and dynamic routing options for Site-to-Site VPN, routing priority and tunnel endpoint updates.

- [Static and dynamic routing](https://docs.aws.amazon.com/vpn/latest/s2svpn/vpn-static-dynamic.html): Learn about static and dynamic routing in Site-to-Site VPN.
- [Route tables and route priority](https://docs.aws.amazon.com/vpn/latest/s2svpn/vpn-route-priority.html): Learn about route tables and route priority in Site-to-Site VPN.
- [Routing during VPN tunnel endpoint updates](https://docs.aws.amazon.com/vpn/latest/s2svpn/routing-vpn-tunnel-updates.html): Learn about routing while a VPN tunnel endpoint is being updated.
- [IPv4 and IPv6 traffic](https://docs.aws.amazon.com/vpn/latest/s2svpn/ipv4-ipv6.html): Configure support for IPv6 traffic on your VPN tunnels.
- [VPN Concentrators](https://docs.aws.amazon.com/vpn/latest/s2svpn/vpn-concentrator.html): Use Site-to-Site VPN Concentrators to connect multiple remote sites with low bandwidth requirements to AWS cost-effectively.


## [Site-to-Site VPN architectural scenarios](https://docs.aws.amazon.com/vpn/latest/s2svpn/site-site-architectures.html)

- [Single and multiple VPN connections](https://docs.aws.amazon.com/vpn/latest/s2svpn/Examples.html): Learn about different Site-to-Site VPN architecture examples for single and multiple VPN connections.
- [Secure communications between VPN connections using VPN CloudHub](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPN_CloudHub.html): Secure communications between AWS Site-to-Site VPN connections using Site-to-Site VPN CloudHub and multiple Site-to-Site VPN connections.
- [Redundant VPN connections](https://docs.aws.amazon.com/vpn/latest/s2svpn/vpn-redundant-connection.html): Learn how you can use redundant Site-to-Site VPN connections to provide connectivity failover between AWS and on-prem networks.


## [Site-to-Site VPN customer gateway devices](https://docs.aws.amazon.com/vpn/latest/s2svpn/your-cgw.html)

- [Requirements](https://docs.aws.amazon.com/vpn/latest/s2svpn/CGRequirements.html): Understand the customer gateway device requirements for Site-to-Site VPN.
- [Best practices](https://docs.aws.amazon.com/vpn/latest/s2svpn/cgw-best-practice.html): Understand the best practices for using your customer gateway device with Site-to-Site VPN.
- [Firewall rules](https://docs.aws.amazon.com/vpn/latest/s2svpn/FirewallRules.html): Understand the requirements for firewall rules on your customer gateway device.

### [Static and dynamic routing configuration files](https://docs.aws.amazon.com/vpn/latest/s2svpn/example-configuration-files.html)

Learn general information about example configuration files customer gateway devices provided by AWS for Site-to-Site VPN connections.

### [Downloadable static routing configuration files](https://docs.aws.amazon.com/vpn/latest/s2svpn/cgw-static-routing-examples.html)

Explore example configuration files for Site-to-Site VPN connections using static routing.

- [Configure static routing](https://docs.aws.amazon.com/vpn/latest/s2svpn/cgw-static-routing-example-interface.html): Learn about user interface procedures for configuring your customer gateway device with static routing.

### [Downloadable dynamic configuration files](https://docs.aws.amazon.com/vpn/latest/s2svpn/cgw-dynamic-routing-examples.html)

Explore example configuration files for Site-to-Site VPN connections using dynamic routing.

- [Configure dynamic routing](https://docs.aws.amazon.com/vpn/latest/s2svpn/cgw-dynamic-routing-example-interface.html): Learn about user interface procedures for configuring your customer gateway device with dynamic routing.
- [Configure Windows Server as a customer gateway device](https://docs.aws.amazon.com/vpn/latest/s2svpn/customer-gateway-device-windows.html): Learn how to configure a Windows server to use as a customer gateway device for a Site-to-Site VPN connection.

### [Troubleshooting customer gateway devices](https://docs.aws.amazon.com/vpn/latest/s2svpn/Troubleshooting.html)

Learn how to troubleshoot connectivity issues with your customer gateway device.

- [Device with BGP](https://docs.aws.amazon.com/vpn/latest/s2svpn/Generic_Troubleshooting.html): Learn the troubleshooting procedure for Site-to-Site VPN connections that use Border Gateway Protocol.
- [Device without BGP](https://docs.aws.amazon.com/vpn/latest/s2svpn/Generic_Troubleshooting_noBGP.html): Learn the troubleshooting procedure for Site-to-Site VPN connections not using Border Gateway Protocol.
- [Cisco ASA](https://docs.aws.amazon.com/vpn/latest/s2svpn/Cisco_ASA_Troubleshooting.html): Troubleshoot common issues with IKE, IPsec, and routing on Site-to-Site VPN connections using Cisco ASA devices.
- [Cisco IOS](https://docs.aws.amazon.com/vpn/latest/s2svpn/Cisco_Troubleshooting.html): Troubleshoot common issues with IKE, IPsec, BGP, and routing on Site-to-Site VPN connections using Cisco IOS devices.
- [Cisco IOS without BGP](https://docs.aws.amazon.com/vpn/latest/s2svpn/Cisco_Troubleshooting_NoBGP.html): Troubleshoot common IKE, IPsec, and tunnel issues on Site-to-Site VPN connections using Cisco IOS devices without Border Gateway protocol (BGP).
- [Juniper JunOS](https://docs.aws.amazon.com/vpn/latest/s2svpn/Juniper_Troubleshooting.html): Troubleshoot common IKE, IPsec, BGP, and tunnel issues on Site-to-Site VPN connections using Juniper JunOS devices.
- [Juniper ScreenOS](https://docs.aws.amazon.com/vpn/latest/s2svpn/Juniper_ScreenOs_Troubleshooting.html): Troubleshoot the connectivity of a Site-to-Site VPN Juniper ScreenOS-based customer gateway device.
- [Yamaha](https://docs.aws.amazon.com/vpn/latest/s2svpn/Yamaha_Troubleshooting.html): Troubleshoot common IKE, IPsec, BGP, and tunnel issues on Site-to-Site VPN connections using Yamaha devices.
- [eero Integration](https://docs.aws.amazon.com/vpn/latest/s2svpn/eero-integration.html): Learn general information about eero integration with Site-to-Site VPN connections.


## [Work with Site-to-Site VPN](https://docs.aws.amazon.com/vpn/latest/s2svpn/working-with-site-site.html)

### [Create and manage VPN Concentrators](https://docs.aws.amazon.com/vpn/latest/s2svpn/create-manage-vpn-concentrators.html)

Learn how to create and manage Site-to-Site VPN Concentrators for connecting multiple remote sites.

- [Create a VPN Concentrator](https://docs.aws.amazon.com/vpn/latest/s2svpn/create-vpn-concentrator.html): Learn how to create and configure a Site-to-Site VPN Concentrator for connecting multiple remote sites.
- [Manage VPN Concentrator tags](https://docs.aws.amazon.com/vpn/latest/s2svpn/manage-vpn-concentrator-tags.html): Learn how to add, modify, and remove tags from your Site-to-Site VPN Concentrators for better organization and cost tracking.
- [Delete a VPN Concentrator](https://docs.aws.amazon.com/vpn/latest/s2svpn/delete-vpn-concentrator.html): Learn how to delete Site-to-Site VPN Concentrators when they are no longer needed.

### [Create a VPN connection](https://docs.aws.amazon.com/vpn/latest/s2svpn/create-vpn-connection.html)

Learn how to create Site-to-Site VPN connections for transit gateways and Cloud WAN.

- [Create a VPN transit gateway connection using the CLI or API](https://docs.aws.amazon.com/vpn/latest/s2svpn/create-tgw-cli-api.html): Learn how to create a transit gateway VPN attachment using the AWS CLI and API.
- [Create a VPN Cloud WAN connection using the CLI or API](https://docs.aws.amazon.com/vpn/latest/s2svpn/create-cwan-vpn-attachment.html): Learn the procedure for creating an attachment to connect Site-to-Site VPN to AWS Cloud WAN.
- [Create a VPN Concentrator connection using the CLI or API](https://docs.aws.amazon.com/vpn/latest/s2svpn/create-vpn-concentrator-cli-api.html): Learn how to create VPN connections that use a Site-to-Site VPN Concentrator using the AWS CLI and API.
- [View VPN connections](https://docs.aws.amazon.com/vpn/latest/s2svpn/viewing-vpn-connections.html): Learn how to view VPN connection details using the AWS Management Console, AWS CLI, and AWS API.
- [Test a VPN connection](https://docs.aws.amazon.com/vpn/latest/s2svpn/HowToTestEndToEnd_Linux.html): Learn how to test a Site-to-Site VPN connection from AWS to your on-premises network.

### [Delete a VPN connection and gateway](https://docs.aws.amazon.com/vpn/latest/s2svpn/delete-vpn.html)

Learn the procedure for how to delete a Site-to-Site VPN connection.

- [Delete a VPN connection](https://docs.aws.amazon.com/vpn/latest/s2svpn/delete-vpn-connection.html): Delete a Site-to-Site VPN connection if the connection is no longer needed.
- [Delete a customer gateway](https://docs.aws.amazon.com/vpn/latest/s2svpn/delete-cgw.html): Delete a Site-to-Site VPN customer gateway if it's no longer needed.
- [Detach and delete a virtual private gateway](https://docs.aws.amazon.com/vpn/latest/s2svpn/delete-vgw.html): Detach and delete a virtual private gateway if it's no longer needed.
- [Modify the target gateway of a VPN connection](https://docs.aws.amazon.com/vpn/latest/s2svpn/modify-vpn-target.html): Learn the steps required to modify the target gateway of an existing Site-to-Site VPN connection.
- [Modify VPN connection options](https://docs.aws.amazon.com/vpn/latest/s2svpn/modify-vpn-connection-options.html): Modify the connection options for your Site-to-Site VPN connection.
- [Modify VPN tunnel options](https://docs.aws.amazon.com/vpn/latest/s2svpn/modify-vpn-tunnel-options.html): Learn how to modify the tunnel options for your Site-to-Site VPN connection.
- [Edit static routes for a VPN connection](https://docs.aws.amazon.com/vpn/latest/s2svpn/vpn-edit-static-routes.html): Learn how to add or remove static routes from a Site-to-Site VPN connection.
- [Change the customer gateway for a VPN connection](https://docs.aws.amazon.com/vpn/latest/s2svpn/change-vpn-cgw.html): Learn the procedure for changing the customer gateway on a Site-to-Site VPN connection.
- [Replace compromised credentials](https://docs.aws.amazon.com/vpn/latest/s2svpn/CompromisedCredentials.html): Replace the tunnel credentials for your Site-to-Site VPN connection.
- [Rotate VPN tunnel endpoint certificates](https://docs.aws.amazon.com/vpn/latest/s2svpn/rotate-vpn-certificate.html): Learn how Site-to-Site VPN certificates get rotated.

### [Private IP VPN with Direct Connect](https://docs.aws.amazon.com/vpn/latest/s2svpn/private-ip-dx.html)

Understand the key concepts, benefits, behavior, and requirements for using private IP addresses with a Site-to-Site VPN and Direct Connect.

- [Create a private IP VPN over Direct Connect](https://docs.aws.amazon.com/vpn/latest/s2svpn/private-ip-dx-steps.html): Create a private IP VPN connection over Direct Connect.


## [Security](https://docs.aws.amazon.com/vpn/latest/s2svpn/security.html)

### [Enhanced security features using Secrets Manager](https://docs.aws.amazon.com/vpn/latest/s2svpn/enhanced-security.html)

AWS Site-to-Site VPN's Security Rebase feature provides enhanced security capabilities that gives you greater control and visibility over your VPN connections.

- [Change the Secrets Manager pre-shared key](https://docs.aws.amazon.com/vpn/latest/s2svpn/enhanced-security-tunnel.html): If your tunnel is inaccessible in Secrets Manager, you can change the pre-shared key for that tunnel.
- [Change the pre-shared key storage mode](https://docs.aws.amazon.com/vpn/latest/s2svpn/enhanced-security-storage.html): Change the pre-shared key storage mode for an existing VPN tunnel.
- [Data protection](https://docs.aws.amazon.com/vpn/latest/s2svpn/data-protection.html): Learn how the AWS shared responsibility model applies to data protection in Site-to-Site VPN.

### [Identity and access management](https://docs.aws.amazon.com/vpn/latest/s2svpn/security-iam.html)

Control access to Site-to-Site VPN resources using IAM.

- [How AWS Site-to-Site VPN works with IAM](https://docs.aws.amazon.com/vpn/latest/s2svpn/security_iam_service-with-iam.html): Learn how the IAM service works with the Site-to-Site VPN service.
- [Identity-based policy examples](https://docs.aws.amazon.com/vpn/latest/s2svpn/security_iam_id-based-policy-examples.html): Learn how to use identity-based policies to grant users and roles access to Site-to-Site VPN.
- [Troubleshooting](https://docs.aws.amazon.com/vpn/latest/s2svpn/security_iam_troubleshoot.html): Troubleshoot common issues with IAM in Site-to-Site VPN.
- [AWS managed policies](https://docs.aws.amazon.com/vpn/latest/s2svpn/s2s-security-iam-awsmanpol.html): Learn about AWS managed policies for AWS Site-to-Site VPN and recent changes to those policies.
- [Using service-linked roles](https://docs.aws.amazon.com/vpn/latest/s2svpn/using-service-linked-roles.html): How to use service-linked roles to give Site-to-Site VPN access to resources in your AWS account.
- [Resilience](https://docs.aws.amazon.com/vpn/latest/s2svpn/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and learn about specific AWS Site-to-Site VPN features for data resiliency.
- [Infrastructure security](https://docs.aws.amazon.com/vpn/latest/s2svpn/infrastructure-security.html): Learn how Site-to-Site VPN isolates service traffic.


## [Monitor a Site-to-Site VPN connection](https://docs.aws.amazon.com/vpn/latest/s2svpn/monitoring-overview-vpn.html)

### [Site-to-Site VPN logs](https://docs.aws.amazon.com/vpn/latest/s2svpn/monitoring-logs.html)

Describes what Site-to-Site VPN logs are available, and how to use the logging feature.

- [View Site-to-Site VPN logs configuration](https://docs.aws.amazon.com/vpn/latest/s2svpn/status-logs.html): View Site-to-Site VPN configuration details for your connections.
- [Enable Site-to-Site VPN logs](https://docs.aws.amazon.com/vpn/latest/s2svpn/enable-logs.html): Enable Site-to-Site VPN logs to log VPN activity, such as tunnel state and other details.
- [Disable Site-to-Site VPN logs](https://docs.aws.amazon.com/vpn/latest/s2svpn/disable-logs.html): Disable VPN logging on a connection if you no longer want to track any activity on that connection.

### [Monitor Site-to-Site VPN tunnels using CloudWatch](https://docs.aws.amazon.com/vpn/latest/s2svpn/monitoring-cloudwatch-vpn.html)

Learn how to use Amazon CloudWatch to monitor Site-to-Site VPN vpn tunnels.

- [View VPN CloudWatch metrics](https://docs.aws.amazon.com/vpn/latest/s2svpn/viewing-metrics.html): View CloudWatch metrics for a Site-to-Site VPN connection.
- [Create CloudWatch alarms to monitor VPN tunnels](https://docs.aws.amazon.com/vpn/latest/s2svpn/creating-alarms-vpn.html): Create CloudWatch alarms for a Site-to-Site VPN connection.
- [AWS Health and Site-to-Site VPN events](https://docs.aws.amazon.com/vpn/latest/s2svpn/monitoring-vpn-health-events.html): Learn how AWS Site-to-Site VPN sends notifications to the Health Dashboard when one or both of your tunnel endpoints is replaced.
