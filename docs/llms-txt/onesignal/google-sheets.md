# Source: https://documentation.onesignal.com/docs/en/google-sheets.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Google Sheets

> Sync custom events from Google Sheets to OneSignal to trigger automated Journeys and personalized messaging campaigns based on user behavior.

export const PLATFORM_0 = "Google Sheets"

export const DATA_TYPE_0 = "columns"

export const COLUMN_HEADER_0 = "Sheets Column Examples"

export const PROPERTIES_DESCRIPTION_0 = "Multiple columns combined into JSON"

## Overview

The OneSignal + Google Sheets integration enables automatic syncing of custom events from your Google Sheets to OneSignal. This allows you to trigger automated Journeys and personalized messaging campaigns based on user behavioral data stored in your spreadsheets, perfect for teams that manage event data collaboratively.

***

## Requirements

* Access to [Event Streams](/docs/en/event-streams) for outbound message events (Plan limitations and overages apply)
* Access to [Custom Events](/docs/en/custom-events) for inbound event syncing (Plan limitations and overages apply)
* [Updated Account Plan](https://onesignal.com/pricing) (not available on free apps)

### Google Sheets

* **Google Account** with access to the sheet containing event data
* **Event spreadsheet** with proper column structure for event data
* **Sheet sharing permissions** for OneSignal to access the data
* **Consistent data format** in your event tracking sheet

***

## Setup

<Steps>
  <Step title="Prepare your event data sheet">
    Structure your Google Sheet with the required columns for event data:

    **Required columns:**

    * `event_name` or `event_type`: The name of the event (String)
    * `user_id` or `email`: User identifier (String)
    * `timestamp` or `created_at`: Event timestamp (Date/DateTime)
    * `properties`: Event properties as JSON or separate columns (Optional)

    **Example sheet structure:**

    ```
    | event_name | user_id | timestamp           | product_id | amount |
    |------------|---------|---------------------|------------|--------|
    | purchase   | user123 | 2024-01-15 10:30:00 | prod_abc   | 29.99  |
    | signup     | user456 | 2024-01-15 11:45:00 |            |        |
    ```
  </Step>

  <Step title="Configure sheet permissions">
    Share your Google Sheet with OneSignal's service account:

    1. Open your Google Sheet
    2. Click **Share** button in the top right
    3. Add OneSignal's service account email (provided during setup)
    4. Set permissions to **Viewer** (read-only access)
    5. Click **Send** to grant access

    <Info>
      OneSignal will provide the specific service account email during the integration setup process.
    </Info>
  </Step>

  <Step title="Add integration in OneSignal">
    In OneSignal, go to **Data > Integrations** and click **Add Integration**.

    Select **Google Sheets** and provide:

    * **Sheet URL**: The full URL of your Google Sheet
    * **Sheet Name**: The specific tab/sheet name containing event data
    * **Header Row**: Row number containing column headers (usually 1)
    * **Data Range**: Cell range containing your event data (e.g., `A2:F1000`)
  </Step>

  <Step title="Configure column mapping">
    Map your Google Sheets columns to OneSignal event fields:

    * **Event Name Column**: Select the column containing event names
    * **User ID Column**: Select the column with user identifiers
    * **Timestamp Column**: Select the column with event timestamps
    * **Properties Columns**: Select additional columns to include as event properties

    <Info>
      You can map multiple columns as event properties. OneSignal will combine them into a single event payload.
    </Info>
  </Step>

  <Step title="Set sync schedule">
    Configure how often OneSignal should check for new event data:

    * **Sync Frequency**: Choose from 15 minutes, hourly, or daily
    * **Incremental Sync**: Enable to only sync new rows since last update
    * **Timestamp Filter**: Only sync events within a specific time range

    <Warning>
      Google Sheets has API rate limits. More frequent syncing may be throttled for sheets with large datasets.
    </Warning>
  </Step>

  <Step title="Test the connection">
    Click **Test Connection** to verify OneSignal can access your Google Sheet and read the event data correctly.
  </Step>
</Steps>

***

### Event data mapping

Map your {PLATFORM_0} {DATA_TYPE_0} to OneSignal's custom events format:

| OneSignal Field | {COLUMN_HEADER_0} | Description                | Required |
| --------------- | ----------------- | -------------------------- | -------- |
| `name`          | `event_name`      | Event identifier           | Yes      |
| `external_id`   | `user_id`         | User identifier            | Yes      |
| `timestamp`     | `event_timestamp` | When event occurred        | No       |
| `properties`    | `event_data`      | {PROPERTIES_DESCRIPTION_0} | No       |

***

## Advanced Configuration

### Incremental Sync Setup

Configure incremental syncing to only process new events:

1. **Timestamp Column**: Ensure your sheet has a consistent timestamp column
2. **Sort Order**: Keep events sorted by timestamp (newest last)
3. **Append-Only**: Add new events to the bottom of your sheet
4. **Avoid Edits**: Don't modify historical event rows after they're synced

### Data Validation

Implement data validation in your Google Sheet:

```
Data > Data validation
- Event Name: List from range (predefined event types)
- User ID: Custom formula to check format
- Timestamp: Date/Time format validation
- Amount: Number validation for numeric properties
```

### Collaborative Workflows

Best practices for team collaboration:

* **Named Ranges**: Use named ranges for event data sections
* **Protected Ranges**: Protect header rows from accidental changes
* **Comments**: Add comments to explain event definitions
* **Version History**: Use Google Sheets' version history for tracking changes
* **Access Controls**: Limit edit access to data entry team members

### Performance Optimization

Optimize for large datasets:

* **Sheet Limits**: Keep individual sheets under 10,000 rows for best performance
* **Multiple Sheets**: Use separate sheets for different event types
* **Data Archival**: Archive old data to separate sheets monthly
* **Formulas**: Minimize complex formulas in event data ranges

<Warning>
  Google Sheets performs best with under 50,000 total cells. For high-volume event tracking, consider using a database source instead.
</Warning>

***

## FAQ

### How often does OneSignal sync events from Google Sheets?

OneSignal can sync as frequently as every 15 minutes, but we recommend hourly or daily syncing for most use cases to respect Google's API limits.

### Can multiple team members add events to the same sheet?

Yes, Google Sheets supports real-time collaboration. However, ensure team members understand the required data format and column structure.

### What happens if someone edits historical event data?

OneSignal syncs based on timestamps and row positions. Editing historical data may cause duplicate events or data inconsistencies. We recommend append-only workflows.

Built with [Mintlify](https://mintlify.com).
