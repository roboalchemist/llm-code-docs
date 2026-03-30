# Source: https://docs.axonius.com/docs/mapping-roles-in-axonius-to-okta-groups-in-saml.md

# Mapping Roles in Axonius to Okta Groups in SAML

This procedure describes how to map roles in Axonius using groups in Okta with SAML. Note that you need access to both Axonius and Okta to complete this process.

## In Axonius

### 1. Create an *Admin* role

1. Ensure you have the *Admin* role.
2. From the top right corner of any page, click ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/System%20Settings%20icon.png) to navigate to **System Settings**.
3. Go to **User and Role Management > Roles**.
4. Click **Add Role**.
5. Enter a descriptive name for your new role (for example: `Auditor`). Note this name for a later step.
6. Update the permissions as required and click **Save Changes**.

### 2. Configure User Assignment Rules

1. Navigate to **Access Management > LDAP & SAML**.
2. In **SAML-Based Login Settings**, scroll down to the **User Assignment Rules** section.
3. Set **Apply on** to **New Users Only** or **New and Existing Users** depending on whether you want roles updated for existing users or only applied on new account creation. You can also apply a data scope to the role here.
4. Click **+** to add a new rule.
5. In the first text field, enter `axoniusRole`.
6. In the second text field, enter the name of the role you will be passing from Okta (for example,`okta_axonius_auditor`). Note this name for a later step.
7. In the third field, select the corresponding Axonius role from the dropdown (this can be a default role or the custom role you created earlier, for example, `Auditor`).

   <Image align="center" width="550px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/settings/AddAxRolestoOkta.png" />

## In Okta

### 1. General Configuration

1. Ensure you have Super Admin or Application Admin privileges in Okta.
2. Navigate to your Axonius Application and click on the **Sign On** tab.

   ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/settings/AddAxRolestoOktaSignOnTab.png)
3. In the SAML Settings section, click **Edit**.
4. *(Optional)* Under Attribute Statements, scroll down and click **Edit**.

   ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/settings/AddAxRolestoOktaProfileAttr.png)
5. Add a new attribute statement:
   * **Name:** `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/axoniusRole`
   * **Name format:** Unspecified
   * **Value:** `appuser.axoniusRole` (This assumes you will map the role from a custom user attribute or a group in a later step.)
6. Click **Save**.

If you want additional information synced to the System User table, add the following attribute statements and click **Save**.

* **Given Name**
  * **Schema Name:** `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/givenname`
  * **Attribute:** firstName
  * **Name Format:** Unspecified
  * **Value:** `user.firstName`

* **Surname**
  * **Schema Name:** `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/surname`
  * **Attribute:** lastName
  * **Name Format:** Unspecified
  * **Value:** `user.lastName`

* **Title**
  * **Schema Name:** `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/title`
  * **Attribute:** title
  * **Name Format:** Unspecified
  * **Value:** `user.title`

* **Department**
  * **Schema Name:** `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/department`
  * **Attribute:** department
  * **Name Format:** Unspecified
  * **Value:** `user.department`

* **Email Address**
  * **Schema Name:** `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress`
  * **Attribute:** emailaddress
  * **Name Format:** Unspecified
  * **Value:** `user.email`

### 2. Configure the Custom Attribute in Profile Editor

1. Navigate to **Directory > Profile Editor**.

   <Image align="center" width="300px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/settings/AddAxRolestoOktaAdminCon.png" />
2. Search for your Axonius Application and open its profile.
3. Click **Add Attribute**.
4. Configure:
   * **Data Type:** string
   * **Display Name:** A name for the attribute as it appears in Okta (for example,`Axonius Role`)
   * **Variable Name:** `axoniusRole`
5. Check the box for **Define enumerated list of values** (if you want a controlled list of roles).
6. *(Optional)*  Enter the Display Name and Value for your roles. The Value must match the name you entered in the Axonius User Assignment Rules (for example, `okta_axonius_auditor`).
7. **Attribute type:** Select **Group** (This is the most common way to map Axonius roles from Okta groups).
8. Click **Save**.

   <Image align="center" width="450px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/settings/AddAxRolestoOktaAxonRole.png" />

### 3. Create and Assign the Entitlement Group

1. Create a new Group in Okta (e.g., `Axonius_Role_Auditor`).
2. Assign this group to the Axonius Application.
3. Map the role to the group: In the Axonius app assignment settings for the group, set the appropriate role attribute to the value you noted earlier (e.g., `okta_axonius_auditor`).

   <Image align="center" width="450px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/settings/AddAxRolestoOktaAssignAxon.png" />

<Callout icon="📘" theme="info">
  Note

  If a user is in multiple groups, Okta will pass the role from the group with the highest priority level, as configured in your Okta Group Priority settings.
</Callout>

4. Add the users who should have this role to the group.

### Validation

Instruct users to sign in to Axonius via Okta and validate that they are receiving the correct role in Axonius.