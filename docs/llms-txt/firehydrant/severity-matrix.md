# Source: https://docs.firehydrant.com/docs/severity-matrix.md

# Severity Matrix

<Image alt="Example Severity Matrix in FireHydrant" align="center" src="https://files.readme.io/6d5798a-image.png">
  Example Severity Matrix in FireHydrant
</Image>

Have you ever been uncertain about the criticality of an incident? FireHydrant's severity matrix allows you to specify what severity levels should be automatically assigned to different combinations of fault states and impacted infrastructure. Let's take a look at how this is implemented.

> 📘 Note:
>
> Auto-assigning severity only occurs when an incident is **started** with components marked impacted. It does not automatically change the severity if a catalog item is added mid-incident.

## Prerequisites

* Access to managing Severity Matrix is restricted to FireHydrant [Owners and Members](https://docs.firehydrant.com/docs/role-based-access-controls)
* Make sure you're happy with your [configured Severities](https://docs.firehydrant.com/docs/severities-and-priorities) as well as [Conditions](https://docs.firehydrant.com/docs/conditions)
* Ensure you have components and entries within [your Service Catalog](https://docs.firehydrant.com/docs/intro-to-service-catalog)

## Configure Severity Matrix

<Image alt="Adding a new row to the Severities matrix table" align="center" src="https://files.readme.io/b96c65a-image.png">
  Adding a new row to the Severities matrix table
</Image>

1. From the FireHydrant web UI, go to **Settings** > **Severities matrix**.
2. Click on the tab for the type of component you'd like to configure automatic severities for: Services, Functionalities, or Environments.
3. Click "+ Add impact" at the bottom left of the table to add rows to the matrix. A modal will pop up where you can select the appropriate Catalog component to conditionally assign severities and impacts for. Click "Save".
4. Once the row is inserted into the table, you can configure different severities according to the condition(s) applied to the component. Click the dropdown and select the default severity for each condition applied to the given catalog component. For example, in the following example matrix:

![](https://files.readme.io/bfd76bb-image.png)

* If the **api-server** is marked as **Unavailable** when starting an incident, FireHydrant will automatically assign a `SEV1` to the incident.
* Conversely, if the **app-admin-web** is marked as **Unavailable** when starting an incident, FireHydrant will assign a `SEV2` to the incident instead.

> 📘 Note:
>
> If multiple components from the matrix are marked impacted at incident start, the higher severity takes precedence.

5. To save your severity matrix changes, click "Submit" on the bottom right of the table.

Now when anyone in your organization kicks off an incident you can be assured that it is being set to the appropriate severity based on business needs.

## Suggested Severities

<Image alt="FireHydrant warning the user that their selected severity/impact combination doesn't match what's configured in Severity Matrix" align="center" width="400px" src="https://files.readme.io/2787396-CleanShot_2024-08-13_at_16.05.21.png">
  FireHydrant warning the user that their selected severity/impact combination doesn't match what's configured in Severity Matrix
</Image>

When you've configured your severity matrix, FireHydrant will cross-check with it whenever users are declaring incidents. If the user is about to declare an incident and the set severity/impacted component combination doesn't match what's configured in the severity matrix, FireHydrant will warn them.

This is shown when declaring in Slack, MS Teams, and the web UI, and it's also available when changing severities mid-incident and the severity doesn't match the matrix in MS Teams tab interface and web UI.

## Next Steps

There are other powerful ways to automate things in FireHydrant via Runbooks. For example:

* **Take a look at the[Add Incident Impacts](https://docs.firehydrant.com/docs/runbook-step-add-incident-impacts) Runbook step to automatically mark certain components as impacted**.
  * This allows you to use the numerous other conditions available to Runbooks. For example, "if **component A** is down, then automatically mark **component B** down too," etc.
* **You can also look at the[Update Incident Details](https://docs.firehydrant.com/docs/runbook-step-update-incident-details) Runbook step**.
  * This step allows you to change the incident's details like Severity, Priority, etc. automatically. With the availability of numerous conditions, you can configure flexible automation like, "If incident has X service impacted and a tag `cache-issue` is added to the incident, then change the severity of the incident to `SEV2`.
* **You can potentially skip the Severity Matrix entirely if you want to predefine the[types of incidents](https://docs.firehydrant.com/docs/incident-types) your organization has**.
  * This simplifies the declaration process so users simply need to select a type, and everything else - from Runbooks, to severity assignment, team assignment, task lists, and more - are already pre-configured.