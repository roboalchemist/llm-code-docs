# Source: https://docs.frigade.com/integrations/amplitude.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.frigade.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Amplitude

Frigade supports sending events to Amplitude. The following guide will help you set up this integration in just a few steps.

## Sending Frigade events to Amplitude

You can set up Frigade to send events to Amplitude when your users take actions in your Flows.
The event types and data schema is identical to the events sent in [Frigade Webhooks](/api-reference/webhooks).

<Steps>
  <Step title="Copy your Amplitude API Key">
    Log in to your Amplitude account, open the settings menu, and select **Organization settings**. Select the **Projects** tab and copy the API Key for the project you want to send events to. Do not copy the secret API key as only the public API key is required.

    <img src="https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/amplitude-1.png?fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=cb793dc1cd31739ad093c80fb904e809" className="rounded" data-og-width="1471" width="1471" data-og-height="1188" height="1188" data-path="images/amplitude-1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/amplitude-1.png?w=280&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=188cd96f97dbd480e37763dd769562ab 280w, https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/amplitude-1.png?w=560&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=17dc33c9387d94ade461614082be54f0 560w, https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/amplitude-1.png?w=840&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=b84c99f6ca0a01c9088792c56ffd72ef 840w, https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/amplitude-1.png?w=1100&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=39b08cd005223ababfea581840b6a77f 1100w, https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/amplitude-1.png?w=1650&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=5ea895c4dc166728929ee1074b36b937 1650w, https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/amplitude-1.png?w=2500&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=af4c59c2c03eaaafc5b3fc297a180753 2500w" />
  </Step>

  <Step title="Add Amplitude as an integration in Frigade">
    Open the **Integrations** page in Frigade and select **Amplitude**. Paste the API key you copied in step 1 and click **Save**. If the integration is enabled, events will start streaming to Amplitude immediately.

    <img src="https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/amplitude.png?fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=0bd8ef8b05ba31ea930921b461acd737" className="rounded" data-og-width="3248" width="3248" data-og-height="2124" height="2124" data-path="images/integrations/amplitude.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/amplitude.png?w=280&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=daa2446ce8fa7ae54eff1bab412d5304 280w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/amplitude.png?w=560&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=e47eb5d33eb86b9eb65c94237a8a4a69 560w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/amplitude.png?w=840&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=df9716537176a4e0baa4e23b9b197516 840w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/amplitude.png?w=1100&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=8aaaff68c0189795afedf8b79ca03302 1100w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/amplitude.png?w=1650&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=f2b2788b9c828c5527f03739725979ca 1650w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/amplitude.png?w=2500&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=2453f5c43d3171bebb49fa719978d261 2500w" />
  </Step>

  <Step title="See data in Amplitude">
    Open the dashboard for the project you selected in step 1 and take some action in any given Frigade Flow such as completing a step. You should see events starting to stream from Frigade in the **Realtime event stream** widget:

    <img src="https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/amplitude-2.png?fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=888e39d259276c646c97490422f590b3" className="rounded" data-og-width="1471" width="1471" data-og-height="1188" height="1188" data-path="images/amplitude-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/amplitude-2.png?w=280&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=caa38c6fd57a33c77d59c2d615cbbab8 280w, https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/amplitude-2.png?w=560&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=72d137ccaa11791b98b11c1efae15578 560w, https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/amplitude-2.png?w=840&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=e386123d83186fa12d7b06b9cb3e6205 840w, https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/amplitude-2.png?w=1100&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=562d2795e3011a55c86a104b4b833ed0 1100w, https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/amplitude-2.png?w=1650&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=55506b07f06caa7b300803e1019659f4 1650w, https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/amplitude-2.png?w=2500&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=5db397e5c09e318c73cc0b6abbaf357d 2500w" />
  </Step>
</Steps>

## Sending Amplitude data to Frigade

Bidirectional read/write to Amplitude is not yet available on all Frigade plans. If you're interested in this feature, please [get in touch](mailto:support@frigade.com).
