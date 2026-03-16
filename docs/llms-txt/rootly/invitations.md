# Source: https://docs.rootly.com/managing-users/invitations.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Managing Invitations

> View, resend, and delete pending invitations from Organization Settings.

The **Invitations** page lets you manage pending invitations for users who have not yet joined your Rootly organization. From here, you can review invitation details, resend an invitation email, or remove an invitation that is no longer needed.

<Callout icon="info" color="#3b82f6">
  Invitation emails are sent automatically when an invitation is created. If a recipient does not receive the email, you can resend it from the Invitations page.
</Callout>

## Access the Invitations Page

<Steps>
  <Step title="Open Organization Settings">
    In the top-left corner, click the drop-down next to your organization name and select **Organization Settings**.
  </Step>

  <Step title="Navigate to Invitations">
    Select **[Invitations](https://rootly.com/account/invitations)** to view all pending invitations.

    The table shows each invitation’s:

    * **Email**
    * **Incident Response role**
    * **On-Call role**
    * **Sent date**
    * **Invited by**

        <img src="https://mintcdn.com/rootly/JFQ1ZeVNi4nNRKF5/images/user-management/invitations.webp?fit=max&auto=format&n=JFQ1ZeVNi4nNRKF5&q=85&s=f2319b3c52fb47e020c4006f1217e2c4" alt="" width="1118" height="320" data-path="images/user-management/invitations.webp" />
  </Step>

  <Step title="Manage a pending invitation">
    Hover over an invitation row to access available actions:

    * **Resend** to send the invitation email again
    * **Delete** to remove the invitation

    <Callout icon="warning" color="#f59e0b">
      Invitations cannot be edited. To change the email address or assigned roles, delete the invitation and create a new one.
    </Callout>
  </Step>
</Steps>

## What You Can Do

From the Invitations page, you can:

<CardGroup cols={2}>
  <Card title="View Pending Invitations" icon="list">
    See all outstanding invitations and review the roles assigned to each recipient.
  </Card>

  <Card title="Resend Invitations" icon="paper-plane">
    Send the invitation email again if the original message was not received.
  </Card>

  <Card title="Delete Invitations" icon="trash">
    Remove invitations that are no longer needed.
  </Card>

  <Card title="Review Assigned Roles" icon="user-shield">
    Confirm which Incident Response and On-Call roles will be assigned when the invitation is accepted.
  </Card>
</CardGroup>

## How Invitations Work

When you invite a user to Rootly:

1. An invitation email is sent to the specified email address
2. The recipient opens the invitation link
3. After accepting, the user joins the organization with the assigned roles
4. The invitation is removed from the pending list

If no roles are specified when the invitation is created, the team’s default roles are applied.

<Callout icon="info" color="#3b82f6">
  Invitations are tied to the invited email address. The recipient must accept the invitation using that email.
</Callout>

## Best Practices

* Double-check email addresses before sending invitations
* Assign roles carefully to avoid unnecessary permission changes later
* Resend invitations before creating duplicates
* Periodically remove stale invitations that are no longer needed

## Troubleshooting

<AccordionGroup>
  <Accordion title="The user did not receive the invitation email" icon="mail">
    Verify the email address is correct, ask the recipient to check their spam or junk folder, and resend the invitation if needed.
  </Accordion>

  <Accordion title="The invited user cannot accept the invitation" icon="triangle-alert">
    Confirm the user is signing in with the same email address that received the invitation. If the invitation was deleted or already accepted, create a new one.
  </Accordion>

  <Accordion title="I need to change the email address or assigned roles" icon="file-pen">
    Invitations cannot be edited. Delete the existing invitation and create a new one with the correct details.
  </Accordion>
</AccordionGroup>

## Related Documentation

<CardGroup cols={2}>
  <Card title="Inviting Users" icon="user-plus" href="/team-user-management/inviting-users">
    Learn how to create new invitations.
  </Card>

  <Card title="Managing Users" icon="user-gear" href="/team-user-management/manage-users">
    Learn how to manage existing organization members.
  </Card>

  <Card title="User Roles" icon="user-shield" href="/team-user-management/roles">
    Understand Incident Response and On-Call roles.
  </Card>

  <Card title="Manage User Permissions" icon="shield-check" href="/team-user-management/manage-user-permissions">
    Learn how permissions are controlled across teams and products.
  </Card>
</CardGroup>


Built with [Mintlify](https://mintlify.com).