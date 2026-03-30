# Source: https://docs.datadoghq.com/data_observability/jobs_monitoring/emr.md

---
title: 'Enable Data Observability: Jobs Monitoring for Spark on Amazon EMR'
description: >-
  Configure Data Observability: Jobs Monitoring for Apache Spark applications on
  Amazon EMR clusters using AWS Secrets Manager and bootstrap actions.
breadcrumbs: >-
  Docs > Data Observability Overview > Data Observability: Jobs Monitoring >
  Enable Data Observability: Jobs Monitoring for Spark on Amazon EMR
---

# Enable Data Observability: Jobs Monitoring for Spark on Amazon EMR

[Data Observability: Jobs Monitoring](https://docs.datadoghq.com/data_jobs) gives visibility into the performance and reliability of Apache Spark applications on Amazon EMR.

If you are using [EMR on EKS](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks.html), follow these [instructions for setting up DJM on Kubernetes](https://docs.datadoghq.com/data_jobs/kubernetes/).

## Requirements{% #requirements %}

[Amazon EMR Release 6.0.1](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-601-release.html) or later is required.

## Setup{% #setup %}

Follow these steps to enable Data Observability: Jobs Monitoring for Amazon EMR.

1. Store your Datadog API key in AWS Secrets Manager (Recommended).
1. Grant permissions to EMR EC2 instance profile.
1. Create and configure your EMR cluster.
1. Specify service tagging per Spark application.

### Store your Datadog API key in AWS Secrets Manager (Recommended){% #store-your-datadog-api-key-in-aws-secrets-manager-recommended %}

1. Take note of your [Datadog API key](https://app.datadoghq.com/organization-settings/api-keys).
1. In [AWS Secrets Manager](https://console.aws.amazon.com/secretsmanager/), choose **Store a new secret**.
   - Under **Secret type**, select **Other type of secret**.
   - Under **Key/value pairs**, add your Datadog API key as a key-value pair, where the key is `dd_api_key`.
     {% image
        source="https://datadog-docs.imgix.net/images/data_jobs/emr/key_value.36d09d59097eb62ef9fc7f2c670dfba4.png?auto=format"
        alt="AWS Secrets Manager, Store a new secret. A section titled 'Key/value pairs'. On the left, a text box containing 'dd_api_key'. On the right, a text box containing a redacted API key." /%}
   - Then, click **Next**.
1. On the **Configure secret** page, enter a **Secret name**. You can use `datadog/dd_api_key`. Then, click **Next**.
1. On the **Configure rotation** page, you can optionally turn on [automatic rotation](https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotating-secrets.html). Then, click **Next**.
1. On the **Review** page, review your secret details. Then, click **Store**.
1. In AWS Secrets Manager, open the secret you created. Take note of the **Secret ARN**.

### Grant permissions to EMR EC2 instance profile{% #grant-permissions-to-emr-ec2-instance-profile %}

EMR EC2 instance profile is a IAM role assigned to every EC2 instance in an Amazon EMR cluster when the instance launches. Follow [the Amazon guide](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-iam-role-for-ec2.html) to prepare this role based on your application's need to interact with other AWS services. The following additional permissions may be required for Data Observability: Jobs Monitoring.

#### Permissions to get secret value using AWS Secrets Manager{% #permissions-to-get-secret-value-using-aws-secrets-manager %}

{% alert level="danger" %}
These permissions are **required** if you are using AWS Secrets Manager.
{% /alert %}

1. In your [AWS IAM console](https://console.aws.amazon.com/iam/), click on **Access management** > **Roles** in the left navigation bar.
1. Click on the IAM role you plan to use as the instance profile for your EMR cluster.
1. On the next page, under the **Permissions** tab, find the **Permissions policies** section. Click on **Add permissions** > **Create inline policy**.
1. On the **Specify permissions** page, find the **Select a service** section. Under **Service**, select **Secrets Manager**.
   {% image
      source="https://datadog-docs.imgix.net/images/data_jobs/emr/specify_permissions.84b562581db9791c8e9257147ecdf287.png?auto=format"
      alt="AWS IAM console, Specify Permissions page." /%}

   - Then, under **Actions allowed**, select `GetSecretValue`. This is a **Read** action.
   - Under **Resources**, select **Specific**. Then, next to **Secret**, click on **Add ARNs** and add the ARN of the secret you created in the first step on this page.
   - Click **Next**.
1. On the next page, give your policy a name. Then, click **Create policy**.

#### Permissions to describe cluster{% #permissions-to-describe-cluster %}

{% alert level="danger" %}
These permissions are **required** if you are **NOT** using the default role, `EMR_EC2_DefaultRole`.
{% /alert %}

1. In your [AWS IAM console](https://console.aws.amazon.com/iam/), click on **Access management** > **Roles** in the left navigation bar.
1. Click on the IAM role you plan to use as the instance profile for your EMR cluster.
1. On the next page, under the **Permissions** tab, find the **Permissions policies** section. Click on **Add permissions** > **Create inline policy**.
1. On the **Specify permissions** page, toggle on the **JSON** tab.
   - Then, copy and paste the following policy into the **Policy editor**

   ```json
   {
      "Version": "2012-10-17",
      "Statement": [
         {
            "Effect": "Allow",
            "Action": [
               "elasticmapreduce:ListBootstrapActions",
               "elasticmapreduce:ListInstanceFleets",
               "elasticmapreduce:DescribeCluster",
               "elasticmapreduce:ListInstanceGroups"
            ],
            "Resource": [
               "*"
            ]
         }
      ]
   }
   ```

   - Click **Next**.
1. On the next page, give your policy a name. Then, click **Create policy**.

Take note of the name of the IAM role you plan to use as the instance profile for your EMR cluster.

### Create and configure your EMR cluster{% #create-and-configure-your-emr-cluster %}

When you create a new EMR cluster in the [Amazon EMR console](https://console.aws.amazon.com/emr), add a bootstrap action on the **Create Cluster** page:

1. Save the following script to an S3 bucket that your EMR cluster can read. Take note of the path to this script.

   ```shell
   #!/bin/bash

   # Set required parameter DD_SITE
   export DD_SITE=<YOUR_DATADOG_SITE>

   # Set required parameter DD_API_KEY with Datadog API key.
   # The commands below assumes the API key is stored in AWS Secrets Manager, with the secret name as datadog/dd_api_key and the key as dd_api_key.
   # IMPORTANT: Modify if you choose to manage and retrieve your secret differently.
   SECRET_NAME=datadog/dd_api_key
   export DD_API_KEY=$(aws secretsmanager get-secret-value --secret-id $SECRET_NAME | jq -r .SecretString | jq -r '.["dd_api_key"]')

   # Optional: uncomment to send spark driver and worker logs to Datadog
   # export DD_EMR_LOGS_ENABLED=true

   # Download and run the latest init script
   curl -L https://install.datadoghq.com/scripts/install-emr.sh > djm-install-script; bash djm-install-script || true
   ```

Optionally, the script can be configured adding the following environment variables: The script above sets the required parameters, and downloads and runs the latest init script for Data Observability: Jobs Monitoring in EMR. If you want to pin your script to a specific version, you can replace the filename in the URL with `install-emr-0.13.5.sh` to use version `0.13.5`, for example. The source code used to generate this script, and the changes between script versions can be found on the [Datadog Agent repository](https://github.com/DataDog/datadog-agent/blob/main/pkg/fleet/installer/setup/djm/emr.go).

Optionally, the script can be configured by adding the following environment variables:

| Variable                        | Description                                                                                                                                                                                                                          | Default |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------- |
| DD_TAGS                         | Add tags to EMR cluster and Spark performance metrics. Comma or space separated key:value pairs. Follow [Datadog tag conventions](https://docs.datadoghq.com/getting_started/tagging/). Example: `env:staging,team:data_engineering` |
| DD_ENV                          | Set the `env` environment tag on metrics, traces, and logs from this cluster.                                                                                                                                                        |
| DD_EMR_LOGS_ENABLED             | Send Spark driver and worker logs to Datadog.                                                                                                                                                                                        | false   |
| DD_LOGS_CONFIG_PROCESSING_RULES | Filter the logs collected with processing rules. See [Advanced Log Collection](https://docs.datadoghq.com/agent/logs/advanced_log_collection/?tab=environmentvariable#global-processing-rules) for more details.                     |

1. On the **Create Cluster** page, find the **Bootstrap actions** section. Click **Add** to bring up the **Add bootstrap action** dialog.

   {% image
      source="https://datadog-docs.imgix.net/images/data_jobs/emr/add_bootstrap_action_without_arguments.a3a6d8ab8ed6f4de697453d7a195f852.png?auto=format"
      alt="Amazon EMR console, Create Cluster, Add Bootstrap Action dialog. Text fields for name, script location, and arguments." /%}



   - For **Name**, give your bootstrap action a name. You can use `datadog_agent`.
   - For **Script location**, enter the path to where you stored the init script in S3.
   - Click **Add bootstrap action**.

1. On the **Create Cluster** page, find the **Identity and Access Management (IAM) roles** section. For **instance profile** dropdown, select the IAM role you have granted permissions in Grant permissions to EMR EC2 instance profile.

When your cluster is created, this bootstrap action installs the Datadog Agent and downloads the Java tracer on each node of the cluster.

### Specify service tagging per Spark application{% #specify-service-tagging-per-spark-application %}

Tagging enables you to better filter, aggregate, and compare your telemetry in Datadog. You can configure tags by passing `-Ddd.service`, `-Ddd.env`, `-Ddd.version`, and `-Ddd.tags` options to your Spark driver and executor `extraJavaOptions` properties.

In Datadog, each job's name corresponds to the value you set for `-Ddd.service`.

```shell
spark-submit \
 --conf spark.driver.extraJavaOptions="-Ddd.service=<JOB_NAME> -Ddd.env=<ENV> -Ddd.version=<VERSION> -Ddd.tags=<KEY_1>:<VALUE_1>,<KEY_2:VALUE_2>" \
 --conf spark.executor.extraJavaOptions="-Ddd.service=<JOB_NAME> -Ddd.env=<ENV> -Ddd.version=<VERSION> -Ddd.tags=<KEY_1>:<VALUE_1>,<KEY_2:VALUE_2>" \
 application.jar
```

## Validation{% #validation %}

In Datadog, view the [Data Observability: Jobs Monitoring](https://app.datadoghq.com/data-jobs/) page to see a list of all your data processing jobs.

## Troubleshooting{% #troubleshooting %}

If you don't see any data in DJM after installing the product, follow these steps.

The init script installs the Datadog Agent. To make sure it is properly installed, ssh into the cluster and run the Agent status command:

```shell
sudo datadog-agent status
```

## Advanced Configuration{% #advanced-configuration %}

### Tag spans at runtime{% #tag-spans-at-runtime %}

You can set tags on Spark spans at runtime. These tags are applied *only* to spans that start after the tag is added.

```scala
// Add tag for all next Spark computations
sparkContext.setLocalProperty("spark.datadog.tags.key", "value")
spark.read.parquet(...)
```

To remove a runtime tag:

```scala
// Remove tag for all next Spark computations
sparkContext.setLocalProperty("spark.datadog.tags.key", null)
```

## Further Reading{% #further-reading %}

- [Data Observability: Jobs Monitoring](https://docs.datadoghq.com/data_jobs)
