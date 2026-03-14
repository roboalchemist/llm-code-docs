# Source: https://fivetran.com/docs/getting-started/glossary

Title: Glossary | Definitions of Fivetran terms

URL Source: https://fivetran.com/docs/getting-started/glossary

Markdown Content:
Some common terms have specific meanings in the context of Fivetran documentation.

* * *

Account[](https://fivetran.com/docs/getting-started/glossary#account)
---------------------------------------------------------------------

When we talk about your account, we mean your Fivetran account. You can manage your account using your Fivetran dashboard. When we need to talk about a source or destination account, we call it out by name (for example, your Jira account or your BigQuery account). See also [**Fivetran dashboard**](https://fivetran.com/docs/getting-started/glossary#fivetrandashboard).

Alert[](https://fivetran.com/docs/getting-started/glossary#alert)
-----------------------------------------------------------------

Alerts appear on your Fivetran dashboard to give you important information about your Fivetran account. There are two types of alerts: errors and warnings. Errors inform you about actions you must take to fix your connections or transformations. Warnings inform you that something is wrong but is not disrupting your syncs. See also [**error**](https://fivetran.com/docs/getting-started/glossary#error) and [**warning**](https://fivetran.com/docs/getting-started/glossary#warning).

Connection[](https://fivetran.com/docs/getting-started/glossary#connection)
---------------------------------------------------------------------------

A connection is a data pipeline that replicates data from your source to your destination. For example, a MySQL connection moves your data from your MySQL database to your destination.

Connector[](https://fivetran.com/docs/getting-started/glossary#connector)
-------------------------------------------------------------------------

Connectors let you create connections between sources and destinations. Think of connectors as pre-built components that you use to create individual connections. For example, you might use the Salesforce connector to create a connection to replicate data from Salesforce to your Snowflake data warehouse.

Sometimes, you might create multiple connections based on the same Fivetran connector. For example, you might want to replicate data from two different PostgreSQL databases to your destination and so create two separate connections using the PostgreSQL connector. You can also create more than one connection from a single source. Fivetran offers connectors for hundreds of sources and destinations.

Core tables[](https://fivetran.com/docs/getting-started/glossary#coretables)
----------------------------------------------------------------------------

Fivetran identifies core tables in the source that must be included in the sync to ensure data accuracy. Each Fivetran connector has a different sync strategy that determines the tables that are required. These core tables fetch elementary data from the source that is essential for the connector's efficient functioning. You cannot deselect or [block](https://fivetran.com/docs/using-fivetran/features#datablocking) core tables from your connection's **Schema** tab.

Cursor[](https://fivetran.com/docs/getting-started/glossary#cursor)
-------------------------------------------------------------------

The cursor is the marker that lets us know where the last Fivetran sync left off in your source data. When we start the next sync, we use the cursor to decide where to begin syncing again. Think of the cursor as a metaphorical high-water mark that shows where our sync got to.

The cursor takes different forms depending on the source. For example, in Salesforce, it refers to the last updated timestamp on a particular endpoint, and in PostgreSQL, it refers to an entry in the database's Write-ahead Logs.

Destination[](https://fivetran.com/docs/getting-started/glossary#destination)
-----------------------------------------------------------------------------

Fivetran connectors replicate your source data to a destination system. Fivetran supports the following destination types:

*   cloud data warehouses
*   databases
*   online data platforms
*   data lakes

You can have multiple destinations in your Fivetran account. All connections and transformations are assigned to a particular destination. Each destination is mapped on a 1:1 basis to its [group](https://fivetran.com/docs/getting-started/glossary#group), which is used for user management within the destination. This also means that a destination and its group have the same ID. When you create and manage destinations in your [Fivetran dashboard](https://fivetran.com/docs/getting-started/glossary#fivetrandashboard), we automatically manage the associated group. When you create and manage destinations using our [REST API](https://fivetran.com/docs/rest-api), you manage connections and transformations using our [Destination Management REST API resource](https://fivetran.com/docs/rest-api/api-reference/destinations) destination, and users - using our [Group Management REST API resource](https://fivetran.com/docs/rest-api/api-reference/groups).

Learn more about our [supported destinations](https://fivetran.com/docs/destinations#destinations).

Error[](https://fivetran.com/docs/getting-started/glossary#error)
-----------------------------------------------------------------

An error is a type of alert in your Fivetran dashboard that tells you about an action you must take to fix your connections or transformations. We also generate a notification email to let you know about the error. Fivetran creates an error when the problem with your connection or transformation is caused by something that’s on your side. For example, if you have set insufficient permissions in your source and Fivetran can’t sync your data, we generate an error that tells you about the problem and what permissions you must set. See also [**alert**](https://fivetran.com/docs/getting-started/glossary#alert) and [**warning**](https://fivetran.com/docs/getting-started/glossary#warning).

Fivetran data models[](https://fivetran.com/docs/getting-started/glossary#fivetrandatamodels)
---------------------------------------------------------------------------------------------

[Fivetran data models](https://fivetran.com/docs/transformations/data-models) are pre-built, open-source SQL statements provided by Fivetran and used to transform your raw data. These models are designed to simplify and accelerate the transformation of raw data into an analytics-ready format by leveraging the source data schemas of Fivetran connectors. You can import Fivetran data models into your dbt project and execute them like any other dbt project. See also [Transformation](https://fivetran.com/docs/getting-started/glossary#transformation) and [Quickstart data models](https://fivetran.com/docs/getting-started/glossary#quickstartdatamodels).

Fivetran dashboard[](https://fivetran.com/docs/getting-started/glossary#fivetrandashboard)
------------------------------------------------------------------------------------------

Your [Fivetran dashboard](https://fivetran.com/dashboard/) is the web-based control center for your Fivetran account. Your dashboard provides a comprehensive overview of your account details, including all your connections and billing information. From your dashboard, you can create and edit connections, manage your destination, add transformations, add and delete users, review logs, view alerts, and much more. The best way to learn about the dashboard is to explore it yourself. Your view of the dashboard varies depending on your user permissions. Navigate to [https://fivetran.com/dashboard/](https://fivetran.com/dashboard/) in any browser and log in to your Fivetran account to access your Fivetran dashboard.

Group[](https://fivetran.com/docs/getting-started/glossary#group)
-----------------------------------------------------------------

A group maps users to the [destination](https://fivetran.com/docs/getting-started/glossary#destination). Each group is mapped on a 1:1 basis to its destination. This also means that a destination and its group have the same ID. When you create and manage destinations in your [Fivetran dashboard](https://fivetran.com/docs/getting-started/glossary#fivetrandashboard), we automatically manage the associated group. When you create and manage destinations using our [REST API](https://fivetran.com/docs/rest-api), you manage connections and transformations using our [Destination Management REST API resource](https://fivetran.com/docs/rest-api/api-reference/destinations) destination, and users - using our [Group Management REST API resource](https://fivetran.com/docs/rest-api/api-reference/groups).

Historical sync[](https://fivetran.com/docs/getting-started/glossary#historicalsync)
------------------------------------------------------------------------------------

During a historical sync, Fivetran connects to your source and copies the entire contents of every table that you’ve selected to sync. Historical syncs include all your selected data, including data that is old. How long the historical sync takes depends on the amount of data and the limitations of your source. For example, some sources only allow a limited number of API calls.

A connection's first-ever historical sync is called an [initial sync](https://fivetran.com/docs/getting-started/glossary#initialsync). See also [sync](https://fivetran.com/docs/getting-started/glossary#sync).

### Historical sync time frame[](https://fivetran.com/docs/getting-started/glossary#historicalsynctimeframe)

Some connectors allow you to specify the total time range of historical data you want to sync during historical syncs. This time range is called the historical sync time frame. The time frame varies by connector. Some connectors support modifying the time frame even after a connection has been set up, while others do not.

Expand to see which connectors support the historical sync time frame option, but do not support modifying it after a connection has been set up.
*   Adobe Analytics
*   Adroll
*   Apple App Store
*   Apple Search Ads
*   Criteo
*   Eloqua
*   Facebook Ads
*   Google Ad Manager
*   Google Ads
*   Google Analytics 4
*   Google Campaign Manager 360
*   Google Display & Video 360
*   Google Search Ads 360
*   Google Search Console
*   Instagram Business
*   Klaviyo
*   LinkedIn Company Pages
*   Marketo
*   Microsoft Advertising
*   Outbrain
*   Pardot
*   Pinterest Ads
*   Sailthru
*   Snapchat Ads
*   Taboola
*   The Trade Desk
*   TikTok Ads
*   Twitter Ads
*   Twitter Organic
*   Yahoo DSP

Expand to see which connectors support the historical sync time frame option, as well as modifying it after a connection has been set up.
*   Amazon Selling Partner
*   Google Ads
*   Google Ad Manager
*   Google Analytics 4
*   Google Campaign Manager 360
*   Google Display & Video 360
*   Google Search Ads 360
*   Google Search Console
*   HubSpot
*   Klaviyo
*   Marketo
*   Mixpanel
*   Pardot
*   ServiceNow
*   SFMC
*   Shopify
*   Stripe
*   Zendesk Support

History mode[](https://fivetran.com/docs/getting-started/glossary#historymode)
------------------------------------------------------------------------------

History mode is a sync mode that Fivetran uses to track history. In this mode, we record every version of each record in the source table to the corresponding table in your destination.

Depending on the connector, Fivetran uses different approaches to retain historical data:

*   For connectors where Fivetran defines the schema, we track history for a predefined connector-specific set of tables. We select those tables based on the analytical value of their historical data. For these connectors, you cannot change which tables track history.
*   For connectors where Fivetran just replicates the schema, we give you the option to select which tables track history. For these connectors, you can switch any supported table to history mode to track its history.

Read more about [history mode](https://fivetran.com/docs/core-concepts/sync-modes/history-mode).

Incremental sync[](https://fivetran.com/docs/getting-started/glossary#incrementalsync)
--------------------------------------------------------------------------------------

Incremental sync is also known as **incremental update**.

Incremental syncs update only new or modified data. Fivetran connectors sync most tables using incremental updates. We use a variety of mechanisms to capture the changes in the source data, depending on how the source provides change data. During incremental syncs, Fivetran maintains an internal set of progress cursors, which let us track the exact point where our last successful sync left off. Incremental syncs are efficient because they update only the changed data, instead of re-importing whole tables. See also [sync](https://fivetran.com/docs/getting-started/glossary#sync).

Initial sync[](https://fivetran.com/docs/getting-started/glossary#initialsync)
------------------------------------------------------------------------------

An initial sync is a connection's first-ever [historical sync](https://fivetran.com/docs/getting-started/glossary#historicalsync). When you first create a connection and sync the historical data in your source, we don’t charge you for the historical data. However, the incremental data may count towards paid MAR, depending on the scenario.

If you choose to [block or hash columns](https://fivetran.com/docs/using-fivetran/features/data-blocking-column-hashing) before running the initial sync for your new connection, we query your data source and cache your data while we fetch the full schema. We write to the destination only the data you selected as tables and columns from the fully fetched schema and only when you approved the selection.

Lite connector[](https://fivetran.com/docs/getting-started/glossary#liteconnector)
----------------------------------------------------------------------------------

A Fivetran [Lite connector](https://fivetran.com/docs/connectors/applications/lite-connectors) is a type of connector built for specific use cases with an accelerated development cycle.

Monthly model runs[](https://fivetran.com/docs/getting-started/glossary#monthlymodelruns)
-----------------------------------------------------------------------------------------

Monthly model runs is the metric we use to measure data transformation activity and usage levels. It is the total number of models successfully executed as part of your transformation jobs in a given month. This includes any upstream and intermediate models before the final output model.

Normalize[](https://fivetran.com/docs/getting-started/glossary#normalize)
-------------------------------------------------------------------------

When Fivetran normalizes data, we organize the data into tables and columns in a way that reduces data redundancy and stores it logically. Normalization divides larger tables into smaller tables and links them using relationships, according to specific rules.

Quickstart data models[](https://fivetran.com/docs/getting-started/glossary#quickstartdatamodels)
-------------------------------------------------------------------------------------------------

[Quickstart data models](https://fivetran.com/docs/transformations/quickstart) is a no-code implementation of [Fivetran data models](https://fivetran.com/docs/getting-started/glossary#fivetrandatamodels). It allows you to use the data models without needing to manually write or edit code. See also [Transformation](https://fivetran.com/docs/getting-started/glossary#transformation).

Re-sync[](https://fivetran.com/docs/getting-started/glossary#resync)
--------------------------------------------------------------------

A full re-sync completely overwrites the data in your destination with new data from your source. A table re-sync lets you overwrite the data in a specific table so that you can fix data integrity issues in selected tables without re-syncing the entire connection. Normally, Fivetran uses incremental updates to sync data from your source to your destination, so we only sync data that has changed. However, sometimes discrepancies occur between the data in your destination and your source. Then you need to overwrite existing data in your destination to make it consistent with the source, and a re-sync lets you do that. Read more about our [re-sync feature](https://fivetran.com/docs/using-fivetran/features#resync). See also [sync](https://fivetran.com/docs/getting-started/glossary#sync) and [**incremental sync**](https://fivetran.com/docs/getting-started/glossary#incrementalsync).

Re-import[](https://fivetran.com/docs/getting-started/glossary#reimport)
------------------------------------------------------------------------

If we cannot sync a table [incrementally](https://fivetran.com/docs/getting-started/glossary#incrementalsync) (for example, due to a missing corresponding incremental endpoint), we must sync it in full during every sync. We call this operation a re-import. Re-import tables [incur more MAR](https://fivetran.com/docs/usage-based-pricing#reimporttables) than incremental tables.

When we know a re-import table is slow or problematic, we flag that table as Not Recommended on your connection's [**Schema** tab](https://fivetran.com/docs/using-fivetran/fivetran-dashboard/connectors/schema). Some connectors with many re-import tables, like NetSuite SuiteAnalytics, have a special logic to only sync re-import tables once a day or once a week.

Rollback sync[](https://fivetran.com/docs/getting-started/glossary#rollbacksync)
--------------------------------------------------------------------------------

A rollback sync is a sync that automatically runs once a day. It captures the changes that happen outside the incremental sync time frame, including metrics that may have been revised after your last sync. Revision is common practice for many applications that generate reports. See also [sync](https://fivetran.com/docs/getting-started/glossary#sync).

The rollback window is how many days' worth of data we request in each sync. For example, with a rollback window of 30 days, the connection syncs all data from the past 30 days. Some connectors have default rollback windows; others allow you to customize your rollback window within a certain range (for example, between 2 and 90 days). To ensure data integrity, we align our rollback windows with the time frame in which each source application revises its data.

Schema[](https://fivetran.com/docs/getting-started/glossary#schema)
-------------------------------------------------------------------

A database schema defines how the data is organized in a database. It contains the different tables, their fields, and the relationship between tables. When you create a new Fivetran connection, you choose the name that the schema will have and Fivetran creates it in your destination.For most sources, each connection results in one schema in your destination. Database sources are the exception because a single database connection can replicate multiple schemas. Read more about how [database connectors handle multiple source schemas](https://fivetran.com/docs/connectors/databases#schemasandtables).

Source[](https://fivetran.com/docs/getting-started/glossary#source)
-------------------------------------------------------------------

A source is a specific database, application, file storage service, event tracking service, or function from which you wish to sync your data. Some examples of sources are MongoDB, Salesforce, or Google Sheets. Sometimes we will pull data in different ways for a single source, such as Adobe Analytics with our unique Adobe Analytics and Adobe Analytics Data Feed connectors.

Sync[](https://fivetran.com/docs/getting-started/glossary#sync)
---------------------------------------------------------------

During a sync, Fivetran replicates data from your source and loads it into your destination. Fivetran does not retain sync data except [in specific circumstances](https://fivetran.com/docs/privacy#retentionofcustomerdata). Learn how Fivetran syncs work in our [Sync Overview documentation](https://fivetran.com/docs/core-concepts/syncoverview). See also [historical sync](https://fivetran.com/docs/getting-started/glossary#historicalsync), [incremental sync](https://fivetran.com/docs/getting-started/glossary#incrementalsync), [initial sync](https://fivetran.com/docs/getting-started/glossary#initialsync), [re-sync](https://fivetran.com/docs/getting-started/glossary#resync), and [rollback sync](https://fivetran.com/docs/getting-started/glossary#rollbacksync).

Transformation[](https://fivetran.com/docs/getting-started/glossary#transformation)
-----------------------------------------------------------------------------------

Transformations are SQL scripts that are executed on your data based on specific events or conditions. Transformations map incoming data into a specific shape that is easier or faster to use in the next part of your data pipeline. Fivetran uses the term "transformation" to refer to two different types of reshaping:

*   Pre-load transformations: Fivetran performs some [minor transformations](https://fivetran.com/docs/core-concepts#transformationsandmapping) on your data before we load it into your destination.

*   Post-load transformations: Fivetran offers a feature called Transformations, which supports custom transformations in the destination after your data is loaded.

Fivetran offers [Transformations for dbt Core](https://fivetran.com/docs/transformations/dbt)*. Read our [Transformations documentation](https://fivetran.com/docs/transformations) for details. See also [Fivetran data models](https://fivetran.com/docs/getting-started/glossary#fivetrandatamodels)

Transformation Scheduling[](https://fivetran.com/docs/getting-started/glossary#transformationscheduling)
--------------------------------------------------------------------------------------------------------

[Transformation scheduling](https://fivetran.com/docs/transformations/transformation-scheduling) defines when and in what order transformations are executed. Scheduling allows transformations to run at designated times, in response to specific events, or at regular intervals, ensuring that the data is always up-to-date and ready for analysis.

Warning[](https://fivetran.com/docs/getting-started/glossary#warning)
---------------------------------------------------------------------

Warnings are a type of alert in your Fivetran dashboard that tell you about a problem with your connection that you may need to fix but that is not disrupting your data syncs. For example, a warning might tell you that we were unable to sync specific tables or columns because you are still using a column that has been deprecated by your application's API. See also [**alert**](https://fivetran.com/docs/getting-started/glossary#alert) and [**error**](https://fivetran.com/docs/getting-started/glossary#error).

* * *

* dbt Core is a trademark of dbt Labs, Inc. All rights therein are reserved to dbt Labs, Inc. Fivetran Transformations is not a product or service of or endorsed by dbt Labs, Inc.

Thanks for your feedback!

Was this page helpful?
