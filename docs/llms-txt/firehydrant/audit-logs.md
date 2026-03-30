# Source: https://docs.firehydrant.com/docs/audit-logs.md

# Audit Logs

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th style={{ textAlign: "left" }}>
        Plans
      </th>

      <th style={{ textAlign: "left" }}>
        Required Permissions
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td style={{ textAlign: "left" }}>
        * <Glossary>Enterprise Plan</Glossary>
      </td>

      <td style={{ textAlign: "left" }}>
        * <Glossary>Owner</Glossary>
      </td>
    </tr>
  </tbody>
</Table>

Audit logs give organizations transparency and visibility into the events happening on the FireHydrant platform. From Runbook modifications to incident declarations, logins, and more, you can find a full history and detailed trail of events for security and audit purposes.

## Browsing Audit Logs

<Image align="center" alt="Audit Events page" border={false} caption="Audit Events page" src="https://files.readme.io/9b8b1fd775e21f8bfec490253de6ae6be4b7991e219ae11e79066106f7cb849e-image.png" width="650px" />

Audit logs can be found in your **Settings** under **Integrations** on the left-hand side. On this page, you'll see a paginated table of all relevant events for the given period which defaults to the past 7 days.

<Image align="center" alt="Details drawer expanded for a specific event" border={false} caption="Details drawer expanded for a specific event" src="https://files.readme.io/844ae1e8e4e54b379581cc580401a8b7a598f5394b119fec8ee84bc44103b66d-image.png" width="650px" />

For any entry on the table, you can click on it to expand key information about the particular event. You'll find information including:

* **Actor Details** - ID, Name, Source, and Email of the user who performed this action
* **Event Information** - Key (type) and Timestamp of specific activity/event that occurred
* **Resource Details** - ID, Type, and Change Status of the resource that was modified
* **Diff** - At the bottom of the details drawer, you should find a full diff of what items changed for the specific resource

<Image align="center" alt="Example of a Runbook modification event" border={false} caption="Example of a Runbook modification event" src="https://files.readme.io/be63d18ddd2914a3ac466b46a4697ff4fde43b8ebf885f52e73ff0e1f574096c-image.png" width="650px" />

The diff allows finding specific keys or parameters as well as filtering so you only see the differences/changes from the before/after states. It's highly useful for understanding exactly what changed, on top of when and by whom.

> 📘 Note:
>
> Audit logs are currently retained for 1 year.

## Filtering Audit Logs

The available filters include:

* **Event Type** - User Authentication, Resource Creation, Resource Update, and Resource Deletion
* **Actor Type** - User (done by a FireHydrant user), System (done by FireHydrant's automation, e.g., Runbooks), or Service (
* **Actor ID** - Takes an argument for a specific UUID of an actor whose events you want to find
* **Resource Type** - User Session, Configuration (any changes to FireHydrant settings), Permission (any changes to permissions, roles, etc.)
* **Resource ID** - Takes an argument for a specific UUID of a modified resource whose events you want to find
* **Response** - Success, Failed, or Error
* **Message** - The system's message or returned payload for the attempted event/action

## Currently Tracked

Currently, Audit Logs on FireHydrant can track user login/auth events as well as the creation, update, and deletion of various resources within the FireHydrant platform:

* **Signals**
  * **Escalation Policies**
  * **On-Call Schedules**
  * **Schedule Shifts**
* **Incident Management**
  * **Audiences**
  * **[API Keys](https://docs.firehydrant.com/docs/api-keys)**
  * **Incidents**
  * **Runbooks**
* **Other**
  * **User logins/authentication events**