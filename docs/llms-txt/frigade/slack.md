# Source: https://docs.frigade.com/integrations/slack.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.frigade.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Slack

> Easily send messages to a Slack channel when users take actions in your Flows

<Steps>
  <Step title="Create a Slack Workflow">
    In Slack, open the Workflow page by searching for **Workflows** in the search bar and click the **Create a Workflow** button. Then, choose the **From a webhook** option:

    <img src="https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/slack/slack-1.png?fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=444b970032ad05b7f12e1732751e7b32" className="rounded" data-og-width="1527" width="1527" data-og-height="991" height="991" data-path="images/integrations/slack/slack-1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/slack/slack-1.png?w=280&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=d729bb593121dfc4f5a55df84be7d93b 280w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/slack/slack-1.png?w=560&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=8e9d4a579e3395c0b040078ac68d3efb 560w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/slack/slack-1.png?w=840&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=8529485aea7b994eae2c640c28620825 840w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/slack/slack-1.png?w=1100&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=96aa4f3920c1668218f234ca8a2406ae 1100w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/slack/slack-1.png?w=1650&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=b816132834b53d43cfc6819c70429699 1650w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/slack/slack-1.png?w=2500&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=6922ad09e7f333019d753bacad64c946 2500w" />
  </Step>

  <Step title="Create a webhook in Frigade">
    Copy the **Webhook request URL** from Slack. Then press **X**.

    <img src="https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/slack/slack-2.png?fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=4639bf93ecd7922928b3a16b12b2253e" className="rounded" data-og-width="1527" width="1527" data-og-height="991" height="991" data-path="images/integrations/slack/slack-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/slack/slack-2.png?w=280&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=7907ecbe0ed61f88636102ee1edc9c29 280w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/slack/slack-2.png?w=560&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=dc33ab6d9e8bc512e98a5d7c0ecbd152 560w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/slack/slack-2.png?w=840&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=92512e6bb215e55069b284c266b4764d 840w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/slack/slack-2.png?w=1100&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=8225c4a03a425504a36cab67d76a5aa4 1100w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/slack/slack-2.png?w=1650&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=08dc5dfaab9b41f0a92c589537cb7b85 1650w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/slack/slack-2.png?w=2500&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=352505861be56530fddf553e586861d2 2500w" />

    In the Frigade dashboard, navigate to the **Developer** section and click on **Webhooks**. Click the **New webhook** button and fill in the details as shown below with your Flow of choice. In this example, we use a simple [Form Flow](/component/form):

    <img src="https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/slack/slack-3.png?fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=764dd1db37fc89d5f4637c8d584d79de" className="rounded" data-og-width="1527" width="1527" data-og-height="989" height="989" data-path="images/integrations/slack/slack-3.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/slack/slack-3.png?w=280&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=8363b342921a539056096f0faed479a3 280w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/slack/slack-3.png?w=560&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=5e4feb5ce3796f9bc71038251e1ad162 560w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/slack/slack-3.png?w=840&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=859aa2f1d252e3c4140de770ac2bb920 840w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/slack/slack-3.png?w=1100&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=54a3d0ae0dfb1c937a7c39d80bb157cb 1100w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/slack/slack-3.png?w=1650&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=ec00b9b7b05f2e24fd9fca4a0c9c4489 1650w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/slack/slack-3.png?w=2500&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=b3dd1a3b1df2d4b4b05a665d83ca7011 2500w" />

    <Tip>You can use a free service such as [Webhook.site](https://webhook.site/) to test your webhook.</Tip>
  </Step>

  <Step title="Set up data variables in Slack">
    In the Slack Workflow, click the **Starts with a webhook** card at the top and add the variables you'd like to send in your Slack message as seen below:

    <img src="https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/slack/slack-4.png?fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=98dec1e271f438a948e44e1fe2041430" className="rounded" data-og-width="1527" width="1527" data-og-height="991" height="991" data-path="images/integrations/slack/slack-4.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/slack/slack-4.png?w=280&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=88fc089d9017f45f8b962ef6e53687bc 280w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/slack/slack-4.png?w=560&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=80b4350bf3afaaf3843a38511f3029f5 560w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/slack/slack-4.png?w=840&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=293ee4c14eb31a124502fa91e3483fd6 840w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/slack/slack-4.png?w=1100&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=54588c4adc5febd042221c99bdae923b 1100w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/slack/slack-4.png?w=1650&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=98b5ce32b4df544de7ff49310a18c1c2 1650w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/slack/slack-4.png?w=2500&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=b78056f6181ad0292d848ecf04519d2b 2500w" />

    By default Frigade sends `user__email` and `user__name` for the given user if the data has been [provided in the SDK](/sdk/hooks/user). In this case, we also want to send the value of the `message` field from the Form Flow. To do this, we add a new variable `data__data__message` to map it to the field. You can target any field in a Frigade Form by prefixing the variable name with `data__data__`.
    <Tip>Select and radio form inputs will include both the label and the value in the webhook.  Therefore, if your field is named `industry` you should use `data__data__industry__label` to get the label or `data__data__industry__value` to get the value.</Tip>
  </Step>

  <Step title="Send a message to a Slack channel">
    Add a new step to the Slack Workflow by clicking the **Messages** link in the right menu. Then pick your channel of choice and add the variables you'd like to send in your Slack message as seen below:

    <img src="https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/slack/slack-5.png?fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=45412088fcf18852d58fd4db68a191f8" className="rounded" data-og-width="1395" width="1395" data-og-height="928" height="928" data-path="images/integrations/slack/slack-5.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/slack/slack-5.png?w=280&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=f3bd76dc02e793a179e7b3ca73dbb15e 280w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/slack/slack-5.png?w=560&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=3bb825b8427d71b0e2c370ea892f05f1 560w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/slack/slack-5.png?w=840&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=4d57412dd190836ceb6395822386fe4b 840w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/slack/slack-5.png?w=1100&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=b4a4b3ef72c79f18509f0eebcf51d941 1100w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/slack/slack-5.png?w=1650&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=01cd392315bb5ce28b4a09793a2b6cf0 1650w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/slack/slack-5.png?w=2500&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=e59a6a63c56900cc57608c534538dbfb 2500w" />

    Finally, hit the **Publish** button in the top right corner to make your Slack Workflow live.
  </Step>

  <Step title="Test your Slack integration">
    You're now all set to test your Slack integration. In your application, complete the Flow you've set up the webhook for. In this case, we'll submit the Form Flow:

    <img src="https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/slack/slack-6.png?fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=e0321d0946bd2e98db4bdef6501e2ed7" className="rounded" data-og-width="1527" width="1527" data-og-height="989" height="989" data-path="images/integrations/slack/slack-6.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/slack/slack-6.png?w=280&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=d01c65a5d3b5149f275eb00589041147 280w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/slack/slack-6.png?w=560&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=3fe983e115c0ceca3a1b84b848078b70 560w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/slack/slack-6.png?w=840&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=b2cc8317d0d3bf064b35131ce39cb309 840w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/slack/slack-6.png?w=1100&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=fd0fd635b1e95f4ae35b2d55cab88411 1100w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/slack/slack-6.png?w=1650&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=6141cde5fca85748b9d071df692b8b14 1650w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/slack/slack-6.png?w=2500&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=d51b2c9843f55174f84d2e4557760a12 2500w" />

    After completing a step in the Frigade Flow, you should now see the following show up in your Slack channel:

    <img src="https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/slack/slack-7.png?fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=20a317d919e06793f1185fdbdc75ab55" className="rounded" data-og-width="1396" width="1396" data-og-height="926" height="926" data-path="images/integrations/slack/slack-7.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/slack/slack-7.png?w=280&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=fcf51fb4276ec45379126976516003c9 280w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/slack/slack-7.png?w=560&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=5ac7ae9f4b728a491a8930645e62d7a8 560w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/slack/slack-7.png?w=840&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=52238002dc08e042d3ea9aeadcbc34c5 840w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/slack/slack-7.png?w=1100&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=636685666c2a5366d19a30f58cd3ab42 1100w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/slack/slack-7.png?w=1650&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=4f4e2632fd2a35995ede4d949af19f13 1650w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/slack/slack-7.png?w=2500&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=650491572d525b4f85cf63cf75a14193 2500w" />
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
