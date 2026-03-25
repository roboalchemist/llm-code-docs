# Source: https://docs.axonius.com/docs/bamboohr-status-change.md

# BambooHR Status Change

You can create a webhook in BambooHR that monitors changes to user status. Each time a user's status changes, Bamboo HR webhook sends a webhook event to a webhook URL configured in Axonius.

**To configure BambooHR to send webhook events to Axonius:**

1. In Axonius: Navigate to **System Settings>External Integrations> Workflows Events**, and in the **Product** dropdown, select **BambooHR** to display the Axonius webhook URL.
2. In BambooHR: [Create a webhook in Bamboo HR that monitors changes to user status](https://help.bamboohr.com/s/article/787428#:~:text=To%20create%20a%20webhook,%20navigate,Webhook%20Name:%20Name%20the%20webhook), configure the following in the instructions:
   * In step 1: In **Webhook Name**, give the Webhook a meaningful name.

   * In step 2: From the **What fields do you want to monitor?** dropdown, select **Status** to monitor only the 'Status' field.

   * In step 5: In the **Post to URL** field, paste the Axonius Webhook URL that is displayed for BambooHR in the Axonius [**Webhook settings**](/docs/generic-webhook-events#/configuring-the-external-service). Click the Copy icon near the URL to copy it.

   * In step 6: In **Private Signature Key**, click **Generate Key** to create a signature key, and paste this key into the **Private Secure Key** field in the Axonius [**Workflows Events settings**](/docs/bamboohr-status-change). Axonius users can send the key to BambooHR to verify that the webhook came from BambooHR.

   * In step 7: In **When should the data be sent?**, specify when BambooHR should trigger the webhook and send it to the Axonius Webhook URL.
     * To send the webhook every time there is a change in status (chosen field), keep the configuration as shown in the screen in the BambooHR instructions (**Every** selected in **Hour**, **Minute**, **Day**, and **Month**).
     * To send the webhook at a specific time, select from the **Hour**, **Minute**, **Day**, and **Month** dropdowns the time and date to send it.