# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.financialservices_prediction_result.dataset.md

---
title: Financial Services Prediction Result
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Financial Services Prediction Result
---

# Financial Services Prediction Result

This table represents the Financial Services Prediction Result resource from Google Cloud Platform.

```
gcp.financialservices_prediction_result
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                                                     | Description |
| -------------------- | ---- | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| create_time          | core | timestamp     | Output only. The timestamp of creation of this resource.                                                                                                                      |
| datadog_display_name | core | string        |
| dataset              | core | string        | Required. The resource name of the Dataset to do predictions on Format: `/projects/{project_num}/locations/{location}/instances/{instance}/dataset/{dataset_id}`              |
| end_time             | core | timestamp     | Required. Specifies the latest time from which data is used to generate features for predictions. This time should be no later than the end of the date_range of the dataset. |
| labels               | core | array<string> | Labels                                                                                                                                                                        |
| line_of_business     | core | string        | Output only. The line of business (Retail/Commercial) this prediction is for. Determined by Model, cannot be set by user.                                                     |
| model                | core | string        | Required. The resource name of the Model to use to use to make predictions Format: `/projects/{project_num}/locations/{location}/instances/{instance}/models/{model}`         |
| name                 | core | string        | Output only. The resource name of the PredictionResult. format: `/projects/{project_num}/locations/{location}/instances/{instance}/predictionResults/{prediction_result}`     |
| organization_id      | core | string        |
| outputs              | core | json          | Required. Where to write the output of the predictions.                                                                                                                       |
| parent               | core | string        |
| prediction_periods   | core | int64         | The number of consecutive months to produce predictions for, ending with the last full month prior to end_time according to the dataset's timezone.                           |
| project_id           | core | string        |
| project_number       | core | string        |
| region_id            | core | string        |
| resource_name        | core | string        |
| state                | core | string        | Output only. State of the PredictionResult (creating, active, deleting, etc.)                                                                                                 |
| tags                 | core | hstore_csv    |
| update_time          | core | timestamp     | Output only. The timestamp of the most recent update of this resource.                                                                                                        |
| zone_id              | core | string        |
