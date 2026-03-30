# Source: https://docs.axonius.com/docs/example-saml-based-authentication-with-okta.md

# Example: SAML Based Authentication with Okta

The following example describes how to enable SAML-based authentication in Axonius with Okta.

See [Okta Documentation](https://help.okta.com/en-us/Content/Topics/Apps/Apps_App_Integration_Wizard_SAML.htm) for more about creating SAML app integrations.

<Callout icon="📘" theme="info">
  Note

  Okta updates their UI from time to time. The location of fields on the Okta pages may be different than described here.
</Callout>

**Do the following in Okta:**

1. Log in to your Okta admin panel.
2. In the left pane, click **Applications** and under that, click **Applications**. Click **Browse App Catalog** and use the **Search** box to find **"Axonius"** and select it.

<Image alt="SAMLOktaExample-BrowseAppCatalog.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SAMLOktaExample-BrowseAppCatalog.png" />

3. Click **Add Integration**.
4. Set the **Domain** to match the IP or domain name of your Axonius instance, and then click **Done**. You can change the **Application label** to a custom value.

<Image alt="Screen Shot 2020-03-04 at 3.42.18 PM" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Screen%20Shot%202020-03-04%20at%203.42.18%20PM.png" />

4. Under **Sign On**, click **Edit** in the upper right-hand corner. Set the **Default Relay State** value to **https\://\[\[domain]]/api/login/saml?idp=XX**, replacing **\[\[domain]]** with the value used in Step 3 and *XX* with the unique IDP name for the SAML configuration using this Okta application (see **Do the following in Axonius** below). Then click the green **Save** button in the bottom right-hand corner.

<Image alt="Screen Shot 2020-03-19 at 3.17.47 PM" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Screen%20Shot%202020-03-19%20at%203.17.47%20PM.png" />

5. Once the application is created, on the **Sign on** tab, under **Metadata Details**:
   1. Append **saml?idp=XX** to the end of the metadata URL: **https\://\[\[domain]]/api/login/saml?idp=XX**
   2. Copy the URL in the field **Metadata URL**.

<Image alt="image.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image(749).png" />

6. Under More Details:
   1. In **Sign On URL** and **Sign Out URL**,
7. On the **Assignments** tab, click Assign and configure the users (people) / groups you want to assign to this app.

**Do the following in Axonius:**

1. Log into Axonius as an admin. Go to **Settings** `>` **Access Management** `>` **LDAP & SAML**`>`**SAML-Based Login Settings**. Then fill in the following details:
   * **Name of the Identity Provider** - A custom string of your choosing that identifies this connection.
   * **Unique name of IDP** - Enter a unique name for this specific SAML integration. This value is for when there are multiple SAML integrations from the same identity provider (in this case Okta) and must be entered now before saving the configuration. Once saved, this value **cannot** be changed. If not provided and you want to add a SAML integration later, you will need to delete this configuration and recreate it with an IDP value.
   * **Metadata URL** - The URL you have copied in step #5 above under **In Okta**. If you do not want to use the metadata URL, fill in the following fields (the correct values can be found in Okta):
     * **Single sign-on service URL**
     * **Entity ID**
     * **Single logout service URL**
     * **IdP Signing certificate** - Download the certificate from Okta and upload it to Axonius by clicking **Upload File**.
   * **Axonius External URL** - The URL that is used to access Axonius. If the instance is not behind a proxy, this can be left empty.

2. Under **User Assignment Settings**:
   * In **Default role for new SAML user only** user, select a default role. This role is assigned when there is no matching assignment rule.
   * In **Default Data Scope for new SAML user only**, select the Data Scope to assign to new users. This Data Scope is assigned when there is no matching assignment rule.
   * In **Evaluate user assignment on**, select to which users the role assignment setting will apply.
     * **New users** - The selected role is assigned to new users logging in with SAML for the first time.
     * **New and existing users** - The selected role is assigned to all users when they log in with SAML.

3. Click **Save** to save the SAML configuration. You can now Log in to Axonius with Okta.