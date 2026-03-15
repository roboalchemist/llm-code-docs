# Source: https://docs.firehydrant.com/docs/zendesk-integration.md

# Zendesk

From a customer-impact standpoint, support tickets are one of the indicators of how an incident impacts customers. FireHydrant's Zendesk integration allows users to link Zendesk support tickets to an incident to help track customer impact and guide customer communications.

There are two parts to the Zendesk integration configuration:

* Enabling the Zendesk integration from the FireHydrant **Integrations** page
* Installing the FireHydrant Zendesk Marketplace app in Zendesk

## Prerequisites

* You will need <Glossary>Owner</Glossary> permissions on FireHydrant to configure integrations
* You'll also need to have a **service account**/**user** with Zendesk administrator role to install the FireHydrant app in the Zendesk Marketplace
* The Zendesk integration is only available for [Enterprise-level FireHydrant accounts](https://firehydrant.com/pricing/)

> 📘 Note:
>
> FireHydrant will create and manage data as the user that is logged in to Zendesk when performing the installation. FireHydrant recommends using a generic Zendesk service account rather than an individual named user to avoid problems if the named employee were to depart the organization.

## Connecting FireHydrant to Zendesk

<Image alt="Zendesk integration lookup under **Available**" align="center" width="650px" src="https://files.readme.io/fc9a0b5a069ba2104de892a1037a21e0627539e3b1a76411e498becc7b46bdd1-CleanShot_2025-06-11_at_17.10.26.jpg">
  Zendesk integration lookup under **Available**
</Image>

1. Go to the [Integrations page](https://app.firehydrant.io/organizations/integrations) and search for the Zendesk app under the "Available" category if you haven't yet installed it. Click '+'.
2. Here, you will see an input for the Zendesk subdomain. Insert *only* the subdomain, not the full URL:

<Image alt="Input the subdomain (e.g., if your URL is `https://acme.zendesk.com`, only put `acme` here)" align="center" width="650px" src="https://files.readme.io/14841235ddabe9ed6e0d5c4a0b5b529d17914337c302900a28f008341baed704-CleanShot_2025-06-11_at_17.27.33.jpg">
  Input the subdomain (e.g., if your URL is `https://acme.zendesk.com`, only put `acme` here)
</Image>

3. Click **Authorize Application**. If you're not already logged in as the service account, this will take you to a login screen for Zendesk. Log in here to continue.
4. After successfully authenticating, the Zendesk integration will be finished configuring, and you should be taken back to the Zendesk settings page in FireHydrant. The integration details will appear, including the installation date and the authorizer.

<Image alt="Successful Zendesk integration" align="center" width="650px" src="https://files.readme.io/7e597ef5e7d996cc924f6b98dfce57908ced1f0434b38d047588c632bf1bb913-CleanShot_2025-06-11_at_17.29.06.jpg">
  Successful Zendesk integration
</Image>

## (Optional) Adding the FireHydrant Zendesk Marketplace App

The [FireHydrant Zendesk Marketplace app](https://www.zendesk.com/marketplace/apps/support/854375/firehydrant/) allows support staff to create FireHydrant incidents directly from a support ticket. If you prefer not to install the marketplace app, linking Zendesk tickets to an incident from FireHydrant is still possible. But you won't be able to create new incidents or connect existing FireHydrant incidents from Zendesk.

1. First, you will need to [generate an API key](https://docs.firehydrant.com/docs/api-keys) in FireHydrant (requires <Glossary>Owner</Glossary> permissions).
2. From the Zendesk Marketplace, find [the FireHydrant app](https://www.zendesk.com/marketplace/apps/support/854375/firehydrant/). Click **Install**.  This will take you to the Zendesk Admin Center.  Provide the following information to configure the FireHydrant app:
   1. Title of the FireHydrant environment
   2. API key from FireHydrant
   3. Zendesk role restrictions (optional)
   4. Zendesk group restrictions (optional)
3. Click **Install**.

<Image alt="Screen_Shot_2022-08-31_at_4.43.49_PM.png" align="center" width="400px" src="https://support.firehydrant.com/hc/article_attachments/8989506057748/Screen_Shot_2022-08-31_at_4.43.49_PM.png">
  FireHydrant app in the Zendesk Marketplace
</Image>

Once you're done, you should be able to create incidents or link the current support ticket to an incident in FireHydrant directly from the support portal.

<Image alt="Looking at the FireHydrant app while managing a customer ticket in Zendesk" align="center" width="650px" src="https://files.readme.io/66db70c801f191ba317bf3257497ac8dcd534f13f8e65c4f6f5a3fc3dcde9451-CleanShot_2025-06-11_at_17.31.41.jpg">
  Looking at the FireHydrant app while managing a customer ticket in Zendesk
</Image>

> 📘 Note:
>
> The Zendesk form here for declaring incidents from customer tickets will also respect your configured settings for [Incident Fields](https://docs.firehydrant.com/docs/incident-fields) and field requirements.

## Uninstalling Zendesk

1. In FireHydrant, on the Zendesk integrations settings page, you can simply click **Uninstall Zendesk**.
2. From the Zendesk Admin Center, find the FireHydrant app. Hover over the bottom right of the app icon until the configuration icon appears.  From the configuration menu, select **Uninstall**.

## Next Steps

* With the Zendesk integration configured, learn more about [Attaching Support Tickets](https://docs.firehydrant.com/docs/attaching-support-tickets) to incidents and automatically posting ticket updates!
* Learn more about [the rest of FireHydrant's integrations](https://docs.firehydrant.com/docs/integrations-overview)
* If you're not on the Enterprise plan, see the [pricing page](https://firehydrant.com/pricing/) and learn more about what Enterprise can unlock for you