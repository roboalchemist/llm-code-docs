# Source: https://docs.curator.interworks.com/embedding_using_analytics/tableau_dashboards/email_subscriptions.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.curator.interworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Email Subscriptions

> Set up automated email notifications for users when Tableau Server views are updated with new data.

Curator allows users to subscribe to dashboards where updates to the underlying Tableau Server views will be emailed to
them on a set schedule.

## Known Limitations

There is currently a limitation in Tableau's APIs that make subscribing to Custom Views unavailable for embedded
applications.  Curator can only create a subscription to the Dashboard's default view through Tableau's subscription
engine.  However,
[Report Builder](/embedding_using_analytics/report_builder/overview_and_enabling_report_builder)
supports subscriptions to Custom Views.

This functionality requires that the Tableau Server REST API is enabled. This allows you to subscribe to a Dashboard or
to the workbook the Dashboard belongs to on the associated Tableau Server.  See the
[Tableau Connection Setup](/creating_integrations/tableau_connection/creating_a_connection)
section for more information.

***To enable email subscriptions:***

1. Navigate to the backend of the system (e.g. `http://curatorexample.com/backend`).
2. Log in if prompted.
3. Click on the **Settings** > **Curator** > **Portal Settings** in the left-hand side navigation.
4. Click on the "Features" tab at the top of the main page content.
5. Click to switch on the "Subscriptions" setting under the "Toolbar Buttons (Tableau Actions)" section and click the
   "Save" button.

***To subscribe to an eligible Dashboard/workbook:***

1. Navigate to the frontend of the system (e.g. `http://curatorexample.com`).
2. Log in if prompted.
3. Navigate to the desired Dashboard by using the navigation menu.
4. Click on the envelope icon at the top right portion of the screen. Normally this is displayed on the right side of
   the title bar in the Dashboard.
5. Select the desired schedule.
6. Select either workbook or Dashboard in the dropdown to receive subscriptions.
7. Click on the "Add Subscription" button.
