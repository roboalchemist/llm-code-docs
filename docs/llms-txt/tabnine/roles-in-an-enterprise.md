# Source: https://docs.tabnine.com/main/administering-tabnine/managing-your-team/roles-in-an-enterprise.md

# Roles in an Enterprise

This article describes how Tabnine Enterprise Server's Authorization roles are managed.

## Roles in the Tabnine System <a href="#roles-in-the-tabnine-system" id="roles-in-the-tabnine-system"></a>

There are three types of Tabnine roles:

### **Member/User**

A member is a user that's authorized to use Tabnine within your organization.\
To become a team member, a user must be part of one of Tabnine's teams defined in your organization.

A user can join one of the Tabnine teams by accepting an invitation that's generated via email invitation or invitation link.

### Team Lead

{% hint style="info" %}
The team lead role was introduced in version [5.25.0](https://docs.tabnine.com/main/administering-tabnine/release-notes).
{% endhint %}

The Team Lead role allows for a manager to further delegate tasks and more closely reflects the hierarchy of enterprise companies. It allows for easier user management with limited access to more advanced features and settings.

A team lead can do the following:

* View analytics of their own team
* Manage users of their own team
* Invite users to their team
* Managing team repositories ([5.26.0](https://docs.tabnine.com/main/administering-tabnine/release-notes#v5.26.0))
* *<mark style="color:yellow;">Managing team guidelines (coming soon)</mark>*

A team lead cannot invite, remove, or perform any operation on a user with a manager or admin role.

### Manager

{% hint style="info" %}
The manager role was introduced in version 5.8.0.
{% endhint %}

A manager (or Account Manager) is a team member who can manage teams and users but cannot configure or set up the account.

In addition to being a team member who can use Tabnine, the manager can perform the following actions in the management console UI:

* View Tabnine team members inside the Admin Console.
* Invite users to join Tabnine (as members, team leads, or managers).
* Deactivate or remove users (except for admins).
* Create new teams.
* View the usage report.
* Extract usage reports.
* Configure the workspace settings.

A manager cannot invite, remove, or perform any operation on a user with an admin role.

### **Admin**

An Admin (or Account Admin) is a team member who has all the privileges of a manager but can also have all the privileges of configuring and setting up the account.

In addition to all the privileges of an account manager, the Admin can perform the following actions:

* Invite or assign other Admins to the team.
* Deactivate or remove other Admins from Tabnine.
* Delete teams.
* View and configure the account settings: [General](https://docs.tabnine.com/main/administering-tabnine/managing-your-team/settings/general-settings), [Email](https://docs.tabnine.com/main/administering-tabnine/managing-your-team/settings/email-settings), [License](https://docs.tabnine.com/main/administering-tabnine/managing-your-team/settings/license-settings), and models.

{% hint style="info" %}
In private installations, certain admins are designated as **Installation Admins**. This implicit role is automatically assigned to the initial user of the installation.

To transfer the Installation Admin role to another admin, please contact <support@tabnine.com>.

**Installation Admins** have exclusive authority to:

* Configure and modify system-wide SMTP settings.
* Manage core system configuration parameters.
  {% endhint %}

#### Multi-Team Switching

As of [5.26.0](https://docs.tabnine.com/main/administering-tabnine/release-notes#v5.26.0), Admins can define a specific list of allowed teams per user. This prevents production delays from waiting for team switch approvals.

Users themselves can switch between the teams, but only the ones that have been defined by their respective Admins. Users can only be members of one team at a time (this may change in the future).&#x20;

To switch between teams, navigate to the new dropdown in the Tabnine IDE plugin and select your desired team:

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2FrasFcqnMBCMnK7BVMYJ4%2Funknown.png?alt=media&#x26;token=b9abf50e-693a-4ed9-88c2-3e904e6fcf1f" alt=""><figcaption></figcaption></figure>

### Comparison of Roles

This table summarizes all the differences between the four roles:

| Ability / Permission                                          | Member                                                                                                                                        | Team Lead                                                                                                                                     | Manager                                                                                                                         | Admin                                                                                                             |
| ------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| Use Tabnine within the org                                    | <mark style="color:green;">✓⃝</mark>                                                                                                          | <mark style="color:green;">✓⃝</mark>                                                                                                          | <mark style="color:green;">✓⃝</mark>                                                                                            | <mark style="color:green;">✓⃝</mark>                                                                              |
| View analytics                                                | <mark style="color:red;">**ⓧ**</mark>                                                                                                         | Own team only                                                                                                                                 | All teams                                                                                                                       | All teams                                                                                                         |
| Manage users                                                  | <mark style="color:red;">**ⓧ**</mark>                                                                                                         | Own team only                                                                                                                                 | <ul><li>Members</li><li>Team Leads</li><li>Managers</li></ul>                                                                   | <ul><li>Members</li><li>Team Leads</li><li>Managers</li><li>Admins</li></ul>                                      |
| Invite users                                                  | <mark style="color:red;">**ⓧ**</mark>                                                                                                         | Own team only                                                                                                                                 | <ul><li>Members</li><li>Team Leads</li><li>Managers</li></ul>                                                                   | <ul><li>Members</li><li>Team Leads</li><li>Managers</li><li>Admins</li></ul>                                      |
| Create/manage repositories                                    | <mark style="color:red;">**ⓧ**</mark>                                                                                                         | Own team only                                                                                                                                 | All teams                                                                                                                       | All teams                                                                                                         |
| Manage guidelines                                             | <mark style="color:red;">**ⓧ**</mark>                                                                                                         | <mark style="color:red;">**ⓧ**</mark> <mark style="color:yellow;">(coming soon)</mark>                                                        | All teams                                                                                                                       | All teams                                                                                                         |
| View usage reports                                            | <mark style="color:red;">**ⓧ**</mark>                                                                                                         | Own team only                                                                                                                                 | <mark style="color:green;">✓⃝</mark>                                                                                            | <mark style="color:green;">✓⃝</mark>                                                                              |
| Join multiple teams                                           | <mark style="color:red;">**ⓧ**</mark> <mark style="color:yellow;">(coming soon)</mark>                                                        | <mark style="color:red;">**ⓧ**</mark> <mark style="color:yellow;">(coming soon)</mark>                                                        | <mark style="color:red;">**ⓧ**</mark> <mark style="color:yellow;">(coming soon)</mark>                                          | <mark style="color:red;">**ⓧ**</mark> <mark style="color:yellow;">(coming soon)</mark>                            |
| Access “Teams” overview                                       | <mark style="color:red;">**ⓧ**</mark>                                                                                                         | <mark style="color:red;">**ⓧ**</mark>                                                                                                         | <mark style="color:green;">✓⃝</mark>                                                                                            | <mark style="color:green;">✓⃝</mark>                                                                              |
| Manage account-wide settings (Models, Jira, Provenance, etc.) | <mark style="color:red;">**ⓧ**</mark>                                                                                                         | <mark style="color:red;">**ⓧ**</mark>                                                                                                         | <mark style="color:green;">✓⃝</mark>                                                                                            | <mark style="color:green;">✓⃝</mark>                                                                              |
| Create or delete teams                                        | <ul><li><mark style="color:red;"><strong>ⓧ</strong></mark> Create</li><li><mark style="color:red;"><strong>ⓧ</strong></mark> Delete</li></ul> | <ul><li><mark style="color:red;"><strong>ⓧ</strong></mark> Create</li><li><mark style="color:red;"><strong>ⓧ</strong></mark> Delete</li></ul> | <ul><li><mark style="color:green;">✓⃝</mark> Create</li><li><mark style="color:red;"><strong>ⓧ</strong></mark> Delete</li></ul> | <ul><li><mark style="color:green;">✓⃝</mark> Create</li><li><mark style="color:green;">✓⃝</mark> Delete</li></ul> |
| Assign roles                                                  | <mark style="color:red;">**ⓧ**</mark>                                                                                                         | <ul><li>Members (own team only)</li></ul>                                                                                                     | <ul><li>Members</li><li>Team Leads</li><li>Managers</li></ul>                                                                   | <ul><li>Members</li><li>Team Leads</li><li>Managers</li><li>Admins</li></ul>                                      |
| Remove users                                                  | <mark style="color:red;">**ⓧ**</mark>                                                                                                         | Own team only                                                                                                                                 | <ul><li>Members</li><li>Team Leads</li><li>Managers</li></ul>                                                                   | <ul><li>Members</li><li>Team Leads</li><li>Managers</li><li>Admins</li></ul>                                      |
| View or configure license/system settings                     | <mark style="color:red;">**ⓧ**</mark>                                                                                                         | <mark style="color:red;">**ⓧ**</mark>                                                                                                         | <mark style="color:red;">**ⓧ**</mark>                                                                                           | <mark style="color:green;">✓⃝</mark>                                                                              |
| Installation-level settings (SMTP, system configs)            | <mark style="color:red;">**ⓧ**</mark>                                                                                                         | <mark style="color:red;">**ⓧ**</mark>                                                                                                         | <mark style="color:red;">**ⓧ**</mark>                                                                                           | Installation Admin only                                                                                           |

## Assigning and reassigning a role to another user

Admins and managers can assign (or reassign) a role to other users.

Managers can assign a Manager, Team Lead, or Member role.

Admins can assign Admin, Manager, Team Lead, or a Member role. Only Admins can reassign a role to another Admin.

Team leads can manage roles on their own teams *only*.

An Admin (or a manager) can assign a role to a user when inviting a new user by email or link by setting the role in the invitation popup. The admin can also reassign that role.

To assign or reassing a role, navigate to the User Management page. In the Role column of the table, select the arrow next to the current role and a dropdown menu will appear with all four role options to select from. Choose which one you want.

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-84436bfa332f498446af3ffeb6850eb9e3856217%2FUser%20Management%20update%202%20-%20Nov-10.png?alt=media" alt=""><figcaption></figcaption></figure>
