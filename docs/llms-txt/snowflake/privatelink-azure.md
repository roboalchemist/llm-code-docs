# Source: https://docs.snowflake.com/en/user-guide/privatelink-azure.md

# Azure Private Link and Snowflake

This topic describes how to configure Azure Private Link to connect your Azure Virtual Network (VNet) to the Snowflake VNet in Azure.

Note that Azure Private Link is not a service provided by Snowflake. It is a Microsoft service that Snowflake enables for use with
your Snowflake account.

## Overview

[Azure Private Link](https://docs.microsoft.com/en-us/azure/private-link/private-link-overview) provides private connectivity to Snowflake
by ensuring that access to Snowflake is through a private IP address. Traffic can only occur from the customer virtual network (VNet) to the
Snowflake VNet using the Microsoft backbone and avoids the public Internet. This significantly simplifies the network configuration by
keeping access rules private while providing secure and private communication.

The following diagram summarizes the Azure Private Link architecture with respect to the customer VNet and the Snowflake VNet.

From either a virtual machine (1) or through peering (2), you can connect to the Azure Private Link endpoint (3) in your virtual network.
That endpoint then connects to the Private Link Service (4) and routes to Snowflake.

Here are the high-level steps to integrate Snowflake with Azure Private Link:

1. Create a Private Endpoint.
2. Generate and retrieve an access token from your Azure subscription.

   Note that if you plan to use Azure Private Link to connect to a Snowflake internal stage on Azure, you must register your
   subscription with the Azure Storage resource provider before connecting to the internal stage from a private endpoint.
3. Enable your Snowflake account on Azure to use Azure Private Link.
4. Update your outbound firewall settings to allow the Snowflake account URL and OCSP URL.
5. Update your DNS server to resolve your account URL and OCSP URL to the Private Link IP address. You can add the DNS entry to your
   on-premises DNS server or private DNS on your VNet, and use DNS forwarding to direct queries for the entry from other locations where
   your users will access Snowflake.
6. After the Private Endpoint displays a CONNECTION STATE value of Approved, test your connection to Snowflake with
   [SnowCD (Connectivity Diagnostic Tool)](snowcd.md) and [SYSTEM$ALLOWLIST_PRIVATELINK](../sql-reference/functions/system_allowlist_privatelink.md).
7. Connect to Snowflake using your private connectivity account URL.

To further harden your security posture, Snowflake recommends [Pinning private connectivity endpoints for inbound traffic](pin-private-endpoints.md) for your Snowflake account.

### Requirements and limitations

Before attempting to configure Azure Private Link to connect your Azure VNet to the Snowflake VNet on Azure, note the following:

* In Azure at the subnet level, optionally
  [enable a network policy](https://learn.microsoft.com/en-us/azure/private-link/disable-private-endpoint-network-policy?tabs=network-policy-portal)
  for the Private Endpoint.

  Verify that the TCP ports 443 and 80 allow traffic to `0.0.0.0` in the network security group of the Private Endpoint network card.

  For help with the port configuration, contact your internal Azure administrator.
* Use [ARM VNets](https://docs.microsoft.com/en-us/azure/azure-resource-manager/).
* Use IPv4 TCP traffic only.
* Currently, the self-service enablement process described in this topic does not support authorizing a managed Private Endpoint from Azure
  Data Factory, Synapse, or other managed services.

  For details on how to configure a managed private endpoint for this use case, see this
  [article](https://community.snowflake.com/s/article/How-to-set-up-a-managed-private-endpoint-from-Azure-Data-Factory-or-Synapse-to-Snowflake)
  (in the Snowflake community).

For more information on the requirements and limitations of Microsoft Azure Private Link, see the Microsoft documentation on
[Private Endpoint Limitations](https://docs.microsoft.com/en-us/azure/private-link/private-endpoint-overview#limitations) and
[Private Link Service Limitations](https://docs.microsoft.com/en-us/azure/private-link/private-link-service-overview#limitations).

## Configure access to Snowflake with Azure Private Link

> **Attention:**
>
> This section only covers the Snowflake-specific details for configuring your VNet environment. Also, note that Snowflake is not
> responsible for the actual configuration of the required firewall updates and DNS records. If you encounter issues with any of these
> configuration tasks, please contact Microsoft Support directly.

This section describes how to configure your Azure VNet to connect to the Snowflake VNet on Azure using Azure Private Link. After initiating
the connection to Snowflake using Azure Private Link, you can determine the approval state of the connection in the Azure portal.

For installation help, see the Microsoft documentation for the
[Azure CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli?view=azure-cli-latest)
or [Azure PowerShell](https://docs.microsoft.com/en-us/powershell/azure/install-az-ps?view=azps-2.6.0).

Complete the configuration procedure to configure your Microsoft Azure VNet and initiate the Azure Private Link connection to Snowflake.

### Procedure

This procedure manually creates and initializes the necessary Azure Private Link resources to use Azure Private Link to connect to
Snowflake on Azure. Note that this procedure assumes that your use case does not involve Using SSO with Azure Private Link
(in this topic).

1. As a representative example using the Azure CLI, execute `az account list --output table`. Note the output values in the
   `Name`, `SubscriptionID` and `CloudName` columns.

   ```text
   Name     CloudName   SubscriptionId                        State    IsDefault
   -------  ----------  ------------------------------------  -------  ----------
   MyCloud  AzureCloud  13c...                                Enabled  True
   ```

2. Navigate to the Azure portal. Search for Private Link and click Private Link.
3. Click Private endpoints and then click Add.

# . In the Basics section, complete the Subscription, Resource group, Name, and Region fields
for your environment and then click Next: Resource.

1. In the Resource section, complete the Connection method and the Resource ID or alias Field fields.

   * For Connection Method, select the Connect to an Azure resource by resource ID or alias.
   * In Snowflake, execute [SYSTEM$GET_PRIVATELINK_CONFIG](../sql-reference/functions/system_get_privatelink_config.md) and input the value for `privatelink-pls-id`
     into the Resource ID or alias field. Note that the screenshot in this step uses the alias value for the `east-us-2`
     region as a representative example, and that Azure confirms a valid alias value with a green checkmark.
   * If you receive an error message regarding the alias value, contact [Snowflake Support](https://docs.snowflake.com/user-guide/contacting-support) to receive the resource ID value and then
     repeat this step using the resource ID value.
2. Return to the Private endpoints section and allow a few minutes to wait. On approval, the Private Endpoint displays a
   CONNECTION STATE value of Pending. This value will update to Approved after completing the authorization in
   the next step.
3. Enable your Snowflake account on Azure to use Azure Private Link by completing the following steps:

   * In your command-line environment, record the private endpoint resource ID value using the following Azure CLI
     [network](https://docs.microsoft.com/en-us/cli/azure/network/private-endpoint?view=azure-cli-latest#az-network-private-endpoint-show)
     command:

     > ```bash
     > az network private-endpoint show
     > ```
     >
     > The private endpoint was created in the previous steps using the template files. The resource ID value takes the following form,
     > which has a truncated value:
     >
     > `/subscriptions/26d.../resourcegroups/sf-1/providers/microsoft.network/privateendpoints/test-self-service`
   * In your command-line environment, execute the following
     [Azure CLI account](https://docs.microsoft.com/en-us/cli/azure/account?view=azure-cli-latest#az_account_get_access_token) command
     and save the output. The output will be used as the value for the `federated_token` argument in the next step.

     > ```bash
     > az account get-access-token --subscription <SubscriptionID>
     > ```

     Extract the access token value from the command output. This value will be used as the `federated_token` value in the next
     step. In this example, the values are truncated and the access token value is `eyJ...`:

     > ```sqljson
     > {
     >    "accessToken": "eyJ...",
     >    "expiresOn": "2021-05-21 21:38:31.401332",
     >    "subscription": "0cc...",
     >    "tenant": "d47...",
     >    "tokenType": "Bearer"
     >  }
     > ```
     >
     > > **Important:**
     > >
     > > The user generating the Azure access Token must have Read permissions on the Subscription. The least privilege permission is
     > > [Microsoft.Subscription/subscriptions/acceptOwnershipStatus/read](https://docs.microsoft.com/en-us/azure/role-based-access-control/resource-provider-operations#microsoftsubscription).
     > > Alternatively, the default role `Reader` grants more coarse-grained permissions.
     > >
     > > The `accessToken` value is sensitive information and should be treated like a password value — do not share this
     > > value.
     > >
     > > If it is necessary to contact Snowflake Support, redact the access token from any commands and URLs before creating a support
     > > ticket.
   * In Snowflake, call the [SYSTEM$AUTHORIZE_PRIVATELINK](../sql-reference/functions/system_authorize_privatelink.md) function,
     using the `private-endpoint-resource-id` value and the `federated_token` value as arguments, which are truncated in
     this example:

     > ```sqlexample
     > USE ROLE ACCOUNTADMIN;
     >
     > SELECT SYSTEM$AUTHORIZE_PRIVATELINK (
     >   '/subscriptions/26d.../resourcegroups/sf-1/providers/microsoft.network/privateendpoints/test-self-service',
     >   'eyJ...'
     >   );
     > ```

   To verify your authorized configuration, call the [SYSTEM$GET_PRIVATELINK](../sql-reference/functions/system_get_privatelink.md) function in your
   Snowflake account on Azure. Snowflake returns `Account is authorized for PrivateLink.` for a successful authorization.

   If it is necessary to *disable* Azure Private Link in your Snowflake account, call the
   [SYSTEM$REVOKE_PRIVATELINK](../sql-reference/functions/system_revoke_privatelink.md) function, using the argument values for
   `private-endpoint-resource-id` and `federated_token`.
4. DNS Setup. All requests to Snowflake need to be routed via the Private Endpoint. Update your DNS to resolve the Snowflake account and
   OCSP URLs to the private IP address of your Private Endpoint.

   * To get the endpoint IP address, navigate to Azure portal search bar and enter the name of the endpoint
     (i.e. the NAME value from Step 5). Locate the Network Interface result and click it.
   * Copy the value for the Private IP address (i.e. `10.0.27.5`).
   * Configure your DNS to have the appropriate endpoint values from the [SYSTEM$GET_PRIVATELINK_CONFIG](../sql-reference/functions/system_get_privatelink_config.md)
     function resolve to the private IP address.

     The values to obtain from the output of SYSTEM$GET_PRIVATELINK_CONFIG depend on which Snowflake features you access using private
     connectivity. For a description of the possible values, see [Return values](../sql-reference/functions/system_get_privatelink_config.md).

     Note that the values for `regionless-snowsight-privatelink-url` and `snowsight-privatelink-url` allow access to
     Snowsight and the Snowflake Marketplace using private connectivity. However, there is additional configuration if you want to enable
     URL redirects. For information, see [Snowsight & Private Connectivity](ui-snowsight-gs.md).

     > **Note:**
     >
     > A full explanation of DNS configuration is beyond the scope of this procedure. For example, you can choose to integrate an
     > [Azure Private DNS zone](https://docs.microsoft.com/en-us/azure/dns/private-dns-privatednszone) into your environment. Please
     > consult your internal Azure and Cloud Infrastructure administrators to configure and resolve the URLs in DNS properly.
5. After verifying your outbound firewall settings and DNS records include your Azure Private Link account and OCSP URLs, test your
   connection to Snowflake with [SnowCD (Connectivity Diagnostic Tool)](snowcd.md) and [SYSTEM$ALLOWLIST_PRIVATELINK](../sql-reference/functions/system_allowlist_privatelink.md).
6. Connect to Snowflake with your private connectivity account [URL](organizations-connect.md).

   Note that if you want to connect to Snowsight via Azure Private Link, follow the instructions in the
   [Snowsight documentation](ui-snowsight-gs.md).

## Using SSO with Azure Private Link

Snowflake supports using SSO with Azure Private Link. For more information, see:

* [SSO with private connectivity](admin-security-fed-auth-overview.md)
* [Partner applications](oauth-snowflake-overview.md)

## Using Client Redirect with Azure Private Link

Snowflake supports using Client Redirect with Azure Private Link.

For more information, see [Redirecting client connections](client-redirect.md).

## Using replication and Tri-Secret Secure with private connectivity

Snowflake supports replicating your data from the source account to the target account, regardless of whether you enable
Tri-Secret Secure or this feature in the target account.

## Blocking public access — *Recommended*

After testing the Azure Private Link connectivity with Snowflake, you can optionally block public access to Snowflake using
[Controlling network traffic with network policies](network-policies.md).

Configure the CIDR block range to block public access to Snowflake using your organization’s IP address range. This range can be
from within your virtual network.

Once the CIDR Block ranges are set, only IP addresses within the CIDR block range can access Snowflake.

To block public access using a network policy:

1. Create a new network policy or edit an existing network policy. Add the CIDR block range for your organization.
2. Activate the network policy for your account.
