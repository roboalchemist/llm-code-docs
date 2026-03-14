# Source: https://docs.acceldata.io/documentation/snaplogic.md

# SnapLogic

SnapLogic is an iPaaS (Integration Platform as a Service) platform used to build, orchestrate, and run data pipelines across cloud and on-prem systems. ADOC integrates natively with SnapLogic to provide visibility into pipeline executions, operational health, failures, and logs directly within the ADOC Pipelines module.

Once integrated, ADOC automatically discovers SnapLogic pipelines and enables monitoring, alerting, and policy-driven observability for ELT workflows.

## Prerequisites

Before adding SnapLogic as a data source in ADOC, ensure the following requirements are met:

- A **running ADOC Data Plane** deployed in the customer environment
- Access to a **SnapLogic account** with sufficient privileges to read pipeline execution metadata
    - Read access to pipeline executions, logs, and project metadata is required

- (Optional) Knowledge of SnapLogic **project paths** if you want to restrict pipeline discovery

## Adding SnapLogic as a Data Source

To add SnapLogic as a data source in ADOC:

1. Navigate to **Register** from the main left navigation menu.
2. Click **Add Data Source**.
3. Select **SnapLogic** from the list of available data sources.
4. Provide the SnapLogic account details:
    - SnapLogic endpoint URL
    - Account credentials with required read access

5. (Optional) Specify a **Project Path**:
    - If a project path is provided, ADOC discovers and monitors only pipelines under that path.
    - If no project path is provided, ADOC automatically discovers all pipelines in the account.

6. Click **Submit** to complete onboarding. Once configured, the data source is added to the list of data sources on Data Sources tab.

## Pipeline Discovery Behavior

- SnapLogic pipelines are **automatically discovered** when they are executed after onboarding.
- Only pipelines that run after the integration is added are discovered.
- Discovery is based on execution metadata received from SnapLogic APIs via the data plane.

## What You Can Do After Adding SnapLogic

After SnapLogic is added as a data source, users can:

- View SnapLogic pipelines in the **Pipelines** module
- Monitor pipeline execution states:
    - Running
    - Completed
    - Failed

- Inspect pipeline execution details, including:
    - Execution duration
    - Spans and events
    - Error messages and logs (when available)

- Track historical pipeline runs for operational analysis
- Configure **monitoring and reliability policies** based on pipeline outcomes (for example, pipeline duration or failure conditions)

This provides end-to-end visibility into SnapLogic pipeline health without requiring users to leave ADOC.

## Next Steps

Once SnapLogic is successfully integrated, navigate to the [Pipelines](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/pipelines) page to view and monitor SnapLogic pipelines.