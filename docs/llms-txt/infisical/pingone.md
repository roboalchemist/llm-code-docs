# Source: https://infisical.com/docs/documentation/platform/scim/pingone.md

> ## Documentation Index
> Fetch the complete documentation index at: https://infisical.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# PingOne SCIM

> Learn how to configure SCIM provisioning with PingOne for Infisical.

<Info>
  PingOne SCIM provisioning is a paid feature.

  If you're using Infisical Cloud, then it is available under the **Enterprise Tier**. If you're self-hosting Infisical,
  then you should contact [sales@infisical.com](mailto:sales@infisical.com) to purchase a self-hosted license to use it.
</Info>

Prerequisites:

* [Configure PingOne OIDC for Infisical](/documentation/platform/sso/pingone-oidc)

<Steps>
  <Step title="Create a SCIM token in Infisical">
    In Infisical, head to the **Single Sign-On (SSO)** page and select the **Provisioning** tab. Under SCIM Configuration,
    press the **Enable SCIM provisioning** toggle to allow PingOne to provision/deprovision users for your organization.

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/scim/scim-enable-provisioning.png" alt="SCIM enable provisioning" />

    Next, press **Manage SCIM Tokens** and then **Create** to generate a SCIM token for PingOne.

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/scim/scim-create-token.png" alt="SCIM create token" />

    Next, copy the **SCIM URL** and **New SCIM Token** to use when configuring SCIM in PingOne.

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/scim/scim-copy-token.png" alt="SCIM copy token" />
  </Step>

  <Step title="Add Users and Groups in PingOne">
    Inside your PingOne environment, navigate to Directory > Users. Add any users and/or groups to your application that you would like
    to be provisioned over to Infisical.

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/scim/pingone/pingone-create-user.png" alt="SCIM PingOne Users and Groups" />
  </Step>

  <Step title="Configure SCIM Connection in PingOne">
    **1. Create a new connection**

    In PingOne, head to Integrations > Provisioning, and inside provisioning, press the **Connections** tab. Here you'll see a plus icon to add a new connection.

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/scim/pingone/pingone-new-connection.png" alt="SCIM PingOne Connections" />

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/scim/pingone/pingone-new-connection-identity-store.png" alt="SCIM PingOne Connections" />

    Select the "Identity Store" option.

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/scim/pingone/pingone-connection-select-scim-outbound.png" alt="SCIM PingOne SCIM Outbound" />

    Search for the "SCIM Outbound" option to start the configuration process for SCIM. Finally, press the **Next** button. Give the connection a name and optionally add a description.

    **2. Configure the connection**

    Once you have selected the SCIM Outbound option, you'll be prompted to enter the authentication details that PingOne will use to authenticate with Infisical SCIM. This is the **SCIM URL** and **New SCIM Token** from the previous step.

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/scim/pingone/pingone-connection-auth.png" alt="SCIM PingOne SCIM Outbound" />

    Set the following fields:

    * `SCIM BASE URL`: Input the **SCIM URL** from the previous step.
    * `Users Resource`: Leave as default, `/Users`.
    * `Groups Resource`: Leave as default, `/Groups`.
    * `SCIM Version`: Leave as default, `2.0`.
    * `Authentication Method`: Select `OAuth 2 Bearer Token`.
    * `Oauth Access Token`: Input the **New SCIM Token** from step 1.
    * `Auth Type Header`: Select `Bearer`.

    Once this is done, you can press the **Test Connection** button to check that SCIM is configured properly. You should see a success message saying "Connection Successful".
    If the connection is successful, press the "Next" button.

    In the final step, you'll be prompted to configure the mappings for the connection.

    Set the following fields:

    * `User Filter Expression`: `email.value Eq "%s"`.
    * `User Identifier`: `workEmail`.
    * `Deprovision on Rule Deletion:` Enabled.

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/scim/pingone/pingone-connection-preferences.png" alt="SCIM PingOne Connection Mappings" />

    Once this is configured, press the "Save" button.

    **3. Enable the connection**

    Finally, remember to enable the connection by pressing the enable toggle.

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/scim/pingone/pingone-connection-enable.png" alt="SCIM PingOne Connection Enable" />
  </Step>

  <Step title="Configure SCIM Provisioning in PingOne">
    **1. Create a new rule**

    After creating a connection, you can now access the "Rules" tab under the Provisioning section. Here you can configure the rules for the connection.

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/scim/pingone/pingone-new-rule-1.png" alt="SCIM PingOne Create New Rule 1" />

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/scim/pingone/pingone-new-rule-2.png" alt="SCIM PingOne Create New Rule 2" />

    Select the "New Rule" button and choose a name for the rule, then press the "Create Rule" button.

    **2. Configure the rule connection**

    Once you have created a rule, you now need to configure the connection to use for the rule.

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/scim/pingone/pingone-rule-select-connection.png" alt="SCIM PingOne Create New Rule 3" />

    Select the connection you created in the previous step and press the "Save" button.

    **3. Configure the rule user filter**

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/scim/pingone/pingone-rule-select-user-filter.png" alt="SCIM PingOne Create New Rule 4" />

    Select the Edit pencil icon to open the user filter configuration. This step dictates which users will be provisioned to Infisical.

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/scim/pingone/pingone-rule-user-filter.png" alt="SCIM PingOne Create New Rule 5" />

    In this case, we are provisioning all users that are enabled in PingOne. Configure your user filter to match your desired users, and then press the "Save" button.

    **4. Configure Groups**

    This step is optional and only relevant if you want to provision PingOne groups to Infisical.

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/scim/pingone/pingone-rule-group-provisioning-tab.png" alt="SCIM PingOne Create New Rule 6" />

    Open the "Group Provisioning" tab and press the "Add Groups" button to select which groups will be provisioned to Infisical.

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/scim/pingone/pingone-select-group.png" alt="SCIM PingOne Create New Rule 7" />

    Select the groups you want to provision to Infisical and press the "Save" button.

    **5. Enable the rule**

    Once you have configured the rule, you can enable it by pressing the "Enable" toggle.

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/scim/pingone/pingone-rule-enable.png" alt="SCIM PingOne Create New Rule 8" />
  </Step>
</Steps>

**FAQ**

<AccordionGroup>
  <Accordion title="Why do SCIM-provisioned users have to finish setting up their account?">
    Infisical's SCIM implementation accounts for retaining the end-to-end encrypted architecture of Infisical because we decouple the **authentication** and **decryption** steps in the platform.

    For this reason, SCIM-provisioned users are initialized but must finish setting up their account when logging in the first time by creating a master encryption/decryption key. With this implementation, IdPs and SCIM providers cannot and will not have access to the decryption key needed to decrypt your secrets.
  </Accordion>
</AccordionGroup>
