# Source: https://docs.firehydrant.com/docs/sso-with-saml.md

# SSO with SAML

If you have an identity provider (IDP) that supports SAML 2.0, you can use it with FireHydrant as a single sign-on provider.

## Prerequisites

* You'll need to [reach out to our support team](https://support.firehydrant.com/hc/en-us/requests/new) to enable SSO for your organization
* You will need <Glossary>Owner</Glossary> permissions to configure SSO settings on FireHydrant
* You will need administrative access to your IDP to create a new SAML application and administer users

> 📘 Finding Your Organization ID:
>
> If you need multi-org support, your Organization ID is required when configuring SAML with your identity providers. This unique identifier ensures your SAML assertions are routed to the correct organization.
>
> **Important for Multi-Org Accounts:** Using organization-specific URLs prevents users from landing in the wrong FireHydrant organization. When multiple applications point to the same generic ACS URL, users assigned to multiple apps could be directed to an incorrect organization.
>
> **How to Find Your Organization ID:**
>
> 1. Log into FireHydrant at [https://app.firehydrant.io](https://app.firehydrant.io)
> 2. Navigate to **Settings** → **Single Sign On**
>    1. Your Organization ID is displayed at the SAML Configuration metadata section
>    2. Format: UUID (example: `a1b2c3d4-e5f6-7890-abcd-ef1234567890`)
>
> **Where to Use This ID:**
>
> When configuring your identity provider, you'll need to provide URLs that
> include your Organization ID:
>
> * **Assertion Consumer Service (ACS) URL**:
>   `https://api.firehydrant.io/sso/saml/org/{YOUR_ORG_ID}/consume`
>
> * **Entity ID / Audience**:
>   `https://api.firehydrant.io/sso/saml/org/{YOUR_ORG_ID}/entity`
>
> **Example:**
> If your Organization ID is `a1b2c3d4-e5f6-7890-abcd-ef1234567890`, your ACS URL would be:
> [https://api.firehydrant.io/sso/saml/org/a1b2c3d4-e5f6-7890-abcd-ef1234567890/consume](https://api.firehydrant.io/sso/saml/org/a1b2c3d4-e5f6-7890-abcd-ef1234567890/consume)

## Entra ID (Azure AD)

> 📘 Note:
>
> If you manage multiple FireHydrant organizations with SSO enabled, you'll need to use
> organization-specific URLs. See [Finding Your Organization ID](#finding-your-organization-id)
> and use these formats instead:
>
> * **Entity ID**: `https://app.firehydrant.io/sso/saml/org/{organization-id}/entity`
> * **Reply URL**: `https://app.firehydrant.io/sso/saml/org/{organization-id}/consume`

Setting up single-sign on with Entra ID enables employees in your Entra tenant to authenticate to and access FireHydrant accounts.

1. From the [Entra Portal](https://entra.microsoft.com), click into **Applications** > **Enterprise Applications**
2. Click **New Application** > **Create your own application**
3. Name your app "FireHydrant" and select "Integrate any other application you don't find in the gallery (Non-gallery). Click **Create**.
4. Click into **Single Sign-on** once your app has been created and select **SAML**
5. Click Edit for "Basic SAML Configuration" and configure it as follows, then Save (**please note** all fields are case-sensitive).
   1. **Identifier (Entity ID)**: firehydrant
      1. Add this as a second identifier without switching it to the default: [https://app.firehydrant.io/sso/saml/consume](https://app.firehydrant.io/sso/saml/consume)
   2. **Reply URL (Assertion Consumer Service URL)**: [https://app.firehydrant.io/sso/saml/consume](https://app.firehydrant.io/sso/saml/consume)
   3. **Sign on URL**: Leave empty (do not enter a value)

      ⚠️ **Important:** Adding a Sign on URL can prevent IdP-initiated SSO (My Apps tile)
      from working properly. Leave this field blank for best compatibility.
6. Click Edit for "Attributes & Claims" and configure it as follows, then Save:

   1. **Unique User Identifier (Name ID)**
      1. **Name identifier format**: Email address
      2. **Source**: Set to attribute that stores the user's email address. This should match how you expect the user to appear in FireHydrant.
   2. **Additional Claims**

      | Claim Name   | Namespace                                                                                                      | Recommended Mapping                        |
      | :----------- | :------------------------------------------------------------------------------------------------------------- | :----------------------------------------- |
      | emailAddress | [http://schemas.xmlsoap.org/ws/2005/05/identity/claims](http://schemas.xmlsoap.org/ws/2005/05/identity/claims) | Attribute that stores user's email address |
      | firstName    | [http://schemas.xmlsoap.org/ws/2005/05/identity/claims](http://schemas.xmlsoap.org/ws/2005/05/identity/claims) | user.givenname                             |
      | lastName     | [http://schemas.xmlsoap.org/ws/2005/05/identity/claims](http://schemas.xmlsoap.org/ws/2005/05/identity/claims) | user.surname                               |
7. Under "SAML Certificates," download the **Certificate (Base64)**. In order to open the certificate in a readable format that you can enter into FireHydrant, you will need to run to run the following:
   `openssl x509 -in certificatename.cer -outform PEM -out certificatename.pem`
   Open the resulting file in a text editor.
8. In a separate browser tab, open [FireHydrant's SSO settings page](https://app.firehydrant.io/organizations/sso/settings/edit) and check **Enable SSO**. Enter the following information from Entra ID:

   | Entra ID Value             | FireHydrant Field    |
   | :------------------------- | :------------------- |
   | Login URL                  | IdP Login URL        |
   | Microsoft Entra Identifier | IdP Issuer           |
   | Use the output from step 6 | IdP X509 Certificate |

   1. (Optional) Add a domain for SP-initiated logins. When users attempt to log in to FireHydrant directly with an email address that matches this domain, FireHydrant will display a note and redirect them to your IDP sign-in.
9. Click **Save**. You will now be able to test the login process from within Entra by assigning it to yourself and using the **Test This Application** button.

## Google SSO

Setting up single sign-on with Google enables your G Suite account users to authenticate and access FireHydrant accounts.

1. Follow Google's instructions on [setting up a custom SAML application](https://support.google.com/a/answer/6087519?hl=en) until you get to the **Google Identity Provider details page**.
2. In a separate browser tab, open [FireHydrant's SSO settings page](https://app.firehydrant.io/organizations/sso/settings/edit) and check **Enable SSO**. Three additional fields will appear: IDP Login URL, IDP Issuer, and IDP X509 Certificate. Copy the values from Google into FireHydrant as follows:

| Google Value | FireHydrant Field    |
| :----------- | :------------------- |
| SSO URL      | IDP Login URL        |
| Entity ID    | IDP Issuer           |
| Certificate  | IDP X509 Certificate |

3. (Optional) In the **Domains** section of FireHydrant, you can add the email domain name for your organization.
   1. When users attempt to log in to FireHydrant directly with an email address that matches this domain, FireHydrant will display a note and redirect them to your IDP sign-in.
4. Click **Save** in FireHydrant.
5. In Google, click **Next**. Google prompts you to fill in Service Provider details. For the **ACS URL** and **Entitiy ID** fields, enter `https://app.firehydrant.io/sso/saml/consume`.
6. Enable the **Signed Response** checkbox.
7. Verify that **Primary Email** is selected for the Name ID section. This is how your SSO configuration automatically creates accounts or logs existing users into FireHydrant.
8. For the **Name ID Format** field, select **Email**. Click **Next**.
9. (Optional) On the last step of the Google setup, provide any attribute mappings you'd like to include when users are sent to FireHydrant. These are optional, but we recommend setting the first and last name attributes so when users are provisioned, their names are automatically set correctly in FireHydrant.

   <Image align="center" alt="Attribute mapping in Google" border={false} caption="Attribute mapping in Google" src="https://files.readme.io/6b5f39f-image.png" width="400px" />
10. Click **Finish**. This completes your Google SSO setup.

## Okta SSO

> 📘 User Provisioning and Lifecycle:
>
> **User Deactivation:**
>
> **Without SCIM:** When a user is removed from Okta, they are **NOT automatically removed** from FireHydrant. Organization owners must manually deactivate users in FireHydrant Settings → Members.
>
> **With SCIM Provisioning:** When SCIM is enabled and a user is removed from Okta, they are **automatically deactivated** in FireHydrant. See the [SCIM Configuration Guide](/docs/scim-configuration) for automated user lifecycle management.
>
> Our Okta SAML integration provides one-way user provisioning - FireHydrant accounts will be automatically provisioned via JIT (Just-In-Time) provisioning, but not automatically de-provisioned without SCIM. Users whose accounts are auto-provisioned with Okta are set to the <Glossary>Member</Glossary> role by default.

### Configuration Steps

1. As an Okta admin, view all applications in the **Applications** tab. Then:
2. Click **Browse App Catalog**
3. Search for the **FireHydrant** app (**FireHydrant Enterprise** for multi-org), click it, and then click **Add Integration**
4. (Multi-org Support Only) Configure Organization ID Application Property

   To enable proper SAML routing, you must configure the Organization ID as an Application Instance Property in Okta:

   1. In your Okta application settings, locate the **Application Instance Properties** section

   2. Find the **Organization ID** field

   3. Enter your FireHydrant Organization ID (Check [at the beginning of this guide](#finding-your-organization-id) to learn how to get it)
      The Organization ID is used to construct the organization-specific SAML endpoints:

   * **ACS URL**: `https://api.firehydrant.io/sso/saml/org/{organizationId}/consume`
   * **Entity ID**: `https://api.firehydrant.io/sso/saml/org/{organizationId}/entity`
5. Name your app and click **Next**. This will drop you onto the **Assignments** page.
6. Click into **Sign On** and go to **View SAML setup instructions**.
7. In a separate browser tab, open [FireHydrant's SSO settings page](https://app.firehydrant.io/organizations/sso/settings/edit) and check **Enable SSO**. Enter the IDP Login URL, IDP Issuer, and IDP X509 Certificate details from Step #4 into FireHydrant.
8. (Optional but Recommended) Configure Email Domain:
   Enter your organization's email domain, this:
   * Enables SSO for new users before they're provisioned via SCIM
   * Improves login experience by automatically detecting SSO
     :blue\_book: **Note:** SP-initiated SSO works without this for existing users.
9. Enable SSO and save your configuration. This completes the setup for Okta SAML 2.0.

#### Attribute Statements

When configuring your Okta application, FireHydrant requires the following SAML attribute statements:

* **firstName** (Required): Maps to `user.firstName` - Used to populate the user's first name in FireHydrant
* **lastName** (Required): Maps to `user.lastName` - Used to populate the user's last name in FireHydrant
* **email** (Required): Maps to `user.email` - Used as the primary user identifier

These attributes ensure that user profiles are properly populated when users authenticate via SAML SSO.

### Supported SSO Flows

FireHydrant supports both IdP-initiated and SP-initiated SAML authentication with full organization-aware routing:

* **IdP-Initiated (Recommended):** Users click the FireHydrant app tile in their Okta dashboard and are automatically logged in. This flow is fully supported with organization-specific SAML endpoints, ensuring proper routing to the correct FireHydrant organization.

* **SP-Initiated:** Users navigate to [https://app.firehydrant.io](https://app.firehydrant.io), enter their email, and are redirected to Okta for authentication.

Both flows work seamlessly with the organization-specific endpoints configured in your Identity Provider.

## Generic

1. For other identity providers aside from Google and Okta, you can set up the integration by entering FireHydrant's SAML details as below when creating a new SAML application:
   1. **Consumer URL**: `https://app.firehydrant.io/sso/saml/consume`
   2. **Recipient URL and Audience URL**: Same as the consumer URL
   3. **Audience**: `firehydrant`
   4. **Attribute statements**: **First Name** as `firstName`, **Last Name** as `lastName`
2. After you've created your SAML application, you will then need to configure settings within FireHydrant:
   1. In FireHydrant, navigate to **Settings> Single Sign On**.
   2. On the Single Sign On page, check the box labeled  **Enable SSO**.
   3. Additional fields appear. In these fields, provide your IDP login URL, IDP issuer, and IDP X509 certificate as generated by your identity provider.
   4. (Optional) If you'd like, you can add **Domains**. When users attempt to log in to FireHydrant directly with an email address that matches this domain, FireHydrant will display a note and redirect them to your IDP sign-in.

## Testing

To test, leave your session in FireHydrant open. Visit your IDP in a new window or tab and attempt to log in with your newly configured integration.

Leaving your FireHydrant session open should prevent you from getting locked out of your account during setup. If you encounter a lockout, submit a ticket on our [contact form](https://support.firehydrant.com/hc/en-us/requests/new) for help.

<br />

## Common Errors (and how to fix them)

This guide explains the various error messages that users may encounter when attempting to log in via SAML SSO to FireHydrant, along with troubleshooting steps for each scenario.

## Error Messages

### "No Organization has been setup for that SSO issuer: \[issuer\_name]"

**When this occurs:**

* The SAML response contains an issuer that doesn't match any configured SSO settings in FireHydrant
* This typically happens when the Identity Provider (IdP) is sending an incorrect issuer value (or the issuer is not configured in FireHydrant correctly)

**What to check:**

* Verify that your Identity Provider's issuer/entity ID matches exactly what's configured in FireHydrant
* Check with your FireHydrant administrator to confirm the SSO configuration is complete
* Ensure you're using the correct SSO login URL for your organization

**Next steps:**

* Contact your FireHydrant administrator to verify the SSO configuration
* If the issue persists, email [support@firehydrant.com](mailto:support@firehydrant.com) with your organization name and the issuer value shown in the error

***

### "Invalid SSO login - Invalid user for organization"

**When this occurs:**

* A user with your email address exists in FireHydrant but belongs to a different account/organization
* You're attempting to log in to an organization that you don't belong to

**What to check:**

* Confirm you're using the correct SSO login URL for your organization
* Verify with your administrator that your email should have access to this specific FireHydrant organization
* Check if you might have multiple FireHydrant accounts under the same email address

**Next steps:**

* Use the correct SSO login URL provided by your organization
* Contact your FireHydrant administrator to verify your account membership
* If you need to be added to the organization, have an admin invite you

***

### "Your membership in this organization has been deactivated. Please contact one of your organization's owners for access."

**When this occurs:**

* Your user account exists but has been deactivated/disabled in the organization
* An administrator has removed your access, either intentionally or accidentally

**What to check:**

* Confirm with your team if there were any recent changes to user access
* Verify if this was an intentional deactivation (e.g., role change, department transfer)

**Next steps:**

* Contact your organization's FireHydrant administrator or owner
* Request reactivation of your account if appropriate
* Your admin can reactivate your account from the Users settings page

***

### "Could not create account from SSO login: \[specific\_error\_message]"

**When this occurs:**

* FireHydrant attempted to create a new user account based on your SSO login but failed
* The specific error message will provide more details about what went wrong

**Common specific errors:**

* **User limit reached**: For free tier accounts, there's a maximum of 10 users
* **Invalid email format**: The email from your IdP doesn't meet validation requirements
* **Missing required attributes**: Your IdP isn't sending required user information

**What to check:**

* Review the specific error message for details
* For user limit errors, check if your organization needs to upgrade their plan
* Verify your IdP is configured to send all required SAML attributes (email, name)

**Next steps:**

* Share the complete error message with your FireHydrant administrator
* For user limit issues, consider upgrading your FireHydrant plan
* Contact [support@firehydrant.com](mailto:support@firehydrant.com) with the full error message if unclear

***

### "Invalid SSO login"

**When this occurs:**

* The SAML response from your Identity Provider is invalid or malformed
* The digital signature on the SAML response doesn't match the configured certificate
* The SAML response has expired or has timestamp issues

**What to check:**

* Ensure your Identity Provider's certificate in FireHydrant matches the current certificate
* Verify there are no time synchronization issues between your IdP and FireHydrant
* Check if your IdP recently updated their signing certificate

**What to check:**

* Try logging in again - sometimes this is a temporary issue
* Clear your browser cache and cookies
* Ensure you're not using a bookmarked/outdated SSO URL

**Next steps:**

* Have your administrator verify the SSO configuration, especially the certificate
* Check your Identity Provider's logs for any errors
* Contact [support@firehydrant.com](mailto:support@firehydrant.com) with timestamp of the failed attempt

***

## General Troubleshooting Tips

1. **Always use the SSO login URL** provided by your organization, not the general FireHydrant login page
2. **Clear browser cache and cookies** if experiencing persistent issues
3. **Use an incognito/private browser window** to rule out browser-related issues
4. **Check with colleagues** to see if others are experiencing the same issue
5. **Note the exact time** of any errors to help with troubleshooting

## Need Further Assistance?

If you continue to experience issues after following this guide:

1. Gather the following information:

   * Exact error message
   * Time and date of the error
   * Your email address
   * Organization name
   * Browser and version being used

2. Contact [support@firehydrant.com](mailto:support@firehydrant.com) with the above information

Our support team will help diagnose and resolve your SSO login issues as quickly as possible.