# Source: https://docs.firehydrant.com/docs/runbook-step-add-incident-impacts.md

# Add Incident Impacts

FireHydrant allows you to add impacted infrastructure to your incident automatically through a Runbook step.

<Image alt="Add incident impacts step" align="center" width="650px" src="https://files.readme.io/7915c96-image.png">
  Add incident impacts step
</Image>

## Prerequisites

You must have at least one configured component within your [Service Catalog](https://docs.firehydrant.com/docs/intro-to-service-catalog).

## Adding the Runbook step

To add the step, edit a Runbook and search for "Add Incident Impacts." In this step, you can add any combination of Services, Environments, and Functionalities to your incident and specify the condition with which you'd like these attached.

This can be helpful for automatically adding a consistent set of functionalities to every incident or programmatically adding services to an incident when specific conditions are met.

## Example Use Cases

* **Adding a Functionality or Environment when a specific Service is impacted**
  * For example, if you initiate an incident with a known Service that's impacted, you may want to mark the upstream Functionality or Environment it's tied to as `Degraded` or some other condition.
* **Add multiple Services, Functionalities, or Environments when a specific tag is added to the incident**
  * Maybe you have certain types of incidents that you track via tags. Aside from using our [incident types](/docs/incident-types/), you could also automate using this step.
  * For example, "If the incident is tagged `full-ui`" then add "User Portal," "Admin Portal" functionalities, and "app-cdn" and "app-fe" services.