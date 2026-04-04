# Source: https://docs.curator.interworks.com/embedding_using_analytics/tableau_dashboards/tableau_worksheets_and_stories.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.curator.interworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Tableau Worksheets and Stories

> Learn how to embed and configure individual Tableau worksheets and stories alongside dashboards in Curator.

In certain situations, especially if your Tableau Server's metadata API is disabled,you will be able to embed
single worksheets or stories instead of a Tableau Dashboard. Although it is technically possible it is not fully
supported as Tableau embedding API is limited in this area.

We added an informational popup to let the front end user know that, especially the toolbar buttons' functionality
is limited. If you wish to hide this information from your users you can simply disable it with the following steps:

1. Login to the backend of your Curator instance (e.g. `https://www.curatorexample.com/backend`).
2. Navigate to the **Settings** > **Tableau** > **Tableau Server Settings** section from the left-hand menu.
3. Under the "General" tab, look for the *Workbooks* section.
4. Enable the switch "Hide 'not a Dashboard' info".
5. Click the "Save" button.

The easiest workaround to avoid this situation of limited functionality is to put the worksheet on a Dashboard and
republish your workbook with visible sheets and stories.
