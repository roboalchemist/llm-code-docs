# Source: https://www.aptible.com/docs/how-to-guides/platform-guides/scim-entra-guide.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.aptible.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Provisioning with Entra Identity (SCIM)

> Aptible supports SCIM 2.0 provisioning through Entra Identity using the Aptible SCIM integration. This setup enables you to automate user provisioning and de-provisioning for your organization.

With SCIM enabled, users won't have the option to leave your organization on their own and won't be able to change their account email or password. Only organization owners have permission to remove team members. Entra Identity administrators can use SCIM to manage user account details if they're associated with a domain your organization verified.

> 📘 Note

> You must be an Aptible organization owner to enable SCIM for your organization.

### Step 1: Create a SCIM Integration in Aptible

1. **Log in to Aptible**: Sign in to your Aptible account with OrganizationOwner privileges.
2. **Navigate to Provisioning**: Go to the 'Settings' section in your Aptible dashboard and select Provisioning.

<img src="https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/scim-app-ui.png?fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=5260a9ef9a9db23bb071b37d227c3f4a" alt="" data-og-width="2798" width="2798" data-og-height="1610" height="1610" data-path="images/scim-app-ui.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/scim-app-ui.png?w=280&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=071934bf1f70707bafb512a0cd4ae747 280w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/scim-app-ui.png?w=560&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=824ed9af14a135f5150b6d3a69185cd3 560w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/scim-app-ui.png?w=840&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=54b811abcf11736862deaa76eeaaab5b 840w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/scim-app-ui.png?w=1100&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=fb58221cd08909817daaeaa58d5e7630 1100w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/scim-app-ui.png?w=1650&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=30b6e5063e17a311d283de916ad069c9 1650w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/scim-app-ui.png?w=2500&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=e9b2db705777beebe884e66910bcf195 2500w" />

3. **Define Default Role**: Update the Default Aptible Role. New users created by SCIM will be automatically assigned to this role.
4. **Generate SCIM Token**: Aptible will provide a SCIM token, which you will need for Entra Identity configuration. Save this token securely; it will only be displayed once.

> 📘 Note

> Please note that the SCIM token has a validity of one year.

5. **Save the Changes**: Save the configuration.

### Step 2: Enable SCIM in Entra Identity

Entra Identity supports SCIM 2.0, allowing you to enable user provisioning directly through the Entra Identity portal.

1. **Access the Entra Identity Portal**: Log in to your Entra Identity admin center.
2. **Go to Enterprise Applications**: Navigate to Enterprise applications > All applications.
3. **Add an Application**: Click on 'New application', then select 'Non-gallery application'. Enter a name for your custom application (i.e., "Aptible") and add it.
4. **Setup SCIM**: In your custom application settings, go to the 'Provisioning' tab.
5. **Configure SCIM**: Click on 'Get started' and select 'Automatic' for the Provisioning Mode.
6. **Enter SCIM Connection Details**:
   * **Tenant URL**: Enter `https://auth.aptible.com/scim_v2`.
   * **Secret Token**: Paste the SCIM token you previously saved.
     <img src="https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/entra-enable-scim.png?fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=68348bb267de390498d9e6f0efcd0ace" alt="" data-og-width="1498" width="1498" data-og-height="1476" height="1476" data-path="images/entra-enable-scim.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/entra-enable-scim.png?w=280&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=aff8218b9359c65cce7d1f4661a58838 280w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/entra-enable-scim.png?w=560&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=8336fb5b2b2e7f6b279a4bd01c89b4e2 560w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/entra-enable-scim.png?w=840&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=cb350d62f8fa81104c6e3d88d5689252 840w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/entra-enable-scim.png?w=1100&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=3847ef234fa35fa7b3360e9b60c4d76c 1100w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/entra-enable-scim.png?w=1650&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=e6150e30b619491e2355d4708416d1bd 1650w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/entra-enable-scim.png?w=2500&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=cb7ff6d4e360ac8669cb6d9635ad392a 2500w" />
7. **Test Connection**: Test the SCIM connection to verify that the SCIM endpoint is functional and that the token is correct.
8. **Save and Start Provisioning**: Save the settings and turn on provisioning to start syncing users.

### Step 3: Configure Attribute Mapping

Customize the attributes that Entra Identity will send to Aptible through SCIM:

1. **Adjust the Mapping**: In the 'Provisioning' tab of your application, select 'Provision Microsoft Entra ID Users' to modify the attribute mappings.

<img src="https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/entra-attribute-configuration.png?fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=e5b01a32c9f669dc889f66a3fa9055d2" alt="" data-og-width="1584" width="1584" data-og-height="1584" height="1584" data-path="images/entra-attribute-configuration.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/entra-attribute-configuration.png?w=280&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=331e11421cc0d4e84f0b0d28d983c44e 280w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/entra-attribute-configuration.png?w=560&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=be5cb7becb3df7a2d69bde703b6bf716 560w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/entra-attribute-configuration.png?w=840&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=36694250a2fa0ed25cb2ebf119dc638f 840w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/entra-attribute-configuration.png?w=1100&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=7195ef12590aff7f8d752c09d860bc0a 1100w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/entra-attribute-configuration.png?w=1650&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=7885becb172573bf7e1ba9dde5add864 1650w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/entra-attribute-configuration.png?w=2500&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=376e2c9b9d036ae2d0b0f302ba0d6526 2500w" />

2. **Edit Attribute Mapping**: Ensure to align with what Aptible expects, focusing on core attributes like **User Principal Name**, **Given Name**, and **Surname**.

3. **Include required attributes**: Make sure to map essential attributes such as:
   * **userPrincipalName** to **userName**
   * **givenName** to **firstName**
   * **surname** to **familyName**
   * **Switch(\[IsSoftDeleted], , "False", "True", "True", "False")** to **active**
   * **mailNickname** to **externalId**

<img src="https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/entra-attribute-mapping.png?fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=0e65f67017917bd1e2ab8541cb720202" alt="" data-og-width="2606" width="2606" data-og-height="1872" height="1872" data-path="images/entra-attribute-mapping.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/entra-attribute-mapping.png?w=280&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=9161b0d7bfeb52fdef8f7ca333e7383a 280w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/entra-attribute-mapping.png?w=560&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=e54c39b4c7c0a575733b97f2c3446d6f 560w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/entra-attribute-mapping.png?w=840&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=0258c25099d7a0fe706637473b322d8c 840w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/entra-attribute-mapping.png?w=1100&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=fe91f0f02fd5edddd27aa2072820850c 1100w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/entra-attribute-mapping.png?w=1650&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=cdb7a1850c5063e3a68d1a2db4628af8 1650w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/entra-attribute-mapping.png?w=2500&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=d1cc21c7cd7ca29cf5c8360e9451ea27 2500w" />

### Step 4: Test the SCIM Integration

1. **Test User Provisioning**: Create a test user in Entra Identity and verify that the user is provisioned in Aptible.
2. **Test User De-provisioning**: Deactivate or delete the test user in Entra Identity and confirm that the user is de-provisioned in Aptible.

By following these steps, you can successfully configure SCIM provisioning between Aptible and Entra Identity to automate your organization's user management.
