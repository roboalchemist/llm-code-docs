# Source: https://docs.roboflow.com/roboflow/roboflow-ko/workspaces/team-members/invite-a-team-member.md

# Source: https://docs.roboflow.com/roboflow/roboflow-jp/workspaces/team-members/invite-a-team-member.md

# Source: https://docs.roboflow.com/roboflow/roboflow-hi/workspaces/team-members/invite-a-team-member.md

# Source: https://docs.roboflow.com/workspaces/team-members/invite-a-team-member.md

# Invite a Team Member

If you want to invite a Team Member to join your workspace, there are three possible ways to accomplish this.

First, navigate to the [Team Member management page](https://app.roboflow.com/settings/members), located under workspace settings.

## Invite via Email

Type multiple emails in a row, comma separated, and select a role to assign to each of these users. By clicking "Send Invites" you can send multiple invites simultaneously, as long as there are enough invites left.

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-6f1f7263406c404edba4a19a448614eadaad0acc%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>

Once invites have been sent, they can be tracked in the section below. From here, you can cancel or resend invites.

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-25bf665607f4be512be81ef96f4fcdf4e62aa1c9%2Fimage%20(6)%20(1).png?alt=media" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
A pending invite still counts against your team member seat limit, since the spot is being reserved.
{% endhint %}

## Invite via Link

You can always copy a link and share it directly with team members. A different URL is generated based on the selected role.

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-0e45bac7d43cbfc8df969da67dd7839ef1add125%2Fimage%20(9)%20(1).png?alt=media" alt=""><figcaption></figcaption></figure>

{% hint style="danger" %}
Be careful how you share your invite link! These links are static for your workspace and can't ever be changed.
{% endhint %}

## Allow Same Domain

If your workspace was created with a verified email (using Google sign in) you can always allow team members from the same domain (`company.com`) to have visibility into your workspace.

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-d6232b43c176a3fb0978b4a4eb594bcb449d8d32%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>

By flipping this switch, when a user first creates an account or creates a new workspace, they will be able to see the workspace from a list and request to join.

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-67aa8cb3879a5c76fd26d51462de2a538996c876%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>

### Accepting the request to join

There are two ways to accept a user's request to join your workspace.

#### Team Member management

On the [Team Member management page](https://app.roboflow.com/settings/members) you can accept the team member as a specific role or decline their request.

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-f4fdeafcebbccbc9412f12dc2f16defc7146dcc0%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>

#### Notifications

By clicking "Notifications" on the sidebar, you can see all incoming requests. From this modal, you can accept the user as a specific role or deny their request.

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-f5f465b2e66f31943016b041b2008d9188942fcb%2Fimage%20(14)%20(1).png?alt=media" alt=""><figcaption></figcaption></figure>

### Verifying Invitation Status

As an admin, you will receive confirmation emails letting you know when a new team member has joined your workspace.

You can also confirm their status by looking at the "Team Members with Access" section of the [Team Member management page](https://app.roboflow.com/settings/members). If their name and email appear in the list, they have access to the workspace!

## Troubleshooting

Having issues with team members getting access to your workspace? Check these common situations that can cause this to arise.

<details>

<summary>Workspace out of Team Member Seats</summary>

Check your [usage dashboard](https://app.roboflow.com/test-growth-plan/settings/usage) to see the number of team members in your workspace and your workspace's overall limits.

<div align="left" data-full-width="true"><figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-1db95e093cd46f85b936e687849bc1c80b883c08%2Fimage.png?alt=media" alt="" width="563"><figcaption><p>Workspace at the max limit of team members</p></figcaption></figure></div>

If you're currently at the maximum number of seats, there are two ways to resolve the issue:

1. Upgrade your plan to a higher level.
2. Remove an existing team member.

</details>

<details>

<summary>Invite Expired</summary>

For security, invites sent via email expire after 3 days of not being accepted by a team member. This can cause invite links in their email to no longer work.

If the invite is old, there are three ways to resolve the issue:

* Click "Resend" on the pending invite.
* Cancel the pending invite and invite the team member via email again.
* Invite the user to the workspace with another method.

</details>
