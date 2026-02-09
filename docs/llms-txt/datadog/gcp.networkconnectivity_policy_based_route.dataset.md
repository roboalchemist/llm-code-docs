# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.networkconnectivity_policy_based_route.dataset.md

---
title: Policy Based Route
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Policy Based Route
---

# Policy Based Route

A Policy Based Route in Google Cloud lets you define advanced routing rules that go beyond standard destination-based routing. It allows traffic to be directed based on attributes such as source IP, protocol, or next hop. This enables fine-grained control over how traffic flows between networks, on-premises environments, and the internet, supporting use cases like traffic steering, service chaining, and custom egress routing.

```
gcp.networkconnectivity_policy_based_route
```

## Fields

| Title                   | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                                                                                     | Description |
| ----------------------- | ---- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                    | core | string        |
| ancestors               | core | array<string> |
| create_time             | core | timestamp     | Output only. Time when the policy-based route was created.                                                                                                                                                                                                                                                                                                    |
| datadog_display_name    | core | string        |
| description             | core | string        | Optional. An optional description of this resource. Provide this field when you create the resource.                                                                                                                                                                                                                                                          |
| filter                  | core | json          | Required. The filter to match L4 traffic.                                                                                                                                                                                                                                                                                                                     |
| interconnect_attachment | core | json          | Optional. The interconnect attachments that this policy-based route applies to.                                                                                                                                                                                                                                                                               |
| kind                    | core | string        | Output only. Type of this resource. Always networkconnectivity#policyBasedRoute for policy-based Route resources.                                                                                                                                                                                                                                             |
| labels                  | core | array<string> | User-defined labels.                                                                                                                                                                                                                                                                                                                                          |
| name                    | core | string        | Immutable. Identifier. A unique name of the resource in the form of `projects/{project_number}/locations/global/PolicyBasedRoutes/{policy_based_route_id}`                                                                                                                                                                                                    |
| network                 | core | string        | Required. Fully-qualified URL of the network that this route applies to, for example: projects/my-project/global/networks/my-network.                                                                                                                                                                                                                         |
| next_hop_ilb_ip         | core | string        | Optional. The IP address of a global-access-enabled L4 ILB that is the next hop for matching packets. For this version, only nextHopIlbIp is supported.                                                                                                                                                                                                       |
| next_hop_other_routes   | core | string        | Optional. Other routes that will be referenced to determine the next hop of the packet.                                                                                                                                                                                                                                                                       |
| organization_id         | core | string        |
| parent                  | core | string        |
| priority                | core | int64         | Optional. The priority of this policy-based route. Priority is used to break ties in cases where there are more than one matching policy-based routes found. In cases where multiple policy-based routes are matched, the one with the lowest-numbered priority value wins. The default value is 1000. The priority value must be from 1 to 65535, inclusive. |
| project_id              | core | string        |
| project_number          | core | string        |
| region_id               | core | string        |
| resource_name           | core | string        |
| self_link               | core | string        | Output only. Server-defined fully-qualified URL for this resource.                                                                                                                                                                                                                                                                                            |
| tags                    | core | hstore_csv    |
| update_time             | core | timestamp     | Output only. Time when the policy-based route was updated.                                                                                                                                                                                                                                                                                                    |
| virtual_machine         | core | json          | Optional. VM instances that this policy-based route applies to.                                                                                                                                                                                                                                                                                               |
| warnings                | core | json          | Output only. If potential misconfigurations are detected for this route, this field will be populated with warning messages.                                                                                                                                                                                                                                  |
| zone_id                 | core | string        |
