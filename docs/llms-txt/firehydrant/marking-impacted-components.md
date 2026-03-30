# Source: https://docs.firehydrant.com/docs/marking-impacted-components.md

# Impacted Components

FireHydrant's [Service Catalog](https://docs.firehydrant.com/docs/intro-to-service-catalog) is a critical platform feature that helps you conduct better incidents. By tracking which parts of your infrastructure/application are impacted, as well as assigning owning users and teams, you can unlock capabilities like:

* Tracking [Impact Statistics](https://docs.firehydrant.com/docs/analytics-impact-statistics) by components, users, teams, and more
* Automatically [adding the right teams](https://docs.firehydrant.com/docs/adding-responders) for a particular component as well as [alerting/paging them](https://docs.firehydrant.com/docs/auto-alerting-services) on an incident
* Associating [recent changes](https://docs.firehydrant.com/docs/change-events) with incidents to give responders a head start on what to investigate

Depending on how your organization has configured [Incident Fields](https://docs.firehydrant.com/docs/incident-fields), impacted Environments, Functionalities, and Services are fields you should be able to set when declaring and at any point throughout the incident.

## Adding impacted components via Slack

<Image alt="Adding a Catalog impact when updating with `/fh update`" align="center" width="400px" src="https://files.readme.io/9f04022-image.png">
  Adding a Catalog impact when updating with `/fh update`
</Image>

In Slack, you can set affected components using a few commands:

* `/fh new` - You can set impacted components when declaring the incident (unless your admins have hidden these fields)
* `/fh update` - You select components when posting incident updates. This allows you to change the incident's [milestone](https://docs.firehydrant.com/docs/incident-milestones), change impacted components, and post updates to a status page in one swift motion. This command can be run at any point through the incident and even through Retrospective if the incident channel still exists.

Once you've added components during an incident, FireHydrant will also surface the related Teams, Services, Functionalities, or other items for you to take action:

<Image alt="FireHydrant surfaces related items for components" align="center" width="400px" src="https://files.readme.io/4abc6c3-image.png">
  FireHydrant surfaces related items for components
</Image>

## Adding impacted components via Command Center

<Image alt="Adding Impacts via the Command Center" align="center" width="650px" src="https://files.readme.io/5dea861-Screenshot_2024-01-29_at_3.46.47_PM.png">
  Adding Impacts via the Command Center
</Image>

You can add impacted components in the user interface by scrolling down to the **Impacts** section of the details panel on the right side. Clicking the edit pencil will open a modal to select items from the Catalog.

## Adding impacted components via integrations

Some integrations allow you to select impacted components when declaring an incident via the external application:

<Image alt="Declaring an incident from the FireHydrant app within Zendesk" align="center" width="400px" src="https://files.readme.io/5a48267-Screenshot_2024-01-29_at_4.13.09_PM.png">
  Declaring an incident from the FireHydrant app within Zendesk
</Image>

* The [Zendesk integration](https://docs.firehydrant.com/docs/zendesk-integration) allows you to choose **Functionalities** and any custom fields when declaring from the Zendesk support portal.