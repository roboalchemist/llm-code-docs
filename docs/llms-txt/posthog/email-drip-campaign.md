# Source: https://posthog.com/docs/workflows/email-drip-campaign.md

# Set up an email drip campaign - Docs

In this guide we'll walk through creating a simple **drip campaign**. After following this guide, you will:

-   Send a welcome email when a user signs up
-   Follow up 1 day later if they haven't completed onboarding

1.  1

    ## Create a workflow

    Required

    Go to [Workflows](https://app.posthog.com/workflows) and click the **\+ New workflow button**.

    ![Click the New Workflow button](https://res.cloudinary.com/dmukukwp6/image/upload/w_1600,c_limit,q_auto,f_auto/messaging_new_campaign_light_c1f7b79b46.png)![Click the New Workflow button](https://res.cloudinary.com/dmukukwp6/image/upload/w_1600,c_limit,q_auto,f_auto/messaging_new_campaign_dark_6a4ea06e58.png)

    This will open the workflow builder.

    The new workflow only has two blocks:

    -   A trigger block: This defines the event that will start the workflow.
    -   An exit block: This defines the event that will end the workflow.

    ![Fresh workflow with trigger block](https://res.cloudinary.com/dmukukwp6/image/upload/w_1600,c_limit,q_auto,f_auto/new_campaign_light_acfabde4ca.png)![Fresh workflow with trigger block](https://res.cloudinary.com/dmukukwp6/image/upload/w_1600,c_limit,q_auto,f_auto/new_campaign_dark_8ed34dd06e.png)

    The trigger block has a little exclamation mark. This means it is not configured. In general, if there are problems with a block, it will have a little exclamation mark.

2.  2

    ## Set the trigger

    Required

    Now, let's click on the trigger block and configure it. In a new workflow, the trigger doesn't have any default trigger events. Triggers tell PostHog what events will start the workflow.

    Change the frequency drop down to `"One time"` this means a user will only go through this workflow once, and cannot be re-enrolled.

    ![Trigger warning that event is required](https://res.cloudinary.com/dmukukwp6/image/upload/q_auto,f_auto/frequency_trigger_ff50a0016d.png)![Trigger warning that event is required](https://res.cloudinary.com/dmukukwp6/image/upload/q_auto,f_auto/frequency_trigger_ff50a0016d.png)

    Click the **\+ Add trigger event** button and search for the event you want to use as the trigger.

    Search for your the signup event you capture with PostHog SDKs, (e.g. `user signed up`) and click it. This tells the workflow to start when this event is captured:

    ![Trigger event configuration](https://res.cloudinary.com/dmukukwp6/image/upload/c_crop,g_north,h_0.9,w_1.0/w_1600,c_limit,q_auto,f_auto/messaging_new_campaign_event_select_light_a08c890a53.png)![Trigger event configuration](https://res.cloudinary.com/dmukukwp6/image/upload/c_crop,g_north,h_0.9,w_1.0/w_1600,c_limit,q_auto,f_auto/messaging_new_campaign_event_select_dark_be58972ba1.png)

    Don't worry about the conversion goal or exit conditions for now, and exit this step by clicking on the back arrow in the sidepanel - this is how you will exit any step after configuring it.

    ![Back arrow in sidepanel](https://res.cloudinary.com/dmukukwp6/image/upload/c_crop,h_0.3,w_0.4,x_0.25,y_0.13/messaging_new_campaign_event_select_light_a08c890a53.png)![Back arrow in sidepanel](https://res.cloudinary.com/dmukukwp6/image/upload/c_crop,h_0.3,w_0.4,x_0.25,y_0.13/w_1600,c_limit,q_auto,f_auto/messaging_new_campaign_event_select_dark_be58972ba1.png)

3.  3

    ## Send the first email

    Required

    Drag an **Email** dispatch beneath the trigger, into the workflow like this:

    ![Dragging email dispatch](https://res.cloudinary.com/dmukukwp6/image/upload/w_1600,c_limit,q_auto,f_auto/new_email_light_98795f1414.png)![Dragging email dispatch](https://res.cloudinary.com/dmukukwp6/image/upload/w_1600,c_limit,q_auto,f_auto/new_email_dark_e2811207c7.png)

    Then, click on the email block to configure it. Set the **subject line** and **sender**.

    ![Configure email template](https://res.cloudinary.com/dmukukwp6/image/upload/w_1600,c_limit,q_auto,f_auto/configure_email_template_light_ed7a551fec.png)![Configure email template](https://res.cloudinary.com/dmukukwp6/image/upload/w_1600,c_limit,q_auto,f_auto/configure_email_template_dark_a58f62c95f.png)

    > If you haven't configured an email channel yet, you will need to do that first.
    >
    > [Configure an email channel](/docs/workflows/configure-channels.md)

    And also select your welcome email template or create a new one, and then click out.

    ![Email template selection](https://res.cloudinary.com/dmukukwp6/image/upload/w_1600,c_limit,q_auto,f_auto/email_template_editor_811f405d88.png)![Email template selection](https://res.cloudinary.com/dmukukwp6/image/upload/w_1600,c_limit,q_auto,f_auto/email_template_editor_dark_24acb77e74.png)

4.  4

    ## Wait until condition branch

    Required

    This is where things get interesting. We will want to send a follow up email **only** to those users who have `not completed onboarding`. We can achieve this with a `wait until condition` step.

    After the email, add a **Wait until Condition**.

    ![Adding wait until condition](https://res.cloudinary.com/dmukukwp6/image/upload/w_1600,c_limit,q_auto,f_auto/us_posthog_com_project_198052_messaging_campaigns_new_workflow_mode_build_and_node_action_wait_until_condition_bf71d044_c8e3_439f_88ed_39144053dc6c_11e113cc7a.png)![Adding wait until condition](https://res.cloudinary.com/dmukukwp6/image/upload/w_1600,c_limit,q_auto,f_auto/us_posthog_com_project_198052_messaging_campaigns_new_workflow_mode_build_and_node_action_wait_until_condition_bf71d044_c8e3_439f_88ed_39144053dc6c_1_0b01bed325.png)

    In the **wait until condition** block, you can configure the following:

    -   **Wait time**: The time to wait for the condition to be met. For this example, we'll wait 1 day.
    -   **Conditions to wait for**: The condition to wait for. For this example, we'll wait for the person property `onboarding_completed` to be set to `true`. This can be a [person property](/docs/product-analytics/person-properties.md) set on users after they complete onboarding.

    Click **Create** to create the wait until condition.

5.  5

    ## Add follow up email

    Required

    For users who haven't completed onboarding after the wait period, we'll send a follow-up email. Drag an email dispatch to the `no match` branch of the `wait until condition`.

    ![Adding follow up email](https://res.cloudinary.com/dmukukwp6/image/upload/w_1600,c_limit,q_auto,f_auto/add_condition_email_light_e9e592cb19.png)![Adding follow up email](https://res.cloudinary.com/dmukukwp6/image/upload/w_1600,c_limit,q_auto,f_auto/add_condition_email_dark_0b6917818c.png)

    Configure this email with content encouraging them to complete onboarding. Some tips:

    -   Keep it short and focused
    -   Include a clear call-to-action
    -   Highlight the value they'll get from completing onboarding
    -   Consider offering help or support

    The workflow will now:

    -   Exit if their person property `first_onboarding_complete` is set to `true` (they've completed onboarding)
    -   Send the follow-up email if they have not completed onboarding after the wait period

6.  6

    ## Review and launch

    Required

    Now the complete workflow should look like this:

    ![Complete drip campaign workflow](https://res.cloudinary.com/dmukukwp6/image/upload/w_2000,c_limit,q_auto,f_auto/email_drip_overview_light_a84567a8f9.png)![Complete drip campaign workflow](https://res.cloudinary.com/dmukukwp6/image/upload/w_2000,c_limit,q_auto,f_auto/email_drip_overview_dark_2bb57406d6.png)

    Click **Create** to publish the workflow.

7.  7

    ## Enable the workflow

    Required

    Once you have confirmed the workflow works as expected, you can enable it by clicking the **Enable** button at the top right of the workflow builder.

    Your new users will now automatically receive this email drip campaign to help guide them through onboarding.

### Community questions

Ask a question

### Was this page useful?

HelpfulCould be better