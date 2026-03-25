# Source: https://docs.rootly.com/managing-users/inviting-users-via-third-party-integrations.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Inviting Users via Third-Party Integrations

> Invite users directly from supported integrations such as Slack, Opsgenie, PagerDuty, and Splunk On-Call.

You can invite users directly from supported third-party integrations to quickly onboard your team without manually entering email addresses.

Rootly currently supports inviting users from:

* **Slack**
* **Opsgenie**
* **PagerDuty**
* **Splunk On-Call (formerly VictorOps)**

<Callout icon="info" color="#3b82f6">
  The integration must be configured before users can be imported or invited.
</Callout>

## Invite Users from an Integration

<Steps>
  <Step title="Open Organization Settings">
    In the top-left corner, click the drop-down next to your organization name and select **Organization Settings**.

        <img src="https://mintcdn.com/rootly/JFQ1ZeVNi4nNRKF5/images/user-management/invitememberbuttons.webp?fit=max&auto=format&n=JFQ1ZeVNi4nNRKF5&q=85&s=54283a985cf94a077bc09bce38aefaa6" alt="Invite Member buttons." width="767" height="57" data-path="images/user-management/invitememberbuttons.webp" />
  </Step>

  <Step title="Open the integration invite flow">
    Select **[Members](https://rootly.com/account/memberships)**, then choose **Invite from \[Integration]**.

    Depending on the integrations configured for your organization, you may see:

    * **Invite from Slack**
    * **Invite from Opsgenie**
    * **Invite from PagerDuty**
    * **Invite from Splunk On-Call**
  </Step>

  <Step title="Select users">
    Rootly loads a list of users from the selected integration.

    Use the search field to filter users by name or email (or username for Opsgenie).

        <img src="https://mintcdn.com/rootly/JFQ1ZeVNi4nNRKF5/images/user-management/inviteslackusers.webp?fit=max&auto=format&n=JFQ1ZeVNi4nNRKF5&q=85&s=08157604fcbe514d51b796c843d90a1e" alt="Invite Slack Users modal" width="592" height="448" data-path="images/user-management/inviteslackusers.webp" />
  </Step>

  <Step title="Send invitations">
    Select the users you want to invite and click **Invite**.

    Invitation emails are sent automatically to the selected users.
  </Step>
</Steps>

## Role Assignment

Users invited through third-party integrations are assigned roles the same way as standard invitations.

You can assign:

* **Incident Response roles** for incident management permissions
* **On-Call roles** for schedules, alerting, and escalation workflows

If roles are not selected during invitation, Rootly applies your team’s **default roles**.

<Callout icon="info" color="#3b82f6">
  Configure default roles in **Organization Settings** to standardize permissions for new users.
</Callout>

## Integration Behavior

### Slack

Slack invitations may be limited by your configured **email domain restrictions**.

If your organization restricts invitations by email domain, only Slack users with matching email addresses will appear in the list.

### PagerDuty, Opsgenie, and Splunk On-Call

Users are pulled from the connected integration account. If expected users do not appear, verify the integration connection and permissions.

## Browsing and Searching Users

The integration user list supports:

* **Search** to filter users by name, email, or username
* **Pagination** for navigating large user lists
* **Sorting** by user name

This helps you quickly locate users in large organizations.

## User Acceptance and Sign-Up

After an invitation is sent, the user receives an email with a link to join your Rootly organization.

Accepting the invite takes them to the sign-up page:

<img src="https://mintcdn.com/rootly/JFQ1ZeVNi4nNRKF5/images/user-management/signuppage.webp?fit=max&auto=format&n=JFQ1ZeVNi4nNRKF5&q=85&s=5b63f3237a7d9662a55ce56b3614a612" alt="Rootly sign up form" width="589" height="784" data-path="images/user-management/signuppage.webp" />

Users can sign in using:

* **Google**
* **Slack**
* **SSO**
* **Email and password**

Passwords must include:

* At least **10 characters**
* One **lowercase letter**
* One **uppercase letter**
* One **number**
* One **special character**

After completing sign-up, the user is added to your organization with the assigned roles.

## Best Practices

* Confirm integrations are configured before inviting users
* Review your default role configuration before onboarding users
* Use integration-based invitations to onboard large teams faster
* Use search to locate specific users in large integration lists

## Troubleshooting

<AccordionGroup>
  <Accordion title="The integration invite option does not appear" icon="plug">
    Ensure the integration is configured and connected in **Organization Settings → Integrations**.
  </Accordion>

  <Accordion title="No users appear in the list" icon="users">
    Verify the integration connection and permissions. If the integration cannot access user data, the list may appear empty.
  </Accordion>

  <Accordion title="Some Slack users are missing" icon="slack">
    Slack user visibility may depend on your configured email domains. Only users with matching domains may appear.
  </Accordion>

  <Accordion title="An invitation failed" icon="triangle-alert">
    Invitations may fail if the email address is invalid, the user is already a member, or a duplicate invitation already exists.
  </Accordion>

  <Accordion title="I cannot assign roles when inviting" icon="user-shield">
    Role assignment depends on your organization permissions and configuration. If roles are not set, default roles will be applied automatically.
  </Accordion>
</AccordionGroup>

## Related Documentation

<CardGroup cols={2}>
  <Card title="Inviting Users" icon="envelope" href="/team-user-management/inviting-users">
    Invite users manually by entering email addresses.
  </Card>

  <Card title="Managing Invitations" icon="paper-plane" href="/team-user-management/managing-invitations">
    View, resend, or delete pending invitations.
  </Card>

  <Card title="Slack Integration" icon="slack" href="/integrations/slack">
    Configure Slack for user imports and collaboration.
  </Card>

  <Card title="PagerDuty Integration" icon="plug" href="/integrations/pagerduty">
    Configure PagerDuty before inviting users from it.
  </Card>
</CardGroup>


Built with [Mintlify](https://mintlify.com).