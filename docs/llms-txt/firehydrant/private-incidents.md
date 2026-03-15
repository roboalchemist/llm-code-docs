# Source: https://docs.firehydrant.com/docs/private-incidents.md

# Private Incidents

In some instances, you may need to manage an incident privately. For example, there may be a security incident or a large-scale incident where complex information needs to be coordinated without mass confusion—in these cases, a private incident may be your best option.

Private Incidents, sometimes called "restricted incidents," can only be managed by a select group of users and are not publicly viewable to the organization. This includes all places - in the incidents page, within analytics, in the FireHydrant weekly summary emails, and more.

## Prerequisites

To be able to work with Private Incidents, a user will need **Private access** or must be added to a private incident ad-hoc by someone with permissions. Learn about configuring these permissions at [Role-Based Access Controls (RBAC)](https://docs.firehydrant.com/docs/role-based-access-controls).

Users who have private incident access can:

* Declare private incidents
* Manage and respond to private incidents/*/*
* Convert a public incident to a private one

> 📘 /\_/\_Note
>
> Users with **private access** can view all Private Incidents across the whole platform. However, individual users with only public access can still be added to private incidents by someone who has private access.
>
> This allows users to have ad-hoc access to specific private incidents they're added to without having blanket access to all private incidents.

### Private Runbooks

By default, Public Runbooks cannot attach to Private incidents, and vice versa. This simplifies and prevents unintended public automation from executing for private incidents like notifying a public channel, sending out emails, posting to status pages, etc.

When creating a Runbook, any user with private access can check a Runbook's setting to **Restrict to private incidents only**. Checking this setting will:

* **Restrict editing it to Owners and Members with Private permissions**. Collaborators and Viewers cannot edit any Runbooks.
* **Prevent the Private Runbook from attaching to Public incidents.** This is irrespective of manual or automatic attachment rules.
* **Enable the Private Runbook to attach to Private incidents.** This is irrespective of manual or automatic attachment rules.

So if you want Runbooks to attach and execute for Private incidents, automatically or manually, you must have configured at least one Private Runbook.

> 🚧 Note:
>
> Setting a Private Runbook to "Always attach" will automatically attach and execute on newly-created Private incidents. However, Private Runbooks ***will not automatically attach to Public incidents converted to Private post-declaration.***

## Declaring a private incident

In FireHydrant, only **Owners** and private-access users have the ability to declare a private incident.

> 📘 Note:
>
> If you need all users to be able to create private incidents without necessarily accessing or responding to them, reach out to our support team.

### via Slack

<Image alt="Private Incident setting for Slack declaration modal" align="center" width="400px" src="https://files.readme.io/8678478-image.png">
  Private Incident setting for Slack declaration modal
</Image>

1. Anywhere in Slack, run the `/fh new` command.
2. Depending on your [field visibility settings](/docs/incident-fields#showinghiding-fields), you should see a **Private Incident** dropdown, or available to add under "Additional Details" dropdown.
3. Select "Yes", fill in other details, and declare the incident as normal.

### via Web UI

<Image alt="Private incident toggle in the UI" align="center" width="650px" src="https://files.readme.io/2cbd366-image.png">
  Private incident toggle in the UI
</Image>

1. From anywhere in the UI, click **Declare an incident** at the top right.
2. Depending on your [field visibility settings](/docs/incident-fields#showinghiding-fields), you should see a **Private Incident** checkbox, or a button to add the field under "Add details" section.
3. Check the box, fill in other details, and declare the incident as normal.

## Converting a Public Incident to Private

A user with private access can convert any public incident to.

**It's important to note that when converting an incident from Public to Private**:

* Any attached Runbooks will immediately terminate. Any repeating or pending steps within will be canceled.
* All existing user roles and teams will be unassigned from the incident unless they are specified on the conversion modal to transfer to the private incident.
* If the existing Slack incident channel is public, a new private channel will be created, and all FireHydrant activity will switch to that new private channel. The current public channel will remain and must be manually deleted.
  * We create a new channel because converting a channel from public to private is a highly restricted permission in Slack and is only available in Enterprise Grid accounts. Deleting channels also requires highly elevated permissions, which FireHydrant has opted not to request from users.
* If a user manually converts the existing Slack channel to private, a new channel will not be created, and the FireHydrant incident will continue using that channel.
* Once an incident is converted to Private, it cannot be converted back to Public.
* Incidents cannot be converted to private if they are already private, and they also cannot be converted if they are a [child of a parent incident](https://docs.firehydrant.com/docs/related-incidents).

> 🚧 Note:
>
> Runbooks set to "Always attach" will not automatically attach to incidents that converted to Private. They will only attach to incidents that were created as Private to begin with.

### via Slack

<Image alt="Slack conversion modal when running `/fh restrict`" align="center" width="400px" src="https://files.readme.io/4c68b01-image.png">
  Slack conversion modal when running `/fh restrict`
</Image>

1. Navigate to the incident channel.
2. Run `/fh private` or `/fh restrict`.
3. Assign any users or teams, and then desired Runbooks. Note that Public Runbooks, even if selected, cannot be attached to Private incidents and will fail. See [section above on private Runbooks](#private-runbooks).
4. Optionally check or uncheck removing the incident from an attached external status page if one has been attached for the incident.
5. Click "Restrict".

### via Web UI

<Image alt="Converting incident privacy in the UI" align="center" width="650px" src="https://files.readme.io/acdd2df-image.png">
  Converting incident privacy in the UI
</Image>

1. Navigate to the incident.
2. Click the ellipses/menu next to the "Resolve incident" button, and then select "Convert to private incident".
3. Assign any users or teams, and then desired Runbooks. Note that Public Runbooks, even if selected, cannot be attached to Private incidents and will fail. See [section above on private Runbooks](#private-runbooks).
4. Optionally check or uncheck removing the incident from an attached external status page if one has been attached for the incident.
5. Click "Convert".

## Ad-Hoc Users

Sometimes, situations may arise where people or teams need access to specific Private incidents on an ad hoc basis rather than blanket access to all of them.

### Assigning

<Image alt="Assigning responders via Slack" align="center" width="400px" src="https://files.readme.io/61c3d15-assign-users-slack.png">
  Assigning responders via Slack
</Image>

In these scenarios, any responder with Private incident access can [add these users or teams](https://docs.firehydrant.com/docs/adding-responders) as they normally would on any other incident.

Assignment allows access to those users and teams for this specific Private incident, and they will have permissions to interact with the incident based on their configured [access roles](https://docs.firehydrant.com/docs/role-based-access-controls).

FireHydrant will also handle automatically adding them to the appropriate Slack channel when they are assigned on the incident.

### Removing specific access

In the same way, access to a Private incident can be removed by unassigning a user from the incident, which revokes their access. Once revoked, when they try to access this incident from the UI, they will see a 404.

> 🚧 Note:
>
> However, if the removed user is in the private Slack channel for the incident, FireHydrant cannot automatically remove them because we lack sufficient permissions to do so. A Slack admin in your organization will need to remove them manually.

## Known constraints

### Slack Mentions

If someone is mentioned and then added to a private incident channel by something other than FireHydrant automation, they still would not be able to see the incident's details in the UI.

We recommend training and enabling your responders to ensure they're always using the `/fh assign role` or `/fh assign team` functions instead of directly `@`ing the user.

### API keys

Currently, API keys have **Owner** privileges. This means, in effect, anyone with access to an API key also has access over user permissions.

We recommend restricting applications and usage of the API key to avoid unauthorized privilege escalation.

### Incident counts and pagination when fetching via API

When the collection exceeds a certain size (\~10k or higher), pagination numbers may not match the actual length of returned collections. If you're using a script to fetch incidents via API, the script should rely on total item counts in lieu of pagination totals. Pagination cursoring should continue to function as expected.

## Next Steps

* For an overview on declaring incidents in general, see [Starting Incidents](https://docs.firehydrant.com/docs/starting-incidents).
* Learn more about configuring access permissions in [Private Incident Access](https://docs.firehydrant.com/docs/private-incident-access) or at [Role-Based Access Controls](https://docs.firehydrant.com/docs/role-based-access-controls).