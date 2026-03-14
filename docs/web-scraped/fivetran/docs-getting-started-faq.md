# Source: https://fivetran.com/docs/getting-started/faq

Title: Frequently Asked Questions

URL Source: https://fivetran.com/docs/getting-started/faq

Markdown Content:
Get answers to technical questions about getting started with Fivetran.

* * *

How long does it take to set up Fivetran?[](https://fivetran.com/docs/getting-started/faq#howlongdoesittaketosetupfivetran)
---------------------------------------------------------------------------------------------------------------------------

It depends on your source and destination. Check our setup guides to see the tasks for your source and destination. Each source and destination also has a list of prerequisites for setup. To make setup faster, get your prerequisites ready before you start to set up your connection. During the setup process, you may need to contact others (like a database administrator or AWS account owner) for help, which might slow you down.

When does my 14-day free trial start?[](https://fivetran.com/docs/getting-started/faq#whendoesmy14dayfreetrialstart)
--------------------------------------------------------------------------------------------------------------------

The free trial begins when a connection completes its [initial sync](https://fivetran.com/docs/getting-started/glossary#initialsync) or, in some cases (for example, [priority-first sync connectors](https://fivetran.com/docs/usage-based-pricing#priorityfirstsync)), when it starts an [incremental sync](https://fivetran.com/docs/getting-started/glossary#incrementalsync) and the system detects incremental data.

What's the difference between a connector and a connection?[](https://fivetran.com/docs/getting-started/faq#whatsthedifferencebetweenaconnectorandaconnection)
--------------------------------------------------------------------------------------------------------------------------------------------------------------

A _connector_ is a tool Fivetran provides to integrate a specific data source with a destination. For example, our Salesforce connector allows you to sync data from Salesforce to your destination.

A _connection_ is a specific instance of a data pipeline that uses a connector. You can create multiple connections using the same connector. For example, you might set up several Salesforce connections to send data from different Salesforce accounts to different destinations.

In summary:

*   _Connector_ - The tool for a type of data source (for example, Salesforce connector).
*   _Connection_ - An individual pipeline you create with that tool (for example, your Salesforce connection syncing to a destination).

Where can I see my data in Fivetran?[](https://fivetran.com/docs/getting-started/faq#wherecaniseemydatainfivetran)
------------------------------------------------------------------------------------------------------------------

You can’t see your data in Fivetran because we don’t store it. The Fivetran sync loads your data into your destination. While you can’t see your data directly in Fivetran, you can check your schema and sync status on your Fivetran dashboard.

Why don’t I see any data in my destination yet?[](https://fivetran.com/docs/getting-started/faq#whydontiseeanydatainmydestinationyet)
-------------------------------------------------------------------------------------------------------------------------------------

It can take a while for Fivetran to load data into your destination. Some sources have restrictive API limits which constrain how much data we can sync in a given time. Large amounts of data in your source can also make the initial sync take longer. You can check your sync status on your Fivetran dashboard.

What happens if a Fivetran sync fails?[](https://fivetran.com/docs/getting-started/faq#whathappensifafivetransyncfails)
-----------------------------------------------------------------------------------------------------------------------

You do not lose data when a sync fails, but no data is added or updated in your destination. Fivetran notifies you about your failed sync so that you can begin troubleshooting:

*   We update the connection status in your Fivetran dashboard to "broken."

*   We create an Error message in your Fivetran dashboard with details about your failed sync. (Learn more about Errors in our [Alerts documentation](https://fivetran.com/docs/using-fivetran/fivetran-dashboard/alerts).)

*   If you have email notifications enabled on your Fivetran account, we send you an email notification.

*   If you use the [Fivetran Platform Connector](https://fivetran.com/docs/logs), you can see the sync failure in your logs.

Once you resolve the issues that caused your sync to fail, Fivetran resumes your sync from where it left off.

To get help from our support team, log in to your Fivetran account and go to our [Zendesk-based support portal](https://support.fivetran.com/hc/en-us). You can open tickets, update your tickets, and track their progress and status. You can also find answers to frequently asked questions.

When working on a support ticket, we sometimes need access to your data to troubleshoot or fix your connections or destination. We will send an email asking you to grant Fivetran access to your data for the next 21 days. The email contains a link to your Fivetran dashboard. After you follow the link, you can **Allow** access to your data, or **Deny** it.

You do not have to grant Fivetran access to your data. However, doing so lets us troubleshoot or fix your connections or destination faster.

Fivetran then adds a message to the support ticket, confirming that you approved or denied data access. You can revoke the data access before the 21-day access period has expired. To revoke the access, click **Revoke Access** in the ticket and then click **Revoke** in your Fivetran dashboard to confirm your action.

![Image 1: Revoke Data Access in Zendesk](https://fivetran.com/static-assets-docs/_next/static/media/revoke-access-support.8be8a7df.webp)

You need to have Edit access to the affected connections or destination to be able to grant access to the data. If you do not have Edit access, you can add another user with Edit access to the support ticket and ask them to grant access.

What kind of notifications do I get?[](https://fivetran.com/docs/getting-started/faq#whatkindofnotificationsdoiget)
-------------------------------------------------------------------------------------------------------------------

You will get two kinds of notifications - email notifications and alerts in your Fivetran dashboard. You can customize your notification settings in your Fivetran dashboard. Learn more in our [Alerts](https://fivetran.com/docs/using-fivetran/fivetran-dashboard/alerts)&[Notifications](https://fivetran.com/docs/using-fivetran/fivetran-dashboard/user-management/notifications) documentation.

Can I sync from a non-native source?[](https://fivetran.com/docs/getting-started/faq#canisyncfromanonnativesource)
------------------------------------------------------------------------------------------------------------------

Yes. Learn how in our [non-native source Troubleshooting page](https://fivetran.com/docs/getting-started/troubleshooting/syncing-from-unsupported-sources).

Can I select a specific region to process my data with Fivetran?[](https://fivetran.com/docs/getting-started/faq#caniselectaspecificregiontoprocessmydatawithfivetran)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------

Yes. Learn about the regions Fivetran supports in our [data residency documentation](https://fivetran.com/docs/privacy#fivetrandataresidency).

Can I calculate sync speed?[](https://fivetran.com/docs/getting-started/faq#canicalculatesyncspeed)
---------------------------------------------------------------------------------------------------

Yes. Learn how in our [Sync Speed Calculation Troubleshooting page](https://fivetran.com/docs/getting-started/troubleshooting/calculating-sync-speed).

Can I monitor the current status of Fivetran services?[](https://fivetran.com/docs/getting-started/faq#canimonitorthecurrentstatusoffivetranservices)
-----------------------------------------------------------------------------------------------------------------------------------------------------

Yes. Learn how in our [Fivetran Services Status Monitoring Troubleshooting page](https://fivetran.com/docs/getting-started/troubleshooting/monitor-services-status).

How does triggering a manual sync affect scheduled syncs?[](https://fivetran.com/docs/getting-started/faq#howdoestriggeringamanualsyncaffectscheduledsyncs)
-----------------------------------------------------------------------------------------------------------------------------------------------------------

Learn how in our [Manual Sync Impact on Scheduled Sync Troubleshooting page](https://fivetran.com/docs/getting-started/troubleshooting/manual-sync-affects-scheduled).

What does the name Fivetran mean?[](https://fivetran.com/docs/getting-started/faq#whatdoesthenamefivetranmean)
--------------------------------------------------------------------------------------------------------------

Fivetran is a play on the [programming language Fortran](https://en.wikipedia.org/wiki/Fortran). Our co-founders George Fraser and Taylor Brown started in late 2012 with an idea for a new programming language for working with big data. That evolved into a [spreadsheet for big data](https://www.ycombinator.com/blog/fivetran-yc-w13-launches-to-bring-spreadsheets-into-the-modern-age-sql-and-matlab-meet-easy-point-and-click/), which they built. The spreadsheet was a webapp that stored and queried data in what was then a brand new technology: [AWS Redshift](https://en.wikipedia.org/wiki/Amazon_Redshift), the first cloud data warehouse. The feedback from one of the users testing the spreadsheet was that they only valued moving Salesforce data into Redshift. That was when Fivetran pivoted, in startup fashion, to data pipelines.

What is a Lite connector?[](https://fivetran.com/docs/getting-started/faq#whatisaliteconnector)
-----------------------------------------------------------------------------------------------

A Lite connector is a new tier of connector built for specific use cases with an accelerated development cycle. For more information, see our [Lite connectors documentation](https://fivetran.com/docs/connectors/applications/lite-connectors).

Where can I find the Fivetran Master Subscription Agreement and nondisclosure terms?[](https://fivetran.com/docs/getting-started/faq#wherecanifindthefivetranmastersubscriptionagreementandnondisclosureterms)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

To see the Master Subscription Agreement, visit our [legal page](https://www.fivetran.com/legal). The nondisclosure terms are included in section [4.3](https://www.fivetran.com/legal#:~:text=the%20disclosing%20party.-,4.3%20Nondisclosure,-.%20The%20receiving%20party).

Where can I find Fivetran's compliance documents, such as the SOC 2 Type I, SOC 2 Type II, and ISO 27001 certificates?[](https://fivetran.com/docs/getting-started/faq#wherecanifindfivetranscompliancedocumentssuchasthesoc2typeisoc2typeiiandiso27001certificates)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

To see our compliance documents, visit the [Fivetran Trust Center](https://trust.fivetran.com/).

What web browser should I use?[](https://fivetran.com/docs/getting-started/faq#whatwebbrowsershouldiuse)
--------------------------------------------------------------------------------------------------------

We recommend using any of the last two major versions of the following web browsers for the best experience when working in your [Fivetran dashboard](https://fivetran.com/dashboard/), reading our [documentation](https://fivetran.com/docs), or exploring our [blog](https://www.fivetran.com/blog):

*   [Google Chrome](https://www.google.com/chrome/)
*   [Safari](https://www.apple.com/safari/)
*   [Firefox](https://www.mozilla.org/firefox/browsers/)
*   [Chromium-based browsers](https://www.chromium.org/):
    *   [Microsoft Edge](https://www.microsoft.com/edge)
    *   [Opera](https://www.opera.com/)
    *   [Yandex Browser](https://browser.yandex.com/)

Some Google Chrome extensions (for example, AdBlock) may affect your user experience with the [Fivetran website](https://fivetran.com/).

### Why do some column or table names in my destination not match those in my source?[](https://fivetran.com/docs/getting-started/faq#whydosomecolumnortablenamesinmydestinationnotmatchthoseinmysource)

When we sync data to your destination, we use two different table and column naming rule sets:

*   [Naming rule set for non-database connectors](https://fivetran.com/docs/core-concepts/naming-conventions#tableandcolumnnamingrulesetfornondatabaseconnectors)
*   [Naming rule set for database connectors](https://fivetran.com/docs/core-concepts/naming-conventions#tableandcolumnnamingrulesetfordatabaseconnectors)

See our [naming conventions documentation](https://fivetran.com/docs/core-concepts/naming-conventions) for more information.

### Why is some data missing following the completion of my initial sync?[](https://fivetran.com/docs/getting-started/faq#whyissomedatamissingfollowingthecompletionofmyinitialsync)

If your connector supports [priority-first syncs](https://fivetran.com/docs/using-fivetran/features#priorityfirstsync), we only sync the most recent data to your destination during the initial sync. We then fetch historical data during subsequent syncs.

### Can I manage multiple environments by connecting one destination to multiple Fivetran accounts?[](https://fivetran.com/docs/getting-started/faq#canimanagemultipleenvironmentsbyconnectingonedestinationtomultiplefivetranaccounts)

Yes, you can connect one destination to multiple accounts. However, we recommend managing multiple environments by creating multiple destinations in one Fivetran account and syncing data from each connection to its respective destination. This approach leverages our destination [user roles](https://fivetran.com/docs/using-fivetran/fivetran-dashboard/account-settings/role-based-access-control#standardrolesinourrbacmodel) and optimizes connection and billing management.

Thanks for your feedback!

Was this page helpful?
