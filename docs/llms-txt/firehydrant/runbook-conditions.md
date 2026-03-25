# Source: https://docs.firehydrant.com/docs/runbook-conditions.md

# Runbook Conditions

FireHydrant's Runbooks offer the powerful ability to customize execution based on various conditions. This allows controlling when certain Runbooks, as well as steps within them, should attach/execute. If you configure any [Custom Fields](https://docs.firehydrant.com/docs/incident-custom-fields), they will also be available as conditions.

## Runbook Conditions

<Image align="center" alt="Example of Runbook whose only condition is when severity is SEV1" border={false} caption="Example of Runbook whose only condition is when severity is SEV1" src="https://files.readme.io/43b8e52-CleanShot_2024-08-07_at_10.49.07.png" width="400px" />

Runbook-level conditions will determine whether a Runbook will attach to an incident. This allows you to create Runbooks tailored to specific situations, such as only `SEV1` incidents, or only incidents where `my-specific-service` is impacted.

FireHydrant is constantly scanning your incidents for matching incident conditions. This means Runbooks can attach to any of your incidents at any point in the incident lifecycle (*with some exceptions. See[Condition Expiration](#condition-expiration) below*).

### How to edit Runbook conditions

1. Click **Runbooks** in the navigation, then click the Runbook you want to configure.
2. In the edit page, you can configure Runbook conditions on the right panel under **Execution rules**.

For the full list of available conditions and triggers, visit [All Available Conditions](#all-available-conditions) below.

## Step Conditions

<Image align="center" alt="Example condition on a Runbook step" border={false} caption="Example condition on a Runbook step" src="https://files.readme.io/b1a81c1-CleanShot_2024-08-07_at_10.50.54.png" width="650px" />

Individual steps within Runbooks can also be conditionally executed.

* **Available rules**
  * Runbook execution rules include all of the available conditions for Runbook-level conditions, in addition to several execution-specific conditions
* **Scheduling**
  * You can configure certain Runbook steps to repeat on intervals or specific transitions. See [Repeating Steps](#repeating-steps).
  * You can also configure whether a step should immediately evaluate and execute, or if it should be triggered manually by a user. This can be done via the UI or via `/fh runbooks` in chat apps (see below).

> 🚧 Note:
>
> All steps within a Runbook execute concurrently as soon as the Runbook attaches. If you want to ensure sequential execution of steps, use the **Previous Runbook step** condition and reorder the steps in the order you'd like them to execute.

### How to edit step conditions

1. Follow the same steps above to navigate to the Runbook.
2. Find the specific step you'd like to add conditions to and click the writing icon on the right side.

   <Image align="center" border={false} width="650px" src="https://files.readme.io/43ad217-CleanShot_2024-08-07_at_10.54.12.png" />
3. In the modal that opens for that step, click the **Triggers** tab. This opens your options for applying rules that dictate when this specific step runs.

For the full list of available conditions and triggers, visit [All Available Conditions](#all-available-conditions) below.

## Repeating steps

Some Runbook steps allow for repetition and rescheduling, depending on the conditions selected. This allows, for example, things like reminding the incident channel to post updates **every 30 minutes** or to send an email on every incident update or note. If a step can be repeated, you will see extra checkboxes.

### Repeat on Interval

<Image align="center" alt="Setting a repetition interval for a step" border={false} caption="Setting a repetition interval for a step" src="https://files.readme.io/9024176-CleanShot_2024-08-07_at_11.14.16.png" width="650px" />

By default, the checkbox for **Repeat After Interval** is available for any steps that can be repeated. When checked, an additional input is shown to specify the repetition time. This interval repeat behavior is mutually exclusive to repeating on transitions, covered in the next subsection.

> 📘 Note:
>
> The shortest interval allowed today is 5 minutes.

### Rerun on every transition

<Image align="center" alt="Rerun on every transition checkbox enabled" border={false} caption="Rerun on every transition checkbox enabled" src="https://files.readme.io/77fd947-CleanShot_2024-08-07_at_11.16.30.png" width="650px" />

The other repetition option is for specific incident updates or transitions. This checkbox is only enabled when certain conditions are selected:

* **Current milestone\[changes, moves forward, moves backward]**
* **Current severity\[changes, escalates, de-escalates]**
* **Incident Note\[is added]**

When this checkbox is enabled, the step will automatically reschedule and re-evaluate conditions after the specified change triggers it. This repetition option is mutually exclusive to interval repetitions.

## Condition Expiration

Runbooks and Steps will not always execute or be on the lookout for forever. FireHydrant expires condition checks for Runbooks and Steps based on various conditions.

### Runbook Expiration

FireHydrant will stop checking incidents for matching Runbook conditions when one of the following occurs:

* **The incident reaches the`Resolved` milestone**
  * After an incident is resolved, no new Runbooks will automatically attach, even if conditions match. You will need to attach them manually. "When Current milestone = Resolved," etc., conditions will still not automatically attach the Runbook.
* **The Runbook has already attached**
  * We do not support unattaching and reattaching the same Runbooks to the same incident currently. You may stop/restart the Runbook, but this will re-execute the same steps configured before. Other Runbooks not yet attached will still be evaluated as normal.
* **The incident is older than 90 days**
  * All condition checks expire after 90 days, even if an incident has not been resolved yet. So, any changes to an incident after 90 days will not trigger a new Runbook attachment.

If you want Runbooks to attach post-resolution, you can workaround this limitation by adding a [Attach a Runbook](https://docs.firehydrant.com/docs/runbook-step-attach-a-runbook) step to other Runbooks that do attach pre-resolution.

Alternatively, you can still manually attach a Runbook to an incident at any time.

### Step Expiration

FireHydrant will expire steps or certain aspects of steps when one of the following occurs:

* **When the incident reaches the`Resolved` milestone**\*\*
  * FireHydrant terminates any recurring steps when an incident is resolved
  * \*\*This does not apply to post-incident steps/conditions (e.g. `When current milestone is Retrospective Completed`). Those will still execute as normal post-resolution.
* **When a step has been polling for longer than 90 days**
  * If a step has been waiting and checking for matching conditions for longer than 90 days, the step will expire.

## All Available Conditions

### Runbook Only

These conditions are only available at the Runbook level and must be evaluated to true first before the steps within are evaluated/executed.

* **Use for tutorial incidents** - Controls whether this is the Runbook used for `/fh tutorial`/`@FireHydrant tutorial` commands.
* **Restrict to private incidents only** - Specific setting to toggle whether this Runbook will attach to private incidents. Runbooks are mutually exclusive to each type - they can only attach to general incidents OR private incidents, not both. For more information, see [Private Incidents](https://docs.firehydrant.com/docs/private-incidents).
* **Manual Attachment only**/**When invoked manually** - The Runbook will not automatically attach; at some point, a user must manually attach the Runbook to an incident for it to execute.

### Steps Only

These steps are only applicable to specific Runbook steps and will not be found at the Runbook level.

* **Previous Runbook step** - Dependency on the result of the previous Runbook step (e.g., directly above this one). Can choose from **Started**, **Errored**, **Completed** (successfully)

### Both

These conditions exist at both Runbook and Step levels.

* **Incident Slack channel** - Whether the incident has or does not have an existing [Slack channel](https://docs.firehydrant.com/docs/runbook-step-create-incident-channel)
* **Incident Microsoft Teams channel** - Whether the incident has or does not have an existing [Microsoft Teams channel](https://docs.firehydrant.com/docs/runbook-step-create-microsoft-teams-incident-channel)
* **Current milestone** - If the current [milestone](https://docs.firehydrant.com/docs/incident-milestones) matches the supplied conditions:
  * **Is** - Direct match for a specific milestone
  * **Is not** - Direct non-match for specific milestone
  * **Is one of** - Matches any of a list of milestones
  * **Is not one of** - Excluding any of a list of milestones
  * **Changes** - Triggers when the milestone changes in either direction
  * **Moves forward** - Triggers when the milestone moves forward (e.g., *Acknowledged* -> *Investigating*)
  * **Moves backward** - Triggers when the milestone moves backward (e.g., *Mitigated* -> *Identified*)
* **Current severity** - If the current [severity](https://docs.firehydrant.com/docs/severities-and-priorities) matches the supplied conditions:
  * **Is** - Matches a specific severity
  * **Is not** - Does not match a specific severity
  * **Is one of** - Matches any of a list of severities
  * **Is not one of** - Does not match any of a list of severities
  * **Matches regex** - Matches a pattern of severity or severities
  * **Changes** - On any severity change
  * **Escalates** - Triggers when the severity increases (e.g., *SEV2* -> *SEV1*)
  * **De-escalates** - Triggers when the severity decreases (e.g., *SEV1 -> SEV2*)
* **Current priority** - If the current [priority](https://docs.firehydrant.com/docs/severities-and-priorities) matches the supplied conditions:
  * **Is** - Matches a specific priority
  * **Is not** - Does not match a specific priority
  * **Is one of** - Matches any of a list of priorities
  * **Is not one of** - Does not match any of a list of priorities
  * **Matches regex** - Matches a pattern of priority or priorities
* **Incident tags** - If the current [tags](https://docs.firehydrant.com/docs/incident-tags) match the supplied conditions
  * **Includes any of** - OR match for any tag in the list
  * **Includes all of** - AND match for all tags in the list
  * **Does not include any of** - No match for any tag in the list
  * **Is empty** - No tags on the incident
  * **Is not empty** - If at least one tag on the incident
* **Incident ticket** - Whether the incident already has an [incident ticket](/docs/integrations-overview#ticketing-integrations) created
* **Time since incident opened** - Checks the time elapsed from when the incident was declared/started on FireHydrant
* **Time since last incident note** - Checks the time elapsed from when there was last an incident note or update (not general chat messages, but specifically incident updates)
* **Incident assigned roles** - Whether the specified role(s) has/have at least one person assigned
* **Incident assigned teams** - Whether the specified team(s) have been assigned to the incident
* **Incident impacted infrastructure** - Whether the incident has any of the specified [Service Catalog components](https://docs.firehydrant.com/docs/service-catalog-basics) marked as impacted
* **Incident impacted service tiers** - Whether any of the specified Service Catalog components impacted on the incident match the specified tiers
* **Incident attached Runbooks** - Whether the specified Runbooks are also attached to the Incident
* **Incident Note** - Specific trigger for when an incident update/note is posted. Supports transition-based repetition
* **Incident type** - Specific trigger for when an incident is created from a specific [Incident Type](https://docs.firehydrant.com/docs/incident-types)
* **Incident details changed** - Triggers whenever any of the selected fields have been modified on an incident. The available triggers include changes to Name, Description, Severity, Priority, Milestone, and Impacted Infrastructure.
* **Incident restricted** - Whether the incident is private or not private
* **AI Summary** - Whether an AI-generated audience summary exists or changes for a specific audience. This allows you to trigger runbook steps (such as sending emails or other communications) based on the presence or updates to audience-specific summaries
* **Custom Fields** - Conditions according to your defined [custom fields](https://docs.firehydrant.com/docs/incident-custom-fields). Depending on the type of custom field, you may see options such as:
  * **Includes any of** OR **Is one of** - Matches on a list of specified item(s)
  * **Includes all of** - Must include all specified item(s)
  * **Does not include** - Does not include specified item(s)
  * **Is empty** OR **Does not exist** - No value is specified
  * **Is** - Matches exactly specified value
  * **Exists** - A value is specified
  * **Matches regex** - Matches a pattern of specified item(s)
* **Time since milestone \[...]** - Checks the time elapsed from when the incident first entered the specified milestone

## Resolved and Retrospective States

When any incident reaches the **Resolved<Glossary>Milestone</Glossary>** or beyond, any automation on Runbooks will change to a delayed model that executes every 10 minutes.

For example, if you have a step to [Archive Incident Channel](https://docs.firehydrant.com/docs/runbook-step-archive-incident-channel) when the Milestone is **Retrospective Completed**, it may not archive immediately after you've completed your retro.

However, steps will consistently execute within 10 minutes after an incident is resolved.

## Race Conditions

Several Runbook steps have prerequisites. As noted above, all steps within a Runbook execute concurrently upon attachment to an incident. Subsequently, you'll need to be aware of potential race conditions for steps that require certain things. Some examples:

* Let's say you want to [Add a Bookmark to Incident Channel](https://docs.firehydrant.com/docs/runbook-step-add-a-bookmark-to-incident-channel). You will need to, for example, ensure in the conditions for that step that the **Incident channel exists**. This will delay the step from executing until the channel is confirmed created, otherwise it may try to set a bookmark in a non-existent channel and fail.
* If you want to [name the incident channel](https://docs.firehydrant.com/docs/runbook-step-create-incident-channel) after [the Jira ticket](https://docs.firehydrant.com/docs/runbook-step-create-a-jira-issue), then you'll want to either set the condition to **Previous step has completed** and put the Slack channel step just after the Jira step. Or, you can use the **Incident ticket exists** condition.

In general, if a Runbook step depends on some condition that another Runbook step changes, then you'll want to pay careful attention to the conditions of downstream, dependent steps to avoid race conditions.

## Next Steps

* Read about [Runbook Best Practices](https://docs.firehydrant.com/docs/runbook-best-practices) for strategies on how to organize your automation
* Browse the list of available [Runbook Steps](https://docs.firehydrant.com/docs/runbook-steps)