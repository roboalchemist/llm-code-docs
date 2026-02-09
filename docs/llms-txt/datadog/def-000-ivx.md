# Source: https://docs.datadoghq.com/security/default_rules/def-000-ivx.md

---
title: Security Group should restrict UDP access from the internet
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Security Group should restrict UDP
  access from the internet
---

# Security Group should restrict UDP access from the internet
 
## Description{% #description %}

Regular evaluation of network security groups is essential to identify and address any misconfigurations related to ports. It is important to assess the necessity of certain ports and protocols that may be exposed to the internet and restrict them if they are not explicitly required. This is crucial as broad exposure of UDP services can lead to potential security issues, such as attackers utilizing DDoS amplification techniques to cause disruptions within the Azure Virtual Network and even target external networked devices. Commonly exploited UDP-based services, including DNS, NTP, SSDP, SNMP, and CLDAP, can be used as amplification sources by attackers.

## Remediation{% #remediation %}

If UDP is not explicitly required and narrowly configured for resources attached to the Network Security Group, Internet-level access to your Azure resources should be restricted or eliminated.

To reconfigure UDP access in Azure Security Groups, follow these steps:

1. Log in to the Azure portal at [https://portal.azure.com](https://portal.azure.com) and navigate to the **Azure Security Group** that contains the virtual machine(s) you want to modify.

1. In the Security Group settings, locate the inbound or inbound security rules section depending on your desired configuration.

1. Look for the specific rule that allows UDP access from the internet. This is usually denoted by the source IP set to "Internet", "Any" or "0.0.0.0/0".

1. Edit the rule and update the source IP to a more restricted range or a specific IP address that is allowed to initiate UDP connections. Alternatively, you can remove the rule altogether if UDP access is not required from the internet.

1. Save the changes to the Security Group.

For internal access to relevant resources, consider configuring an encrypted network tunnel using one of the following options:

1. **ExpressRoute**: To establish a private connection between your on-premises network and Azure, you can utilize ExpressRoute. This provides a dedicated and reliable connection with higher security and better network performance. Read about [ExpressRoute](https://azure.microsoft.com/services/expressroute/) to learn more.

1. **Site-to-site VPN**: You can set up a site-to-site VPN to connect your on-premises network to Azure securely. This creates an encrypted tunnel over the internet, allowing you to access Azure resources securely as if they were on the same network. For more information, read [create a site-to-site VPN](https://docs.microsoft.com/azure/vpn-gateway/vpn-gateway-howto-site-to-site-resource-manager-portal).

1. **Point-to-site VPN**: This option enables secure connections between individual devices and Azure resources. Point-to-site VPN allows remote clients to connect to Azure securely over the internet. To learn more, read [configuring a point-to-site VPN](https://docs.microsoft.com/azure/vpn-gateway/vpn-gateway-howto-point-to-site-resource-manager-portal).
