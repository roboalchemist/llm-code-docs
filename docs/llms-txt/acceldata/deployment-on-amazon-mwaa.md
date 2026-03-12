# Source: https://docs.acceldata.io/documentation/deployment-on-amazon-mwaa.md

# Deployment on Amazon MWAA

To deploy the plugin on Managed Workflows for Apache Airflow (MWAA), perform the following:

### 1. Setup Environment Variables

Configure the necessary environment variables within your MWAA environment. For a detailed list of required variables and their values, refer the [configuration](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/observing-airflow-dags-with-adoc-listener-plugin#configuration) section.

### 2. Create Plugins.zip File

Package the environment variables into a `plugins.zip` file. For instructions on creating a custom plugin that generates runtime environment variables, refer [Creating a custom plugin that generates runtime environment variables - Amazon Managed Workflows for Apache Airflow](https://docs.aws.amazon.com/mwaa/latest/userguide/samples-env-variables.html).

The following screenshot is a sample `env_var_plugin.py` file for your reference:

![](https://uploads.developerhub.io/prod/Yoq2/5beq4l3m5la6jhv4bf1dm0o36eeynaw30uqbnz93bze1zz23cyt0ydeirq9twc94.png)

You can either hardcode the environment variables directly in the file or use AWS Secrets Manager to securely store them and configure the `plugins.zip` file to read from Secrets Manager.

### 3. Install Required Packages

- **Check for** `requirements.txt`: Inspect your DAG code folder in the Amazon S3 bucket to see if a `requirements.txt` file is already present.
    - **If** `requirements.txt` does not exist:
        - Upload a new `requirements.txt` file that includes the latest versions of the `adoc_airflow_plugin` package.

    - **If** `requirements.txt` exists:
        - Verify that it includes the `adoc_airflow_plugin` packages. If they are not listed, update the file to include their latest versions.

### 4. Update Airflow Environment Packages

Point your MWAA environment to the updated versions of the `plugins.zip` and `requirements.txt` files. Apply these changes in the MWAA console to ensure the updated configurations are loaded correctly.

### 5. Validate the Plugin Installation

Navigate to **Admin &gt; Plugins** in your Airflow UI. Ensure that both `AcceldataListenerPlugin` and `env_var_plugin` are listed, confirming successful installation.

### 6. Verify Instrumentation

After installing the plugin and configuring the environment, trigger a DAG in your Airflow instance. Once the DAG run is complete, navigate to **ADOC UI &gt; Pipelines** to confirm successful instrumentation. Locate the pipeline corresponding to your DAG’s name; it should be displayed with its associated spans and events, as shown in the screenshot below.

![](https://uploads.developerhub.io/prod/Yoq2/a7ti8tplm0n0apwlq0jbn7sexxli8sjhfdea0ql3ebb8lgcvwlxfslr4ajyaikes.png)