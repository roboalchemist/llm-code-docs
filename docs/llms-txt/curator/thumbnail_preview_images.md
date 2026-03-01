# Source: https://docs.curator.interworks.com/site_content_design/content_discovery/thumbnail_preview_images.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.curator.interworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Thumbnail Preview Images

> Set up thumbnail and preview images for content to enhance visual discovery and user engagement.

When viewing a list of dashboards, Curator has the ability to display a custom preview of the Tableau Server view as a
thumbnail image.

These thumbnails can either be set manually while creating or
[editing a Dashboard](/site_content_design/pages/pages_overview) or the system will attempt to automatically grab the
thumbnail from the Tableau Server if the Dashboard is created without one.

Once the Dashboard is created you can manually refresh the thumbnail by pressing the Refresh Thumbnail button.

***To refresh the dashboards thumbnail:***

1. Login to the backend of your Curator instance (e.g. `http://curatorexample.com/backend`).
2. Navigate to the **Tableau** > **Dashboards** section from the left-hand menu.
3. Click on the "New Dashboard" button or select an existing Dashboard.
4. In the Misc tab, expand the Look/Feel section and click the "Refresh Thumbnail" button.

You can manually upload a thumbnail on the Dashboard edit page.

***To manually upload a thumbnail:***

1. Login to the backend of your Curator instance (e.g. `http://curatorexample.com/backend`).
2. Navigate to the **Tableau** > **Dashboards** section from the left-hand menu.
3. Click on the "New Dashboard" button or select an existing Dashboard.
4. In the **Misc** tab, expand the Look/Feel section and use the Thumbnail Image form to upload your custom image.
   *Note: You will need to click the "X" in the bottom-right corner to remove an existing image.*

***To set a global default thumbnail:***

1. Login to the backend of your Curator instance (e.g. `http://curatorexample.com/backend`).
2. Navigate to the **Settings** > **Curator** > **Portal Settings** section from the left-hand menu.
3. Click on the **Home** tab and expand the Tile Type section.
4. Use the "Custom Default Thumbnail" form to upload your custom image.
   *Note: You will need to click the "X" in the bottom-right corner to remove an existing image.*
5. If you wish to use this image for *all* dashboards, disable *Refresh Dashboard Thumbnails* under **Settings** >
   **Curator** > **Portal Settings** > **Features** tab.

Curator also has a feature to enable nightly refreshes of the site's Dashboard thumbnails. This helps to keep the thumbnail
up to date with any changes while also saving time from manually updating every Dashboard thumbnail.

***Enabling or Disabling Refresh Dashboard Thumbnails:***

1. Login to the backend of your Curator instance (e.g. `http://curatorexample.com/backend`).
2. Navigate to the **Settings** > **Curator** > **Portal Settings** section from the left-hand menu.
3. Click on the **Features** tab at the top of the main page content.
4. Toggle the switch to enable/disable *Refresh Dashboard Thumbnails* setting under the Functionality section and click
   the "Save" button.
