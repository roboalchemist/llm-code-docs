# Source: https://docs.firehydrant.com/docs/import-and-link-components.md

# Import and Link Components

This article covers importing catalog items from external providers and linking them to enable additional capabilities. Importing components will automatically link them, but if you already have existing FireHydrant Services, Functionalities, or Environments, you can link them in bulk using the same workflow.

Depending on the third-party provider's category, linking components enables several different capabilities:

* **For alerting providers like Opsgenie, PagerDuty, and Splunk On-Call**:
  * Importing will create entries in FireHydrant's Catalog for each imported external service/routing key
  * The link created with the external service enables capabilities like [On-Call Paging and Lookup](https://docs.firehydrant.com/docs/on-call-paging-and-lookup) and [Auto-Alerting Services](https://docs.firehydrant.com/docs/auto-alerting-services)
* **For repository providers like GitHub**:
  * Importing creates entries in FireHydrant's Catalog for each repository imported and links the repo to the service.
  * This enables the ingestion of [Change Events](https://docs.firehydrant.com/docs/change-events), where any merges to the main branch of your repository register as change events, giving your responders a handy avenue to explore when an incident occurs
* **For Atlassian Statuspage**:
  * Importing Statuspage components will create entries in FireHydrant's Catalog and link the Statuspage component to the FireHydrant component.
  * This link allows automatically marking the relevant component impacted on the Statuspage if the linked component is marked impacted in a FireHydrant incident. Learn more [here](https://docs.firehydrant.com/docs/external-status-pages).

> 📘 Note:
>
> Importing and/or linking services is a one-time task and does not automatically continue synchronizing FireHydrant's Service Catalog with the 3rd-party. For automatic syncing, see [Automatic Service Ingestion](https://docs.firehydrant.com/docs/automatic-service-ingestion) and [Backstage](https://docs.firehydrant.com/docs/backstage).

## Prerequisites

Ensure you've configured the integration for whichever provider(s) you'd like to link:

* [Atlassian Statuspage](https://docs.firehydrant.com/docs/atlassian-statuspage-integration)
* [Datadog](https://docs.firehydrant.com/docs/datadog-integration)
* [GitHub](https://docs.firehydrant.com/docs/github-integration)
* [Opsgenie](https://docs.firehydrant.com/docs/opsgenie-integration)
* [PagerDuty](https://docs.firehydrant.com/docs/pagerduty-integration)
* [Splunk On-Call (VictorOps)](https://docs.firehydrant.com/docs/splunk-on-call-victorops-integration)
  * **Note:** For VictorOps, FireHydrant supports importing and linking [Routing Keys](https://help.victorops.com/knowledge-base/routing-keys/) as Services

## Importing Services

1. In the navigation, click on **Catalog**.
2. This should take you to the **Services** page of the Catalog. On the right side, click on the **Add service** dropdown and select **Import from third party**.
3. On this page, click the **Import** button next to your provider of choice.

   <Image alt="Service catalog import page. This page is identical for all components, differing only in the number of 3rd-party options depending on component type" align="center" width="650px" src="https://files.readme.io/b6d95dc-CleanShot_2024-08-12_at_12.31.28.png">
     Service catalog import page. This page is identical for all components, differing only in the number of 3rd-party options depending on component type
   </Image>
4. Select whether you want to import all the services or if you'd like to pick and choose. This only impacts which external components are pre-checked on the next page.
5. On the next page, FireHydrant will load all the services it can read and display them in a list. Select the checkbox for each service you want to import. Then, using the dropdown menu, indicate whether you want to import each service as net new or link it to an existing service. If you selected "Import all" on the previous screen, everything will be pre-checked here.

<Image alt="Bulk import and link services screen" align="center" width="650px" src="https://files.readme.io/26de18e-image.png">
  Bulk import and link services screen
</Image>

6. When you're done selecting, click **Import X Selected Services** to initiate the importing and linking process.

7. Once the import is finished, you should be taken to a summary page showing the new services you've created/imported and the link to the external service from which it was imported.

> 📘 Note:
>
> Service Catalog components can have links to multiple types of external services (e.g., linked alerting service and repository). To handle this, we recommend importing from one specific provider and then [configuring additional links](#linking-existing-components) for other providers afterwards.

## Importing Functionalities and Environments

The import process for Functionalities and Environments is identical, except Environments support importing and linking with fewer providers.

## Linking Existing Components

As you saw above, the "import" flow also allows bulk linking many existing FireHydrant components with external providers. If you'd like to link many components in bulk, follow the "import" flow above and ensure that for each external component, you select an existing Service under "FireHydrant Services" instead of "Create New."

To link on a more ad-hoc basis, you can:

1. Select a desired component and go into its "Edit" screen.

2. Scroll down to the section titled **Integration links**.

<Image alt="Integration Links section of a component" align="center" width="400px" src="https://files.readme.io/709948a-image.png">
  Integration Links section of a component
</Image>

3. For any integration you've installed and configured, you can click **Configure** next to the provider.
4. Once you click **Configure**, FireHydrant will return a list of external components from the provider. You can select one or more values to link to your catalog item in FireHydrant. Once you have finished selecting, scroll down and click **Save edits**.

## Linking via API

You can also programmatically link Services by using the [PATCH `/services/{service_id}`](https://developers.firehydrant.com/#/operations/patchV1ServicesServiceId) endpoint. The parameter of interest for this will be the `external_resources` argument.

## Next Steps

Now that you've read about importing and linking services from external tools:

* See how you can [look up and page](https://docs.firehydrant.com/docs/on-call-paging-and-lookup) whoever's on call for a Service, Functionality, or Environment.
* You can also [automatically page said components](https://docs.firehydrant.com/docs/auto-alerting-services) any time they're marked impacted on an incident.
* Read some more about [Change Events](https://docs.firehydrant.com/docs/change-events) and how they can potentially speed up identifying problematic recent changes.
* Learn more about FireHydrant's [Atlassian Statuspage](https://docs.firehydrant.com/docs/atlassian-statuspage-integration) for posting updates to external end users.