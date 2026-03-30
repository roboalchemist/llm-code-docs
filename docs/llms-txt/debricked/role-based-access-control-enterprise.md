# Source: https://docs.debricked.com/product/administration/users/role-based-access-control-enterprise.md

# Role-Based Access Control (Enterprise)

{% hint style="info" %}
*This feature is only available for our* [*SCA Enterprise*](https://debricked.com/pricing/) *users. Already have an account?* [*Click here to upgrade.*](https://debricked.com/app/en/repositories?billingModal=enterprise,free)
{% endhint %}

### Role-Based Access Control (RBAC)&#x20;

Role-Based Access Control (RBAC) allows you to grant and enforce access to functionalities and integrated repositories by assigning pre-defined roles to users. To give you better control over what functionality and data can be accessed by different users, these roles are assigned per individual repository. A single user can have one level of access rights for one repository and a different level for another. Anything a user can see and do in an integrated repository is defined by their role.

### Default user role

By default, once a new repository is integrated, only the company admin(s) get access to it (apart from the user integrating it), while other users are assigned the *No access* role. As a company admin, you are able to set the default role to one of your choice (up to the Reviewer role), which will be assigned to users every time a new repository is integrated.&#x20;

To do so:

1. Go to **Admin tools.**
2. Type your password to enter the administrative mode.
3. In the **Company Settings** tab, click the drop-down and select a role of your choice.

### User roles <a href="#userroles" id="userroles"></a>

Following are the seven different user roles:

<details>

<summary>No access</summary>

Users with this role can only see the name of the repository, but cannot access any more information.

</details>

<details>

<summary>Viewer</summary>

Recommended for non-code contributors who want to view or discuss your project.&#x20;

Users with this role can:

* View repository information
* View Start Left information
* Add comments
* Create exports
* Access the API (limited by endpoints)

</details>

<details>

<summary>Developer</summary>

Recommended for contributors who should be able to create pull requests and fix vulnerabilities.&#x20;

Users with this role can:

* Access the repository
* View repository information
* Integrate repositories
* Add comments
* View Start Left information
* Create exports
* Access the API (limited by endpoints)
* Create Pull Requests
* Pause vulnerabilities
* Perform manual uploads (only via the API)

</details>

<details>

<summary>Reviewer</summary>

Recommended for contributors who need to review and triage vulnerabilities and the like.&#x20;

Users with this role can:

* Access the repository
* View repository information
* Integrate repositories
* Add comments
* View Start Left information
* Create exports
* Access the API (limited by endpoints)
* Create Pull Requests
* Pause and snooze vulnerabilities
* Set and change the review status
* Perform manual uploads

</details>

<details>

<summary>Maintainer</summary>

Recommended for contributors who don’t need to review and triage, but are able to manage the repository, perform manual uploads, and invite users.&#x20;

Users with this role can:

* Access the repository
* View repository information
* Integrate repositories
* Add comments
* View Start Left information
* Create exports
* Access the API (limited by endpoints)
* Create Pull Requests
* Pause vulnerabilities
* Modify repository automation rules
* Edit other users’ permissions (up to own levels)
* Invite users
* Edit repository use cases
* Set the default branch for the repository
* Enable or disable GitHub scanning
* Delete repositories
* Delete commits
* Perform manual uploads

</details>

<details>

<summary>Repository admin</summary>

Recommended for people who need full access to the repository, including reviews and triaging.&#x20;

Users with this role can:

* Access the repository
* View repository information
* Integrate repositories
* Add comments
* View Start Left information
* Create exports
* Access the API (limited by endpoints)
* Create Pull Requests
* Pause and snooze vulnerabilities
* Modify repository automation rules
* Edit other users’ permissions (up to own levels)
* Invite users
* Edit repository use cases
* Set the default branch for the repository
* Enable or disable GitHub scanning
* Delete the repository
* Delete commits
* Perform manual uploads
* Set and edit the review status

</details>

<details>

<summary>Company admin</summary>

The highest level of access. Recommended for people who need full access to all repositories and settings.&#x20;

Users with this role can perform all actions of a Repository admin and also:

* Modify all automation rules
* Edit all use cases
* Delete the company account
* Access billing self-serve
* Whitelist email domains
* Enforce 2 factor authentication
* Change SSO settings
* Modify default automations
* Toggle allowing or disallowing snooze
* Delete other accounts
* Disable other accounts
* Update account information for other users
* Manage policies

</details>

### Available actions for each user role <a href="#companyadmin" id="companyadmin"></a>

<table><thead><tr><th width="200">Action</th><th width="90">Viewer</th><th width="107">Developer</th><th>Reviewer</th><th>Maintainer</th><th>Repository Admin</th><th>Company Admin</th></tr></thead><tbody><tr><td>View repository information</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td></tr><tr><td>View Start Left information</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td></tr><tr><td>Access to API</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td></tr><tr><td>Create exports</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td></tr><tr><td>Add comments</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td></tr><tr><td>Access the repository</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td></tr><tr><td>Integrate repositories</td><td> </td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td></tr><tr><td>Create Pull Requests</td><td> </td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td></tr><tr><td>Pause vulnerabilities</td><td> </td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td></tr><tr><td>Perform manual uploads</td><td> </td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td></tr><tr><td>Snooze vulnerabilities</td><td> </td><td> </td><td>✓</td><td> </td><td>✓</td><td>✓</td></tr><tr><td>Set and change the review status</td><td> </td><td> </td><td>✓</td><td> </td><td>✓</td><td>✓</td></tr><tr><td>Modify automation rules for a given repository</td><td> </td><td> </td><td> </td><td>✓</td><td>✓</td><td>✓</td></tr><tr><td>Edit other users’ permissions (up to own levels)</td><td> </td><td> </td><td> </td><td>✓</td><td>✓</td><td>✓</td></tr><tr><td>Invite users</td><td> </td><td> </td><td> </td><td>✓</td><td>✓</td><td>✓</td></tr><tr><td>Edit repository use cases</td><td> </td><td> </td><td> </td><td>✓</td><td>✓</td><td>✓</td></tr><tr><td>Set the default branch for the repository</td><td> </td><td> </td><td> </td><td>✓</td><td>✓</td><td>✓</td></tr><tr><td>Enable or disable GitHub scanning</td><td> </td><td> </td><td> </td><td>✓</td><td>✓</td><td>✓</td></tr><tr><td>Delete repositories</td><td> </td><td> </td><td> </td><td>✓</td><td>✓</td><td>✓</td></tr><tr><td>Delete commits</td><td> </td><td> </td><td> </td><td>✓</td><td>✓</td><td>✓</td></tr><tr><td>Create access tokens</td><td> </td><td> </td><td> </td><td> </td><td>✓</td><td>✓</td></tr><tr><td>Delete the company account</td><td> </td><td> </td><td> </td><td> </td><td> </td><td>✓</td></tr><tr><td>Access billing self-serve</td><td> </td><td> </td><td> </td><td> </td><td> </td><td>✓</td></tr><tr><td>Whitelist email domains</td><td> </td><td> </td><td> </td><td> </td><td> </td><td>✓</td></tr><tr><td>Enforce 2 factor authentication</td><td> </td><td> </td><td> </td><td> </td><td> </td><td>✓</td></tr><tr><td>Change SSO settings</td><td> </td><td> </td><td> </td><td> </td><td> </td><td>✓</td></tr><tr><td>Modify default automations</td><td> </td><td> </td><td> </td><td> </td><td> </td><td>✓</td></tr><tr><td>Toggle allowing/disallowing snooze</td><td> </td><td> </td><td> </td><td> </td><td> </td><td>✓</td></tr><tr><td>Delete other accounts</td><td> </td><td> </td><td> </td><td> </td><td> </td><td>✓</td></tr><tr><td>Disable other accounts</td><td> </td><td> </td><td> </td><td> </td><td> </td><td>✓</td></tr><tr><td>Update information for other user</td><td> </td><td> </td><td> </td><td> </td><td> </td><td>✓</td></tr><tr><td>Manage policies</td><td></td><td></td><td></td><td></td><td></td><td>✓</td></tr></tbody></table>

### Assign roles when inviting new users <a href="#howdoiassignroleswheninvitingnewusers" id="howdoiassignroleswheninvitingnewusers"></a>

1. Go to **Admin tools.** You can also go to either **Repositories, Vulnerabilities** or **Dependencies** view.
2. If needed, type your password to enter the administrative mode.
3. Click **Invite users.**
4. Select the repository(s) you want the users to be invited to.
5. Add the emails of the invitee(s).
6. Select a user role for each of the invitee.
7. Click **Create invite**.
8. The invitation then shows up in the **Invitations to send** tab. Here, you can **Edit** or **Delete** it if needed.
9. &#x20;Once you review it, click **Send invite.**
10. The invitation then shows up in **Sent invitations**. Here, you can withdraw the invitation by clicking **Delete**.

### Modify access for an existing user <a href="#howdoimodifyaccessofanexistinguser" id="howdoimodifyaccessofanexistinguser"></a>

1. Go to **Admin tools.**
2. Type your password to enter the administrative mode.
3. In the **Users** tab, find a list of users in your company. If you hover over the rule name in the **User role** column, you can see all of the current roles of that user and their scope(s).
4. To edit the role, click **Edit** (pen icon) on the right side of the table.
5. Click either the **Handle access** tab, or **Handle access** button. Here, you can edit the user’s existing role(s) and their scope(s).&#x20;
6. To assign a new role click the **+** button.

For information on configuring user access using API, refer the following topic:

{% content-ref url="../../../tips-and-tricks/workarounds/configuring-user-access-using-api" %}
[configuring-user-access-using-api](https://docs.debricked.com/tips-and-tricks/workarounds/configuring-user-access-using-api)
{% endcontent-ref %}
