# Source: https://docs.curator.interworks.com/embedding_using_analytics/data_manager/sending_data_to_webhooks.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.curator.interworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Sending Data to Webhooks

> Configure Data Manager to automatically send collected data to external systems via webhook integrations.

When using mark commenting, you have the option to send the metadata to a webhook. This features allows you to send
mark commenting data to any webhook endpoint, instead of Data Manager.

To enable this feature,

1. Login to the backend of your Curator instance (e.g. `http://curatorexample.com/backend`).
2. Navigate to the **Settings** > **Portal Settings** > **Features** section from the left-hand menu.
3. Enable "Integration Automation" in the Functionality Section.
4. Save and refresh the page.
5. Navigate to **Integrations** > **Automation** > **API Relay** section from the left-hand menu.
6. Create a new API Relay. Use the webhook endpoint as the URL field.
7. "Outgoing Request Content" and "Incoming Request Validation" can be edited as needed for more complex webhook usage.
8. Once an API Relay is created, it needs to be selected for the necessary Data Group. For more information on Data
   Manager, take a look [here](/embedding_using_analytics/data_manager/data_manager_basics).
9. Visit **Data Manager** > **Data Groups** and select the necessary Data Group. Enable "Send to Webhook" and select
   the appropriate API Relay from the dropdown.
10. Visit **Tableau** > **Dashboards** and select the Dashboard you wish to enable. In the
    "Mark Commenting" tab, now select the Data Manager Group you wish to use (from step 9).
11. Data from the Data Manager Group form will now be sent to the webhook provided.
