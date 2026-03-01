# Source: https://docs.curator.interworks.com/embedding_using_analytics/report_builder/scheduled_reports.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.curator.interworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Scheduled Reports

> Configure automated report generation and distribution on recurring schedules for consistent business intelligence delivery.

The Scheduled Reports feature allows you to set a report to be sent out via email on a recurring schedule. This feature
requires that the
[Report Builder](/embedding_using_analytics/report_builder/overview_and_enabling_report_builder)
and
[Report Builder: Email Option](/embedding_using_analytics/report_builder/email_option)
both be turned on.

As of the 2024.09-02 release, [Scheduled Reports](/embedding_using_analytics/report_builder/email_option)
now have an unsubscribe option.  Recipients who receive the email can remove themselves from the distribution list -
unless they are the only recipient, in which case the report needs to be deleted to cease distribution via the schedule.

## Setup

### To enable the Scheduled Reports Option

1. Navigate to the backend of the system (e.g. `https://www.curatorexample.com/backend`).
2. Log in if prompted.
3. Click on **Settings** > **Curator** > **Portal Settings** in the left navigation.
4. Click on the "Features" tab at the top of the main page content.
5. Click to switch on the "Scheduled Reports Option" setting under the "Toolbar Buttons (Curator Actions)" section and
   click the "Save" button.

### To configure the default bcc, subject, and body

1. Navigate to the backend of the system (e.g. `https://www.curatorexample.com/backend`).
2. Log in if prompted.
3. Click on **Settings** > **Curator** > **Portal Settings** in the left navigation.
4. Click on the "[Report Builder](/embedding_using_analytics/report_builder/overview_and_enabling_report_builder)"
   tab at the top of the main page content.
5. Scroll down and expand the
   "[Report Builder Email Settings](/embedding_using_analytics/report_builder/email_option)"
   section.
6. Fill out the "Email BCC Addresses", "Email subject", or "Email body" files as desired, under the
   "[Report Builder Email Settings](/embedding_using_analytics/report_builder/email_option)"
   section and click the "Save" button.

### To send a scheduled report with the built report

1. Navigate to the backend of the system (e.g. `https://www.curatorexample.com/backend`).
2. Log in if prompted.
3. Navigate to the desired Dashboard by using the navigation menu.
4. Generate the images you want to use for your report.
5. Click on the presentation icon at the top right portion of the screen. Normally this is displayed on the right side
   of the title bar in the Dashboard.
6. Click on the Schedule button to "Schedule recurring report email".
7. Click on the "New Scheduled Report" button
8. Fill out the Email Address(es) field with the desired recipients. You can enter multiple email addresses by using
   commas to separate them.
9. If you have the correct permissions you can edit the subject and body.
10. Select the Recurring Schedule time frame you want your report sent out on.
11. Click the send button when finished.

## Existing Scheduled Reports

### Backend overview

1. Once Scheduled Reports are setup, navigate to the backend of the system (e.g. `https://www.curatorexample.com/backend`).
2. Log in if prompted.
3. Click on **Tableau** > **Scheduled Reports** in the left navigation.

In this view, you can see all existing Scheduled Reports and status information like ***last sent*** and
***is active?***. By using the checkboxes on the left side, you can select which Scheduled Reports you want to send out
immediately.
You can also create a new Scheduled Report by clicking on ***New Scheduled Report***.
By clicking on a specific Scheduled Report you enter Edit Mode. You can edit details of your Scheduled Report, change
the schedule, change the status and trigger sending out the report. You can also delete the Scheduled Report.

### Clone Scheduled Reports (2023.10-03)

To duplicate a scheduled report, this can be done on the backend of Curator by system administrators.  To clone a
report, simply visit the edit-report page, and click the "Clone" button in the top-right corner of the page.  This will
display a "Clone Report" page where you can change the title and create your new report.

### Frontend overview (available in release 2023.02.22)

If you want to give users an overview of their existing Scheduled Reports, follow the steps below:

1. Navigate to the backend of the system (e.g. `https://www.curatorexample.com/backend`).
2. Log in if prompted.
3. Click on **Settings** > **Curator** > **Portal Settings** in the left navigation.
4. Navigate to the **Features** tab > open the **Toolbar Buttons (Curator Actions)** section.
5. Enable **Manage my Scheduled Reports - Page**

As a frontend user:

1. Navigate to the frontend of the system (e.g. [https://www.curatorexample.com](https://www.curatorexample.com)).
2. Open the user menu in the top right corner by clicking on your username.
3. Click on **My Scheduled Reports**.

In this view, you can see all your existing Scheduled Reports and information like ***schedule***, ***timezone*** and
***is active?***.
By clicking on the pencil icon of a specific Scheduled Report you enter Edit Mode. You can edit details of your
Scheduled Report, change the schedule, change the status and trigger sending out the report.
By clicking on the bin icon, you delete the specific Scheduled Report.
