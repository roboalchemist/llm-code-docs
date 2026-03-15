# Source: https://docs.firehydrant.com/docs/runbook-step-auto-add-functionalities-related-to-service.md

# Auto-Add Functionalities Related to Service

As your team grows, you may occasionally find that the person declaring an incident does not know which specific functionalities are impacted but does know which service is involved. With this Runbook step, all functionalities related to a service are automatically added to an incident, assuring you that the correct end-user functionalities will be associated with your incident no matter what.

> 📘 Note
>
> Before getting started, make sure you have **Functionalities** and **Services** added in FireHydrant. To learn more about these features, see our article on [Service Catalog management](https://docs.firehydrant.com/docs/intro-to-service-catalog).

## Adding the Runbook Step

To add the Runbook step:

1. From the FireHydrant top nav, click **Runbooks**.
2. Click into an existing **Runbook** and then **Edit runbook**, or create a new one with **Add runbook**.
3. From inside the Runbook, scroll down and click **Add Step**.
4. Within **Select step type**, find **Auto-Add Functionalities Related To Service** and click **Add step**. This adds the step to the Runbook.
5. When you're done adding or editing steps, click **Save runbook**.

## Activating the Runbook Step

How and when this Runbook step is activated depends on the condition rules you set for it. In this example, we use the default execution of the Runbook step. 

When you declare an incident, you can add a service to it. When an incident is declared with an attached service, the Runbook step automatically adds functionalities to the incident that are related to that particular service. Functionalities are added with the same impact as the service; if the **service** is added to an incident with the status **degraded**, then the three related **functionalities** will also be added to the incident as **degraded**.

## Extending this functionality

For example, a functionality related to a service is marked impacted in an incident (through a Runbook step at the time of declaration). It has **automatic alerting** turned on. In that case, the default escalation policy *of the linked functionality* will be paged. For more information on how to turn on automatic alerting for functionalities, see [Auto-Alerting Services](https://docs.firehydrant.com/docs/auto-alerting-services).