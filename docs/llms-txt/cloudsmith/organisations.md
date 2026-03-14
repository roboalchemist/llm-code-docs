# Source: https://help.cloudsmith.io/docs/organisations.md

# Workspaces

Creating a *Workspace*  in Cloudsmith allows you to configure access for teams, individuals and machines that map to your company's organizational structure. Building security and resilience in managing teams and workflows is essential in today's ecosystem. This is a quick start guide to the powerful permission system within Cloudsmith and how you can get started.

## Create a Workspace

To create a new Workspace:

1. Navigate to "Workspaces" in the global menu
2. Click "Workspaces"
3. Click "Create Workspace"

<img src="https://files.readme.io/cfdd1f15b797468042b95b6e4616402426e5f08720e503039b3b86a269487648-create-new-workspace.png" alt="Create a new Workspace" caption="Create a new Workspace" align="center" />

<img src="https://files.readme.io/adb1abd30fd7eb115d376c7ebde10f7ec7f21eb24c58564544e3c9342fd5889a-create-workspace-button.png" align="center" />

You are now presented with the "Create a new workspace" form. You are required to enter a name for your Workspace (don't worry, we will check your workspace name is unique for you before creating it).

<img src="https://files.readme.io/a80d50085cb632806e49b1d8266dfcbde01afb8bc1108381db48d6eb4bf4f4f3-create-a-new-workspace-form.png" align="center" />

To configure the settings for the Workspace, just click on the Settings menu item:

<img src="https://files.readme.io/7ea55d80fcf7a86db156b47aafb9c5e0eff26cabb5bb832fafbd7c0fd2ade07f-settings-workspaces.png" align="center" />

***

## Workspace Settings

The menu on the left is where you can modify/configure Workspace settings, and has the following sections:

* Workspace
* Billing
* Privileges
* Accounts and Teams
* Authentication
* Custom domains
* Usage limits
* Manage policies

***

### Workspace

The Workspace profile settings are where you configure the Workspace name, avatar and contact email addresses (including billing email address if different from the primary email address):

<img src="https://files.readme.io/ebfd1af9bdfbb8a0015e8e885c01164fa68055d41a1ededa538c5fd55f77eb0d-workspace-profile.png" align="center" />

From within the Workspace profile settings, you have the ability to rename your organization's slug/identifier, and if you really need too, you can delete an organization (caution: this is a permanent action and cannot be undone).

> 🚧
>
> If you rename the Workspace, then the URI that is used to connect to any repositories will change.  This change will affect any users that currently use the repositories as the URI would no longer be valid.

***

### Billing

The Workspace Billing settings are where you add or change your payment source, view your invoices and select / modify your current plan.

<img src="https://files.readme.io/f68019bfd870d2451ab22cd5291ee99120e96b7a6931401e164727d0faacdb88-billing-settings.png" align="center" />

***

### Privileges

The Workspace Privileges settings are where you set global privileges and default object privileges.

#### Global Privileges

Global privileges settings are where you configure the permissions for current Workspace members to:

* Create new teams in the organization
* Invite members to the organization
* Invite collaborators to the organization
* Allow members to view other members' email addresses
* Create new package repositories (with admin permissions in the new repository)

<img src="https://files.readme.io/13a08bb0b4e09840757898328a717c25a2e978d68a1daff7816c0f44a06cf311-global-privileges.png" align="center" />

***

#### Default Object Privileges

Default object privileges settings are where you configure the default privileges for objects within a package repository:

<img src="https://files.readme.io/2437eb9334abde4fdaf268840bff7b39ea4894e795f7c01d3d094f20592229ac-object-privileges.png" align="center" />

|       |                                                     |
| :---- | :-------------------------------------------------- |
| Admin | Members have full control over repositories         |
| Write | Members can upload and download from the repository |
| Read  | Members can download from the repository            |
| None  | Members have no repository access                   |

***

### Accounts and Teams

Workspace Accounts and Teams settings is used to control the default visibility of teams:

<img src="https://files.readme.io/5a7210ce89a4ad40fc961f1500a76a7fa469f363f3ac7d7a07fbe2e7dd41a636-teams.png" align="center" />

* Hidden - Non-Members are not able to view the team
* Visible - Non-Members are able to view the team

### Authentication

Workspace Authentication settings is where you can configure and modify the authentication settings for your users, including:

* Set up and enforce SAML authentication
* Configure and modify SAML Group Sync
* Configure and modify SCIM
* Enforce two-factor authentication
* Create and manage OIDC provider settings

<img src="https://files.readme.io/0eae5024250d241c5d1bba1228990f707e72251fc86740061f1f0e6d19803f12-auth-settings.png" align="center" />

***

#### SAML

Workspace SAML settings is where you can enable and enforce SAML authentication. To enable SAML Authentication, you just need to either provide a URL to remote fetch your SAML XML Metadata, or provide the SAML XML Metadata directly inline using the form.

<img src="https://files.readme.io/2db51e96490046173aab8e5e306522f177c8f5d61e6a80a06946e649e5c0eba1-saml.png" align="center" />

#### SAML Group Sync

SAML Group Sync is where you can configure automatic mapping of your SAML Groups to Cloudsmith Teams. Please see the [SAML Group Sync](https://help.cloudsmith.io/docs/single-sign-on#saml-group-sync)  documentation for further details.

<img src="https://files.readme.io/75df13493e3495a67167702377ad5f544757f9b59c95bdaa9d34b5e665e5c0bf-saml-group-sync.png" align="center" />

***

#### SCIM

SCIM is where you can enable SCIM provisioning and de-provisioning and obtain your username and password to configure SCIM in your chosen Identity Provider. Please see the [Single Sign-On with Okta](https://help.cloudsmith.io/docs/single-sign-on-with-okta) documentation for an example of how you can configure SCIM for an Identity Provider.

<img src="https://files.readme.io/0d3164ccada96c7e05cfef347a7446d83389c218249a8916848a7099f769b781-scim.png" align="center" />

#### 2FA

Workspace 2FA is where you can enable Two-Factor Authentication.  This will force members to set up Two-Factor Authentication for additional security.

### Custom Domains

Custom domains let you utilize branded domains for any endpoint. Custom Domains settings are where you can view what custom domains have been configured for your Workspace account.

<img src="https://files.readme.io/0f67b9df1936ad70829df5e29411d625d3b5487ff7ce4a6c44b00960d575d6ac-custom-domains.png" align="center" />

### Usage Limits

The Usage Limits settings are where you can configure additional usage of artifact data and package delivery for the Workspace.

<img src="https://files.readme.io/4ffbcf8f4da7c4c67d9dd347744fe35e63cdc9595711d2215e19346ad077c10e-usage-limits.png" align="center" />

> 📘
>
> Setting a limit of 0GB will disable any overage

### Manage policies

Cloudsmith's Policy Management lets your protect your workspace by defining policies that suit your business. Manage Policies settings is where you can configure and manage your workspace policies. Policy types include:

* License policies
* Vulnerability policies
* Authentication policies
* Package deny policies

Please see [Policy Management](https://help.cloudsmith.io/docs/policy-management) documentation for more details on each policy type.