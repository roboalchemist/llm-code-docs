# Source: https://docs.venice.ai/overview/guides/generating-api-key.md

# Generating an API Key

Venice's API is protected via API keys. To begin using the Venice API, you'll first need to generate a new key. Follow these steps to get started.

<Steps>
  <Step title="Visit the API Settings Page">
    To get to the API settings page, by visiting [https://venice.ai/settings/api](https://venice.ai/settings/api). This page is accessible by clicking "API" in the left hand toolbar, or by clicking “API” within your user settings.

    Within this dashboard, you're able to view your Diem and USD balances, your API Tier, your API Usage, and your API Keys.

    <Frame>
      <img src="https://mintcdn.com/veniceai/IFxWLBK8qRcf4Dhb/images/guides/API-Overview.png?fit=max&auto=format&n=IFxWLBK8qRcf4Dhb&q=85&s=0077ee4359a34036007b6cc94967adbf" alt="API Overview" data-og-width="2572" width="2572" data-og-height="1252" height="1252" data-path="images/guides/API-Overview.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/veniceai/IFxWLBK8qRcf4Dhb/images/guides/API-Overview.png?w=280&fit=max&auto=format&n=IFxWLBK8qRcf4Dhb&q=85&s=e846521d3874f780ee11b5f2cfcd15ff 280w, https://mintcdn.com/veniceai/IFxWLBK8qRcf4Dhb/images/guides/API-Overview.png?w=560&fit=max&auto=format&n=IFxWLBK8qRcf4Dhb&q=85&s=aaaf8a8c96de1f9f48466ac82703caa7 560w, https://mintcdn.com/veniceai/IFxWLBK8qRcf4Dhb/images/guides/API-Overview.png?w=840&fit=max&auto=format&n=IFxWLBK8qRcf4Dhb&q=85&s=98918b29973a499c40b96c2ab87a6726 840w, https://mintcdn.com/veniceai/IFxWLBK8qRcf4Dhb/images/guides/API-Overview.png?w=1100&fit=max&auto=format&n=IFxWLBK8qRcf4Dhb&q=85&s=c7dedd1e4e2da578c3902ae2f0788101 1100w, https://mintcdn.com/veniceai/IFxWLBK8qRcf4Dhb/images/guides/API-Overview.png?w=1650&fit=max&auto=format&n=IFxWLBK8qRcf4Dhb&q=85&s=4deecf2a10e87e9142f83f0a1e641f29 1650w, https://mintcdn.com/veniceai/IFxWLBK8qRcf4Dhb/images/guides/API-Overview.png?w=2500&fit=max&auto=format&n=IFxWLBK8qRcf4Dhb&q=85&s=81f7e4f1b3713cf16c84d573a553f0ef 2500w" />
    </Frame>
  </Step>

  <Step title="Click Generate New API Key">
    Scroll down the dashboard and select "Generate New API Key". You'll be presented with a list of options.

    * **Description:** This is used to name your API key

    * **API Key Type:**

      * “Admin” keys have the ability to delete or generate additional API keys programmatically.

      * “Inference Only” keys are only permitted to run inference.

    * **Expires at:** You can choose to set an expiration date for the API key after which it will cease to function. By default, a date will not be set, and the key will work in perpetuity.

    * **Epoch Consumption Limits:** This allows you to create limits for API usage from the individual API key. You can choose to limit the Diem or USD amount allowable within a given epoch (24hrs).

    <Frame>
      <img src="https://mintcdn.com/veniceai/IFxWLBK8qRcf4Dhb/images/guides/api-keys/create-key.png?fit=max&auto=format&n=IFxWLBK8qRcf4Dhb&q=85&s=b053f218d2aaa8c88bbd802a7d6ddc50" alt="Generate New API Key" data-og-width="2624" width="2624" data-og-height="1296" height="1296" data-path="images/guides/api-keys/create-key.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/veniceai/IFxWLBK8qRcf4Dhb/images/guides/api-keys/create-key.png?w=280&fit=max&auto=format&n=IFxWLBK8qRcf4Dhb&q=85&s=0f2afc0a5ff0d7082674fca359c3fa62 280w, https://mintcdn.com/veniceai/IFxWLBK8qRcf4Dhb/images/guides/api-keys/create-key.png?w=560&fit=max&auto=format&n=IFxWLBK8qRcf4Dhb&q=85&s=db9c8ffd40a01eac65f6c17e9f726838 560w, https://mintcdn.com/veniceai/IFxWLBK8qRcf4Dhb/images/guides/api-keys/create-key.png?w=840&fit=max&auto=format&n=IFxWLBK8qRcf4Dhb&q=85&s=92f9c039ea5dc316e59006b65dd1c41f 840w, https://mintcdn.com/veniceai/IFxWLBK8qRcf4Dhb/images/guides/api-keys/create-key.png?w=1100&fit=max&auto=format&n=IFxWLBK8qRcf4Dhb&q=85&s=c35cf11766f8c774e68d59ca9b6268d5 1100w, https://mintcdn.com/veniceai/IFxWLBK8qRcf4Dhb/images/guides/api-keys/create-key.png?w=1650&fit=max&auto=format&n=IFxWLBK8qRcf4Dhb&q=85&s=c5b95320320ddc865b5cad607ca8a100 1650w, https://mintcdn.com/veniceai/IFxWLBK8qRcf4Dhb/images/guides/api-keys/create-key.png?w=2500&fit=max&auto=format&n=IFxWLBK8qRcf4Dhb&q=85&s=9a5fe0e9e9151e795fd48b3422e965d0 2500w" />
    </Frame>
  </Step>

  <Step title="Generate the key">
    Clicking Generate will show you the API key.

    <Warning>
      **Important:** This key is only shown once. Make sure to copy it and store it in a safe place. If you lose it, you'll need to delete it and create a new one.
    </Warning>

    <Frame>
      <img src="https://mintcdn.com/veniceai/IFxWLBK8qRcf4Dhb/images/guides/api-keys/result.png?fit=max&auto=format&n=IFxWLBK8qRcf4Dhb&q=85&s=1a9ede76b5428bd0dc00291ea73d93f7" alt="Your API Key" data-og-width="1198" width="1198" data-og-height="660" height="660" data-path="images/guides/api-keys/result.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/veniceai/IFxWLBK8qRcf4Dhb/images/guides/api-keys/result.png?w=280&fit=max&auto=format&n=IFxWLBK8qRcf4Dhb&q=85&s=deaf0f447a6aab1a230fd0f5bcf0fa94 280w, https://mintcdn.com/veniceai/IFxWLBK8qRcf4Dhb/images/guides/api-keys/result.png?w=560&fit=max&auto=format&n=IFxWLBK8qRcf4Dhb&q=85&s=e46d47c3e10195f5ad51fc7b5b7c33a6 560w, https://mintcdn.com/veniceai/IFxWLBK8qRcf4Dhb/images/guides/api-keys/result.png?w=840&fit=max&auto=format&n=IFxWLBK8qRcf4Dhb&q=85&s=12a4038b4af62c624f32c9c3968c0522 840w, https://mintcdn.com/veniceai/IFxWLBK8qRcf4Dhb/images/guides/api-keys/result.png?w=1100&fit=max&auto=format&n=IFxWLBK8qRcf4Dhb&q=85&s=b0f2e2f5da7c2e651739f72e56257781 1100w, https://mintcdn.com/veniceai/IFxWLBK8qRcf4Dhb/images/guides/api-keys/result.png?w=1650&fit=max&auto=format&n=IFxWLBK8qRcf4Dhb&q=85&s=8eb0819d5c5a50d74570b12634253311 1650w, https://mintcdn.com/veniceai/IFxWLBK8qRcf4Dhb/images/guides/api-keys/result.png?w=2500&fit=max&auto=format&n=IFxWLBK8qRcf4Dhb&q=85&s=1377d84068a97a6c209c5356069b4e8a 2500w" />
    </Frame>
  </Step>
</Steps>
