# Source: https://docs.frigade.com/integrations/mixpanel.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.frigade.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Mixpanel

Frigade supports ingesting Mixpanel data and using this data to [Target flows](/platform/targeting) to users.

There are two ways to integrate Mixpanel with Frigade: real-time sync (via Mixpanel Webhooks) or a daily sync (via the Mixpanel API). Both options can also be used together.

Depending on your use case, we recommend using the Webhook integration for real-time data and the API integration for historical data as well as syncing non-standard user properties.

## Mixpanel Webhooks (Webhook sync)

Sending Mixpanel data via Webhooks allows you to send real-time data to Frigade as your users enter and leave cohorts. The setup process is as follows:

<Steps>
  <Step title="Create a Webhook in Mixpanel">
    Following the [Mixpanel documentation](https://docs.mixpanel.com/docs/cohort-sync/webhooks), create a new Webhook on the Mixpanel **Integrations** page.
    You should use the following parameters when creating the webhook:

    * **Connector name:** `Frigade`
    * **URL:** `https://api.frigade.com/v1/thirdParty/cdp/mixpanel`
    * **Username:** `frigade`
    * **Password:** Your <i>private</i> Frigade API key (found on the **Developer** page in the Frigade dashboard)

    <img src="https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/mixpanel/webhook-1.png?fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=ed5a954894da7024871e313c1913e57e" className="rounded" data-og-width="2800" width="2800" data-og-height="1996" height="1996" data-path="images/integrations/mixpanel/webhook-1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/mixpanel/webhook-1.png?w=280&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=d039dac8383c04c7c36350afb464b488 280w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/mixpanel/webhook-1.png?w=560&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=6096cf4e27e69943eb36f24703e6b1e6 560w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/mixpanel/webhook-1.png?w=840&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=2cde3c53e0925cc016d48a21114f1604 840w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/mixpanel/webhook-1.png?w=1100&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=eff3d9d445606dfdb0aa99a6e2d25bd2 1100w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/mixpanel/webhook-1.png?w=1650&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=3f98671eaa9d60343fa362b2e7af17fc 1650w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/mixpanel/webhook-1.png?w=2500&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=02a3f106b94f7bddba9f8a7731a2acac 2500w" />
  </Step>

  <Step title="View cohort data in Frigade">
    After setting up the Webhook, you will see the cohort data in the Frigade dashboard. Note that it may take up to 30 minutes the first time before all data is synced.

    <img src="https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/mixpanel/webhook-2.png?fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=c5718e6927779a1f29f4591fd46697b7" className="rounded" data-og-width="2902" width="2902" data-og-height="1992" height="1992" data-path="images/integrations/mixpanel/webhook-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/mixpanel/webhook-2.png?w=280&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=96afcbd6c22fac3f4370f1c9b1fbba34 280w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/mixpanel/webhook-2.png?w=560&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=26a2e749fa11e3084c0751e8c7666e16 560w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/mixpanel/webhook-2.png?w=840&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=063d8c3308f11e1dfe7daaa2da72c3e9 840w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/mixpanel/webhook-2.png?w=1100&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=4e9dd8c8d7dc108cbcaf615524870bff 1100w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/mixpanel/webhook-2.png?w=1650&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=cbe69ca912b4eb3da56806e25536ae8b 1650w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/mixpanel/webhook-2.png?w=2500&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=d05a4a45a6ababb48804fc8d72f4d8ca 2500w" />
  </Step>
</Steps>

## Mixpanel Cohorts in Frigade (API sync)

To send your Cohorts to Frigade, you will need to create a service account in Mixpanel and add the keys to Frigade. Frigade will then automatically sync your cohorts from Mixpanel.

<Steps>
  <Step title=" Create a Mixpanel Service Account for Frigade">
    To create a service account for Frigade, open your Mixpanel project, then click **Project Settings** and select the **Service Accounts** tab. Then click **Add Service Account** and select **Analyst** as the role.

    <img src="https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/mixpanel-1.png?fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=7604297781f5dc49f0550957fb74ecc3" className="rounded" data-og-width="1540" width="1540" data-og-height="1121" height="1121" data-path="images/mixpanel-1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/mixpanel-1.png?w=280&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=62e9cb7070d57bd1b87c1e58d04f36d6 280w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/mixpanel-1.png?w=560&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=e821d9a42308858c3ccda2ecd127ead6 560w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/mixpanel-1.png?w=840&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=7aa21e8b4c638c05620fb97adff42eb5 840w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/mixpanel-1.png?w=1100&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=594a1d4969d572ce7bc7cb431d3eb83e 1100w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/mixpanel-1.png?w=1650&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=8debd8b0001dc46d0af280fb143f205e 1650w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/mixpanel-1.png?w=2500&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=c0b1d5a4f544f1d77a302c6cf35aaafe 2500w" />
  </Step>

  <Step title="Add the Mixpanel Service Account keys to Frigade">
    Open the [Integrations](https://app.frigade.com/integrations) page in the Frigade dashboard and click the "Connect" button for Mixpanel. Then paste the two keys you copied in the previous step into the corresponding fields.

    Then, copy the **Project ID** from Mixpanel that you wish to sync cohorts from. You can find the Project ID on the Project Settings page in Mixpanel:

    <img src="https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/mixpanel-2.png?fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=f471191ddfc81704dbfb891775d06136" className="rounded" data-og-width="1540" width="1540" data-og-height="1121" height="1121" data-path="images/mixpanel-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/mixpanel-2.png?w=280&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=750e18a1cbd6d06f85c99d5cc41eeb43 280w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/mixpanel-2.png?w=560&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=2ae6650eaa4dcdc23b3069beb147f33a 560w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/mixpanel-2.png?w=840&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=0338d22c3080805e35322ee79d2324d0 840w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/mixpanel-2.png?w=1100&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=788c855bfb471e13a925d84376b3b05e 1100w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/mixpanel-2.png?w=1650&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=0af007772aa3c6d76b5af8bb1503b8b4 1650w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/mixpanel-2.png?w=2500&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=dc11d8bfa29d9cfd4fecbc6d99280bba 2500w" />
  </Step>

  <Step title="See your Mixpanel Cohorts in Frigade">
    Your Mixpanel cohorts appear as properties on your users in Frigade. Each cohort is prefixed with `mixpanel_cohort_` and the name of the cohort. For example, if you have a cohort named `NewUsers`, you will see a property named `mixpanel_cohort_NewUsers` on your users in Frigade.

    <img src="https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/mixpanel-3.png?fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=58d6d81abb9bbf50c23d2bafcea6e24c" className="rounded" data-og-width="2980" width="2980" data-og-height="2136" height="2136" data-path="images/mixpanel-3.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/mixpanel-3.png?w=280&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=cdcfd968617f0cddad59d87863dc8dfa 280w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/mixpanel-3.png?w=560&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=8b00d23a23f7f44d31a2c4f50f6d074e 560w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/mixpanel-3.png?w=840&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=f8f03a7aed9fee357d8a23e3fe011707 840w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/mixpanel-3.png?w=1100&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=f585743a19993fa122481d15fee6b61f 1100w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/mixpanel-3.png?w=1650&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=8bc27427a16e6476af2f4cb0773425ab 1650w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/mixpanel-3.png?w=2500&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=61a9e7e6c76218673e7601942b324049 2500w" />
  </Step>
</Steps>

## Targeting Mixpanel Cohorts

You can target users based on these properties in the [Targeting](/platform/targeting) section of the Frigade dashboard. For instance, to target users in the `NewUsers` cohort, you can use the following targeting rule:

```js  theme={"system"}
user.property('mixpanel_cohort_NewUsers') == true
```
