# Source: https://docs.acceldata.io/documentation/single-sign-on.md

# Single Sign-On

Single Sign-On (SSO) lets you log into ADOC using your organization’s existing authentication system, instead of managing a separate username and password which is vulnerable to security risks such as weak passwords, reuse, or phishing attacks. Once set up, you sign in once and get access to ADOC resources you’re entitled to, no extra authentication required.

SSO is managed through authentication providers (like Okta, Azure AD) and user federations (systems that sync user identities across platforms).

## Accessing SSO Settings

1. Click the **Settings** icon in the left menu.
2. Under **Users and Access**, click **SSO**.

You’ll see two main areas:

- **SSO Authentications** – Connect ADOC to your identity provider for login.
- **User Federations** – Sync and manage user accounts from external directories.

## SSO Authentication Options

### Prerequisites for SSO Authentication

 Before configuring **SAML** or **OpenID Connect (OIDC)** in ADOC, ensure that your organization already has a supported **Identity Provider (IdP)** (such as **Okta, Azure AD, Ping Identity, or other SAML/OIDC-compliant systems**) set up and managing user authentication.

- For **SAML**, your IdP must be able to provide a valid metadata XML file and endpoints for Single Sign-On and Authentication.
- For **OIDC**, your IdP must support OAuth 2.0 flows and provide client credentials (Client ID and Client Secret), token claims, and metadata endpoints.
- You should also confirm that you have **administrative access** within your IdP to create or configure new application integrations for ADOC.

Without these prerequisites in place, you will not be able to complete the SSO setup in ADOC.

You can set up SSO in ADOC using two industry-standard methods:

### 1. SAML (Security Assertion Markup Language)

- Lets users log in to multiple applications with one set of credentials.
- Widely supported and secure.

**Example:** You log into your company’s Okta portal → you’re automatically signed in to ADOC.

Setup basics:

1. Click **SAML** in ADOC’s **SSO** settings.
2. Upload the **SAML XML** file provided by your Identity Provider (IdP).
3. Enter:
4. **Single Sign-On URL** – Where ADOC sends login requests.
5. **Auth URL** – Where your IdP prompts users for credentials.
6. Save the configuration.

### 2. OpenID Connect (OIDC)

Built on top of OAuth 2.0, adds identity verification on top of secure token-based access.

**Example:** You log into your Microsoft or Google account → ADOC recognizes you and signs you in.

Setup basics:

- Before configuring ADOC, create and register an app in your IdP (Azure AD, Okta, etc.).
- Gather: Client ID, Client Secret, Metadata URL, and Token Claims (email, first name, last name).

In ADOC:

1. Enter these values in the OIDC setup form.
2. If using Metadata URL, ADOC auto-fills most details; otherwise, enter endpoints manually.
3. Save your changes.

## User Federations (Syncing Users)

User federations connect ADOC to external directories, so you don’t have to manually add or update users.

### LDAP (Lightweight Directory Access Protocol)

Used to pull in users from your company’s existing directory service.

**Example:** If a new employee is added in your corporate directory, they’ll automatically appear in ADOC after sync.

Setup basics:

1. Click **LDAP** in ADOC’s SSO settings.
2. Enter LDAP server details: URL, Distinguished Names (DNs), Bind credentials, and attribute mappings (username, unique ID, etc.).
3. Test the connection and save.

### Provisioning (SCIM)

Provisioning automates user and group creation in ADOC from your identity provider (IdP).

**Example:** HR adds a new employee to Okta → they instantly get an ADOC account with the right roles.

Setup basics:

1. Go to the **Provisioning** tab in SSO settings.
2. Enable **SCIM** (System for Cross-domain Identity Management).
3. Copy the **SCIM URL** and token into your IdP’s provisioning configuration.
4. Test and save.

Note Groups managed by SCIM can’t have their roles edited directly in ADOC. To change roles, update them in the IdP.

#### Assigning Roles to SCIM-Managed Groups

1. Click the group name in ADOC.
2. Select the roles you want assigned.
3. Save the changes.