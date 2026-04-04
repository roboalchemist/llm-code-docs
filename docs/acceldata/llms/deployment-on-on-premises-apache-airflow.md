# Source: https://docs.acceldata.io/documentation/deployment-on-on-premises-apache-airflow.md

# Deployment on On-Premises Apache Airflow

To deploy the plugin on an on-premises instance of Apache Airflow, perform the following:

### 1. Setup Environment Variables

Configure the required and optional environment variables for the plugin. For a detailed list of these variables and their descriptions, refer to the [configuration](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/observing-airflow-dags-with-adoc-listener-plugin#configuration) section.

### 2. Verify Airflow Version

Verify that the Airflow environment where you plan to deploy the plugin is running version 2.5.0 or later. You can check the version by running:

```bash
airflow version
```



Confirm if the output version is  `2.5.0` or higher, such as `2.5.3`.

### 3. Install Required Packages

Install the following package on all Airflow components: **adoc_airflow_plugin**.

Use the appropriate package manager or installation method for your environment to install this dependency.

### 4. Restart Airflow Components

Restart all Airflow components to apply the plugin changes.

### 5. Validate the Plugin Installation

Navigate to **Admin &gt; Plugins** in your Airflow UI. Confirm that the `AcceldataListenerPlugin` is listed correctly, indicating successful installation.

### 6. Verify Instrumentation

Once the plugin is installed and the environment is configured, execute a DAG in your Airflow instance. After the DAG run is complete, go to **ADOC UI &gt; Pipelines** to verify successful instrumentation. Find the pipeline matching your DAG's name; it should appear with its associated spans and events, as shown in the screenshot below.

![](https://uploads.developerhub.io/prod/Yoq2/durfl3zeb9bo87ju48ef6yp5j09fksy891zb6lfuq35buq2qkhj0ax9k0b3d0tvq.png)