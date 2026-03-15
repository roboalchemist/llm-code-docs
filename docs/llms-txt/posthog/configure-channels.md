# Source: https://posthog.com/docs/workflows/configure-channels.md

# Configure a workflows channel - Docs

1.  1

    ## Create a new workflows channel

    Required

    Before you can design a workflow, you need to configure a workflows channel. Channels let you dispatch actions or messages to your users.

    To create a new channel, go to workflows > [**Channels** tab](https://app.posthog.com/workflows/channels) > click **\+ New channel**, and select the channel you want to configure:

    **CDP channels**

    Other than the channels shown below, you can also dispatch to any [realtime destination](/docs/cdp/destinations.md) in CDP. If you plan to use a CDP destination, you can configure them directly when you [design a workflow](/docs/workflows/workflow-builder.md).

    ## Email

    Email is the default workflows channel in PostHog.

    You can use it to send **[drip campaigns](/docs/workflows/email-drip-campaign.md), transactional messages, or announcements** directly from the [workflow builder](/docs/workflows/workflow-builder.md).

    To configure the channel, you need to provide the following details:

    -   Enter your **from name** (e.g. `PostHog Team`).
    -   Enter your **from email** (e.g. `team@yourdomain.com`).

    This is the address that recipients will see in their inbox.

    To maximize deliverability and avoid spam folders, you must verify your domain.

    1.  After adding your email address, PostHog shows DNS records for **SPF** and **DKIM**.
    2.  Copy these into your domain host (e.g. Cloudflare, GoDaddy).
    3.  Verification may take a few minutes to propagate.

    Once verified, you'll see a green check mark in your settings.

    ![How to verify your domain in PostHog](https://res.cloudinary.com/dmukukwp6/image/upload/w_1000,c_limit,q_auto,f_auto/verified_email_light_c2f3b925c5.png)![How to verify your domain in PostHog](https://res.cloudinary.com/dmukukwp6/image/upload/w_1000,c_limit,q_auto,f_auto/verified_email_8fc6c512da.png)

    ## Slack

    A Slack connection enables you to deliver messages to a Slack channel.

    Starting in PostHog, you can add the PostHog Slack app to your workspace in [your project settings](https://app.posthog.com/settings/project#integration-slack).

    ![Allow PostHog Slack app permissions](https://res.cloudinary.com/dmukukwp6/image/upload/allow_slack_bb68272218.png)![Allow PostHog Slack app permissions](https://res.cloudinary.com/dmukukwp6/image/upload/allow_slack_bb68272218.png)

    The PostHog Slack app will require some basic permissions which you can grant by clicking the **Allow** button.

    Then, head to **Slack** and add PostHog to **specific Slack channels**. To do this:

    1.  In the Slack [channel header](https://slack.com/help/articles/360059928654-How-to-use-Slack--your-quick-start-guide#channels), click the top right menu and click **Open channel details**
    2.  Navigate to the **Integrations** tab
    3.  Click the **Add an app** button
    4.  Under **In your workspace**, click **PostHog**

    You can also try tagging the `@PostHog` bot in the channel to add it to the channel.

    ## Twilio

    Twilio enables you to send SMS messages to your users. To configure the channel, you need to provide the following details:

    | Field | Example | More info |
    | --- | --- | --- |
    | Account SID | AC5e66a2da9f32addea17ffe6d58891bf | [Twilio docs](https://help.twilio.com/articles/14726256820123-What-is-a-Twilio-Account-SID-and-where-can-I-find-it-) |
    | Auth Token | 4C2d86b28811*****111111111111111 | [Twilio docs](https://help.twilio.com/articles/223136027-Auth-Tokens-and-How-to-Change-Them) |

    Once configured, you'll be able to use the channel in a workflow to send SMS messages to your users.

2.  2

    ## Create a template

    Recommended

    If you plan to send email messages, you can create a template to reuse across your workflows. If you only plan to send Slack and SMS messages, you do not need to create a template.

    Navigate to **Workflows** > **Library** tab > click **New template**.

    -   Give your template a name.
    -   Write your subject line and body content (HTML and text versions are supported).
    -   Use variables like `{{ person.name }}` to personalize your message. See the [library](/docs/workflows/library.md) documentation for more information.

    Save your template — you'll be able to select it later when you design a workflow.

    You'll still be able to edit the message directly in the workflow builder.

3.  3

    ## Use in a workflow

    Required

    Once your channel is created, you can use it in a workflow to deliver messages to your users.

    [Launch your first workflow](/docs/workflows/launch-workflow.md)

4.  ## Troubleshooting

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