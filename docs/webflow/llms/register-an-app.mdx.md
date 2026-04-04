# Source: https://developers.webflow.com/data/docs/register-an-app.mdx

***

title: Register an App
slug: data/docs/register-an-app
description: Create your first Webflow App in minutes
hidden: false
'og:title': 'Getting Started with Webflow Apps: Register an App'
'og:description': Create your first Webflow App in minutes
----------------------------------------------------------

To start developing a Webflow App, you'll first need to register an app to a workspace. This guide will walk you through creating and registering your app with Webflow.

## Watch: How to register a Webflow App

<iframe width="100%" height="400" src="https://www.youtube.com/embed/rfEkIB0_ZDA?start=102" title="How to register a Webflow App" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen />

## Prerequisites

* A Webflow account.
* A Webflow Workspace with Admin permissions.

<Warning title="Admin access required">
  Only Workspace admins can create apps, view client secrets, upload bundles, and modify app settings.
</Warning>

## Register an app

![Webflow Dashboard](https://files.buildwithfern.com/https://webflow.docs.buildwithfern.com/d5af2bfd73559d94bb617df3760dd5164a00eff22cb6164715eacd13a64f827a/products/data/pages/Apps/getting-started-apps/register-an-app/Webflow-Dashboard.png)

<Note title="App installations for external users">
  New apps are only available to users in your app's workspace. By default, external users can't install your app until it's approved and published in the Webflow Marketplace.

  You can test your app with external users before submitting for review. See the [user testing instructions](/apps/docs/marketplace/overview#user-testing-before-publishing) for details.
</Note>

<Steps>
  ### Open the Webflow Dashboard

  Login to your Webflow account and navigate to your Dashboard.

  ### Choose a Workspace

  Select the Workspace for your app. While you can use any workspace, it's recommended to create a dedicated development workspace to keep your apps organized and separate from production environments.

  <Note title="New to Webflow?">
    Get started with Webflow's [free Developer Workspace](/data/docs/developer-workspace) designed for testing and developing Apps.
  </Note>

  ### Navigate to Workspace settings

  From the "settings" menu on the left sidebar, select the "Apps & Integrations" tab. Scroll down to the "App Development" section and click the "Create an App" button. This will open the App creation modal.

  <Frame background="subtle">
    ![App Development section](https://files.buildwithfern.com/https://webflow.docs.buildwithfern.com/4ab65f7265756f55c267c7b3ab1bf2196bd7d937133b251c2917a6af073157c2/products/data/pages/Apps/getting-started-apps/register-an-app/App-Development.png)
  </Frame>

  ### Add app details

  <Frame background="subtle"> ![App Details](https://files.buildwithfern.com/https://webflow.docs.buildwithfern.com/6cc205d25f4dce71de2585fc1eba464befddd8b87dfed8d638197b3d600d1066/products/data/pages/Apps/getting-started-apps/register-an-app/App-Details.png)</Frame>
  Here, you'll add the following basic information for your app:

  * **Name:** The name of your app
  * **Description:** A brief summary of your app's purpose (140 characters max)
  * **Icon:** An icon to represent your app
  * **Homepage URL:** A valid HTTPS link to your app's website

  For more details on how your App will appear in the Marketplace, see the [app listing guide](/apps/docs/marketplace/listing-your-app).

  <Accordion title="Installation settings (optional)">
    You can configure your app's installation scope by toggling the "Restrict app installation to a specific site" option. When enabled, users will only be able to authorize your app for a single site at a time, providing more granular control over permissions. When disabled (default), users can authorize your app for multiple sites or their entire Workspace at once, which is convenient for apps that need broader access. Choose the option that best aligns with your app's security requirements and user experience.
  </Accordion>

  ### Define App capabilities

  Click the "Continue" button to define your App's capabilities.

  <Frame background="subtle">
     

    ![App Capabilities](https://files.buildwithfern.com/https://webflow.docs.buildwithfern.com/ea35928839fea44cda18a2382e37f5be34e2646520fcb1072d461c03d6fb7e7f/products/data/pages/Apps/getting-started-apps/register-an-app/select-scopes.gif)
  </Frame>

  Here, you'll select the capabilities your App needs to function. You can choose from the following capabilities:

  * **[Designer Extension](/apps/docs/designer-extensions):** Enables your App to interact with the Webflow Designer.
  * **[Data Client](/data/docs/data-clients):** Enables your App to access and update data from Webflow's servers.

  You can select one or both of these capabilities. [Selecting both will allow your App to interact with both Webflow's servers and the Webflow Designer as a hybrid app.](/apps/docs/hybrid-apps)

  <Accordion title="Data Client: OAuth configuration">
    If you've selected the Data Client capability, you'll need to configure OAuth settings for your app:

    * **Select scopes:** Choose the specific API permissions your app requires to function properly. Each scope grants access to different Webflow resources such as sites, collections, or assets. [Learn more about available scopes in our guide.](/data/reference/scopes)
    * **Add redirect URI:** Enter a valid HTTPS URL where users will be redirected after authorizing your app. This is a critical security component of the OAuth flow that ensures authorization codes are only sent to trusted destinations. [Learn more about implementing OAuth authentication](/data/reference/oauth-app). You can add or modify redirect URIs later as needed.
  </Accordion>

  After configuring your app's capabilities and OAuth settings, click the "Create app" button to finalize the registration process.

  ### Review your App

  <Frame background="subtle">
    ![App details](https://files.buildwithfern.com/https://webflow.docs.buildwithfern.com/b69033ed6e835003a385e6bd83e7a2c4f56d32940e240cbe6abb7647e3db7a8b/products/data/pages/Apps/getting-started-apps/register-an-app/Completed-App-Details.png)
  </Frame>

  Congratulations! You've successfully registered your App in Webflow. On successful registration, your App will be displayed in the App Development section. You'll see key details including the Client ID and Client Secret. From here, you can also update your App's details, capabilities, and installation settings.

  <Accordion title="Designer Extension: App information">
    If you've selected the Designer Extension capability, you'll see additional information specific to Designer Extensions:

    * **Publish Extension Version:** This button will open a modal where you can upload a new version of your Designer Extension and add version notes. For detailed publishing instructions, see our [Publishing Designer Extensions guide](/apps/docs/publishing-your-app).

    * **Designer Extension URI:** The URI where your extension will be served within the Webflow Designer iframe. This URI is important when configuring CORS settings for your extension.

    * **Versions:** View all previously published versions of your Designer Extension. This helps you track your extension's version history and rollback if needed.
  </Accordion>

  <Warning title="App Security">
    * Never commit your Client Secret to version control
    * Rotate your Client Secret if it's ever exposed
    * Store secrets in environment variables or a secure secret management system
    * Implement proper CORS policies for Designer Extensions
  </Warning>
</Steps>

## Troubleshooting

<AccordionGroup>
  <Accordion title="Why am I getting an Invalid Redirect URI error?">
    When you receive an "Invalid Redirect URI" error during OAuth authorization, it typically means there's a mismatch between the URI you're using and what you registered. To resolve this:

    * Ensure the redirect URI matches **exactly** what you registered
    * Check for trailing slashes - `https://example.com/callback` and `https://example.com/callback/` are treated as different URIs
    * If using localhost for development, make sure the port number matches exactly
    * For Ngrok or other tunneling services, remember that the URL changes each time you restart the tunnel - update your registered URI accordingly
  </Accordion>

  <Accordion title="Why can't I see the app development section in my workspace settings?">
    Verify that:

    * You're in the correct Workspace
    * You have Admin permissions on the Workspace (only Workspace admins can view and manage apps)
    * Your account has been verified via email and has 2-factor authentication enabled
    * You've navigated to Workspace Settings > App Development (not Site Settings)
    * Your Webflow plan supports app development (available on Team and Enterprise plans)

    If you've confirmed all these requirements and still can't see the App Development section, try clearing your browser cache or using a different browser, then contact Webflow Support if the issue persists.
  </Accordion>

  <Accordion title="Why can't external users install my app?">
    New apps are only available to users in your app's workspace. External users can't install your app until it's approved and published in the Webflow Marketplace.

    You can invite external test users to your app before submitting for review. See the [user testing instructions](/data/docs/overview#user-testing-before-publishing) for details.
  </Accordion>
</AccordionGroup>

## Next steps

To see your new App in action, follow these Quickstart guides, which will get your App up and running in Webflow.

<CardGroup cols={3}>
  <Card
    title="Data Client"
    href="/data/docs/getting-started-data-clients"
    iconPosition="left"
    iconSize="10"
    icon={
    <>
      <img src="https://dhygzobemt712.cloudfront.net/Icons/Dark/64px/Switch.svg" alt="" className="hidden dark:block" />
      <img src="https://dhygzobemt712.cloudfront.net/Icons/Light/64px/Switch.svg" alt="" className="block dark:hidden" />
    </>
  }
  >
    Access and manipulate Webflow site data including CMS collections, items, assets, and form submissions through secure API endpoints.
  </Card>

  <Card
    title="Designer Extension"
    href="/designer/docs/getting-started-designer-extensions"
    iconPosition="left"
    iconSize="10"
    icon={
    <>
      <img src="https://dhygzobemt712.cloudfront.net/Icons/Dark/64px/Styles.svg" alt="" className="hidden dark:block" />
      <img src="https://dhygzobemt712.cloudfront.net/Icons/Light/64px/Styles.svg" alt="" className="block dark:hidden" />
    </>
  }
  >
    Create extensions that automate design tasks, manipulate elements, and enhance the Webflow Designer experience.
  </Card>

  <Card title="Hybrid App" href="/data/docs/hybrid-apps">
    Use both the Data Client and Designer Extension in tandem.
  </Card>
</CardGroup>
