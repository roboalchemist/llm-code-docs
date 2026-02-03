# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/databricks/use_spark_submit_task.md

---
title: Beta - job's task is legacy (spark_submit_task)
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Beta - job's task is legacy
  (spark_submit_task)
---

# Beta - job's task is legacy (spark_submit_task)

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `375cdab9-3f94-4ae0-b1e3-8fbdf9cdf4d7`

**Cloud Provider:** Databricks

**Platform:** Terraform

**Severity:** Medium

**Category:** Best Practices

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/databricks/databricks/latest/docs/resources/job#spark_submit_task-configuration-block)

### Description{% #description %}

This rule detects `databricks_job` resources with `task.spark_submit_task` and reports an `IncorrectValue` issue. Use of `spark_submit_task` in job tasks is not allowed.

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "databricks_job" "negative1" {
  name = "Job with multiple tasks"

  job_cluster {
    job_cluster_key = "j"
    new_cluster {
      num_workers   = 2
      spark_version = data.databricks_spark_version.latest.id
      node_type_id  = data.databricks_node_type.smallest.id
    }
  }

  task {
    task_key = "a"

    new_cluster {
      num_workers   = 1
      spark_version = data.databricks_spark_version.latest.id
      node_type_id  = data.databricks_node_type.smallest.id
    }

    notebook_task {
      notebook_path = databricks_notebook.this.path
    }
  }
}
```

```terraform
resource "databricks_job" "negative1" {
  name = "Job with multiple tasks"

  job_cluster {
    job_cluster_key = "j"
    new_cluster {
      num_workers   = 2
      spark_version = data.databricks_spark_version.latest.id
      node_type_id  = data.databricks_node_type.smallest.id
    }
  }

  task {
    task_key = "a"

    new_cluster {
      num_workers   = 1
      spark_version = data.databricks_spark_version.latest.id
      node_type_id  = data.databricks_node_type.smallest.id
    }

    notebook_task {
      notebook_path = databricks_notebook.this.path
    }
  }

  task {
    task_key = "b"
    //this task will only run after task a
    depends_on {
      task_key = "a"
    }

    existing_cluster_id = databricks_cluster.shared.id

    spark_jar_task {
      main_class_name = "com.acme.data.Main"
    }
  }

  task {
    task_key = "c"

    job_cluster_key = "j"

    notebook_task {
      notebook_path = databricks_notebook.this.path
    }
  }
  //this task starts a Delta Live Tables pipline update
  task {
    task_key = "d"

    pipeline_task {
      pipeline_id = databricks_pipeline.this.id
    }
  }
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "databricks_job" "positive" {
  name = "Job with multiple tasks"

  job_cluster {
    job_cluster_key = "j"
    new_cluster {
      num_workers   = 2
      spark_version = data.databricks_spark_version.latest.id
      node_type_id  = data.databricks_node_type.smallest.id
    }
  }

  task {
    task_key = "a"

    existing_cluster_id = databricks_cluster.shared.id

    spark_submit_task {
      main_class_name = "com.acme.data.Main"
    }
  }
}
```

```terraform
resource "databricks_job" "positive" {
  name = "Job with multiple tasks"

  job_cluster {
    job_cluster_key = "j"
    new_cluster {
      num_workers   = 2
      spark_version = data.databricks_spark_version.latest.id
      node_type_id  = data.databricks_node_type.smallest.id
    }
  }

  task {
    task_key = "a"

    new_cluster {
      num_workers   = 1
      spark_version = data.databricks_spark_version.latest.id
      node_type_id  = data.databricks_node_type.smallest.id
    }

    notebook_task {
      notebook_path = databricks_notebook.this.path
    }
  }

  task {
    task_key = "b"
    //this task will only run after task a
    depends_on {
      task_key = "a"
    }

    existing_cluster_id = databricks_cluster.shared.id

    spark_submit_task {
      main_class_name = "com.acme.data.Main"
    }
  }

  task {
    task_key = "c"

    job_cluster_key = "j"

    notebook_task {
      notebook_path = databricks_notebook.this.path
    }
  }
  //this task starts a Delta Live Tables pipline update
  task {
    task_key = "d"

    pipeline_task {
      pipeline_id = databricks_pipeline.this.id
    }
  }
}
```
