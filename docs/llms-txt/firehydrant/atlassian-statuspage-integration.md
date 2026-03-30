# Source: https://docs.firehydrant.com/docs/atlassian-statuspage-integration.md

# Atlassian Statuspage

Atlassian Statuspage is a tool for publicizing incidents currently occurring with your product. [We use them](https://status.firehydrant.io) along with thousands of other companies. Integrating your public status page updates into an incident response process makes sense, so we built our Atlassian Statuspage integration to do just that. This guide goes over how to set up and use the integration.

## Prerequisites

* You'll need <Glossary>Owner</Glossary> privileges to configure integrations on FireHydrant
* You'll need to have owner access to your Atlassian Statuspage account

## Configuring Statuspage

1. Sign in to Atlassian Statuspage as an owner.
2. Click your avatar in the upper right and select **API Info**.

<Image alt="API info in Atlassian Statuspage" align="center" width="650px" src="https://files.readme.io/2d71d7a-Screenshot_2024-01-11_at_5.44.24_PM.png">
  API info in Atlassian Statuspage
</Image>

3. On this screen, click the **Create key** and enter a name (e.g., "FireHydrant").
4. Copy the key that it provides for the next section.
5. On FireHydrant (logged in as an **Owner**), navigate to your [Integrations page](https://app.firehydrant.io/organizations/integrations) and search for "statuspage." Click the '+' on the tile.
6. Paste the API key from Step 4 into the API Token field and click **Authorize Application**.
7. Once this finishes, you should be taken back to the Statuspage settings in FireHydrant. Scroll down to **Statuspage.io Page** and select which Statuspage you'd like to connect to FireHydrant.
8. Once you've selected a Statuspage, the **Severity Map** and **Condition Map** sections will appear below, where you can map FireHydrant's [Severities](https://docs.firehydrant.com/docs/severities-and-priorities) and [Conditions](https://docs.firehydrant.com/docs/conditions) to the Atlassian Statuspage's severities and conditions.

<Image alt="Mapping severities and conditions for a Statuspage" align="center" width="400px" src="https://files.readme.io/5abbb39-image.png">
  Mapping severities and conditions for a Statuspage
</Image>

10. Map FireHydrant Incident Milestones to Atlassian Statuspage statuses. This ensures that when you transition a FireHydrant incident, it will display the right status updates to the incident within Statuspage.

<Image alt="Mapping FireHydrant milestones to Atlassian Statuspage statuses" align="center" width="400px" src="https://files.readme.io/4ac94c2802c03722b5d7386f623fc47b14e87625e12c18019522b6c7b86d1b08-image.png">
  Mapping FireHydrant milestones to Atlassian Statuspage statuses
</Image>

11. Click **Save Changes** to finalize these settings and finish the integration setup
12. (Optional) If you have more than one Atlassian Statuspage, repeat steps 5 - 9 above. Each Statuspage requires a separate connection, but you should be able to reuse the same Atlassian API key. A new "Atlassian Statuspage" tile will always be available to connect more pages in the Integrations list.

## Linking & Importing Components

Once the integration is set up, you'll want to import a Statuspage component to FireHydrant's Service Catalog or link your Statuspage components to existing FireHydrant components. This step is required to automatically mark the right Statuspage components impacted on an incident.

1. Navigate to **Catalog> Services** or **Catalog> Functionalities** and click on **Addce | Functionality] > Im > Import from third party > Statuspage**.
   1. You can also get here by going to that Statuspage's settings in the integrations list and click **Link and import** at the top.
2. This takes you to the import screen, where you're presented with two options:
   1. **Import all as new services** - Pull up the complete list of components from this Statuspage, and all of them will be checked and set to "Create New."
   2. **Select pages to import** - Will show the same view as above, but with no components checked.

<Image alt="The import view for Statuspages" align="center" width="650px" src="https://files.readme.io/7bad652-image.png">
  The import view for Statuspages
</Image>

3. Here, you can check/uncheck which components you'd like to import or link, and then in the dropdown, you can choose to either:
   * **Create New** which will create a new Service or Functionality with the same name as said component in Statuspage and link them together
   * **Link to existing** will link the Statuspage component and the existing component you choose in FireHydrant
4. When you're done choosing, click **Import selected pages**. You can confirm whether this worked by going to the Functionalities in question from the confirmation page and checking underneath the **External Links** section of the FireHydrant Service or Functionality.

## Next Steps

Once you've configured your Atlassian Statuspage and linked components, you can use it to post incidents and updates in various ways:

* [Create a Statuspage.io Incident](https://docs.firehydrant.com/docs/runbook-step-create-a-statuspageio-incident) - This runbook step automatically creates an incident on the selected Statuspage. If a linked component is impacted on said incident, it will also mark that component impacted on Statuspage.
* [External Status Pages](https://docs.firehydrant.com/docs/external-status-pages) - Learn more about how to attach external status pages (Atlassian or FireHydrant) to incidents both automatically and manually.
* [Posting Updates](https://docs.firehydrant.com/docs/posting-updates) - FireHydrant makes it easy to seamlessly post incident update notes that propagate to the attached status pages.
* [Browse the rest of our integrations](https://docs.firehydrant.com/docs/integrations-overview)