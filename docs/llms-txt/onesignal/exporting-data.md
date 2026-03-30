# Source: https://documentation.onesignal.com/docs/en/exporting-data.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Exporting data

> Learn how to export user, message, and outcome data from the OneSignal dashboard and API, including CSV delivery reports, subscription data, and per-user message event activity.

## Overview

You can export data from OneSignal in several ways depending on your use case. This includes dashboard CSV exports, API endpoints, and real-time data streaming integrations. This guide covers how to export:

* Message and delivery data
* Audience activity per message
* Subscription and user profile data
* Email message delivery reports
* Alternative programmatic methods via API or Event Streams

***

## Data retention

Messages sent via our dashboard **Messages** form are accessible for the lifetime of the app.

Messages sent via our API and Audience Activity are only accessible for around 30 days from when they were created.

Journeys-sent messages are downloadable from the dashboard. See [Journey analytics](./journeys-analytics) for more details.

***

## Export methods

<Columns cols={2}>
  <Card title="Event Streams" href="./event-streams" arrow={true}>
    Send message events like sents, opens, clicks, and more to your chosen destination.
  </Card>

  <Card title="View Messages API" href="/reference/view-messages" arrow={true}>
    Retrieve message reports in JSON format including delivery and performance stats.
  </Card>

  <Card title="Journey Analytics" href="./journeys-analytics" arrow={true}>
    Track performance for messages sent via Journeys and download reports.
  </Card>

  <Card title="Template Analytics" href="./template-analytics" arrow={true}>
    Export performance data for reusable templates.
  </Card>

  <Card title="Integrations" href="./integrations" arrow={true}>
    Export data into third-party tools like Segment, Mixpanel, or Google BigQuery.
  </Card>

  <Card title="Dashboard exports">
    Export data from the dashboard in CSV format.
  </Card>
</Columns>

***

## Export message data

<Tabs>
  <Tab title="Dashboard">
    You can export individual push, in-app, email, SMS, and Live Activity message data when viewing the message within the dashboard.

    * [Push message reports](./push-notification-message-reports)
    * [In-app message reports](./in-app-message-reports)
    * [Email message reports](./email-message-reports)
    * [SMS message reports](./sms-message-reports)
    * [Live Activity message reports](./live-activities#message-reports)

    You can bulk export push, email, SMS and Live Activity messages from the **Delivery > Sent Messages** page.

    Available filters:

    * Source: Dashboard, API, Automated, or Test Messages
    * Device Type: Push, In-App, Email, SMS, or Live Activity
    * Text Search: Search by message Content, Heading and name. **Currently only available with Source: Dashboard Messages**.
    * Start Date & End Date: Select a start date and end date to filter messages by. Filters based on "Sent At" date based on your current timezone.

    <Frame caption="Messages table export">
      <img src="https://mintcdn.com/onesignal/ciRrThfP6xMpI7GY/images/dashboard/export-messages.png?fit=max&auto=format&n=ciRrThfP6xMpI7GY&q=85&s=2b0e2421bd05ce8783064fab3a895786" style={{ width:"100%" }} width="2352" height="1336" data-path="images/dashboard/export-messages.png" />
    </Frame>
  </Tab>

  <Tab title="API">
    You can export message data via our REST API using the following endpoints:

    * [View message](/reference/view-message): Fetch data for a single message using its `id`.
    * [View messages](/reference/view-messages): Retrieve a paginated list (up to 50 per page).
    * [Export audience activity CSV](/reference/export-csv-of-events): Per-user event CSV including sent, open, click data.
    * [Message history](/reference/message-history): Limited to `sent` and `clicked` events within a 7-day window.
  </Tab>
</Tabs>

***

## Export user and subscription data

<Tabs>
  <Tab title="Dashboard">
    1. Go to **Audience > Subscriptions**.
    2. Optionally filter by Segment.
    3. Ensure all desired columns are visible.
    4. Click **Export**.

    <Frame caption="Subscriptions table export">
            <img src="https://mintcdn.com/onesignal/ciRrThfP6xMpI7GY/images/dashboard/export-subscriptions.png?fit=max&auto=format&n=ciRrThfP6xMpI7GY&q=85&s=7ca55f32c2cb298b7edef9f546545a14" alt="" width="2384" height="1604" data-path="images/dashboard/export-subscriptions.png" />
    </Frame>
  </Tab>

  <Tab title="API">
    You can export user and subscription data via our REST API using the following endpoints:

    * [CSV export](/reference/csv-export): Provides a download link to a CSV file of all user data.
    * [View user](/reference/view-user): Retrieve the current state of a user, identified by the `alias_label` and `alias_id`.
  </Tab>
</Tabs>

***

Built with [Mintlify](https://mintlify.com).
