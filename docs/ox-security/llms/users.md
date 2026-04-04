# Source: https://docs.ox.security/admin-settings/users.md

# Users

{% hint style="success" %}
**At a glance:** View and manage the users in your organization. Invite new users, remove existing users, and assign them permissions to access features, applications, and issues.
{% endhint %}

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-8595e68b832b3f8f7fe67a79acc4c14fb087017f%2Fusers_new.png?alt=media" alt=""><figcaption></figcaption></figure>

### Overview <a href="#overview" id="overview"></a>

OX organizations can have multiple users, each with individually-managed permissions. Each user’s permissions are defined along 2 dimensions:

* **Role** defines a user's capabilities to access features and perform actions.
* **Scope** defines the applications and issues a user can access.

Permissions within each of these dimensions are assigned independently. In other words, you might decide to assign a user a **role** with broad functional capabilities but allow them to exercise those capabilities only within a narrowly defined set of apps and issues (limited **scope**).

{% hint style="info" %}
**Why does it matter?**

The independent abilities to: (1) assign a user the most appropriate option from a wide variety of roles; and (2) granularly define their access to only necessary applications and issues enables you to employ the [principle of least privilege](https://www.cloudflare.com/learning/access-management/principle-of-least-privilege/).
{% endhint %}

{% hint style="info" %}
**Note for companies with more than one OX organization**

Users are invited separately to each organization and can have different permissions (roles and scopes) in different organizations.
{% endhint %}

### Role <a href="#role" id="role"></a>

Each user in your organization must be assigned a **role** that defines the specific OX features the user can access and the actions they can perform. OX supports the following predefined roles:

* **Admin:** Has full visibility and management capabilities.
* **Policy Manager:** Has full visibility and management capabilities for applications, issues, policies, workflows, and connectors.
* **Dev Manager/Security Champion:** Can view applications and perform certain application-related actions; can view issues and perform all issue-related actions (including the ability to exclude issues and change severity).
* **Developer:** Can view issues and perform remediation/collaboration actions (such as open a PR, create a ticket, send to Slack, and others).
* **Read Only:** Has read-only access to all pages; cannot perform actions.

{% hint style="warning" %}
See the [Reference](#reference-ox-roles-and-capabilities) section at the end of this article for a detailed list of each role's capabilities.
{% endhint %}

The functional capabilities for each role are fixed: no "mixing and matching" allowed. However, you can change a user’s functional capabilities at any time by assigning them to a different role.

#### **EXAMPLE**

You have assigned Luke Skywalker the role of Dev Manager/Security Champion. This role gives Luke the ability to exclude an issue but not the ability to make an app irrelevant.

* **Question:** Can you keep Luke in the Dev Manager/Security Champion role but also give him the ability to make an app irrelevant? Can you take away his ability to exclude an issue?
* **Answer:** No. As long as Luke is in this role, you cannot give him the ability to make an app irrelevant. Nor can you remove his ability to exclude an issue. Of course, you can assign Luke a different role, and his capabilities will change to those defined by that role.

### Scope

In addition to their role, each user is assigned a scope that determines which applications and issues they can access. No matter what a user's role, they can view data and perform actions **only for applications within their scope and the issues related to those applications.**

By default, users can access all apps and issues in the organization. This unlimited scope is called **"Entire organization"**. OX provides 2 different ways to limit this access:

* **User's applications only:** The user can access only those applications (and related issues) for which they are an App owner.
* **Custom:** The user can access specific applications (and related issues) based on the apps' App owners and/or tags.

#### EXAMPLES

**Example 1:** Obi-Wan Kenobi is a developer in your organization. As a team lead, he is an App owner for several apps and works exclusively with them. Define Obi-Wan's scope as **User's applications only.** This allows him to access all the apps for which he is an App owner and all the issues related to those apps.

**Example 2:** Han Solo is a developer on Obi-Wan Kenobi's team. He isn't designated as an App owner for any apps, but he works only on apps for which Obi-Wan is an App owner. Define Han Solo's scope using the **Custom** option and give him access only to apps for which Obi-Wan Kenobi is an App owner.

**Example 3:** C3PO is a developer on Obi-Wan Kenobi's team. He isn't designated as an App owner for any apps, but he usually works on apps for which Obi-Wan is an App owner. However, C3PO is also an expert on PostgreSQL, and he is often asked by developers on other teams for help in resolving PostgreSQL security issues. Define C3PO's scope using the **Custom** option and give him access to:

* Apps for which Obi-Wan is an App owner; **and**
* Apps with the PostgreSQL tag.

This gives C3PO access to Obi-Wan's apps **and** apps tagged as PostgreSQL.

## User management actions

{% hint style="info" %}
**Note:** Only Admins can perform user management actions.
{% endhint %}

### Inviting new users

<div align="left"><figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-cd8545740a8e7e8c1d5548046a9b016704fde53a%2Finvite_users_dialog.png?alt=media" alt="" width="375"><figcaption></figcaption></figure></div>

**To invite a new user to your organization:**

1. From the OX side navigation menu, go to the **Users** page.
2. Click the <img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-47c88da75c0cc7786f42ed34bba0e0e8513397fd%2Finvite_users_button.png?alt=media" alt="" data-size="line"> button in the top right-hand corner of the page.
3. In the dialog, enter the user's email address.
4. From the **Assign role** dropdown, select the [role](#role) you want to assign.
5. In the **Assign scope** section:
   1. If you want to limit the user's [scope](#scope) to specific applications and issues, click the <img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-3a7240ff484be05daf68ea946c9404c6859a417b%2Flimit_scope_button.png?alt=media" alt="" data-size="line"> button.
      * **Important!** If you don't limit the user's scope, they will have access to all applications and issues in the organization **(Entire organization).**
   2. Select the method you want to use to limit the user's scope (**User's applications only** or **Custom**).
   3. If you are using the **Custom** method, select the App owners and tags for the applications the user can access.
6. Click the <img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-ad4c9586f175c20a7d606d4534e8c97eff0d807a%2Finvite_button.png?alt=media" alt="" data-size="line"> button.

The new user is added to the table in **Invited** status.

{% hint style="info" %}
To invite more than one user at the same time, press **Enter** on your keyboard between each email address or paste a comma- or semicolon-separated list of emails into the **Emails** field.

**Important!** The **role and scope** you select will be assigned to all the users you entered in the **Emails** field. To add groups of users in different roles or with different scopes, follow the steps separately for each role/scope combination.
{% endhint %}

#### Invitation acceptance

The new user receives an invitation at the email you entered. The invitation contains a link for them to create an OX account and join your organization.

* Once the user accepts the invitation and joins the organization, their status on the **Users** page will change to **Active.**
* If the user doesn't accept the invitation within 7 days, the invitation link will expire. You'll need to send them a new invitation to add them later.

### Revoking an invitation

If an invited user has not yet accepted an invitation to join the organization (in other words, they are still in **Invited** status), you can revoke the invitation.

**To revoke a user invitation:**

1. From the OX side navigation menu, go to the **Users** page.
2. Click the **Actions** icon <img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-22a02bc32aa25670ae35904e534bf6ad83dfb84c%2Factions_icon.png?alt=media" alt="" data-size="line"> on the far right side of the user's row.
3. In the dialog, confirm that you want to revoke the invitation.

The user is removed from the table.

{% hint style="info" %}
If a user has already accepted the invitation, it's not possible to revoke it. Instead, follow the steps to [remove the user](#removing-a-user).
{% endhint %}

### Changing a user's role or scope

**To change a user's role or scope:**

1. From the OX side navigation menu, go to the **Users** page.
2. Click the **Actions** icon <img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-22a02bc32aa25670ae35904e534bf6ad83dfb84c%2Factions_icon.png?alt=media" alt="" data-size="line"> on the far right side of the user's row.
3. Select the **Edit user** option.
4. If you want to change the user's role:
   1. In the **Assign role** dropdown, click **X** on the currently assigned role.
   2. From the dropdown, select the user's new role.
5. If you want to change the user's scope, make the necessary changes in the **Assign scope** section. (For more information, see step 5 of [Inviting new users](#inviting-new-users), above.)
6. Click the <img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-6b8d6757c3cf88cbb923ff386963ac11b3a20bdf%2Fsave_button.png?alt=media" alt="" data-size="line"> button.

The table now shows the user with their new role and/or scope.

### Removing a user

**To remove a user from your organization:**

1. From the OX side navigation menu, go to the **Users** page.
2. Click the **Actions** icon <img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-22a02bc32aa25670ae35904e534bf6ad83dfb84c%2Factions_icon.png?alt=media" alt="" data-size="line"> on the far right side of the user's row.
3. Select the **Remove user** option.
4. In the dialog, confirm that you want to remove the user.

The user is removed from the table and no longer has access to the organization.

## Reference: OX roles and capabilities

{% embed url="<https://docs.google.com/spreadsheets/d/1BgqqSwNX7HevmXcbzFhwLbT8G_69qBSPSZZJ5TLzQ8w/edit?usp=sharing>" %}
Scroll down to see more. Click [here](https://docs.google.com/spreadsheets/d/1BgqqSwNX7HevmXcbzFhwLbT8G_69qBSPSZZJ5TLzQ8w/edit?usp=sharing) to open or download the full list.
{% endembed %}
