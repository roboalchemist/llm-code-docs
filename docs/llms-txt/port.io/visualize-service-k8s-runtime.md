# Source: https://docs.port.io/guides/all/visualize-service-k8s-runtime.md

# Visualize your services' k8s runtime

Portâs Kubernetes integration helps you model and visualize your clusterâs workloads alongside your existing workloads in Port. This guide will help you set up the integration and visualize your services' Kubernetes runtime.

## Common use cases[â](#common-use-cases "Direct link to Common use cases")

* Developers can easily view the health and status of their services' K8s runtime.
* Platform engineers can create custom views and dashboards for different stakeholders.
* Platform engineers can set, maintain, and track standards for Kubernetes resources.
* R\&D managers can track data about services' Kubernetes resources, enabling high-level oversight and better decision-making.

## Prerequisites[â](#prerequisites "Direct link to Prerequisites")

* This guide assumes you have a Port account and that you have finished the [onboarding process](/getting-started/overview.md). We will use the `Workload` blueprint that was created during the onboarding process.
* You will need an accessible k8s cluster. If you don't have one, here is how to quickly set-up a [minikube cluster](https://minikube.sigs.k8s.io/docs/start/).
* [Helm](https://helm.sh/docs/intro/install/) - required to install Port's Kubernetes exporter.

## Set up data model[â](#set-up-data-model "Direct link to Set up data model")

To visualize your cluster's workloads in Port, we will first install Portâs Kubernetes exporter, which automatically creates Kubernetes-related blueprints and entities in your portal.

### Install Port's Kubernetes exporter[â](#install-ports-kubernetes-exporter "Direct link to Install Port's Kubernetes exporter")

To install the integration using Helm:

1. Go to the [Kubernetes data source page](https://app.getport.io/settings/data-sources?section=EXPORTERS\&provider=Kubernetes) in your portal.

2. A `helm` command will be displayed, with default values already filled out (e.g. your Port client ID, client secret, etc).<br /><!-- -->Copy the command, replace the placeholders with your values, then run it in your terminal to install the integration.

Selecting a Port API URL by account region

The `port_region`, `port.baseUrl`, `portBaseUrl`, `port_base_url` and `OCEAN__PORT__BASE_URL` parameters select which Port API instance to use:

* **EU** ([app.port.io](https://app.port.io)) â `https://api.port.io`
* **US** ([app.us.port.io](https://app.us.port.io)) â `https://api.us.port.io`

#### What does the exporter do?[â](#what-does-the-exporter-do "Direct link to What does the exporter do?")

After installation, the exporter will:

1. Create [blueprints]() in your [Builder](https://app.getport.io/settings/data-model) (as defined [here](https://github.com/port-labs/port-k8s-exporter/blob/main/assets/defaults/blueprints.json)) that represent Kubernetes resources:

   ![](/img/guides/k8sBlueprintsCreated.png)

   <br />

   <br />

   What is K8sWorkload?

   `K8sWorkload` is an abstraction of Kubernetes objects which create and manage pods (e.g. `Deployment`, `StatefulSet`, `DaemonSet`).

   <br />

2. Create [entities]() in your [Software catalog](https://app.getport.io/services). You will see a new page for each [blueprint]() containing your resources, filled with data from your Kubernetes cluster (according to the default mapping that is defined [here](https://github.com/port-labs/port-k8s-exporter/blob/main/assets/defaults/appConfig.yaml)):

   ![](/img/guides/k8sEntitiesCreated.png)

   <br />

   <br />

3. Create [scorecards]() for the blueprints that represent your K8s resources (as defined [here](https://github.com/port-labs/port-k8s-exporter/blob/main/assets/defaults/scorecards.json)). These scorecards define rules and checks over the data ingested from your K8s cluster, making it easy to check that your K8s resources meet your standards.

4. Create dashboards that provide you with a visual view of the data ingested from your K8s cluster.

5. Listen to changes in your Kubernetes cluster and update your [entities]() accordingly.

<br />

## Set up automatic discovery[â](#set-up-automatic-discovery "Direct link to Set up automatic discovery")

After installing the integration, the relationship between the **Workload** blueprint and the **k8\_workload** blueprint is established automatically. To ensure each **Workload** entity is properly related to its respective **k8\_workload** entity, we will configure automatic discovery using labels.

In this guide we will use the following convention:<br /><!-- -->A `k8_workload` with a label in the form of `portWorkload: <workload-identifier>` will automatically be assigned to a `Workload` with that identifier.

For example, a k8s deployment with the label `portWorkload: myWorkload` will be assigned to a `Workload` with the identifier `myWorkload`.

We achieved this by adding a [mapping definition](https://github.com/port-labs/template-assets/blob/main/kubernetes/full-configs/k8s-guide/k8s_guide_config.yaml#L111-L119) in the configuration YAML we used when installing the exporter. The definition uses `jq` to perform calculations between properties.

**Let's see this in action:**

1. Create a `Deployment` resource in your cluster with a label matching the identifier of a `Workload` in your [Software catalog](https://app.getport.io/services).<br /><!-- -->You can use the simple example below and change the `metadata.labels.portWorkload` value to match your desired `Workload`. Copy it into a file named `deployment.yaml`, then apply it:

   ```
   kubectl apply -f deployment.yaml
   ```

   **Deployment example (Click to expand)**

   ```
       apiVersion: apps/v1
       kind: Deployment
       metadata:
         name: awesomeapp
         labels:
           app: nginx
           portWorkload: AwesomeWorkload
       spec:
         replicas: 2
         selector:
           matchLabels:
             app: nginx
         template:
           metadata:
             labels:
               app: nginx
           spec:
             containers:
               - name: nginx
                 image: nginx:1.14.2
                 resources:
                   limits:
                     cpu: "200m"
                     memory: "256Mi"
                   requests:
                     cpu: "100m"
                     memory: "128Mi"
                 ports:
                   - containerPort: 80
   ```

   <br />

2. To see the new data, we need to update the mapping configuration that the K8s exporter uses to ingest data.<br /><!-- -->To edit the mapping, go to your [data sources page](https://app.getport.io/settings/data-sources), find the K8s exporter card, click on it and you will see a YAML editor showing the current configuration.

   Add the following block to the mapping configuration and click `Resync`:

   ```
   resources:
     # ... Other resource mappings installed by the K8s exporter
   - kind: apps/v1/deployments
     selector:
       query: .metadata.namespace | startswith("kube") | not
     port:
       entity:
         mappings:
           - identifier: .metadata.labels.portWorkload
             title: .metadata.name
             blueprint: '"workload"'
             relations:
               k8s_workload: >-
                 .metadata.name + "-Deployment-" + .metadata.namespace + "-" +
                 env.CLUSTER_NAME
   ```

   <br />

3. Go to your [Software catalog](https://app.getport.io/services), and click on `Workloads`. Click on the `Workload` for which you created the deployment, and you should see the `k8_workload` relation filled.

   ![](/img/guides/k8sEntityAfterIngestion.png)

   <br />

   <br />

## Visualize data from your Kubernetes environment[â](#visualize-data-from-your-kubernetes-environment "Direct link to Visualize data from your Kubernetes environment")

We now have a lot of data about our workloads, and some metrics to track their quality. Let's see how we can visualize this information in ways that will benefit the routine of our developers and managers. Let's start by creating a few widgets that will help us keep track of our services' health and availability.

### Add an "Unhealthy services" table to your homepage[â](#add-an-unhealthy-services-table-to-your-homepage "Direct link to Add an \"Unhealthy services\" table to your homepage")

In the configuration provided for this guide, a `workload` is considered `Healthy` if its defined number of replicas is equal to its available replicas (of course, you can change this definition).

1. Go to your [homepage](https://app.getport.io/home), click on the `+ Widget` button in the top right corner, then select `Table`.

2. Fill the form out like this, then click `Save`:

   ![](/img/guides/k8sHomepageTableUnhealthyServices.png)

   <br />

   <br />

3. In your new table, click on `Filter`, then on `+ Add new filter`. Fill out the fields like this:

   ![](/img/guides/k8sHomepageTableFilterUnhealthy.png)

   <br />

   <br />

Now you can keep track of services that need your attention right from your homepage.

![](/img/guides/k8sHomepageTableUnhealthyFilter.png)

*These services were not included in this guide, but serve to show an example of how this table might look.*

### Use your scorecards to get a clear overview of your workloads' availability[â](#use-your-scorecards-to-get-a-clear-overview-of-your-workloads-availability "Direct link to Use your scorecards to get a clear overview of your workloads' availability")

In the configuration provided for this guide, the availability metric is defined like this:

* Bronze: >=1 replica
* Silver: >=2 replicas
* Gold: >=3 replicas

To get an overall picture of our workloads' availability, we can use a table operation.

1. Go to the [`Workloads` catalog page](https://app.getport.io/workloads).

2. Click on the `Group by` button, then choose `High availability` from the dropdown:

   ![](/img/guides/k8sGroupByAvailability.png)

   <br />

   <br />

3. Click on any of the metric levels to see the corresponding workloads:

   ![](/img/guides/k8sWorkloadsAfterGroupByAvailability.png)

   <br />

   <br />

Note that you can also set this as the default view by click on the `Save this view` button ð

## Visualization[â](#visualization "Direct link to Visualization")

By leveraging Port's dashboards, you can create custom views to track your Kubernetes runtime metrics and monitor your services' performance over time.

![](/img/guides/k8sRuntimeMetricsDashboard.png)

### Dashboard setup[â](#dashboard-setup "Direct link to Dashboard setup")

1. Go to your [software catalog](https://app.getport.io/organization/catalog).

2. Click on the `+ New` button in the left sidebar.

3. Select **New dashboard**.

4. Name the dashboard **K8s Runtime Metrics**.

5. Choose an icon (**optional**).

6. Click `Create`.

### Add widgets[â](#add-widgets "Direct link to Add widgets")

In your new dashboard, create the following widgets:

**Service health overview (click to expand)**

1. Click `+ Widget` and select **Table**.

2. Type `Service health overview` in the **Title** field.

3. Choose an icon (**optional**).

4. Choose **Workload** as the **Blueprint**.

5. Click on `Save`.

6. Click on the `...` on the widget and select `Customize table`.

7. Click on the `Group by any Column` icon and select **Health Status**.

8. Click on `Manage properties` and add the following:

   * Title
   * Owning Team
   * Revision
   * Last Update

9. Click on the `Save` icon.

   ![](/img/guides/serviceHealthOverview.png)

**Resource usage trends (click to expand)**

1. Click `+ Widget` and select **Line Chart**.

2. Type `Resource usage trends` in the **Title** field.

3. Choose an icon (**optional**).

4. Choose `Aggregate Property (All Entities)` as the **Chart type**.

5. Choose **Workload** as the **Blueprint**.

6. Choose `High Throughput`, `Open Issues Count`, `Error Rate` as the **Y axis Property**.

7. Choose `createdAt` as the **X axis Property**.

8. Select `Hour` for **Time interval**.

9. Select `Today` for **Time range**.

10. Click on `Save`

![](/img/guides/resourceUsageTrends.png)

**Namespace distribution (click to expand)**

1. Click `+ Widget` and select **Pie Chart**.

2. Title: `Workload distribution by namespace`.

3. Choose an icon (**optional**).

4. Select **Workload** as the **Blueprint**.

5. Choose `Service Label` as the **Breakdown by Property**.

6. Click on `Save`

   ![](/img/guides/namespaceDistribution.png)

**Resource allocation overview(click to expand)**

1. Click `+ Widget` and select **Table**.

2. Title: `Resource allocation overview`.

3. Choose an icon (**optional**).

4. Select **Workload** as the **Blueprint**.

5. Click on `Save`.

6. Click on the `...` on the widget and select `Customize table`.

7. Click on the `Group by any Column` icon and select **Service Label**.

8. Click on `Manage properties` and add the following:

   * Title
   * Health Status
   * Standardization
   * Environment

9. Click on the `Save` icon.

   ![](/img/guides/resourceAllocationOverview.png)

These widgets will give you a comprehensive view of your Kubernetes runtime, making it easy to monitor service health, resource usage, and deployment status across your cluster.

## Possible daily routine integrations[â](#possible-daily-routine-integrations "Direct link to Possible daily routine integrations")

* Send a slack message in the R\&D channel to let everyone know that a new deployment was created.
* Notify Devops engineers when a service's availability drops.
* Send a weekly/monthly report to R\&D managers displaying the health of services' production runtime.

## Conclusion[â](#conclusion "Direct link to Conclusion")

Kubernetes is a complex environment that requires high-quality observability. Port's Kubernetes integration allows you to easily model and visualize your Kubernetes resources, and integrate them into your daily routine.<br /><!-- -->Customize your views to display the data that matters to you, grouped or filtered by teams, namespaces, or any other criteria.<br /><!-- -->With Port, you can seamlessly fit your organization's needs, and create a single source of truth for your Kubernetes resources.

More guides & tutorials will be available soon, in the meantime feel free to reach out with any questions via our [community slack](https://www.getport.io/community) or [Github project](https://github.com/port-labs?view_as=public).
