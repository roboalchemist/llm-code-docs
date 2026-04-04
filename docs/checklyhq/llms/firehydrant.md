# Source: https://checklyhq.com/docs/integrations/incident-management/firehydrant.md

> ## Documentation Index
> Fetch the complete documentation index at: https://checklyhq.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Send Alerts to FireHydrant

> Integrate with FireHydrant to create and resolve incidents from Checkly alerts

Checkly integrates with [FireHydrant](https://firehydrant.io/) to create and resolve incidents in your FireHydrant installation. More specifically, Checkly will:

* Alert you on Slack when a check fails, allowing you to create an incident on FireHydrant with one click.
* Close incidents automatically when a failing check recovers.

Assuming you already have [set up Slack on FireHydrant](https://support.firehydrant.io/hc/en-us/articles/360058203511), the integration can be configured as follows:

1. Log in to FireHydrant and navigate to `Integrations > Connected & available`, then select Checkly.

<img src="https://mintcdn.com/checkly-422f444a/0b4gCdAyz7Dv4O-Z/images/docs/images/integrations/firehydrant/firehydrant_step1.png?fit=max&auto=format&n=0b4gCdAyz7Dv4O-Z&q=85&s=569ca20d6827000578a7b2b6d095abdb" alt="firehydrant integration step 1" width="1552" height="957" data-path="images/docs/images/integrations/firehydrant/firehydrant_step1.png" />

2. Next, copy the generated URL to your clipboard.

<img src="https://mintcdn.com/checkly-422f444a/0b4gCdAyz7Dv4O-Z/images/docs/images/integrations/firehydrant/firehydrant_step2.png?fit=max&auto=format&n=0b4gCdAyz7Dv4O-Z&q=85&s=9e4f1cba918c574c69fc90044fb7d4f7" alt="firehydrant integration step 2" width="1552" height="957" data-path="images/docs/images/integrations/firehydrant/firehydrant_step2.png" />

3. Log in to Checkly and navigate to `Alert Settings`. Click the `Add more channels` button, find FireHydrant on the list, and click `Add channel`.

<img src="https://mintcdn.com/checkly-422f444a/0b4gCdAyz7Dv4O-Z/images/docs/images/integrations/firehydrant/firehydrant_step3.png?fit=max&auto=format&n=0b4gCdAyz7Dv4O-Z&q=85&s=fa3a1f31e61247a358ef220016846aef" alt="firehydrant integration step 3" width="3104" height="1786" data-path="images/docs/images/integrations/firehydrant/firehydrant_step3.png" />

4. Enter a name of your choosing for the alert channel, together with the URL you copied from FireHydrant. Make sure that the right checks are subscribing to the channel and that the `Send when` rules are correctly set, then hit `Save FireHydrant Webhook`.

<img src="https://mintcdn.com/checkly-422f444a/0b4gCdAyz7Dv4O-Z/images/docs/images/integrations/firehydrant/firehydrant_step4.png?fit=max&auto=format&n=0b4gCdAyz7Dv4O-Z&q=85&s=efa23d8211b4c9bba1c1cedeafd263ee" alt="firehydrant integration step 4" width="3104" height="1762" data-path="images/docs/images/integrations/firehydrant/firehydrant_step4.png" />

You are all set! Now, when a check fails, you will see an alert in your configured Slack channel:

<img src="https://mintcdn.com/checkly-422f444a/0b4gCdAyz7Dv4O-Z/images/docs/images/integrations/firehydrant/firehydrant_step5.png?fit=max&auto=format&n=0b4gCdAyz7Dv4O-Z&q=85&s=ce022485eb4356a197d96a1f932e35ce" alt="firehydrant integration step 5" width="1204" height="230" data-path="images/docs/images/integrations/firehydrant/firehydrant_step5.png" />

At this point, you can choose to either create an incident on FireHydrant or dismiss the alert. In case the related check recovers, the incident will be closed.

<img src="https://mintcdn.com/checkly-422f444a/0b4gCdAyz7Dv4O-Z/images/docs/images/integrations/firehydrant/firehydrant_step6.png?fit=max&auto=format&n=0b4gCdAyz7Dv4O-Z&q=85&s=3ddb04179d5883b547afcde3b9687aba" alt="firehydrant integration step 6" width="1342" height="357" data-path="images/docs/images/integrations/firehydrant/firehydrant_step6.png" />

Congratulations, you have successfully integrated Checkly with FireHydrant!


Built with [Mintlify](https://mintlify.com).