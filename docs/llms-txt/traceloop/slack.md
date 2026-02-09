# Source: https://www.traceloop.com/docs/integrations/slack.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.traceloop.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Slack

> Get daily or weekly messages about your AI flows directly in Slack

Connecting Traceloop to Slack allows you to receive automated updates about your AI flows. You can configure daily or weekly messages to stay informed about your application's performance and insights.

<Steps>
  <Step title="Set up the Integration within Traceloop">
    Go to the [integrations page](https://app.traceloop.com/settings/integrations) within Traceloop and click on the Slack card.

    <Frame>
      <img className="block dark:hidden" src="https://mintcdn.com/enrolla/pLLlNcf8Qyyp9R0l/img/traceloop-integrations/integrations-light.png?fit=max&auto=format&n=pLLlNcf8Qyyp9R0l&q=85&s=35ac5fe45caf3c3530228c0a3b0bff35" data-og-width="2570" width="2570" data-og-height="1536" height="1536" data-path="img/traceloop-integrations/integrations-light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/enrolla/pLLlNcf8Qyyp9R0l/img/traceloop-integrations/integrations-light.png?w=280&fit=max&auto=format&n=pLLlNcf8Qyyp9R0l&q=85&s=7808c9d3c6effed886279981cedd62ef 280w, https://mintcdn.com/enrolla/pLLlNcf8Qyyp9R0l/img/traceloop-integrations/integrations-light.png?w=560&fit=max&auto=format&n=pLLlNcf8Qyyp9R0l&q=85&s=c34accf8f8506402b2a1206d1fbc9bb1 560w, https://mintcdn.com/enrolla/pLLlNcf8Qyyp9R0l/img/traceloop-integrations/integrations-light.png?w=840&fit=max&auto=format&n=pLLlNcf8Qyyp9R0l&q=85&s=da7f7d0802920e44a2b77dad15c5e0e5 840w, https://mintcdn.com/enrolla/pLLlNcf8Qyyp9R0l/img/traceloop-integrations/integrations-light.png?w=1100&fit=max&auto=format&n=pLLlNcf8Qyyp9R0l&q=85&s=7bc22776339cf7dc4fb8fdd1d8fae87d 1100w, https://mintcdn.com/enrolla/pLLlNcf8Qyyp9R0l/img/traceloop-integrations/integrations-light.png?w=1650&fit=max&auto=format&n=pLLlNcf8Qyyp9R0l&q=85&s=cbbd5dc3dfc7c05bbde8a7d5c072b623 1650w, https://mintcdn.com/enrolla/pLLlNcf8Qyyp9R0l/img/traceloop-integrations/integrations-light.png?w=2500&fit=max&auto=format&n=pLLlNcf8Qyyp9R0l&q=85&s=6f81b4b7119103acf0aa0e70b5be2dfc 2500w" />

      <img className="hidden dark:block" src="https://mintcdn.com/enrolla/pLLlNcf8Qyyp9R0l/img/traceloop-integrations/integrations-dark.png?fit=max&auto=format&n=pLLlNcf8Qyyp9R0l&q=85&s=23c023f1759a68c3fd35cf8d58b5e4e2" data-og-width="2570" width="2570" data-og-height="1536" height="1536" data-path="img/traceloop-integrations/integrations-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/enrolla/pLLlNcf8Qyyp9R0l/img/traceloop-integrations/integrations-dark.png?w=280&fit=max&auto=format&n=pLLlNcf8Qyyp9R0l&q=85&s=7e01c6589cfc972a43bcbe0b5cb9ac43 280w, https://mintcdn.com/enrolla/pLLlNcf8Qyyp9R0l/img/traceloop-integrations/integrations-dark.png?w=560&fit=max&auto=format&n=pLLlNcf8Qyyp9R0l&q=85&s=2277536bbdef309a55006740413c2bd5 560w, https://mintcdn.com/enrolla/pLLlNcf8Qyyp9R0l/img/traceloop-integrations/integrations-dark.png?w=840&fit=max&auto=format&n=pLLlNcf8Qyyp9R0l&q=85&s=77276213c59309e1e435bae21852f088 840w, https://mintcdn.com/enrolla/pLLlNcf8Qyyp9R0l/img/traceloop-integrations/integrations-dark.png?w=1100&fit=max&auto=format&n=pLLlNcf8Qyyp9R0l&q=85&s=8fb7db7d10a5a5b0ac27b72e654c12dd 1100w, https://mintcdn.com/enrolla/pLLlNcf8Qyyp9R0l/img/traceloop-integrations/integrations-dark.png?w=1650&fit=max&auto=format&n=pLLlNcf8Qyyp9R0l&q=85&s=6a91559b2ce8ad7173298530618e21db 1650w, https://mintcdn.com/enrolla/pLLlNcf8Qyyp9R0l/img/traceloop-integrations/integrations-dark.png?w=2500&fit=max&auto=format&n=pLLlNcf8Qyyp9R0l&q=85&s=b5f88909d17b892d0e2a6bc6a0233bc3 2500w" />
    </Frame>
  </Step>

  <Step title="Authorize Slack">
    Click on the Slack integration and follow the "Connect to Slack" button to authorize Traceloop to send messages to your Slack workspace.
  </Step>

  <Step title="Configure your preferences">
    Choose your notification preferences:

    * Select the Slack channel where you want to receive updates

    <Info>
      **Important:** Make sure to invite the Traceloop app to the channel before enabling the integration.
    </Info>

    <Frame>
      <img src="https://mintcdn.com/enrolla/pLLlNcf8Qyyp9R0l/img/traceloop-integrations/slack-invite-app.png?fit=max&auto=format&n=pLLlNcf8Qyyp9R0l&q=85&s=bf2d85ccfbfd32eee84dea0db1897a62" data-og-width="1870" width="1870" data-og-height="644" height="644" data-path="img/traceloop-integrations/slack-invite-app.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/enrolla/pLLlNcf8Qyyp9R0l/img/traceloop-integrations/slack-invite-app.png?w=280&fit=max&auto=format&n=pLLlNcf8Qyyp9R0l&q=85&s=b0bf2273ac7400da2c1500cbc4a3ab6a 280w, https://mintcdn.com/enrolla/pLLlNcf8Qyyp9R0l/img/traceloop-integrations/slack-invite-app.png?w=560&fit=max&auto=format&n=pLLlNcf8Qyyp9R0l&q=85&s=1ba506f45b0cb8742446b07d529d742f 560w, https://mintcdn.com/enrolla/pLLlNcf8Qyyp9R0l/img/traceloop-integrations/slack-invite-app.png?w=840&fit=max&auto=format&n=pLLlNcf8Qyyp9R0l&q=85&s=7e9c5729e88f0fef93d58588795ae547 840w, https://mintcdn.com/enrolla/pLLlNcf8Qyyp9R0l/img/traceloop-integrations/slack-invite-app.png?w=1100&fit=max&auto=format&n=pLLlNcf8Qyyp9R0l&q=85&s=067adddc4a257e7ae02bf28dc6428844 1100w, https://mintcdn.com/enrolla/pLLlNcf8Qyyp9R0l/img/traceloop-integrations/slack-invite-app.png?w=1650&fit=max&auto=format&n=pLLlNcf8Qyyp9R0l&q=85&s=8844d171b265ae5c5ee829c4b932d215 1650w, https://mintcdn.com/enrolla/pLLlNcf8Qyyp9R0l/img/traceloop-integrations/slack-invite-app.png?w=2500&fit=max&auto=format&n=pLLlNcf8Qyyp9R0l&q=85&s=faf3e41548049a5352b39fa1f5d6a634 2500w" />
    </Frame>

    * Select the desired schedule -  daily/weekly
    * Set the required time and timezone
    * Choose which environment to monitor

    <Frame>
      <img className="block dark:hidden" src="https://mintcdn.com/enrolla/pLLlNcf8Qyyp9R0l/img/traceloop-integrations/slack-settings-light.png?fit=max&auto=format&n=pLLlNcf8Qyyp9R0l&q=85&s=90492a5b6ee99ce51d1957cfdc121586" data-og-width="1628" width="1628" data-og-height="1420" height="1420" data-path="img/traceloop-integrations/slack-settings-light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/enrolla/pLLlNcf8Qyyp9R0l/img/traceloop-integrations/slack-settings-light.png?w=280&fit=max&auto=format&n=pLLlNcf8Qyyp9R0l&q=85&s=b45c7ffcd9474dd361902c4b4bf0a5ff 280w, https://mintcdn.com/enrolla/pLLlNcf8Qyyp9R0l/img/traceloop-integrations/slack-settings-light.png?w=560&fit=max&auto=format&n=pLLlNcf8Qyyp9R0l&q=85&s=b391f4fba8a4bbe977f6b1343f5faab8 560w, https://mintcdn.com/enrolla/pLLlNcf8Qyyp9R0l/img/traceloop-integrations/slack-settings-light.png?w=840&fit=max&auto=format&n=pLLlNcf8Qyyp9R0l&q=85&s=5abdf67b7cb00be3ec6845eea37afe0e 840w, https://mintcdn.com/enrolla/pLLlNcf8Qyyp9R0l/img/traceloop-integrations/slack-settings-light.png?w=1100&fit=max&auto=format&n=pLLlNcf8Qyyp9R0l&q=85&s=eb1377d5254ff4bd3533ecb57428332c 1100w, https://mintcdn.com/enrolla/pLLlNcf8Qyyp9R0l/img/traceloop-integrations/slack-settings-light.png?w=1650&fit=max&auto=format&n=pLLlNcf8Qyyp9R0l&q=85&s=2a726d12ebd12260d00b08f4e077d5ee 1650w, https://mintcdn.com/enrolla/pLLlNcf8Qyyp9R0l/img/traceloop-integrations/slack-settings-light.png?w=2500&fit=max&auto=format&n=pLLlNcf8Qyyp9R0l&q=85&s=363ce75b593bac7bfa968670a23ce241 2500w" />

      <img className="hidden dark:block" src="https://mintcdn.com/enrolla/pLLlNcf8Qyyp9R0l/img/traceloop-integrations/slack-settings-dark.png?fit=max&auto=format&n=pLLlNcf8Qyyp9R0l&q=85&s=3dfadbba5fb666187c3a947aa282ddac" data-og-width="1628" width="1628" data-og-height="1420" height="1420" data-path="img/traceloop-integrations/slack-settings-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/enrolla/pLLlNcf8Qyyp9R0l/img/traceloop-integrations/slack-settings-dark.png?w=280&fit=max&auto=format&n=pLLlNcf8Qyyp9R0l&q=85&s=d22f0cb52cdeed2df3a231106e1a0546 280w, https://mintcdn.com/enrolla/pLLlNcf8Qyyp9R0l/img/traceloop-integrations/slack-settings-dark.png?w=560&fit=max&auto=format&n=pLLlNcf8Qyyp9R0l&q=85&s=7b8680c083877aebdc4248523d659081 560w, https://mintcdn.com/enrolla/pLLlNcf8Qyyp9R0l/img/traceloop-integrations/slack-settings-dark.png?w=840&fit=max&auto=format&n=pLLlNcf8Qyyp9R0l&q=85&s=d12c1af42a417d0e99522d81b5fef038 840w, https://mintcdn.com/enrolla/pLLlNcf8Qyyp9R0l/img/traceloop-integrations/slack-settings-dark.png?w=1100&fit=max&auto=format&n=pLLlNcf8Qyyp9R0l&q=85&s=87ff62438d3d370b4f09bf17c4f3cf6f 1100w, https://mintcdn.com/enrolla/pLLlNcf8Qyyp9R0l/img/traceloop-integrations/slack-settings-dark.png?w=1650&fit=max&auto=format&n=pLLlNcf8Qyyp9R0l&q=85&s=4a2a7d4cdc381f933449ba97685d833d 1650w, https://mintcdn.com/enrolla/pLLlNcf8Qyyp9R0l/img/traceloop-integrations/slack-settings-dark.png?w=2500&fit=max&auto=format&n=pLLlNcf8Qyyp9R0l&q=85&s=e1a655f6b1cb06cb03c0d17bd267d465 2500w" />
    </Frame>
  </Step>
</Steps>

**That's it!**

You'll now receive automated messages in your chosen Slack channel with insights about your AI flows, including key metrics and performance updates.

<Frame>
  <img src="https://mintcdn.com/enrolla/pLLlNcf8Qyyp9R0l/img/traceloop-integrations/slack-example.png?fit=max&auto=format&n=pLLlNcf8Qyyp9R0l&q=85&s=c0489636d1a9bb96f431e06b9185b327" data-og-width="568" width="568" data-og-height="361" height="361" data-path="img/traceloop-integrations/slack-example.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/enrolla/pLLlNcf8Qyyp9R0l/img/traceloop-integrations/slack-example.png?w=280&fit=max&auto=format&n=pLLlNcf8Qyyp9R0l&q=85&s=0032e3b3a6138314e51d0547c6f2443e 280w, https://mintcdn.com/enrolla/pLLlNcf8Qyyp9R0l/img/traceloop-integrations/slack-example.png?w=560&fit=max&auto=format&n=pLLlNcf8Qyyp9R0l&q=85&s=ce474ab1a81fd62eb7fccfd07c32586a 560w, https://mintcdn.com/enrolla/pLLlNcf8Qyyp9R0l/img/traceloop-integrations/slack-example.png?w=840&fit=max&auto=format&n=pLLlNcf8Qyyp9R0l&q=85&s=76557b8fb9f0299d0d2cdf525a46c1e7 840w, https://mintcdn.com/enrolla/pLLlNcf8Qyyp9R0l/img/traceloop-integrations/slack-example.png?w=1100&fit=max&auto=format&n=pLLlNcf8Qyyp9R0l&q=85&s=fec5942168d4b07f7acf52d30eaa15b6 1100w, https://mintcdn.com/enrolla/pLLlNcf8Qyyp9R0l/img/traceloop-integrations/slack-example.png?w=1650&fit=max&auto=format&n=pLLlNcf8Qyyp9R0l&q=85&s=d2786691a3d03ec2899486ccdc980814 1650w, https://mintcdn.com/enrolla/pLLlNcf8Qyyp9R0l/img/traceloop-integrations/slack-example.png?w=2500&fit=max&auto=format&n=pLLlNcf8Qyyp9R0l&q=85&s=ed9a750e25e04bc5d7ba574d68ff9087 2500w" />
</Frame>
