# Source: https://docs.datafold.com/security/single-sign-on/saml/examples/okta.md

# Source: https://docs.datafold.com/security/single-sign-on/okta.md

# Source: https://docs.datafold.com/security/single-sign-on/saml/examples/okta.md

# Source: https://docs.datafold.com/security/single-sign-on/okta.md

# Okta (OIDC)

<Info>
  **NOTE**

  Okta SSO is available for both SaaS and dedicated cloud installations of Datafold.
</Info>

## Create Okta App Integration[](#create-okta-app-integration "Direct link to Create Okta App Integration")

<Note>
  **INFO**

  Creating an App Integration in Okta may require admin privileges.
</Note>

Start the integration by creating a web app integration in Okta.

Next, log in to Okta interface and navigate to **Applications** and click **Create App Integration**.

Then, in the configuration form, select **OpenId Connect (OIDC)** and **Web Application** as the Application Type.

<Frame>
  <img src="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/okta_create_new_app-0b8566bc3dd329ef3d80f849c0065fef.png?fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=cd99a119a39d2e15d3ca3584783311d1" data-og-width="2796" width="2796" data-og-height="2120" height="2120" data-path="images/okta_create_new_app-0b8566bc3dd329ef3d80f849c0065fef.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/okta_create_new_app-0b8566bc3dd329ef3d80f849c0065fef.png?w=280&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=cb914e5cd780c78edb7d4387d9e6dda8 280w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/okta_create_new_app-0b8566bc3dd329ef3d80f849c0065fef.png?w=560&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=cf9347ff420148fb85989217583fed0c 560w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/okta_create_new_app-0b8566bc3dd329ef3d80f849c0065fef.png?w=840&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=0a56b06a16cfb02e8d16798d37545725 840w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/okta_create_new_app-0b8566bc3dd329ef3d80f849c0065fef.png?w=1100&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=0a820232d15b1226f6ca3eac5a8ddb2c 1100w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/okta_create_new_app-0b8566bc3dd329ef3d80f849c0065fef.png?w=1650&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=ca39877292b3a2b12449ae01affeedde 1650w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/okta_create_new_app-0b8566bc3dd329ef3d80f849c0065fef.png?w=2500&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=c8a2be1ae8ac2402e9be775b34bdd58e 2500w" />
</Frame>

In the following section, you will set:

* **App integration name**: A name to identify the integration. We suggest you use `Datafold`.
* **Grant type**: Should be set to `Authorization code` automatically.
* **Sign-in redirect URI**:

<Tabs>
  <Tab title=" SaaS">
    The redirect URL should be `https://app.datafold.com/oauth/okta/client_id`, where `client_id` is the Client ID of the configuration.

    <Warning>
      **CAUTION**
      You will be given the Client ID after saving the integration and need to come back to update the client ID afterwards.
    </Warning>
  </Tab>

  <Tab title="Dedicated cloud installations of Datafold">
    The redirect URL should be `https://your-dns-name/oauth/okta`, replacing `your-dns-name` with the DNS name for your installation.
  </Tab>
</Tabs>

* **Sign-out redirect URIs**: Leave this empty.
* **Trusted Origins**: Leave this empty too.
* **Assignments**: Select `Skip group assignment for now`. Later you should assign the correct groups and users.
* Click "Save" to create the app integration in Okta.

<Frame>
  <img src="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/okta_redirect_uri-b64d1ac6c24ab8577bf8a52f14da842b.png?fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=47fe81beba56d13cbbc6e3e5e7cd061c" data-og-width="915" width="915" data-og-height="733" height="733" data-path="images/okta_redirect_uri-b64d1ac6c24ab8577bf8a52f14da842b.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/okta_redirect_uri-b64d1ac6c24ab8577bf8a52f14da842b.png?w=280&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=9c7caf3ed96608bf9639fcf93f993253 280w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/okta_redirect_uri-b64d1ac6c24ab8577bf8a52f14da842b.png?w=560&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=2b8d1aa51a2b32c28c7c6fadbffa3f44 560w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/okta_redirect_uri-b64d1ac6c24ab8577bf8a52f14da842b.png?w=840&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=ab630f62ba5587489e2ba9ea76df774e 840w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/okta_redirect_uri-b64d1ac6c24ab8577bf8a52f14da842b.png?w=1100&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=e4fcfbc510a482468b8239fa89680449 1100w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/okta_redirect_uri-b64d1ac6c24ab8577bf8a52f14da842b.png?w=1650&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=c303f1bb514d6ab2dae609b168bb7353 1650w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/okta_redirect_uri-b64d1ac6c24ab8577bf8a52f14da842b.png?w=2500&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=2044f3cc5192388676699fe9eea5a7b1 2500w" />
</Frame>

Once the save is successful, on the next screen, you'll be presented with Client ID and Client Secret. We need these IDs to update the redirect URLs that Datafold needs. We'll also apply the Client ID and Client Secret in the Datafold integration later.

* Edit "General settings"
* Scroll down to the **Login** section
* Update the **Sign-in redirect URI**. See above for details.
* Click "Save" to persist the changes.

## Set Up Okta-initiated login

<Tip>
  **TIP**

  Organization admins will always be able to log in with either password or Okta. Non-admin users will be required to log in through Okta once configured.
</Tip>

This step is optional and should be done at the discretion of the Okta administrator.

Users in your organization can log in to the application directly from the Okta end-user dashboard. To enable this feature, configure the integration as follows:

1. Edit "General settings"
2. Set **Login initiated by** to `Either Okta or App`.
3. Set **Application visibility** to `Display application icon to users`.
4. Set **Login flow** to `Redirect to app to initiate login (OIDC Compliant)`.
5. Set **Initiate login URI**:

<Tabs>
  <Tab title=" SaaS">
    * `https://app.datafold.com/login/sso/client-id?action=desired_action`
    * Replace `client-id` with the Client ID of the configuration, and
    * Replace `desired_action` with `signup` if you enabled users auto-creation, or `login` otherwise.
  </Tab>

  <Tab title="Dedicated cloud installations of Datafold">
    * `https://your-dns-name/login/sso/client-id?action=desired_action`
    * Replace `client-id` with the Client ID of the configuration, and
    * Replace `desired_action`with `signup` if you enabled users auto-creation, or `login` otherwise.
    * Replace `your-dns-name` with the DNS name for your installation.
  </Tab>
</Tabs>

<Frame>
  <img src="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/okta_initiated_login-8a7541151582487dd21f8381207e25fd.png?fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=b6ee8ab50310409a28abd3d7de8d6461" data-og-width="1398" width="1398" data-og-height="1206" height="1206" data-path="images/okta_initiated_login-8a7541151582487dd21f8381207e25fd.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/okta_initiated_login-8a7541151582487dd21f8381207e25fd.png?w=280&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=fcf22e2b4132131726db58c35ce17172 280w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/okta_initiated_login-8a7541151582487dd21f8381207e25fd.png?w=560&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=4f08bc2138da08428cff82a9b023ce4f 560w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/okta_initiated_login-8a7541151582487dd21f8381207e25fd.png?w=840&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=73f277df42db7db8092fbdde06cf8144 840w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/okta_initiated_login-8a7541151582487dd21f8381207e25fd.png?w=1100&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=a63bc6f8d1be025ce82640f95ffc0fbb 1100w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/okta_initiated_login-8a7541151582487dd21f8381207e25fd.png?w=1650&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=8a90c035fad8640ab3cf1620b90ac05b 1650w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/okta_initiated_login-8a7541151582487dd21f8381207e25fd.png?w=2500&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=fe75b2e60c9b96cb0db5d1fa06373a4f 2500w" />
</Frame>

1. Click "Save" to persist the changes.

The Okta configuration is now complete.

## Configure Okta in Datafold

To finish the configuration, create an Okta integration in Datafold.

To complete the integration in Datafold, create a new integration by navigating to **Settings** → **Integrations** → **SSO** → **Add new integration** → **Okta**.

<Frame>
  <img src="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/okta_create-8269c208d4fa7df43a8c5ad99e675297.png?fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=805f5b088b6fb89000adb5533c4df0da" data-og-width="2072" width="2072" data-og-height="762" height="762" data-path="images/okta_create-8269c208d4fa7df43a8c5ad99e675297.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/okta_create-8269c208d4fa7df43a8c5ad99e675297.png?w=280&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=840215cc19908a03df300dd3100c2952 280w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/okta_create-8269c208d4fa7df43a8c5ad99e675297.png?w=560&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=5a40fcabb66de9c8003303075dc3c64f 560w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/okta_create-8269c208d4fa7df43a8c5ad99e675297.png?w=840&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=b5c462ec60a76a86f944a98bae702e05 840w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/okta_create-8269c208d4fa7df43a8c5ad99e675297.png?w=1100&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=a7531d669ae279ed8749e1eb93b4219a 1100w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/okta_create-8269c208d4fa7df43a8c5ad99e675297.png?w=1650&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=0ff47734f6144b3494b6d7220ce41c61 1650w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/okta_create-8269c208d4fa7df43a8c5ad99e675297.png?w=2500&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=5d439d069e5acc348e9897de5d21182e 2500w" />
</Frame>

* Paste in your Okta **Client Id** and **Client Secret**.
* The **Metadata Url** of Okta OAuth server is `https://<okta-server-name>/.well-known/openid-configuration`, replace `okta-server-name` with the name of your Okta domain.
* If you'd like to auto-create users in Datafold that are authorized in Okta, enable the **Allow Okta to auto-create users in Organization** switch.
* Finally, click **Save**.

<Tip>
  **TIP**

  Users can either be explicitly invited in Datafold by an admin user, using the same email as used in Okta, or they can be auto-created. When the `signup` action is set in the login URI, authenticated users on Okta who have been assigned as a user in Okta of the Datafold application will then be able to login. If that user has not yet been invited, Datafold will then automatically create a user for them, since they're already authenticated by the Okta server of your domain. The user will then receive an email to confirm their email address.
</Tip>

## Synchronize state with Datafold \[Optional]

This step is essential if you want to ensure that users from your organization are automatically logged out when they are unassigned or deactivated in Okta.

1. Navigate to **Okta Admin panel** → **Workflow** → **Event Hooks**
2. Click **Create Event Hook**
3. Set **Name** to `Datafold`
4. Set **URL** to `https://app.datafold.com/hooks/oauth/okta/<client-id>`
5. Set **Authentication field** to `secret`
6. Go to Datafold and generate a secret token in **Settings** → **Integrations** → **SSO** → **Okta**. Click the **Generate** button, copy it by using the **Copy** button and click **Save**. Use the pasted code in the **Authentication secret** field in Okta.

<Frame>
  <img src="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/generate_token_input-3ef82f777565226aa5da10b52464549e.png?fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=36e3752ce79f7e792d543efcb9012fc0" data-og-width="1756" width="1756" data-og-height="216" height="216" data-path="images/generate_token_input-3ef82f777565226aa5da10b52464549e.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/generate_token_input-3ef82f777565226aa5da10b52464549e.png?w=280&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=42cdb90429a3a9c1ac36888fc9277617 280w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/generate_token_input-3ef82f777565226aa5da10b52464549e.png?w=560&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=bf21a126379a58a2fa8dd94bd21cd30c 560w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/generate_token_input-3ef82f777565226aa5da10b52464549e.png?w=840&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=ca29ed5c6a2fd6a7dfebc34891031ebb 840w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/generate_token_input-3ef82f777565226aa5da10b52464549e.png?w=1100&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=c06e7ece043a1c514be15aaa9484b529 1100w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/generate_token_input-3ef82f777565226aa5da10b52464549e.png?w=1650&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=3c20b9682b00d32fdd6cb6ee2625dacc 1650w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/generate_token_input-3ef82f777565226aa5da10b52464549e.png?w=2500&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=da00aaac4c96e48594c0bde2039ce3ef 2500w" />
</Frame>

<Warning>
  **CAUTION**

  Keep this secret token safe as you won't be able to see after saving your Integration.
</Warning>

7. In **Subscribe to events** add events: `User suspended`, `User deactivated`, `Deactivate application`, `User unassigned from app`
8. Click **Save & Continue**

<Frame>
  <img src="https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/config_okta_event_hooks-ed108690a4e2e94d8158527dcc2f4196.png?fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=aa1f13e3d70bef5f4a2660eb91da93cd" data-og-width="1466" width="1466" data-og-height="1484" height="1484" data-path="images/config_okta_event_hooks-ed108690a4e2e94d8158527dcc2f4196.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/config_okta_event_hooks-ed108690a4e2e94d8158527dcc2f4196.png?w=280&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=2f61f0553001c73c059076e15531fa8d 280w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/config_okta_event_hooks-ed108690a4e2e94d8158527dcc2f4196.png?w=560&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=1fb17f3a93e18e547fa114cc75a34390 560w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/config_okta_event_hooks-ed108690a4e2e94d8158527dcc2f4196.png?w=840&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=086e57959bf93c73d5c0dae7ecc5262f 840w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/config_okta_event_hooks-ed108690a4e2e94d8158527dcc2f4196.png?w=1100&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=7e2739c1430dd272623cf379caeda9bc 1100w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/config_okta_event_hooks-ed108690a4e2e94d8158527dcc2f4196.png?w=1650&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=6126ae5abd4292a7386a5bd21afca293 1650w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/config_okta_event_hooks-ed108690a4e2e94d8158527dcc2f4196.png?w=2500&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=38ef84c1a464f499ee3d02ab6c66a0ff 2500w" />
</Frame>

. On **Verify Endpoint Ownership** click **Verify**

<Frame>
  <img src="https://mintcdn.com/datafold/4ZNRDufNo9R1p08Q/images/verify_okta_event_hooks-57c17ee772834faf39e6c7689743d1f5.png?fit=max&auto=format&n=4ZNRDufNo9R1p08Q&q=85&s=697f26bc7f857a68847d006d0fa4d9c7" data-og-width="1368" width="1368" data-og-height="650" height="650" data-path="images/verify_okta_event_hooks-57c17ee772834faf39e6c7689743d1f5.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/4ZNRDufNo9R1p08Q/images/verify_okta_event_hooks-57c17ee772834faf39e6c7689743d1f5.png?w=280&fit=max&auto=format&n=4ZNRDufNo9R1p08Q&q=85&s=5a2317b502377f247113237261a3d467 280w, https://mintcdn.com/datafold/4ZNRDufNo9R1p08Q/images/verify_okta_event_hooks-57c17ee772834faf39e6c7689743d1f5.png?w=560&fit=max&auto=format&n=4ZNRDufNo9R1p08Q&q=85&s=df89bf3c345b9d9445864a73199931fe 560w, https://mintcdn.com/datafold/4ZNRDufNo9R1p08Q/images/verify_okta_event_hooks-57c17ee772834faf39e6c7689743d1f5.png?w=840&fit=max&auto=format&n=4ZNRDufNo9R1p08Q&q=85&s=f24c0068d11085cea226aa4f527a1540 840w, https://mintcdn.com/datafold/4ZNRDufNo9R1p08Q/images/verify_okta_event_hooks-57c17ee772834faf39e6c7689743d1f5.png?w=1100&fit=max&auto=format&n=4ZNRDufNo9R1p08Q&q=85&s=63658165aaf8da903275cda34e0efb55 1100w, https://mintcdn.com/datafold/4ZNRDufNo9R1p08Q/images/verify_okta_event_hooks-57c17ee772834faf39e6c7689743d1f5.png?w=1650&fit=max&auto=format&n=4ZNRDufNo9R1p08Q&q=85&s=bcbb4899597517b563e03c3388725a29 1650w, https://mintcdn.com/datafold/4ZNRDufNo9R1p08Q/images/verify_okta_event_hooks-57c17ee772834faf39e6c7689743d1f5.png?w=2500&fit=max&auto=format&n=4ZNRDufNo9R1p08Q&q=85&s=c0d3d8173cd58326b94639dcb77cc066 2500w" />
</Frame>

* If the verification is successful, you have completed the setup.

## Testing the Okta integration

<Tabs>
  <Tab title="SaaS">
    * Visit [https://app.datafold.com](https://app.datafold.com)
    * Type in your email and wait up to five seconds.
    * The Okta button should switch from disabled to enabled.
    * Click the Okta login button.
    * The browser should be redirected to your Okta domain, authenticate the user there and be redirected back to the Datafold application.
  </Tab>

  <Tab title="Dedicated cloud installations of Datafold">
    * Visit `https://your-dns-name`, replacing your-dns-name with the domain name of your installation.
    * Type in your email and wait up to five seconds.
    * The Okta button should switch from disabled to enabled.
    * Click the Okta login button.
    * The browser should be redirected to your Okta domain, authenticate the user there and be redirected back to the Datafold application.
  </Tab>
</Tabs>

If this didn't work, pay close attention to any error messages, or contact `support@datafold.com`.
