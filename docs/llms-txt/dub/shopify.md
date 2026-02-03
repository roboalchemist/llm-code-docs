# Source: https://dub.co/docs/sdks/client-side/installation-guides/shopify.md

# Source: https://dub.co/docs/conversions/sales/shopify.md

> ## Documentation Index
> Fetch the complete documentation index at: https://dub.co/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Shopify

> Learn how to track sale conversion events with Shopify and Dub

<Note>
  Conversion tracking requires a [Business plan](https://dub.co/pricing)
  subscription or higher.
</Note>

When it comes to [conversion tracking](/conversions/quickstart), a `sale` event happens when a user purchases a product from your Shopify store.

<Frame>
  <img className="rounded-lg border border-gray-100" src="https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/shopify-conversion-tracking.png?fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=157e896388f79922fcebb31855721d13" alt="A diagram showing how lead events are tracked in the conversion funnel" data-og-width="1387" width="1387" data-og-height="694" height="694" data-path="images/shopify-conversion-tracking.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/shopify-conversion-tracking.png?w=280&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=fb38e6dce31107643296e59761634b09 280w, https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/shopify-conversion-tracking.png?w=560&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=6cac2f4cfa7e487b9d565123f7327e75 560w, https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/shopify-conversion-tracking.png?w=840&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=9c1833111d85d0d9bef5ed08a10018f1 840w, https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/shopify-conversion-tracking.png?w=1100&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=f68e8cb7a9d8cc73a9033a6fafbdb896 1100w, https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/shopify-conversion-tracking.png?w=1650&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=1033332ae1ea1c733a7777071ab3c5e0 1650w, https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/shopify-conversion-tracking.png?w=2500&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=a0eb26b91e24a9fe6013b7fdc6585f8d 2500w" />
</Frame>

In this guide, we will be focusing on tracking sale events from Shopify by leveraging Dub's Shopify integration.

<iframe width="100%" height="469px" className="rounded-xl" src="https://www.loom.com/embed/936970b8db5b41488657fa92ffec384a?sid=04030975-6d7e-4126-8487-a1d9a3095efc" title="Loom video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen />

## Step 1: Enable conversion tracking for your links

First, you'll need to enable conversion tracking for your Dub links to be able to start tracking conversions.

There are a few ways to do this:

1. [On a workspace-level](/conversions/quickstart#option-1-on-a-workspace-level)
2. [On a link-level](/conversions/quickstart#option-2-on-a-link-level)
3. [Via the API](/conversions/quickstart#option-3-via-the-api)

## Step 2: Install the Dub Shopify app

<Steps>
  <Step title="Install the Shopify app">
    Install the [Dub Shopify App](https://d.to/shopify/app) from the App Store.

    <Frame>
      <img src="https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/shopify/shopify-app.png?fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=db64b4f582cc7fbcf8ab3c3f419513ba" alt="The connection status in the Dub app" data-og-width="2462" width="2462" data-og-height="1470" height="1470" data-path="images/shopify/shopify-app.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/shopify/shopify-app.png?w=280&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=99be7cb71113f6b59085264e51077216 280w, https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/shopify/shopify-app.png?w=560&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=97406171627afc25dddbc32589704ff0 560w, https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/shopify/shopify-app.png?w=840&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=8dd2d7ad787edc6e80c1d3c3f84a5458 840w, https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/shopify/shopify-app.png?w=1100&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=fc6a55899a887868c574bbb98befaebc 1100w, https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/shopify/shopify-app.png?w=1650&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=a3ac04088efe4cc2d1e77c58f4df859e 1650w, https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/shopify/shopify-app.png?w=2500&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=2bcb290e5018168a179d54fc9bfaee46 2500w" />
    </Frame>
  </Step>

  <Step title="Connect Shopify to your Dub workspace">
    After installation, you will be prompted to link one of your Dub workspaces to
    the app. Select **Connect** to establish a connection between your
    Shopify store and your Dub workspace.

    You'll be redirected back to your Shopify store after this step and you'll see a list of the links in your Dub workspace:

    <Frame>
      <img src="https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/shopify/shopify-links-table.png?fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=24b1576d1df96314bd235a80792da17b" alt="The list of links in your Dub workspace" data-og-width="1480" width="1480" data-og-height="810" height="810" data-path="images/shopify/shopify-links-table.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/shopify/shopify-links-table.png?w=280&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=028a9f36d511dac5b98161cc9a0a33b0 280w, https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/shopify/shopify-links-table.png?w=560&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=308b1cd761319102680c370c276d38a8 560w, https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/shopify/shopify-links-table.png?w=840&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=895dd70477b09527bbc234591912c839 840w, https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/shopify/shopify-links-table.png?w=1100&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=f0acd909d5a125fd1c2cc6fbac4aa715 1100w, https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/shopify/shopify-links-table.png?w=1650&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=78fc255420e20c185365a19634e3fb0b 1650w, https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/shopify/shopify-links-table.png?w=2500&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=99c3e8fd7be534f21fe1416a1450460f 2500w" />
    </Frame>

    With the Shopify app, you can also create [conversion-enabled links](/conversions//quickstart#step-1%3A-enable-conversion-tracking-for-your-links) directly from your Shopify store:

    <Frame>
      <img src="https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/shopify/shopify-create-link.png?fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=e6d453fce40b3cab9541397a6e651fed" alt="Create a conversion-enabled link from your Shopify store" data-og-width="1480" width="1480" data-og-height="810" height="810" data-path="images/shopify/shopify-create-link.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/shopify/shopify-create-link.png?w=280&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=356ff4021c5785974770c880771bf5b1 280w, https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/shopify/shopify-create-link.png?w=560&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=ecc99977dc618e76232f5b7e3a22e8ef 560w, https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/shopify/shopify-create-link.png?w=840&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=7a11ddd7fba125c789a2e99c1a39e91e 840w, https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/shopify/shopify-create-link.png?w=1100&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=c2ff4429b6929158efaa9b7b7e648168 1100w, https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/shopify/shopify-create-link.png?w=1650&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=baa03fae99832eac628abaf268cb4de5 1650w, https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/shopify/shopify-create-link.png?w=2500&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=586e1640c6b1dc1fa3bf6cb25d64054b 2500w" />
    </Frame>

    If you want a more powerful link builder, you can also use the [Dub Link Builder](https://dub.co/help/article/dub-link-builder) to create conversion-enabled links.
  </Step>

  <Step title="Activate Dub Analytics Script">
    After installing the Dub Shopify app, the Dub Analytics script is added as an app embed. However, it needs to be activated manually to ensure it is included in your current theme.

    To activate the Dub Analytics script, follow these steps:

    1. Navigate to your Shopify admin panel.
    2. Go to **Online Store** > **Themes**.
    3. Click on **Customize** for your current theme.
    4. In the theme editor, select the **App embeds** tab.
    5. Locate the **Analytics Script** for the Dub Shopify app and toggle it to activate.

    <Frame>
      <img src="https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/shopify/shopify-enable-tracking-script.png?fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=b9d6b8c577fc62435e81da381deff6b6" alt="Enable the Dub Analytics script in your Shopify theme" data-og-width="1412" width="1412" data-og-height="983" height="983" data-path="images/shopify/shopify-enable-tracking-script.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/shopify/shopify-enable-tracking-script.png?w=280&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=00720d7b5b41664b91583029ca770b50 280w, https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/shopify/shopify-enable-tracking-script.png?w=560&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=87662f2a7554a1e21a99e6eda8636cbd 560w, https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/shopify/shopify-enable-tracking-script.png?w=840&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=e04f6b379749465c280b98e74b166e29 840w, https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/shopify/shopify-enable-tracking-script.png?w=1100&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=19afd70e33fc905f367bc177e6c696fe 1100w, https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/shopify/shopify-enable-tracking-script.png?w=1650&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=54a6538fd634de8631db53f1049c0f2a 1650w, https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/shopify/shopify-enable-tracking-script.png?w=2500&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=0d077d63724ef208aeacd80723953b37 2500w" />
    </Frame>
  </Step>
</Steps>

<Tip>
  Dub’s Shopify integration will automatically forward the following events to Dub:

  * `orders/paid`: This event is triggered when a customer completes a purchase on your Shopify store. It is utilized to track sales that originate from Dub links.
  * `app/uninstalled`: This event occurs when the app is uninstalled from a store. It is used to remove the integration from your Dub workspace.

  In addition to the above, we also subscribe to the mandatory compliance webhook topics that are required by Shopify.
</Tip>

## Step 3: View conversion results

And that's it – you're all set! You can now sit back, relax, and watch your conversion revenue grow. We provide 3 different views to help you understand your conversions:

* **Time-series**: A [time-series view](https://app.dub.co/dub/analytics?view=timeseries) of the number clicks, leads and sales.

<Frame>
  <img src="https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/timeseries-chart.png?fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=7380bc6120ade538b2b65eefdc76d3ed" alt="Time-series line chart" data-og-width="2400" width="2400" data-og-height="1260" height="1260" data-path="images/conversions/timeseries-chart.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/timeseries-chart.png?w=280&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=430758e529cd22c5d28f976ee7da5379 280w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/timeseries-chart.png?w=560&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=9cf861c9aa7cf680f46ce32585303d2b 560w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/timeseries-chart.png?w=840&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=999b05a7805bd208b4649fc67a3b45e0 840w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/timeseries-chart.png?w=1100&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=42baa1d9d42c26ed191875fef033128a 1100w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/timeseries-chart.png?w=1650&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=127ee673f66f2079f236985ec754416e 1650w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/timeseries-chart.png?w=2500&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=1c0696bb18043dd86388f03d09aed450 2500w" />
</Frame>

* **Funnel chart**: A [funnel chart view](http://app.dub.co/analytics?view=funnel) visualizing the conversion & dropoff rates across the different steps in the conversion funnel (clicks → leads → sales).

<Frame>
  <img src="https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/funnel-chart.png?fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=6275caafcfc3be6d8b498149222f225e" alt="Funnel chart view showing the conversion & dropoff rates from clicks → leads → sales" data-og-width="2400" width="2400" data-og-height="1260" height="1260" data-path="images/conversions/funnel-chart.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/funnel-chart.png?w=280&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=df57b14d04dd585c5236f6fcf16a4963 280w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/funnel-chart.png?w=560&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=fc1689a06ce8ceecf1487faca8730d06 560w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/funnel-chart.png?w=840&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=b69533d460a2bc95964d7f6d2e5f23f4 840w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/funnel-chart.png?w=1100&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=43b86431662a4c214a36fbf5405abb4a 1100w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/funnel-chart.png?w=1650&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=687f900f0b8732301c43c8ee18ca7dd4 1650w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/funnel-chart.png?w=2500&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=aed9e63c7fd1fb67c463920c73911cba 2500w" />
</Frame>

* **Real-time events stream**: A [real-time events stream](https://app.dub.co/events) of every single conversion event that occurs across all your links in your workspace.

<Frame>
  <img src="https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/events-table.png?fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=c2467f9fa2e755f06b3e7b147fa0bd81" alt="The Events Stream dashboard on Dub" data-og-width="2400" width="2400" data-og-height="1260" height="1260" data-path="images/conversions/events-table.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/events-table.png?w=280&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=8e747ccc2f01015e014a9b4fbc98d588 280w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/events-table.png?w=560&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=4a0c65b37cf99181b712beb063e46dc2 560w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/events-table.png?w=840&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=345d5b0b36c6f2093ea7b6a97d73ff49 840w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/events-table.png?w=1100&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=5deb48ab5e08bf2e31447fd32615c05e 1100w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/events-table.png?w=1650&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=33d6f27b5c067eb8586cfea15fe0a040 1650w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/events-table.png?w=2500&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=132a7592c8ecf518b31c043dad2093f4 2500w" />
</Frame>

## Currency conversion support

For simplicity, Dub records all sales in the native currency of the Shopify store. For example, if you're using USD for your Shopify store, Dub will record all sales in USD – even if your customers are paying in a different currency.

```json orders/paid theme={null}
// Shopify orders/paid event payload
// @see: https://shopify.dev/docs/api/webhooks?reference=toml#list-of-topics-orders/paid
{
  ...
  "current_subtotal_price_set": {
    "shop_money": {
      "amount": "398.00", // this is the amount that Dub will record
      "currency_code": "USD" // this is the currency of your Shopify store
    },
    "presentment_money": {
      "amount": "572.25",
      "currency_code": "CAD"
    }
  },
  ...
}
```
