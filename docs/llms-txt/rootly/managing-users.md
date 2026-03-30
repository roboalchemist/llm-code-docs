# Source: https://docs.rootly.com/managing-users/managing-users.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Manage Users

> View and manage organization members, including their contact information, roles, and integration statuses in Rootly.

The **Members** page gives you a centralized view of everyone in your Rootly organization. From here, you can review member details, check connected integrations, and manage access and roles.

<Callout icon="info" color="#3b82f6">
  Contact information such as phone numbers and device status may only be visible to **Owners**, **Admins**, or users with the appropriate contact-viewing permissions.
</Callout>

## Access the Members Page

<Steps>
  <Step title="Open Organization Settings">
    In the top-left corner, click the drop-down next to your organization name and select **Organization Settings**.
  </Step>

  <Step title="Navigate to Members">
    Select **[Members](https://rootly.com/account/memberships)**.
  </Step>

  <Step title="View and manage users">
    The Members table displays all active users along with their:

    * **Name**
    * **Email**
    * **Phone number**
    * **Mobile device status**
    * **Slack connection status**
    * **Incident response role**
    * **On-call role**

    Hover over a user row to access quick actions, or open a member to update their details.
  </Step>
</Steps>

## What You Can Do

From the Members page, you can:

<CardGroup cols={2}>
  <Card title="Manage Roles" icon="user-pen">
    Update incident response and on-call roles for members in your organization.
  </Card>

  <Card title="Review Contact Details" icon="phone">
    View member contact information used for alerts and escalations, based on your permissions.
  </Card>

  <Card title="Check Integrations" icon="plug">
    See whether users have connected Slack or registered a mobile device.
  </Card>

  <Card title="Remove Access" icon="user-minus">
    Remove users who no longer need access to your Rootly organization.
  </Card>

  <Card title="Search and Filter" icon="magnifying-glass">
    Quickly find members by name, email, role, or connection status.
  </Card>

  <Card title="Export Members" icon="download">
    Export your member list for reporting or administrative review.
  </Card>
</CardGroup>

## Understand Member Information

### Contact Information

Each member record may include:

* **Email**: The member’s primary email address
* **Phone number**: Used for SMS or voice notifications
* **Mobile device status**: Indicates whether the member has connected a mobile device for push notifications

<Callout icon="warning" color="#f59e0b">
  Phone numbers and device status may be restricted based on your role and organization permissions.
</Callout>

### Integration Status

The Members table also shows whether a user has connected:

* **Slack**
* **A mobile device**

These statuses help confirm whether members are ready to receive notifications through the expected channels.

### Roles

Each member can have separate roles for:

* **Incident response**, which determines access to incident management features
* **On-call**, which determines access to on-call schedules, escalations, and alerting workflows

## Manage Users

### Edit roles

To update a user’s role:

1. Hover over the member row or open the member record
2. Select **Edit**
3. Update the user’s **Incident Response Role** or **On-Call Role**
4. Save your changes

### Remove a user

To remove a member from the organization:

1. Hover over the member row
2. Select **Delete** or use the actions menu
3. Confirm the removal

<Callout icon="warning" color="#f59e0b">
  Removing a user immediately revokes their access to the organization.
</Callout>

### Search and filter

Use search and filters to find members by:

* Name
* Email
* Slack connection status
* Mobile device status
* Incident response role
* On-call role

## Export Member Data

You can export the Members table for reporting or operational review.

1. Click **Export**
2. Choose your preferred format
3. Download the exported file

The exported data includes the member information visible to you based on your permissions.

## Frequently Asked Questions

<AccordionGroup>
  <Accordion title="Can users belong to multiple teams?" icon="users">
    Yes. Users can belong to multiple teams in Rootly, and each team membership can have its own roles and permissions.
  </Accordion>

  <Accordion title="What's the difference between Incident Response Role and On-Call Role?" icon="user-shield">
    **Incident Response Role** controls access to incident-related workflows and features. **On-Call Role** controls access to schedules, escalations, and alerting workflows.
  </Accordion>

  <Accordion title="Why can't I see phone numbers for some users?" icon="phone">
    Phone numbers and device status may be hidden if you do not have the required permissions to view contact information.
  </Accordion>

  <Accordion title="What happens when I remove a user?" icon="user-minus">
    Removing a user immediately revokes their access to the organization. Historical data may still remain for auditing or reporting purposes.
  </Accordion>

  <Accordion title="Why does Slack show as not connected?" icon="plug">
    This usually means the user has not connected their Slack account, or the Slack integration is not fully configured for the organization.
  </Accordion>

  <Accordion title="Can I export the member list?" icon="file-export">
    Yes. You can export the Members table using the **Export** option, subject to the data visible to you based on your permissions.
  </Accordion>
</AccordionGroup>

## Related Documentation

<CardGroup cols={2}>
  <Card title="User Roles" icon="user-shield" href="/team-user-management/roles">
    Learn more about incident response and on-call roles.
  </Card>

  <Card title="Inviting Users" icon="user-plus" href="/team-user-management/inviting-users">
    Learn how to add new users to your organization.
  </Card>

  <Card title="Slack Integration" icon="slack" href="/integrations/slack">
    Configure Slack for incident response and notifications.
  </Card>

  <Card title="Mobile App" icon="mobile-screen-button" href="/on-call/mobile-app">
    Learn how the Rootly mobile app supports notifications and response.
  </Card>
</CardGroup>


Built with [Mintlify](https://mintlify.com).