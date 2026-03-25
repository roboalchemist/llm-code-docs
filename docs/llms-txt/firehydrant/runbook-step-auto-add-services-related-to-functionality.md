# Source: https://docs.firehydrant.com/docs/runbook-step-auto-add-services-related-to-functionality.md

# Auto-Add Services Related to Functionality

As your team grows, you may occasionally find that the person declaring an incident does not know which specific service is involved but does know what end-user functionality is impacted.

With this Runbook step, all Services related to a Functionality are automatically added to an incident, assuring you that the right teams and services will be associated with your incident no matter what.

## Prerequisites

* Ensure you have **Functionalities** and **Services** within your [Service Catalog](https://docs.firehydrant.com/docs/intro-to-service-catalog)
* Ensure that the Functionality is linked to at least one Service you'd like automatically pulled into the incident

## Adding the Runbook Step

<Image alt="Auto-Add Services Related to Functionality step" align="center" src="https://files.readme.io/25cb1fd-image.png">
  Auto-Add Services Related to Functionality step
</Image>

To add the Runbook step:

1. Click into an existing **Runbook** or create a new one.
2. Click "+ Add Step" in the Runbook settings and search for **Auto-Add Services Related to Functionality**.
3. Then click "Add step" and then "Save Runbook."

## Activating the Runbook Step

How and when this Runbook step is activated depends on the condition rules you set for it.

When you declare an incident, you can add a functionality as impacted. When an incident is declared with attached functionality, the Runbook step automatically adds services to the incident that are related to that particular functionality.

Services are added with the same impact as the functionality; for example, if a **functionality** is added to an incident with a **degraded** condition, then the three related **services** will also be added to the incident as **degraded**.

## Extending this functionality

If a service related to a functionality is brought in to an incident (by way of a Runbook step at the time of declaration) and has **automatic alerting** turned on, the default escalation policy *of the linked service* will be paged. For more information on how to turn on automatic alerting for services, see [Auto-Alerting Services](https://docs.firehydrant.com/docs/auto-alerting-services).