# Source: https://docs.asapp.com/agent-desk/integrations/user-management.md

# Source: https://docs.asapp.com/agent-desk/digital-agent-desk/user-management.md

# User Management

> Learn how to manage users and roles in the Digital Agent Desk.

You control the User Management (Roles and Permissions) within the Digital Agent Desk.

These roles dictate if a user can authenticate to *Agent Desk*, *Admin Dashboard*, or both. In addition, roles determine what view and data users see in the Admin Dashboard. You can pass User Data to ASAPP via *SSO*, AD/LDAP, or other approved integration.

<Frame>
  <img src="https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-6f3c5891-ad4d-bf0b-06f3-31d6bf3b96ac.png?fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=54905ac24ba5ff2ed16b53aa4a0b1366" data-og-width="1462" width="1462" data-og-height="1132" height="1132" data-path="image/uuid-6f3c5891-ad4d-bf0b-06f3-31d6bf3b96ac.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-6f3c5891-ad4d-bf0b-06f3-31d6bf3b96ac.png?w=280&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=8057d5387d513182f84c55e36cf6ad75 280w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-6f3c5891-ad4d-bf0b-06f3-31d6bf3b96ac.png?w=560&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=af2e242729027b50e9ff3d063d9fa93e 560w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-6f3c5891-ad4d-bf0b-06f3-31d6bf3b96ac.png?w=840&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=bbc0fc19332416a9b08de3a57236c7ac 840w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-6f3c5891-ad4d-bf0b-06f3-31d6bf3b96ac.png?w=1100&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=6bc45940f020776738e87bf79c84b0e0 1100w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-6f3c5891-ad4d-bf0b-06f3-31d6bf3b96ac.png?w=1650&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=81821f2d659c03c9911a3dc7e7ac4e1b 1650w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-6f3c5891-ad4d-bf0b-06f3-31d6bf3b96ac.png?w=2500&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=292f998e4aef93e57aae1783abee6bd9 2500w" />
</Frame>

This section describes the following:

* [Process Overview](#process-overview)
* [Resource Overview](#resource-overview)
* [Definitions](#definitions "Definitions")

## Process Overview

This is a high-level overview of the User Management setup process.

1. ASAPP demos the Desk/Admin Interface.
2. Call with ASAPP to confirm the access and permission requirements. ASAPP and you complete a Configuration spreadsheet defining all the Roles & Permissions.
3. ASAPP sends you a copy of the Configuration spreadsheet for review and approval. ASAPP will make additional changes if needed and send to you for approval.
4. ASAPP implements and tests the configuration.
5. ASAPP trains you to set up and modify User Management.
6. ASAPP goes live with your new Customer Interaction system.

## Resource Overview

The following table lists and defines all resources:

<table class="informaltable frame-box rules-all">
  <thead>
    <tr>
      <th class="th"><p>Feature</p></th>
      <th class="th"><p>Overview</p></th>
      <th class="th"><p>Resource</p></th>
      <th class="th"><p>Definition</p></th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td class="td" rowspan="2"><p>Agent Desk</p></td>
      <td class="td" rowspan="2"><p>The App where Agents communicate with customers.</p></td>
      <td class="td"><p>Authorization</p></td>
      <td class="td"><p>Allows you to successfully authenticate via Single Sign-On (SSO) into the ASAPP Agent Desk.</p></td>
    </tr>

    <tr>
      <td class="td"><p>Go to Desk</p></td>
      <td class="td"><p>Allows you to click <strong>Go to Desk</strong> from the Nav to open Agent Desk in a new tab. Requires Agent Desk access.</p></td>
    </tr>

    <tr>
      <td class="td"><p>Default Concurrency</p></td>
      <td class="td"><p>The default value for the maximum number of chats a newly added agent can handle at the same time.</p></td>
      <td class="td"><p>Default Concurrency</p></td>
      <td class="td"><p>Sets the default concurrency of all new users with access to Agent Desk if no concurrency was set via the ingest method.</p></td>
    </tr>

    <tr>
      <td class="td"><p>Admin Dashboard</p></td>
      <td class="td"><p>The App where you can monitor agent activity in real-time, view agent metrics, and take operational actions (e.g. biz hours adjustments)</p></td>
      <td class="td"><p>Authorization</p></td>
      <td class="td"><p>Allows you to successfully authenticate via SSO into the ASAPP Admin Dashboard.</p></td>
    </tr>

    <tr>
      <td class="td" rowspan="2"><p>Live Insights</p></td>
      <td class="td" rowspan="2"><p>Dashboard in Admin that displays how each of your queues are performing in real-time. You can drill down into each queue to gain insight into what areas need attention.</p></td>
      <td class="td"><p>Access</p></td>
      <td class="td"><p>Allows you to see Live Insights in the Admin navigation and access it.</p></td>
    </tr>

    <tr>
      <td class="td"><p>Data Security</p></td>
      <td class="td"><p>Limits the agent-level data that certain users can see in Live Insights. If a user is not allowed to see data for any agents who belong to a given queue, that queue will not be visible to that user in Live Insights.</p></td>
    </tr>

    <tr>
      <td class="td" rowspan="4"><p>Historical Reporting</p></td>
      <td class="td" rowspan="4"><p>Dashboard in Admin where you can find data and insights from customer experience and automation all the way to agent performance and workforce management.</p></td>
      <td class="td"><p>Power Analyst Access</p></td>

      <td class="td">
        <p>Allows you to see the Historical Reporting page in the Admin Navigation with Power Analyst access type, which entails the following:</p>

        <ul>
          <li><p>Access to ASAPP Reports</p></li>
          <li><p>Ability to change widget chart type</p></li>
          <li><p>Ability to toggle dimensions and filters on/off for any report</p></li>
          <li><p>Export data per widget and dashboard</p></li>
          <li><p>Cannot share reports to other users</p></li>
          <li><p>Cannot create or copy widgets and dashboards</p></li>
        </ul>
      </td>
    </tr>

    <tr>
      <td class="td"><p>Creator Access</p></td>

      <td class="td">
        <p>Allows you to see the Historical Reporting page in the Admin Navigation with Creator access type, which entails the following:</p>

        <ul>
          <li><p>Power Analyst privileges</p></li>
          <li><p>Can share reports</p></li>
          <li><p>Can create net new widgets and dashboards</p></li>
          <li><p>Can copy widgets and dashboards</p></li>
          <li><p>Can create custom dimensions/calculated metrics</p></li>
        </ul>
      </td>
    </tr>

    <tr>
      <td class="td"><p>Reporting Groups</p></td>

      <td class="td">
        <p>Out-of-the-box groups are:</p>

        <ul>
          <li><p>Everybody: all users</p></li>
          <li><p>Power Analyst: Users with Power Analyst Role</p></li>
          <li><p>Creator: Users with Creator role</p></li>
        </ul>

        <p>If a client has data security enabled for Historical Reporting, policies need to be written to add users to the following 3 groups:</p>

        <ul>
          <li><p>Core: Users who can see the ASAPP Core Reports</p></li>
          <li><p>Contact Center: Users who can see the ASAPP Contact Center Reports</p></li>
          <li><p>All Reports: Users who can see both the ASAPP Contact Center and ASAPP Core Reports</p></li>
        </ul>

        <p>If you have any Creator users, you may want custom groups created. This can be achieved by writing a policy to create reporting groups based on a specific user attribute (i.e. I need reporting groups per queue, where queue is the attribute).</p>
      </td>
    </tr>

    <tr>
      <td class="td"><p>Data Security</p></td>
      <td class="td"><p>Limits the agent-level data that certain users can see in Historical Reporting. If anyone has these policies, then the Core, Contact Center, and All Reports groups should be enabled.</p></td>
    </tr>

    <tr>
      <td class="td"><p>Business Hours</p></td>
      <td class="td"><p>Allows Admin users to set their business hours of operation and holidays on a per queue basis.</p></td>
      <td class="td"><p>Access</p></td>
      <td class="td"><p>Allows you to see Business Hours in the Admin navigation, access it, and make changes.</p></td>
    </tr>

    <tr>
      <td class="td"><p>Triggers</p></td>
      <td class="td"><p>An ASAPP feature that allows you to specify which pages display the ASAPP Chat UI. You can show the ASAPP Chat UI on all pages with the ASAPP Chat SDK embedded and loaded, or on just a subset of those pages.</p></td>
      <td class="td"><p>Access</p></td>
      <td class="td"><p>Allows you to see Triggers in the Admin navigation, access it, and make changes.</p></td>
    </tr>

    <tr>
      <td class="td"><p>Knowledge Base</p></td>
      <td class="td"><p>An ASAPP feature that helps Agents access information without the needing to navigate any external systems by surfacing KB content directly within Agent Desk.</p></td>
      <td class="td"><p>Access</p></td>
      <td class="td"><p>Allows you to see Knowledge Base content in the Admin navigation, access it, and make changes.</p></td>
    </tr>

    <tr>
      <td class="td" rowspan="5"><p>Conversation Manager</p></td>
      <td class="td" rowspan="5"><p>Admin Feature where you can monitor current conversations individually in the Conversation Manager. The Conversation Manager shows all current, queued, and historical conversations handled by SRS, bot, or by a live agent.</p></td>
      <td class="td"><p>Access</p></td>
      <td class="td"><p>Allows you to see Conversation Manager in the Admin navigation and access it.</p></td>
    </tr>

    <tr>
      <td class="td"><p>Conversation Download</p></td>
      <td class="td"><p>Allows you to select 1 or more conversations in Conversation Manager to export to either an HTML or CSV file.</p></td>
    </tr>

    <tr>
      <td class="td"><p>Whisper</p></td>
      <td class="td"><p>Allows you to send an inline, private message to an agent within a currently live chat, selected from the Conversation Manager.</p></td>
    </tr>

    <tr>
      <td class="td"><p>SRS Issues</p></td>
      <td class="td"><p>Allows you to see conversations only handled by SRS in the Conversation Manager.</p></td>
    </tr>

    <tr>
      <td class="td"><p>Data Security</p></td>
      <td class="td"><p>Limits the agent-assisted conversations that certain users can see at the agent-level in the Conversation Manager.</p></td>
    </tr>

    <tr>
      <td class="td" rowspan="4"><p>User Management</p></td>
      <td class="td" rowspan="4"><p>Admin Feature to edit user roles and permissions.</p></td>
      <td class="td"><p>Access</p></td>
      <td class="td"><p>Allows you to see User Management in their Admin navigation, access it, and make changes to queue membership, status, and concurrency per user.</p></td>
    </tr>

    <tr>
      <td class="td"><p>Editable Roles</p></td>
      <td class="td"><p>Allows you to change the role(s) of a user in User Management.</p></td>
    </tr>

    <tr>
      <td class="td"><p>Editable Custom Attributes</p></td>
      <td class="td"><p>Allows you to change the value of a custom user attribute per user in User Management. If Off, then these custom attributes will be read-only in the list of users.</p></td>
    </tr>

    <tr>
      <td class="td"><p>Data Security</p></td>
      <td class="td"><p>Limits the users that certain users can see or edit in User Management.</p></td>
    </tr>
  </tbody>
</table>

## Definitions

The following table defines the key terms related to ASAPP Roles & Permissions.

<table class="informaltable frame-box rules-all">
  <thead>
    <tr>
      <th class="th"><p>Role</p></th>
      <th class="th"><p>Definition</p></th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td class="td"><p>Resource</p></td>
      <td class="td"><p>The ASAPP functionality that you can permission in a certain way. ASAPP determines Resources when features are built.</p></td>
    </tr>

    <tr>
      <td class="td"><p>Action</p></td>
      <td class="td"><p>Describes the possible privileges a user can have on a given resource. (i.e. View Only vs. Edit)</p></td>
    </tr>

    <tr>
      <td class="td"><p>Permission</p></td>
      <td class="td"><p>Action + Resource. ex. "can view Live Insights"</p></td>
    </tr>

    <tr>
      <td class="td"><p>Target</p></td>
      <td class="td"><p>The user or a set of users who are given a permission.</p></td>
    </tr>

    <tr>
      <td class="td"><p>User Attribute</p></td>
      <td class="td"><p>A describing attribute for a client user. User Attributes are either sent to ASAPP via accepted method by the client, or ASAPP Native.</p></td>
    </tr>

    <tr>
      <td class="td"><p>ASAPP Native User Attribute</p></td>

      <td class="td">
        <p>A user attribute that exists within the ASAPP platform without the client needing to send it. Currently:</p>

        <ul>
          <li><p>Role</p></li>
          <li><p>Group</p></li>
          <li><p>Status</p></li>
          <li><p>Concurrency</p></li>
        </ul>
      </td>
    </tr>

    <tr>
      <td class="td"><p>Custom User Attribute</p></td>
      <td class="td"><p>An attribute specific to the client's organization that is sent to ASAPP.</p></td>
    </tr>

    <tr>
      <td class="td"><p>Clarifier</p></td>
      <td class="td"><p>An additional and optional layer of restriction in a policy. Must be defined by a user attribute that already exists in the system.</p></td>
    </tr>

    <tr>
      <td class="td"><p>Policy</p></td>
      <td class="td"><p>An individual rule that assigns a permission to a user or set of users. The structure is generally: Target + Permission (opt. + Clarifier) = Target + Action + Resource (opt. + Clarifier)</p></td>
    </tr>
  </tbody>
</table>

## Grouping and Data Filtering via SSO

You can use attributes from your SSO/SAML configuration to control what chats and metrics users see within Live Insights, Conversation Manager, and User Management. This ensures users only see information relevant to their role and responsibilities.

These attributes create a hierarchical structure where:

* BPOs only see their service chats
* Workforce Management users see all chats and metrics for their BPO
* Agents see only their own chats and data
* Managers see chats for their assigned teams

To use this grouping, you need to:

<Steps>
  <Step title="Define attribute group mapping">
    Define groups using the following attributes:

    * BPO
    * Product
    * Role
    * Location

    Make sure to define a name for each group.

    Reach out to your ASAPP account team with the groups you define. ASAPP will implement the groups for you.
  </Step>

  <Step title="Send attributes to ASAPP">
    Ensure that your SSO/SAML System sends the necessary attributes to ASAPP.

    You can reach out to your ASAPP account team with any questions.
  </Step>

  <Step title="Use groups for filtering and queue association">
    Within Live Insights, Conversation Manager, and User Management, you can map the groups you defined to filters and queues. The groups will be applied to filter data and control access based on your defined mappings.
  </Step>
</Steps>
