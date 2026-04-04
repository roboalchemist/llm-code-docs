# Source: https://docs.datadoghq.com/security/default_rules/def-000-igl.md

---
title: Security Group should restrict SSH access from the internet
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Security Group should restrict SSH
  access from the internet
---

# Security Group should restrict SSH access from the internet

## Description{% #description %}

Restricting SSH access from the public internet is crucial for network security. SSH vulnerabilities can be exploited by attackers to gain unauthorized access to Azure Virtual Machines. Attackers can then use the compromised virtual machine to launch further attacks within the Azure Virtual Network or target networked devices outside of Azure. RDP access should be restricted to specific IP addresses, ranges, or encrypted network tunnels.

## Remediation{% #remediation %}

If SSH is not explicitly required and narrowly configured for resources attached to the Network Security Group, Internet-level access to your Azure resources should be restricted or eliminated.

To reconfigure SSH access in Azure Security Groups, follow these steps:

1. Log in to the Azure portal at [https://portal.azure.com](https://portal.azure.com) and navigate to the **Azure Security Group** that contains the virtual machine(s) you want to modify.

1. In the Security Group settings, locate the inbound or inbound security rules section depending on your desired configuration.

1. Look for the specific rule that allows SSH access from the internet. This is usually denoted by the source IP set to "Internet", "Any" or "0.0.0.0/0".

1. Edit the rule and update the source IP to a more restricted range or a specific IP address that is allowed to initiate SSH connections. Alternatively, you can remove the rule altogether if SSH access is not required from the internet.

1. Save the changes to the Security Group.

For internal access to relevant resources, consider configuring an encrypted network tunnel using one of the following options:

1. **ExpressRoute**: To establish a private connection between your on-premises network and Azure, you can utilize ExpressRoute. This provides a dedicated and reliable connection with higher security and better network performance. Read about [ExpressRoute](https://azure.microsoft.com/services/expressroute/) to learn more.

1. **Site-to-site VPN**: You can set up a site-to-site VPN to connect your on-premises network to Azure securely. This creates an encrypted tunnel over the internet, allowing you to access Azure resources securely as if they were on the same network. For more information, read [create a site-to-site VPN](https://docs.microsoft.com/azure/vpn-gateway/vpn-gateway-howto-site-to-site-resource-manager-portal).

1. **Point-to-site VPN**: This option enables secure connections between individual devices and Azure resources. Point-to-site VPN allows remote clients to connect to Azure securely over the internet. To learn more, read [configuring a point-to-site VPN](https://docs.microsoft.com/azure/vpn-gateway/vpn-gateway-howto-point-to-site-resource-manager-portal).
