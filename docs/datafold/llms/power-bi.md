# Source: https://docs.datafold.com/integrations/bi-data-apps/power-bi.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.datafold.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Power BI

> Include Power BI entities in Data Explorer and column-level lineage.

## Overview

Our Power BI integration can help you visualize column-level lineage dependencies between warehouse tables and Power BI entities using [Data Explorer](/data-explorer/how-it-works). Datafold supports the following Power BI entity types:

* Tables (with Columns)
* Reports (with Fields)
* Dashboards

## Choose your authentication method

Datafold supports two authentication methods for Power BI. Choose the one that best fits your organization's needs. Key difference:

* <strong>Delegated auth</strong> uses your user's identity, is tied to your account and permissions, also requiring you to be a <strong>Power Platform Administrator</strong>;
* <strong>Service Principal</strong> is an independent application identity that doesn't depend on any user, but can be a bit more complicated to setup.

<Tabs>
  <Tab title="Delegated (User OAuth)">
    ### Set up the integration

    <Steps>
      <Step title="Open Microsoft 365 admin center">
        Navigate to [**Microsoft 365 admin center** -> **Active users**](https://admin.microsoft.com/#/users) and choose the user that Datafold will authenticate under.

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
          <img src="https://mintcdn.com/datafold/qH5vFV99qD-5khom/images/power-bi/new-integration-delegated.png?fit=max&auto=format&n=qH5vFV99qD-5khom&q=85&s=196ffe47f065efe282c31431bf577629" data-og-width="2696" width="2696" data-og-height="1046" height="1046" data-path="images/power-bi/new-integration-delegated.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/qH5vFV99qD-5khom/images/power-bi/new-integration-delegated.png?w=280&fit=max&auto=format&n=qH5vFV99qD-5khom&q=85&s=8bba7dd0b7f7e40b1c752758efec6335 280w, https://mintcdn.com/datafold/qH5vFV99qD-5khom/images/power-bi/new-integration-delegated.png?w=560&fit=max&auto=format&n=qH5vFV99qD-5khom&q=85&s=efbf4a81048d82ea8ec2ed658218e40a 560w, https://mintcdn.com/datafold/qH5vFV99qD-5khom/images/power-bi/new-integration-delegated.png?w=840&fit=max&auto=format&n=qH5vFV99qD-5khom&q=85&s=73059330280ffcd4f828b65af8d7ba4a 840w, https://mintcdn.com/datafold/qH5vFV99qD-5khom/images/power-bi/new-integration-delegated.png?w=1100&fit=max&auto=format&n=qH5vFV99qD-5khom&q=85&s=5dad990158fb067a4ce5a425f0c96aa3 1100w, https://mintcdn.com/datafold/qH5vFV99qD-5khom/images/power-bi/new-integration-delegated.png?w=1650&fit=max&auto=format&n=qH5vFV99qD-5khom&q=85&s=e813ce2e0b1e471f7d0f527ff84f0ba5 1650w, https://mintcdn.com/datafold/qH5vFV99qD-5khom/images/power-bi/new-integration-delegated.png?w=2500&fit=max&auto=format&n=qH5vFV99qD-5khom&q=85&s=dd48270169ea094727f457f4ff40f8ab 2500w" />
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
    </Steps>
  </Tab>

  <Tab title="Service Principal">
    ### Set up the integration

    <Steps>
      <Step title="Create a Microsoft Entra ID App Registration">
        1. Go to [Microsoft Entra admin center - New Registration](https://entra.microsoft.com/?l=en.en-us#view/Microsoft_AAD_RegisteredApps/CreateApplicationBlade/quickStartType~/null/isMSAApp~/false)
        2. Configure the application:
           * **Name**: `Datafold Power BI Integration` (or similar)
           * **Supported account types**: "Accounts in this organizational directory only"
           * **Redirect URI**: Leave blank (not needed for Service Principal)

        <Frame>
          <img src="https://mintcdn.com/datafold/qH5vFV99qD-5khom/images/power-bi/service-principal/register-an-application.png?fit=max&auto=format&n=qH5vFV99qD-5khom&q=85&s=e1944be09e095f08af049fcc7ee3671c" data-og-width="2696" width="2696" data-og-height="1046" height="1046" data-path="images/power-bi/service-principal/register-an-application.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/qH5vFV99qD-5khom/images/power-bi/service-principal/register-an-application.png?w=280&fit=max&auto=format&n=qH5vFV99qD-5khom&q=85&s=a51b6c233ea8476fa102e81f570c855c 280w, https://mintcdn.com/datafold/qH5vFV99qD-5khom/images/power-bi/service-principal/register-an-application.png?w=560&fit=max&auto=format&n=qH5vFV99qD-5khom&q=85&s=a2407102e575fc8798086244a438e1bc 560w, https://mintcdn.com/datafold/qH5vFV99qD-5khom/images/power-bi/service-principal/register-an-application.png?w=840&fit=max&auto=format&n=qH5vFV99qD-5khom&q=85&s=8c7941bbeba3bb159c7b234c866be2f7 840w, https://mintcdn.com/datafold/qH5vFV99qD-5khom/images/power-bi/service-principal/register-an-application.png?w=1100&fit=max&auto=format&n=qH5vFV99qD-5khom&q=85&s=cfce71d6fc75cfb008bbfc04dada6210 1100w, https://mintcdn.com/datafold/qH5vFV99qD-5khom/images/power-bi/service-principal/register-an-application.png?w=1650&fit=max&auto=format&n=qH5vFV99qD-5khom&q=85&s=aaec689006f4a031f224cf028ff1ccbb 1650w, https://mintcdn.com/datafold/qH5vFV99qD-5khom/images/power-bi/service-principal/register-an-application.png?w=2500&fit=max&auto=format&n=qH5vFV99qD-5khom&q=85&s=716fea1d42ee355f54e956a0b1bce10a 2500w" />
        </Frame>

        3. Click **Register**
        4. Note the **Application (client) ID** and **Directory (tenant) ID** from the Overview page
      </Step>

      <Step title="Create a Client Secret">
        1. In the App Registration, go to **Certificates & secrets**
        2. Click **New client secret**
        3. Add a description (e.g., "Datafold integration") and choose an expiration period
        4. Click **Add**

        <Frame>
          <img src="https://mintcdn.com/datafold/qH5vFV99qD-5khom/images/power-bi/service-principal/certificates-and-secrets.png?fit=max&auto=format&n=qH5vFV99qD-5khom&q=85&s=f0f35b46b7c6d692f7737c5261412c9d" data-og-width="2696" width="2696" data-og-height="1046" height="1046" data-path="images/power-bi/service-principal/certificates-and-secrets.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/qH5vFV99qD-5khom/images/power-bi/service-principal/certificates-and-secrets.png?w=280&fit=max&auto=format&n=qH5vFV99qD-5khom&q=85&s=8a64ed8fcaee07adb337e1fe7ea5a1fa 280w, https://mintcdn.com/datafold/qH5vFV99qD-5khom/images/power-bi/service-principal/certificates-and-secrets.png?w=560&fit=max&auto=format&n=qH5vFV99qD-5khom&q=85&s=64083cb44bde1ca7aa86e4f7d478ed10 560w, https://mintcdn.com/datafold/qH5vFV99qD-5khom/images/power-bi/service-principal/certificates-and-secrets.png?w=840&fit=max&auto=format&n=qH5vFV99qD-5khom&q=85&s=1a2756a5de48d2c6fcc435e2b64ebd71 840w, https://mintcdn.com/datafold/qH5vFV99qD-5khom/images/power-bi/service-principal/certificates-and-secrets.png?w=1100&fit=max&auto=format&n=qH5vFV99qD-5khom&q=85&s=ab7453b127aec164b91ac38f311d4a6d 1100w, https://mintcdn.com/datafold/qH5vFV99qD-5khom/images/power-bi/service-principal/certificates-and-secrets.png?w=1650&fit=max&auto=format&n=qH5vFV99qD-5khom&q=85&s=73fcf12b62abdcc17b002e1e6ed59b42 1650w, https://mintcdn.com/datafold/qH5vFV99qD-5khom/images/power-bi/service-principal/certificates-and-secrets.png?w=2500&fit=max&auto=format&n=qH5vFV99qD-5khom&q=85&s=9a6f19142eebc2fcfe39ad3c3b4e19d2 2500w" />
        </Frame>

        5. **Important**: Copy the secret **Value** immediately—it won't be shown again
      </Step>

      <Step title="Create a Security Group">
        1. Go to [Microsoft Entra admin center - Groups](https://entra.microsoft.com/?l=en.en-us#view/Microsoft_AAD_IAM/AddGroupBlade)
        2. Click **New group**
        3. Configure:
           * **Group type**: Security
           * **Group name**: `Power BI Service Principals` (or similar)
           * **Group description**: "Service principals allowed to access Power BI APIs"
           * **Membership type**: Assigned
        4. In the **Members** section, click **Add members**
        5. Search for and add your App Registration (by name or Client ID)

        <Frame>
          <img src="https://mintcdn.com/datafold/qH5vFV99qD-5khom/images/power-bi/service-principal/new-group.png?fit=max&auto=format&n=qH5vFV99qD-5khom&q=85&s=77ccc8b428b414d0a904d7eea4e86f24" data-og-width="2696" width="2696" data-og-height="1046" height="1046" data-path="images/power-bi/service-principal/new-group.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/qH5vFV99qD-5khom/images/power-bi/service-principal/new-group.png?w=280&fit=max&auto=format&n=qH5vFV99qD-5khom&q=85&s=cd9e7459323c08af99c834b37f177ab3 280w, https://mintcdn.com/datafold/qH5vFV99qD-5khom/images/power-bi/service-principal/new-group.png?w=560&fit=max&auto=format&n=qH5vFV99qD-5khom&q=85&s=14f129e9b7e4292bbebd15ff7823310f 560w, https://mintcdn.com/datafold/qH5vFV99qD-5khom/images/power-bi/service-principal/new-group.png?w=840&fit=max&auto=format&n=qH5vFV99qD-5khom&q=85&s=2dc0f50fb920bb73cbe9778d11b9c7d4 840w, https://mintcdn.com/datafold/qH5vFV99qD-5khom/images/power-bi/service-principal/new-group.png?w=1100&fit=max&auto=format&n=qH5vFV99qD-5khom&q=85&s=e7b46b493b4d995871b2950695a460e6 1100w, https://mintcdn.com/datafold/qH5vFV99qD-5khom/images/power-bi/service-principal/new-group.png?w=1650&fit=max&auto=format&n=qH5vFV99qD-5khom&q=85&s=792abef80ac604019b35412f7c16e719 1650w, https://mintcdn.com/datafold/qH5vFV99qD-5khom/images/power-bi/service-principal/new-group.png?w=2500&fit=max&auto=format&n=qH5vFV99qD-5khom&q=85&s=7bf0a4b767bf717826635083ae2af61f 2500w" />
        </Frame>

        6. Click **Create**
      </Step>

      <Step title="Configure Power BI Admin Portal">
        1. Go to [Power BI Admin Portal](https://app.powerbi.com/admin-portal/tenantSettings)
        2. Navigate to **Tenant settings**
        3. Enable these settings and apply them to your security group (or to the whole organization, as you see fit):

        * **Allow service principals to use Power BI APIs**
        * **Allow service principals to use read-only admin APIs**
        * **Enhance admin APIs responses with detailed metadata**
        * **Enhance admin APIs responses with DAX and mashup expressions**

        <Frame>
          <img src="https://mintcdn.com/datafold/qH5vFV99qD-5khom/images/power-bi/service-principal/power-bi-admin-api-settings.png?fit=max&auto=format&n=qH5vFV99qD-5khom&q=85&s=e490901f5013423f0e9e996bec7d86ea" data-og-width="2696" width="2696" data-og-height="1046" height="1046" data-path="images/power-bi/service-principal/power-bi-admin-api-settings.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/qH5vFV99qD-5khom/images/power-bi/service-principal/power-bi-admin-api-settings.png?w=280&fit=max&auto=format&n=qH5vFV99qD-5khom&q=85&s=469bb12f11163e10742255171e16de48 280w, https://mintcdn.com/datafold/qH5vFV99qD-5khom/images/power-bi/service-principal/power-bi-admin-api-settings.png?w=560&fit=max&auto=format&n=qH5vFV99qD-5khom&q=85&s=c037f8ee55e49f5b82e01ed258f482f8 560w, https://mintcdn.com/datafold/qH5vFV99qD-5khom/images/power-bi/service-principal/power-bi-admin-api-settings.png?w=840&fit=max&auto=format&n=qH5vFV99qD-5khom&q=85&s=76874fd0e33a22042bee94586ea6878c 840w, https://mintcdn.com/datafold/qH5vFV99qD-5khom/images/power-bi/service-principal/power-bi-admin-api-settings.png?w=1100&fit=max&auto=format&n=qH5vFV99qD-5khom&q=85&s=44e0d035d20235d26311cba34be76f6c 1100w, https://mintcdn.com/datafold/qH5vFV99qD-5khom/images/power-bi/service-principal/power-bi-admin-api-settings.png?w=1650&fit=max&auto=format&n=qH5vFV99qD-5khom&q=85&s=38069d9467584fb805c55696b9bafcdc 1650w, https://mintcdn.com/datafold/qH5vFV99qD-5khom/images/power-bi/service-principal/power-bi-admin-api-settings.png?w=2500&fit=max&auto=format&n=qH5vFV99qD-5khom&q=85&s=21463bb3faa0204d3df7836114a21a1b 2500w" />
        </Frame>
      </Step>

      <Step title="Grant Workspace Access">
        You must explicitly grant access to each workspace you want Datafold to sync:

        1. Open the Power BI workspace you want to sync
        2. Click **Access** (or the gear icon -> Manage access)

        <Frame>
          <img src="https://mintcdn.com/datafold/qH5vFV99qD-5khom/images/power-bi/service-principal/manage-access.png?fit=max&auto=format&n=qH5vFV99qD-5khom&q=85&s=25cc38c99e8da06fd3eb81caf97013fd" data-og-width="2696" width="2696" data-og-height="1046" height="1046" data-path="images/power-bi/service-principal/manage-access.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/qH5vFV99qD-5khom/images/power-bi/service-principal/manage-access.png?w=280&fit=max&auto=format&n=qH5vFV99qD-5khom&q=85&s=b9e36551fe9d1a4d704988dbd8d58c53 280w, https://mintcdn.com/datafold/qH5vFV99qD-5khom/images/power-bi/service-principal/manage-access.png?w=560&fit=max&auto=format&n=qH5vFV99qD-5khom&q=85&s=1e41c44b915ae0437ed63436aea58330 560w, https://mintcdn.com/datafold/qH5vFV99qD-5khom/images/power-bi/service-principal/manage-access.png?w=840&fit=max&auto=format&n=qH5vFV99qD-5khom&q=85&s=ffa56ed8a2961a23aa25e2f51dc385a8 840w, https://mintcdn.com/datafold/qH5vFV99qD-5khom/images/power-bi/service-principal/manage-access.png?w=1100&fit=max&auto=format&n=qH5vFV99qD-5khom&q=85&s=22ffbb37580e3e2aaba1c9ae128b54ee 1100w, https://mintcdn.com/datafold/qH5vFV99qD-5khom/images/power-bi/service-principal/manage-access.png?w=1650&fit=max&auto=format&n=qH5vFV99qD-5khom&q=85&s=06981fbcbfc06c50a792b437f26b219e 1650w, https://mintcdn.com/datafold/qH5vFV99qD-5khom/images/power-bi/service-principal/manage-access.png?w=2500&fit=max&auto=format&n=qH5vFV99qD-5khom&q=85&s=db78d67572858824c86b8dc7263fe9ac 2500w" />
        </Frame>

        3. Add your App Registration as an **Admin** or **Member**
        4. Repeat for each workspace you want Datafold to access
      </Step>

      <Step title="Configure Datafold">
        1. Go to Datafold -> **Settings** -> **BI & Data Apps**
        2. Click **+ Add new integration** -> **Power BI**
        3. Select **Service Principal** as the authentication type
        4. Enter the credentials:
           * **Client ID**: The Application (client) ID from Step 1
           * **Client Secret**: The secret value from Step 2
           * **Tenant ID**: The Directory (tenant) ID from Step 1

        <Frame>
          <img src="https://mintcdn.com/datafold/qH5vFV99qD-5khom/images/power-bi/service-principal/new-integration-service-principal.png?fit=max&auto=format&n=qH5vFV99qD-5khom&q=85&s=461a583185c280df56a716c310aef123" data-og-width="2696" width="2696" data-og-height="1046" height="1046" data-path="images/power-bi/service-principal/new-integration-service-principal.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/qH5vFV99qD-5khom/images/power-bi/service-principal/new-integration-service-principal.png?w=280&fit=max&auto=format&n=qH5vFV99qD-5khom&q=85&s=7c326a5fca5c30047ed9972a7a44ce98 280w, https://mintcdn.com/datafold/qH5vFV99qD-5khom/images/power-bi/service-principal/new-integration-service-principal.png?w=560&fit=max&auto=format&n=qH5vFV99qD-5khom&q=85&s=a2ac31fee9a880e9292a9f2af53891d0 560w, https://mintcdn.com/datafold/qH5vFV99qD-5khom/images/power-bi/service-principal/new-integration-service-principal.png?w=840&fit=max&auto=format&n=qH5vFV99qD-5khom&q=85&s=0878b56c8ad6b2bd77de2b1e944d7e36 840w, https://mintcdn.com/datafold/qH5vFV99qD-5khom/images/power-bi/service-principal/new-integration-service-principal.png?w=1100&fit=max&auto=format&n=qH5vFV99qD-5khom&q=85&s=ec2d6551cefa8811763bdcc5b8f4e8de 1100w, https://mintcdn.com/datafold/qH5vFV99qD-5khom/images/power-bi/service-principal/new-integration-service-principal.png?w=1650&fit=max&auto=format&n=qH5vFV99qD-5khom&q=85&s=e36d7b550382c2bd1b64446851de2857 1650w, https://mintcdn.com/datafold/qH5vFV99qD-5khom/images/power-bi/service-principal/new-integration-service-principal.png?w=2500&fit=max&auto=format&n=qH5vFV99qD-5khom&q=85&s=4a243255b6b97ec594a6c784d76ca710 2500w" />
        </Frame>

        5. Click **Save**
      </Step>
    </Steps>
  </Tab>
</Tabs>

## Verify the integration

<Steps>
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
