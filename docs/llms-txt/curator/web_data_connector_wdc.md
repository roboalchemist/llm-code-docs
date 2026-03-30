# Source: https://docs.curator.interworks.com/embedding_using_analytics/data_manager/web_data_connector_wdc.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.curator.interworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Web Data Connector (WDC)

> Integrate external data sources using Web Data Connector technology for dynamic data access in analytics platforms.

**As of Tableau Server version 2023.1, Tableau has deprecated Web Data Connector and will no longer be available**
**through Curator. Read more**
**[here](https://kb.Tableau.com/articles/Issue/web-data-connectors-deprecated-in-2023-1-release)**

The Web Data Connector allows you to connect easily to your Data Manager tables and a few usage statistics. The Data
Manager needs to be enabled only if you want to connect to your Data Manager tables.

1. Open Tableau Desktop and add a new datasource of the type **Web Data Connector** to your workbook.
2. Enter the url to your Web Data Connector, e.g. [https://www.curatorexample.com\*\*/backend/interworks/datamanager/wdc\*\*](https://www.curatorexample.com/backend/interworks/datamanager/wdc).
3. Log in with your backend administrator credentials.
4. Select the table you want to analyze in Tableau and start your analysis.

Available usage statistics are:

* Views per Dashboard
* Curator Content Views
* Curator Data Manager Groups
* Curator Favorites
* Curator Files
* Curator Keywords
* Curator Pages
* Curator Power BI Dashboards
* Curator Power BI Reports
* Curator Tableau Dashboards
* Curator Usage Log

For further usage tracking consider adding Matomo or Google Analytics as your web analytics tool to your Curator
instance as described in [this blog post](https://interworks.com/blog/morr/2018/07/26/portals-for-tableau-new-feature-spotlight-on-premises-analytics-tracking/).

## Refreshing WDC Extracts

Connecting to a [Tableau Web Data Connector](https://help.tableau.com/current/pro/desktop/en-us/examples_web_data_connector.htm)
creates an extract of the data's state at a specific point in time. Yet, you might want to do a continuous and automated
analysis of your Curator's usage.
Publish the data source on Tableau Server where you can run scheduled refreshes of the extract. For security reasons,
you need to add your Curator's WDC to Tableau Server's safe list by running the following command on tsm:

```bash  theme={null}
tsm data-access web-data-connectors add --name "Curator WDC" --url https://[your-curator-url-here]:443/wdc --secondary https://fonts.googleapis.com/.*,https://use.typekit.net/.*,https://[your-curator-url-here]/.*,https://connectors.tableau.com/.*
```

The above command allows Tableau Server to connect to the WDC and the asset domains used by the WDC. Tableau explains
[further details in their documentation](https://help.tableau.com/current/server/en-us/datasource_wdc.htm). To make the
above change effective **Tableau Server needs a restart**.
