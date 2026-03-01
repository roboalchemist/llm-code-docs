# Source: https://docs.curator.interworks.com/embedding_using_analytics/report_builder/overview_and_enabling_report_builder.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.curator.interworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Overview and Enabling Report Builder

> Introduction to Report Builder functionality and step-by-step instructions for enabling report generation capabilities.

The system can allow users to export one or more Dashboard snapshots as a Microsoft PowerPoint or PDF presentation.

## Optimal Tableau Connection

This functionality requires either Trusted Ticket authentication is enabled, or that you use Connected Apps. However
**Connected Apps are the most stable option**.  If you are experiencing any issues with image-retrieval and you are
using Trusted Tickets with your Tableau connection, make sure to change to Connected Apps.

## Enable Report Builder

1. Navigate to the backend of the system (e.g. `http://curatorexample.com/backend`).
2. Log in if prompted.
3. Click on **Settings** > **Curator** > **Portal Settings** in the left navigation.
4. Click on the "Features" tab at the top of the main page content.
5. Scroll down to, and expand the "Toolbar Buttons (Curator Actions)" section.
6. Click to toggle on the "Report Builder" function and click the "Save" button.

## Download one or more dashboards as a PowerPoint or PDF presentation

1. Navigate to the frontend of the system (e.g. `http://curatorexample.com`).
2. Log in if prompted.
3. Navigate to the desired Dashboard by using the navigation menu.
4. Modify the filters, etc. as desired on the Dashboard.
5. Click on the presentation icon at the top right portion of the screen. Normally this is displayed on the right side
   of the title bar in the Dashboard.
6. Click on the camera icon to take a snapshot of the current Dashboard as a presentation slide.
7. Repeat steps 3-6 as desired to create the slides that should be included in the presentation. Note: You can navigate
   to other eligible dashboards to add as slides to the same PowerPoint presentation.
8. If you need to rearrange the ordering of the slides, you can drag and drop them as needed.
9. If you need to delete all of the slides, click on the trash can icon to remove them and repeat steps 3-6 as desired
   to add the correct slides.  If you need to delete a single slide, drag and drop the slide on to the trash can icon.
10. Click on the PowerPoint button to create a PowerPoint presentation of the specified slides. Click on the PDF button
    to create a PDF presentation of the specified slides.

## Adding all Tabs from a Single Workbook

When capturing slides for your Report Builder Report, you may want to capture the entirety of a workbook that has been
embedded into Curator.  This setting can be enabled by administrators and will present an optional button in the
Report Builder modal in addition to the standard "Capture Dashboard" button.  To enable this additional button:

1. Click on **Settings** > **Curator** > **Portal Settings** in the left navigation.
2. Click on the "Report Builder" tab.
3. Click to toggle ON the "Enable Workbook Capture" button and click the "Save" button.

NOTE: When using this feature with Connected Apps, Tableau requires that the Dashboard be published with the
[Show Sheets as Tabs](https://help.tableau.com/current/pro/desktop/en-us/publish_workbooks_howto.htm#show-sheets-as-tabs)
checkbox is selected.
