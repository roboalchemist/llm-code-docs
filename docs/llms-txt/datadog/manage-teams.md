# Source: https://docs.datadoghq.com/cloudcraft/account-management/manage-teams.md

---
title: Manage Your Team
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Cloudcraft (Standalone) > Account Management > Manage Your Team
source_url: https://docs.datadoghq.com/account-management/manage-teams/index.html
---

# Manage Your Team

Make architecture reviews a team effort, share your real-time cloud infrastructure views, or collaboratively design your next project with the help of Cloudcraft teams.

Adding people to a team in Cloudcraft is easy, and allows everyone to collaborate in real-time.

The account owner and team members with the admin role can invite and remove users, as well as change member's roles.

Team features are available with Cloudcraft Pro and Enterprise plans.

## User management{% #user-management %}

### Invite new users{% #invite-new-users %}

To add members to your team, head to **User â Team settings** inside Cloudcraft.

Next, click the blue **Add member** button at the bottom of the **Manage Team** window that appeared.

{% image
   source="https://datadog-docs.imgix.net/images/cloudcraft/account-management/manage-teams/add-member.153ac0d173120ff2b1ef31afdc29967b.png?auto=format"
   alt="Screenshot of a 'Manage Team' interface in Cloudcraft with an 'Add Member' button highlighted." /%}

After clicking the button, you need to enter the user's email address and select a role for them on your team.

{% image
   source="https://datadog-docs.imgix.net/images/cloudcraft/account-management/manage-teams/add-teammate.e86e459821bbe79dc1c25e23a62be4f6.png?auto=format"
   alt="User interface for adding a team member in Cloudcraft with email input and role selection options." /%}

Selecting the correct role is a critical step in this process, as different roles have different levels of access. Select the role that best fits this user, but try to follow the [principle of least privilege](https://en.wikipedia.org/wiki/Principle_of_least_privilege).

Lastly, click the **Send invite** button to invite the user to your team. The user you invited will receive an email that includes a link to join your team and set up their account if they have not already.

The user will inherit their cross-organizational role if they are a member of a cross-organizational team.

### Remove existing users{% #remove-existing-users %}

When someone leaves the team â or if someone is added by mistake â you will want to remove them from your team. For that, head to **User â Team settings** inside Cloudcraft.

Next, select the user you want to have removed and click the gray trash can icon to the right of their name.

{% image
   source="https://datadog-docs.imgix.net/images/cloudcraft/account-management/manage-teams/trash-can-icon.a1f6f35ce9041246e915e6f617b1d086.png?auto=format"
   alt="Screenshot of a Cloudcraft Manage Team interface highlighting user collaboration features with delete action icon." /%}

A confirmation dialog will appear on your screen. Click the red **Remove** button and the user will be removed from your team.

Diagrams that were created by the removed user and that were shared with the team, will continue to be available to the team. If you need help migrating all of the user's data prior to removing them, please [contact our support team from inside the application](https://app.cloudcraft.co/app/support "Contact our support team").

Team access to data of removed users can also be restored if requested within our 30-day data retention period.

### Change an existing user's role{% #change-an-existing-users-role %}

If you need to change what a user has access to, head to **User â Team settings** inside Cloudcraft.

Next, click the gray pencil icon to the left of the user.

{% image
   source="https://datadog-docs.imgix.net/images/cloudcraft/account-management/manage-teams/edit-user.5d255ee32eadbf05c811ede16246b1bd.png?auto=format"
   alt="User interface for managing team members in Cloudcraft, highlighting edit options." /%}

On the next prompt, select a new role for the user and click the blue **Save** button. That is all there is to it.

## Team management{% #team-management %}

The multi-team management feature is only available for the Enterprise plan

### Create a new team{% #create-a-new-team %}

To create a new team for your account, head to **User â Team settings** inside Cloudcraft.

Click the blue **Create Team** button at the bottom of the team list, on the left.

{% image
   source="https://datadog-docs.imgix.net/images/cloudcraft/account-management/manage-teams/create-new-team.1b323d7fae44cae4b5def08623d6ec74.png?auto=format"
   alt="User interface for team management in Cloudcraft highlighting the 'Create Team' button with a list of team members." /%}

Next, you need to give your team a name and set its visibility. A **Visible** team can be seen by anyone in your organization, while a **Secret** team can only be seen by the account owner and members of the team.

{% image
   source="https://datadog-docs.imgix.net/images/cloudcraft/account-management/manage-teams/create-new-team-settings.bcffe2854a0b1e5965dc492390433abd.png?auto=format"
   alt="Screenshot of a team creation interface in Cloudcraft with options for team visibility and roles." /%}

Before creating the team, you can also check the **Cross-organizational** box to make this a cross-organizational team, which are teams with members that are automatically added to all other teams in your organization. An example of cross-organizational team would be a central security management team, which need visibility into all of the individual teams.

Unless they are already a member of another team, cross-organizational members inherit their cross-organizational roles.

Click the **Create** button at the bottom and that is it, you are ready to start inviting team members.

### Removing or updating existing teams{% #removing-or-updating-existing-teams %}

If you need to update or remove a team that you own, head to **User â Team settings** inside Cloudcraft.

Select the team you want to update and click on the gray pencil icon that sits next to its name.

{% image
   source="https://datadog-docs.imgix.net/images/cloudcraft/account-management/manage-teams/edit-team.3a02171f7703b79210983830bb9a0ccf.png?auto=format"
   alt="Screenshot from Cloudcraft with a highlighted edit button within the 'Manage Teams' interface." /%}

Here you can update the name of the team, make a visible team secret â and vice-versa â, change a team to cross-organizational, or remove a team entirely.

To update other team settings, make the change you want to make and click the blue **Save** button at the bottom.

{% image
   source="https://datadog-docs.imgix.net/images/cloudcraft/account-management/manage-teams/update-team-settings.bab19792e8251f2d7376be69161a6d08.png?auto=format"
   alt="Screenshot of a Cloudcraft's team management interface with options to edit team visibility and roles." /%}

To remove a team, simply click on the red **Delete** button and confirm that you want to delete your team.

{% image
   source="https://datadog-docs.imgix.net/images/cloudcraft/account-management/manage-teams/delete-team.f2243d735b29f889ecb9cab9d028a1ad.png?auto=format"
   alt="Cloudcraft interface showing a confirmation dialog for deleting a team." /%}

If you have any questions or trouble with the process, [get in touch with our support team](https://app.cloudcraft.co/app/support), and we will be happy to help.
