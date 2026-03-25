# Source: https://learn.microsoft.com/en-us/azure/azure-web-pubsub/howto-monitor-azure-policy

Title: Azure Web PubSub service Compliance using Azure Policy

URL Source: https://learn.microsoft.com/en-us/azure/azure-web-pubsub/howto-monitor-azure-policy

Markdown Content:
[Azure Policy](https://learn.microsoft.com/en-us/azure/governance/policy/overview) is a free service in Azure to create, assign, and manage policies that enforce rules and effects to ensure your resources stay compliant with your corporate standards and service level agreements. Use these policies to audit Web PubSub resources for compliance.

This article describes the built-in policies for Azure Web PubSub Service.

The following table contains an index of Azure Policy built-in policy definitions for Azure Web PubSub. For Azure Policy built-ins for other services, see [Azure Policy built-in definitions](https://learn.microsoft.com/en-us/azure/governance/policy/samples/built-in-policies).

The name of each built-in policy definition links to the policy definition in the Azure portal. Use the link in the Version column to view the source on the [Azure Policy GitHub repo](https://github.com/Azure/azure-policy).

| Name (Azure portal) | Description | Effect(s) | Version (GitHub) |
| --- | --- | --- | --- |
| [Azure Web PubSub Service should disable public network access](https://portal.azure.com/#blade/Microsoft_Azure_Policy/PolicyDetailBlade/definitionId/%2Fproviders%2FMicrosoft.Authorization%2FpolicyDefinitions%2Fbf45113f-264e-4a87-88f9-29ac8a0aca6a) | Disabling public network access improves security by ensuring that Azure Web PubSub service isn't exposed on the public internet. Creating private endpoints can limit exposure of Azure Web PubSub service. Learn more at: [https://aka.ms/awps/networkacls](https://aka.ms/awps/networkacls). | Audit, Deny, Disabled | [1.0.0](https://github.com/Azure/azure-policy/blob/master/built-in-policies/policyDefinitions/Web%20PubSub/PublicNetworkAccessDisabled_AuditDeny.json) |
| [Azure Web PubSub Service should enable diagnostic logs](https://portal.azure.com/#blade/Microsoft_Azure_Policy/PolicyDetailBlade/definitionId/%2Fproviders%2FMicrosoft.Authorization%2FpolicyDefinitions%2Fee8a7be2-e9b5-47b9-9d37-d9b141ea78a4) | Audit enabling of diagnostic logs. This enables you to recreate activity trails to use for investigation purposes; when a security incident occurs or when your network is compromised | AuditIfNotExists, Disabled | [1.0.0](https://github.com/Azure/azure-policy/blob/master/built-in-policies/policyDefinitions/Web%20PubSub/DiagnosticLog_AINE.json) |
| [Azure Web PubSub Service should have local authentication methods disabled](https://portal.azure.com/#blade/Microsoft_Azure_Policy/PolicyDetailBlade/definitionId/%2Fproviders%2FMicrosoft.Authorization%2FpolicyDefinitions%2Fb66ab71c-582d-4330-adfd-ac162e78691e) | Disabling local authentication methods improves security by ensuring that Azure Web PubSub Service exclusively require Azure Active Directory identities for authentication. | Audit, Deny, Disabled | [1.0.0](https://github.com/Azure/azure-policy/blob/master/built-in-policies/policyDefinitions/Web%20PubSub/DisableLocalAuth_AuditDeny.json) |
| [Azure Web PubSub Service should use a SKU that supports private link](https://portal.azure.com/#blade/Microsoft_Azure_Policy/PolicyDetailBlade/definitionId/%2Fproviders%2FMicrosoft.Authorization%2FpolicyDefinitions%2F82909236-25f3-46a6-841c-fe1020f95ae1) | With supported SKU, Azure Private Link lets you connect your virtual network to Azure services without a public IP address at the source or destination. The Private Link platform handles the connectivity between the consumer and services over the Azure backbone network. By mapping private endpoints to Azure Web PubSub service, you can reduce data leakage risks. Learn more about private links at: [https://aka.ms/awps/privatelink](https://aka.ms/awps/privatelink). | Audit, Deny, Disabled | [1.0.0](https://github.com/Azure/azure-policy/blob/master/built-in-policies/policyDefinitions/Web%20PubSub/AllowedSKU_AuditDeny.json) |
| [Azure Web PubSub Service should use private link](https://portal.azure.com/#blade/Microsoft_Azure_Policy/PolicyDetailBlade/definitionId/%2Fproviders%2FMicrosoft.Authorization%2FpolicyDefinitions%2Feb907f70-7514-460d-92b3-a5ae93b4f917) | Azure Private Link lets you connect your virtual networks to Azure services without a public IP address at the source or destination. The private link platform handles the connectivity between the consumer and services over the Azure backbone network. By mapping private endpoints to your Azure Web PubSub Service, you can reduce data leakage risks. Learn more about private links at: [https://aka.ms/awps/privatelink](https://aka.ms/awps/privatelink). | Audit, Disabled | [1.0.0](https://github.com/Azure/azure-policy/blob/master/built-in-policies/policyDefinitions/Web%20PubSub/PrivateEndpointEnabled_Audit_v2.json) |
| [Configure Azure Web PubSub Service to disable local authentication](https://portal.azure.com/#blade/Microsoft_Azure_Policy/PolicyDetailBlade/definitionId/%2Fproviders%2FMicrosoft.Authorization%2FpolicyDefinitions%2F17f9d984-90c8-43dd-b7a6-76cb694815c1) | Disable local authentication methods so that your Azure Web PubSub Service exclusively requires Azure Active Directory identities for authentication. | Modify, Disabled | [1.0.0](https://github.com/Azure/azure-policy/blob/master/built-in-policies/policyDefinitions/Web%20PubSub/DisableLocalAuth_Modify.json) |
| [Configure Azure Web PubSub Service to disable public network access](https://portal.azure.com/#blade/Microsoft_Azure_Policy/PolicyDetailBlade/definitionId/%2Fproviders%2FMicrosoft.Authorization%2FpolicyDefinitions%2F5b1213e4-06e4-4ccc-81de-4201f2f7131a) | Disable public network access for your Azure Web PubSub resource so that it's not accessible over the public internet. This can reduce data leakage risks. Learn more at: [https://aka.ms/awps/networkacls](https://aka.ms/awps/networkacls). | Modify, Disabled | [1.0.0](https://github.com/Azure/azure-policy/blob/master/built-in-policies/policyDefinitions/Web%20PubSub/PublicNetworkAccessDisabled_Modify.json) |
| [Configure Azure Web PubSub Service to use private DNS zones](https://portal.azure.com/#blade/Microsoft_Azure_Policy/PolicyDetailBlade/definitionId/%2Fproviders%2FMicrosoft.Authorization%2FpolicyDefinitions%2F0b026355-49cb-467b-8ac4-f777874e175a) | Use private DNS zones to override the DNS resolution for a private endpoint. A private DNS zone links to your virtual network to resolve to Azure Web PubSub service. Learn more at: [https://aka.ms/awps/privatelink](https://aka.ms/awps/privatelink). | DeployIfNotExists, Disabled | [1.0.0](https://github.com/Azure/azure-policy/blob/master/built-in-policies/policyDefinitions/Web%20PubSub/PrivateEndpointDNSZone_DINE.json) |
| [Configure Azure Web PubSub Service with private endpoints](https://portal.azure.com/#blade/Microsoft_Azure_Policy/PolicyDetailBlade/definitionId/%2Fproviders%2FMicrosoft.Authorization%2FpolicyDefinitions%2F1b9c0b58-fc7b-42c8-8010-cdfa1d1b8544) | Private endpoints connect your virtual networks to Azure services without a public IP address at the source or destination. By mapping private endpoints to Azure Web PubSub service, you can reduce data leakage risks. Learn more about private links at: [https://aka.ms/awps/privatelink](https://aka.ms/awps/privatelink). | DeployIfNotExists, Disabled | [1.0.0](https://github.com/Azure/azure-policy/blob/master/built-in-policies/policyDefinitions/Web%20PubSub/PrivateEndpointEnabled_DINE.json) |

When assigning a policy definition:

*   You can assign policy definitions using the [Azure portal](https://learn.microsoft.com/en-us/azure/governance/policy/assign-policy-portal), [Azure CLI](https://learn.microsoft.com/en-us/azure/governance/policy/assign-policy-azurecli), a [Resource Manager template](https://learn.microsoft.com/en-us/azure/governance/policy/assign-policy-template), or the Azure Policy SDKs.
*   Policy assignments can be scoped to a resource group, a subscription, or an [Azure management group](https://learn.microsoft.com/en-us/azure/governance/management-groups/overview).
*   You can enable or disable [policy enforcement](https://learn.microsoft.com/en-us/azure/governance/policy/concepts/assignment-structure#enforcement-mode) at any time.
*   Web PubSub policy assignments apply to existing and new Web PubSub resources within the scope.

Note

After you assign or update a policy, it takes some time for the assignment to be applied to resources in the defined scope. See information about [policy evaluation triggers](https://learn.microsoft.com/en-us/azure/governance/policy/how-to/get-compliance-data#evaluation-triggers).

Access compliance information generated by your policy assignments using the Azure portal, Azure command-line tools, or the Azure Policy SDKs. For details, see [Get compliance data of Azure resources](https://learn.microsoft.com/en-us/azure/governance/policy/how-to/get-compliance-data).

When a resource is non-compliant, there are many possible reasons. To determine the reason or to find the change responsible, see [Determine non-compliance](https://learn.microsoft.com/en-us/azure/governance/policy/how-to/determine-non-compliance).

1.   Open the Azure portal and search for **Policy**.
2.   Select **Policy**.
3.   Select **Compliance**.
4.   Use the filters to display by **Scope**, **Type** or **Compliance state**. Use search list by name or ID. [![Image 1: Screenshot showing policy compliance in portal.](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/media/howto-monitor-azure-policy/azure-policy-compliance.png)](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/media/howto-monitor-azure-policy/azure-policy-compliance.png#lightbox)
5.   Select a policy to review aggregate compliance details and events.
6.   Select a specific Web PubSub for resource compliance.

You can use the Azure CLI to get compliance data. Use the [az policy assignment list](https://learn.microsoft.com/en-us/cli/azure/policy/assignment#az-policy-assignment-list) command to get the policy IDs of the Azure Web PubSub Service policies that are applied:

```
az policy assignment list --query "[?contains(displayName,'Web PubSub')].{name:displayName, ID:id}" --output table
```

Example output:

```
Name                                                                                   ID
-------------------------------------------------------------------------------------  --------------------------------------------------------------------------------------------------------------------------------
[Preview]: Azure Web PubSub Service should use private links  /subscriptions/<subscriptionId>/resourceGroups/<resourceGroup>/providers/Microsoft.Authorization/policyAssignments/<assignmentId>
```

Run the [az policy state list](https://learn.microsoft.com/en-us/cli/azure/policy/state#az-policy-state-list) command to return the JSON-formatted compliance state for all resources under a specific resource group:

```
az policy state list --g <resourceGroup>
```

Run the [az policy state list](https://learn.microsoft.com/en-us/cli/azure/policy/state#az-policy-state-list) command to return the JSON-formatted compliance state of a specific Web PubSub resource:

```
az policy state list \
 --resource /subscriptions/<subscriptionId>/resourceGroups/<resourceGroup>/providers/Microsoft.SignalRService/WebPubSub/<resourceName> \
 --namespace Microsoft.SignalRService \
 --resource-group <resourceGroup>
```

*   Learn more about Azure Policy [definitions](https://learn.microsoft.com/en-us/azure/governance/policy/concepts/definition-structure) and [effects](https://learn.microsoft.com/en-us/azure/governance/policy/concepts/effects)

*   Create a [custom policy definition](https://learn.microsoft.com/en-us/azure/governance/policy/tutorials/create-custom-policy-definition)

*   Learn more about [governance capabilities](https://learn.microsoft.com/en-us/azure/governance/) in Azure
