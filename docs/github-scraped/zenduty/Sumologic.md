---
id: Sumologic
title: Sumo Logic
---
Sumo Logic is industry's leading, secure, cloud-based service for logs & metrics management for modern apps, providing real-time analytics and insights.

To integrate Sumologic with Zenduty, complete the following steps:

## In Zenduty

1. To add a new Sumologic integration, go to "Teams" on Zenduty and click on the "Manage" button corresponding to the team you want to add the integration to.

2. Next, go to "Services" and click on the "Manage" button corresponding to the relevant Service.

3. Go to "Integrations" and then "Add New Integration". Give it a name and select the application "Sumologic" from the dropdown menu.

4. Go to "Configure" under your integrations and copy the webhooks URL generated.

## In Sumologic

1. After logging in, go to Manage Data -> Settings -> Connections

2. Click the '+' button at the top right of the screen to add a webhook.

![](/img/Integrations/Sumologic/1.png)

1. In the URL field, add the Webhook URL copied from before.

2. In the payload section, paste the following:

```
{
  "alert_status": "critical",
  "search_name": "{{SearchName}}",
  "search_description": "{{SearchDescription}}",
  "search_query": "{{SearchQuery}}",
  "search_query_url": "{{SearchQueryUrl}}",
  "time_range": "{{TimeRange}}",
  "fire_time": "{{FireTime}}",
  "raw_results_json": "{{RawResultsJson}}",
  "num_raw_results": "{{NumRawResults}}",
  "aggregate_results_json" : "{{AggregateResultsJson}}"
}
```

1. Click on Save

2. Go to the SumoLogic Scheduled Search screen. Click on "Save as" under your Search query. In the "Save Search As" section, enter a name for the search.

3. Click Schedule this search.

4. Choose an option from the "Run Frequency" menu.

5. For Alert Type, choose "Webhook". Select "Zenduty"

6. Click on "Save"

And that's it! The rules should trigger alerts which will then be visible on the Zenduty incidents page.
