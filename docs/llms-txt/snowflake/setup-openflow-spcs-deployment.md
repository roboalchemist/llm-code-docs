# Source: https://docs.snowflake.com/en/user-guide/data-integration/openflow/setup-openflow-spcs-deployment.md

# Set up Openflow - Snowflake Deployment: Create deployment

After configuring core Snowflake, create an Openflow deployment. A deployment is the
control plane component that manages your runtimes and connectors. Each deployment can host
multiple runtimes, and each runtime can run multiple connectors, giving you flexibility to
isolate workloads by project, team, or environment. There is no separate charge for the
deployment itself; only active runtimes consume Snowflake credits.

1. Create a deployment - create the deployment itself.
2. [Optional] Configure an Openflow-specific event table - configure an Openflow-specific event table to store Openflow logs and metrics.

## Create a deployment

> **Note:**
>
> To access the Openflow Runtime UI using PrivateLink as described in [Setup PrivateLink UI access](setup-openflow-spcs-configure-pr-ui.md),
> ensure the **PrivateLink** option is enabled when creating a new Openflow - Snowflake Deployment.

1. Sign in to [Snowsight](../../ui-snowsight-gs.md) with a role defined in [Configure core Snowflake requirements](setup-openflow-spcs-sf.md).
2. In the navigation menu, select Ingestion » Openflow.
3. Select Launch Openflow.
4. In the Openflow UI, select Create a deployment. The Deployments tab opens.
5. Select Create a deployment. The Creating a deployment wizard opens.
6. In the Prerequisites step, ensure that you meet all the requirements. Select Next.
7. In the Deployment location step, select Snowflake as the deployment location.
   Enter a name for your deployment. Select Next.
8. Select Create Deployment.

Your deployment will then be created.

## [Optional] Configure an Openflow-specific event table

Openflow generates logs and metrics and sends them to the Snowflake Event Table.
For helpful queries to analyze this telemetry data, see [Monitor Openflow](monitor.md).

By default, Openflow uses the [account event table](../../../developer-guide/logging-tracing/event-table-setting-up.md) (SNOWFLAKE.TELEMETRY.EVENTS), but you can configure an Openflow-specific event table per deployment. A dedicated event table is recommended to optimize query performance, enable granular access control, and simplify Openflow monitoring and maintenance.

1. To store the event table outside the Openflow database, grant the OPENFLOW_ADMIN role
   access to the `<DATABASE>` and `<SCHEMA>` where you want to store it:

   ```sqlexample
   USE ROLE ACCOUNTADMIN;

   GRANT USAGE ON DATABASE <DATABASE> TO ROLE OPENFLOW_ADMIN;
   GRANT USAGE ON SCHEMA <DATABASE>.<SCHEMA> TO ROLE OPENFLOW_ADMIN;
   ```

2. Create the event table:

   ```sqlexample
   USE ROLE OPENFLOW_ADMIN;

   CREATE EVENT TABLE IF NOT EXISTS <DATABASE>.<SCHEMA>.EVENTS;
   ```

3. Get your dataplane name, which you use in the next step, from the `name` column:

   ```sqlexample
   SHOW OPENFLOW DATA PLANE INTEGRATIONS;
   ```

4. Set the event table for this deployment, replacing `<OPENFLOW_DATAPLANE_NAME>` with the value from the previous step:

   ```sqlexample
   ALTER OPENFLOW DATA PLANE INTEGRATION <OPENFLOW_DATAPLANE_NAME>
     SET EVENT_TABLE = '<DATABASE>.<SCHEMA>.EVENTS';
   ```

## [Optional] Create a monitoring role

A monitoring role lets data engineers or operations teams monitor Openflow without having the OPENFLOW_ADMIN role.

* To create a monitoring role, run the following code:

  ```sqlexample
  USE ROLE OPENFLOW_ADMIN;

  -- Create a role for monitoring Openflow deployments and runtimes if it doesn't yet exist
  CREATE ROLE IF NOT EXISTS <OPENFLOW_MONITOR_ROLE>;

  GRANT MONITOR ON OPENFLOW DATA PLANE INTEGRATION <OPENFLOW_DATAPLANE_NAME> TO ROLE <OPENFLOW_MONITOR_ROLE>;

  -- Add to role hierarchy so administrators can manage objects owned by this role
  GRANT ROLE <OPENFLOW_MONITOR_ROLE> TO ROLE <OPENFLOW_ADMIN_ROLE>;

  -- Grant the role to the appropriate Snowflake users
  GRANT ROLE <OPENFLOW_MONITOR_ROLE> TO USER <SNOWFLAKE_USER>;
  ```

### Next steps

[Create Snowflake role](setup-openflow-spcs-create-rr.md)
