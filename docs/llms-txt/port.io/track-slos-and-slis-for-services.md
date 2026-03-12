# Source: https://docs.port.io/guides/all/track-slos-and-slis-for-services.md

# Track SLOs and SLIs for your services

This guide helps you set up a monitoring solution to track **Service Level Indicators (SLIs)** and compare them against **Service Level Objectives (SLOs)** using Port's integration with **New Relic**.

## Common use cases[â](#common-use-cases "Direct link to Common use cases")

* Model and visualize service **SLIs** and compare them against **SLOs**.
* Create dashboards and reports to monitor SLOs over time.

## Prerequisites[â](#prerequisites "Direct link to Prerequisites")

This guide assumes the following:

* You have a Port account and have completed the [onboarding process](https://docs.port.io/getting-started/overview).
* You have [installed and set up Port's New Relic integration](https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/apm-alerting/newrelic).

## Set up data model[â](#set-up-data-model "Direct link to Set up data model")

In this setup, we will create or update the `New Relic Service Level` blueprint.<br />**Skip** to [update blueprint](#update-the-blueprint) if you already have the blueprint.

### Create the blueprint[â](#create-the-blueprint "Direct link to Create the blueprint")

Follow the steps below to **create** the `New Relic Service Level` blueprint:

1. Go to the [Builder](https://app.getport.io/settings/data-model) in your Port portal.

2. Click on "+ Blueprint".

3. Click on the `{...}` button in the top right corner, and choose "Edit JSON".

4. Add this JSON schema:

   **New Relic Service Level blueprint (Click to expand)**

   Create in Port

   ```
   {
     "identifier": "newRelicServiceLevel",
     "description": "This blueprint represents a New Relic Service Level",
     "title": "New Relic Service Level",
     "icon": "NewRelic",
     "schema": {
       "properties": {
         "description": {
           "title": "Description",
           "type": "string"
         },
         "targetThreshold": {
           "icon": "DefaultProperty",
           "title": "Target Threshold",
           "type": "number"
         },
         "createdAt": {
           "title": "Created At",
           "type": "string",
           "format": "date-time"
         },
         "updatedAt": {
           "title": "Updated At",
           "type": "string",
           "format": "date-time"
         },
         "createdBy": {
           "title": "Creator",
           "type": "string",
           "format": "user"
         },
         "sli": {
           "type": "number",
           "title": "SLI"
         },
         "tags": {
           "type": "object",
           "title": "Tags"
         }
       },
       "required": []
     },
     "mirrorProperties": {
       "running_service_identifier": {
         "title": "runningServiceIdentifier",
         "path": "newRelicService.$identifier"
       },
       "domain": {
         "title": "Domain",
         "path": "newRelicService.domain"
       }
     },
     "calculationProperties": {
       "sloStatus": {
         "title": "SLO Status",
         "calculation": "if .properties.sli >= .properties.targetThreshold then \"Passed\" else \"Failed\" end",
         "type": "string",
         "colorized": true,
         "colors": {
           "Passed": "green",
           "Failed": "red"
         }
       }
     },
     "aggregationProperties": {},
     "relations": {
       "newRelicService": {
         "title": "New Relic service",
         "target": "newRelicService",
         "required": false,
         "many": false
       }
     }
   }
   ```

5. Click "Save" to create the blueprint.

### Update the blueprint[â](#update-the-blueprint "Direct link to Update the blueprint")

Follow the steps below to **update** the `New Relic Service Level` blueprint:

1. Navigate to the `New Relic Service Level` blueprint in your Port [Builder](https://app.getport.io/settings/data-model).

2. Hover over it, click on the `...` button on the right, and select "Edit JSON".

3. Add the calculation property:

   **Calculation property (Click to expand)**

   ```
   "sloStatus": {
     "title": "SLO Status",
     "calculation": "if .properties.sli >= .properties.targetThreshold then \"Passed\" else \"Failed\" end",
     "type": "string",
     "colorized": true,
     "colors": {
       "Passed": "green",
       "Failed": "red"
     }
   }
   ```

4. Add these mirror properties:

   **Mirror properties (Click to expand)**

   ```
   "running_service_identifier": {
     "title": "runningServiceIdentifier",
     "path": "newRelicService.$identifier"
   },
   "domain": {
     "title": "Domain",
     "path": "newRelicService.domain"
   }
   ```

## Visualize metrics[â](#visualize-metrics "Direct link to Visualize metrics")

In this section, you'll learn how to create dashboards that visualize key service metrics using SLIs and SLOs for production and engineering teams.

### Create a dashboard[â](#create-a-dashboard "Direct link to Create a dashboard")

1. Navigate to your [software catalog](https://app.getport.io/organization/catalog).
2. Click on the **`+ New`** button in the left sidebar.
3. Select **New dashboard**.
4. Name the dashboard **Production Deployment Overview** and click `Create`.
5. Repeat the same process to create an **Engineering Overview** dashboard.

You now have a blank dashboard where you can start adding widgets to visualize your SLIs and SLOs.

### Add widgets[â](#add-widgets "Direct link to Add widgets")

**Production Deployment Overview - SLI vs SLO Table**

1. Click **`+ Widget`** and select **Table**.

2. Title the widget **Service Level Performance Overview**.

3. Choose the **New Relic Service Level** blueprint.

   ![](/img/guides/sliVsSloTable.png)

4. Click **Save**.

5. Click on the **`...`** button in the top right corner of the table and select **Customize table**.

6. In the top right corner of the table, click on `Manage Properties` button and add the following properties:

   * **Running service identifier**
   * **Target threshold**
   * **SLI**
   * **SLO Status**

7. Click on the **save icon** on the far right top conner of the widget to save the state of the table.

This table gives you a high-level overview of how your services are performing against their SLOs.

**Engineering Overview - Failed SLOs Table**

1. Click **`+ Widget`** and select **Table**.

2. Title the widget **Domain Performance & SLO Failures**.

3. Choose the **New Relic Service Level** blueprint.

   ![](/img/guides/failedSloTable.png)

4. Click **Save**.

5. Click on the **`...`** button in the top right corner of the table and select **Customize table**.

6. Group the table by **Domain**.

7. Apply a filter to display only the **Failed** SLOs.

### Visualize SLI trends[â](#visualize-sli-trends "Direct link to Visualize SLI trends")

Tracking weekly performance trends for key services is crucial to identifying patterns and making data-driven decisions.

**Weekly Latency Trend for API Gateway**

1. Click **`+ Widget`** and select **Line Chart**.
2. Title the chart **API Gateway Weekly Latency Trend**.
3. Choose the **New Relic Service Level** blueprint.
4. Select the **Target Threshold** and **SLI** properties to compare actual latency with the target.
5. Set the time interval to **Week**.
6. Click **Save**.

**Weekly Write Failure Trend for Main Database**

1. Click **`+ Widget`** and select **Line Chart**.
2. Title the chart **Main Database Weekly Write Failure Trend**.
3. Choose the **New Relic Service Level** blueprint.
4. Select the **Target Threshold** and **SLI** properties to track write failures.
5. Set the time interval to **Week**.
6. Click **Save**.

**Weekly Transaction Volume for Payment Processing**

1. Click **`+ Widget`** and select **Line Chart**.
2. Title the chart **Payment Processing Weekly Transaction Volume Trend**.
3. Choose the **New Relic Service Level** blueprint.
4. Select the **Target Threshold** and **SLI** properties to track transaction volumes.
5. Set the time interval to **Week**.
6. Click **Save**.

#### Team-Level and Organization-Level dashboards[â](#team-level-and-organization-level-dashboards "Direct link to Team-Level and Organization-Level dashboards")

You can also create dashboards specific to teams or organization-wide, depending on the scope of monitoring.

1. First, add the following properties to the New Relic Service blueprint:

**Calculation and aggregation properties**

```
"calculationProperties": {
    "has_slo": {
      "title": "Has SLO",
      "icon": "DefaultProperty",
      "description": "Boolean for if SLO exists",
      "calculation": ".properties.number_of_slos != null",
      "type": "boolean"
    }
  },
  "aggregationProperties": {
    "number_of_slos": {
      "title": "Number of SLOs",
      "icon": "DefaultProperty",
      "type": "number",
      "target": "newRelicServiceLevel",
      "calculationSpec": {
        "func": "count",
        "calculationBy": "entities"
      }
    }
```

2. Add the dashboards

**Create My Teamâs SLOs Dashboard (Team Lead View)**

1. Click **`+ New`** in the sidebar to create a new dashboard.
2. Name the dashboard **My Teamâs SLOs**.

**Create Organization SLOs Dashboard (SRE View)**

1. Click **`+ New`** in the sidebar to create a new dashboard.
2. Name the dashboard **Organization SLOs**.

#### SLO tables and charts[â](#slo-tables-and-charts "Direct link to SLO tables and charts")

**All SLOs Table**

1. Click **`+ Widget`** and select **Table**.
2. Title the widget **All SLOs**.
3. Select the **New Relic Service Level** blueprint.
4. ![](/img/guides/allSloTable.png)

4.Click **Save**.

**SLO Status Pie Chart**

1. Click **`+ Widget`** and select **Pie Chart**.

2. Title the chart **SLO Status**.

3. Choose the **New Relic Service Level** blueprint.

4. Select the **SLO Status** property as `Breakdown by Property` value

   ![](/img/guides/sloStatusPieChart.png)

5. Click **Save**.

**Services with a Defined SLO Pie Chart**

1. Click **`+ Widget`** and select **Pie Chart**.

2. Title the chart **Services with a Defined SLO**.

3. Choose the **New Relic Service** blueprint.

4. Select the **Has SLO** property as `Breakdown by Property` for ser

   ![](/img/guides/hasSloPieChart.png)

5. Click **Save**.

**Latency SLI Chart**

1. Click **`+ Widget`** and select **Line Chart**.

2. Title the chart **Latency SLI**.

3. Choose the **New Relic Service Level** blueprint.

4. Choose an `Entity`

5. Select the **SLI** and **Target Threshold** as `Properties`.

6. Set the time interval to **Day** and the time range to **in the past 90 days**.

   ![](/img/guides/latencySliChart.png)

7. Click **Save**.

**Success SLI Chart**

1. Click **`+ Widget`** and select **Line Chart**.

2. Title the chart **Success SLI**.

3. Choose the **New Relic Service Level** blueprint.

4. Choose an `Entity`

5. Select the **SLI** and **Target Threshold** as `Properties`.

6. Set the time interval to **Day** and the time range to **in the past 90 days**.

   ![](/img/guides/successSliChart.png)

7. Click **Save**.

Team and organization level

You can use the above steps for both team and an organization level dashboard.

![](/img/guides/sloDBVisualization.png)

<br />

<br />

By following this guide, you have successfully set up dashboards to track your services' SLIs and SLOs. These visualizations provide real-time insights into service performance and compliance, allowing your teams to quickly identify and address underperforming services.
