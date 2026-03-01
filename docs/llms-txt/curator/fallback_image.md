# Source: https://docs.curator.interworks.com/embedding_using_analytics/report_builder/fallback_image.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.curator.interworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Fallback Image

> Configure fallback images for reports when live dashboard content cannot be rendered or is unavailable.

There may be occasional issues when generating reports using Curator's Scheduled Reports.  This can be for a variety of
reasons, such as bad Tableau Server configuration, networking interruptions, permission changes, or dashboards getting
moved/deleted.  To handle these scenarios, the majority of them are fixed by simply having your user log back in to
Curator, and re-create the slide.  See the steps below on how to update the existing "Fallback Image" if you'd like to
customize this for your users.

## Updating the Fallback Image

Before you proceed below, you need to upload your file using the [File](/site_content_design/files/files)
system in Curator.

1. Login to the backend of your Curator instance (e.g. `http://curatorexample.com/backend`).
2. Navigate to the **Settings** > **Curator** > **Portal Settings** section from the left-hand menu.
3. Click on the "Report Builder" tab at the top of the main page content.
4. Expand the "Report Builder E-Mail Settings" and update the Fallback Image.
5. Click the save button.
