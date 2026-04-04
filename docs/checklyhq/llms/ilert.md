# Source: https://checklyhq.com/docs/integrations/incident-management/ilert.md

> ## Documentation Index
> Fetch the complete documentation index at: https://checklyhq.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Send Alerts to ilert

> Configure ilert integration to monitor incidents from Checkly alerts

Checkly integrates with [ilert](https://www.ilert.com/) to monitor your incidents in your ilert installation. Let's get started!

1. Log in to ilert and navigate to `Alert sources > Create a new alert source`.

<img src="https://mintcdn.com/checkly-422f444a/Shzx8VYv0RJK1Wbz/images/docs/images/integrations/ilert/ilert_step1.png?fit=max&auto=format&n=Shzx8VYv0RJK1Wbz&q=85&s=6d201cb048f6f862c0b92c96f21ce067" alt="ilert integration step 1" width="1068" height="288" data-path="images/docs/images/integrations/ilert/ilert_step1.png" />

2. Next, create a new alert source with Checkly as integration type.

<img src="https://mintcdn.com/checkly-422f444a/Shzx8VYv0RJK1Wbz/images/docs/images/integrations/ilert/ilert_step2.png?fit=max&auto=format&n=Shzx8VYv0RJK1Wbz&q=85&s=97abc2abb98ff1ca32ec409d6b4cf4b9" alt="ilert integration step 2" width="1000" height="645" data-path="images/docs/images/integrations/ilert/ilert_step2.png" />

3. Copy the generated API key to your clipboard.

<img src="https://mintcdn.com/checkly-422f444a/Shzx8VYv0RJK1Wbz/images/docs/images/integrations/ilert/ilert_step3.png?fit=max&auto=format&n=Shzx8VYv0RJK1Wbz&q=85&s=7515239f367f70d19466f78f1e72910b" alt="ilert integration step 3" width="907" height="590" data-path="images/docs/images/integrations/ilert/ilert_step3.png" />

4. Log in to Checkly and navigate to `Alert Settings`. Click the `Add more channels` button, find ilert icon on the list, and click `Add channel`.

<img src="https://mintcdn.com/checkly-422f444a/Shzx8VYv0RJK1Wbz/images/docs/images/integrations/ilert/ilert_step4.png?fit=max&auto=format&n=Shzx8VYv0RJK1Wbz&q=85&s=35dabd1ff3c22f1d2d813a0fe2ec2438" alt="ilert integration step 4" width="837" height="415" data-path="images/docs/images/integrations/ilert/ilert_step4.png" />

5. Enter a name of your choosing for the alert channel, together with the ilert URL and your API key (`https://api.ilert.com/api/v1/events/checkly/{api-key}`). Make sure that the right checks are subscribing to the channel and that the `Send when` rules are correctly set, then hit `Save ilert Webhook`.

<img src="https://mintcdn.com/checkly-422f444a/Shzx8VYv0RJK1Wbz/images/docs/images/integrations/ilert/ilert_step5.png?fit=max&auto=format&n=Shzx8VYv0RJK1Wbz&q=85&s=9b83cdcb270be91d4165155d841fe1b5" alt="ilert integration step 5" width="1384" height="597" data-path="images/docs/images/integrations/ilert/ilert_step5.png" />

Congratulations, you've successfully integrated Checkly with ilert!


Built with [Mintlify](https://mintlify.com).