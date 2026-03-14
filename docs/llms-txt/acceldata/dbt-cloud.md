# Source: https://docs.acceldata.io/documentation/dbt-cloud.md

# dbt Cloud

**dbt Cloud** is a managed platform for orchestrating and monitoring DBT projects. The DBT Cloud connector in the ADOC platform enables seamless integration with your DBT projects. By onboarding this connector, you can automatically ingest DBT metadata—such as models, tests, and lineage—into ADOC. This enhances visibility into data transformations and improves the accuracy of data reliability metrics.

This integration empowers data teams to govern and monitor DBT-managed assets more effectively within a unified observability layer.

## Prerequisites 

Before setting up the dbt Cloud connector, ensure you have the following:

- A **dbt** **Cloud account** with an active project
- A **dbt** **Cloud Access Token** to retrieve run history and metadata
- The **dbt** **Cloud URL**, **Account ID**, and **Auth Token**

## 1. Create dbt Cloud Project

To create a sample dbt Cloud project:

1. Log in to your dbt Cloud account**.**
2. From the dashboard, click **New Project**.
3. Select **Build a sample project** when prompted for the project type.
4. Configure your sample project:
    1. Choose the **Sample Managed Project** template.
    2. Select your data warehouse (e.g., `Snowflake_test`).
    3. Enter your warehouse credentials.

5. Set up project details:
    1. Provide a name for your project.
    2. Configure the development environment settings.
    3. Set up the repository connection (DBT Cloud will create a managed repository).

6. DBT Cloud initializes your project with sample models, tests, and documentation.
7. Explore the project:
    1. Navigate to the **Develop** tab.
    2. Review the sample models, schema files, and documentation.

8. Run your first command: In the development environment, run `dbt run` to execute the sample models.
9. Set up a deployment environment:
    1. Configure environments for staging.
    2. In connections, select `Snowflake_test`.

## 2. Create New Job in dbt Cloud Job

To create and configure a job:

1. Navigate to the **Jobs** section.
2. Select your project.
3. Click **+ Create Job** or **New Job**.
4. Configure the job:
    1. Provide a descriptive name (e.g., `manual`).
    2. Select the environment created earlier.
    3. Choose the DBT version to use.
    4. Set the commands to run (e.g., `dbt run`, `dbt test`, `dbt docs generate`).

5. Save the job.
6. To trigger the job manually, go to the job’s details page and click **Run Now**.

## 3. Generate Access token for dbt Cloud

ADOC requires a dbt Cloud access token to retrieve run history and metadata. To generate one:

1. In dbt Cloud, go to **Account Settings**.
2. Click **API Tokens &gt; Service Tokens**.
3. Generate a new token.
4. Assign the token **Job Viewer** permissions.

## 4. Setup dbt Cloud as a Data Source in ADOC

The dbt Cloud connector uses a **pull-based mechanism** to retrieve metadata regularly from your DBT Cloud account.

To configure the connector:

1. In ADOC, navigate to **Register** -&gt; **Add Data Source** -&gt; Select **dbt Cloud**.
2. Provide a name and description for the data source.
3. Ensure the **Data Reliability** toggle is enabled and choose a **Data Plane**.
4. Enter the required dbt connection details.
5. Click **Test Connection**, then **Submit**.

Once the data source is created, ADOC will begin regularly pulling metadata from dbt Cloud.

To view the ingested data, navigate to the **Pipelines** page on the ADOC platform to see dbt Cloud run information.