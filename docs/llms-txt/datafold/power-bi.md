# Source: https://docs.datafold.com/integrations/bi-data-apps/power-bi.md

# Power BI

> Include Power BI entities in Data Explorer and column-level lineage.

## Overview

Our Power BI integration can help you visualize column-level lineage dependencies between warehouse tables and Power BI entities using [Data Explorer](/data-explorer/how-it-works). Datafold supports the following Power BI entity types:

* Tables (with Columns)
* Reports (with Fields)
* Dashboards

## Set up the integration

<Steps>
  <Step title="Open Microsoft 365 admin center">
    Navigate to [**Microsoft 365 admin center** -> 👤 **Active users**](https://admin.microsoft.com/#/users) and choose the user that Datafold will authenticate under.

    <Frame>
      <img src="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/microsoft-admin-user.png?fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=38be66f2206263532520e4dc5ccd56a9" data-og-width="2056" width="2056" data-og-height="915" height="915" data-path="images/power-bi/microsoft-admin-user.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/microsoft-admin-user.png?w=280&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=c239123f4290a9343a5f9623578fc50a 280w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/microsoft-admin-user.png?w=560&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=a6e8e8e842a76bf59f82e9280918d639 560w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/microsoft-admin-user.png?w=840&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=1a8d05276bfa28413b56ca27c0fc7647 840w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/microsoft-admin-user.png?w=1100&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=9a5d3dfb92285c4ee6e660835b477699 1100w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/microsoft-admin-user.png?w=1650&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=3a4fc4206ed16e884f9286dc23c3332c 1650w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/microsoft-admin-user.png?w=2500&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=f5ef23e3b54795de89b11cd448b91dd7 2500w" />
    </Frame>

    As highlighted in the screenshot above, this user should have the **Power Platform Administrator** role assigned to it.
  </Step>

  <Step title="If the role is missing, assign it">
    Click **Manage roles**, enable the **Power Platform Administrator** role, and save changes.

    <Frame>
      <img src="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/microsoft-role.png?fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=10a2d7a38614008498702ea653240b45" data-og-width="2056" width="2056" data-og-height="915" height="915" data-path="images/power-bi/microsoft-role.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/microsoft-role.png?w=280&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=135fedd2022b556e6c743e17c6a874d1 280w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/microsoft-role.png?w=560&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=707191572a27daa24a7c19ec9cf98775 560w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/microsoft-role.png?w=840&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=2c255e4049b67b1c23bcdef6409c0923 840w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/microsoft-role.png?w=1100&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=e19cf19b04387d5e640612acc9a5cc5c 1100w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/microsoft-role.png?w=1650&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=ceb86ec7519bb644dde283c300fd82c7 1650w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/microsoft-role.png?w=2500&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=53811079ed2129f6eaed889c2a02c3d1 2500w" />
    </Frame>
  </Step>

  <Step title="Configure Power BI API">
    Navigate to [Power BI Admin Portal](https://app.powerbi.com/admin-portal/tenantSettings?experience=power-bi) and enable the following two settings:

    * Enhance admin APIs responses with detailed metadata
    * Enhance admin APIs responses with DAX and mashup expressions

    <Frame>
      <img src="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/admin-portal.png?fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=947277d450e3507854f041e1dc1bf924" data-og-width="2060" width="2060" data-og-height="1179" height="1179" data-path="images/power-bi/admin-portal.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/admin-portal.png?w=280&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=03c6e0431149d3b69eccc559613c6233 280w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/admin-portal.png?w=560&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=c4a9720692c6da78b09d6e2ebcd5f252 560w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/admin-portal.png?w=840&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=e34423eff722ab3da9a50584f45fe096 840w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/admin-portal.png?w=1100&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=0b26f8d48a81d35a829f7a95d4aa2f4e 1100w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/admin-portal.png?w=1650&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=2ae52e01cc773182c4222690ceb182ef 1650w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/admin-portal.png?w=2500&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=efc8d3ccca4113fb3d9171dbb74659f8 2500w" />
    </Frame>
  </Step>

  <Step title="Create Power BI integration in Datafold">
    In the Datafold app, navigate to **Settings** -> **BI & Data Apps**, and click **+ Add new integration**. Choose **Power BI** from the list.

    <Frame>
      <img src="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/create.png?fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=b19abe212823cc0404644d16668aa588" data-og-width="2056" width="2056" data-og-height="915" height="915" data-path="images/power-bi/create.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/create.png?w=280&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=cb41d2c71af15c48ccf4b5fe13cca705 280w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/create.png?w=560&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=7ef487fcf9f95185a0b17a47e27deb4a 560w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/create.png?w=840&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=4fab71dda7d3bcbc45a72b75932c8586 840w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/create.png?w=1100&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=876a313842469e44916c7b58369ba5a7 1100w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/create.png?w=1650&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=e3f9c38e910776ce55d9bf271ed17bfe 1650w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/create.png?w=2500&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=527c729ffc3699385eb9c2044e5995e5 2500w" />
    </Frame>
  </Step>

  <Step title="Fill in the name for your new integration">
    ...and then **Save**.

    <Frame>
      <img src="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/new.png?fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=dd2456c5ce5f75e9a21a3e7512f6a185" data-og-width="2056" width="2056" data-og-height="915" height="915" data-path="images/power-bi/new.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/new.png?w=280&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=a8331be34f53169e87489d717dd79a2f 280w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/new.png?w=560&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=d8c5750189a08759f887454212b6a8bb 560w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/new.png?w=840&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=4dc6e1ae5da5f606957852bd83e728cf 840w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/new.png?w=1100&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=a2cc9a84fba89dc44bdf8436dcf70edd 1100w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/new.png?w=1650&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=eba79ddc95ec4195db9141301e044524 1650w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/new.png?w=2500&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=dbd0c8fe63944e77f4898e16efe65b6e 2500w" />
    </Frame>

    On clicking **Save**, the system will redirect you to Power BI.
  </Step>

  <Step title="Sign in to Power BI">
    ...if not already signed in.

    <Frame>
      <img src="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/sign-in.png?fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=9bb6c26dca422fdc86ee250477dc0d5c" data-og-width="2056" width="2056" data-og-height="915" height="915" data-path="images/power-bi/sign-in.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/sign-in.png?w=280&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=9af33152cd51cb5e02045af45a22225a 280w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/sign-in.png?w=560&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=628c843aaae78cecda7331ba1aa0bf55 560w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/sign-in.png?w=840&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=0ba10f215486c0d56ed48eb05fac81cb 840w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/sign-in.png?w=1100&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=483e864be52f27b1d2df28dc0009d17b 1100w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/sign-in.png?w=1650&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=20a52a33dd3ac6e3d67b7c6869dbf69d 1650w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/sign-in.png?w=2500&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=c9ad62068f7a74d7907c40f903f3c2ae 2500w" />
    </Frame>
  </Step>

  <Step title="Grant permissions to Datafold">
    Allow the Datafold integration to use Power BI. Depending on the roles configured for your user in the Admin center, you may require a confirmation from a **Global Administrator**. Follow the steps in the wizard.

    <Frame>
      <img src="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/consent.png?fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=6a1ad1535bbf09d220fb5c2783e1d6aa" data-og-width="2060" width="2060" data-og-height="1179" height="1179" data-path="images/power-bi/consent.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/consent.png?w=280&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=42bab1e9bc0bfffa60c7f866b9fc7198 280w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/consent.png?w=560&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=485af431c98886614bf02eef0f24ec6e 560w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/consent.png?w=840&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=5dda72b878229f133d2ff4a532622f96 840w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/consent.png?w=1100&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=4d8d47bd55db39bcfae0cabea0d69119 1100w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/consent.png?w=1650&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=c940d24cf6c2cfa07f5280b31a35b152 1650w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/consent.png?w=2500&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=7bd105a4ce6f55287b68f2cbc6ec1c9f 2500w" />
    </Frame>
  </Step>

  <Step title="Integration is ready">
    You will be redirected back to Datafold and see a message that Power BI is successfully connected.

    <Frame>
      <img src="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/success.png?fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=756557c082662c5834d34daa351ddc60" data-og-width="2056" width="2056" data-og-height="915" height="915" data-path="images/power-bi/success.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/success.png?w=280&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=10a59c3d5bf3d152580f9da10d2cf3e5 280w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/success.png?w=560&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=286cfcce60a83035fb0ee2102fd7316e 560w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/success.png?w=840&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=b683cd8370384a46df812b142e5ebe11 840w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/success.png?w=1100&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=97695434f3d811edfd556acae9f63134 1100w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/success.png?w=1650&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=6d403cde6068c0c5d9b7db41221cd68a 1650w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/success.png?w=2500&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=cecdaca2a75ad077c6db925235195f1d 2500w" />
    </Frame>
  </Step>

  <Step title="Power BI integration needs some time to sync">
    You can check out **Jobs** -> **BI & Data Apps** for the status of the sync job.

    <Frame>
      <img src="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/jobs.png?fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=a1288e76fb558f0c37875a812f1bc119" data-og-width="2056" width="2056" data-og-height="915" height="915" data-path="images/power-bi/jobs.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/jobs.png?w=280&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=58cce51b5b9b130375500cd331dde57a 280w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/jobs.png?w=560&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=b89d04036a352969d0c940c6c088222f 560w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/jobs.png?w=840&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=445452b8324ea69be064142a79795f53 840w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/jobs.png?w=1100&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=95084316d73d3e0132819ae007393a26 1100w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/jobs.png?w=1650&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=2a01cbad96e2516b90cda37be1bbe23b 1650w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/jobs.png?w=2500&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=afe0e676178e7fc871e8c04cc3802f1b 2500w" />
    </Frame>

    See [Tracking Jobs](/integrations/bi-data-apps/tracking-jobs) for more details.
  </Step>

  <Step title="Power BI entities are now searchable">
    When the sync is complete, you will see Power BI entities in **Data Explorer**.

    <Frame>
      <img src="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/data-explorer.png?fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=4d97fd3f9b6da71c68b07af43723c3e5" data-og-width="2056" width="2056" data-og-height="915" height="915" data-path="images/power-bi/data-explorer.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/data-explorer.png?w=280&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=b3f4b58d3892ba3b88f52bd90a345d22 280w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/data-explorer.png?w=560&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=54197de01b02d766838a5f036949ecdb 560w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/data-explorer.png?w=840&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=dccf4ff5939cf98aa43a9eb776a8c933 840w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/data-explorer.png?w=1100&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=ddd08530b3363569eaf07fe08771298e 1100w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/data-explorer.png?w=1650&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=e5686245370a9e74d0ce07fb7b726166 1650w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/data-explorer.png?w=2500&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=15fbf0b692c6064f4d835103d4ae1a34 2500w" />
    </Frame>
  </Step>

  <Step title="Lineage is now available">
    <Frame>
      <img src="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/lineage.png?fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=ab5d1896b8ccfa79e156cec7a604b6bb" data-og-width="2056" width="2056" data-og-height="915" height="915" data-path="images/power-bi/lineage.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/lineage.png?w=280&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=3e50a4292b7f81104131474360a6547e 280w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/lineage.png?w=560&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=ee6a1bd7c66158437c917829881d0e2b 560w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/lineage.png?w=840&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=cd61db20c1fbc090bb25d47e1d5f88e0 840w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/lineage.png?w=1100&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=1389caf0e01891afe363c01cb5547959 1100w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/lineage.png?w=1650&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=ce0f73e05c0a5912bdcb655aa98b579f 1650w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/lineage.png?w=2500&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=985117daf40d54d725ee6a1808086ca3 2500w" />
    </Frame>
  </Step>
</Steps>

## Need help?

If you have any questions about our Power BI integration, please reach out to our team via Slack, in-app chat, or email us at [support@datafold.com](mailto:support@datafold.com).
