# Source: https://help.aikido.dev/getting-started/task-management-systems/map-aikido-data-to-jira-custom-fields.md

# Map Aikido Data to Jira Custom Fields

#### **Why use custom field mapping:**

* **Required fields** — If your Jira issue types have required custom fields, Aikido cannot create tickets without mapping values to them
* **Richer ticket data** — Send Aikido data like severity, SLA dates, and teams directly into Jira fields
* **Jira automations** — Use mapped field values to trigger workflows, route tickets, or set priorities automatically

#### **Simple setup**

* Just enter your Jira field names exactly as they appear in Jira
* No field IDs, API lookups, or special formatting required
* Use plain text for fixed values — just the readable name

#### **Supported Jira field types:**

* Free text: `short text` `paragraph`
* Links: `URL Field`
* Selection fields: `select list (single choice)`&#x20;
* Multi-selection fields:  `select list (multiple choice)`&#x20;
* Numbers: `Number field`
* Dates: `Date Picker`
* Datetimes: `Datetime Picker`

#### Configure Field Mappings

1. Go to [**Integrations** > **Jira** > **Jira Field Mapping**](https://app.aikido.dev/settings/integrations/tasktracker/fields/custom) and click **Add Field**<br>

   <figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2F5Q61tL1tVo2tXEyd33ge%2Fimage.png?alt=media&#x26;token=bc92d764-32b1-41f2-b516-de3f300ef0a0" alt=""><figcaption></figcaption></figure>

2. Enter the Jira custom field name in the **Custom Field** input — just the name as it appears in Jira

3. Enter an Aikido shortcode (e.g., `$SEVERITY`) or a fixed text value in the **Aikido Value** input<br>

   <figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FeUKSnTq0LnrumxkV4LSP%2Fimage.png?alt=media&#x26;token=545a6aef-abe4-4a81-a385-287909485ce1" alt=""><figcaption></figcaption></figure>

4. Click **Save Changes**

The **Preview** column shows what value will be sent to Jira. These can be values based on shortcodes or fixed values / free text.

#### Aikido Value: Fixed Text vs Shortcodes

**Option 1: Send Fixed Values to Jira via free text**

Enter plain text instead of a shortcode to set a constant value. Just use the readable name — no Jira IDs or special formatting needed.

For example, entering `Security` populates that Jira field with "Security" for every ticket created from Aikido.

**Option 2: Send Aikido Values to Jira via Shortcodes**

Shortcodes are placeholders that pull data from your Aikido issues. When a Jira ticket is created, the shortcode is replaced with the actual value. You can also combine shortcodes with fixed text — for example, `Issue: $TLDR` or `Detected on $FIRST_DETECTED_DATE`. Need a shortcode that's not listed? Reach out to us.

| Shortcode              | Description                                                 |
| ---------------------- | ----------------------------------------------------------- |
| `$SEVERITY`            | Severity level (Critical, High, Medium, Low)                |
| `$ASSIGNEE`            | User assigned to handle the issue in Aikido                 |
| `$TLDR`                | Summary of the issue group                                  |
| `$TEAMS`               | Teams responsible for the related issues                    |
| `$SCOPES`              | Scopes/locations related to the task (repo, container, etc) |
| `$SLA_DATE`            | SLA due date                                                |
| `$SLA_TIME`            | SLA due date as a Unix timestamp                            |
| `$FIRST_DETECTED_DATE` | Date when the issue was first detected                      |
| `$FIRST_DETECTED_TIME` | First detected date as a Unix timestamp                     |
| `$AIKIDO_LINK`         | Link to the issue group in Aikido                           |

####

#### Date and Datetime Fields

For Jira **date** fields, use the `YYYY-MM-DD` format (e.g., `2024-03-15`) or the `_DATE` shortcodes.

For Jira **datetime** fields, use the `_TIME` shortcodes (e.g., `$SLA_TIME`, `$FIRST_DETECTED_TIME`). These output Unix timestamps, which Aikido automatically converts to Jira's required datetime format.
