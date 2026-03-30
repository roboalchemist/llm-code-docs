# Source: https://docs.firehydrant.com/docs/runbook-step-update-incident-details.md

# Update Incident Details

<Image alt="Update Incident Details Runbook step" align="center" width="650px" src="https://files.readme.io/cb08b60-image.png">
  Update Incident Details Runbook step
</Image>

Sometimes, incident details must be updated according to a changing situation. If the patterns are consistent, then they can be automated with FireHydrant's "Update Incident Details" step.

## Configuration

To add this step, go to Create a Runbook or Edit an existing Runbook and then click "+ Add step." Look up "update" or "details" and click on the "Update Incident Details" step.

This step comes with a variety of configurable fields, none of which are mandatory:

* **Milestone** - Allows you to move an incident through various [milestone states](https://docs.firehydrant.com/docs/incident-milestones).
* **Severity** - Allows you to escalate or deescalate the [severity](https://docs.firehydrant.com/docs/severities-and-priorities) of an incident automatically. This could be based on a set of impacts or a certain duration of an incident.
* **Priority** - The [priority](https://docs.firehydrant.com/docs/severities-and-priorities) field works similarly to the severity field.
* **Tags** - Allows you to add more [tags](https://docs.firehydrant.com/docs/incident-tags) automatically.
* **Labels** - Allows you to add more [labels](https://docs.firehydrant.com/docs/incident-labels). The values should be in the form of `key=value` on each line. This field supports [Template Variables](https://docs.firehydrant.com/docs/template-variables).
* **Description** - Allows you to update the description of the incident automatically.
  * Any changes made here will *overwrite* the previous description. To append more information, you can make use of the existing description by referencing `{{ incident.description }}` in the body.
  * This field supports [Template Variables](https://docs.firehydrant.com/docs/template-variables).
* **Customer Impact** - Allows you to update the customer impact statement on the incident automatically.
  * Any changes made here will *overwrite* the previous customer impact statement. To append more information, you can make use of the existing customer impact statement by referencing `{{ incident.customer_impact_summary }}`.
  * This field supports [Template Variables](https://docs.firehydrant.com/docs/template-variables).
* **Note** - Allows you to automatically post an [incident note/update](https://docs.firehydrant.com/docs/posting-updates). Incident Notes will always be included on the [internal status page](https://docs.firehydrant.com/docs/internal-status-pages) by default.
* **Status pages to post to automatically** - Any [external status pages](https://docs.firehydrant.com/docs/external-status-pages) that the **Note** above should be posted to automatically.
  * If a pre-existing incident is on a selected status page and is linked to the current incident, the note will be posted to that specific incident. If no matching incident is found, no new incident will be created, and the note will not be posted.

You can also optionally configure conditional execution rules, which many FireHydrant users do.

## Runbook Execution

This step will change the incident's details as configured by you in the step, and these changes are also logged as part of the [Incident Timeline](https://docs.firehydrant.com/docs/incident-timeline).

Some common and example use cases include:

* Automatically set an incident to **Mitigated** milestone if there haven't been any updates in 48 hours.
* Automatically escalate the severity of an incident if it has been open for longer than 24 hours.
* As soon as a specific component is added to the incident (e.g., `caching-service`), add a tag `caching-issues` to the incident
* Automatically post a note ("We are continuing to investigate the issue") to the external status page if there have been no recent, manual updates in the last 15 minutes.