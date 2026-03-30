# Source: https://docs.rootly.com/managing-users/inviting-users-via-web-ui.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Inviting Users

> Invite new users to join your Rootly organization and assign Incident Response or On-Call roles during setup.

Use invitations to add new users to your Rootly organization. You can invite one or more users at a time, assign roles during invitation, and let users join using the sign-in method configured for your organization.

<Callout icon="info" color="#3b82f6">
  Invitation emails are sent automatically after you create an invitation.
</Callout>

<Callout icon="lightbulb" color="#7748f6">
  You can invite multiple users at once by entering more than one email address in the invite flow.
</Callout>

## Invite Users

<Steps>
  <Step title="Open Organization Settings">
    In the top-left corner, click the drop-down next to your organization name and select **Organization Settings**.
  </Step>

  <Step title="Open the invite flow">
    Select **[Members](https://rootly.com/account/memberships)**, then click **+ Invite Member**.

        <img src="https://mintcdn.com/rootly/JFQ1ZeVNi4nNRKF5/images/user-management/Invitemember.webp?fit=max&auto=format&n=JFQ1ZeVNi4nNRKF5&q=85&s=dc038ff14724cbf28ad870aa90d26c3b" alt="Invite members modal." width="589" height="375" data-path="images/user-management/Invitemember.webp" />
  </Step>

  <Step title="Enter email addresses and assign roles">
    Enter one or more email addresses for the users you want to invite.

    You can separate multiple email addresses using:

    <Tip>
      **Commas**

      [maria@candly.org](mailto:maria@candly.org),[tim@candly.org](mailto:tim@candly.org),[kirija@candly.org](mailto:kirija@candly.org)

      **New lines**

      [maria@candly.org](mailto:maria@candly.org)

      [tim@candly.org](mailto:tim@candly.org)

      [kirija@candly.org](mailto:kirija@candly.org)

      **Spaces**

      [maria@candly.org](mailto:maria@candly.org) [tim@candly.org](mailto:tim@candly.org) [kirija@candly.org](mailto:kirija@candly.org)
    </Tip>

    You can optionally assign:

    * **Incident Response role**
    * **On-Call role**

    When inviting multiple users at once, the selected roles apply to all invited users in that batch.

    If no role is selected, the team’s default role is applied.

        <img src="https://mintcdn.com/rootly/JFQ1ZeVNi4nNRKF5/images/user-management/defaultrolenew.webp?fit=max&auto=format&n=JFQ1ZeVNi4nNRKF5&q=85&s=2a0cc9892e04edb245f5f13fe0284891" alt="Default Incident Response Role field." width="538" height="88" data-path="images/user-management/defaultrolenew.webp" />
  </Step>

  <Step title="Send the invitation">
    Click **Invite** to send the invitation email.
  </Step>
</Steps>

## What You Can Do

From the invite flow, you can:

<CardGroup cols={2}>
  <Card title="Invite One or More Users" icon="users">
    Add a single user or invite multiple users at the same time.
  </Card>

  <Card title="Assign Roles" icon="user-shield">
    Set Incident Response and On-Call roles during invitation.
  </Card>

  <Card title="Use Default Roles" icon="settings">
    Allow Rootly to apply your team’s default roles when no role is selected.
  </Card>

  <Card title="Streamline Onboarding" icon="mail-check">
    Send users directly into the account creation or sign-in flow.
  </Card>
</CardGroup>

## Role Assignment

You can assign roles during invitation to control what access a user receives after joining.

* **Incident Response roles** control access to incidents, workflows, retrospectives, and related configuration
* **On-Call roles** control access to schedules, escalation policies, alerting, and responder workflows

If a role is not selected, Rootly assigns the team’s default role for that product.

<Callout icon="info" color="#3b82f6">
  Configure default roles in **Organization Settings** to standardize access for new users.
</Callout>

<Callout icon="warning" color="#f59e0b">
  Ensure you have available seats for the roles you’re assigning. If seats are limited, some roles may be unavailable.
</Callout>

## Email Requirements

Invitations require valid email addresses that meet your organization’s requirements.

* **Valid format**
* **Not already a member**
* **Allowed email domain**, if your organization restricts invitations by domain

<Callout icon="info" color="#3b82f6">
  Rootly validates email addresses during invitation creation. Invalid addresses will return an error.
</Callout>

## User Acceptance and Sign-Up

After an invitation is sent, the user receives an email with a link to join your organization.

When they open the invitation, they can complete sign-up using one of the methods available in your environment, such as:

* **Google**
* **Slack**
* **SSO**
* **Email and password**

<img src="https://mintcdn.com/rootly/JFQ1ZeVNi4nNRKF5/images/user-management/signuppage.webp?fit=max&auto=format&n=JFQ1ZeVNi4nNRKF5&q=85&s=5b63f3237a7d9662a55ce56b3614a612" alt="Rootly sign up form." width="589" height="784" data-path="images/user-management/signuppage.webp" />

If the user signs up with email and password, the password must include:

* At least **10 characters**
* One **lowercase** letter
* One **uppercase** letter
* One **number**
* One **special character**

Once sign-up is complete, the user is added to your organization with the assigned roles.

## Bulk Invitations

When you invite multiple users at once, Rootly processes invitations in batches.

* Invitations may take longer to appear for larger batches
* Individual errors do not prevent valid invitations from being created
* You can review progress from the **Invitations** page

<Callout icon="info" color="#3b82f6">
  Large invitation batches may take a few minutes to complete.
</Callout>

## Who Can Send Invitations?

Invitation access depends on the user’s assigned permissions.

* **Owners** can send invitations
* **Admins** can send invitations
* **On-Call Admins** may be able to assign On-Call access, depending on configuration

<Callout icon="info" color="#3b82f6">
  Contact your team administrator if you do not have permission to invite users.
</Callout>

## Best Practices

* Configure default roles before inviting users with standard access needs
* Double-check email addresses before sending invitations
* Assign roles during invitation to reduce manual updates later
* Use bulk invitations when onboarding multiple users at once
* Review pending invitations and resend or remove them as needed

## Troubleshooting

<AccordionGroup>
  <Accordion title="The user did not receive the invitation email" icon="mail">
    Confirm the email address is correct, ask the user to check spam or junk folders, and resend the invitation if needed.
  </Accordion>

  <Accordion title="I need to change the assigned role or email address" icon="file-pen">
    Invitations cannot be edited after they are sent. Delete the pending invitation and create a new one with the correct details.
  </Accordion>

  <Accordion title="The user cannot accept the invitation" icon="triangle-alert">
    Make sure the user is signing in with the same email address that received the invitation. If the invitation is no longer valid, send a new one.
  </Accordion>

  <Accordion title="Cannot assign certain roles" icon="user-shield">
    This usually means your plan has reached its seat limit for that role type, or you do not have permission to assign that role.
  </Accordion>

  <Accordion title="Email validation fails" icon="envelope">
    The email may be invalid, already belong to an existing member, or fail your organization’s domain restrictions.
  </Accordion>

  <Accordion title="Bulk invitation is slow" icon="clock">
    Large invitation batches may take time to process. Check the Invitations page to review progress.
  </Accordion>
</AccordionGroup>

## Related Documentation

<CardGroup cols={2}>
  <Card title="Managing Invitations" icon="paper-plane" href="/team-user-management/managing-invitations">
    View, resend, or delete pending invitations.
  </Card>

  <Card title="Managing Users" icon="user-gear" href="/team-user-management/manage-users">
    Manage existing users in your organization.
  </Card>

  <Card title="User Roles" icon="user-shield" href="/team-user-management/roles">
    Learn more about Incident Response and On-Call roles.
  </Card>

  <Card title="Manage User Permissions" icon="shield-check" href="/team-user-management/manage-user-permissions">
    Understand how permissions are controlled across teams and products.
  </Card>
</CardGroup>


Built with [Mintlify](https://mintlify.com).