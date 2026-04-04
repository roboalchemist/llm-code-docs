# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.k8s_storage_class.dataset.md

---
title: K8s Storage Class
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > K8s Storage Class
---

# K8s Storage Class

This table represents the k8s_storage_class resource from Google Cloud Platform.

```
gcp.k8s_storage_class
```

## Fields

| Title                  | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                                                     | Description |
| ---------------------- | ---- | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                   | core | string        |
| allow_volume_expansion | core | bool          | allowVolumeExpansion shows whether the storage class allow volume expand.                                                                                                                                                                                                                                                     |
| allowed_topologies     | core | json          | allowedTopologies restrict the node topologies where volumes can be dynamically provisioned. Each volume plugin defines its own supported topology specifications. An empty TopologySelectorTerm list means there is no topology restriction. This field is only honored by servers that enable the VolumeScheduling feature. |
| ancestors              | core | array<string> |
| api_version            | core | string        | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources                             |
| datadog_display_name   | core | string        |
| kind                   | core | string        | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds                            |
| labels                 | core | array<string> |
| metadata               | core | json          | Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata                                                                                                                                                                                           |
| mount_options          | core | array<string> | mountOptions controls the mountOptions for dynamically provisioned PersistentVolumes of this storage class. e.g. ["ro", "soft"]. Not validated - mount of the PVs will simply fail if one is invalid.                                                                                                                         |
| organization_id        | core | string        |
| parent                 | core | string        |
| project_id             | core | string        |
| project_number         | core | string        |
| provisioner            | core | string        | provisioner indicates the type of the provisioner.                                                                                                                                                                                                                                                                            |
| reclaim_policy         | core | string        | reclaimPolicy controls the reclaimPolicy for dynamically provisioned PersistentVolumes of this storage class. Defaults to Delete.                                                                                                                                                                                             |
| region_id              | core | string        |
| resource_name          | core | string        |
| tags                   | core | hstore_csv    |
| volume_binding_mode    | core | string        | volumeBindingMode indicates how PersistentVolumeClaims should be provisioned and bound. When unset, VolumeBindingImmediate is used. This field is only honored by servers that enable the VolumeScheduling feature.                                                                                                           |
| zone_id                | core | string        |
