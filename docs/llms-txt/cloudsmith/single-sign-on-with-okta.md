# Source: https://help.cloudsmith.io/docs/single-sign-on-with-okta.md

# Single Sign-On with Okta

This guide provides step-by-step instructions on setting up Okta as a SAML IdP for your Cloudsmith Organization.

## Adding Cloudsmith to Okta

Cloudsmith is not yet an integrated application in [Okta](https://www.okta.com/). You'll have to add Cloudsmith manually so you can configure SSO.

<HTMLBlock>
  {`
  <div class="cs-step"><span class="cs-step-desc cs-swatch-midnight-blue">Step</span><span class="cs-step-number cs-swatch-action-blue">1</span></div>
  `}
</HTMLBlock>

Log into Okta and click "Applications" and then "Create App Integration"

<Image align="center" width="80%" src="https://files.readme.io/c6fa9a9-okta-create-app-integration.png" />

You will then see a modal window pop up where you define the application details

<HTMLBlock>
  {`
  <div class="cs-step"><span class="cs-step-desc cs-swatch-midnight-blue">Step</span><span class="cs-step-number cs-swatch-action-blue">2</span></div>
  `}
</HTMLBlock>

Select SAML 2.0 and click next:

<Image align="center" className="border" width="80%" border={true} src="https://files.readme.io/6476b61-okta-create-app-integration-modal.png" />

<HTMLBlock>
  {`
  <div class="cs-step"><span class="cs-step-desc cs-swatch-midnight-blue">Step</span><span class="cs-step-number cs-swatch-action-blue">3</span></div>
  `}
</HTMLBlock>

On the next screen (General Settings), enter the App name as "Cloudsmith". (You can optionally add the Cloudsmith logo too for easier visibility, you can find hi-res versions of the logo [here](https://cloudsmith.io/branding/)):

<Image align="center" width="80%" src="https://files.readme.io/48b6395-okta-create-app-integration-step1.png" />

<HTMLBlock>
  {`
  <div class="cs-step"><span class="cs-step-desc cs-swatch-midnight-blue">Step</span><span class="cs-step-number cs-swatch-action-blue">4</span></div>
  `}
</HTMLBlock>

Next, we'll configure SAML settings. To determine your **Single sign on URL** use the following format:

```
https://cloudsmith.io/orgs/{ACCOUNT}/saml/acs/
```

Where `{ACCOUNT}` is your Cloudsmith organization identifier (slug).

We use the same URL for the **Audience URI** value.

For **Name ID Format** choose "EmailAddress"\
For **Application username** choose "Email".

<Image align="center" className="border" width="80%" border={true} src="https://files.readme.io/4e5b80b-okta-create-app-integration-step2.png" />

<HTMLBlock>
  {`
  <div class="cs-step"><span class="cs-step-desc cs-swatch-midnight-blue">Step</span><span class="cs-step-number cs-swatch-action-blue">5</span></div>
  `}
</HTMLBlock>

Next, we'll configure Okta to also send the user's first and last names during sign-in:

<Image align="center" width="80%" src="https://files.readme.io/3d740f0-okta-create-app-integration-sttribute-statements.png" />

Then click the blue **Next** button at the bottom of the page.

<HTMLBlock>
  {`
  <div class="cs-step"><span class="cs-step-desc cs-swatch-midnight-blue">Step</span><span class="cs-step-number cs-swatch-action-blue">6</span></div>
  `}
</HTMLBlock>

Fill out the **Feedback** section on the next page and click the blue **Finish** button:

<Image align="center" width="80%" src="https://files.readme.io/e16e76b-okta-create-app-integration-step3.png" />

<HTMLBlock>
  {`
  <div class="cs-step"><span class="cs-step-desc cs-swatch-midnight-blue">Step</span><span class="cs-step-number cs-swatch-action-blue">7</span></div>
  `}
</HTMLBlock>

Your application is now configured on Okta and you can add users and groups as required using the **Assignments** tab of your application management screen:

<Image align="center" width="80%" src="https://files.readme.io/d48b24a-okta-assign-people.png" />

## Providing configuration to Cloudsmith

Once configured as above, you'll need to provide metadata to Cloudsmith to connect to your newly configured IdP.

In the **Sign On** tab of your application management screen, you can see a link to view the IdP metadata (under SAML Signing Certificates):

<Image align="center" width="80%" src="https://files.readme.io/636281f-okta-saml-metadata.png" />

Copy this metadata and add it to your Cloudsmith organization [SAML settings](https://help.cloudsmith.io/docs/organisations#saml-authentication) as Inline XML.

You can then [enable SAML authentication](https://help.cloudsmith.io/docs/single-sign-on#enable-saml) in your Cloudsmith organization, and you can use Okta to begin logging in straight away.

You'll be able to access the landing page of your organization at the following URL:

```
https://app.cloudsmith.com/{ACCOUNT}/saml/login/
```

Where `{ACCOUNT}` is your organization's slug/identifier (what you would normally see in the URL when accessing your organization within Cloudsmith). If you're unsure what this is, please just [contact us](https://help.cloudsmith.io/docs/contact-us)!

You can also optionally set up [SAML Group Sync mappings](https://help.cloudsmith.io/reference/orgs_saml-group-sync_create) to automatically map OKTA groups to teams in your Cloudsmith organization, and SCIM to provision, deprovision and update user profile information.

## SAML Group Sync

Once SAML has been setup, group sync can then be configured in order to automatically assign teams from your OKTA directory to Cloudsmith.

In order to get started, go to your Cloudsmith application in OKTA and click on the **General** tab:

![](https://files.readme.io/aa6b34a-image.png)

Under **SAML Settings** click **Edit**:

![](https://files.readme.io/d1568be-image.png)

Click **Next** to proceed to step 2 and under **A** section on the very bottom **(Group Attribute Statements)** insert the name of the group from Okta along with the valid filter, for example, a group called "Dev" in OKTA will look like this:

![](https://files.readme.io/1430b35-image.png)

The attribute for the group:

![](https://files.readme.io/04b7376-image.png)

Once all desired groups are inserted in Okta, you can now configure the group mapping in Cloudsmith. In your Cloudsmith workspace, go to "Settings" -> "Authentication" -> "SAML Group Sync", click "Enable SAML Group Sync" then "Create Group Sync Mapping".

The name and value will be the same as the group attribute created in OKTA:

<Image alt="Create SAML Group Sync Mapping" align="center" src="https://files.readme.io/f644e56a69fe3fea8d0371a39d146a7ce36412a4fc498f1dfd88f5633b7bb368-sso-with-okta-screenshot4.png">
  Create SAML Group Sync Mapping
</Image>

> 📘 To test SAML Group Sync, the user must re-log for the sync to apply.

## SCIM

SCIM, or System for Cross-domain Identity Management, is an open standard designed to manage user identity information. Cloudsmith is SCIM 2.0-compliant. With Cloudsmith's support for SCIM, you can automatically provision new users, de-provision existing users and update existing users profile information based on changes within your idP.

To get started using SCIM, go to "Settings" -> "Authentication" -> "SCIM" and "Allow SCIM":

<Image alt="Allow SCIM in your Cloudsmith workspace" align="center" src="https://files.readme.io/03aa91ea5a1b2107d0582299e5bbc1e9904eea098733f1dbec45afd5ab65009b-sso-okta-scim-edited.png">
  Allow SCIM in your Cloudsmith workspace
</Image>

Once SCIM functionality is allowed in Cloudsmith, you then enable SCIM for the Cloudsmith application in Okta on the "General" tab:

<Image title="Screenshot 2022-11-15 at 10.00.08.png" alt={1087} align="center" src="https://files.readme.io/ae20261-Screenshot_2022-11-15_at_10.00.08.png">
  Okta Enable SCIM
</Image>

You then use the "Provisioning" tab to configure SCIM as follows:

<Image title="Screenshot 2022-11-15 at 10.04.53.png" alt={1055} align="center" src="https://files.readme.io/a4625db-Provisioning.png">
  Okta Configure SCIM
</Image>

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th />

      <th />
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        SCIM Connector base URL
      </td>

      <td>
        [https://api.cloudsmith.io/scim/v2](https://api.cloudsmith.io/scim/v2)
      </td>
    </tr>

    <tr>
      <td>
        Unique Identifier for users
      </td>

      <td>
        email
      </td>
    </tr>

    <tr>
      <td>
        Supported provisioning actions
      </td>

      <td>
        Push New Users\
        Push Profile Updates
      </td>
    </tr>

    <tr>
      <td>
        Authentication Mode
      </td>

      <td>
        Basic Auth
      </td>
    </tr>

    <tr>
      <td>
        Basic Auth Username
      </td>

      <td>
        token
      </td>
    </tr>

    <tr>
      <td>
        Basic Auth Password
      </td>

      <td>
        In your Cloudsmith workspace, go to "Settings" -> "Authentication" -> "SCIM" to retrieve your password token.
      </td>
    </tr>
  </tbody>
</Table>

Then test and save the configuration.

Once saved, you can then enable the "Create Users", "Update User Attributes" and "Deactivate Users" functionality via the "Provisioning" > "To App" tab:

<Image align="center" src="https://files.readme.io/93fc9ed-To_app.png" />

Okta is now configured to provision, update and de-provision users from your Cloudsmith organization.