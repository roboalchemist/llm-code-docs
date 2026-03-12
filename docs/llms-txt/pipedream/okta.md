# Source: https://pipedream.com/docs/workspaces/sso/okta.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://pipedream.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Configure SSO With Okta

Pipedream supports Single Sign-On (SSO) with Okta. This guide shows you how to configure SSO in Pipedream to authenticate with your Okta org.

## Requirements

* SSO is only supported for [workspaces](/workspaces/) on the Business plan. Visit the [Pipedream pricing page](https://pipedream.com/pricing) to upgrade.
* You must be an administrator of your Pipedream workspace
* You must have an Okta account

## Configuration

<Steps>
  <Step title="Visit your Okta dashboard">
    In your Okta **Admin** dashboard, select the **Applications** section and click **Applications** below that:

    <Frame>
      <img src="https://mintcdn.com/pipedream/Acz4Z1ch6TM7-aI8/images/bac60372-image.png?fit=max&auto=format&n=Acz4Z1ch6TM7-aI8&q=85&s=4243b43948e6492e135eb558a59e0ec5" width="528" height="616" data-path="images/bac60372-image.png" />
    </Frame>
  </Step>

  <Step title="Browse App Catalog">
    Click **Browse App Catalog**:

    <Frame>
      <img src="https://mintcdn.com/pipedream/h8oodpUDiyR1Ssvt/images/326e546a-step-2_iv1a2c.png?fit=max&auto=format&n=h8oodpUDiyR1Ssvt&q=85&s=941b97d6ca154cc24ec9b1e497205b2c" width="784" height="272" data-path="images/326e546a-step-2_iv1a2c.png" />
    </Frame>
  </Step>

  <Step title="Search for Pipedream">
    Search for “Pipedream” and select the Pipedream app:

    <Frame>
      <img src="https://mintcdn.com/pipedream/grEzwYhEB2vZSwGw/images/8b6bb035-step-3_z2buml.png?fit=max&auto=format&n=grEzwYhEB2vZSwGw&q=85&s=21e1ebd4abc8154596d5a20f80d889c8" width="2078" height="538" data-path="images/8b6bb035-step-3_z2buml.png" />
    </Frame>
  </Step>

  <Step title="Click Add">
    <Frame>
      <img src="https://mintcdn.com/pipedream/xnRKrRxEtt3vxd6I/images/d80f8bb6-step-4_mfd5bs.png?fit=max&auto=format&n=xnRKrRxEtt3vxd6I&q=85&s=3be608ef02cd5863436ab11abde3718d" width="2122" height="1188" data-path="images/d80f8bb6-step-4_mfd5bs.png" />
    </Frame>
  </Step>

  <Step title="Configure General Settings">
    Fill out the **General Settings** that Okta presents, and click **Done**:

    <Frame>
      <img src="https://mintcdn.com/pipedream/anb6FA0wpd8jtdUB/images/55dec310-step-5_fqmywz.png?fit=max&auto=format&n=anb6FA0wpd8jtdUB&q=85&s=c9b93bf5ebb3f1058f5300f065d39cb0" width="1544" height="1056" data-path="images/55dec310-step-5_fqmywz.png" />
    </Frame>
  </Step>

  <Step title="Edit Sign On">
    Select the **Sign On** tab, and click **Edit** at the top right:

    <Frame>
      <img src="https://mintcdn.com/pipedream/xnRKrRxEtt3vxd6I/images/c62f9570-step-6_zzeeul.png?fit=max&auto=format&n=xnRKrRxEtt3vxd6I&q=85&s=2ea3bc9a9cb51a93a5fe452b5adb4b9a" width="1556" height="1414" data-path="images/c62f9570-step-6_zzeeul.png" />
    </Frame>
  </Step>

  <Step title="Configure Default Relay State">
    Scroll down to the **SAML 2.0** settings. In the **Default Relay State** section, enter `organization_username`:

    <Frame>
      <img src="https://mintcdn.com/pipedream/h8oodpUDiyR1Ssvt/images/4c74f713-step-7_dqtq43.png?fit=max&auto=format&n=h8oodpUDiyR1Ssvt&q=85&s=c928c48bde2ce157e493b9bbca689c2a" width="1384" height="800" data-path="images/4c74f713-step-7_dqtq43.png" />
    </Frame>
  </Step>

  <Step title="Save your configuration">
    Set any other configuration options you need in that section or in the **Credentials Details** section, and click **Save**.
  </Step>

  <Step title="Copy the Identity Provider metadata URL">
    In the **Sign On** section, you’ll see a section that includes the setup instructions for SAML:

    <Frame caption="Okta - SAML">
      <img src="https://mintcdn.com/pipedream/grEzwYhEB2vZSwGw/images/802edbf0-step-9-1_ucbq6e.png?fit=max&auto=format&n=grEzwYhEB2vZSwGw&q=85&s=2df6ddfa773a1f9222c2d1a938d5f5ca" width="1398" height="1999" data-path="images/802edbf0-step-9-1_ucbq6e.png" />
    </Frame>

    Click the **Identity Provider metadata** link and copy the URL from your browser’s address bar:

    <Frame>
      <img src="https://mintcdn.com/pipedream/h8oodpUDiyR1Ssvt/images/2ed51a1b-step-9-2_nlrois.png?fit=max&auto=format&n=h8oodpUDiyR1Ssvt&q=85&s=00212be941d4acad76195507fa592e7b" width="1748" height="412" data-path="images/2ed51a1b-step-9-2_nlrois.png" />
    </Frame>
  </Step>

  <Step title="Enable SSO in Pipedream">
    Visit your [Pipedream workspace authentication settings](https://pipedream.com/settings/authentication). Click the toggle to **Enable SSO**, then click **Edit SSO Configuration**, and add the metadata URL in the **SAML** section and click **Save**:

    <Frame>
      <img src="https://mintcdn.com/pipedream/NF77kliJSewMqg65/images/0a43ec81-pipedream.com_settings_authentication_3_dtt5fa.png?fit=max&auto=format&n=NF77kliJSewMqg65&q=85&s=db493454d8209faa096c83ad03527d73" width="1280" height="862" data-path="images/0a43ec81-pipedream.com_settings_authentication_3_dtt5fa.png" />
    </Frame>
  </Step>

  <Step title="Assign the application to users">
    Back in Okta, click on the **Assignments** tab of the Pipedream application. Click on the **Assign** dropdown and select **Assign to People**:

    <Frame>
      <img src="https://mintcdn.com/pipedream/grEzwYhEB2vZSwGw/images/875682d5-step-11_i8wm6k.png?fit=max&auto=format&n=grEzwYhEB2vZSwGw&q=85&s=c23b4006685ef3d1bf32976425c3eef8" width="1508" height="1018" data-path="images/875682d5-step-11_i8wm6k.png" />
    </Frame>

    Assign the application to the relevant users in Okta, and Pipedream will configure the associated accounts on our end.
  </Step>
</Steps>

Users configured in your Okta app can log into Pipedream at [https://pipedream.com/auth/sso](https://pipedream.com/auth/sso) by entering your workspaces’s name (found in your [Settings](https://pipedream.com/settings/account)). You can also access your SSO sign in URL directly by visiting [https://pipedream.com/auth/org/your-workspace-name](https://pipedream.com/auth/org), where `your-workspace-name` is the name of your workspace.

## Important details

Before you configure the application in Okta, make sure all your users have matching email addresses for their Pipedream user profile and their Okta profile. Once SSO is enabled, they will not be able to change their Pipedream email address.

If a user’s Pipedream email does not match the email in their IDP profile, they will not be able to log in.

If existing users signed up for Pipedream using an email and password, they will no longer be able to do so. They will only be able to sign in using SSO.

Built with [Mintlify](https://mintlify.com).
