# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.transcoder_job_template.dataset.md

---
title: Transcoder Job Template
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Transcoder Job Template
---

# Transcoder Job Template

A Transcoder Job Template in Google Cloud is a reusable configuration that defines how media files should be processed and converted using the Transcoder API. It specifies input and output formats, video and audio settings, and other transcoding parameters. Templates simplify job creation by allowing consistent encoding workflows without redefining settings for each job.

```
gcp.transcoder_job_template
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                   | Description |
| -------------------- | ---- | ------------- | --------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| config               | core | json          | The configuration for this template.                                                                                        |
| datadog_display_name | core | string        |
| labels               | core | array<string> | The labels associated with this job template. You can use these to organize and group your job templates.                   |
| name                 | core | string        | The resource name of the job template. Format: `projects/{project_number}/locations/{location}/jobTemplates/{job_template}` |
| organization_id      | core | string        |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| region_id            | core | string        |
| resource_name        | core | string        |
| tags                 | core | hstore_csv    |
| zone_id              | core | string        |
