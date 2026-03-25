# Source: https://www.courier.com/docs/platform/analytics/audit-trail.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Audit Trail

> Track workspace user activity including API key changes, user actions, publishing events, and integration updates.

<Note>
  **Availability**: Audit Trail is available for Enterprise customers. Contact [Courier Support](mailto:support@courier.com) for access.
</Note>

The Audit Trail provides a record of security-relevant events in your workspace. Use it to monitor API key management, user access changes, publishing activity, and integration configuration for compliance and security purposes.

<Frame caption="Audit Trail in Settings">
  <img src="https://mintcdn.com/courier-4f1f25dc/BELbxySbf5lFIcUH/assets/platform/content/audit-trail.png?fit=max&auto=format&n=BELbxySbf5lFIcUH&q=85&s=150f1780b42db97ca30ff2008e2b0baa" alt="Audit Trail showing event log with timestamps, source, actor, and target" width="3456" height="1798" data-path="assets/platform/content/audit-trail.png" />
</Frame>

## Supported Events

### API Keys

| Event             | Description                   |
| ----------------- | ----------------------------- |
| `API Key Created` | New API key generated         |
| `API Key Deleted` | API key removed               |
| `API Key Rotated` | API key credentials refreshed |

### Users

| Event               | Description                   |
| ------------------- | ----------------------------- |
| `User Invited`      | New user invited to workspace |
| `User Role Changed` | User's permissions updated    |
| `User Deleted`      | User removed from workspace   |
| `User Logout`       | User signed out               |

### Workspace Settings

| Event                                        | Description                                  |
| -------------------------------------------- | -------------------------------------------- |
| `Workspace Name Changed`                     | Workspace renamed                            |
| `Workspace Discoverability Enabled/Disabled` | Controls whether workspace appears in search |
| `Workspace Accessibility Changed`            | Workspace access settings updated            |
| `SSO Required Enabled/Disabled`              | Single sign-on requirement toggled           |
| `Click-Through Tracking Enabled/Disabled`    | Link tracking toggled                        |
| `Email Open Tracking Enabled/Disabled`       | Open tracking pixel toggled                  |
| `Guard Rails Updated`                        | Workspace safety limits changed              |

### Templates

| Event                                     | Description                           |
| ----------------------------------------- | ------------------------------------- |
| `Notification Published`                  | Template published to production      |
| `Notification Deleted`                    | Template removed                      |
| `Notification Duplicated`                 | Template copied                       |
| `Notification Draft Created`              | New draft version created             |
| `Notification Rolled Back`                | Template reverted to previous version |
| `Notification Subscription Topic Changed` | Template's preference topic updated   |

### Brands

| Event                   | Description             |
| ----------------------- | ----------------------- |
| `Brand Created`         | New brand added         |
| `Brand Updated`         | Brand settings modified |
| `Brand Published`       | Brand changes published |
| `Brand Deleted`         | Brand removed           |
| `Default Brand Updated` | Default brand changed   |

### Automations

| Event                           | Description          |
| ------------------------------- | -------------------- |
| `Automation Template Published` | Automation published |
| `Automation Template Deleted`   | Automation removed   |

### Preferences

| Event                                      | Description                             |
| ------------------------------------------ | --------------------------------------- |
| `Preferences Page Published`               | Hosted preferences page published       |
| `Preferences Notification Linked`          | Template linked to preference topic     |
| `Preferences Notification Unlinked`        | Template unlinked from preference topic |
| `Preferences Section Created`              | New preference section added            |
| `Preferences Section Deleted`              | Preference section removed              |
| `Preferences Section Channel Added`        | Channel added to section                |
| `Preferences Section Channel Removed`      | Channel removed from section            |
| `Preferences Topic Created`                | New preference topic added              |
| `Preferences Topic Deleted`                | Preference topic removed                |
| `Preferences Topic Default Status Changed` | Topic opt-in/out default updated        |

### Outbound Integrations

| Event                                                                   | Description                     |
| ----------------------------------------------------------------------- | ------------------------------- |
| `Segment Source Created/Archived/Updated/Restored`                      | Segment integration changes     |
| `Rudderstack Source Created/Archived/Enabled/Disabled/Updated/Restored` | Rudderstack integration changes |
| `Datadog Source Created/Archived/Enabled/Disabled/Updated/Restored`     | Datadog integration changes     |
| `NewRelic Source Created/Archived/Enabled/Disabled/Updated/Restored`    | NewRelic integration changes    |

## API Access

Audit trail events are accessible via the [Audit Events API](/api-reference/audit-events/get-all-audit-events). Use the API to programmatically retrieve events for external logging, SIEM integration, or custom dashboards.
