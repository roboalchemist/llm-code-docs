# Source: https://help.aikido.dev/cloud-scanning/connect-your-cloud/azure/connect-azure-cloud-account-to-aikido.md

# Connect Your Azure Cloud

Securing your cloud infrastructure is crucial to protecting your data. You can leverage Aikido's security checks to detect and address any misconfigurations in your infrastructure.

To view the list of security checks performed by Aikido on your cloud environment, go to the 'checks' tab on the [cloud overview page](https://app.aikido.dev/clouds) at. Filter to Azure to see specific checks performed on your connected Azure subscription(s).

To get started, head to the [cloud overview page](https://app.aikido.dev/clouds) on Aikido and click 'Connect cloud.' Follow the step-by-step setup wizard to connect your Azure subscription with Aikido.

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FutN155tLUAKrAB0PGkTN%2Fimage.png?alt=media&#x26;token=fffe9d41-2607-4bb4-9428-8ac954f64a9b" alt=""><figcaption></figcaption></figure>

The setup wizard will guide you through creating a new 'App registration' inside of the **Microsoft Entra ID service** with an API secret specifically for Aikido. In the last step, you'll assign specific reader roles ("Security reader", "Log analytics reader") to grant limited, read-only access to specific services in your Azure cloud. This ensures that Aikido can perform its security checks without the risk of unintended modifications to your resources.

The API secret will be used by Aikido to make the necessary API requests to scan your resources. Aikido will notify you via email when the secret is about to expire.

Finally, you can name your connected subscription in Aikido and specify the environment it operates in (development, production,..). This information helps Aikido prioritize findings based on the severity and impact to your business.

![](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-5a150e43145ee0115fe707e10aefed6b77d30fa1%2Fconnect-azure-cloud-account-to-aikido_6bdf014a-abc6-4d69-9f8d-c90724e58850.png?alt=media)

Within 1-2 minutes after connecting your account, Aikido will report misconfigurations that could pose a threat.

### Advanced Rules

Besides the checks mentioned above, Aikido offers a suit of complementary checks/rules that you can enable. We call these advanced cloud rules and you can find them [here](https://app.aikido.dev/clouds/checks?cloudCheckType=advanced). After enabling any of these rules, you can expect to see the results (as new issues in [the feed](https://app.aikido.dev/queue)) within a few seconds.

Just like the standard checks, these are evaluated with each scan of your cloud environments. Moreover, they are mapped to the compliance reports. By default, the advanced rules will appear as *disabled* in the compliance reports, unless you activate them.

#### Azure Advanced Rules Changelog

**Aug 27, 2025**

34 new advanced rules for Azure are now available, covering the following services/resources:

* **AKS**: RBAC, Entra ID integration, Key Vault integration, and more.
* Cosmos DB, Azure Cache for Redis, Azure SQL
* Event Grid, Service Bus, Event Hubs
* Application Gateway

**Jul 25, 2025**

We've added the first batch of six advanced rules for Azure. These focus on Azure Storage Accounts, Azure File Shares, and Azure Container Registry.
