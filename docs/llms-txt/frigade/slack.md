# Source: https://docs.frigade.com/integrations/slack.md

# Slack

> Easily send messages to a Slack channel when users take actions in your Flows

<Steps>
  <Step title="Create a Slack Workflow">
    In Slack, open the Workflow page by searching for **Workflows** in the search bar and click the **Create a Workflow** button. Then, choose the **From a webhook** option:

    <img src="https://mintlify.s3.us-west-1.amazonaws.com/frigade-docs/images/integrations/slack/slack-1.png" className="rounded" />
  </Step>

  <Step title="Create a webhook in Frigade">
    Copy the **Webhook request URL** from Slack. Then press **X**.

    <img src="https://mintlify.s3.us-west-1.amazonaws.com/frigade-docs/images/integrations/slack/slack-2.png" className="rounded" />

    In the Frigade dashboard, navigate to the **Developer** section and click on **Webhooks**. Click the **New webhook** button and fill in the details as shown below with your Flow of choice. In this example, we use a simple [Form Flow](/component/form):

    <img src="https://mintlify.s3.us-west-1.amazonaws.com/frigade-docs/images/integrations/slack/slack-3.png" className="rounded" />

    <Tip>You can use a free service such as [Webhook.site](https://webhook.site/) to test your webhook.</Tip>
  </Step>

  <Step title="Set up data variables in Slack">
    In the Slack Workflow, click the **Starts with a webhook** card at the top and add the variables you'd like to send in your Slack message as seen below:

    <img src="https://mintlify.s3.us-west-1.amazonaws.com/frigade-docs/images/integrations/slack/slack-4.png" className="rounded" />

    By default Frigade sends `user__email` and `user__name` for the given user if the data has been [provided in the SDK](/sdk/hooks/user). In this case, we also want to send the value of the `message` field from the Form Flow. To do this, we add a new variable `data__data__message` to map it to the field. You can target any field in a Frigade Form by prefixing the variable name with `data__data__`.
    <Tip>Select and radio form inputs will include both the label and the value in the webhook.  Therefore, if your field is named `industry` you should use `data__data__industry__label` to get the label or `data__data__industry__value` to get the value.</Tip>
  </Step>

  <Step title="Send a message to a Slack channel">
    Add a new step to the Slack Workflow by clicking the **Messages** link in the right menu. Then pick your channel of choice and add the variables you'd like to send in your Slack message as seen below:

    <img src="https://mintlify.s3.us-west-1.amazonaws.com/frigade-docs/images/integrations/slack/slack-5.png" className="rounded" />

    Finally, hit the **Publish** button in the top right corner to make your Slack Workflow live.
  </Step>

  <Step title="Test your Slack integration">
    You're now all set to test your Slack integration. In your application, complete the Flow you've set up the webhook for. In this case, we'll submit the Form Flow:

    <img src="https://mintlify.s3.us-west-1.amazonaws.com/frigade-docs/images/integrations/slack/slack-6.png" className="rounded" />

    After completing a step in the Frigade Flow, you should now see the following show up in your Slack channel:

    <img src="https://mintlify.s3.us-west-1.amazonaws.com/frigade-docs/images/integrations/slack/slack-7.png" className="rounded" />
  </Step>
</Steps>

That's it! You've successfully integrated Slack with Frigade. Remember, Frigade webhooks are unique for the Development and Production environments, so make sure to create a new webhook for each environment you want to integrate with Slack.

# Example

If you want a new Slack message when a user provides an NPS score in a Frigade Form, you can set up a webhook in Frigade and a Slack Workflow as follows:

1. Create a new workflow in Slack and copy the Webhook URL.
2. Create a new webhook in Frigade and paste the Slack Webhook URL.
3. Pick **Flow completed** and **Flow dismissed**.
4. Add the variables `data__nps-score-page__nps-score` (for the NPS Score) and `data__nps-feedback-page__nps-feedback-text` (for the NPS Comment) to the Slack Workflow.
5. Craft a message and pick a channel to send the data to.
