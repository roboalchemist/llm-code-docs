# Source: https://documentation.onesignal.com/docs/en/generate-an-amazon-api-key.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Amazon API key generation

> Step-by-step guide

An Amazon API Key is required for all **Amazon** apps.

## Requirements

* An Amazon app.
* An [Amazon Developer account](https://developer.amazon.com/login.html) account.
* A [OneSignal Account](https://onesignal.com/), if you do not already have one.

<Steps titleSize="h2">
  <Step title="Create a security profile">
    Log in to your [Amazon Developer account](https://developer.amazon.com/login.html) and select your app.

    Click on the **Device Messaging** tab and click **Create a New Security Profile**.

    <Frame>
      <img src="https://mintcdn.com/onesignal/tc0EvmtSSX56SX0c/images/docs/92REq7thRFiW728xOiNS_AmazonSecurityProfile1.png?fit=max&auto=format&n=tc0EvmtSSX56SX0c&q=85&s=f9bcc17153bcd37e78ace556b5c6b2e3" width="976" height="573" data-path="images/docs/92REq7thRFiW728xOiNS_AmazonSecurityProfile1.png" />
    </Frame>

    Give your Security Profile the required name and description, then click Save.

    <Frame>
      <img src="https://mintcdn.com/onesignal/RWtLFPeffHrC81wI/images/docs/aIDGySBrR7iFANxPak1L_AmazonSecurityProfile2.png?fit=max&auto=format&n=RWtLFPeffHrC81wI&q=85&s=51b2c5defe0c7574892e298475e9b37d" width="927" height="394" data-path="images/docs/aIDGySBrR7iFANxPak1L_AmazonSecurityProfile2.png" />
    </Frame>

    You should get a series of success messages. Next, click **View Security Profile** to continue.

    <Frame>
      <img src="https://mintcdn.com/onesignal/6tscVAtiSqz353kV/images/docs/D4frRRzJQue8WZufNbDr_AmazonSecurityProfile3.png?fit=max&auto=format&n=6tscVAtiSqz353kV&q=85&s=0936b1b5aff5919fa3a8ede15b2bf06f" width="865" height="366" data-path="images/docs/D4frRRzJQue8WZufNbDr_AmazonSecurityProfile3.png" />
    </Frame>

    You will then see a settings page that lists your **Client ID** and **Client Secret**. Leave this page open, as you will need this information in Step 2.

    <Frame>
      <img src="https://mintcdn.com/onesignal/6v_cVPknFpo5qSVB/images/docs/06k5hfGR5OtUjHqSvzHp_AmazonSecurityProfile4.png?fit=max&auto=format&n=6v_cVPknFpo5qSVB&q=85&s=861a5e61a21b3df438d16164c7a16389" width="912" height="341" data-path="images/docs/06k5hfGR5OtUjHqSvzHp_AmazonSecurityProfile4.png" />
    </Frame>
  </Step>

  <Step title="Configure your OneSignal app's Amazon platform settings">
    In the OneSignal dashboard, select your app from the All Apps page, then go to Settings. Under Native App Platforms, click Amazon Fire.

    <Frame>
      <img src="https://mintcdn.com/onesignal/ciRrThfP6xMpI7GY/images/docs/0228067-settings-platforms-amazon.jpg?fit=max&auto=format&n=ciRrThfP6xMpI7GY&q=85&s=b13a44382021c0eda86d6a9ff7796f13" width="2480" height="1180" data-path="images/docs/0228067-settings-platforms-amazon.jpg" />
    </Frame>

    Paste your Client ID and Client Secret into the fields and click Save.

    <Frame>
      <img src="https://mintcdn.com/onesignal/Z6xkXGfmy814If53/images/docs/d5e8d7e-settings-platforms-amazon-configure.jpg?fit=max&auto=format&n=Z6xkXGfmy814If53&q=85&s=2cbf928c8c4194421d8bbc5cfa68bb17" width="2480" height="1132" data-path="images/docs/d5e8d7e-settings-platforms-amazon-configure.jpg" />
    </Frame>
  </Step>

  <Step title="Creating an Amazon API key">
    The following steps are required to test push notifications before publishing your app to the Amazon App Store.

    Go back to the Amazon Security Profile page for your app, and select the **Android/Kindle Settings** tab.

    Enter any name you like for the **API Key Name**.

    Enter your Android package name. **NOTE**: the package name is case sensitive.

    Enter the MD5 signature of your Android Keystore you used to sign the APK file with. See [Amazon's instructions](https://developer.amazon.com/public/apis/engage/login-with-amazon/docs/android_app_signatures.html) to get this value.

    We recommend not using the default debugging keystore, but if you do, make sure you redo this again with your Production keystore, or let Amazon sign your app for you.

    When you're done, click **Generate New Key**.

    <Frame>
      <img src="https://mintcdn.com/onesignal/6tscVAtiSqz353kV/images/docs/QmpjKGuXTnqb9BSTNyPA_AmazonSecurityProfile6.png?fit=max&auto=format&n=6tscVAtiSqz353kV&q=85&s=08ec7fa49a093ba5da1151c0b2e3d1b8" width="906" height="399" data-path="images/docs/QmpjKGuXTnqb9BSTNyPA_AmazonSecurityProfile6.png" />
    </Frame>

    Copy the **Key** shown in the results and save it into a new file named `api_key.txt`.

    When your app is built, this file needs to be located in `/assets/` in the root of your APK.

    More details on the placement of this file can be found in our [Amazon SDK Setup](./amazon-sdk-setup) documentation.

    <Frame>
      <img src="https://mintcdn.com/onesignal/KSCNwSpBCNSQ8xdF/images/docs/vFkWzWcASaSyBzMlF6ps_AmazonSecurityProfile7.png?fit=max&auto=format&n=KSCNwSpBCNSQ8xdF&q=85&s=84b572223fd92ee102ac1a4bb28a616d" width="910" height="612" data-path="images/docs/vFkWzWcASaSyBzMlF6ps_AmazonSecurityProfile7.png" />
    </Frame>
  </Step>
</Steps>

***

<Check>
  **Done!** You now have a key to send push notifications from your app. 🥳

  Return to the [Amazon SDK Setup](./amazon-sdk-setup) guide to install the OneSignal SDK in your app.
</Check>

***

Built with [Mintlify](https://mintlify.com).
