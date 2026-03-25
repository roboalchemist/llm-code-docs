# Source: https://documentation.onesignal.com/docs/en/sso.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Single Sign-On (SSO)

> Configure SSO authentication for your OneSignal dashboard and team.

<Warning>
  Please reach out to your account manager or `support@onesignal.com` for assistance with setting this up.

  We also recommend having a product owner of SSO from your team to bring to our Support/Sales calls.
</Warning>

## What is Single Sign-On (SSO)?

* With SSO, a user only has to enter their login credentials (username, password, etc.) one time on a single page to access all of their SaaS applications.
* Whenever a user signs in to an SSO service, the service creates an authentication token that remembers that the user is verified. An authentication token is a piece of digital information stored either in the user's browser or within the SSO service's servers, like a temporary ID card issued to the user. Any app the user accesses will check with the SSO service. The SSO service passes the user's authentication token to the app and the user is allowed in. If, however, the user has not yet signed in, they will be prompted to do so through the SSO service.

## Available SSO identity providers (IdP)

|                                                                                                        |                                                                                                                                                            |                                                                                                                                                |
| ------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| [ADP](https://marketplace.adp.com/downloads/setting-up-sso.pdf)                                        | [Duo](https://duo.com/docs/sso)                                                                                                                            | [OneLogin](https://www.onelogin.com/blog/saml-configuration)                                                                                   |
| [Auth0](https://auth0.com/docs/get-started/applications/enable-sso-for-applications)                   | [Google Workspace](https://support.google.com/a/answer/12032922?hl=en)                                                                                     | [Oracle](https://docs.oracle.com/en/cloud/paas/content-cloud/administer/enable-single-sign-sso.html#GUID-8C87B98B-362E-4AD4-8AB9-BD7057935AFE) |
| [Azure AD](https://learn.microsoft.com/en-us/azure/active-directory/hybrid/connect/how-to-connect-sso) | [JumpCloud](https://support.jumpcloud.com/support/s/article/getting-started-applications-saml-sso2)                                                        | PingFederate                                                                                                                                   |
| CAS                                                                                                    | KeyCloak                                                                                                                                                   | PingOne                                                                                                                                        |
| ClassLink                                                                                              | [LastPass](https://support.lastpass.com/s/document-item?language=en_US\&bundleId=lastpass\&topicId=LastPass/c_lastpass_admins_toolkit_sso.html&_LANG=enus) | [Rippling](https://developer.rippling.com/docs/rippling-api/dii48ovix1887-saml-sso-guide)                                                      |
| [CloudFlare](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/)               | [Microsoft ADFS](https://learn.microsoft.com/en-us/microsoft-365/troubleshoot/active-directory/set-up-adfs-for-single-sign-on)                             | [Salesforce](https://help.salesforce.com/s/articleView?id=sf.sso_about.htm\&type=5)                                                            |
| Custom OpenID Connect                                                                                  | miniOrange                                                                                                                                                 | Shibboleth                                                                                                                                     |
| Custom SAML                                                                                            | NetIQ                                                                                                                                                      | Shibboleth Unsolicited                                                                                                                         |
| [Cyber Ark](https://docs.cyberark.com/Idaptive/Latest/en/Content/Applications/AppsOvw/ConfigSSO.htm)   | [Okta](https://developer.okta.com/docs/guides/build-sso-integration/openidconnect/main/)                                                                   | SimpleSAML php                                                                                                                                 |
|                                                                                                        |                                                                                                                                                            | [VMWare](https://docs.vmware.com/en/VMware-vSphere/6.7/com.vmware.psc.doc/GUID-75D4E587-3F9B-4B50-96DA-D6DB6D1781D7.html)                      |

If you are using an IdP that isn't listed here, please reach out to `support@onesignal.com` to request it.

***

# Setup

### Step 1. Obtain setup link

`support@onesignal.com` will provide the setup link and will guide you through the process.

### Step 2. Identity Provider

Please let `support@onesignal.com` know what identity provider you are using.

### Step 3. Follow IdP-specific guide

Each identity provider has a slightly different process. Use the table above to find a guide.

### Step 4. Test your connection

Now you have connected your IdP, you'll proceed to sign-on with your SSO IdP.

### Step 5. Onboard Existing Users into OneSignal using SSO

If you are an existing user, you should now be able to click onto `Continue with Single Sign-On`You will additionally also be able to continue signing on with your username and password, until you want to enforce SSO logins across the organization.

We provide this a dual login function of SSO login and username and password whilst you are testing SSO, as it ensures message sending is not disrupted whilst onboarding with SSO.

Please provide `support@onesignal.com` the emails you want to test out SSO with so we can enable them for testing.

<Frame caption="OneSignal sign-in interface with SSO option">
  <img src="https://mintcdn.com/onesignal/KSCNwSpBCNSQ8xdF/images/docs/f7d3f9c-signin.png?fit=max&auto=format&n=KSCNwSpBCNSQ8xdF&q=85&s=4ff34c990fa5380e8f263c1414d19ff2" width="856" height="984" data-path="images/docs/f7d3f9c-signin.png" />
</Frame>

### Step 6. Enforcing SSO

Once you are ready to move out of testing, or if you want to switch the to SSO immediately, contact us at `support@onesignal.com` to begin enforcing SSO on this organization.

***

# Adding Users into SSO Org

## Using our Org Admin Invite Flow

An Org Admin can invite users as specified in our guide for managing team members [here](./manage-team-members)

## What Happens if you invite someone not within your SSO org domain?

The email domain has to be added under the SSO org, to invite a user into that org. An error occurs if a user invites someone who is not under that org.

<Frame caption="Email invitation interface for adding users">
  <img src="https://mintcdn.com/onesignal/Z6xkXGfmy814If53/images/docs/d80d5d6-adding_person_to_app.png?fit=max&auto=format&n=Z6xkXGfmy814If53&q=85&s=437d5dbc5f292562f76aa9158b195785" width="660" height="498" data-path="images/docs/d80d5d6-adding_person_to_app.png" />
</Frame>

## Signing in with SSO

All new SSO users will be invited into the application from the team members page below. Click on the button `Invite to Organization`. You'll be able to set the role of the user as you invite them into the App, or Org.

<Frame caption="Team Members page with Invite to Organization button">
  <img src="https://mintcdn.com/onesignal/Z6xkXGfmy814If53/images/docs/d930dcf883e3134f1a688d4b94bb9976d447e70c55da9f4efdea7182ee37bada-Screenshot_2024-12-04_at_3.25.08_PM.png?fit=max&auto=format&n=Z6xkXGfmy814If53&q=85&s=ee79b4a6896baa1487096cfcf6b753b1" width="2822" height="1026" data-path="images/docs/d930dcf883e3134f1a688d4b94bb9976d447e70c55da9f4efdea7182ee37bada-Screenshot_2024-12-04_at_3.25.08_PM.png" />
</Frame>

<Frame caption="Email input form for adding team members">
  <img src="https://mintcdn.com/onesignal/MUgio66t0sYhGEvj/images/docs/6f6bc0b-adding_person_to_app.png?fit=max&auto=format&n=MUgio66t0sYhGEvj&q=85&s=a081dd660c2ec2794a95f28e1f3ebff3" width="660" height="350" data-path="images/docs/6f6bc0b-adding_person_to_app.png" />
</Frame>

Your invited user will receive an email to accept the invitation.

<Frame caption="OneSignal invitation email example">
  <img src="https://mintcdn.com/onesignal/KSCNwSpBCNSQ8xdF/images/docs/f7c4d0c-invite-email.png?fit=max&auto=format&n=KSCNwSpBCNSQ8xdF&q=85&s=d9dd9c8bd0e6a2e8393cfcf5013ca3bb" width="900" height="674" data-path="images/docs/f7c4d0c-invite-email.png" />
</Frame>

Once they receive an invitation, they can log in by clicking "Accept invitation".

<Frame caption="SSO login page after invitation acceptance">
  <img src="https://mintcdn.com/onesignal/YOTSrtBSoqdrJ37A/images/docs/47c7434-login_to_sso.png?fit=max&auto=format&n=YOTSrtBSoqdrJ37A&q=85&s=8e6392b319a32ac40bbb6b18f01a6a99" width="700" height="544" data-path="images/docs/47c7434-login_to_sso.png" />
</Frame>

***

# FAQ

### Who Can Use SSO?

SSO is for enterprise customers only. Here is our [pricing page](https://onesignal.com/pricing) for more details. Contact `support@onesignal.com` to get set up with SSO.

### Is there any restriction to the number of seats an SSO I can have?

We will not be restricting the number of seats under an SSO org.

### How can I test SSO for myself?

We'll walk you through and help you get set up with SSO. You'll be provided with a magic link, to enter your SSO credentials for your organization. Once set up, only your username will be assigned to login with SSO. You can then continue onboarding all of your org users into OneSignal using SSO. Once all of your users are using SSO, let us know at `support@onesignal.com` and we'll ensure SSO is enforced for all users going forward.

We allow you to onboard your users slowly, as needed, to ensure your messaging is not disrupted.

### Why do we use domains? How many domains can an org have?

Website domains are also used for email addresses, aka. onesignal.com maps to `x@onesignal.com` . This means as you set up an org for SSO you add website domains that represent those underlying emails.

<Note>An organization can have multiple domains as part of SSO login.</Note>

### How do I de-provision and provision users?

A user can be de-provisioned and provisioned from within the OneSignal dashboard. At this time we do not support de-provisioning and provisioning users from within the IdP.

### I want to use SSO, but I don't know who is my Admin for my Organization. What do I do?

Please contact `support@onesignal.com` for us to provide you information to contact your admin with.

### What email domains are used within my Organization for OneSignal?

Please get your Organizational Admin to contact `support@onesignal.com` for us to provide you with a list of email domains your organization uses.

### What happens if my IdP goes down?

If the IdP goes down, OneSignal users will not be able to log in. However, if they have an existing session, they won't need to log in.

### I want to use SSO but I don't have an IdP now

Unfortunately, SSO is not a suitable solution for you if you do not have an IdP. It's best to work within your internal team or with a consultancy to help you set this up.

### Is a mixed mode (SSO and regular username/password login) supported simultaneously? Can users either log in via SSO or the local username/password?

We don't have a mixed mode but it is something we can consider. Usually SSO is the primary login. One way to do a mixed mode is to separate your SSO apps into one org, then other non-SSO apps into another org. However, an org is used for billing purposes

### Could we connect more than one IdP tenant to an organization?

You're allowed one IdP tenant per organization. Please reach out to `support@onesignal.com` for any further questions or feedback.

***

Built with [Mintlify](https://mintlify.com).
