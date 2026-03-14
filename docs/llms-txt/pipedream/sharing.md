# Source: https://pipedream.com/docs/workflows/building-workflows/sharing.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://pipedream.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Sharing Workflows

You can share your workflows as templates with other Pipedream accounts with a unique shareable link.

Creating a share link for your workflow will allow anyone with the link to create a template version of your workflow in their own Pipedream account. This will allow others to use your workflow with their own Pipedream account and also their own connected accounts.

[Here’s an example of a workflow](https://pipedream.com/new?h=tch_OYWfjz) that sends you a daily SMS message with today’s schedule:

<Frame>
  <img src="https://mintcdn.com/pipedream/h8oodpUDiyR1Ssvt/images/3cb292b5-New_Project_6_n63kju.png?fit=max&auto=format&n=h8oodpUDiyR1Ssvt&q=85&s=1cf0286e8cf98b6fdf33412b94d6467a" width="400" height="400" data-path="images/3cb292b5-New_Project_6_n63kju.png" />
</Frame>

Click **Deploy to Pipedream** below to create a copy of this workflow in your own Pipedream account.

<Card horizontal icon="rocket" href="https://pipedream.com/new?h=tch_OYWfjz">
  Deploy to Pipedream
</Card>

The copied workflow includes the same trigger, steps, and connected account configuration, but it has a separate event history and versioning from the original.

<Warning>
  Steps that are paused within your workflow will be omitted from the generated share link.
</Warning>

## Creating a share link for a workflow

To share a workflow, open the workflow in your browser. Then in the top right menu, select **Create Share Link**.

<Frame>
  <img src="https://mintcdn.com/pipedream/h8oodpUDiyR1Ssvt/images/3f019305-image.png?fit=max&auto=format&n=h8oodpUDiyR1Ssvt&q=85&s=7542ff6023e888936226fe86d5e3cce2" width="868" height="779" data-path="images/3f019305-image.png" />
</Frame>

Now you can define which prop values should be included in this shareable link.

### Including props

Optionally, you can include the actual individual prop configurations as well. This helps speed up workflow development if the workflow relies on specific prop values to function properly.

You can choose to **Include all** prop values if you’d like, or only select specific props.

For the daily schedule reminder workflow, we included the props for filtering Google Calendar events, but we did *not* include the SMS number to send the message to. This is because the end user of this workflow will use their own phone number instead:

<Frame>
  <img src="https://mintcdn.com/pipedream/Acz4Z1ch6TM7-aI8/images/acaac04b-image.png?fit=max&auto=format&n=Acz4Z1ch6TM7-aI8&q=85&s=6185fbc32b89b5578f78841aae363897" width="1080" height="1338" data-path="images/acaac04b-image.png" />
</Frame>

<Note>
  **Your connected accounts are not shared.** When other users configure your workflow from the shared link they’ll be prompted to connect their own accounts.
</Note>

### Versioning

* When you create a shared link for your workflow, that link is frozen to the version of your workflow at the time the link was created
* If you make changes to the original workflow, those changes will *not* be included in the shared workflow link, nor in any workflows copied from the original shared link
* To push out new changes to a workflow, you’ll need to generate a new share link

<Note>
  **Share links persist**. You can create multiple share links for the same workflow with different prop configurations, or even different steps. Share links do not expire, nor do newly created link overwrite existing ones.
</Note>

## FAQ

### If changes are made to the original workflow, will copied versions of the workflow from the shared link also change?

No, workflows copied from a shared link will have separate version histories from the original workflow. You can modify your original workflow and it will not affect copied workflows.

### Will my connected accounts be shared with the workflow?

No, your connected accounts are not shared. Instead, copied workflows display a slot in actions that require a connected account, so the user of the copied workflow can provide their own accounts instead.

For example, if one of your steps relies on a Slack connected account to send a message, then the copied workflow will display the need to connect a Slack account.

### I haven’t made any changes to my workflow, but if I generate another shared link will it override my original link?

No, if the steps and prop configuration of the workflow is exactly the same, then the shared link URL will also be exactly the same.

The shared workflow link is determined by the configuration of your workflow, it’s not a randomly generated ID.

### Will generating new shared links disable or delete old links?

No, each link you generate will be available even if you create new versions based on changes or included props from the original workflow.

### What plan is this feature available on?

Sharing workflows via link is available on all plans, including the Free plan.

### Do users of my workflow need to have a subscription?

To copy a workflow, a subscription is not required. However, the copied workflow is subject to the current workspace’s plan limits.

For example, if a workflow requires more connected accounts than what’s available on the [Free plan](/pricing/#free-plan), then users of your workflow will require a plan to run the workflow properly.

### Will copies of my workflow use my credits?

No. Copied workflows have entirely separate versioning, connected accounts, and billing. Sharing workflow copies is free, and the user of the copy usage is responsible for credit usage. Your original workflow is entirely separate from the copy.

### How can I transfer all of my workflows from one account to another?

It’s only possible to share a single workflow at time with a link at this time.

If you’re trying to migrate all resources from one workspace to another [please contact us for help](mailto:support@pipedream.com).

### Are step notes included when I share a workflow?

Yes any [step notes](/workflows/#step-notes) you’ve added to your workflow are included in the copied version.

Built with [Mintlify](https://mintlify.com).
