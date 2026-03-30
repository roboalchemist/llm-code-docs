# Source: https://help.cloudsmith.io/docs/okta.md

# SCIM with Okta

Setting Up SCIM with Okta

SCIM, or System for Cross-domain Identity Management, is an open standard designed to manage user identity information. Cloudsmith is SCIM 2.0-compliant. With Cloudsmith's support for SCIM, you can automatically provision new users, de-provision existing users, and update existing users' profile information based on changes within your Identity Provider (IdP).

To begin using SCIM, you need to enable the SCIM functionality in the [Cloudsmith Workspace Settings](https://help.cloudsmith.io/docs/organisations#scim)

Follow these steps:

1. Navigate to the Cloudsmith Workspace settings
2. Navigate to Authentication >> SCIM settings and enable the SCIM functionality by selecting "Allow SCIM."

<Image align="center" src="https://files.readme.io/039ea4c884315e862a79be98f12717b08e6d8092fc23f79beb23dfc7c4cc2550-scim-steps.png" />

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
        Please see your [Organization Account Settings](https://help.cloudsmith.io/docs/organisations#scim) on Cloudsmith for your SCIM password.
      </td>
    </tr>
  </tbody>
</Table>

Then test and save the configuration.

Once saved, you can then enable the "Create Users", "Update User Attributes" and "Deactivate Users" functionality via the "Provisioning" > "To App" tab:

<Image align="center" src="https://files.readme.io/93fc9ed-To_app.png" />

Okta is now configured to provision, update and de-provision users from your Cloudsmith organization.