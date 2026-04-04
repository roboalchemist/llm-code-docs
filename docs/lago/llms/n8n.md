# Source: https://getlago.com/docs/integrations/alerting/n8n.md

> ## Documentation Index
> Fetch the complete documentation index at: https://getlago.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# N8N

Here is a typical use case of using Lago and N8N to create powerful alerting automation.

## Overconsumption Alerting Example (with N8N)

When one of your customers is overconsuming during a period, you might need to warn her. This might happen for Cloud or API products. Automatic billing does not mean that your customers should have a bad surprise when opening their invoices.

Here is a full workflow to create an alerting system based on your customers' current usage, using [N8N](https://n8n.io/), a powerful automation tool for developers.

<Frame caption="N8N Alerting Workflow">
  <img src="https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/integrations/alerting/images/n8n-current-usage-ffe518dc30433d5f993f3cfb67a31374.png?fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=c075dfc7a1b578988ab22f5b41a7c08f" data-og-width="1582" width="1582" data-og-height="528" height="528" data-path="integrations/alerting/images/n8n-current-usage-ffe518dc30433d5f993f3cfb67a31374.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/integrations/alerting/images/n8n-current-usage-ffe518dc30433d5f993f3cfb67a31374.png?w=280&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=74d76664c50a70c238d522c9cad9139b 280w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/integrations/alerting/images/n8n-current-usage-ffe518dc30433d5f993f3cfb67a31374.png?w=560&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=9329f6cda847a075fe912913cbf778e3 560w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/integrations/alerting/images/n8n-current-usage-ffe518dc30433d5f993f3cfb67a31374.png?w=840&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=c08e0ec8cf515a9bac2b1fb5be0e5f75 840w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/integrations/alerting/images/n8n-current-usage-ffe518dc30433d5f993f3cfb67a31374.png?w=1100&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=31cd55e45420f473282428d0a6d6a2b0 1100w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/integrations/alerting/images/n8n-current-usage-ffe518dc30433d5f993f3cfb67a31374.png?w=1650&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=e32fba23b5b4317493eae03b617786e6 1650w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/integrations/alerting/images/n8n-current-usage-ffe518dc30433d5f993f3cfb67a31374.png?w=2500&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=995bd576481e1e95b302cb3dc23ccc16 2500w" />
</Frame>

In this example, we are going to build an alert anytime a usage threshold is overcome. Here is a summary of this workflow:

1. Use a **Cron** expression to call the Lago API every X minutes/hours/days
2. Call the [**Current usage**](/api-reference/customer-usage/get-current) endpoint available in Lago to fetch your customers' current usage;
3. Create a **IF statement** to condition the trigger (in our case, messages are triggered above a specific overconsumption); and
4. **Send a message** whenever this threshold is reached. You could use an emailing tool, Slack or a CRM. In our case, we are using Slack.

## 1st Node - CRON expression to repeat tasks at a defined interval

The first node is repeatedly and automatically triggering the automation at a defined interval.

1. Add a new **Node**;
2. Select **CRON** as a new application node;
3. The **Mode** is set to `Every X`; and
4. The **Value** is defined to `10` and the the **Units** to `minutes`.

This will trigger the flow automatically every 10 minutes. You can obviously change the value and the units to your preferred interval.

<Frame caption="Cron expression">
  <img src="https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/integrations/alerting/images/cron-alerting-a3cc55668cedb59003c788201dcfaf16.png?fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=5279fc885f85e09ba9a07c88cbe597bc" data-og-width="2426" width="2426" data-og-height="702" height="702" data-path="integrations/alerting/images/cron-alerting-a3cc55668cedb59003c788201dcfaf16.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/integrations/alerting/images/cron-alerting-a3cc55668cedb59003c788201dcfaf16.png?w=280&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=2680cdb7bb68938e278c35622cddf216 280w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/integrations/alerting/images/cron-alerting-a3cc55668cedb59003c788201dcfaf16.png?w=560&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=48c45b85b682de4b5f9fd8444a06c5fa 560w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/integrations/alerting/images/cron-alerting-a3cc55668cedb59003c788201dcfaf16.png?w=840&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=bb8e9b47a86fe3bdd744fe055072a306 840w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/integrations/alerting/images/cron-alerting-a3cc55668cedb59003c788201dcfaf16.png?w=1100&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=c57ae68d617017fb0d0b989fa1348ec1 1100w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/integrations/alerting/images/cron-alerting-a3cc55668cedb59003c788201dcfaf16.png?w=1650&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=c195d7f013b02637e1b2d38479e90523 1650w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/integrations/alerting/images/cron-alerting-a3cc55668cedb59003c788201dcfaf16.png?w=2500&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=3a03cf34fcb5700f652461b16d69e2ff 2500w" />
</Frame>

## 2nd Node - Catch customers' current usage with a HTTP Request

This node is used to fetch current usage from Lago API, using a HTTP request.

1. Add a new **Node**;
2. Select **HTTP Request** as a new application node;
3. Fetch [customers' current usage](/api-reference/customer-usage/get-current) from Lago API;
4. Make sure to set the `API_KEY` and the `Content-Type` as headers of your request; and
5. Execute the node to fetch the payload from Lago's API.

<Frame caption="Customer current usage">
  <img src="https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/integrations/alerting/images/current-usage-http-request-f534e90c3cc02f462a65c859218ac063.png?fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=3429e12a1edd5be24e332f9d7a9f40c1" data-og-width="2406" width="2406" data-og-height="812" height="812" data-path="integrations/alerting/images/current-usage-http-request-f534e90c3cc02f462a65c859218ac063.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/integrations/alerting/images/current-usage-http-request-f534e90c3cc02f462a65c859218ac063.png?w=280&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=b8bacb62dfef6a0c34e34766b211d859 280w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/integrations/alerting/images/current-usage-http-request-f534e90c3cc02f462a65c859218ac063.png?w=560&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=901f07bdab0e7c14e11e8279cfeaed1c 560w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/integrations/alerting/images/current-usage-http-request-f534e90c3cc02f462a65c859218ac063.png?w=840&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=df4df13e5d519291a01529667a116006 840w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/integrations/alerting/images/current-usage-http-request-f534e90c3cc02f462a65c859218ac063.png?w=1100&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=28d075975ac0bca3baefbd108dc5a3a8 1100w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/integrations/alerting/images/current-usage-http-request-f534e90c3cc02f462a65c859218ac063.png?w=1650&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=098a6dd7a0dbf90a6a324b66eaf225f5 1650w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/integrations/alerting/images/current-usage-http-request-f534e90c3cc02f462a65c859218ac063.png?w=2500&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=0cab870929dfd8ff8feacdee737ede3e 2500w" />
</Frame>

## 3rd Node - IF conditional statement to trigger messages under conditions

This node is used to trigger the alert only when your customers overcome a threshold of usage. Those limits depend on your product and your paying features.

In our present use case, we want to trigger an alert **when the total consumption of usage-based features overcomes \$200**. You could also use the `number of units` consumed or another useful value from the payload.

1. Add a new **Node**;
2. Select **IF** as a new application node;
3. Create a condition for the **TRUE** branch (when conditions are met);
4. The **Value** is the parameter of your condition (in our case the `amount_cents` of the current usage);
5. The **Operation** is the math operation you want to apply (in our case, condition is met when the total `amount_cents` is larger or equal to \$200);

It is important to mention that:

* You can add as many conditions as you need;
* You could add an action when the condition is `FALSE`.

<Frame caption="Customer current usage with if statement">
  <img src="https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/integrations/alerting/images/if-statement-current-usage-4186fee96e606f9554fa1bbcd6f07f5b.png?fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=4fba6213a0e749a27ec5143e3cb817c0" data-og-width="2418" width="2418" data-og-height="896" height="896" data-path="integrations/alerting/images/if-statement-current-usage-4186fee96e606f9554fa1bbcd6f07f5b.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/integrations/alerting/images/if-statement-current-usage-4186fee96e606f9554fa1bbcd6f07f5b.png?w=280&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=1d50416f9c9e87bb46ab48fa0cdd5581 280w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/integrations/alerting/images/if-statement-current-usage-4186fee96e606f9554fa1bbcd6f07f5b.png?w=560&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=07010fc773531a7ec41578b076f0f531 560w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/integrations/alerting/images/if-statement-current-usage-4186fee96e606f9554fa1bbcd6f07f5b.png?w=840&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=33b0361c338b3c69db679428fbfb8897 840w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/integrations/alerting/images/if-statement-current-usage-4186fee96e606f9554fa1bbcd6f07f5b.png?w=1100&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=1c26ad8ce29e061af8544e6dcbe75e8b 1100w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/integrations/alerting/images/if-statement-current-usage-4186fee96e606f9554fa1bbcd6f07f5b.png?w=1650&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=959cffe30ad5344a540ef8e4d7a3269e 1650w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/integrations/alerting/images/if-statement-current-usage-4186fee96e606f9554fa1bbcd6f07f5b.png?w=2500&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=3097e183ca0425840a713a32ab0abc34 2500w" />
</Frame>

## 4th Node - Send an alert message to Slack

This last node is used to trigger the message. In the example, we use a Slack channel, but you could even decide to send an email directly to your customers when they pass the limits of usage.

1. Add a new **Node**;
2. Select **Slack** as a new application node;
3. Select the targeted **Slack Account** & **Slack Channel**;
4. Choose the option to **POST** a **Message**; and
5. **Define a message** and use the variables of your payload to give context to your customers about their current usage.

<Tip>
  On top of connecting your Slack account, don't forget to authorize the application's bot to post messages to the targeted channel.
</Tip>

<Frame>
  <img src="https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/integrations/alerting/images/slack-alert-current-usage-247e699c94c1e5ec0f8adaac4b7abe8e.png?fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=0bbfbc9fbfac3cf33a0ddaa11479deca" data-og-width="2284" width="2284" data-og-height="1068" height="1068" data-path="integrations/alerting/images/slack-alert-current-usage-247e699c94c1e5ec0f8adaac4b7abe8e.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/integrations/alerting/images/slack-alert-current-usage-247e699c94c1e5ec0f8adaac4b7abe8e.png?w=280&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=38dfa4931998b7160a1c4a05066be0a1 280w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/integrations/alerting/images/slack-alert-current-usage-247e699c94c1e5ec0f8adaac4b7abe8e.png?w=560&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=caa867aecf5c207e5293ad7eacdbc504 560w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/integrations/alerting/images/slack-alert-current-usage-247e699c94c1e5ec0f8adaac4b7abe8e.png?w=840&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=7cc0ae21e81c0126628e3e31e0693c24 840w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/integrations/alerting/images/slack-alert-current-usage-247e699c94c1e5ec0f8adaac4b7abe8e.png?w=1100&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=130250de6b0215f8dd127716d4b10751 1100w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/integrations/alerting/images/slack-alert-current-usage-247e699c94c1e5ec0f8adaac4b7abe8e.png?w=1650&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=da354b01f0428d81a10d44a63c77d303 1650w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/integrations/alerting/images/slack-alert-current-usage-247e699c94c1e5ec0f8adaac4b7abe8e.png?w=2500&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=0aaf29263edaefaee2a9b5d8f4e4c73d 2500w" />
</Frame>

<Frame>
  <img src="https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/integrations/alerting/images/slack-alert-current-usage-message-dcd840bb5aa02098873410a83eb40776.png?fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=f96a9e7442e9c0962a05b5d7c4909d14" data-og-width="1802" width="1802" data-og-height="356" height="356" data-path="integrations/alerting/images/slack-alert-current-usage-message-dcd840bb5aa02098873410a83eb40776.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/integrations/alerting/images/slack-alert-current-usage-message-dcd840bb5aa02098873410a83eb40776.png?w=280&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=a03405795a8e5d24111e49c7fbc7e5ed 280w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/integrations/alerting/images/slack-alert-current-usage-message-dcd840bb5aa02098873410a83eb40776.png?w=560&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=96cbe0cf3434c061c018fadf4fb2d229 560w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/integrations/alerting/images/slack-alert-current-usage-message-dcd840bb5aa02098873410a83eb40776.png?w=840&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=4ef75ca9625920ddf6e3d6370b5e96ed 840w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/integrations/alerting/images/slack-alert-current-usage-message-dcd840bb5aa02098873410a83eb40776.png?w=1100&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=d71086acba592b5df51b628a05af663f 1100w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/integrations/alerting/images/slack-alert-current-usage-message-dcd840bb5aa02098873410a83eb40776.png?w=1650&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=8a375c62fc61dc1827dbeffb0af49105 1650w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/integrations/alerting/images/slack-alert-current-usage-message-dcd840bb5aa02098873410a83eb40776.png?w=2500&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=caade50850f12841db3507826c12c6ad 2500w" />
</Frame>
