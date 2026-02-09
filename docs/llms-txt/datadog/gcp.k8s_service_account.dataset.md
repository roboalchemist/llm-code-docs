# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.k8s_service_account.dataset.md

---
title: K8s Service Account
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > K8s Service Account
---

# K8s Service Account

This table represents the k8s_service_account resource from Google Cloud Platform.

```
gcp.k8s_service_account
```

## Fields

| Title                           | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Description |
| ------------------------------- | ---- | ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                            | core | string        |
| ancestors                       | core | array<string> |
| api_version                     | core | string        | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources                                                                                                                                                                                                                                                                                                                                                                                                                                |
| automount_service_account_token | core | bool          | AutomountServiceAccountToken indicates whether pods running as this service account should have an API token automatically mounted. Can be overridden at the pod level.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| datadog_display_name            | core | string        |
| image_pull_secrets              | core | json          | ImagePullSecrets is a list of references to secrets in the same namespace to use for pulling any images in pods that reference this ServiceAccount. ImagePullSecrets are distinct from Secrets because Secrets can be mounted in the pod, but ImagePullSecrets are only accessed by the kubelet. More info: https://kubernetes.io/docs/concepts/containers/images/#specifying-imagepullsecrets-on-a-pod                                                                                                                                                                                                                                                                                                                          |
| kind                            | core | string        | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds                                                                                                                                                                                                                                                                                                                                                                                                                               |
| labels                          | core | array<string> |
| metadata                        | core | json          | Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| organization_id                 | core | string        |
| parent                          | core | string        |
| project_id                      | core | string        |
| project_number                  | core | string        |
| region_id                       | core | string        |
| resource_name                   | core | string        |
| secrets                         | core | json          | Secrets is a list of the secrets in the same namespace that pods running using this ServiceAccount are allowed to use. Pods are only limited to this list if this service account has a "kubernetes.io/enforce-mountable-secrets" annotation set to "true". The "kubernetes.io/enforce-mountable-secrets" annotation is deprecated since v1.32. Prefer separate namespaces to isolate access to mounted secrets. This field should not be used to find auto-generated service account token secrets for use outside of pods. Instead, tokens can be requested directly using the TokenRequest API, or service account token secrets can be manually created. More info: https://kubernetes.io/docs/concepts/configuration/secret |
| tags                            | core | hstore_csv    |
| zone_id                         | core | string        |
