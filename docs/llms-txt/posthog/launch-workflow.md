# Source: https://posthog.com/docs/workflows/launch-workflow.md

# Launch your first workflow - Docs

This guide covers creating a very basic workflow where we send an email to users who perform an event on your app or site. Since we are sending a message (email), you will need to set up a [channel](/docs/workflows/configure-channels.md) first.

See the [workflow builder](/docs/workflows/workflow-builder.md) for more information on the different components of a workflow, and see the end of this guide for more examples.

1.  1

    ## Create a workflow

    Required

    Go to [Workflows](https://app.posthog.com/workflows) and click the **\+ New workflow button**.

    ![Click the New Workflow button](https://res.cloudinary.com/dmukukwp6/image/upload/w_1600,c_limit,q_auto,f_auto/messaging_new_campaign_light_c1f7b79b46.png)![Click the New Workflow button](https://res.cloudinary.com/dmukukwp6/image/upload/w_1600,c_limit,q_auto,f_auto/messaging_new_campaign_light_c1f7b79b46.png)

    This will open the workflow builder:

    ![Fresh workflow with trigger block](https://res.cloudinary.com/dmukukwp6/image/upload/w_1600,c_limit,q_auto,f_auto/new_campaign_light_acfabde4ca.png)![Fresh workflow with trigger block](https://res.cloudinary.com/dmukukwp6/image/upload/w_1600,c_limit,q_auto,f_auto/new_campaign_dark_8ed34dd06e.png)

    The new workflow only has two blocks:

    -   A trigger block: This defines the event that will start the workflow.
    -   An exit block: This defines the event that will end the workflow.

    On the right side of the workflow builder, you can see the types of blocks available to add to your workflow.

2.  2

    ## Configure the trigger

    Required

    Now, let's click on the trigger block and configure it. In a new workflow, the trigger doesn't have any trigger events. Triggers tell PostHog what events will start the workflow.

    ![Trigger warning that event is required](https://res.cloudinary.com/dmukukwp6/image/upload/q_auto,f_auto/frequency_trigger_ff50a0016d.png)![Trigger warning that event is required](https://res.cloudinary.com/dmukukwp6/image/upload/q_auto,f_auto/frequency_trigger_ff50a0016d.png)

    Click the **\+ Add trigger event** button and search for the event you want to use as the trigger. In this example, we'll use a `pageview` event to send an email to **any** users who view a page on our website.

    You can use any PostHog event as a trigger. For example, you could add a button in your app that captures a `test_email` event when clicked.

    Change the frequency drop down to `"One time"` this means a user cannot be re-enrolled once they are in the workflow

3.  3

    ## Add an Dispatch

    Required

    Now that we have a trigger that can initiate the workflow, we need to add an Dispatch to send a message to the users who trigger the workflow.

    ## Email

    Drag an **Email** dispatch beneath the trigger, into the workflow. Then, click on the email block to configure it.

    ![Configure email template](https://res.cloudinary.com/dmukukwp6/image/upload/w_1600,c_limit,q_auto,f_auto/configure_email_template_light_ed7a551fec.png)![Configure email template](https://res.cloudinary.com/dmukukwp6/image/upload/w_1600,c_limit,q_auto,f_auto/configure_email_template_dark_a58f62c95f.png)

    In the email template, you can configure the following:

    | Field | Description |
    | --- | --- |
    | From | A sender address configured in your channels. |
    | To | The email address of the recipient. By default, it targets the user whose event triggered the workflow. |
    | Subject | The subject line of the email. |
    | Preheader | The optional preheader of the email. |
    | Body | The content of the email. You can use the built-in editor to format your email or use a custom template. |
    | Cc | An optional comma-separated list of CC recipients. |
    | Bcc | An optional comma-separated list of hidden BCC recipients. |
    | Reply-To | An optional comma-separated list of reply-to email addresses. |

    During testing, you can hardcode your own email address in the **To** field for testing.

    The email template has access to event and person properties of the trigger event. You can learn more about this in the [workflow builder](/docs/workflows/workflow-builder.md) documentation.

    ## Slack

    Drag a **Slack** dispatch beneath the trigger, into the workflow. Then, click on the Slack block to configure it.

    In the Slack step, you'll need to configure the following:

    -   **Slack workspace**: Select the Slack workspace you connected to when you configured your Slack workflow channel.
    -   **Channel to post to**: This is the Slack channel messages will be delivered to.
    -   **Emoji icon**: Optional emoji for the bot.
    -   **Bot name**: Optional name for the bot.
    -   **Blocks**: Optionally define [blocks](https://docs.slack.dev/block-kit/) to compose your message.
    -   **Plain text message**: The content of your Slack message. You can use templating variables like `{{ event.event }}` to include event properties in the message.

    ## Twilio

    Drag a **SMS** dispatch beneath the trigger, into the workflow. Then, click on the SMS block to configure it.

    In the SMS step, you'll need to configure the following:

    | Field | Description |
    | --- | --- |
    | Twilio account | The Twilio account you connected when you [configured your channels](/docs/workflows/configure-channels.md). |
    | From phone number | One of the phone numbers available on your Twilio account. |
    | Recipient phone number | The recipient's number. If your workflow is triggered by an identified event, use {{ person.properties.phone }} to reference it from [person properties](/docs/product-analytics/person-properties.md). |
    | Message | The content of your SMS message. You can use templating variables like {{ event.event }} to include event properties in the message. |

4.  ## Test the workflow

    Checkpoint

    *Confirm you can trigger the workflow*

    Before publishing the workflow, you can test it to confirm it works as expected. On the right side of the workflow builder, you can see the **Test** button.

    ![Test workflow](https://res.cloudinary.com/dmukukwp6/image/upload/w_1600,c_limit,q_auto,f_auto/test_campaign_light_898c0791af.png)![Test workflow](https://res.cloudinary.com/dmukukwp6/image/upload/w_1600,c_limit,q_auto,f_auto/test_campaign_dark_9ffc6cdd44.png)

    When you click the **Test** button, you will be directed to test the workflow by creating a mock trigger. The following options are available:

    -   **Make a real request to PostHog:** When enabled, real messages will be delivered to the recipient. When disabled, API calls are mocked and logged.
    -   **Test event:** Click to expand the test event configuration. An example event will be generated by default. You can click the **Load new event** to load a real event's data into the test event.

    You can click the **Run test** button to send the test event. When the test runs, the workflow edges animate with a green highlight to show the execution path, making it easy to see which branches are taken in conditional workflows.

5.  4

    ## Enable the workflow

    Required

    **Saving drafts**

    You can save your workflow as a draft at any point, even with incomplete configuration. Validation is only enforced when you click **Enable**, not when saving.

    Once you have confirmed the workflow works as expected, you can enable it by clicking the **Enable** button at the top right of the workflow builder.

    This will publish the workflow and start delivering messages to your users when the trigger event is triggered. For this example workflow, you can hardcode all emails to your own email address for testing.

6.  ## Monitor the workflow

    Checkpoint

    *Confirm messages are being delivered*

    Once the workflow is enabled, you can monitor your workflow in the **Metrics** and **Logs** tabs of the workflow builder.

    To confirm your workflow is delivering messages, look for these signs:

    -   In the **Metrics** tab, you should see a line chart showing the number of **succeeded** and **triggered** messages.
    -   In the **Logs** tab, you can see logs of recently triggered workflows. Confirm that there aren't any errors.
    -   See the message delivered in your inbox.

7.  ## Troubleshooting

    Checkpoint

    *Common issues you may encounter*

    | Issue | Solution |
    | --- | --- |
    | Emails not sending? | Check that your domain is verified and you've added the DNS records correctly. |
    | Spam folder issues? | Ensure SPF/DKIM are valid, and consider setting up DMARC. |
    | Variables not populating? | Confirm the property exists on the person profile (e.g. person.name). |

### Community questions

Ask a question

### Was this page useful?

HelpfulCould be better