# Source: https://docs.port.io/guides/all/visualize-service-argocd-runtime.md

# Visualize your services' Kubernetes runtime using ArgoCD

Portâs ArgoCD integration allows you to model and visualize your Kubernetes deployments managed by ArgoCD, directly in Port.<br /><!-- -->This guide will help you set up the integration and visualize your services' Kubernetes runtime.

## Common use cases[â](#common-use-cases "Direct link to Common use cases")

* Developers can easily view the health and status of their services' K8s runtime.
* Platform engineers can create custom views and visualizations for different stakeholders in the organization.
* Platform engineers can set, maintain and track standards for K8s resources.
* R\&D managers can track any data about services' K8s resources, using tailor-made views and dashboards.

## Prerequisites[â](#prerequisites "Direct link to Prerequisites")

* The [Git Integration](/build-your-software-catalog/sync-data-to-catalog/git/.md) that is relevant for you needs to be installed.
* You will need an accessible k8s cluster. If you don't have one, here is how to quickly set-up a [minikube cluster](https://minikube.sigs.k8s.io/docs/start/).
* [Helm](https://helm.sh/docs/intro/install/) - required to install Port's ArgoCD integration.

## Set up data model[â](#set-up-data-model "Direct link to Set up data model")

To visualize your Kubernetes deployment managed by ArgoCD in Port, we will first install Port's ArgoCD integration which automatically creates ArgoCD-related blueprints and entities in your portal.

### Install Port's ArgoCD integration[â](#install-ports-argocd-integration "Direct link to Install Port's ArgoCD integration")

1. Go to your [data sources page](https://app.getport.io/settings/data-sources), click on `+ Data source`, find the `Kubernetes Stack` category and select `ArgoCD`.

2. Follow the installation command for your preferred installation method:

   * Helm
   * ArgoCD

   <!-- -->

   1. Go to the [Argocd<!-- --> data source page](https://app.getport.io/settings/data-sources?section=EXPORTERS\&provider=Argocd) in your portal.

   2. Select the `Self-hosted` method.

   3. A `helm` command will be displayed, with default values already filled out (e.g. your Port client ID, client secret, etc). Copy the command, replace the placeholders with your values, then run it in your terminal to install the integration.

   <!-- -->

   ### BaseUrl & webhook configuration[â](#baseurl--webhook-configuration "Direct link to BaseUrl & webhook configuration")

   To enable real-time updates of the data in your software catalog, you need to define the `liveEvents.baseUrl` parameter.<br /><!-- -->This parameter should be set to the URL of your <!-- -->Argocd<!-- --> integration instance, which needs to have the option to setup webhooks via HTTP requests/receive HTTP requests, so ensure the network is configured accordingly.

   * **If <!-- -->Argocd<!-- --> and the integration are in the same cluster/network**: Use an internal URL (e.g., a Kubernetes service DNS name).
     <br />
     <!-- -->
     For Kubernetes deployments, create a service to expose the integration pod and use the service URL as `liveEvents.baseUrl`. If both the source system and integration are in the same cluster, an internal ClusterIP service is sufficient.
   * **If <!-- -->Argocd<!-- --> is external to the integration's network**: The integration must be exposed via an ingress, load balancer, or public URL that
     <!-- -->
     Argocd
     <!-- -->
     can reach.

   If `liveEvents.baseUrl` is not provided, the integration will continue to function correctly. In such a configuration, to retrieve the latest information from the target system, the [`scheduledResyncInterval`](https://ocean.port.io/developing-an-integration/trigger-your-integration) parameter has to be set, or a manual resync will need to be triggered through Port's UI.

   Debugging local integrations

   To test webhooks or live event delivery to your local environment, expose your local pod or service to the internet using ngrok (e.g. `ngrok http http://localhost:8000`)

   <!-- -->

   <!-- -->

   ### Scalable mode for large integrations[â](#scalable-mode-for-large-integrations "Direct link to Scalable mode for large integrations")

   If you are deploying the integration at scale and want to decouple the resync process from the live events process (recommended for large or high-throughput environments), you can enable scalable mode by adding the following flags to your Helm install command:

   ```
     --set workload.kind="CronJob"  \
     --set workload.cron.resyncTimeoutMinutes=60  \
     --set scheduledResyncInterval="'*/60 * * * *'"  \
     --set liveEvents.worker.enabled=true
   ```

   <!-- -->

   <!-- -->

   <!-- -->

   Selecting a Port API URL by account region

   The `port_region`, `port.baseUrl`, `portBaseUrl`, `port_base_url` and `OCEAN__PORT__BASE_URL` parameters select which Port API instance to use:

   * **EU** ([app.port.io](https://app.port.io)) â `https://api.port.io`
   * **US** ([app.us.port.io](https://app.us.port.io)) â `https://api.us.port.io`

   To install the integration using ArgoCD, follow these steps:

   1. Create a `values.yaml` file in `argocd/my-ocean-argocd-integration` in your git repository with the content:

      Variable Replacement

      Remember to replace the placeholders for `TOKEN` and `SERVER_URL`, which represents your ArgoCD API token and server url respectively. Ensure that the token has sufficient permissions to read ArgoCD resources. You can configure the RBAC policy for the token user by following [this guide](https://argo-cd.readthedocs.io/en/stable/operator-manual/rbac/)

      ```
      initializePortResources: true
      scheduledResyncInterval: 120
      integration:
        identifier: my-ocean-argocd-integration
        type: argocd
        eventListener:
          type: POLLING
        config:
          serverUrl: SERVER_URL
        secrets:
          token: TOKEN
      ```

      <br />

   2. Install the `my-ocean-argocd-integration` ArgoCD Application by creating the following `my-ocean-argocd-integration.yaml` manifest:

      Variable Replacement

      Remember to replace the placeholders for `YOUR_PORT_CLIENT_ID` `YOUR_PORT_CLIENT_SECRET` and `YOUR_GIT_REPO_URL`.

      Multiple sources ArgoCD documentation can be found [here](https://argo-cd.readthedocs.io/en/stable/user-guide/multiple_sources/#helm-value-files-from-external-git-repository).

      ArgoCD Application

      ```
      apiVersion: argoproj.io/v1alpha1
      kind: Application
      metadata:
        name: my-ocean-argocd-integration
        namespace: argocd
      spec:
        destination:
          namespace: my-ocean-argocd-integration
          server: https://kubernetes.default.svc
        project: default
        sources:
        - repoURL: 'https://port-labs.github.io/helm-charts/'
          chart: port-ocean
          targetRevision: 0.1.18
          helm:
            valueFiles:
            - $values/argocd/my-ocean-argocd-integration/values.yaml
            parameters:
              - name: port.clientId
                value: YOUR_PORT_CLIENT_ID
              - name: port.clientSecret
                value: YOUR_PORT_CLIENT_SECRET
              - name: port.baseUrl
                value: https://api.port.io
        - repoURL: YOUR_GIT_REPO_URL
          targetRevision: main
          ref: values
        syncPolicy:
          automated:
            prune: true
            selfHeal: true
          syncOptions:
          - CreateNamespace=true
      ```

      Selecting a Port API URL by account region

      The `port_region`, `port.baseUrl`, `portBaseUrl`, `port_base_url` and `OCEAN__PORT__BASE_URL` parameters select which Port API instance to use:

      * **EU** ([app.port.io](https://app.port.io)) â `https://api.port.io`
      * **US** ([app.us.port.io](https://app.us.port.io)) â `https://api.us.port.io`

      <br />

   3. Apply your application manifest with `kubectl`:

      ```
      kubectl apply -f my-ocean-argocd-integration.yaml
      ```

#### What does the integration do?[â](#what-does-the-integration-do "Direct link to What does the integration do?")

After installation, the integration will:

1. Create [blueprints]() in your [Builder](https://app.getport.io/settings/data-model) (as defined [here](https://github.com/port-labs/ocean/blob/main/integrations/argocd/.port/resources/blueprints.json)) that represent ArgoCD resources:

   ![](/img/guides/argoBlueprintsCreated.png)

   <br />

   <br />

2. Create [entities]() in your [Software catalog](https://app.getport.io/services). You will see a new page for each [blueprint]() containing your resources, filled with data from your Kubernetes cluster (according to the default mapping that is defined [here](https://github.com/port-labs/ocean/blob/main/integrations/argocd/.port/resources/port-app-config.yaml)):

   ![](/img/guides/argoEntitiesCreated.png)

   <br />

   <br />

3. Create a [dashboard](https://app.getport.io/argocdDashboard) in your software catalog that provides you with some visual views of the data ingested from your K8s cluster.

4. Listen to changes in your ArgoCD resources and update your [entities]() accordingly.

<br />

## Set up automatic discovery[â](#set-up-automatic-discovery "Direct link to Set up automatic discovery")

After onboarding, the relationship between the **workload** blueprint and the **service** blueprint is established automatically.<br /><!-- -->The next step is to configure automatic discovery to ensure that each **workload** entity is properly related to its respective **service** entity.

You may have noticed that the service relation is empty for all of our workload entities. This is because we haven't specified which **workload** belongs to which **service**. This can be done manually, or via mapping by using a convention of your choice.

In this guide we will use the following convention:<br /><!-- -->An Argo application with a label in the form of `portService: <service-identifier>` will automatically be assigned to a `service` with that identifier.

For example, an ArgoCD application with the label `portService: awesomeService` will be assigned to a `service` with the identifier `awesomeService`.

To achieve this, we need to update the ArgoCD integration's mapping configuration:

1. Go to your [data sources page](https://app.getport.io/settings/data-sources), find the ArgoCD exporter card, click on it and you will see a YAML editor showing the current configuration. Add the following block to the mapping configuration and click `Resync`:

   ```
     - kind: application
       selector:
         query: 'true'
       port:
         entity:
           mappings:
             identifier: .metadata.labels.portService
             blueprint: '"workload"'
             properties: {}
             relations:
               service: .metadata.labels.portService       
   ```

   <br />

2. Go to the [services page](https://app.getport.io/services) of your software catalog. Click on the `service` for which you created the deployment. At the bottom of the page, you will see the `workload` related to this service, along with all of their data:

   ![](/img/guides/argoEntityAfterIngestion.png)

   <br />

## Visualization[â](#visualization "Direct link to Visualization")

By leveraging Port's dashboards, you can create custom views to track your ArgoCD runtime metrics and monitor your applications' performance over time.

![](/img/guides/argoRuntimeMetricsDashboard.png)

### Set up dashboard[â](#set-up-dashboard "Direct link to Set up dashboard")

1. Go to your [software catalog](https://app.getport.io/organization/catalog).

2. Click on the `+ New` button in the left sidebar.

3. Select **New dashboard**.

4. Name the dashboard **ArgoCD Runtime Metrics**.

5. Choose an icon (**optional**).

6. Click `Create`.

### Add widgets[â](#add-widgets "Direct link to Add widgets")

In your new dashboard, create the following widgets:

**ArgoCD sync status overview (click to expand)**

1. Click `+ Widget` and select **Table**.

2. Title: `ArgoCD sync status overview`.

3. Choose an icon (**optional**).

4. Select **Workload** as the **Blueprint**.

5. Click on `Save`.

6. Click on the three dots on the widget and select `Customize table`.

7. Click on the `Group by any Column` icon and select **Sync Status**.

8. Click on the `Manage properties` and add the following:

   * Title
   * Health Status
   * Passed scorecard rules

9. Click on the `Save` icon.

   ![](/img/guides/argocdSyncStatusOverview.png)

**Health status distribution (click to expand)**

1. Click `+ Widget` and select **Pie Chart**.

2. Title: `Application health status distribution`.

3. Choose an icon (**optional**).

4. Select **Workload** as the **Blueprint**.

5. Choose `Health Status` as the **Breakdown by property**.

6. Click on `Save`.

   ![](/img/guides/applicationHealthDistribution.png)

**Resource health status overview (click to expand)**

1. Click `+ Widget` and select **Table**.

2. Title: `Resource health status overview`.

3. Choose an icon (**optional**).

4. Select **Workload** as the **Blueprint**.

5. Click on `Save`.

6. Click on the three dots on the widget and select `Customize table`.

7. Click on the `Group by any Column` icon and select **Health Status**.

8. Click on the `Manage properties` and add the following:

   * Title
   * Sync Status
   * Health and Synced

9. Click on the `Save` icon.

   ![](/img/guides/resourceStatusOverview.png)

These widgets will give you a comprehensive view of your ArgoCD runtime, making it easy to monitor application health, sync status, and deployment progress across your cluster.

## Possible daily routine integrations[â](#possible-daily-routine-integrations "Direct link to Possible daily routine integrations")

* Send a slack message in the R\&D channel to let everyone know that a new deployment was created.
* Notify Devops engineers when a service's availability drops.
* Send a weekly/monthly report to R\&D managers displaying the health of services' production runtime.

## Conclusion[â](#conclusion "Direct link to Conclusion")

Kubernetes is a complex environment that requires high-quality observability. Port's ArgoCD integration allows you to easily model and visualize your ArgoCD & Kubernetes resources, and integrate them into your daily routine.<br /><!-- -->Customize your views to display the data that matters to you, grouped or filtered by teams, namespaces, or any other criteria.
