# Source: https://checklyhq.com/docs/integrations/incident-management/splunk-on-call.md

> ## Documentation Index
> Fetch the complete documentation index at: https://checklyhq.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Send Alerts via Splunk On-Call

> Configure Splunk On-Call integration to receive real-time alerts from Checkly monitors

Checkly integrates with [Splunk On-Call](https://www.splunk.com/en_us/software/splunk-on-call.html) (formerly VictorOps) and can
deliver failure, degradation, and recovery messages to any routing key in any team. More specifically, Checkly will:

* Open new alerts when a check fails.
* Close alerts automatically when a failing check recovers.
* Alert when SSL certificates are about to expire.

1. First, create an **REST integration endpoint**. Log in to your Splunk On-Call account, go to "Integrations" and search for the *REST generic* integration.

   <img src="https://mintcdn.com/checkly-422f444a/Shzx8VYv0RJK1Wbz/images/docs/images/integrations/splunk/splunk_step1.png?fit=max&auto=format&n=Shzx8VYv0RJK1Wbz&q=85&s=3932c8a3557c3e3db3228477377404da" alt="setup checkly splunk_integration step 1" width="1019" height="736" data-path="images/docs/images/integrations/splunk/splunk_step1.png" />

2. Add the **REST generic** integration and click "Enable Integration" on the next screen. Now **copy the URL**.

   <img src="https://mintcdn.com/checkly-422f444a/Shzx8VYv0RJK1Wbz/images/docs/images/integrations/splunk/splunk_step2.png?fit=max&auto=format&n=Shzx8VYv0RJK1Wbz&q=85&s=10ceaa66c914b07d6a7196c8f0ae9f4c" alt="setup checkly splunk integration step 2" width="1019" height="736" data-path="images/docs/images/integrations/splunk/splunk_step2.png" />

   <Callout type="note">
     Notice that you need to **append a routing key**. This should be the routing key you associated with a group e.g. "database" or "product team"
     For more details, [see the Splunk  / VictorOps knowledge base](https://help.victorops.com/knowledge-base/routing-keys/)
   </Callout>

3. Log in to Checkly and navigate to [Alert Settings](https://app.checklyhq.com/alert-settings/).
   Click the "Add more channels" button, find Splunk On-Call on the list, and click "Add channel".

   <img src="https://mintcdn.com/checkly-422f444a/Shzx8VYv0RJK1Wbz/images/docs/images/integrations/splunk/splunk_step3.png?fit=max&auto=format&n=Shzx8VYv0RJK1Wbz&q=85&s=c3c9fd89f8be729dfecddb6ab327af4a" alt="setup checkly splunk integration step 3" width="1085" height="728" data-path="images/docs/images/integrations/splunk/splunk_step3.png" />

4. Give the alert channel a name and **paste the URL** in the dedicated URL input field. You can now also tweak
   which alerts you want to be notified of and which checks or check groups should be subscribed to this channel.

   <img src="https://mintcdn.com/checkly-422f444a/Shzx8VYv0RJK1Wbz/images/docs/images/integrations/splunk/splunk_step4.png?fit=max&auto=format&n=Shzx8VYv0RJK1Wbz&q=85&s=9f11aeb55cf394d4fe5e77a59c943a3e" alt="setup checkly splunk integration step 4" width="1019" height="694" data-path="images/docs/images/integrations/splunk/splunk_step4.png" />

   <Callout type="note">
     Note that we provide a preconfigured message payload but you are free to edit the payload and add more or different
     variables. Just click the "Edit payload" button and reference the "Help & variables tab".
   </Callout>

Congratulations! You have successfully integrated Checkly with Splunk On-Call!


Built with [Mintlify](https://mintlify.com).