# Source: https://docs.acceldata.io/documentation/observing-airflow-dags-with-adoc-listener-plugin.md

# Observing Airflow DAGs with ADOC Listener Plugin

The ADOC Listener plugin integrates Airflow `DAGs` for automatic observation in `ADOC`.

The plugin performs the following actions without requiring any additional code in your Airflow DAG, unless you disable instrumentation through environment variables.

1. **When the DAG starts**:
    1. It creates the pipeline if it does not already exist in ADOC.
    2. It creates a new pipeline run in ADOC.

2. **When a TaskInstance starts**:
    1. It creates jobs in ADOC for each of the airflow operators used in the task.
    2. It constructs job input nodes based on the upstream tasks.
    3. It creates a span and associates it with the jobs.
    4. It emits span events with metadata.

3. **When a TaskInstance is completed**:
    1. It emits span events with metadata.
    2. It ends the spans with either success or failure.

4. **When the DAG is completed**:
    1. It updates the pipeline run with success or failure in ADOC.

## Prerequisites

Ensure to have the following applications installed in your system:

- Python V3.6.0 and above [[Download Python](https://www.python.org/downloads)]
- Airflow V2.3.0 and above [[Apache Airflow](https://pypi.org/project/apache-airflow)]

API keys are essential for authentication when making calls to ADOC.

![](https://uploads.developerhub.io/prod/Yoq2/zygy3wmlb9dddrnx8g7jhbkc8wuqn9wwaooksj4boerwj4w8k1u1ukaepmgfxdpw.png)

## Configuration

### Plugin Environment Variables

The `adoc_listener_plugin` utilizes the `acceldata-sdk` to push data to the ADOC backend.

**Mandatory Environment Variables**

The ADOC client relies on the following environment variables:

- `TORCH_CATALOG_URL`: The URL of the ADOC server.
- `TORCH_ACCESS_KEY`: The API access key generated from the ADOC UI.
- `TORCH_SECRET_KEY`: The API secret key generated from the ADOC UI.

**Optional Environment Variables for v4.8.4 and above**

| **Environment Variable** | **Description** | **Default** | 
| ---- | ---- | ---- | 
| `TORCH_CONNECTION_TIMEOUT_MS` | Maximum time (in milliseconds) to wait while establishing a connection to the ADOC server. | `5000 ms` | 
| `TORCH_READ_TIMEOUT_MS` | Maximum time (in milliseconds) to wait for a response from the ADOC server after a successful connection. | `15000 ms` | 


Example:

```json
export TORCH_CONNECTION_TIMEOUT_MS=10000
export TORCH_READ_TIMEOUT_MS=20000
```



**Optional Environment Variables**

By default, all DAGs are observed. However, the following set of environment variables can be used to modify this behavior. 

> The environment variables for ignoring or observing DAGs are mutually exclusive.

If the following environment variables match with the DAG ids, the observation of the matched DAG ids will be ignored, while all other DAG ids are still observed:

- `DAGIDS_TO_IGNORE`: Comma-separated DAG ids to ignore observation.
- `DAGIDS_REGEX_TO_IGNORE`: Regular expression for DAG ids to ignore observation.

If the following environment variables match with the DAG ids, only the observation of those specific DAG ids will be observed, while all other DAG ids will be ignored:

- `DAGIDS_TO_OBSERVE`: Comma-separated dag ids to observe.
- `DAGIDS_REGEX_TO_OBSERVE`: Regular expression for DAG ids to observe.

## Deployment

- To deploy the plugin on an on-premise instance of Apache Airflow, refer [Deployment on On-Premises Apache Airflow](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/deployment-on-on-premises-apache-airflow).
- To deploy the plugin on Amazon MWAA, refer [Deployment on Amazon MWAA](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/deployment-on-amazon-mwaa).
- To deploy the plugin on Google Cloud Composer, refer [Deployment on Google Cloud Composer](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/deployment-on-google-cloud-composer).

## Enhance Data Reliability with Automated Data Reliability

Consider [Automated Data Reliability](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/observing-airflow-dags-with-adoc-listener-plugin#enhance-data-reliability-with-automated-data-reliability), which complements this plugin integration by enhancing data reliability and observability without requiring modifications to the pipeline code.

## Ways to Observe your DAGs in ADOC

You can observe your pipelines created with Airflow DAGs in ADOC using the following three methods:

1. **Full Code**: In the full code approach, the **Airflow Listener Integration** is not used to observe our DAGs. If you are using the Airflow Listener Integration, you must disregard automated observation for these DAGs, as explained in the [configuration](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/observing-airflow-dags-with-adoc-listener-plugin#configuration) section.
    1. Switching to asset lineage would involve excluding this DAG from the integration and adding complete observability for it.
    2. If you intend to connect multiple DAGs using the `continuation_id` logic, make sure to disable DAG observation in the configuration when using the listener plugin integration. This is crucial as the integration will conclude the pipeline run upon the termination of the DAG run.

Examples demonstrating the full code  approach can be referred [here](https://bitbucket.org/acceldata/ad-pipelines-integ-example/src/master/airflow/full_code/).

2. **Light Code**: In the Light Code approach, you should utilize the **Airflow Listener Integration**  while having the flexibility to enhance the code beyond what the plugin offers. This can involve:
    1. Sending additional span events for the task. You can find an example demonstrating this use case for reference [here](https://bitbucket.org/acceldata/ad-pipelines-integ-example/src/master/airflow/light_code/06example/).
    2. Invoking policies for the DAG. For examples, refer the following:
        1. [Example with Torch Client](https://bitbucket.org/acceldata/ad-pipelines-integ-example/src/master/airflow/light_code/07example/)
        2. [Example with ExecutePolicyOperator](https://bitbucket.org/acceldata/ad-pipelines-integ-example/src/master/airflow/light_code/08example/)

3. **No Code**: In the No Code approach, you should utilize the  **Airflow Listener Integration** exclusively. An example demonstrating how to observe your DAG, along with its corresponding pipeline, spans, and events, without requiring any additional code can be referred [here](https://bitbucket.org/acceldata/ad-pipelines-integ-example/src/master/airflow/no_code/).