# Source: https://docs.snyk.io/snyk-platform-administration/groups-and-organizations/organizations/manage-users-in-organizations.md

# Manage users in Organizations

In the **Organization** where you want to manage users, select the **Members** menu option.

{% hint style="info" %}
You must have the permissions required to perform these tasks. For details, see [Pre-defined user roles](https://docs.snyk.io/snyk-platform-administration/user-roles/pre-defined-roles) for a list of permissions.
{% endhint %}

## Add users

To add new users to your Organization, click **Add members**:

<div align="left"><figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-aeaac4d4bc895f3524f25dd9128a28f00a262ad6%2FScreen%20Shot%202022-02-24%20at%2012.51.45%20PM.png?alt=media&#x26;token=f7f49b1a-28e3-46e0-875c-bfc0070222bc" alt=""><figcaption><p>Add members to your Organization</p></figcaption></figure></div>

You can do the following on the **Add members** screen:

* Select **Invite new members** to send an email invitation to a new user. Enter the email addresses of users to invite, separated by commas, and click **Send invite**.
* Select **Add existing members** to add existing members of your Group to the Organization. Select the users when prompted and click **Invite members.**
* For Free plan users only:\
  Select **Invite by link** to send a link; click **Copy link** and send the link yourself. Note that an invite link expires after 48 hours.
* Use the **New members join as** dropdown to define the default role of a user when joining, such as **Org admin**. For details, see [Manage permissions](https://docs.snyk.io/snyk-platform-administration/user-roles/pre-defined-roles).

For a demonstration of adding users, view this video:

{% embed url="<https://thoughtindustries-1.wistia.com/medias/qqmkcaequj>" %}
Inviting members to an Organization
{% endembed %}

## Revoke pending invites

Follow these steps to cancel pending invites:

1. On the **Members** page, click the **Revoke pending invites link**, which appears when there is at least one pending invite.\\

   <figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-d487b1af18115d86fefc0192fe07b4667195f08b%2FRevoke.png?alt=media" alt=""><figcaption><p>Revoke pending invites</p></figcaption></figure>
2. In the **Pending invites in \_your organization's name**\_ modal that appears, click the trash icon next to the name of the user to cancel the invite.

## Change member roles

To change the role of a user, click on the **Role** entry for the member and use the dropdown to select the new role:

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-80887f353f4a659fba0fa9cf9c8666e5ef214570%2Forg-member-change-role.png?alt=media" alt=""><figcaption><p>Select new role</p></figcaption></figure>

{% hint style="warning" %}
For Enterprise plan customers who create custom roles, Snyk prevents users from assigning roles to other users who have more privileges. If you try to update a role, invite a new user, or add an existing user with a role that has more privileges than you have, you will see the error **Cannot assign higher privilege role**.
{% endhint %}

## Delete Organization members

Follow these steps to delete a member from the Organization:

1. Click the trash icon next to the user.
2. Click **Delete member from** \[**your Organization’s name]** when prompted.

## Filter and sort views of Organization members

### Filter views

Click the filter icon to expand the filter sidebar and then choose to filter the members displayed by role or authentication method:

<div align="left"><figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-5b57187c9cef107832d2f38fb01e2f2529b5fc25%2Forg-member-filters.png?alt=media" alt=""><figcaption><p>Filter members by role or by authentication method</p></figcaption></figure></div>

### Sort views

Click on the column heading to sort user views:

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-f6e695fb756dceccf1b8c6b6c39afcf55c2741f1%2Forg-member-column-sort.png?alt=media" alt=""><figcaption><p>Sort user views</p></figcaption></figure>

You can sort by name, authentication method, role, and date joined.
