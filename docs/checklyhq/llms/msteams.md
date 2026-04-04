# Source: https://checklyhq.com/docs/integrations/alerts/msteams.md

> ## Documentation Index
> Fetch the complete documentation index at: https://checklyhq.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Send Alerts to Microsoft Teams

> Configure Microsoft Teams integration to receive failure, degradation, and recovery messages from Checkly

<Tip>
  **Monitoring as Code**: Learn more about the [MS Teams Alert Channel Construct](/constructs/msteams-alert-channel).
</Tip>

Checkly integrates with [Microsoft Teams](https://www.microsoft.com/en/microsoft-365/microsoft-teams/free) and can
deliver failure, degradation, and recovery messages to any channel in any team. You can add as many Teams channels as you wish.
To enable the MS Teams alert channel, take the following steps:

1. First, create a **Workflow**. Log in to your MS Teams account, go to Apps and search for *workflows*.

   <img src="https://mintcdn.com/checkly-422f444a/Shzx8VYv0RJK1Wbz/images/docs/images/integrations/msteams/msteams_step1.png?fit=max&auto=format&n=Shzx8VYv0RJK1Wbz&q=85&s=4450968a2c5b98e1e1b4480042b9c4e9" alt="setup checkly msteams_integration step 1" width="1134" height="709" data-path="images/docs/images/integrations/msteams/msteams_step1.png" />

2. Open the *Workflows* app, go to *Create* and select the **Post to a channel when a webhook request is received** template, name your workflow, and press "Next".

   <img src="https://mintcdn.com/checkly-422f444a/Shzx8VYv0RJK1Wbz/images/docs/images/integrations/msteams/msteams_step2.png?fit=max&auto=format&n=Shzx8VYv0RJK1Wbz&q=85&s=61162404c079f534a89d7a078bff56ce" alt="setup checkly msteams integration step 2" width="1341" height="868" data-path="images/docs/images/integrations/msteams/msteams_step2.png" />

3. Select which *Team* and *Channel* the integration should post alert notifications to, then press "Create flow".

   <img src="https://mintcdn.com/checkly-422f444a/Shzx8VYv0RJK1Wbz/images/docs/images/integrations/msteams/msteams_step3.png?fit=max&auto=format&n=Shzx8VYv0RJK1Wbz&q=85&s=feb85abbb47d14352b2445883102fc84" alt="setup checkly msteams integration step 3" width="1341" height="868" data-path="images/docs/images/integrations/msteams/msteams_step3.png" />

4. **Copy the displayed URL**. Then close the workflow setup by clicking "Done".

<img src="https://mintcdn.com/checkly-422f444a/Shzx8VYv0RJK1Wbz/images/docs/images/integrations/msteams/msteams_step4.png?fit=max&auto=format&n=Shzx8VYv0RJK1Wbz&q=85&s=9ab4bbb239f8e25cb3d8e5e112698afd" alt="setup checkly msteams integration step 4" width="1341" height="868" data-path="images/docs/images/integrations/msteams/msteams_step4.png" />

5. Log in to Checkly and navigate to [Alert Settings](https://app.checklyhq.com/alert-settings/).
   Click the "Add more channels" button, find MS Teams on the list, and click "Add channel".

   <img src="https://mintcdn.com/checkly-422f444a/Shzx8VYv0RJK1Wbz/images/docs/images/integrations/msteams/msteams_step5.png?fit=max&auto=format&n=Shzx8VYv0RJK1Wbz&q=85&s=e840e3d8e4c651ab47e5692b0d5781b5" alt="setup checkly msteams integration step 5" width="1419" height="806" data-path="images/docs/images/integrations/msteams/msteams_step5.png" />

6. Give the alert channel a name and **paste the URL** in the dedicated URL input field. You can now also tweak
   which alerts you want to be notified of and which checks or check groups should be subscribed to this channel.

   <img src="https://mintcdn.com/checkly-422f444a/Shzx8VYv0RJK1Wbz/images/docs/images/integrations/msteams/msteams_step6.png?fit=max&auto=format&n=Shzx8VYv0RJK1Wbz&q=85&s=d6abb4d2258873b6735ba72735bc66d3" alt="setup checkly msteams integration step 6" width="1419" height="998" data-path="images/docs/images/integrations/msteams/msteams_step6.png" />

7. Save your alert channel. The next time checks subscribed to this channel triggers an alert, the integration will post a message to the configured Channel.
   Below is an example of an alert message using the default configuration.

   <img src="https://mintcdn.com/checkly-422f444a/Shzx8VYv0RJK1Wbz/images/docs/images/integrations/msteams/msteams_step7.png?fit=max&auto=format&n=Shzx8VYv0RJK1Wbz&q=85&s=d91734306ebbbefe26a486a5a1f725f1" alt="checkly msteams integration example" width="1181" height="728" data-path="images/docs/images/integrations/msteams/msteams_step7.png" />

   > Note that we provide a preconfigured message payload but you are free to edit the payload and add more or different
   > variables. Just click the "Edit payload" button and reference the "Help & variables tab".

Congratulations! You have successfully integrated Checkly with Microsoft Teams!


Built with [Mintlify](https://mintlify.com).