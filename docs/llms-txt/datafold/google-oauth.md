# Source: https://docs.datafold.com/security/single-sign-on/google-oauth.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.datafold.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Google OAuth

<Info>
  **NOTE**

  Google SSO is available for both SaaS and VPC installations of Datafold.
</Info>

## Datafold SaaS

For Datafold SaaS the setup only involves enabling Google SSO integration.

If Google SSO is already enabled for your organization you will see it in the **Settings** → **Integrations** → **SSO**.

<Frame>
  <img src="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/google_oauth_list-5b0c84c5bdddde31c6e82cce055ba758.png?fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=e7bb80685a41723dfa3c34b3b1d7a805" data-og-width="2658" width="2658" data-og-height="680" height="680" data-path="images/google_oauth_list-5b0c84c5bdddde31c6e82cce055ba758.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/google_oauth_list-5b0c84c5bdddde31c6e82cce055ba758.png?w=280&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=f51be9cc7fef460deba05481652f7192 280w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/google_oauth_list-5b0c84c5bdddde31c6e82cce055ba758.png?w=560&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=c2d390e4ebb466aa3741d6c8bd58c003 560w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/google_oauth_list-5b0c84c5bdddde31c6e82cce055ba758.png?w=840&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=39a1e787718342851cb3faf64d47743b 840w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/google_oauth_list-5b0c84c5bdddde31c6e82cce055ba758.png?w=1100&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=9625b01d4558d8e1bef2d065d0aeb820 1100w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/google_oauth_list-5b0c84c5bdddde31c6e82cce055ba758.png?w=1650&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=903f432652191545e0c04ad5384cd171 1650w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/google_oauth_list-5b0c84c5bdddde31c6e82cce055ba758.png?w=2500&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=69202005106959bd93244e33b67af714 2500w" />
</Frame>

If this is not the case, create a new Google SSO Integration by clicking on the **Add new integration** button.

Enable the **Allow Google logins in organization** switch and click **Save**. That's it!
If you are not using Datafold SaaS, please see below.

## Create OAuth Client ID

To begin, navigate to the [Google admin console](https://console.cloud.google.com/apis/credentials?authuser=1%5C\&folder=%5C) for your organization, click **Create Credentials**, and select **OAuth Client ID**.

<Frame>
  <img src="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/google_oauth_create_credential-95776eb793bc1a1115c5fe1b18d9203f.png?fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=2dd9a41200dbec554854e8f2152d4967" data-og-width="2546" width="2546" data-og-height="1212" height="1212" data-path="images/google_oauth_create_credential-95776eb793bc1a1115c5fe1b18d9203f.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/google_oauth_create_credential-95776eb793bc1a1115c5fe1b18d9203f.png?w=280&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=5c04ab9c87f3433a4321ad094cff0444 280w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/google_oauth_create_credential-95776eb793bc1a1115c5fe1b18d9203f.png?w=560&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=3237419a4fbc116379685d0f3baf3ee0 560w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/google_oauth_create_credential-95776eb793bc1a1115c5fe1b18d9203f.png?w=840&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=d79b7171c609bafcf9f214a74ceaa2b7 840w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/google_oauth_create_credential-95776eb793bc1a1115c5fe1b18d9203f.png?w=1100&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=0d6e57a10068535692854bb690d680dc 1100w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/google_oauth_create_credential-95776eb793bc1a1115c5fe1b18d9203f.png?w=1650&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=81386a187e89ad982cd136fc168b44ec 1650w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/google_oauth_create_credential-95776eb793bc1a1115c5fe1b18d9203f.png?w=2500&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=738ceb21992881ed330289cc0d781296 2500w" />
</Frame>

<Tip>
  **TIP**

  To configure OAuth, you may need to first configure your consent screen. We recommend selecting **Internal** to keep access limited to users in your Google workspace and organization.
</Tip>

<Frame>
  <img src="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/google_oauth_consent_screen-6fd858ff5d1fc5fd43be910f055fe0ca.png?fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=f8fbe61a51916af96fac74baba6e0c57" data-og-width="1100" width="1100" data-og-height="928" height="928" data-path="images/google_oauth_consent_screen-6fd858ff5d1fc5fd43be910f055fe0ca.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/google_oauth_consent_screen-6fd858ff5d1fc5fd43be910f055fe0ca.png?w=280&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=85a18952eaa280999dca0b9d7d7c4fac 280w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/google_oauth_consent_screen-6fd858ff5d1fc5fd43be910f055fe0ca.png?w=560&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=bda6ab56698d40e1e0bf0981ea705725 560w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/google_oauth_consent_screen-6fd858ff5d1fc5fd43be910f055fe0ca.png?w=840&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=1d8b214ee69deba0807a3d8265484b4b 840w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/google_oauth_consent_screen-6fd858ff5d1fc5fd43be910f055fe0ca.png?w=1100&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=43e2ef08d691297c9f52ce6dd1d6ea40 1100w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/google_oauth_consent_screen-6fd858ff5d1fc5fd43be910f055fe0ca.png?w=1650&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=d2f3fd70ae47170db93229c4ac7f5db4 1650w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/google_oauth_consent_screen-6fd858ff5d1fc5fd43be910f055fe0ca.png?w=2500&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=ab043b43d1570852e18186d29c44d827 2500w" />
</Frame>

### Configure OAuth[](#configure-oauth "Direct link to Configure OAuth")

* **Application type**: "Web application"
* **Authorized JavaScript origins**: `https://<your.domain.name>`
* **Authorized redirect URIs**: `https://<your.domain.name>/oauth/google`

<Frame>
  <img src="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/google_oauth_authorizations-002a9446a71ba66ba4d375d897c4cdf7.png?fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=d81a93fc47ce61af186a44b1e3032d73" data-og-width="1301" width="1301" data-og-height="1224" height="1224" data-path="images/google_oauth_authorizations-002a9446a71ba66ba4d375d897c4cdf7.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/google_oauth_authorizations-002a9446a71ba66ba4d375d897c4cdf7.png?w=280&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=d38aff3864a2f31b85cf4279d768b225 280w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/google_oauth_authorizations-002a9446a71ba66ba4d375d897c4cdf7.png?w=560&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=ef1fda51909f5b439221d1775330bfe5 560w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/google_oauth_authorizations-002a9446a71ba66ba4d375d897c4cdf7.png?w=840&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=05ded4cda10a1342c47b4199e0fff443 840w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/google_oauth_authorizations-002a9446a71ba66ba4d375d897c4cdf7.png?w=1100&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=9dbfe9a60e75feaa9b053b4611cab4f7 1100w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/google_oauth_authorizations-002a9446a71ba66ba4d375d897c4cdf7.png?w=1650&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=f44d8a4fbc916f5e92488c87deb604e1 1650w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/google_oauth_authorizations-002a9446a71ba66ba4d375d897c4cdf7.png?w=2500&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=88e03d3a62ead7ce5afd9c8c771d8922 2500w" />
</Frame>

Finally, click **Create**. You will see a set of credentials that you will copy over to your Datafold Global Settings.

## Configure Google OAuth in Datafold

To finish the configuration, create a Google SSO Integration in Datafold.

To complete the integration in Datafold, create a new integration by navigating to **Settings** → **Integrations** → **SSO** → **Add new integration** → **Google**.

<Frame>
  <img src="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/google_oauth_create-463bc5c0d7cd049e0ba4ae8fdd577185.png?fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=f6236303e7386aa134d770bc9004ba80" data-og-width="2070" width="2070" data-og-height="666" height="666" data-path="images/google_oauth_create-463bc5c0d7cd049e0ba4ae8fdd577185.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/google_oauth_create-463bc5c0d7cd049e0ba4ae8fdd577185.png?w=280&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=7e3406de67b5c070cd7ac99c440f248e 280w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/google_oauth_create-463bc5c0d7cd049e0ba4ae8fdd577185.png?w=560&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=ebc3357ab62687407deb5d9fd63e6067 560w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/google_oauth_create-463bc5c0d7cd049e0ba4ae8fdd577185.png?w=840&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=b10e57e922bcfb26dd6fc27031b41555 840w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/google_oauth_create-463bc5c0d7cd049e0ba4ae8fdd577185.png?w=1100&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=224b5d6d21fcec28cb2a45aece520f5f 1100w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/google_oauth_create-463bc5c0d7cd049e0ba4ae8fdd577185.png?w=1650&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=184fecd1f44546ff584188b888aba4a9 1650w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/google_oauth_create-463bc5c0d7cd049e0ba4ae8fdd577185.png?w=2500&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=921da1190b889757ca1f86f21f8ddd34 2500w" />
</Frame>

* Enable the **Google OAuth** switch.
* Enter the **domain** or URL of your OAuth client Id on the respective field.
* Paste the **Client Secret** on the respective field.
* Enable the **Allow Google logins in Organization** switch.
* Finally, click **Save**.
