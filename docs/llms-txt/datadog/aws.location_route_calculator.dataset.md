# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.location_route_calculator.dataset.md

---
title: Location Route Calculator
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Location Route Calculator
---

# Location Route Calculator

Location Route Calculator in AWS provides details about a specific route calculator resource within the Amazon Location Service. A route calculator is used to compute travel routes and directions between geographic points, considering factors like travel mode and road networks. This resource description includes metadata such as the calculator's name, data source, and configuration details, enabling applications to generate optimized routes for logistics, navigation, or mapping use cases.

```
aws.location_route_calculator
```

## Fields

| Title           | ID   | Type       | Data Type                                                                                                                                                                                                              | Description |
| --------------- | ---- | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key            | core | string     |
| account_id      | core | string     |
| calculator_arn  | core | string     | The Amazon Resource Name (ARN) for the Route calculator resource. Use the ARN when you specify a resource across Amazon Web Services. Format example: arn:aws:geo:region:account-id:route-calculator/ExampleCalculator |
| calculator_name | core | string     | The name of the route calculator resource being described.                                                                                                                                                             |
| create_time     | core | timestamp  | The timestamp when the route calculator resource was created in ISO 8601 format: YYYY-MM-DDThh:mm:ss.sssZ. For example, 2020â07-2T12:15:20.000Z+01:00                                                                  |
| data_source     | core | string     | The data provider of traffic and road network data. Indicates one of the available providers: Esri Grab Here For more information about data providers, see Amazon Location Service data providers.                    |
| description     | core | string     | The optional description of the route calculator resource.                                                                                                                                                             |
| pricing_plan    | core | string     | Always returns RequestBasedUsage.                                                                                                                                                                                      |
| tags            | core | hstore_csv |
| update_time     | core | timestamp  | The timestamp when the route calculator resource was last updated in ISO 8601 format: YYYY-MM-DDThh:mm:ss.sssZ. For example, 2020â07-2T12:15:20.000Z+01:00                                                             |
