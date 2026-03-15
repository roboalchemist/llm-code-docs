# Source: https://docs.firehydrant.com/docs/runbook-best-practices.md

# Runbook Best Practices

Runbooks, when used correctly, can not only automate your processes but also help organize different responses across various situations and teams.

Runbooks are constantly polling for matching conditions on incidents, **which enables powerful "layering" and "escalation" abilities.** For example, an incident can be "escalated" from **SEV2** to **SEV1** and subsequently attach the SEV1 Runbook and fire SEV1-specific automation.

If you haven't already, you can read [Runbooks Basics](https://docs.firehydrant.com/docs/runbooks-basics) and [Runbook Conditions](https://docs.firehydrant.com/docs/runbook-conditions) to learn how they work, as they play key roles in the examples presented below.

Below are examples of common paradigms we've seen FireHydrant customers use.

## Common, Organization-Wide Response

<Image align="center" width="400px" src="https://files.readme.io/2c087fe-image.png" />

Many organizations, especially if smaller, may find value in keeping automation simple. This can mean having just a single primary Runbook that will **Always attach** and handle most of the necessities. The most common Runbook steps usually include:

* [Create Incident Channel](https://docs.firehydrant.com/docs/runbook-step-create-incident-channel)
* [Create a Zoom Meeting](https://docs.firehydrant.com/docs/runbook-step-create-a-zoom-meeting) (or other video conferencing)
* [Create a Jira Issue](https://docs.firehydrant.com/docs/runbook-step-create-a-jira-issue) (or other ticketing)
* [Assign a Role](https://docs.firehydrant.com/docs/runbook-step-assign-a-role) or [Assign a Team](https://docs.firehydrant.com/docs/runbook-step-assign-a-team) (often SRE)
* [Add Task List](https://docs.firehydrant.com/docs/runbook-step-add-task-list)
* [Notify Channel](https://docs.firehydrant.com/docs/runbook-step-notify-channel) or [Notify Channel w/ Custom Message](https://docs.firehydrant.com/docs/runbook-step-notify-channel-w-custom-message)
* [Export Retrospective to Confluence](https://docs.firehydrant.com/docs/runbook-step-export-retrospective-to-confluence) or [Export Retrospective to Google Docs](https://docs.firehydrant.com/docs/runbook-step-export-to-google-docs)
* [Archive Incident Channel](https://docs.firehydrant.com/docs/runbook-step-archive-incident-channel)

The steps above help promote robust, consistent incident response regardless of the situation.

## Severity-Based Response

<Image align="center" width="650px" src="https://files.readme.io/a300aac-image.png" />

Some organizations will have different responses based on differing severities of an incident. They may start from the lowest severity, add the most common steps, and escalate from there. For example:

* **SEV3 and Up Runbook: if Severity == SEV3, SEV2, or SEV1**
  * [Create a Jira Issue](https://docs.firehydrant.com/docs/runbook-step-create-a-jira-issue) (or other ticketing)
  * [Create Incident Channel](https://docs.firehydrant.com/docs/runbook-step-create-incident-channel)
  * [Assign a Role](https://docs.firehydrant.com/docs/runbook-step-assign-a-role)
  * [Archive Incident Channel](https://docs.firehydrant.com/docs/runbook-step-archive-incident-channel) (when Milestone is Retrospective Completed)
* **SEV2 and Up Runbook: if Severity == SEV2 or SEV1**
  * [Create a Zoom Meeting](https://docs.firehydrant.com/docs/runbook-step-create-a-zoom-meeting) (or other video conferencing)
  * [Publish to Status Page (FireHydrant)](https://docs.firehydrant.com/docs/runbook-step-publish-to-status-page-firehydrant) or [Create a Statuspage.io Incident](https://docs.firehydrant.com/docs/runbook-step-create-a-statuspageio-incident)
  * [Assign a Team](https://docs.firehydrant.com/docs/runbook-step-assign-a-team) (e.g., Customer Support/Success for comms)
  * [Export Retrospective to Confluence](https://docs.firehydrant.com/docs/runbook-step-export-retrospective-to-confluence) or [Export Retrospective to Google Docs](https://docs.firehydrant.com/docs/runbook-step-export-to-google-docs) (when Milestone is Retrospective Completed)
* **SEV1 Runbook: if Severity == SEV1**
  * [Send an Email Notification](https://docs.firehydrant.com/docs/runbook-step-send-an-email-notification) (e.g. email stakeholders/execs)
  * [Create PagerDuty Incident](https://docs.firehydrant.com/docs/runbook-step-create-pagerduty-incident) (e.g. page technical leadership)
  * [Notify Channel](https://docs.firehydrant.com/docs/runbook-step-notify-channel) (e.g., notify other Slack channels of a major ongoing incident)
  * [Notify Incident Channel w/ Custom Message](https://docs.firehydrant.com/docs/notify-incident-channel-w-custom-message) (e.g., remind the incident channel to post updates every 15 minutes, etc.)

The above example uses a layering strategy to intensify the response as an incident progressively becomes more severe. Most notably, it works for both new incidents that start at a specific severity and when incidents escalate and change severity.

## NOC and Team-Based Response

<Image align="center" width="650px" src="https://files.readme.io/af820f5-image.png" />

Some organizations have not adopted <Glossary>Service Ownership</Glossary> and always have a front line of defense to respond to incidents. From there, they will try to resolve the incidents themselves or may call on extra help when needed.

This strategy helps when teams always have an initial responding team who will try to diagnose the issue. In these instances, they will typically know which additional teams need to be called in and directly summon them.

* **On-call/Primary Runbook: always**
  * [Create Incident Channel](https://docs.firehydrant.com/docs/runbook-step-create-incident-channel)
  * [Create a Jira Issue](https://docs.firehydrant.com/docs/runbook-step-create-a-jira-issue) (or other ticketing)
  * [Assign a Role](https://docs.firehydrant.com/docs/runbook-step-assign-a-role)
  * [Create a Zoom Meeting](https://docs.firehydrant.com/docs/runbook-step-create-a-zoom-meeting) (or other video conferencing)
  * [Publish to Status Page (FireHydrant)](https://docs.firehydrant.com/docs/runbook-step-publish-to-status-page-firehydrant) or [Create a Statuspage.io Incident](https://docs.firehydrant.com/docs/runbook-step-create-a-statuspageio-incident)
  * [Export Retrospective to Confluence](https://docs.firehydrant.com/docs/runbook-step-export-retrospective-to-confluence) or [Export Retrospective to Google Docs](https://docs.firehydrant.com/docs/runbook-step-export-to-google-docs) (when Milestone is Retrospective Completed)
  * [Archive Incident Channel](https://docs.firehydrant.com/docs/runbook-step-archive-incident-channel) (when Milestone is Retrospective Completed)
* **Team-Specific Runbook(s): when assigned**
  * [Create PagerDuty Incident](https://docs.firehydrant.com/docs/runbook-step-create-pagerduty-incident) (or other alerting)
  * [Send an Email Notification](https://docs.firehydrant.com/docs/runbook-step-send-an-email-notification)
  * [Notify Channel](https://docs.firehydrant.com/docs/runbook-step-notify-channel) or [Notify Channel w/ Custom Message](https://docs.firehydrant.com/docs/runbook-step-notify-channel-w-custom-message)
  * [Update Incident Details](https://docs.firehydrant.com/docs/runbook-step-update-incident-details)
  * [Add Task List](https://docs.firehydrant.com/docs/runbook-step-add-task-list)

Generally, FireHydrant recommends using Function/Service-Based response (see next section), but the NOC-type response is still very common throughout the industry and FireHydrant's Runbooks will help standardize automation and response regardless of paradigm.

## Function/Service-Based Response

![](https://files.readme.io/424cdba-image.png)

This paradigm is similar to team-based, but rather than focusing specifically on teams, teams are the outcome, and the focus is on functionality or service impact.

With FireHydrant's [Service Catalog](https://docs.firehydrant.com/docs/intro-to-service-catalog), you can link together <Glossary>Services</Glossary> with their respective <Glossary>Functionalities</Glossary>. So if a ticket comes in from a customer or an internal, non-engineering resource notices something is funky with the website, they already know what they need to declare an incident and pull in the #web-team.

## Combination

Once FireHydrant users become familiar with the platform, the most common scenario we see customers use is a combination of the previous paradigms. For example:

<Image align="center" width="650px" src="https://files.readme.io/1bdf654-runbook-layering-example.png" />

Users will most often segregate specific automation by severity and impacted functions within the platform. They may also have dedicated Runbooks specific to teams if individual teams have different naming conventions for their channels and tickets or require specific webhooks, bookmarks, notifications, etc.

## Other Tips

### Keep Runbooks specific

Try to keep Runbooks trim, generally single-purpose and descriptive, similar to writing a function in a programming language. This can simplify maintenance, diagnosing issues, and upkeep of your Runbooks over the long run.

### Align the organization

Given the flexibility of Runbooks, it helps to ensure your organization is aligned on how to organize them. Differing or conflicting methodologies may lead to duplicate and/or repeated Runbook steps between multiple Runbooks. For example, if you have a common Runbook that all incidents/teams must share, then make sure your individual team members know this when they are constructing their own Runbooks.

### Test your Runbooks

All Runbooks have a **Test** button that allows you to execute that Runbook in isolation. This is useful for testing out new steps or changes you've just made. These test incidents are `GAMEDAY` severity, meaning they won't impact your analytics, and these incidents will not attach any other Runbooks.

<Image align="center" width="400px" src="https://files.readme.io/4dc185c-image.png" />

<Image align="center" width="400px" src="https://files.readme.io/8552347-image.png" />

### :warning: ONLY UNINSTALL INTEGRATIONS AS A LAST RESORT

If things don't seem to be working, try things like removing the Runbook step and re-adding to the Runbook, tweaking conditions, etc., as opposed to uninstalling the integration.

**If you uninstall the integration**, all Runbook steps for that particular integration must be deleted and re-added because the connection information is tethered to each Runbook step.

## Next Steps

* Build your Runbooks!
* Learn more about our [Service Catalog](https://docs.firehydrant.com/docs/intro-to-service-catalog) and how, in conjunction with Runbooks, your response process can be streamlined
* Browse the array of [Available Runbook Steps](https://docs.firehydrant.com/docs/runbook-steps) we have