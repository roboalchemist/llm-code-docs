# Source: https://docs.snyk.io/implementation-and-setup/enterprise-setup/service-accounts.md

# Service accounts

{% hint style="info" %}
**Feature availability**\
Service accounts are available only for Enterprise plans. For more information, see [plans and pricing](https://snyk.io/plans/).

Free and Team plan users and Trial users have access to a Snyk user's token under their profile and can use this token to authenticate with a CI/CD, to run the CLI locally or on a build machine, and to authenticate with an IDE manually.
{% endhint %}

Service accounts are a special type of system user. Creating a service account generates an API token that is the only token associated with the service account and takes the place of standard user credentials. Snyk needs authentication in order to initiate Snyk processes.

You can set up a service account to use for automation rather than using a Snyk user's token and to help manage integrations.

You can generate single or multiple tokens on the Organization or Group levels to manage your integrations. Each service account has a unique name to make it easier to recognize. This name cannot be reused.

## When to use a service account

If you are an Enterprise user, you have a Snyk user's token under your profile. You also have access to service account tokens.

### Use a service account to create any kind of automation

This includes, but is not limited to, scanning using a CI/CD or build system plugin and automation with the [Snyk API](https://docs.snyk.io/implementation-and-setup/enterprise-setup/service-accounts/manage-service-accounts-using-the-snyk-api).

### Use a service account for GitHub Enterprise integration

If your team needs to set up a service account in GitHub, you must use [GitHub Enterprise](https://docs.snyk.io/developer-tools/scm-integrations/organization-level-integrations/github-enterprise), which is available only with Snyk Enterprise accounts.

Using a service account to authenticate with an integration rather than a Snyk user's token ensures continuity when users change roles or close their personal Snyk accounts.

### Use Group-level tokens in managing integrations

Use Group-level tokens to call Group API endpoints and Organization API endpoints, and to run the CLI for all Organizations in the Group.

Group roles are only for service accounts on the Group level and are limited to Enterprise accounts.

### Use your Snyk user's token for local scanning and testing API calls

If you are an Enterprise user, use your Snyk user's token to run the CLI locally on your machine, authenticate with an IDE manually, and make an occasional API call, for example, to test the use of an endpoint.

{% hint style="warning" %}
Snyk advises against using a service account token to authenticate with an IDE.
{% endhint %}

## Set up a Group or Organization-level service account

Generate single or multiple tokens on the Group or Organization levels to manage your integrations.

### Prerequisites to set up a service account

{% hint style="info" %}
Group viewers are not able to create service accounts, regardless of their Org role.
{% endhint %}

To create a Group service accoun&#x74;**,** you must be a Group admin. To create an Organization service account, you must be either a Group member and Org Admin, or a Group admin.

This process describes all options. Repeat the steps to create multiple tokens for the same or any other Group or Organization.

### How to set up a Group or Organization service account

* Log in to your account and navigate to the relevant Group and Organization that you want to manage.
* Click on **Settings** > **Service accounts** to view existing service accounts and their details.
* Click **Create a service account** to create a new one.\
  The screen that loads varies depending on whether you chose a **Group** or an **Organization.**

Note that while creating a **Group service account**, you can choose a Group-level role.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-0d0c3898c30cad03a05d17e9c358630fb47aa375%2FScreenshot%202022-07-06%20at%2012.01.28.png?alt=media" alt="Group settings"><figcaption><p>Group settings</p></figcaption></figure>

In contrast, while creating an **Organization service account,** you can choose Organization-level roles, including [custom roles](https://docs.snyk.io/snyk-platform-administration/user-roles/user-role-management#create-a-custom-role) that you have set up for your Organizations.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-3efca15933ab31a03cdc01760086efa7a9fb32cb%2FScreenshot%202022-07-06%20at%2012.06.35.png?alt=media" alt="Organization settings"><figcaption><p>Organization settings</p></figcaption></figure>

#### Enter a service account name

In the **Service Account** name field, enter a unique name for this token. Remember, this name can be used only once for tokens in the same area, either an **Organization** or a **Group**.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-c21a4c03d3fac445edb076b55e1396b872afccf1%2Fuuid-01c4cc98-23c9-3cb1-4972-1aa4f83ad98e-en.png?alt=media&#x26;token=39f1e699-538d-4c39-98f5-ec7e994277c4" alt="Service account name and role"><figcaption><p>Service account name and role</p></figcaption></figure>

#### Select a role

From the **Role** dropdown list, select an appropriate role.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-928105c23638a19b6395d60d24bcc172747342a7%2Fimage%20(1)%20(4).png?alt=media&#x26;token=af57072c-8397-415d-b074-e1773c84d039" alt="Roles"><figcaption><p>Roles</p></figcaption></figure>

For Group service accounts, choose from the following list of roles to configure the scope of the token; Snyk recommends selecting Viewer or Admin.

* **Group Viewer** enables read-only access. Note that to set an API token to be read-only and unable to write to the platform, you must use a service account and set it to Group Viewer. See [Snyk API token permissions users can control](https://docs.snyk.io/snyk-api/authentication-for-api/snyk-api-token-permissions-users-can-control).
* **Group Admin** enables full administrator access.
* **Group Member** associates a service account with a group but does not grant any specific access.

For **Organization service accounts**, choose from the standard roles, **Org Admin** or **Org** **Collaborator**, or a custom role if you have set up any custom roles. See [Pre-defined](https://docs.snyk.io/snyk-platform-administration/user-roles/pre-defined-roles) roles for the scope of the Org Admin and Org Collaborator roles.

### Create the service account

Click **Create**.

The token is generated and displayed.

Ensure that you copy this token, as you will not see it again. You can click **Close and Hide** once you have copied the token; whether you do or not, when you navigate away from this page, the token will no longer be visible. This is a standard security practice to keep your tokens safe.

#### How the token is associated with a Group and Organizations

The new token is also added to your **Existing service accounts** list, like the list in this example:

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-61a8f06ca370909c1292d121c731849f7c68b9fb%2Fuuid-799b88fc-d1d7-72c9-5ceb-30fb2a8d572e-en%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(14).png?alt=media&#x26;token=b46492d0-31d6-4966-945b-e400cae98492" alt="Existing service accounts for a Group"><figcaption><p>Existing service accounts for a Group</p></figcaption></figure>

In addition, if you created the token for the entire Group with a **Group Admin** role, the token also appears in the **Existing service accounts** list for each of its Organizations, though it can only be edited at the **Group** level.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-d2c348bec9eeba42e094090d03daa5b4c1bd1c79%2Fuuid-1110723e-74e7-3090-3e69-da65f93acfcc-en.png?alt=media&#x26;token=0c97c232-a6ca-4b54-acc5-2b24b33b5f2d" alt="Existing accounts for an organization"><figcaption><p>Existing accounts for an Organization</p></figcaption></figure>

If you created the token from an Organization that is part of a Group, the token now also appears in the **Existing service account** list on the Group level. From that list, the Group Admin can also change the token name or delete it.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-8d4eab9032148b48306cb654c29e717bcb05b145%2Fuuid-50563edb-6a75-9f37-2040-cd814fdf9ead-en.png?alt=media&#x26;token=a32007ad-2ffa-4561-afb2-e7b137b8b133" alt="Group service accounts with Organization accounts listed"><figcaption><p>Group service accounts with Organization accounts listed</p></figcaption></figure>

## Update the name for a service account token

Click any of the links to update the name for a service account token:

* For **Group-level tokens**, from the **Group** level only
* For **Organization-level tokens**, from the relevant **Organization** and also from the **Group** level:

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-db14e3590242dfde6a30de7ee617c1c0b30c2c4d%2Fuuid-b34e3d10-bb0c-b608-bc08-12f2bf0a4fc0-en.png?alt=media&#x26;token=2ff08602-e887-4401-a5e2-d1c175dd4e11" alt="Update a service account name"><figcaption><p>Update a service account name</p></figcaption></figure>

## Edit and delete a service account

Administrators can change token names and delete tokens.

### What happens to the service account token for a deleted account

When you delete a service account, the API token associated with it is invalidated immediately.

When an account is managed with Groups, the Organization and the Group admins can delete tokens for the Organization; only Group admins can view and manage tokens on the Group level.

Deleting a service account is the same as revoking the API token.

### How to edit or delete a service account

* Log in to your account and navigate to the Group and Organization that you want to manage.

  For **Group tokens**, navigate to the Group level.\
  For **Organization tokens**, group admins can delete from either the Group or the relevant Organization; Organization admins should navigate to the relevant Organization.
* Click on **Settings** > **Service accounts**.
* Scroll to find the list of existing service accounts:

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-61a8f06ca370909c1292d121c731849f7c68b9fb%2Fuuid-799b88fc-d1d7-72c9-5ceb-30fb2a8d572e-en%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(14).png?alt=media&#x26;token=b46492d0-31d6-4966-945b-e400cae98492" alt="Existing service accounts for a Group"><figcaption><p>Existing service accounts for a Group</p></figcaption></figure>

* From the list of existing tokens:
  * Click the token name to navigate to **change the token name** and click **Save**.
  * Click **Delete** to **delete a token and invalidate it immediately**. When prompted, click **OK**. Remember that you cannot re-generate the same token.

## Assign roles and permissions to a service account

Users with the Group-level View, Create, and Edit service account permissions can set up new service accounts for their Organization and assign a role.

Select an Organization and navigate to **Settings** > **Service Accounts**. Provide a name, choose a role from the dropdown, and click **Create**.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-902b662e3f216e019fed9e01c9f6647ea495f6ee%2Fsnyk-service-accounts.png?alt=media" alt="Select a Role while creating Organization Service Account"><figcaption><p>Select a Role while creating Organization Service Account</p></figcaption></figure>

When you open a role that is assigned to a service account, the system displays a warning message. Consider the possible impact when you update the permissions associated with or delete a role that would lead to reassigning the service accounts and users to a new role.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-2062c6312b6a001818855cd2e3bc1153768415a2%2FScreenshot%202022-06-23%20at%2015.49.49.png?alt=media" alt="Warning that you are about to change a role assigned to a service account"><figcaption><p>Warning that you are about to change a role assigned to a service account</p></figcaption></figure>

{% hint style="warning" %}
Snyk prevents users from creating Organization service accounts with a role that has more privileges than those the user creating the service account has. If you try to create a service account with a role that has more privileges than you have, you will see the error **Cannot create a service account with a higher privilege role than yours**.
{% endhint %}

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-db6aa303a3b682f24af41227d46ec654dd828c72%2FScreenshot%202022-08-01%20at%2015.59.52.png?alt=media" alt="User cannot assign a more privileged role to a service account"><figcaption><p>User cannot assign a more privileged role to a service account</p></figcaption></figure>
