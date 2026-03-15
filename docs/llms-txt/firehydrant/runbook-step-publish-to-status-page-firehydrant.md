# Source: https://docs.firehydrant.com/docs/runbook-step-publish-to-status-page-firehydrant.md

# Publish to Status Page (FireHydrant)

During incidents, it's crucial to post updates to external stakeholders.

## Prerequisites

* You will need to have a [FireHydrant status page configured](https://docs.firehydrant.com/docs/status-page-setup-and-configuration)

## Configuration

<Image alt="Publish to status page (FireHydrant) step" align="center" width="650px" src="https://files.readme.io/1c9926a-image.png">
  Publish to status page (FireHydrant) step
</Image>

To add this step:

1. Go to Create/Edit a Runbook and click "+ Add step."
2. Search for "publish to status page" and then click the step.
3. This step comes with two configurable fields:
   1. **Title** - The title of the incident. This field supports [Template Variables](https://docs.firehydrant.com/docs/template-variables).
   2. **Page** - The FireHydrant status page you want to post to.
   3. (Optional) You can also configure conditions for when this Runbook step will execute.
4. Click "Add step" and then "Save runbook."

## Runbook Execution

If this step executes, FireHydrant will post the incident onto your configured FireHydrant status page.

<Image alt="Example incident posted to a FireHydrant status page" align="center" width="650px" src="https://files.readme.io/85b6fd0-image.png">
  Example incident posted to a FireHydrant status page
</Image>

Additionally, When you mark [Service Catalog components](https://docs.firehydrant.com/docs/service-catalog-basics) impacted on an incident, FireHydrant will automatically mark the corresponding components on the status page if they are displayed there.

<Image alt="A specific component is marked as impacted on days with incidents" align="center" width="650px" src="https://files.readme.io/c891d1c-image.png">
  A specific component is marked as impacted on days with incidents
</Image>