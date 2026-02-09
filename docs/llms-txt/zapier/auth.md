# Source: https://docs.zapier.com/platform/build/auth.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.zapier.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Authentication

> Connecting an app to Zapier starts with authentication. Users select an app they wish to use in their Zap, authenticating their account with that app to allow Zapier to access their data.

Zapier will have access to the account until the authorization expires, is revoked, or credentials are changed. Zapier will automatically refresh OAuth v2 and session authentications when refresh token functionality is enabled in the integration.

Once users authenticate an app account to Zapier, they can use any of that app's triggers/actions in their Zaps without authenticating again. Users would authenticate another connection if they wish to use additional accounts from an app with Zapier, for example if they have a work and personal account in one app.

Zapier integration builders define how Zapier connects to your app to authenticate users, adding an API call where Zapier tests the account authentication.

All Zapier integrations that can access or add private data for users require authentication. The only apps that don't require authentication include data feeds (such as news or weather updates) or utilities (such as file format conversion tools or public search engines). If you're building an integration for any app that stores private data and requires an account to use, your integration will require authentication.

## Zapier Supported Authentication Schemes

Zapier supports the following five authentication schemes in the Platform UI, each with their own settings:

<CardGroup cols={3}>
  <Card title="API Key" icon="key" href="/platform/build/apikeyauth" horizontal />

  <Card title="OAuth v2" icon="lock" href="/platform/build/oauth" horizontal />

  <Card title="Session Auth" icon="user-clock" href="/platform/build/sessionauth" horizontal />

  <Card title="Basic Auth" icon="user-lock" href="/platform/build/basicauth" horizontal />

  <Card title="Digest Auth" icon="shield-halved" href="/platform/build/digestauth" horizontal />
</CardGroup>

<Frame>
  <img src="https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/37e7829169eb2e07278d512c174cd708.webp?fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=39c1c497e30e7a2c1e6acfeb58170d4d" data-og-width="1660" width="1660" data-og-height="994" height="994" data-path="images/37e7829169eb2e07278d512c174cd708.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/37e7829169eb2e07278d512c174cd708.webp?w=280&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=02eea25bdf9733be0d4968092c456a48 280w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/37e7829169eb2e07278d512c174cd708.webp?w=560&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=d07c05208b33ff23328440c849ab5615 560w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/37e7829169eb2e07278d512c174cd708.webp?w=840&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=24301f9a1f53eb3e439fb99b016b97d1 840w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/37e7829169eb2e07278d512c174cd708.webp?w=1100&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=e0b358820175669eb55d6744039e87de 1100w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/37e7829169eb2e07278d512c174cd708.webp?w=1650&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=24661831f847c93784d69684c14ffb54 1650w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/37e7829169eb2e07278d512c174cd708.webp?w=2500&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=a3d2a45f920185776349a56dcd71a16e 2500w" />

  {" "}
</Frame>

Where possible, OAuth v2 authentication is the preferred scheme to simplify a user's account connection and minimize set up time. During the authentication flow via Zapier, a familiar popup window appears from your app to select their account or log in, then verify the connection. This fits the flow most modern apps use for integration authentication.

API Key authentication is next best. Users must be able to obtain their API key from your app without human intervention. Your integration won't be [approved for publishing](/platform/quickstart/private-vs-public-integrations) if your service requires users to email or call your team in order to receive an API key or access to your API.

Basic authentication, while acceptable, is the least appropriate authentication type to use for a third party service like Zapier, as users must type their account credentials directly into Zapier's UI.

For more custom authentication schemes, switch to the [Platform CLI](/platform/manage/export-cli).

## How to Remove or Change Type of Authentication Scheme

You cannot change an integration's authentication scheme directly. First, remove the existing integration's authentication scheme, then add a new authentication scheme.

> **Note:** You can only do this for a (new) integration version that has not yet been promoted and has less than 5 active users, since this will break connected accounts for the version. If an integration's authentication scheme needs to be changed, clone a new major version and add the new authentication. [Learn more](/platform/manage/versions)

To remove a Zapier integration's authentication scheme in the Platform UI, open the *Authentication* page. Click the gear icon beside the existing authentication scheme, click *Delete*, then confirm to remove the authentication.

<Frame>
  <img src="https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/a616ced2f22bdf0873b0f910fc238424.webp?fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=23b7aafea9fb5d8cd6e38080d1d9132c" data-og-width="1663" width="1663" data-og-height="473" height="473" data-path="images/a616ced2f22bdf0873b0f910fc238424.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/a616ced2f22bdf0873b0f910fc238424.webp?w=280&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=a15aed6e5f90bac2e1a501ee7b042899 280w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/a616ced2f22bdf0873b0f910fc238424.webp?w=560&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=030957afc4a7bf87ec38df375f4a7424 560w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/a616ced2f22bdf0873b0f910fc238424.webp?w=840&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=08bd92d56a86b307eda0713244f72f71 840w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/a616ced2f22bdf0873b0f910fc238424.webp?w=1100&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=3449c9895e6428cffdd5fb4d4fa57586 1100w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/a616ced2f22bdf0873b0f910fc238424.webp?w=1650&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=2208ae5fdf1fe4c25a9d2f70e86bcd4a 1650w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/a616ced2f22bdf0873b0f910fc238424.webp?w=2500&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=1e2e9b75dcf368e20ec293c64c02063a 2500w" />

  {" "}
</Frame>

Then add your app's new authentication scheme to the Zapier integration instead.

> **Note:** Again, to not break connected accounts, you can normally not migrate existing users' Zaps and connected accounts to a new version that has a different authentication scheme. For public integrations that meet certain conditions, we can provide support to migrate connected accounts between authentication schemes. [Learn more](/platform/manage/auth-scheme)

## Common Authentication Error Messages

When the test API call to verify users' credentials is unsuccessful, an error message shows in the Test section of your Zapier integration. Zapier shows a simplified error message in the *Response* tab by default.

<Frame>
  <img src="https://mintcdn.com/zapier-82f0e938/FKPl8SjhZXHXKd0_/images/f6e4616d8e457f2ccf8dd872b2a15aac.webp?fit=max&auto=format&n=FKPl8SjhZXHXKd0_&q=85&s=a1b0f0c7beb2e917d0cc4056cc9870dd" data-og-width="1111" width="1111" data-og-height="271" height="271" data-path="images/f6e4616d8e457f2ccf8dd872b2a15aac.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/FKPl8SjhZXHXKd0_/images/f6e4616d8e457f2ccf8dd872b2a15aac.webp?w=280&fit=max&auto=format&n=FKPl8SjhZXHXKd0_&q=85&s=ba2c362c3c4f1404ca648e7d21457315 280w, https://mintcdn.com/zapier-82f0e938/FKPl8SjhZXHXKd0_/images/f6e4616d8e457f2ccf8dd872b2a15aac.webp?w=560&fit=max&auto=format&n=FKPl8SjhZXHXKd0_&q=85&s=a562778565155fcc15f51a05ce526565 560w, https://mintcdn.com/zapier-82f0e938/FKPl8SjhZXHXKd0_/images/f6e4616d8e457f2ccf8dd872b2a15aac.webp?w=840&fit=max&auto=format&n=FKPl8SjhZXHXKd0_&q=85&s=ecb4ec9a8f18a10cab99beadcbcdfff7 840w, https://mintcdn.com/zapier-82f0e938/FKPl8SjhZXHXKd0_/images/f6e4616d8e457f2ccf8dd872b2a15aac.webp?w=1100&fit=max&auto=format&n=FKPl8SjhZXHXKd0_&q=85&s=5292da66a17474bf9c65ccb65bab13d4 1100w, https://mintcdn.com/zapier-82f0e938/FKPl8SjhZXHXKd0_/images/f6e4616d8e457f2ccf8dd872b2a15aac.webp?w=1650&fit=max&auto=format&n=FKPl8SjhZXHXKd0_&q=85&s=e2a758b2bc658163e80bdac496dfd7b5 1650w, https://mintcdn.com/zapier-82f0e938/FKPl8SjhZXHXKd0_/images/f6e4616d8e457f2ccf8dd872b2a15aac.webp?w=2500&fit=max&auto=format&n=FKPl8SjhZXHXKd0_&q=85&s=be78c3ff018f5cddb72b7addd8366f94 2500w" />

  {" "}
</Frame>

The original API response with the full error message is shown in the *HTTP* tab under *Response Content*.

<Frame>
  <img src="https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/2598ca338518d55cb41cebc2116bd1af.webp?fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=1b1a35f0c4389076917fe1df345aeedd" data-og-width="1101" width="1101" data-og-height="905" height="905" data-path="images/2598ca338518d55cb41cebc2116bd1af.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/2598ca338518d55cb41cebc2116bd1af.webp?w=280&fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=a1d1ffac2fd3d3e214997853e14daf41 280w, https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/2598ca338518d55cb41cebc2116bd1af.webp?w=560&fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=bfbe8a16daac7d2eed30b8fcafb4da08 560w, https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/2598ca338518d55cb41cebc2116bd1af.webp?w=840&fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=02802d42f5e523ed25bb6e66a553cf2f 840w, https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/2598ca338518d55cb41cebc2116bd1af.webp?w=1100&fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=111f08833b68b8f632a0ab66fe79e7a0 1100w, https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/2598ca338518d55cb41cebc2116bd1af.webp?w=1650&fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=1cab6cf9d6beae4c1e9bf432bb1a54d6 1650w, https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/2598ca338518d55cb41cebc2116bd1af.webp?w=2500&fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=e173110426edeb79b47adbc041cb00fc 2500w" />

  {" "}
</Frame>

The most common errors include:

### 404

The standard HTTP 404 `Not Found` error is commonly returned when:

* Test API endpoint URL is incorrect
* Test API call method is incorrect
  <Frame>
    <img src="https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/4b268ddfa326ee23cb902d05acc6ac10.webp?fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=7ac89a2a066b1b2de1a91b61305f4c67" data-og-width="1103" width="1103" data-og-height="259" height="259" data-path="images/4b268ddfa326ee23cb902d05acc6ac10.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/4b268ddfa326ee23cb902d05acc6ac10.webp?w=280&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=0ad04353b7180ba81fac0c4c3f9953a9 280w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/4b268ddfa326ee23cb902d05acc6ac10.webp?w=560&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=439fa3ac45e18335307234efbb96140c 560w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/4b268ddfa326ee23cb902d05acc6ac10.webp?w=840&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=032fd7858e0cccf915d3c40bf34c9178 840w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/4b268ddfa326ee23cb902d05acc6ac10.webp?w=1100&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=a774341cad414d8778038840b9906ff7 1100w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/4b268ddfa326ee23cb902d05acc6ac10.webp?w=1650&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=5c01377704315e8ac0a798bebedee89a 1650w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/4b268ddfa326ee23cb902d05acc6ac10.webp?w=2500&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=3335e054eb86b0285c9dee0121db9c0c 2500w" />

    {" "}
  </Frame>

Verify both the API endpoint URL and the call method (typically `GET`). Ensure both are set to what your API expects, then click the *Save & Continue* button, and click the *Test Connected Account* button again.

### 401 or 403

The standard HTTP 401 `Unauthorized` or HTTP 403 `Forbidden` error is commonly returned when:

* User account credentials are incorrect, expired, or revoked

Try authenticating your app user account with Zapier again. Click *Connect an Account*, add credentials for an active account on the app, then try the test again.

<Frame>
  <img src="https://mintcdn.com/zapier-82f0e938/FKPl8SjhZXHXKd0_/images/e8dd16ccd395d9c466d81ce669510296.webp?fit=max&auto=format&n=FKPl8SjhZXHXKd0_&q=85&s=695cfe97d25783afa5ff2339c9599959" data-og-width="1102" width="1102" data-og-height="259" height="259" data-path="images/e8dd16ccd395d9c466d81ce669510296.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/FKPl8SjhZXHXKd0_/images/e8dd16ccd395d9c466d81ce669510296.webp?w=280&fit=max&auto=format&n=FKPl8SjhZXHXKd0_&q=85&s=88a8fbc6913c1f0efce8e738df08930b 280w, https://mintcdn.com/zapier-82f0e938/FKPl8SjhZXHXKd0_/images/e8dd16ccd395d9c466d81ce669510296.webp?w=560&fit=max&auto=format&n=FKPl8SjhZXHXKd0_&q=85&s=ca0e2802a020a5fd6243828f5cd2547a 560w, https://mintcdn.com/zapier-82f0e938/FKPl8SjhZXHXKd0_/images/e8dd16ccd395d9c466d81ce669510296.webp?w=840&fit=max&auto=format&n=FKPl8SjhZXHXKd0_&q=85&s=3b72f947ef712fde7c9dfdf098f7fd16 840w, https://mintcdn.com/zapier-82f0e938/FKPl8SjhZXHXKd0_/images/e8dd16ccd395d9c466d81ce669510296.webp?w=1100&fit=max&auto=format&n=FKPl8SjhZXHXKd0_&q=85&s=4bab41c436f8f58512334d54dd380259 1100w, https://mintcdn.com/zapier-82f0e938/FKPl8SjhZXHXKd0_/images/e8dd16ccd395d9c466d81ce669510296.webp?w=1650&fit=max&auto=format&n=FKPl8SjhZXHXKd0_&q=85&s=3dd7190b6e688ea1854bf76d70ebe064 1650w, https://mintcdn.com/zapier-82f0e938/FKPl8SjhZXHXKd0_/images/e8dd16ccd395d9c466d81ce669510296.webp?w=2500&fit=max&auto=format&n=FKPl8SjhZXHXKd0_&q=85&s=6e24eb09811d5b01b3f6337ba2eaa9bf 2500w" />

  {" "}
</Frame>

### 400

The standard HTTP 400 `Bad Request` error is often returned when:

* OAuth v2 Client ID and/or Secret are incorrect or expired
* Some other part of your request is malformed, particularly a token exchange request

Check the full error message from the error or Zapier's testing logs to see if it lists why the call failed, then correct that part of your authentication flow. Verify each part of your authentication flow is entered correctly, including the request headers, URL parameters, and request body for each part of your authentication flow.

<Frame>
  <img src="https://cdn.zapier.com/storage/photos/91579ed613b77fb803ff52fb900b093b.png" />

  {" "}
</Frame>

### Error Parsing Response

The *Error Parsing Response* error is commonly returned when:

* API returns non-standard and especially non-JSON output
* Test API endpoint URL is incorrect
  <Frame>
    <img src="https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/7dc661d47076c1114b2581289646de48.webp?fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=ef08506ec833e958710bca9a3583164c" data-og-width="1102" width="1102" data-og-height="279" height="279" data-path="images/7dc661d47076c1114b2581289646de48.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/7dc661d47076c1114b2581289646de48.webp?w=280&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=ec3c083b88a698a560bf1bed1abbba9f 280w, https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/7dc661d47076c1114b2581289646de48.webp?w=560&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=81bbdd0a6647559192a2395660b527ed 560w, https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/7dc661d47076c1114b2581289646de48.webp?w=840&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=27b25e10602fb237237f118c3c032d10 840w, https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/7dc661d47076c1114b2581289646de48.webp?w=1100&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=268bc865bbdbb2c6cc032e80cf21c2de 1100w, https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/7dc661d47076c1114b2581289646de48.webp?w=1650&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=b55067c8a00695f5e1da6f499d81e427 1650w, https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/7dc661d47076c1114b2581289646de48.webp?w=2500&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=5d1e26af49ed4f8dc949fb86de501f8a 2500w" />

    {" "}
  </Frame>

Verify the test API URL is entered correctly. If a normal webpage URL is entered in the test field, the site will return its raw HTML content to Zapier and that will likely result in this error. If you do change the URL, click *Save & Continue*, then test your connection again.

If your API call is correct and returning data in a format [Zapier does not expect](/platform/build/response-types), you will need to switch to [Code mode](/platform/build/code-mode) and add custom parsing for your API response. Under the *Test* API call in the top of your app's Authentication settings, click *Switch to Code Mode*, then add custom JavaScript code to parse your API response.

### Authentication Failed Task Timed Out

The *Authentication Failed* error, often including *Task Timed Out*, is commonly returned when:

* The API request does not return a response to Zapier within 30 seconds
* The API request is formatted incorrectly and the server does not respond with an error code

Check your Zapier test logs to see if it shows which URL timed out, then verify you've entered the correct URL in all of your integration authentication settings. Finally, check the API provider to see if their site or API are temporarily down.

If the request seems to be successful but the task still times out, your API call may be taking too long to respond, or could be returning more data than Zapier can parse within the time limit. Use a testing API call in authentication that returns as little data as possible, such as a `/me` call that returns the connected user's account data. Or, if your API supports pagination and/or filtering, enable that and have the API return only the most recent result. Then test again to ensure the call works successfully.

<Frame>
  <img src="https://cdn.zapier.com/storage/photos/2bc7541d4859785d23a64dc5caceec22.png" />

  {" "}
</Frame>

### 500

The HTTP 500 error is the default, unformatted error that may be returned without specifying what went wrong or why. If you encounter this error, check the API endpoint URL that gave the error, and verify your API call is configured correctly with the expected URL params, HTTP headers, and Request Body.

<Frame>
  <img src="https://cdn.zapier.com/storage/photos/22eb6cbc2c965dc196a3646511deeb7d.png" />

  {" "}
</Frame>

***

*Need help? [Tell us about your problem](https://developer.zapier.com/contact) and we'll connect you with the right resource or contact support.*
