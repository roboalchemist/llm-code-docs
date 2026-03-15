# Source: https://docs.firehydrant.com/docs/managing-follow-ups.md

# Managing Follow-Ups

During an incident or its retrospective, responders may identify important action items that, while important, aren't urgent and should be prioritized later. On FireHydrant, we call these **Follow-Ups**, and they are distinct from [**Tasks**](/docs/task-management/) which are mid-incident items.

With FireHydrant, you can track all of your outstanding and completed **Follow-Ups** to ensure your systems are more resilient for the future. In addition, FireHydrant can sync Follow-Ups with apps you have integrated, enabling your project managers to track work seamlessly.

> 🚧 Note:
>
> Slack commands and emojis for Follow-Ups will only work within the context of an incident channel.

## Create and Manage Follow-Ups

You can add Follow-Ups from the incident's Command Center, from Slack, and the Retrospective page. When you create Follow-Ups, FireHydrant will link them to the incident ticket or story for the incident (if one was created). The same **Tasks** tab can be used in the Command Center to view and manage Follow-Ups in the web UI.

<Image alt="Adding follow-ups from Command Center in UI" align="center" width="650px" src="https://files.readme.io/7566c53-image.png">
  Adding follow-ups from Command Center in UI
</Image>

<Image alt="Follow-up modal in Slack" align="center" width="400px" src="https://files.readme.io/a6641f7-Screenshot_2023-12-06_at_1.19.48_PM.png">
  Create Follow-Ups in Slack with `/fh add follow-up`
</Image>

### Using Emojis from Slack

<Image alt="Creating a Follow-Up in Slack with an emoji" align="center" width="650px" src="https://files.readme.io/0905eed-Screenshot_2023-12-04_at_10.58.26_AM.png">
  Creating a Follow-Up in Slack with an emoji
</Image>

Like Tasks, you can create Follow-Ups by responding with an emoji. The default emoji is `:clipboard:` but this can be modified in your **Settings** > **Integrations list** > **Slack settings**. You can view all outstanding Follow-Ups by running `/fh follow-ups`.

<Image alt="Seeing Follow-Up items via `/fh follow-ups`" align="center" width="400px" src="https://files.readme.io/723eb83-image.png">
  Seeing Follow-Up items via `/fh follow-ups`
</Image>

### Inline in Retrospectives

<Image alt="Creating a follow-up inline" align="center" width="650px" src="https://files.readme.io/ec45f4382f19dcf9780703eccac802ba4f2d783b550bf62303c806e1e9efdec8-CleanShot_2025-03-28_at_15.59.20.gif">
  Creating a follow-up inline
</Image>

Our new [Retrospectives](https://docs.firehydrant.com/docs/incident-followup) experience allows not only collaborative editing in freeform text questions but also inline creation of follow-ups. Simply highlight any text and click the :heavy\_check\_mark: button on the right, and the text you've highlighted will be inserted as the title on the follow-up creation modal.

## Importing Existing Follow-Ups (Jira Cloud Only)

Specifically for Jira Cloud, FireHydrant also supports importing an existing Jira ticket as a follow-up for an incident. In  the Command Center view, click on **Add follow-up** > **Add follow-up from URL**. On the modal that pops up, you can paste the URL of the existing Jira ticket, and FireHydrant will automatically link to it.

<Image alt="Adding a Follow-Up from a URL" align="center" width="650px" src="https://files.readme.io/e82ab48-image.png">
  Adding a Follow-Up from a URL
</Image>

<Image alt="FireHydrant copies the name to the FireHydrant Follow-Up and links the original ticket" align="center" width="650px" src="https://files.readme.io/de6feee-image.png">
  FireHydrant copies the name to the FireHydrant Follow-Up and links the original ticket
</Image>

## Project & Field Mapping

You must set up their respective integrations and configure project mappings to link Follow-ups to external ticket providers. Each Project in FireHydrant will typically correspond with a project in the external tool (for example, a Jira project, an Asana project, a Linear Team, etc.).

You must configure a project mapping for each external ticketing project you want to link tickets with. When configuring the projects, you may also need to configure ticket field mappings so FireHydrant knows how to convert from FireHydrant values to values that your external ticketing tool expects.

For more information, visit docs for the following supported ticketing providers:

* [Asana](https://docs.firehydrant.com/docs/asana-integration)
* [Jira Cloud](https://docs.firehydrant.com/docs/jira-cloud-integration)
* [Jira Server (On-Premise)](https://docs.firehydrant.com/docs/jira-server-on-premise-integration)
* [Linear](https://docs.firehydrant.com/docs/linear-integration)
* [Shortcut](https://docs.firehydrant.com/docs/shortcut-integration)

### Available Fields

These are the fields available for Follow-Ups:

* **Summary** - The title for the Follow-Up.
  * This field is automatically mapped to the title/summary field of external ticketing.
* **Description** - More details for the Follow-Up if desired
  * This field is automatically mapped to the description/details field of external ticketing.
  * Due to Slack limitations, the Description field is limited to 2900 characters if created from Slack. To view a description longer than 2900 characters, open the Follow-Up in the Incident Command Center or directly in your ticketing provider (Jira, etc.).
* **Project** - Which Project in external ticketing tool(s) to create a corresponding ticket in.
  * For some ticketing providers (e.g. Shortcut), you can automatically select from the list of available projects. For other providers like Jira, you must [configure project mappings](/docs/configuring-jira-multi-project/).
* **Ticket Priority** - The priority of the Follow-Up.
  * You can customize the ticketing priorities in FireHydrant by visiting **Settings** > **Incidents** > **Ticketing settings** > **Follow-up Ticket Priorities**. However, even with the customizations, you must configure custom field mapping so FireHydrant sends the correct data in the proper format to external ticketing tools.
* **Tags** - Tags for the Follow-Up ticket
  * You will need to configure custom field mapping to define how tags on FireHydrant should map to external ticketing providers.
  * Follow-up ticket tags are separate from Incident tags.
* **Assigned to** - Who the ticket should be assigned to.
  * The user's email address in FireHydrant must match the email address in the ticketing tool for us to assign them to the external ticket correctly\*

> 📘 \*Note:
>
> This is currently not supported for [Jira Server (On-Premise)](https://docs.firehydrant.com/docs/jira-server-on-premise-integration) integration.

* **State** - The status of the Follow-Up (*Open*, *In Progress*, *Done*, or *Cancelled*)
  * These states are FireHydrant-internal and not changeable, but you can configure how these values map to external ticketing providers when configuring projects. For example, *Open* in FireHydrant may be mapped to *Backlog* in Jira.

## Next Steps

* Visit the docs for [Asana](https://docs.firehydrant.com/docs/asana-integration), [Jira Cloud](https://docs.firehydrant.com/docs/jira-cloud-integration), [Jira Server (On-Premise)](https://docs.firehydrant.com/docs/jira-server-on-premise-integration), [Linear](https://docs.firehydrant.com/docs/linear-integration) and [Shortcut](https://docs.firehydrant.com/docs/shortcut-integration) to setup your integrations and map your projects/fields
* Move on using [Internal Status Pages](https://docs.firehydrant.com/docs/internal-status-pages) and [External Status Pages](https://docs.firehydrant.com/docs/external-status-pages) on incidents