# Source: https://www.aptible.com/docs/how-to-guides/platform-guides/setup-sso-auth0.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.aptible.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# How to Set Up Single Sign-On (SSO) for Auth0

> This guide provides detailed instructions on how to set up a custom SAML application in Auth0 for integration with Aptible.

## Prerequisites

* An active Auth0 account
* Administrative access to the Auth0 dashboard
* Aptible Account Owner access to enable and configure SAML settings

## Creating Your Auth0 SAML Application

<Steps>
  <Step title="Accessing the Applications Dashboard">
    Log into your Auth0 dashboard. Navigate to **Applications** using the left navigation menu and click **Create Application**. Enter a name for your application (we suggest "Aptible"), select **Regular Web Applications**, and click **Create**.

        <img src="https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/sso-auth0-create.png?fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=bcc6343645fa1b2ca79bf6f0d28b79e4" alt="" data-og-width="1594" width="1594" data-og-height="1320" height="1320" data-path="images/sso-auth0-create.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/sso-auth0-create.png?w=280&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=ad3dae5e44e869e558866e5f17f378de 280w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/sso-auth0-create.png?w=560&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=d87aab0d8d9785fcea8b01625335e101 560w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/sso-auth0-create.png?w=840&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=9b6f4f8714cc6b4a485fca7465cb80ca 840w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/sso-auth0-create.png?w=1100&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=805120cce4a21bbdfcbbc4b781e0664b 1100w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/sso-auth0-create.png?w=1650&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=955ed2d5ccaaf01df433b476817e2102 1650w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/sso-auth0-create.png?w=2500&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=d628ba6e3f4dd6434f429260dac4442e 2500w" />
  </Step>

  <Step title="Enabling SAML2 WEB APP">
    Select the **Addons** tab and enable the **SAML2 WEB APP** add-on by toggling it on. Navigate to the **Usage** tab and download the Identity Provider Metadata or copy the link to it. Close this window—It will toggle back to off, which is expected. We will activate it later.

        <img src="https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/sso-auth0-metadata.png?fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=02fde8e7f4ec3f687182592ff9a833bd" alt="" data-og-width="1262" width="1262" data-og-height="840" height="840" data-path="images/sso-auth0-metadata.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/sso-auth0-metadata.png?w=280&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=58d9fcdecabfaede40f23ecf2ecf9e5d 280w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/sso-auth0-metadata.png?w=560&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=4c44272296dc0a0f7ba46e5f8a6d4a2c 560w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/sso-auth0-metadata.png?w=840&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=ac23cde6cb0b6d5ccce3dc7a9467bd68 840w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/sso-auth0-metadata.png?w=1100&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=903c39de360bd708c8654a010d1cb410 1100w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/sso-auth0-metadata.png?w=1650&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=7a5a10677e89b8eecb776778a91f6bcd 1650w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/sso-auth0-metadata.png?w=2500&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=e32d7cb67d8d8701b42c6ac563ee0550 2500w" />
  </Step>

  <Step title="Enable SAML Integration">
    Log into your Aptible dashboard as an Account Owner. Navigate to **Settings** and select **Single Sign-On**. Copy the following information; you will need it later:

    * **Single Sign-On URL** (Assertion Consumer Service \[ACS] URL):\
      `https://auth.aptible.com/organizations/xxxxx-xxx-xxxx-xxxx-xxxxxxxxxxxx/saml/consume`

        <img src="https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/sso-auth0-acs.png?fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=282eef17d189276eee417e79a27dd3c1" alt="" data-og-width="1896" width="1896" data-og-height="1086" height="1086" data-path="images/sso-auth0-acs.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/sso-auth0-acs.png?w=280&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=1c4f82abaaa4b86f493462d88f1312eb 280w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/sso-auth0-acs.png?w=560&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=62992c0ea81165e8d60847439397c703 560w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/sso-auth0-acs.png?w=840&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=b7435c4bcb77d9bbd1cffcee4b191db9 840w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/sso-auth0-acs.png?w=1100&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=bfe2625eb2d4b3d7e4c8bf8b7931c408 1100w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/sso-auth0-acs.png?w=1650&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=128e0b34152244deca91b056d9b8518b 1650w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/sso-auth0-acs.png?w=2500&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=a666b0591d6b9fb80d0e06e133493f2e 2500w" />
  </Step>

  <Step title="Upload Identity Provider Metadata">
    On the same screen, locate the option for **Metadata URL**. Copy the content of the metadata file you downloaded from Auth0 into **Metadata File XML Content**, or copy the link to the file into the **Metadata URL** field. Click **Save**. After the information has been successfully saved, copy the newly provided information:

    * **Shortcut SSO login URL**:\
      `https://app.aptible.com/sso/xxxxx-xxx-xxxx-xxxx-xxxxxxxxxxxx`

        <img src="https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/sso-auth0-shortcut.png?fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=8289a856a132dd07065773172568d613" alt="" data-og-width="2308" width="2308" data-og-height="812" height="812" data-path="images/sso-auth0-shortcut.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/sso-auth0-shortcut.png?w=280&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=6ce3a01319d31522b7baf9d217e5241c 280w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/sso-auth0-shortcut.png?w=560&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=16bd5a5268ce0a2545ddb8a996cf0e3f 560w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/sso-auth0-shortcut.png?w=840&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=1d0e87c106f31bc47621eea332a8d22a 840w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/sso-auth0-shortcut.png?w=1100&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=9039f2f91bc1339477512b7caff68ed0 1100w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/sso-auth0-shortcut.png?w=1650&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=a311221b3380daaa05e5944f33ead733 1650w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/sso-auth0-shortcut.png?w=2500&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=1e307bfef28e306ee39761f00af5607f 2500w" />
  </Step>

  <Step title="Configuring SAML2 in Auth0">
    Return to the Auth0 SAML Application. In the Application under **Settings**, configure the following:

    * **Application Login URI**:\
      `https://app.aptible.com/sso/xxxxx-xxx-xxxx-xxxx-xxxxxxxxxxxx`
      (this is the Aptible value of **Shortcut SSO login URL**).
    * **Allowed Callback URLs**:\
      `https://auth.aptible.com/organizations/xxxxx-xxx-xxxx-xxxx-xxxxxxxxxxxx/saml/consume`
      (this is the Aptible value of **Single Sign-On URL - Assertion Consumer Service \[ACS] URL**).
    * Scroll down to **Advanced Settings -> Grant Types**. Select the grant type appropriate for your Auth0 configuration. Save the changes. Re-enable the **SAML2 WEB APP** add-on by toggling it on. Switch to the **Settings** tab. Copy the following into the **Settings** space (ensure that nothing else remains there):

    ```json  theme={null}
    { 
      "nameIdentifierProbes": [ 
        "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress" 
      ] 
    }
    ```

        <img src="https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/sso-auth0-settings.png?fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=94fa509f5550f092193d2e747ece1459" alt="" data-og-width="1948" width="1948" data-og-height="1164" height="1164" data-path="images/sso-auth0-settings.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/sso-auth0-settings.png?w=280&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=96669cd2d78714193f28a28e4179634e 280w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/sso-auth0-settings.png?w=560&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=92ffd9c7ac786e2f1a6677bb94bd3ac9 560w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/sso-auth0-settings.png?w=840&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=37e9c4aec77df5e89fd561c5576fc26b 840w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/sso-auth0-settings.png?w=1100&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=f73f4ec9830aa66f021a575474c61ec0 1100w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/sso-auth0-settings.png?w=1650&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=b9924c23baf9896d97d01343d92936f3 1650w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/sso-auth0-settings.png?w=2500&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=8db0aade344d1d0709695191290ce7a6 2500w" />
  </Step>

  <Step title="Finalize the Setup">
    Click on **Debug** — Ensure the opened page indicates "It works." Close this page, scroll down and select **Enable**.

    * Ensure that the correct users have access to your app (specific to your setup). Save the changes.

        <img src="https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/sso-auth0-itworks.png?fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=9170e3b4a44e01fe97112e8ac2e1f0e6" alt="" data-og-width="1888" width="1888" data-og-height="1676" height="1676" data-path="images/sso-auth0-itworks.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/sso-auth0-itworks.png?w=280&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=0811fe2e651ec75461592700acc6b49c 280w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/sso-auth0-itworks.png?w=560&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=44c4b1ffad918687455296cec9c7c8a0 560w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/sso-auth0-itworks.png?w=840&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=6cf7235519f8438e016790da754c6369 840w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/sso-auth0-itworks.png?w=1100&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=de282653986ac0934654bc8b43281044 1100w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/sso-auth0-itworks.png?w=1650&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=63b5095418db257aad6c786f7d8a6334 1650w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/sso-auth0-itworks.png?w=2500&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=1d36f91d8f6c6fd8731948f6214982ea 2500w" />
  </Step>
</Steps>

### Attribute Mapping

No additional attribute mapping is required for the integration to function.

### Testing the Login

Open a new incognito browser window. Open the link Aptible provided as **Shortcut SSO login URL**. Ensure that you will be able to login.
