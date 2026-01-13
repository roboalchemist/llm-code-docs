# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.globalaccelerator_endpointgroup.dataset.md

---
title: Global Accelerator Endpoint Group
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Global Accelerator Endpoint Group
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.globalaccelerator_endpointgroup.dataset/index.html
---

# Global Accelerator Endpoint Group

This table represents the Global Accelerator Endpoint Group resource from Amazon Web Services.

```
aws.globalaccelerator_endpointgroup
```

## Fields

| Title                         | ID   | Type    | Data Type                                                                                                                                                                                                                                                                                                                                                                                      | Description |
| ----------------------------- | ---- | ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                          | core | string  |
| account_id                    | core | string  |
| endpoint_descriptions         | core | json    | The list of endpoint objects.                                                                                                                                                                                                                                                                                                                                                                  |
| endpoint_group_arn            | core | string  | The Amazon Resource Name (ARN) of the endpoint group.                                                                                                                                                                                                                                                                                                                                          |
| endpoint_group_region         | core | string  | The Amazon Web Services Region where the endpoint group is located.                                                                                                                                                                                                                                                                                                                            |
| health_check_interval_seconds | core | int64   | The timeâ10 seconds or 30 secondsâbetween health checks for each endpoint. The default value is 30.                                                                                                                                                                                                                                                                                            |
| health_check_path             | core | string  | If the protocol is HTTP/S, then this value provides the ping path that Global Accelerator uses for the destination on the endpoints for health checks. The default is slash (/).                                                                                                                                                                                                               |
| health_check_port             | core | int64   | The port that Global Accelerator uses to perform health checks on endpoints that are part of this endpoint group. The default port is the port for the listener that this endpoint group is associated with. If the listener port is a list, Global Accelerator uses the first specified port in the list of ports.                                                                            |
| health_check_protocol         | core | string  | The protocol that Global Accelerator uses to perform health checks on endpoints that are part of this endpoint group. The default value is TCP.                                                                                                                                                                                                                                                |
| port_overrides                | core | json    | Allows you to override the destination ports used to route traffic to an endpoint. Using a port override lets you map a list of external destination ports (that your users send traffic to) to a list of internal destination ports that you want an application endpoint to receive traffic on.                                                                                              |
| tags                          | core | hstore  |
| threshold_count               | core | int64   | The number of consecutive health checks required to set the state of a healthy endpoint to unhealthy, or to set an unhealthy endpoint to healthy. The default value is 3.                                                                                                                                                                                                                      |
| traffic_dial_percentage       | core | float64 | The percentage of traffic to send to an Amazon Web Services Region. Additional traffic is distributed to other endpoint groups for this listener. Use this action to increase (dial up) or decrease (dial down) traffic to a specific Region. The percentage is applied to the traffic that would otherwise have been routed to the Region based on optimal routing. The default value is 100. |
