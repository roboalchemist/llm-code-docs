# Source: https://infisical.com/docs/integrations/app-connections/okta.md

# Source: https://infisical.com/docs/documentation/platform/sso/okta.md

# Source: https://infisical.com/docs/documentation/platform/scim/okta.md

> ## Documentation Index
> Fetch the complete documentation index at: https://infisical.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Okta SCIM

> Learn how to configure SCIM provisioning with Okta for Infisical.

<Info>
  Okta SCIM provisioning is a paid feature.

  If you're using Infisical Cloud, then it is available under the **Enterprise Tier**. If you're self-hosting Infisical,
  then you should contact [sales@infisical.com](mailto:sales@infisical.com) to purchase an enterprise license to use it.
</Info>

Prerequisites:

* [Configure Okta SAML for Infisical](/documentation/platform/sso/okta)

<Steps>
  <Step title="Create a SCIM token in Infisical">
    In Infisical, head to the **Single Sign-On (SSO)** page and select the **Provisioning** tab. Under SCIM Configuration,
    press the **Enable SCIM provisioning** toggle to allow Okta to provision/deprovision users and user groups for your organization.

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/scim/scim-enable-provisioning.png" alt="SCIM enable provisioning" />

    Next, press **Manage SCIM Tokens** and then **Create** to generate a SCIM token for Okta.

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/scim/scim-create-token.png" alt="SCIM create token" />

    Next, copy the **SCIM URL** and **New SCIM Token** to use when configuring SCIM in Okta.

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/scim/scim-copy-token.png" alt="SCIM copy token" />
  </Step>

  <Step title="Configure SCIM in Okta">
    In Okta, head to your Application > General > App Settings. Next, select **Edit** and check the box
    labled **Enable SCIM provisioning**.

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/scim/okta/scim-okta-enable-provisioning.png" alt="SCIM Okta" />

    Next, head to Provisioning > Integration and set the following SCIM connection fields:

    * SCIM connector base URL: Input the **SCIM URL** from Step 1.
    * Unique identifier field for users: Input `email`.
    * Supported provisioning actions: Select **Push New Users**, **Push Profile Updates**, and **Push Groups**.
    * Authentication Mode: `HTTP Header`.

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/scim/okta/scim-okta-config.png" alt="SCIM Okta" />

    Under HTTP Header > Authorization: Bearer, input the **New SCIM Token** from Step 1.

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/scim/okta/scim-okta-auth.png" alt="SCIM Okta" />

    Next, press **Test Connector Configuration** to check that SCIM is configured properly.

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/scim/okta/scim-okta-test.png" alt="SCIM Okta" />

    Next, head to Provisioning > To App and check the boxes labeled **Enable** for **Create Users**, **Update User Attributes**, and **Deactivate Users**.

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/scim/okta/scim-okta-app-settings.png" alt="SCIM Okta" />

    Now Okta can provision/deprovision users and user groups to/from your organization in Infisical.
  </Step>
</Steps>

**FAQ**

<AccordionGroup>
  <Accordion title="Why do SCIM-provisioned users have to finish setting up their account?">
    Infisical's SCIM implmentation accounts for retaining the end-to-end encrypted architecture of Infisical because we decouple the **authentication** and **decryption** steps in the platform.

    For this reason, SCIM-provisioned users are initialized but must finish setting up their account when logging in the first time by creating a master encryption/decryption key. With this implementation, IdPs and SCIM providers cannot and will not have access to the decryption key needed to decrypt your secrets.
  </Accordion>
</AccordionGroup>
