# Source: https://docs.firehydrant.com/docs/status-templates.md

# Status Templates

> 📘 Note:
>
> Only users with <Glossary>Owner</Glossary> permissions can edit/update Status Templates.

Communicating frequently to your stakeholders about an ongoing incident is essential for building trust. Deciding what to communicate can be time-consuming and stressful for a responder during an incident. Status templates allow you to have prewritten communications at responders' fingertips so they can share updates easily and get back to resolving the issue.

## Creating a new status template

In the FireHydrant UI navigation, select **Settings** and then **Status templates** under **Incident settings**. Click **Add template** in the top right corner of the page to create a new template.

Enter a descriptive *name* for the template, such as "Initial investigation," and the *body* of the message for your template. Both name and body are required and support markdown formatting.

<Image alt="Creating a new status template in FireHydrant" align="center" width="650px" src="https://files.readme.io/e1f2103-image.png">
  Creating a new status template in FireHydrant
</Image>

These status template bodies also support [Markdown](https://docs.firehydrant.com/docs/markdown-support) and [Template Variables](https://docs.firehydrant.com/docs/template-variables), so rich text and dynamic data can be rendered at the end destinations depending on where you'd like to post (e.g., status pages).

## Using status templates

When you have configured status templates, you will see them in both the FireHydrant UI and Slack when you post an update. After you select a status template, the message body will be copied into the message field. You are able to edit the message before you post your update.

### From Slack

<Image alt="Using a status template when posting updates from Slack" align="center" width="400px" src="https://files.readme.io/44311ec-image.png">
  Using a status template when posting updates from Slack
</Image>

1. In an incident channel, use the command `/fh update`
2. Select your template from the **Status template** dropdown
3. If necessary, edit the message
4. Update the milestone and status pages you want to post to
5. Click **Update**

### From the FireHydrant UI

<Image alt="Posting an update from UI with dropdown for Status Template selection" align="center" width="400px" src="https://files.readme.io/e0797b9-image.png">
  Posting an update from UI with dropdown for Status Template selection
</Image>

1. Go to the **Command Center** for an incident
2. Click **Status Pages** tab
3. Click **Add an update** for the status page you want to update
4. Select your template from the **Status template** dropdown
5. If necessary, edit the message
6. Click **Post**