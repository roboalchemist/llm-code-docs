# Source: https://getlago.com/docs/integrations/alerting/zapier.md

# Zapier

Here is a typical use case of using Lago with Zapier to create powerful alerting automation.

## Invoice Alerting Example (with Zapier)

<Frame caption="invoice alerting flow">
  <img src="https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/integrations/alerting/images/invoice-alerting-flow-6c86d0faab38b7740a20925797099c70.png?fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=2292b4e46ab092c55ac33931ddcb2e9d" data-og-width="1444" width="1444" data-og-height="322" height="322" data-path="integrations/alerting/images/invoice-alerting-flow-6c86d0faab38b7740a20925797099c70.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/integrations/alerting/images/invoice-alerting-flow-6c86d0faab38b7740a20925797099c70.png?w=280&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=8d95d7de801293bcaebbcfcd7c91a293 280w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/integrations/alerting/images/invoice-alerting-flow-6c86d0faab38b7740a20925797099c70.png?w=560&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=4282d0c23f3aac4b6a947a3e3e5f0fce 560w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/integrations/alerting/images/invoice-alerting-flow-6c86d0faab38b7740a20925797099c70.png?w=840&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=8e2eb4032f711e78203b3f30a56a1af1 840w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/integrations/alerting/images/invoice-alerting-flow-6c86d0faab38b7740a20925797099c70.png?w=1100&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=6b0cd395b585ef50d1eaefa45c22a75e 1100w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/integrations/alerting/images/invoice-alerting-flow-6c86d0faab38b7740a20925797099c70.png?w=1650&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=bc2d83ef1c0be803b4ba6e020da409aa 1650w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/integrations/alerting/images/invoice-alerting-flow-6c86d0faab38b7740a20925797099c70.png?w=2500&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=f59de6d8e51dfe175d000bd2c0eb1444 2500w" />
</Frame>

In this example, we are going to **build an alert anytime a new invoice is emitted**. To create this workflow, we are using:

1. Lago's webhook when a new invoice is emitted;
2. Zapier as an automation tool, to catch, tranform and send the data; and
3. Slack as the "receiver" to alert your team anytime a new invoice is created.

<Frame caption="Zapier alerting flow">
  <img src="https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/integrations/alerting/images/zapier-flow-invoice-alerting-6916f7acabd57ddc10125d0fe1b9f7e1.png?fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=a69497e86c4674d4d766d15c26b74344" data-og-width="1800" width="1800" data-og-height="744" height="744" data-path="integrations/alerting/images/zapier-flow-invoice-alerting-6916f7acabd57ddc10125d0fe1b9f7e1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/integrations/alerting/images/zapier-flow-invoice-alerting-6916f7acabd57ddc10125d0fe1b9f7e1.png?w=280&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=8a1c45bf6f18ca725d6e7cf2c896f6d5 280w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/integrations/alerting/images/zapier-flow-invoice-alerting-6916f7acabd57ddc10125d0fe1b9f7e1.png?w=560&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=99eef254cf2ed016cf2f2cb184428d13 560w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/integrations/alerting/images/zapier-flow-invoice-alerting-6916f7acabd57ddc10125d0fe1b9f7e1.png?w=840&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=de7cb23b05c1a295e41f19510a91c608 840w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/integrations/alerting/images/zapier-flow-invoice-alerting-6916f7acabd57ddc10125d0fe1b9f7e1.png?w=1100&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=f485a3e31e1f7d1c05f6fa9cbf916757 1100w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/integrations/alerting/images/zapier-flow-invoice-alerting-6916f7acabd57ddc10125d0fe1b9f7e1.png?w=1650&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=1dc0ba1299f8a1b02ce938c44badf2f5 1650w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/integrations/alerting/images/zapier-flow-invoice-alerting-6916f7acabd57ddc10125d0fe1b9f7e1.png?w=2500&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=4d2d2392c478706a83961eec129cec67 2500w" />
</Frame>

## 1. Catch a webhook when a new invoice is emitted

Lago automatically creates an invoice when a billable period is over. The invoice's payload gives you a detailed view of what has been invoiced. The first action we need to perform is to catch this invoice with a webhook:

1. In Zapier, create a new Zap;
2. Use the **Webhooks by Zapier** as the trigger of this Zap;
3. Select the **Catch Raw Hook** event trigger;
4. Copy the Zapier Webhook URL and paste it in Lago (**Developers** > **Webhooks** > **Add a webhook**); and
5. Catch your first webhook when an invoice is emitted (whenever you assign an add-on or a subscription).

## 2. Run a script to transform the webhook

In Zapier, create a second action by clicking the `+` icon. This new event action is used to format the webhook with a breakdown of fields that can be used in a message.

1. Select **Code by Zapier** as a new *Event Action*;
2. Click on **Javascript** as the event code language to run;
3. Create a field called `payload`. The value of this field is the full **Raw body** of your invoice object received);
4. Run the script (code snippet below) in the **Code** section;
5. Test the action. If valid, it returns a breakdown of fields.

```javascript  theme={"dark"}
var obj = JSON.parse(inputData.payload);

if(obj.object_type == "invoice"){
  return obj
}
```

<Frame caption="Script to tranform the invoice payload">
  <img src="https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/integrations/alerting/images/script-invoice-alerting-ad7c8393f51e76b0601c2e153b1ee1dc.png?fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=c5cb0c77f8d0a9ffc70fb8f7a7bba54b" data-og-width="1804" width="1804" data-og-height="1290" height="1290" data-path="integrations/alerting/images/script-invoice-alerting-ad7c8393f51e76b0601c2e153b1ee1dc.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/integrations/alerting/images/script-invoice-alerting-ad7c8393f51e76b0601c2e153b1ee1dc.png?w=280&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=656486dca10c29c272c21d7ae1f095c8 280w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/integrations/alerting/images/script-invoice-alerting-ad7c8393f51e76b0601c2e153b1ee1dc.png?w=560&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=2a6f59f425b1d3ac3be94805a34925ad 560w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/integrations/alerting/images/script-invoice-alerting-ad7c8393f51e76b0601c2e153b1ee1dc.png?w=840&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=0c8604fd8a326f5875af1b1c6219fac2 840w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/integrations/alerting/images/script-invoice-alerting-ad7c8393f51e76b0601c2e153b1ee1dc.png?w=1100&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=1bb050918cb2954bf6b2eaf51193521b 1100w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/integrations/alerting/images/script-invoice-alerting-ad7c8393f51e76b0601c2e153b1ee1dc.png?w=1650&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=8c77add28a1a2dfde21bd1b7d8253d06 1650w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/integrations/alerting/images/script-invoice-alerting-ad7c8393f51e76b0601c2e153b1ee1dc.png?w=2500&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=e050b195ef28d452df44791242c6843b 2500w" />
</Frame>

<Frame caption="Breakdown of the invoice payload">
  <img src="https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/integrations/alerting/images/alerting-fields-breakdown-33a58492027cdcbfe5562d1c1cd96397.png?fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=92c1b4cecc269f70f8cb1a8275ad06d6" data-og-width="1806" width="1806" data-og-height="1320" height="1320" data-path="integrations/alerting/images/alerting-fields-breakdown-33a58492027cdcbfe5562d1c1cd96397.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/integrations/alerting/images/alerting-fields-breakdown-33a58492027cdcbfe5562d1c1cd96397.png?w=280&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=c12afa94b745ab51d273fc4ae25984aa 280w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/integrations/alerting/images/alerting-fields-breakdown-33a58492027cdcbfe5562d1c1cd96397.png?w=560&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=9859c3c388fa171fab112ee9a5fae2c0 560w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/integrations/alerting/images/alerting-fields-breakdown-33a58492027cdcbfe5562d1c1cd96397.png?w=840&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=a81e03150612c42648359c20744ba11a 840w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/integrations/alerting/images/alerting-fields-breakdown-33a58492027cdcbfe5562d1c1cd96397.png?w=1100&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=14e8f2d4d99c94925aed8d806118b1e3 1100w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/integrations/alerting/images/alerting-fields-breakdown-33a58492027cdcbfe5562d1c1cd96397.png?w=1650&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=a3c72da2764137d5fc832b87abed4c8e 1650w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/integrations/alerting/images/alerting-fields-breakdown-33a58492027cdcbfe5562d1c1cd96397.png?w=2500&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=a7fd5bc042e0790845e0096986c33da5 2500w" />
</Frame>

## 3. Send a message to a Slack Channel

Once you catch the breakdown of fields returned by the invoice payload, you can easily use them to create a Slack text message.

In Zapier, create a third action by clicking the `+` icon. This new event action is used to send a message to Slack by using the fields of the invoice payload.

1. Select **Slack** as a new app action;
2. Select the **Send Channel Message** action;
3. Choose the targeted **Slack Account**;
4. Choose the targeted **Slack Channel**; and
5. Create a message by using the fields returned by the payload.

By testing and validating the entire Zap, a Slack message is sent anytime a new invoice is emitted by Lago. You can use the same message example as detailed below:

<Frame caption="Breakdown of the invoice payload">
  <img src="https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/integrations/alerting/images/slack-message-example-228799226dec5760962b69c5e7816daf.png?fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=83344caf2ba61cf3d4bc493f2a884a42" data-og-width="1804" width="1804" data-og-height="884" height="884" data-path="integrations/alerting/images/slack-message-example-228799226dec5760962b69c5e7816daf.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/integrations/alerting/images/slack-message-example-228799226dec5760962b69c5e7816daf.png?w=280&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=2757c149db8963ec19ee64cab0370f7d 280w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/integrations/alerting/images/slack-message-example-228799226dec5760962b69c5e7816daf.png?w=560&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=7cd7e76f7a5bdfabe268130734ac01b4 560w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/integrations/alerting/images/slack-message-example-228799226dec5760962b69c5e7816daf.png?w=840&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=be578f1e1015427c2da44599ca184118 840w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/integrations/alerting/images/slack-message-example-228799226dec5760962b69c5e7816daf.png?w=1100&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=cc427430d954421d07024bda054ee4d2 1100w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/integrations/alerting/images/slack-message-example-228799226dec5760962b69c5e7816daf.png?w=1650&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=4ecf899381430f8d656641d541bf7ff3 1650w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/integrations/alerting/images/slack-message-example-228799226dec5760962b69c5e7816daf.png?w=2500&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=0dd69631542042529189ce39e7a55c09 2500w" />
</Frame>

<Frame caption="Slack text message">
  <img src="https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/integrations/alerting/images/slack-test-message-alerting-f3d6a83c9a3468528ebc31d9e57c1a47.png?fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=9c5819bd2c6843587f1509d0a35b1301" data-og-width="1644" width="1644" data-og-height="286" height="286" data-path="integrations/alerting/images/slack-test-message-alerting-f3d6a83c9a3468528ebc31d9e57c1a47.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/integrations/alerting/images/slack-test-message-alerting-f3d6a83c9a3468528ebc31d9e57c1a47.png?w=280&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=c4e51217d861a0c8914974f89c7fc3ca 280w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/integrations/alerting/images/slack-test-message-alerting-f3d6a83c9a3468528ebc31d9e57c1a47.png?w=560&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=8ee32dfa4ce390242c1a2e3487166a03 560w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/integrations/alerting/images/slack-test-message-alerting-f3d6a83c9a3468528ebc31d9e57c1a47.png?w=840&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=17630dac8d4fcbb44a301f4e63ce1aa3 840w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/integrations/alerting/images/slack-test-message-alerting-f3d6a83c9a3468528ebc31d9e57c1a47.png?w=1100&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=5244abab84d1a6f631831e011de1a4e7 1100w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/integrations/alerting/images/slack-test-message-alerting-f3d6a83c9a3468528ebc31d9e57c1a47.png?w=1650&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=86990119aa0c2355e0b846b85501135f 1650w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/integrations/alerting/images/slack-test-message-alerting-f3d6a83c9a3468528ebc31d9e57c1a47.png?w=2500&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=a099bc72875d932e3c8b33bc19616358 2500w" />
</Frame>
