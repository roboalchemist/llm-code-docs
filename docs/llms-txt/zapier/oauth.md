# Source: https://docs.zapier.com/platform/build/oauth.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.zapier.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Add authentication with OAuth v2

> OAuth v2 authentication matches in appearance the login process users expect from most modern apps.

The user interaction with authenticating Zapier typically takes place in full on the app's own site, helping users easily connect accounts without needing to share account credentials or look up API keys.

<Frame>
  <img src="https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/520541acfeeb0e0a812944e599852756.webp?fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=8d854417e8a740bd42ba22258303fe9c" data-og-width="793" width="793" data-og-height="547" height="547" data-path="images/520541acfeeb0e0a812944e599852756.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/520541acfeeb0e0a812944e599852756.webp?w=280&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=41ca9bb9e4a4fa27683242e6c16d3f54 280w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/520541acfeeb0e0a812944e599852756.webp?w=560&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=aef8f179556ba3859bc7a71d8414ad51 560w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/520541acfeeb0e0a812944e599852756.webp?w=840&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=03e07484b5bc076059718e887aeb18bd 840w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/520541acfeeb0e0a812944e599852756.webp?w=1100&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=dd82df0fecc21be7ef2a2ad65f6b3ac0 1100w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/520541acfeeb0e0a812944e599852756.webp?w=1650&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=afd8390a0e915d7dae98f07b335d1106 1650w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/520541acfeeb0e0a812944e599852756.webp?w=2500&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=28ec1d61b83a20e729ad52a27e3bce69 2500w" />
</Frame>

The user will see a familar window from your app showing either a login screen or if they're already logged in, an account selector where they don't need to enter credentials. Once they authorize Zapier access, the app will return an access token that Zapier uses in future API calls.

Zapier implements the “Authorization Code” [grant type](https://tools.ietf.org/html/rfc6749#section-1.3.1) when you choose OAuth v2 in the Platform UI. If your OAuth v2 implementation supports refresh tokens, you can optionally configure a “Refresh Token” [request](https://tools.ietf.org/html/rfc6749#section-1.5).

Platform UI does not currently support other grant types. If your integration requires a different OAuth v2 grant type, you'll need to use another supported authorization type with Zapier such as [Session](/platform/build/sessionauth) or [API Key](/platform/build/apikeyauth).

If your integration requires OAuth v1 authentication, use the [Platform CLI](/platform/quickstart/cli-tutorial) instead of Platform UI.

## 1. Configure the OAuth v2 components

* Open the *Authentication* tab in Zapier visual builder and select *OAuth v2*.

<Frame>
  <img src="https://mintcdn.com/zapier-82f0e938/FKPl8SjhZXHXKd0_/images/e89518edce251293ff42ae0f186c0efb.webp?fit=max&auto=format&n=FKPl8SjhZXHXKd0_&q=85&s=e4b77bf922e99ab59643af05ae2e6a37" data-og-width="1660" width="1660" data-og-height="990" height="990" data-path="images/e89518edce251293ff42ae0f186c0efb.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/FKPl8SjhZXHXKd0_/images/e89518edce251293ff42ae0f186c0efb.webp?w=280&fit=max&auto=format&n=FKPl8SjhZXHXKd0_&q=85&s=ec7620bdb484c62e6ccb63779f17bf03 280w, https://mintcdn.com/zapier-82f0e938/FKPl8SjhZXHXKd0_/images/e89518edce251293ff42ae0f186c0efb.webp?w=560&fit=max&auto=format&n=FKPl8SjhZXHXKd0_&q=85&s=cd2b9e7f33f5360d120fcbdccbbe521b 560w, https://mintcdn.com/zapier-82f0e938/FKPl8SjhZXHXKd0_/images/e89518edce251293ff42ae0f186c0efb.webp?w=840&fit=max&auto=format&n=FKPl8SjhZXHXKd0_&q=85&s=a0b63cc0fac8264aaa83883f02d35375 840w, https://mintcdn.com/zapier-82f0e938/FKPl8SjhZXHXKd0_/images/e89518edce251293ff42ae0f186c0efb.webp?w=1100&fit=max&auto=format&n=FKPl8SjhZXHXKd0_&q=85&s=b6f92e2a5d814bde7db2ae2f28626dd0 1100w, https://mintcdn.com/zapier-82f0e938/FKPl8SjhZXHXKd0_/images/e89518edce251293ff42ae0f186c0efb.webp?w=1650&fit=max&auto=format&n=FKPl8SjhZXHXKd0_&q=85&s=419da8dfb1e8717cf3838794578995e0 1650w, https://mintcdn.com/zapier-82f0e938/FKPl8SjhZXHXKd0_/images/e89518edce251293ff42ae0f186c0efb.webp?w=2500&fit=max&auto=format&n=FKPl8SjhZXHXKd0_&q=85&s=f95e6301ba16136593959a537aafd228 2500w" />
</Frame>

### Optional input form

* Most apps with OAuth v2 authentication do not need an input form. If your API requires data from the user before displaying the authorization URL, or requires URL details to create the authorization URL; such as account team name or site URL for self-hosted apps, or you need to store fields received from your server to use in subsequent API calls - you'll need an input form.

* Add those additional fields by selecting *Add Fields* and fill in the details for any field requiring user input. This will show a form to users with the fields you've added before redirecting them to your authorization URL.

<Frame>
  <img src="https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/3603f9715129250a93ecfcf78d4b5f17.webp?fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=16a4d4f4a2bf007e01f04e39b7558d7f" data-og-width="801" width="801" data-og-height="943" height="943" data-path="images/3603f9715129250a93ecfcf78d4b5f17.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/3603f9715129250a93ecfcf78d4b5f17.webp?w=280&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=d93fdf6bb914a8592bdd0fd2ff4523e4 280w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/3603f9715129250a93ecfcf78d4b5f17.webp?w=560&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=a509159672c9f93858c41106c85c8928 560w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/3603f9715129250a93ecfcf78d4b5f17.webp?w=840&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=9453bfb7723673889bbc7ec0d283e375 840w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/3603f9715129250a93ecfcf78d4b5f17.webp?w=1100&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=8c8f126ea0600df8f18fecfd06467356 1100w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/3603f9715129250a93ecfcf78d4b5f17.webp?w=1650&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=30b354f0a58caafe4bb5c5d4e311054f 1650w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/3603f9715129250a93ecfcf78d4b5f17.webp?w=2500&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=133113198caf8c3506d7118b7f18e525 2500w" />
</Frame>

* Two types of fields are available when building an OAuth v2 input form. Standard Fields, work much like other form fields with Zapier's [input form](/platform/build/field-definitions) in triggers and actions. [Computed Fields](/platform/build/computed-fields) make sure specific fields are returned by your app's authentication API call response.

* For standard fields to be input by the user, select the default *Field* type. Add the most commonly needed fields first, in the order users expect, as you cannot reorder fields once added. Fill in the options as appropriate:

– **Key**: The internal name for your field, used to reference this field in Zapier API calls. For convenience, use the same key as your API uses for this field. Note: `client_id` and `client_secret` are reserved and cannot be used as keys for input form fields.

– **Label**: A human-friendly name for this field that will be shown to users in the authentication form.

– **Required? (checkbox)**: Check if this field is required for successful authentication.

– **Type**: All input fields use the `string` text field by default; select `password` instead if you would like to obscure the data as users enter it.

– **Help Text**: Include details to assist users in authenticating with your app, especially if they may be unsure where to find the data needed within your app. Format text with [Markdown](https://zapier.com/blog/beginner-ultimate-guide-markdown/), and include a hyperlink if needed.

– **Input Format**: (optional) Help users figure out exactly what piece of data you need them to enter. For example, for [a subdomain](/platform/build/subdomain-validation), [https://.yourdomain.com/](https://.yourdomain.com/).

– **Default Value**: Include a value for this field to be used as a fallback. For optional fields, the default value is set on initial connection creation and used in the API call instead of missing or null values every time the Zap runs. For required fields, this value is used during connection creation, but not when the Zap runs (Zapier raises an error for missing/null values instead).

* Input fields marked as password and all authentication fields with sensitive, private data such as both username and password from OAuth v2 are automatically censored at runtime. These values are stored in the Auth bundle and used in API calls, but are replaced in Zapier's logs with a censored value like this `:censored:6:82a3be9927:`. Due to this, it is not possible to view the exact tokens or keys in Zapier's logs. To verify that the same token as was returned by the authentication, is being used in subsequent API calls; you can compare censored value characters, for example `:censored:6:82a3be9927:` would have the same value ending in 9927 when used in a subsequent call.

* Each input field is listed with its label, key, type, and required status in your authentication settings. Click the field to edit it, or click the gear icon and select *Delete* to remove a field.

<Frame>
  <img src="https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/573a3eb19a884c44fd67b9fa421c3bf4.webp?fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=7d77c58be665b908cc11ba28ce254e6c" data-og-width="1661" width="1661" data-og-height="831" height="831" data-path="images/573a3eb19a884c44fd67b9fa421c3bf4.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/573a3eb19a884c44fd67b9fa421c3bf4.webp?w=280&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=192e251bc9eac88d52825ada905efbf8 280w, https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/573a3eb19a884c44fd67b9fa421c3bf4.webp?w=560&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=41fdcb1646d53e372674cc1d213df4e7 560w, https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/573a3eb19a884c44fd67b9fa421c3bf4.webp?w=840&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=3be67df472e84c135d4d606f707db3fb 840w, https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/573a3eb19a884c44fd67b9fa421c3bf4.webp?w=1100&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=f6e4e765b67db7abdfbdf190175d9746 1100w, https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/573a3eb19a884c44fd67b9fa421c3bf4.webp?w=1650&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=04fec4258fc45c1987426186437a5dbf 1650w, https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/573a3eb19a884c44fd67b9fa421c3bf4.webp?w=2500&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=26adb2cacbf9c46a4899561759efb039 2500w" />
</Frame>

* For computed fields, available in OAuth v2 and Session Auth only, review [computed fields documentation](/platform/build/computed-fields).

### OAuth Redirect URL

* Open your app's application, integration, or API settings, and add a new application for your OAuth integration with Zapier. From the Zapier Platform UI's Authentication *Copy your OAuth Redirect URL* section, copy the OAuth Redirect URL and add it to your application's integration settings.
  <Frame>
    <img src="https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/b3e6b9ca7657ba02e4864ec28ab74951.webp?fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=327cb7285b5fa41793a7e1a296e5a002" data-og-width="1205" width="1205" data-og-height="294" height="294" data-path="images/b3e6b9ca7657ba02e4864ec28ab74951.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/b3e6b9ca7657ba02e4864ec28ab74951.webp?w=280&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=3c42b2d8448d737e6beb494b6fd77ad0 280w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/b3e6b9ca7657ba02e4864ec28ab74951.webp?w=560&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=efb56235eb5e5d4a52ea197564f2375e 560w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/b3e6b9ca7657ba02e4864ec28ab74951.webp?w=840&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=9b74842eb93cf740426f32fd271a1ce3 840w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/b3e6b9ca7657ba02e4864ec28ab74951.webp?w=1100&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=47b009b7d1006ce8ab696a8b41adb47e 1100w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/b3e6b9ca7657ba02e4864ec28ab74951.webp?w=1650&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=17ca9667056e5abc9aeb905816e6d3d6 1650w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/b3e6b9ca7657ba02e4864ec28ab74951.webp?w=2500&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=b66c47e343ecdc498748b1cd283021b0 2500w" />
  </Frame>
* To reference the redirect URL inside your Zapier integration, use the following code:

`{{bundle.inputData.redirect_uri}}`

### Add PKCE Support

* Zapier provides built-in support for [PKCE](https://oauth.net/2/pkce/#credentials) (Proof Key for Code Exchange and pronounced “pick-see”), an extension to the authorization code flow that adds a layer of protection against security vulnerabilities. The code generation and exchange steps of the flow occur automatically by Zapier when enabled.
  <Frame>
    <img src="https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/124a3c00d8bc37dadd953f19451205a5.webp?fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=f17deca63b9d3475bb124a7d0f094fd0" data-og-width="841" width="841" data-og-height="484" height="484" data-path="images/124a3c00d8bc37dadd953f19451205a5.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/124a3c00d8bc37dadd953f19451205a5.webp?w=280&fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=97cc8e2eacfe0ea8c2be154e0ad6a041 280w, https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/124a3c00d8bc37dadd953f19451205a5.webp?w=560&fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=5df22f97bb371c938280517778431d6e 560w, https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/124a3c00d8bc37dadd953f19451205a5.webp?w=840&fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=ce5a986825978bb14691127319a5405c 840w, https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/124a3c00d8bc37dadd953f19451205a5.webp?w=1100&fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=cea87be029c132b3eb688a0b6484a73d 1100w, https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/124a3c00d8bc37dadd953f19451205a5.webp?w=1650&fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=5cb91a3754471b41a8f44cfd01656ea1 1650w, https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/124a3c00d8bc37dadd953f19451205a5.webp?w=2500&fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=ab53430ce9923fa89ecb7a8cb9bdf5e5 2500w" />
  </Frame>

### Add Application Credentials to Zapier

* In your application's settings, you'll receive credentials that Zapier will use to verify itself to your app — typically called a *Client ID* and *Client Secret*, though they may have a slightly different name. Copy that data from your app, then in Step 3 of your Zapier OAuth configuration, paste those items in their respective fields. Zapier will use that data along with the authorization URL to receive the request token.

  <Frame>
    <img src="https://mintcdn.com/zapier-82f0e938/2ebL4bG5uJP5JVc0/images/ba093465f009bf6b417d55b2166c4324.webp?fit=max&auto=format&n=2ebL4bG5uJP5JVc0&q=85&s=a3acc0b0c06b5573d6105eadfc003b47" data-og-width="1138" width="1138" data-og-height="452" height="452" data-path="images/ba093465f009bf6b417d55b2166c4324.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/2ebL4bG5uJP5JVc0/images/ba093465f009bf6b417d55b2166c4324.webp?w=280&fit=max&auto=format&n=2ebL4bG5uJP5JVc0&q=85&s=d190b5898e04aead975a5ef98a532dec 280w, https://mintcdn.com/zapier-82f0e938/2ebL4bG5uJP5JVc0/images/ba093465f009bf6b417d55b2166c4324.webp?w=560&fit=max&auto=format&n=2ebL4bG5uJP5JVc0&q=85&s=98a57e5c8730533d7419f9c7c38c9d29 560w, https://mintcdn.com/zapier-82f0e938/2ebL4bG5uJP5JVc0/images/ba093465f009bf6b417d55b2166c4324.webp?w=840&fit=max&auto=format&n=2ebL4bG5uJP5JVc0&q=85&s=8c4c930f267acbbd46d38b3c33a7ca45 840w, https://mintcdn.com/zapier-82f0e938/2ebL4bG5uJP5JVc0/images/ba093465f009bf6b417d55b2166c4324.webp?w=1100&fit=max&auto=format&n=2ebL4bG5uJP5JVc0&q=85&s=9a4b24c5c3772b2e088d8642a63a4fe9 1100w, https://mintcdn.com/zapier-82f0e938/2ebL4bG5uJP5JVc0/images/ba093465f009bf6b417d55b2166c4324.webp?w=1650&fit=max&auto=format&n=2ebL4bG5uJP5JVc0&q=85&s=b90bcab8b18d6cab87d6eb3d3b7d70f1 1650w, https://mintcdn.com/zapier-82f0e938/2ebL4bG5uJP5JVc0/images/ba093465f009bf6b417d55b2166c4324.webp?w=2500&fit=max&auto=format&n=2ebL4bG5uJP5JVc0&q=85&s=d49a5e8fc397098ee8ae03c13a138f2a 2500w" />
  </Frame>

* Click *Save & Continue* to save your progress so far.

* Zapier automatically includes the Client ID and Secret in authentication API calls, but if you need to reference them in your integration's API calls or custom code, use the following codes: – Client Secret: `{{process.env.CLIENT_SECRET}}` – Client ID: `{{process.env.CLIENT_ID}}`

### Add OAuth Endpoint Configuration

* Add your application's Authorization URL, where Zapier will redirect users to authenticate with your app. Copy this URL from your application or integration settings where you copied the client ID and secret previously, or from your app's API page.
  <Frame>
    <img src="https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/1920c552acfc0cc03089feb2e9ada029.webp?fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=c0d921615a3d14056db8ce392491a8d2" data-og-width="1187" width="1187" data-og-height="618" height="618" data-path="images/1920c552acfc0cc03089feb2e9ada029.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/1920c552acfc0cc03089feb2e9ada029.webp?w=280&fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=0c10931348fae4f5527d56f14189e5d6 280w, https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/1920c552acfc0cc03089feb2e9ada029.webp?w=560&fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=7b29f958f2a7e1dfc517f9443aa640c8 560w, https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/1920c552acfc0cc03089feb2e9ada029.webp?w=840&fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=8090b1d5acfbff0adcc0b13e30ed98d3 840w, https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/1920c552acfc0cc03089feb2e9ada029.webp?w=1100&fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=68e9a35669a03a04fc92bbb0ebe7b79e 1100w, https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/1920c552acfc0cc03089feb2e9ada029.webp?w=1650&fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=4151e6db539c55a6c5ceb2981b65ad57 1650w, https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/1920c552acfc0cc03089feb2e9ada029.webp?w=2500&fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=1590e4aa25dd4dc9b0e9e42adefbf36b 2500w" />
  </Frame>
* By default, Zapier will pass the client ID, state, redirect URI, and a standard `code` response type as URL Params in the request to the authorization url. If you need to change that, click the *Show Options* button and add any additional call details needed.

> **Note**: The Oauth2 `state` param is a [standard security feature](https://auth0.com/docs/secure/attack-protection/state-parameters) that helps ensure that authorization requests are only coming from your servers. Most Oauth clients have support for this and will send back the `state` query param that the user brings to your app. The Zapier Platform performs this check and this required field cannot be disabled. The state parameter is automatically generated by Zapier in the background, and can be accessed at `bundle.inputData.state`. Since Zapier uses the `state` to verify that GET requests to your redirect URL truly come from your app, it needs to be generated by Zapier so that it can be validated later (once the user confirms that they'd like to grant Zapier permission to access their account in your app).

* To optionally limit Zapier's scope to let it only access specific data from your app, add OAuth scopes in the *Scope* field with a comma- or space-separated list.

* Add your app's Access Token Request URL from your API documentation, typically with a `POST` call.

<Frame>
  <img src="https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/517f20c1a33012af96b18036332371eb.webp?fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=e040531b66f2bcbd2590eb3eb5a659ff" data-og-width="1201" width="1201" data-og-height="672" height="672" data-path="images/517f20c1a33012af96b18036332371eb.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/517f20c1a33012af96b18036332371eb.webp?w=280&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=2a7c5385476ba0b668f1907257b68df3 280w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/517f20c1a33012af96b18036332371eb.webp?w=560&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=46c97ce5d45a2c800eda2806e8e1060e 560w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/517f20c1a33012af96b18036332371eb.webp?w=840&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=4b0145dbe555375706a955fa2db5fe9a 840w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/517f20c1a33012af96b18036332371eb.webp?w=1100&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=ed87b04161b37ba1d909ffc8ed06696f 1100w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/517f20c1a33012af96b18036332371eb.webp?w=1650&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=502199d730a492409939989d763f031d 1650w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/517f20c1a33012af96b18036332371eb.webp?w=2500&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=d48c709951c5659a585c3d4a57d63233 2500w" />
</Frame>

* By default, Zapier will pass the client ID, client secret, authorization code, redirect URI, and a standard `authorization_code` grant type in the API request body with the access token request. If you need to change that, click the *Show Options* button and add any additional call details needed.

* If your API supports automated token refresh, add your API's Refresh Token Request URL, and check the *Automatically Refresh Token* box. This enables users' Zaps to run in the background without interruptions as long as possible by refreshing expired access tokens automatically.

* If your Access Token and Refresh Token requests don't return the tokens at the top level, use [Code Mode](/platform/build/code-mode) to modify the response so that the tokens are available at the top level. It is not possible to store an object with nested keys from the response.

* Zapier will automatically include the access token in subsequent API requests, but if you need to manually add it, the access token is stored in the `authData` bundle and can be referenced with `{{bundle.authData.access_token}}` or `{{bundle.authData.accessToken}}`, depending on how your API's response references the access token.

## 2. Add a Test API Request

* Add an API call to your API that requires no configuration, typically a `/user` or `/me` call. Add the URL for the API call, and set the call type, typically a `GET`. This will test the user-entered credentials to ensure it enables a successful API call to your app.
  <Frame>
    <img src="https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/48cdb444eab9a329023b3e991bfa0da9.webp?fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=f123d333790ad9bafbca2658497de4b2" data-og-width="1191" width="1191" data-og-height="643" height="643" data-path="images/48cdb444eab9a329023b3e991bfa0da9.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/48cdb444eab9a329023b3e991bfa0da9.webp?w=280&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=fd9535058ad7a82a0878db14b11f7cc7 280w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/48cdb444eab9a329023b3e991bfa0da9.webp?w=560&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=638f99b24ab97a5e88c6a2ad49f88c03 560w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/48cdb444eab9a329023b3e991bfa0da9.webp?w=840&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=3b30d037a93cfffdb458a6ec8914ff9c 840w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/48cdb444eab9a329023b3e991bfa0da9.webp?w=1100&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=7be560211ce323c45f6d234369299a62 1100w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/48cdb444eab9a329023b3e991bfa0da9.webp?w=1650&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=3dbd63fd314f7e61f3d48feb4a2d53ef 1650w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/48cdb444eab9a329023b3e991bfa0da9.webp?w=2500&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=8af82a06048b821fdf7e6fff1efe1816 2500w" />
  </Frame>

* The access token is included with the API call by default, as it will with all subsequent API calls, but if your API requires any additional configuration, click the *Show Options* button and add any options needed for a successful API call.

  <Frame>
    <img src="https://mintcdn.com/zapier-82f0e938/FKPl8SjhZXHXKd0_/images/f9d47ff9bd4af168dcb4c4811a1e184d.webp?fit=max&auto=format&n=FKPl8SjhZXHXKd0_&q=85&s=3015fe558fb79410b99eaaa16e75bbed" data-og-width="1192" width="1192" data-og-height="548" height="548" data-path="images/f9d47ff9bd4af168dcb4c4811a1e184d.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/FKPl8SjhZXHXKd0_/images/f9d47ff9bd4af168dcb4c4811a1e184d.webp?w=280&fit=max&auto=format&n=FKPl8SjhZXHXKd0_&q=85&s=129e90ba6e196fed8bf6e30d1ee3e326 280w, https://mintcdn.com/zapier-82f0e938/FKPl8SjhZXHXKd0_/images/f9d47ff9bd4af168dcb4c4811a1e184d.webp?w=560&fit=max&auto=format&n=FKPl8SjhZXHXKd0_&q=85&s=b5b57fcd1e74bac9c431890a036563fa 560w, https://mintcdn.com/zapier-82f0e938/FKPl8SjhZXHXKd0_/images/f9d47ff9bd4af168dcb4c4811a1e184d.webp?w=840&fit=max&auto=format&n=FKPl8SjhZXHXKd0_&q=85&s=f5da9ad32c240aae479454cd7793f402 840w, https://mintcdn.com/zapier-82f0e938/FKPl8SjhZXHXKd0_/images/f9d47ff9bd4af168dcb4c4811a1e184d.webp?w=1100&fit=max&auto=format&n=FKPl8SjhZXHXKd0_&q=85&s=4a8444669dbd01741d553c9a5b03f7c4 1100w, https://mintcdn.com/zapier-82f0e938/FKPl8SjhZXHXKd0_/images/f9d47ff9bd4af168dcb4c4811a1e184d.webp?w=1650&fit=max&auto=format&n=FKPl8SjhZXHXKd0_&q=85&s=749625c0a59f44701f50bab38f3f0e15 1650w, https://mintcdn.com/zapier-82f0e938/FKPl8SjhZXHXKd0_/images/f9d47ff9bd4af168dcb4c4811a1e184d.webp?w=2500&fit=max&auto=format&n=FKPl8SjhZXHXKd0_&q=85&s=8373e1a03b523aa3436c73fb37795f29 2500w" />
  </Frame>

* To customize the test API request, select *Switch to Code Mode* and write custom JavaScript code to handle your test API call and the response parsing as needed. The first time you click the toggle, Zapier will [convert your API call to code](/platform/build/code-mode). If you switch back to Form Mode though, Zapier will not convert your code changes to the Form Mode, nor will any subsequent changes in the form be added to your code.

## 3. Configure a Connection Label

Review [connection label documentation](/platform/build/connection-label) to optionally differentiate the app accounts users connect.

## 4. Test your authentication

Connect a valid user account to [test authentication](/platform/build/test-auth).

## Video Tutorial

You can also refer to this video on implementing OAuth v2 in your Zapier integration:

<video controls src="https://cdn.zappy.app/29ccff3273d1ae57e276f7acc44d1cfc.mp4" />

***

*Need help? [Tell us about your problem](https://developer.zapier.com/contact) and we'll connect you with the right resource or contact support.*
