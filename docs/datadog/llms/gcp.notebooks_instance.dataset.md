# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.notebooks_instance.dataset.md

---
title: Vertex AI Workbench Instance
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Vertex AI Workbench Instance
---

# Vertex AI Workbench Instance

Vertex AI Workbench Instance is a managed Jupyter-based development environment in Google Cloud designed for data science and machine learning. It integrates with Vertex AI services, BigQuery, and other GCP tools, allowing users to build, train, and deploy models efficiently. It supports both managed and user-managed notebook instances with customizable compute and storage options.

```
gcp.notebooks_instance
```

## Fields

| Title                       | ID   | Type          | Data Type                                                                                                                                                                                                                          | Description |
| --------------------------- | ---- | ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                        | core | string        |
| ancestors                   | core | array<string> |
| create_time                 | core | timestamp     | Output only. Instance creation time.                                                                                                                                                                                               |
| creator                     | core | string        | Output only. Email address of entity that sent original CreateInstance request.                                                                                                                                                    |
| datadog_display_name        | core | string        |
| disable_proxy_access        | core | bool          | Optional. If true, the notebook instance will not register with the proxy.                                                                                                                                                         |
| enable_deletion_protection  | core | bool          | Optional. If true, deletion protection will be enabled for this Workbench Instance. If false, deletion protection will be disabled for this Workbench Instance.                                                                    |
| enable_managed_euc          | core | bool          | Optional. Flag to enable managed end user credentials for the instance.                                                                                                                                                            |
| enable_third_party_identity | core | bool          | Optional. Flag that specifies that a notebook can be accessed with third party identity provider.                                                                                                                                  |
| gce_setup                   | core | json          | Optional. Compute Engine setup for the notebook. Uses notebook-defined fields.                                                                                                                                                     |
| health_state                | core | string        | Output only. Instance health_state.                                                                                                                                                                                                |
| id                          | core | string        | Output only. Unique ID of the resource.                                                                                                                                                                                            |
| instance_owners             | core | array<string> | Optional. The owner of this instance after creation. Format: `alias@example.com` Currently supports one owner only. If not specified, all of the service account users of your VM instance's service account can use the instance. |
| labels                      | core | array<string> | Optional. Labels to apply to this instance. These can be later modified by the UpdateInstance method.                                                                                                                              |
| name                        | core | string        | Output only. Identifier. The name of this notebook instance. Format: `projects/{project_id}/locations/{location}/instances/{instance_id}`                                                                                          |
| organization_id             | core | string        |
| parent                      | core | string        |
| project_id                  | core | string        |
| project_number              | core | string        |
| proxy_uri                   | core | string        | Output only. The proxy endpoint that is used to access the Jupyter notebook.                                                                                                                                                       |
| region_id                   | core | string        |
| resource_name               | core | string        |
| satisfies_pzi               | core | bool          | Output only. Reserved for future use for Zone Isolation.                                                                                                                                                                           |
| satisfies_pzs               | core | bool          | Output only. Reserved for future use for Zone Separation.                                                                                                                                                                          |
| state                       | core | string        | Output only. The state of this instance.                                                                                                                                                                                           |
| tags                        | core | hstore_csv    |
| third_party_proxy_url       | core | string        | Output only. The workforce pools proxy endpoint that is used to access the Jupyter notebook.                                                                                                                                       |
| update_time                 | core | timestamp     | Output only. Instance update time.                                                                                                                                                                                                 |
| upgrade_history             | core | json          | Output only. The upgrade history of this instance.                                                                                                                                                                                 |
| zone_id                     | core | string        |
