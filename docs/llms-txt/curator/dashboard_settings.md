# Source: https://docs.curator.interworks.com/embedding_using_analytics/tableau_dashboards/dashboard_settings.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.curator.interworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Dashboard Settings

> Complete guide to configuring Tableau dashboard settings in Curator including display, functionality and integration options.

When adding a Tableau Dashboard to the Curator backend, there are several tabs that offer a range of settings to
customize the integration, display, and functionality of your Dashboard. This guide will walk you through each tab
and its available options, ensuring you make the most of Curator’s features to enhance your Tableau experience.

To access these settings:

1. Navigate to the backend of the system and log in if prompted.
2. Navigate to Tableau > Dashboards.
3. Select the Dashboard for which you want to adjust the settings.

If you have not added a Dashboard yet, check out our [Adding a Dashboard Guide](/embedding_using_analytics/tableau_dashboards/adding_a_dashboard)

Below, you find detailed explanations of all the toggles, input fields, and settings within each tab:

## Tab: Dashboard

This tab contains the primary settings for adding a Tableau Dashboard to Curator. When you select a Dashboard
from the dropdown fields, the input fields below will automatically populate with the corresponding values.

* **Title**: The name of the Dashboard as it will appear in the Curator portal. It automatically picks up the
  title of your Dashboard from Tableau, but you can adjust it here if you prefer a different title. If you want
  to change titles in Curator, ensure you have the *Use Curator Dashboard Titles* toggle enabled in your Portal
  Settings (Backend > Settings > Curator > Portal Settings > Features tab > Usability section).

* **Tableau Server Dashboard URL**: The direct URL to the Dashboard on Tableau Server. No changes are needed here.
  This is useful for ensuring you are embedding the correct Dashboard - copying and pasting this into a new tab
  ensures you're certain of the Dashboard you're embedding.

* **Curator Dashboard URL "Slug"**: The ending of the URL used to access the Dashboard in Curator. You can adjust
  this as needed, but note that special characters are not supported. The full link to your Dashboard is displayed
  in the top right corner of the edit-Dashboard page.

* **Dashboard Tabs**: Determines whether or not other Dashboards published in the workbook should be shown
  and how. The display options are:

  1. **Off** - Do not show any other Dashboards from this workbook.
  2. **Styled (Web Friendly)** - Show tabs that can be styled in the Themes (Backend > Settings > Curator > Themes >
     select your Theme > *Title and Toolbar* tab). Check out our Design options [here](/site_content_design/theme/titles_and_toolbars).
  3. **Tableau Server Native** - Show tabs as they appear on Tableau Server. When using this option it is important to
     know that Tableau renders the Dashboard with the largest dimensions assigned in the workbook. This may lead to
     scroll bars within the iframe. Please refer to the [Knowledge Base article for more info](https://help.salesforce.com/s/articleView?id=001474123\&type=1).

  **Note:** This selection field is influenced by two factors:

  1. To make a selection, you need to publish your workbook with sheets as tabs.
  2. A global setting takes precedence over whether or not you can show tabs. This setting is found in Tableau
     Server Settings (Backend > Settings > Tableau > Tableau Server Settings > Workbooks section
     > **Global Dashboard Tabs** selection field).

## Tab: Discovery

This tab focuses on how the Dashboard will be discovered within the Curator portal.

* **Search & Content Discovery**: Add keywords to associate with your Dashboard. When users search for the specified
  keyword, the Dashboard will appear in the results. To add new keywords refer to [this guide](/site_content_design/content_discovery/keywords).

  If you turn on the **Hidden** switch, this Dashboard will not be discoverable through search, and it will not be
  displayed in any tiles or in the Explorer.

  The **Featured** flag adds the Dashboard to the list of featured Dashboards. This list can be used for content
  selection in Tiles, Explorer, Feed, and List elements on your pages.

* **Description**: Add context to your Dashboard. This information can be displayed in two places:

  1. **On hover over tiles**:
     * The global setting can be adjusted in Themes (Backend > Settings > Curator > Themes > select your Theme >
       Pages tab > Tiles Styles on the left-hand side > *Show Tile Description* selection field).
     * The individual setting is on the Page > Tiles Element > Tiles Settings > *Show Description*.
     * **Note:** The global setting will enable the individual setting.
  2. **In the toolbar**: Show the description when navigating to the frontend page of the Dashboard. To enable this, go to
     Backend > Settings > Curator > Portal Settings > Features tab > Toolbar Buttons
     (Curator Actions) > switch on *Dashboard Info Button*.

* **Related Content**: Associate menu items with your Dashboard. You can set how related content is displayed in
  Backend > Settings > Curator > Portal Settings > Features tab >
  Usability section > *Related Content Position* selection field.

* **New & Updated Flags**: Use the toggles to manually add a flag to the Dashboard that notifies your users.

## Tab: Display

In this tab, you can configure the visual aspects and layout of how the Dashboard will be displayed within Curator.

* **Thumbnail/Icon**: This displays the current thumbnail of your Dashboard, retrieved using Tableau's REST API
  during regular cron jobs. You can delete the current image by clicking the "x" next to the file name.
  In *Alternate Thumbnail URL*, you can specify a different URL to retrieve the thumbnail. If you want to
  refresh the thumbnail immediately, use the *Refresh Thumbnail* button. If you prefer to upload a static image,
  use the *Icon Image* file upload instead.

* **Loading Screen**: Select the loading screen to display while this Dashboard is loading. If you want to add new
  loading screens to the options, check out [this guide](/site_content_design/loading_screens/loading_screens).

* **Tutorial**: Select a tutorial to show when users navigate to the Dashboard.
  [This guide](/site_content_design/user_notifications_and_email/tutorials)
  walks you through the steps of how to create a tutorial.

* **Comments**: Enable [*User Commenting*](/embedding_using_analytics/data_manager/user_commenting)
  if you want to allow users to add comments to the Dashboard. To use this feature, you need to have Data Manager
  enabled. If you don't have Data Manager enabled yet, refer to [these steps](/embedding_using_analytics/data_manager/data_manager_basics).
  Comments are stored in the Curator database in the `interworks_datamanager_comment` table.

* **Mobile**: Point to a different Dashboard on Tableau Server for use in mobile view. *Note* that this feature is
  deprecated and will be removed in a future release.

## Tab: Filters

The Filters tab allows you to configure the filters and parameters available for users interacting with the Dashboard.

* **Filters**: Add any of the selectable Curator filters to the Dashboard. Filters that don't match any field in your
  applied data source will be greyed out.
  Check out [this guide](/embedding_using_analytics/filters_parameters/filters)
  to add new Filters.

* **Parameters**: Add any of the selectable Curator parameters to the Dashboard. Parameters that don't match any field
  in your applied data source will be greyed out.
  Check out [this guide](/embedding_using_analytics/filters_parameters/parameters)
  to add new Parameters.

* **Specify Filter Sheet**: Specify a sheet from your Dashboard to retrieve filter or parameter options if you want to
  customize Curator's default behavior. Check out
  [this documentation](/embedding_using_analytics/filters_parameters/specify_filter_sheet)
  for all the details.

* **Ignore Filter and Parameter Changes from Dashboard**: By default, Curator listens to filter and parameter changes
  made within the Dashboard and adds them to the Curator URL. This allows the Dashboard to be reloaded with the same
  filters and parameters applied without resetting them. If you prefer not to have this behavior for your Dashboard,
  turn on this switch.

## Tab: Advanced

This tab provides access to more advanced settings and customizations.

* **Data Export Options**: Configure export options for your users. If allowing CSV and/or Excel exports, you can
  either show a list of worksheets for data export or specify a worksheet for automatic download. Alternatively,
  you can specify a link for the export in the *Alternate CSV Link* field. You can also provide an *Alternate PDF
  Link* for downloading in PDF format. *Note*: You need to enable the export features in
  Backend > Settings > Curator > Portal Settings > Features Tab > Toolbar Buttons (Tableau Actions) section.

* **Report Builder**: If Report Builder is enabled, you can specify a sheet for export to presentations in the
  *Use PPTX Tab* field. You can also specify an *Alternate Report Builder Dashboard Link* to use this Dashboard
  for export instead. More details on the Report Builder feature are documented
  [here](/embedding_using_analytics/report_builder/overview_and_enabling_report_builder).

* **Menu Options**: Turn on the *Treat as a Workbook?* switch if you want all Dashboards in this workbook to be
  listed under this Dashboard's menu item. This option also enables tabs.

* **Embedded Options**: Adjust these settings to refine how your Dashboard is embedded in Curator. Your options are:
  1. **Link Target**: Override where links from within the Dashboard should load. For more information, click
     [here](https://help.salesforce.com/s/articleView?language=en_US\&id=url-actions-open-a-new-browser-tab-instead-of-the-same-tab\&type=1\&type2=1).
  2. **Show Toolbar**: Switch on if you want to show the Tableau Server toolbar below the Dashboard, in addition
     to or instead of the Curator toolbar. If enabled, you can also choose to hide the Subscribe and Alert buttons from the
     Tableau Server toolbar.
  3. **Refresh Data**: Switch on to ensure you are loading the latest data, not a cached version from Tableau Server.
     *Note*: This might significantly affect the Dashboard's loading time.
  4. **Render Client-Side**: Override the Tableau Server's configured behavior for this specific Dashboard. Check out
     [this article](https://help.tableau.com/current/server/en-us/browser_rendering.htm) for more details.

* **Miscellaneous**:
  * **Dashboard Timer**: If enabled, a small timer is displayed in a corner of the screen when accessing a Dashboard
    on the frontend.
  * **Disable URL Filter**: Filter/parameter changes will not be added to the URL and will be ignored when loading the
    Dashboard with respective parameters.

* **Custom Code**: Add your own JavaScript snippets here to customize the Dashboard experience. **Important**: We
  cannot guarantee your code will work, as we cannot test it, and we cannot offer support for Custom Code.
  Please refer to
  [this article](https://curator.interworks.com/curator-is-sunsetting-custom-code-support-what-you-should-know)
  for more information.

## Tab: Mark Commenting

In this tab, you can configure the mark commenting functionality, allowing users to leave comments on specific
marks within the Dashboard.

* **Inline Mark Commenting**: Details on Inline Mark Commenting and how to set it up can be found in
  [this documentation article](/embedding_using_analytics/data_manager/mark_commenting).

* **Tableau Group Whitelist**: Add groups from Tableau Server if you want to restrict commenting permissions to
  specific groups only.

***

If you encounter any unclear areas or mistakes, feel free to reach out to your lovely Curator team!
