# Audit Logs

The Audit Logs feature provides a searchable and filterable display of all activities performed by users of the Strapi application.

</IdentityCard>

## Usage

**Path to use the feature:**  Settings > Administration Panel - Audit Logs

The Audit Logs feature logs the following events:

| Event | Actions |
| --- | --- |
| Content Type | `create`, `update`, `delete` |
| Entry (draft/publish) | `create`, `update`, `delete`, `publish`, `unpublish` |
| Media | `create`, `update`, `delete` |
| Login / Logout | `success`, `fail` |
| Role / Permission | `create`, `update`, `delete` |
| User | `create`, `update`, `delete` |

For each log item, the following information is displayed:

- Action: type of action performed by the user (e.g.`create` or `update`).
- Date: date and time of the action.
- User: user who performed the action.
- Details: displays a modal with more details about the action (e.g. the User IP address, the request body, or the response body).

### Filtering logs

By default, all logs are displayed in reverse chronological order. You can filter the logs by:

- Action: select the type of action to filter by (e.g `create` or `update`).
- User: select the user to filter by.
- Date: select a date (range) and time to filter by.

### Accessing log details {#log-details}

For any log item, click the  icon to access a modal with more details about that action. In the modal, the *Payload* section displays the details in an interactive JSON component, enabling you to expand and collapse the JSON object.