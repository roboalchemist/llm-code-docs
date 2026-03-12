# Source: https://pipedream.com/docs/workspaces/sso/google.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://pipedream.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Configure SSO With Google Workspace

Pipedream supports Single Sign-On (SSO) with Google Workspace. This guide shows you how to configure SSO in Pipedream to authenticate with your Google org.

## Requirements

* SSO is only supported for [workspaces](/workspaces/) on the Business plan. Visit the [Pipedream pricing page](https://pipedream.com/pricing) to upgrade.
* You need an administrator of your Pipedream workspace and someone who can [create SAML apps in Google Workspace](https://apps.google.com/supportwidget/articlehome?hl=en\&article_url=https%3A%2F%2Fsupport.google.com%2Fa%2Fanswer%2F6087519%3Fhl%3Den\&assistant_id=generic-unu\&product_context=6087519\&product_name=UnuFlow\&trigger_context=a) to configure SSO.

## Configuration

To configure SSO in Pipedream, you need to set up a [SAML application](https://apps.google.com/supportwidget/articlehome?hl=en\&article_url=https%3A%2F%2Fsupport.google.com%2Fa%2Fanswer%2F6087519%3Fhl%3Den\&assistant_id=generic-unu\&product_context=6087519\&product_name=UnuFlow\&trigger_context=a) in Google Workspace. If you’re a Google Workspace admin, you’re all set. Otherwise, coordinate with a Google Workspace admin before you continue.

<Steps>
  <Step title="Find Web and Mobile apps in Google Workspace">
    In your **Google Workspace** admin console, select **Apps** > **Web and Mobile apps**

    <Frame>
      <img src="https://mintcdn.com/pipedream/NF77kliJSewMqg65/images/1deab1af-Screenshot_2023-09-05_at_6.04.53_PM_kr9oe4.png?fit=max&auto=format&n=NF77kliJSewMqg65&q=85&s=c9e0b3c07a8e13912e2fe486c46483be" width="620" height="408" data-path="images/1deab1af-Screenshot_2023-09-05_at_6.04.53_PM_kr9oe4.png" />
    </Frame>
  </Step>

  <Step title="Add a custom SAML app">
    In the **Add app** menu, select the option to **Add custom SAML app**:

    <Frame>
      <img src="https://mintcdn.com/pipedream/nKh6d_6A4aXFb6xD/images/ea5ee8a5-Screenshot_2023-09-05_at_6.15.12_PM_jrzszg.png?fit=max&auto=format&n=nKh6d_6A4aXFb6xD&q=85&s=911079a3c7e390990797ca1bbc4eace3" width="806" height="570" data-path="images/ea5ee8a5-Screenshot_2023-09-05_at_6.15.12_PM_jrzszg.png" />
    </Frame>
  </Step>

  <Step title="Configure the app">
    First, add **Pipedream** as the app name, and an app description that makes sense for your organization:

    <Frame>
      <img src="https://mintcdn.com/pipedream/NF77kliJSewMqg65/images/093313a8-Screenshot_2023-09-05_at_6.31.46_PM_ggnyrq.png?fit=max&auto=format&n=NF77kliJSewMqg65&q=85&s=e0ba534c23c82e29fa584727b74d82a5" width="1352" height="558" data-path="images/093313a8-Screenshot_2023-09-05_at_6.31.46_PM_ggnyrq.png" />
    </Frame>
  </Step>

  <Step title="Continue past the configuration step">
    <Frame>
      <img src="https://mintcdn.com/pipedream/Acz4Z1ch6TM7-aI8/images/9c77ada8-Screenshot_2023-09-05_at_6.35.15_PM_imjbuy.png?fit=max&auto=format&n=Acz4Z1ch6TM7-aI8&q=85&s=c43b7eae3436f67407dfa4243e1c90e7" width="2800" height="862" data-path="images/9c77ada8-Screenshot_2023-09-05_at_6.35.15_PM_imjbuy.png" />
    </Frame>
  </Step>

  <Step title="Configure the Service provider details">
    In the **Service provider details**, provide the following values:

    * **ACS URL** — `https://api.pipedream.com/auth/saml/consume`
    * **Entity ID** — Pipedream
    * **Start URL** — `https://api.pipedream.com/auth/saml/<your workspace name>`

    replacing `<your workspace name>` with the workspace name at [https://pipedream.com/settings/account](https://pipedream.com/settings/account). For example, if your workspace name is `example-workspace`, your start URL will be `https://api.pipedream.com/auth/saml/example-workspace`.

    <Frame>
      <img src="https://mintcdn.com/pipedream/anb6FA0wpd8jtdUB/images/6b3c1a9a-Screenshot_2023-09-05_at_6.38.12_PM_wplrr0.png?fit=max&auto=format&n=anb6FA0wpd8jtdUB&q=85&s=0f65a925d887c5ce3ef4b632d97ee1dd" width="1432" height="720" data-path="images/6b3c1a9a-Screenshot_2023-09-05_at_6.38.12_PM_wplrr0.png" />
    </Frame>

    In the **Name ID** section, provide these values:

    * **Name ID format** — `EMAIL`
    * **Name ID** — Basic Information > Primary email

    then press **Continue**.

    <Frame>
      <img src="https://mintcdn.com/pipedream/grEzwYhEB2vZSwGw/images/939d0674-Screenshot_2023-09-05_at_6.55.40_PM_f9fgyr.png?fit=max&auto=format&n=grEzwYhEB2vZSwGw&q=85&s=9b81a9a2a1a5d14ba631ef3246d409d9" width="2072" height="728" data-path="images/939d0674-Screenshot_2023-09-05_at_6.55.40_PM_f9fgyr.png" />
    </Frame>
  </Step>

  <Step title="Configure the Attribute mapping">
    Once the app is configured, visit the **User access** section to add Google Workspace users to your Pipedream SAML app. See [step 14 of the Google Workspace SAML docs](https://apps.google.com/supportwidget/articlehome?hl=en\&article_url=https%3A%2F%2Fsupport.google.com%2Fa%2Fanswer%2F6087519%3Fhl%3Den\&assistant_id=generic-unu\&product_context=6087519\&product_name=UnuFlow\&trigger_context=a) for more detail.
  </Step>

  <Step title="Download and host the SAML metadata">
    Pipedream requires access to SAML metadata at a publicly-accessible URL. This communicates public metadata about the identity provider (Google Workspace) that Pipedream can use to configure the SAML setup in Pipedream.

    First, click the **Download Metadata** button on the left of the app configuration page:

    <Frame>
      <img src="https://mintcdn.com/pipedream/nKh6d_6A4aXFb6xD/images/f764938e-Screenshot_2023-09-06_at_11.47.33_AM_mez7j1.png?fit=max&auto=format&n=nKh6d_6A4aXFb6xD&q=85&s=6e2af6bf052f283444f3087134393ac7" width="744" height="584" data-path="images/f764938e-Screenshot_2023-09-06_at_11.47.33_AM_mez7j1.png" />
    </Frame>

    **Host this file on a public web server where Pipedream can access it via URL**, for example: `https://example.com/metadata.xml`. You’ll use that URL in the next step.
  </Step>

  <Step title="Visit your workspace’s authentication settings">
    In Pipedream, visit your workspace’s [authentication settings](https://pipedream.com/settings/authentication).
  </Step>

  <Step title="Add the SAML metadata URL">
    In the **Single Sign-On** section, select **SAML**, and add the URL from step 7 above in the **Metadata URL** field, then click Save.

    <Frame>
      <img src="https://mintcdn.com/pipedream/anb6FA0wpd8jtdUB/images/608d3932-saml-metadata-url_cxciur.png?fit=max&auto=format&n=anb6FA0wpd8jtdUB&q=85&s=477a80df389271b8e545b27ed9958136" width="2262" height="1575" data-path="images/608d3932-saml-metadata-url_cxciur.png" />
    </Frame>
  </Step>
</Steps>

Any user in your workspace can now log into Pipedream at [https://pipedream.com/auth/sso](https://pipedream.com/auth/sso) by entering your workspaces’s name (found in your [Settings](https://pipedream.com/settings/account)). You can also access your SSO sign in URL directly by visiting [https://pipedream.com/auth/org/your-workspace-name](https://pipedream.com/auth/org), where `your-workspace-name` is the name of your workspace.

## Important details

Before you configure the application in Google, make sure all your users have matching email addresses for their Pipedream user profile and their Google Workspace profile. Once SSO is enabled, they will not be able to change their Pipedream email address.

If a user’s Pipedream email does not match the email in their Google profile, they will not be able to log in.

If existing users signed up for Pipedream using an email and password, they will no longer be able to do so. They will only be able to sign in using SSO.

Built with [Mintlify](https://mintlify.com).
