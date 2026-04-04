# Source: https://learn.microsoft.com/en-us/azure/azure-functions/functions-infrastructure-as-code

Title: Automate function app resource deployment to Azure

URL Source: https://learn.microsoft.com/en-us/azure/azure-functions/functions-infrastructure-as-code

Published Time: Tue, 10 Feb 2026 18:07:49 GMT

Markdown Content:
You can use a Bicep file or an Azure Resource Manager (ARM) template to automate the process of deploying your function app. During the deployment, you can use existing Azure resources or create new ones.

You can obtain these benefits in your production apps by using deployment automation, both infrastructure-as-code (IaC) and continuous integration and deployment (CI/CD):

*   **Consistency**: Define your infrastructure in code to ensure consistent deployments across environments.
*   **Version Control**: Track changes to your infrastructure and application configurations in source control, along with your project code.
*   **Automation**: Automate deployment, which reduces manual errors and shortens release process.
*   **Scalability**: Easily replicate infrastructure for multiple environments, such as development, testing, and production.
*   **Disaster Recovery**: Quickly recreate infrastructure after failures or during migrations.

This article shows you how to automate the creation of Azure resources and deployment configurations for Azure Functions. To learn more about continuous deployment of your project code, see [Continuous deployment for Azure Functions](https://learn.microsoft.com/en-us/azure/azure-functions/functions-continuous-deployment).

The template code to create the required Azure resources depends on the desired hosting options for your function app. This article supports the following hosting options:

| Hosting option | Deployment type | Sample templates |
| --- | --- | --- |
| [Flex Consumption plan](https://learn.microsoft.com/en-us/azure/azure-functions/flex-consumption-plan) | Code-only | [Bicep](https://github.com/Azure/azure-quickstart-templates/blob/master/quickstarts/microsoft.web/function-app-flex-managed-identities/main.bicep) [ARM template](https://github.com/Azure/azure-quickstart-templates/blob/master/quickstarts/microsoft.web/function-app-flex-managed-identities/azuredeploy.json) [Terraform](https://github.com/Azure-Samples/azure-functions-flex-consumption-samples/tree/main/IaC/terraformazurerm) |
| [Premium plan](https://learn.microsoft.com/en-us/azure/azure-functions/functions-premium-plan) | Code | Container | [Bicep](https://github.com/Azure-Samples/function-app-arm-templates/blob/main/function-app-premium-plan/main.bicep) [ARM template](https://github.com/Azure-Samples/function-app-arm-templates/blob/main/function-app-premium-plan/azuredeploy.json) |
| [Dedicated plan](https://learn.microsoft.com/en-us/azure/azure-functions/dedicated-plan) | Code | Container | [Bicep](https://github.com/Azure-Samples/function-app-arm-templates/blob/main/function-app-dedicated-plan/main.bicep) [ARM template](https://github.com/Azure-Samples/function-app-arm-templates/blob/main/function-app-dedicated-plan/azuredeploy.json) |
| [Azure Container Apps](https://learn.microsoft.com/en-us/azure/container-apps/functions-overview) | Container-only | [Bicep](https://github.com/Azure/azure-functions-on-container-apps/tree/main/samples/ACAKindfunctionapp) |
| [Consumption plan](https://learn.microsoft.com/en-us/azure/azure-functions/consumption-plan) | Code-only | [Bicep](https://github.com/Azure-Samples/function-app-arm-templates/blob/main/function-app-windows-consumption/main.bicep) [ARM template](https://github.com/Azure-Samples/function-app-arm-templates/blob/main/function-app-windows-consumption/azuredeploy.json) |

Make sure to select your hosting plan at the top of the article.

Important

After 30 September 2028, the option to host your function app on Linux in a Consumption plan is retired. To avoid disruptions, migrate your existing Consumption plan apps that run on Linux to the [Flex Consumption plan](https://learn.microsoft.com/en-us/azure/azure-functions/flex-consumption-plan) before that date. Apps running on Windows in a Consumption plan aren't affected by this change.

After 30 September 2025, no new features and no new language stack support are added to the Linux Consumption plan. The last supported language versions for Linux Consumption are: .NET 9, Python 3.12, Node.js 22, PowerShell 7.4, and Java 21. Newer language versions aren't supported for Linux Consumption.

For more information, see [Migrate Consumption plan apps to the Flex Consumption plan](https://learn.microsoft.com/en-us/azure/azure-functions/migration/migrate-plan-consumption-to-flex).

When using this article, keep these considerations in mind:

*   There's no canonical way to structure an ARM template.

*   A Bicep deployment can be modularized into multiple Bicep files and [Azure Verified Modules (AVMs)](https://azure.github.io/Azure-Verified-Modules/overview/introduction/).

*   This article assumes that you have a basic understanding of [creating Bicep files](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/file) or [authoring Azure Resource Manager templates](https://learn.microsoft.com/en-us/azure/azure-resource-manager/templates/syntax).

*   Examples are shown as individual sections for specific resources. For a broad set of complete Bicep file and ARM template examples, see [these function app deployment examples](https://learn.microsoft.com/en-us/samples/browse/?expanded=azure&terms=%22azure%20functions%22&products=azure-resource-manager).

*   Examples are shown as individual sections for specific resources. For Bicep, [Azure Verified Modules (AVM)](https://azure.github.io/Azure-Verified-Modules/) are shown, when available. For a broad set of complete Bicep file and ARM template examples, see [these Flex Consumption app deployment examples](https://learn.microsoft.com/en-us/samples/browse/?expanded=azure&terms=%22azure%20functions%20flex%22&products=azure-resource-manager).

*   Examples are shown as individual sections for specific resources.

You must create or configure these resources for an Azure Functions-hosted deployment:

| Resource | Requirement | Syntax and properties reference |
| --- | --- | --- |
| A [storage account](https://learn.microsoft.com/en-us/azure/azure-functions/functions-infrastructure-as-code#create-storage-account) | Required | [Microsoft.Storage/storageAccounts](https://learn.microsoft.com/en-us/azure/templates/microsoft.storage/storageaccounts) |
| An [Application Insights](https://learn.microsoft.com/en-us/azure/azure-functions/functions-infrastructure-as-code#create-application-insights) component | Recommended | [Microsoft.Insights/components](https://learn.microsoft.com/en-us/azure/templates/microsoft.insights/components)* |
| A [hosting plan](https://learn.microsoft.com/en-us/azure/azure-functions/functions-infrastructure-as-code#create-the-hosting-plan) | Required | [Microsoft.Web/serverfarms](https://learn.microsoft.com/en-us/azure/templates/microsoft.web/serverfarms) |
| A [function app](https://learn.microsoft.com/en-us/azure/azure-functions/functions-infrastructure-as-code#create-the-function-app) | Required | [Microsoft.Web/sites](https://learn.microsoft.com/en-us/azure/templates/microsoft.web/sites) |

You must create or configure these resources for an Azure Functions-hosted deployment:

| Resource | Requirement | Syntax and properties reference |
| --- | --- | --- |
| A [storage account](https://learn.microsoft.com/en-us/azure/azure-functions/functions-infrastructure-as-code#create-storage-account) | Required | [Microsoft.Storage/storageAccounts](https://learn.microsoft.com/en-us/azure/templates/microsoft.storage/storageaccounts) |
| An [Application Insights](https://learn.microsoft.com/en-us/azure/azure-functions/functions-infrastructure-as-code#create-application-insights) component | Recommended | [Microsoft.Insights/components](https://learn.microsoft.com/en-us/azure/templates/microsoft.insights/components)* |
| A [function app](https://learn.microsoft.com/en-us/azure/azure-functions/functions-infrastructure-as-code#create-the-function-app) | Required | [Microsoft.Web/sites](https://learn.microsoft.com/en-us/azure/templates/microsoft.web/sites) |

An Azure Container Apps-hosted deployment typically consists of these resources:

| Resource | Requirement | Syntax and properties reference |
| --- | --- | --- |
| A [storage account](https://learn.microsoft.com/en-us/azure/azure-functions/functions-infrastructure-as-code#create-storage-account) | Required | [Microsoft.Storage/storageAccounts](https://learn.microsoft.com/en-us/azure/templates/microsoft.storage/storageaccounts) |
| An [Application Insights](https://learn.microsoft.com/en-us/azure/azure-functions/functions-infrastructure-as-code#create-application-insights) component | Recommended | [Microsoft.Insights/components](https://learn.microsoft.com/en-us/azure/templates/microsoft.insights/components)* |
| A [managed environment](https://learn.microsoft.com/en-us/azure/container-apps/functions-overview#) | Required | [Microsoft.App/managedEnvironments](https://learn.microsoft.com/en-us/azure/templates/microsoft.app/managedenvironments) |
| A [function app](https://learn.microsoft.com/en-us/azure/azure-functions/functions-infrastructure-as-code#create-the-function-app) | Required | [Microsoft.Web/sites](https://learn.microsoft.com/en-us/azure/templates/microsoft.web/sites) |

An Azure Arc-hosted deployment typically consists of these resources:

| Resource | Requirement | Syntax and properties reference |
| --- | --- | --- |
| A [storage account](https://learn.microsoft.com/en-us/azure/azure-functions/functions-infrastructure-as-code#create-storage-account) | Required | [Microsoft.Storage/storageAccounts](https://learn.microsoft.com/en-us/azure/templates/microsoft.storage/storageaccounts) |
| An [Application Insights](https://learn.microsoft.com/en-us/azure/azure-functions/functions-infrastructure-as-code#create-application-insights) component | Recommended | [Microsoft.Insights/components](https://learn.microsoft.com/en-us/azure/templates/microsoft.insights/components)1 |
| An [App Service Kubernetes environment](https://learn.microsoft.com/en-us/azure/app-service/overview-arc-integration#app-service-kubernetes-environment) | Required | [Microsoft.ExtendedLocation/customLocations](https://learn.microsoft.com/en-us/azure/templates/microsoft.extendedlocation/customlocations) |
| A [function app](https://learn.microsoft.com/en-us/azure/azure-functions/functions-infrastructure-as-code#create-the-function-app) | Required | [Microsoft.Web/sites](https://learn.microsoft.com/en-us/azure/templates/microsoft.web/sites) |

*If you don't already have a Log Analytics Workspace that can be used by your Application Insights instance, you also need to create this resource.

When you deploy multiple resources in a single Bicep file or ARM template, the order in which resources are created is important. This requirement is a result of dependencies between resources. For such dependencies, make sure to use the `dependsOn` element to define the dependency in the dependent resource. For more information, see either [Define the order for deploying resources in ARM templates](https://learn.microsoft.com/en-us/azure/azure-resource-manager/templates/resource-dependency) or [Resource dependencies in Bicep](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/resource-dependencies).

*   The examples are designed to execute in the context of an existing resource group.
*   Both Application Insights and storage logs require you to have an existing [Azure Log Analytics workspace](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/log-analytics-overview). Workspaces can be shared between services, and as a rule of thumb you should create a workspace in each geographic region to improve performance. For an example of how to create a Log Analytics workspace, see [Create a Log Analytics workspace](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/quick-create-workspace?tabs=azure-resource-manager#create-a-workspace). You can find the fully qualified workspace resource ID in a workspace page in the [Azure portal](https://portal.azure.com/) under **Settings**>**Properties**>**Resource ID**.

*   This article assumes that you have already created a [managed environment](https://learn.microsoft.com/en-us/azure/container-apps/environment) in Azure Container Apps. You need both the name and the ID of the managed environment to create a function app hosted on Container Apps.

*   This article assumes that you have already created an [App Service-enabled custom location](https://learn.microsoft.com/en-us/azure/app-service/overview-arc-integration) on an [Azure Arc-enabled Kubernetes cluster](https://learn.microsoft.com/en-us/azure/azure-arc/kubernetes/overview). You need both the custom location ID and the Kubernetes environment ID to create a function app hosted in an Azure Arc custom location.

All function apps require an Azure storage account. You need a general purpose account that supports blobs, tables, queues, and files. For more information, see [Azure Functions storage account requirements](https://learn.microsoft.com/en-us/azure/azure-functions/storage-considerations#storage-account-requirements).

Important

The storage account is used to store important app data, sometimes including the application code itself. You should limit access from other apps and users to the storage account.

This example section creates a Standard general purpose v2 storage account:

*   [Bicep](https://learn.microsoft.com/en-us/azure/azure-functions/functions-infrastructure-as-code#tabpanel_1_bicep)
*   [ARM template](https://learn.microsoft.com/en-us/azure/azure-functions/functions-infrastructure-as-code#tabpanel_1_json)

```
resource storageAccount 'Microsoft.Storage/storageAccounts@2023-05-01' = {
  name: storageAccountName
  location: location
  kind: 'StorageV2'
  sku: {
    name: 'Standard_LRS'
  }
  properties: {
    supportsHttpsTrafficOnly: true
    defaultToOAuthAuthentication: true
    allowBlobPublicAccess: false
  }
}
```

For more context, see the complete [main.bicep](https://github.com/Azure-Samples/function-app-arm-templates/blob/main/function-app-linux-consumption/main.bicep#L37) file in the templates repository.

You need to set the connection string of this storage account as the `AzureWebJobsStorage` app setting, which Functions requires. The templates in this article construct this connection string value based on the created storage account, which is a best practice. For more information, see [Application configuration](https://learn.microsoft.com/en-us/azure/azure-functions/functions-infrastructure-as-code#application-configuration).

Deployments to an app running in the Flex Consumption plan require a container in Azure Blob Storage as the deployment source. You can use either the default storage account or you can specify a separate storage account. For more information, see [Configure deployment settings](https://learn.microsoft.com/en-us/azure/azure-functions/flex-consumption-how-to#configure-deployment-settings).

This deployment account must already be configured when you create your app, including the specific container used for deployments. To learn more about configuring deployments, see [Deployment sources](https://learn.microsoft.com/en-us/azure/azure-functions/functions-infrastructure-as-code#deployment-sources).

This example shows how to create a container in the storage account:

*   [Bicep](https://learn.microsoft.com/en-us/azure/azure-functions/functions-infrastructure-as-code#tabpanel_2_bicep)
*   [ARM template](https://learn.microsoft.com/en-us/azure/azure-functions/functions-infrastructure-as-code#tabpanel_2_json)

```
}

// Azure Functions Flex Consumption
module functionApp 'br/public:avm/res/web/site:0.16.0' = {
  name: 'functionapp'
  scope: rg
  params: {
    kind: 'functionapp,linux'
    name: functionAppName_resolved
    location: location
    tags: union(tags, { 'azd-service-name': 'api' })
    serverFarmResourceId: appServicePlan.outputs.resourceId
    managedIdentities: {
      systemAssigned: true
    }
    functionAppConfig: {
      deployment: {
        storage: {
          type: 'blobContainer'
          value: '${storage.outputs.primaryBlobEndpoint}${deploymentStorageContainerName}'
          authentication: {
            type: 'SystemAssignedIdentity'
          }
```

This example shows how to use the [AVM for storage accounts](https://github.com/Azure/bicep-registry-modules/tree/main/avm/res/storage/storage-account) to create the blob storage container along with the storage account. For the snippet in context, see [this deployment example](https://github.com/Azure-Samples/azure-functions-flex-consumption-samples/blob/main/IaC/bicep/main.bicep#L133).

Other deployment settings are [configured with the app itself](https://learn.microsoft.com/en-us/azure/azure-functions/functions-infrastructure-as-code#deployment-sources).

Because the storage account is used for important function app data, you should monitor the account for modification of that content. To monitor your storage account, you need to configure Azure Monitor resource logs for Azure Storage. In this example section, a Log Analytics workspace named `myLogAnalytics` is used as the destination for these logs.

*   [Bicep](https://learn.microsoft.com/en-us/azure/azure-functions/functions-infrastructure-as-code#tabpanel_3_bicep)
*   [ARM template](https://learn.microsoft.com/en-us/azure/azure-functions/functions-infrastructure-as-code#tabpanel_3_json)

```
resource blobService 'Microsoft.Storage/storageAccounts/blobServices@2021-09-01' existing = {
  name:'default'
  parent:storageAccountName
}

resource storageDataPlaneLogs 'Microsoft.Insights/diagnosticSettings@2021-05-01-preview' = {
  name: '${storageAccountName}-logs'
  scope: blobService
  properties: {
    workspaceId: myLogAnalytics.id
    logs: [
      {
        category: 'StorageWrite'
        enabled: true
      }
    ]
    metrics: [
      {
        category: 'Transaction'
        enabled: true
      }
    ]
  }
}
```

This same workspace can be used for the Application Insights resource defined later. For more information, including how to work with these logs, see [Monitoring Azure Storage](https://learn.microsoft.com/en-us/azure/storage/blobs/monitor-blob-storage).

You should be using Application Insights for monitoring your function app executions. Application Insights now requires an Azure Log Analytics workspace, which can be shared. These examples assume you're using an existing workspace and have the fully qualified resource ID for the workspace. For more information, see [Azure Log Analytics workspace](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/log-analytics-overview).

In this example section, the Application Insights resource is defined with the type `Microsoft.Insights/components` and the kind `web`:

*   [Bicep](https://learn.microsoft.com/en-us/azure/azure-functions/functions-infrastructure-as-code#tabpanel_4_bicep)
*   [ARM template](https://learn.microsoft.com/en-us/azure/azure-functions/functions-infrastructure-as-code#tabpanel_4_json)

```
resource applicationInsight 'Microsoft.Insights/components@2020-02-02' = {
  name: applicationInsightsName
  location: appInsightsLocation
  tags: tags
  kind: 'web'
  properties: {
    Application_Type: 'web'
    WorkspaceResourceId: '<FULLY_QUALIFIED_RESOURCE_ID>'
  }
}
```

For more context, see the complete [main.bicep](https://github.com/Azure-Samples/function-app-arm-templates/blob/main/function-app-linux-consumption/main.bicep#L60) file in the templates repository.

The connection must be provided to the function app using the [`APPLICATIONINSIGHTS_CONNECTION_STRING`](https://learn.microsoft.com/en-us/azure/azure-functions/functions-app-settings#applicationinsights_connection_string) application setting. For more information, see [Application configuration](https://learn.microsoft.com/en-us/azure/azure-functions/functions-infrastructure-as-code#application-configuration).

The examples in this article obtain the connection string value for the created instance. Older versions might instead use [`APPINSIGHTS_INSTRUMENTATIONKEY`](https://learn.microsoft.com/en-us/azure/azure-functions/functions-app-settings#appinsights_instrumentationkey) to set the instrumentation key, which is no longer recommended.

Flex Consumption is a Linux-based hosting plan that builds on the Consumption _pay for what you use_ serverless billing model. The plan features support for private networking, instance memory size selection, and improved managed identity support.

A Flex Consumption plan is a special type of `serverfarm` resource. You can specify it by using `FC1` for the `Name` property value in the `sku` property with a `tier` value of `FlexConsumption`.

This example section creates a Flex Consumption plan:

*   [Bicep](https://learn.microsoft.com/en-us/azure/azure-functions/functions-infrastructure-as-code#tabpanel_5_bicep)
*   [ARM template](https://learn.microsoft.com/en-us/azure/azure-functions/functions-infrastructure-as-code#tabpanel_5_json)

```
scaleAndConcurrency: {
    maximumInstanceCount: maximumInstanceCount
    instanceMemoryMB: instanceMemoryMB
  }
  runtime: { 
    name: functionAppRuntime
    version: functionAppRuntimeVersion
  }
}
siteConfig: {
  alwaysOn: false
}
configs: [{
  name: 'appsettings'
  properties:{
```

This example uses the [AVM for App Service plans](https://github.com/Azure/bicep-registry-modules/tree/main/avm/res/web/serverfarm). For the snippet in context, see [this deployment example](https://github.com/Azure-Samples/azure-functions-flex-consumption-samples/blob/main/IaC/bicep/main.bicep#L156).

Because the Flex Consumption plan currently only supports Linux, you must also set the `reserved` property to `true`.

The Premium plan offers the same scaling as the Consumption plan but includes dedicated resources and extra capabilities. To learn more, see [Azure Functions Premium Plan](https://learn.microsoft.com/en-us/azure/azure-functions/functions-premium-plan).

A Premium plan is a special type of `serverfarm` resource. You can specify it by using either `EP1`, `EP2`, or `EP3` for the `Name` property value in the `sku` property. The way that you define the Functions hosting plan depends on whether your function app runs on Windows or on Linux. This example section creates an `EP1` plan:

*   [Windows](https://learn.microsoft.com/en-us/azure/azure-functions/functions-infrastructure-as-code#tabpanel_6_windows_bicep)
*   [Linux](https://learn.microsoft.com/en-us/azure/azure-functions/functions-infrastructure-as-code#tabpanel_6_linux_bicep)

To run your app on Linux, you must also set property `"reserved": true` for the `serverfarms` resource:

```
resource hostingPlan 'Microsoft.Web/serverfarms@2022-03-01' = {
  name: hostingPlanName
  location: location
  sku: {
    name: 'EP1'
    tier: 'ElasticPremium'
    family: 'EP'
  }
  kind: 'elastic'
  properties: {
    maximumElasticWorkerCount: 20
    reserved: true
  }
}
```

For more context, see the complete [main.bicep](https://github.com/Azure-Samples/function-app-arm-templates/blob/main/function-app-premium-plan/main.bicep#L62) file in the templates repository.

For more information about the `sku` object, see [`SkuDefinition`](https://learn.microsoft.com/en-us/azure/templates/microsoft.web/serverfarms#skudescription) or review the example templates.

In the Dedicated (App Service) plan, your function app runs on dedicated VMs on Basic, Standard, and Premium SKUs in App Service plans, similar to web apps. For more information, see [Dedicated plan](https://learn.microsoft.com/en-us/azure/azure-functions/dedicated-plan).

For a sample Bicep file/Azure Resource Manager template, see [Function app on Azure App Service plan](https://azure.microsoft.com/resources/templates/function-app-create-dedicated/).

In Functions, the Dedicated plan is just a regular App Service plan, which is defined by a `serverfarm` resource. You must provide at least the `name` value. For a list of supported plan names, see the `--sku` setting in [`az appservice plan create`](https://learn.microsoft.com/en-us/cli/azure/appservice/plan#az-appservice-plan-create) for the current list of supported values for a Dedicated plan.

The way that you define the hosting plan depends on whether your function app runs on Windows or on Linux:

*   [Windows](https://learn.microsoft.com/en-us/azure/azure-functions/functions-infrastructure-as-code#tabpanel_7_windows_bicep)
*   [Linux](https://learn.microsoft.com/en-us/azure/azure-functions/functions-infrastructure-as-code#tabpanel_7_linux_bicep)

```
resource hostingPlan 'Microsoft.Web/serverfarms@2022-03-01' = {
  name: hostingPlanName
  location: location
  sku: {
    tier: 'Standard'
    name: 'S1'
    size: 'S1'
    family: 'S'
    capacity: 1
  }
  properties: {
    reserved: true
  }
}
```

For more context, see the complete [main.bicep](https://github.com/Azure-Samples/function-app-arm-templates/blob/main/function-app-dedicated-plan/main.bicep#L62) file in the templates repository.

You don't need to explicitly define a Consumption hosting plan resource. When you skip this resource definition, a plan is automatically either created or selected on a per-region basis when you create the function app resource itself.

You can explicitly define a Consumption plan as a special type of `serverfarm` resource, which you specify using the value `Dynamic` for the `computeMode` and `sku` properties. This example section shows you how to explicitly define a consumption plan. The way that you define a hosting plan depends on whether your function app runs on Windows or on Linux.

*   [Windows](https://learn.microsoft.com/en-us/azure/azure-functions/functions-infrastructure-as-code#tabpanel_8_windows_bicep)
*   [Linux](https://learn.microsoft.com/en-us/azure/azure-functions/functions-infrastructure-as-code#tabpanel_8_linux_bicep)

To run your app on Linux, you must also set the property `"reserved": true` for the `serverfarms` resource:

```
resource hostingPlan 'Microsoft.Web/serverfarms@2022-03-01' = {
  name: hostingPlanName
  location: location
  sku: {
    name: 'Y1'
    tier: 'Dynamic'
    size: 'Y1'
    family: 'Y'
    capacity: 0
  }
  properties: {
    computeMode: 'Dynamic'
    reserved: true
  }
}
```

For more context, see the complete [main.bicep](https://github.com/Azure-Samples/function-app-arm-templates/blob/main/function-app-linux-consumption/main.bicep#L46) file in the templates repository.

Azure Functions can be deployed to [Azure Arc-enabled Kubernetes](https://learn.microsoft.com/en-us/azure/app-service/overview-arc-integration) either as a code project or a containerized function app.

To create the app and plan resources, you must have already [created an App Service Kubernetes environment](https://learn.microsoft.com/en-us/azure/app-service/manage-create-arc-environment) for an Azure Arc-enabled Kubernetes cluster. The examples in this article assume you have the resource ID of the custom location (`customLocationId`) and App Service Kubernetes environment (`kubeEnvironmentId`) to which you're deploying, which are set in this example:

*   [ARM template](https://learn.microsoft.com/en-us/azure/azure-functions/functions-infrastructure-as-code#tabpanel_9_json)
*   [Bicep](https://learn.microsoft.com/en-us/azure/azure-functions/functions-infrastructure-as-code#tabpanel_9_bicep)

```
param kubeEnvironmentId string
param customLocationId string
```

Both sites and plans must reference the custom location through an `extendedLocation` field. As shown in this truncated example, `extendedLocation` sits outside of `properties`, as a peer to `kind` and `location`:

*   [ARM template](https://learn.microsoft.com/en-us/azure/azure-functions/functions-infrastructure-as-code#tabpanel_10_json)
*   [Bicep](https://learn.microsoft.com/en-us/azure/azure-functions/functions-infrastructure-as-code#tabpanel_10_bicep)

```
resource hostingPlan 'Microsoft.Web/serverfarms@2022-03-01' = {
  ...
  {
    extendedLocation: {
      name: customLocationId
    }
  }
}
```

The plan resource should use the Kubernetes (`K1`) value for `SKU`, the `kind` field should be `linux,kubernetes`, and the `reserved` property should be `true`, since it's a Linux deployment. You must also set the `extendedLocation` and `kubeEnvironmentProfile.id` to the custom location ID and the Kubernetes environment ID, respectively, which might look like this example section:

*   [ARM template](https://learn.microsoft.com/en-us/azure/azure-functions/functions-infrastructure-as-code#tabpanel_11_json)
*   [Bicep](https://learn.microsoft.com/en-us/azure/azure-functions/functions-infrastructure-as-code#tabpanel_11_bicep)

```
resource hostingPlan 'Microsoft.Web/serverfarms@2022-03-01' = {
  name: hostingPlanName
  location: location
  kind: 'linux,kubernetes'
  sku: {
    name: 'K1'
    tier: 'Kubernetes'
  }
  extendedLocation: {
    name: customLocationId
  }
  properties: {
    kubeEnvironmentProfile: {
      id: kubeEnvironmentId
    }
    reserved: true
  }
}
```

The function app resource is defined by a resource of type `Microsoft.Web/sites` and `kind` that includes `functionapp`, at a minimum.

The way that you define a function app resource depends on whether you're hosting on Linux or on Windows:

*   [Windows](https://learn.microsoft.com/en-us/azure/azure-functions/functions-infrastructure-as-code#tabpanel_12_windows)
*   [Linux](https://learn.microsoft.com/en-us/azure/azure-functions/functions-infrastructure-as-code#tabpanel_12_linux)

When running the function app on Linux, you must:

*   Set `kind` to `functionapp,linux`.
*   Set `reserved` to `true`.
*   Set the `linuxFxVersion` property under `siteConfig` to the correct value for your runtime stack in the format of `<runtime>|<runtimeVersion>`. For more information, see the [linuxFxVersion site setting](https://learn.microsoft.com/en-us/azure/azure-functions/functions-app-settings#linuxfxversion) reference.

For a list of application settings required when running on Linux, see [Application configuration](https://learn.microsoft.com/en-us/azure/azure-functions/functions-infrastructure-as-code#application-configuration).

For a sample Bicep file or ARM template, see the [function app hosted on Linux Consumption Plan](https://github.com/Azure-Samples/function-app-arm-templates/tree/main/function-app-linux-consumption) template.

*   [Windows](https://learn.microsoft.com/en-us/azure/azure-functions/functions-infrastructure-as-code#tabpanel_13_windows)
*   [Linux](https://learn.microsoft.com/en-us/azure/azure-functions/functions-infrastructure-as-code#tabpanel_13_linux)

When running the function app on Linux, you must:

*   Set `kind` to `functionapp,linux`.
*   Set `reserved` to `true`.
*   Set the `linuxFxVersion` property under `siteConfig` to the correct value for your runtime stack in the format of `<runtime>|<runtimeVersion>`. For more information, see the [linuxFxVersion site setting](https://learn.microsoft.com/en-us/azure/azure-functions/functions-app-settings#linuxfxversion) reference.

For a list of application settings required when running on Linux, see [Application configuration](https://learn.microsoft.com/en-us/azure/azure-functions/functions-infrastructure-as-code#application-configuration).

Flex Consumption replaces many of the standard application settings and site configuration properties used in Bicep and ARM template deployments. For more information, see [Application configuration](https://learn.microsoft.com/en-us/azure/azure-functions/functions-infrastructure-as-code#application-configuration).

*   [Bicep](https://learn.microsoft.com/en-us/azure/azure-functions/functions-infrastructure-as-code#tabpanel_14_bicep)
*   [ARM template](https://learn.microsoft.com/en-us/azure/azure-functions/functions-infrastructure-as-code#tabpanel_14_json)

```
AzureWebJobsStorage__blobServiceUri: 'https://${storage.outputs.name}.blob.${environment().suffixes.storage}'
        AzureWebJobsStorage__queueServiceUri: 'https://${storage.outputs.name}.queue.${environment().suffixes.storage}'
        AzureWebJobsStorage__tableServiceUri: 'https://${storage.outputs.name}.table.${environment().suffixes.storage}'

        // Application Insights settings are always included
        APPLICATIONINSIGHTS_CONNECTION_STRING: applicationInsights.outputs.connectionString
        APPLICATIONINSIGHTS_AUTHENTICATION_STRING: 'Authorization=AAD'
    }
    }]
  }
}

// Consolidated Role Assignments
module rbacAssignments 'rbac.bicep' = {
  name: 'rbacAssignments'
  scope: rg
  params: {
    storageAccountName: storage.outputs.name
    appInsightsName: applicationInsights.outputs.name
    managedIdentityPrincipalId: functionApp.outputs.?systemAssignedMIPrincipalId ?? ''
    userIdentityPrincipalId: principalId
    allowUserIdentityPrincipal: !empty(principalId)
  }
}

// Outputs
output AZURE_LOCATION string = location
output AZURE_TENANT_ID string = tenant().tenantId
output AZURE_FUNCTION_NAME string = functionApp.outputs.name
output APPLICATIONINSIGHTS_CONNECTION_STRING string = applicationInsights.outputs.connectionString
```

This example uses the [AVM for function apps](https://github.com/Azure/bicep-registry-modules/tree/main/avm/res/web/serverfarm). For the snippet in context, see [this deployment example](https://github.com/Azure-Samples/azure-functions-flex-consumption-samples/blob/main/IaC/bicep/main.bicep#L173).

Note

If you choose to optionally define your Consumption plan, you must set the `serverFarmId` property on the app so that it points to the resource ID of the plan. Make sure that the function app has a `dependsOn` setting that also references the plan. If you didn't explicitly define a plan, one gets created for you.

Set the `serverFarmId` property on the app so that it points to the resource ID of the plan. Make sure that the function app has a `dependsOn` setting that also references the plan.

*   [Windows](https://learn.microsoft.com/en-us/azure/azure-functions/functions-infrastructure-as-code#tabpanel_15_windows_bicep)
*   [Linux](https://learn.microsoft.com/en-us/azure/azure-functions/functions-infrastructure-as-code#tabpanel_15_linux_bicep)

```
resource functionApp 'Microsoft.Web/sites@2021-02-01' = {
  name: functionAppName
  location: location
  kind: 'functionapp,linux'
  properties: {
    reserved: true
    serverFarmId: hostingPlan.id
    siteConfig: {
      linuxFxVersion: 'node|14'
      appSettings: [
        {
          name: 'APPLICATIONINSIGHTS_CONNECTION_STRING'
          value: applicationInsightsName.properties.ConnectionString
        }
        {
          name: 'AzureWebJobsStorage'
          value: 'DefaultEndpointsProtocol=https;AccountName=${storageAccountName};EndpointSuffix=${environment().suffixes.storage};AccountKey=${storageAccount.listKeys().keys[0].value}'
        }
        {
          name: 'WEBSITE_CONTENTAZUREFILECONNECTIONSTRING'
          value: 'DefaultEndpointsProtocol=https;AccountName=${storageAccountName};EndpointSuffix=${environment().suffixes.storage};AccountKey=${storageAccount.listKeys().keys[0].value}'
        }
        {
          name: 'WEBSITE_CONTENTSHARE'
          value: toLower(functionAppName)
        }
        {
          name: 'FUNCTIONS_EXTENSION_VERSION'
          value: '~4'
        }
        {
          name: 'FUNCTIONS_WORKER_RUNTIME'
          value: 'node'
        }
      ]
    }
  }
}
```

For a complete end-to-end example, see this [main.bicep file](https://github.com/Azure-Samples/function-app-arm-templates/blob/main/function-app-linux-consumption/main.bicep).

*   [Windows](https://learn.microsoft.com/en-us/azure/azure-functions/functions-infrastructure-as-code#tabpanel_16_windows_bicep)
*   [Linux](https://learn.microsoft.com/en-us/azure/azure-functions/functions-infrastructure-as-code#tabpanel_16_linux_bicep)

```
resource functionApp 'Microsoft.Web/sites@2022-03-01' = {
  name: functionAppName
  location: location
  kind: 'functionapp,linux'
  properties: {
    reserved: true
    serverFarmId: hostingPlan.id
    siteConfig: {
      alwaysOn: true
      linuxFxVersion: 'node|14'
      appSettings: [
        {
          name: 'APPLICATIONINSIGHTS_CONNECTION_STRING'
          value: applicationInsightsName.properties.ConnectionString
        }
        {
          name: 'AzureWebJobsStorage'
          value: 'DefaultEndpointsProtocol=https;AccountName=${storageAccountName};EndpointSuffix=${environment().suffixes.storage};AccountKey=${storageAccount.listKeys().keys[0].value}'
        }
        {
          name: 'FUNCTIONS_EXTENSION_VERSION'
          value: '~4'
        }
        {
          name: 'FUNCTIONS_WORKER_RUNTIME'
          value: 'node'
        }
      ]
    }
  }
}
```

For a complete end-to-end example, see this [main.bicep file](https://github.com/Azure-Samples/function-app-arm-templates/blob/main/function-app-dedicated-plan/main.bicep).

You can use the [`linuxFxVersion`](https://learn.microsoft.com/en-us/azure/azure-functions/functions-app-settings#linuxfxversion) site setting to request that a specific Linux container be deployed to your app when it's created. More settings are required to access images in a private repository. For more information, see [Application configuration](https://learn.microsoft.com/en-us/azure/azure-functions/functions-infrastructure-as-code#application-configuration).

Important

When you create your own containers, you're required to keep the base image of your container updated to the latest supported base image. Supported base images for Azure Functions are language-specific. See the [Azure Functions base image repos](https://mcr.microsoft.com/catalog?search=functions).

The Functions team is committed to publishing monthly updates for these base images. Regular updates include the latest minor version updates and security fixes for both the Functions runtime and languages. You should regularly update your container from the latest base image and redeploy the updated version of your container. For more information, see [Maintaining custom containers](https://learn.microsoft.com/en-us/azure/azure-functions/container-concepts#maintaining-custom-containers).

The Flex Consumption plan maintains your project code in zip-compressed package file in a blob storage container known as the _deployment container_. You can configure both the storage account and container used for deployment. For more information, see [Deployment](https://learn.microsoft.com/en-us/azure/azure-functions/flex-consumption-plan#deployment).

You must use _[one deploy](https://learn.microsoft.com/en-us/azure/azure-functions/functions-deployment-technologies#one-deploy)_ to publish your code package to the deployment container. During an ARM template or Bicep deployment, you can do this by [defining a package source](https://learn.microsoft.com/en-us/azure/azure-functions/functions-infrastructure-as-code#deployment-package) that uses the `/onedeploy` extension. If you choose to instead directly upload your package to the container, the package doesn't get automatically deployed.

The specific storage account and container used for deployments, the authentication method, and credentials are set in the `functionAppConfig.deployment.storage` element of the `properties` for the site. The container and any application settings must exist when the app is created. For an example of how to create the storage container, see [Deployment container](https://learn.microsoft.com/en-us/azure/azure-functions/functions-infrastructure-as-code#deployment-container).

This example uses a system assigned managed identity to access the specified blob storage container, which is created elsewhere in the deployment:

*   [Bicep](https://learn.microsoft.com/en-us/azure/azure-functions/functions-infrastructure-as-code#tabpanel_17_bicep)
*   [ARM template](https://learn.microsoft.com/en-us/azure/azure-functions/functions-infrastructure-as-code#tabpanel_17_json)

```
// Consolidated Role Assignments
module rbacAssignments 'rbac.bicep' = {
  name: 'rbacAssignments'
  scope: rg
  params: {
    storageAccountName: storage.outputs.name
    appInsightsName: applicationInsights.outputs.name
    managedIdentityPrincipalId: functionApp.outputs.?systemAssignedMIPrincipalId ?? ''
    userIdentityPrincipalId: principalId
    allowUserIdentityPrincipal: !empty(principalId)
  }
}

// Outputs
output AZURE_LOCATION string = location
output AZURE_TENANT_ID string = tenant().tenantId
output AZURE_FUNCTION_NAME string = functionApp.outputs.name
output APPLICATIONINSIGHTS_CONNECTION_STRING string = applicationInsights.outputs.connectionString
```

This example uses the [AVM for function apps](https://github.com/Azure/bicep-registry-modules/tree/main/avm/res/web/site). For the snippet in context, see [this deployment example](https://github.com/Azure-Samples/azure-functions-flex-consumption-samples/blob/main/IaC/bicep/main.bicep#L185).

When using managed identities, you must also enable the function app to access the storage account using the identity, as shown in this example:

*   [Bicep](https://learn.microsoft.com/en-us/azure/azure-functions/functions-infrastructure-as-code#tabpanel_18_bicep)
*   [ARM template](https://learn.microsoft.com/en-us/azure/azure-functions/functions-infrastructure-as-code#tabpanel_18_json)

```
module storageRoleAssignment_User 'br/public:avm/ptn/authorization/resource-role-assignment:0.1.2' = if (allowUserIdentityPrincipal && !empty(userIdentityPrincipalId)) {
  name: 'storageRoleAssignment-User-${uniqueString(storageAccount.id, userIdentityPrincipalId)}'
  params: {
    resourceId: storageAccount.id
    roleDefinitionId: roleDefinitions.storageBlobDataOwner
    principalId: userIdentityPrincipalId
    principalType: 'User'
    description: 'Storage Blob Data Owner role for user identity (development/testing)'
    roleName: 'Storage Blob Data Owner'
  }
}
```

This example uses the [AVM for resource-scoped role assignment](https://github.com/Azure/bicep-registry-modules/tree/main/avm/ptn/authorization/resource-role-assignment). For the snippet in context, see [this deployment example](https://github.com/Azure-Samples/azure-functions-flex-consumption-samples/blob/main/IaC/bicep/rbac.bicep#L45).

This example requires you to know the GUID value for the role being assigned. You can get this ID value for any friendly role name by using the [az role definition list](https://learn.microsoft.com/en-us/cli/azure/role/definition#az-role-definition-list) command, as in this example:

```
az role definition list --output tsv --query "[?roleName=='Storage Blob Data Owner'].{name:name}"
```

When using a connection string instead of managed identities, you need to instead set the `authentication.type` to `StorageAccountConnectionString` and set `authentication.storageAccountConnectionStringName` to the name of the application setting that contains the deployment storage account connection string.

The Flex Consumption plan uses _one deploy_ for deploying your code project. The code package itself is the same as you would use for zip deployment in other Functions hosting plans. However, the name of the package file itself must be `released-package.zip`.

To include a one deploy package in your template, use the `/onedeploy` resource definition for the remote URL that contains the deployment package. The Functions host must be able to access both this remote package source and the deployment container.

This example adds a one deploy source to an existing app:

*   [Bicep](https://learn.microsoft.com/en-us/azure/azure-functions/functions-infrastructure-as-code#tabpanel_19_bicep)
*   [ARM template](https://learn.microsoft.com/en-us/azure/azure-functions/functions-infrastructure-as-code#tabpanel_19_json)

```
@description('The name of the function app.')
param functionAppName string

@description('The location into which the resources should be deployed.')
param location string = resourceGroup().location

@description('The zip content URL for released-package.zip.')
param packageUri string

resource functionAppName_OneDeploy 'Microsoft.Web/sites/extensions@2022-09-01' = {
  name: '${functionAppName}/onedeploy'
  location: location
  properties: {
    packageUri: packageUri
    remoteBuild: false 
  }
}
```

Your Bicep file or ARM template can optionally also define a deployment for your function code using a [zip deployment package](https://learn.microsoft.com/en-us/azure/azure-functions/deployment-zip-push).

To successfully deploy your application by using Azure Resource Manager, it's important to understand how resources are deployed in Azure. In most examples, top-level configurations are applied by using `siteConfig`. It's important to set these configurations at a top level, because they convey information to the Functions runtime and deployment engine. Top-level information is required before the child `sourcecontrols/web` resource is applied. Although it's possible to configure these settings in the child-level `config/appSettings` resource, in some cases your function app must be deployed _before_`config/appSettings` is applied.

Zip deployment is a recommended way to deploy your function app code. By default, functions that use zip deployment run in the deployment package itself. For more information, including the requirements for a deployment package, see [Zip deployment for Azure Functions](https://learn.microsoft.com/en-us/azure/azure-functions/deployment-zip-push). When using resource deployment automation, you can reference the .zip deployment package in your Bicep or ARM template.

To use zip deployment in your template, set the `WEBSITE_RUN_FROM_PACKAGE` setting in the app to `1` and include the `/zipDeploy` resource definition.

For a Consumption plan on Linux, instead set the URI of the deployment package directly in the `WEBSITE_RUN_FROM_PACKAGE` setting, as shown in [this example template](https://github.com/Azure-Samples/function-app-arm-templates/tree/main/function-app-linux-consumption#L152).

This example adds a zip deployment source to an existing app:

*   [Bicep](https://learn.microsoft.com/en-us/azure/azure-functions/functions-infrastructure-as-code#tabpanel_20_bicep)
*   [ARM template](https://learn.microsoft.com/en-us/azure/azure-functions/functions-infrastructure-as-code#tabpanel_20_json)

```
@description('The name of the function app.')
param functionAppName string

@description('The location into which the resources should be deployed.')
param location string = resourceGroup().location

@description('The zip content url.')
param packageUri string

resource functionAppName_ZipDeploy 'Microsoft.Web/sites/extensions@2021-02-01' = {
  name: '${functionAppName}/ZipDeploy'
  location: location
  properties: {
    packageUri: packageUri
  }
}
```

Keep the following things in mind when including zip deployment resources in your template:

*   Consumption plans on Linux don't support `WEBSITE_RUN_FROM_PACKAGE = 1`. You must instead set the URI of the deployment package directly in the `WEBSITE_RUN_FROM_PACKAGE` setting. For more information, see [WEBSITE_RUN_FROM_PACKAGE](https://learn.microsoft.com/en-us/azure/azure-functions/functions-app-settings#website_run_from_package). For an example template, see [Function app hosted on Linux in a Consumption plan](https://github.com/Azure-Samples/function-app-arm-templates/tree/main/function-app-linux-consumption).

*   The `packageUri` must be a location that can be accessed by Functions. Consider using Azure blob storage with a shared access signature (SAS). After the SAS expires, Functions can no longer access the share for deployments. When you regenerate your SAS, remember to update the `WEBSITE_RUN_FROM_PACKAGE` setting with the new URI value.

*   When setting `WEBSITE_RUN_FROM_PACKAGE` to a URI, you must [manually sync triggers](https://learn.microsoft.com/en-us/azure/azure-functions/functions-deployment-technologies#trigger-syncing).

*   Make sure to always set all required application settings in the `appSettings` collection when adding or updating settings. Existing settings not explicitly set are removed by the update. For more information, see [Application configuration](https://learn.microsoft.com/en-us/azure/azure-functions/functions-infrastructure-as-code#application-configuration).

*   Functions doesn't support Web Deploy (`msdeploy`) for package deployments. You must instead use zip deployment in your deployment pipelines and automation. For more information, see [Zip deployment for Azure Functions](https://learn.microsoft.com/en-us/azure/azure-functions/deployment-zip-push).

The deployment process assumes that the .zip file that you use or a zip deployment contains a ready-to-run app. This means that by default no customizations are run.

There are scenarios that require you to rebuild your app remotely. One such example is when you need to include Linux-specific packages in Python or Node.js apps that you developed on a Windows computer. In this case, you can configure Functions to perform a remote build on your code after the zip deployment.

The way that you request a remote build depends on the operating system to which you're deploying:

*   [Windows](https://learn.microsoft.com/en-us/azure/azure-functions/functions-infrastructure-as-code#tabpanel_21_windows)
*   [Linux](https://learn.microsoft.com/en-us/azure/azure-functions/functions-infrastructure-as-code#tabpanel_21_linux)

To enable the same build processes that you get with continuous integration, add `SCM_DO_BUILD_DURING_DEPLOYMENT=true` to your application settings in your deployment code and remove the `WEBSITE_RUN_FROM_PACKAGE` entirely.

The `ENABLE_ORYX_BUILD` setting is set to `true` by default. If you have issues building a .NET or Java function app, instead set it to `false`.

Function apps that are built remotely on Linux can run from a package.

If you're deploying a [containerized function app](https://learn.microsoft.com/en-us/azure/azure-functions/functions-how-to-custom-container) to an Azure Functions Premium or Dedicated plan, you must:

*   Set the [`linuxFxVersion`](https://learn.microsoft.com/en-us/azure/azure-functions/functions-app-settings#linuxfxversion) site setting with the identifier of your container image.
*   Set any required [`DOCKER_REGISTRY_SERVER_*`](https://learn.microsoft.com/en-us/azure/azure-functions/functions-infrastructure-as-code?tabs=linux#application-configuration) settings when obtaining the container from a private registry.
*   Set [`WEBSITES_ENABLE_APP_SERVICE_STORAGE`](https://learn.microsoft.com/en-us/azure/app-service/reference-app-settings#custom-containers) application setting to `false`.

If some settings are missing, the application provisioning might fail with this HTTP/500 error:

> `Function app provisioning failed.`

For more information, see [Application configuration](https://learn.microsoft.com/en-us/azure/azure-functions/functions-infrastructure-as-code#application-configuration).

*   [Bicep](https://learn.microsoft.com/en-us/azure/azure-functions/functions-infrastructure-as-code#tabpanel_22_bicep)
*   [ARM template](https://learn.microsoft.com/en-us/azure/azure-functions/functions-infrastructure-as-code#tabpanel_22_json)

```
resource functionApp 'Microsoft.Web/sites@2022-03-01' = {
  name: functionAppName
  location: location
  kind: 'functionapp'
  properties: {
    serverFarmId: hostingPlan.id
    siteConfig: {
      appSettings: [
        {
          name: 'AzureWebJobsStorage'
          value: 'DefaultEndpointsProtocol=https;AccountName=${storageAccountName};AccountKey=${storageAccount.listKeys().keys[0].value}'
        }
        {
          name: 'FUNCTIONS_WORKER_RUNTIME'
          value: 'node'
        }
        {
          name: 'WEBSITE_NODE_DEFAULT_VERSION'
          value: '~14'
        }
        {
          name: 'FUNCTIONS_EXTENSION_VERSION'
          value: '~4'
        }
        {
          name: 'DOCKER_REGISTRY_SERVER_URL'
          value: dockerRegistryUrl
        }
        {
          name: 'DOCKER_REGISTRY_SERVER_USERNAME'
          value: dockerRegistryUsername
        }
        {
          name: 'DOCKER_REGISTRY_SERVER_PASSWORD'
          value: dockerRegistryPassword
        }
        {
          name: 'WEBSITES_ENABLE_APP_SERVICE_STORAGE'
          value: 'false'
        }
      ]
      linuxFxVersion: 'DOCKER|myacr.azurecr.io/myimage:mytag'
    }
  }
  dependsOn: [
    storageAccount
  ]
}
```

When deploying [containerized functions to Azure Container Apps](https://learn.microsoft.com/en-us/azure/container-apps/functions-overview), your template must:

*   Set the `kind` field to a value of `functionapp,linux,container,azurecontainerapps`.
*   Set the `managedEnvironmentId` site property to the fully qualified URI of the Container Apps environment.
*   Add a resource link in the site's `dependsOn` collection when creating a `Microsoft.App/managedEnvironments` resource at the same time as the site.

The definition of a containerized function app deployed from a private container registry to an existing Container Apps environment might look like this example:

*   [Bicep](https://learn.microsoft.com/en-us/azure/azure-functions/functions-infrastructure-as-code#tabpanel_23_bicep)
*   [ARM template](https://learn.microsoft.com/en-us/azure/azure-functions/functions-infrastructure-as-code#tabpanel_23_json)

```
resource functionApp 'Microsoft.Web/sites@2022-03-01' = {
  name: functionAppName
  kind: 'functionapp,linux,container,azurecontainerapps'
  location: location
  properties: {
    serverFarmId: hostingPlanName
    siteConfig: {
      linuxFxVersion: 'DOCKER|myacr.azurecr.io/myimage:mytag'
      appSettings: [
        {
          name: 'FUNCTIONS_EXTENSION_VERSION'
          value: '~4'
        }
        {
          name: 'AzureWebJobsStorage'
          value: 'DefaultEndpointsProtocol=https;AccountName=${storageAccountName};AccountKey=${storageAccount.listKeys().keys[0].value}'
        }
        {
          name: 'APPLICATIONINSIGHTS_CONNECTION_STRING'
          value: applicationInsightsName.properties.ConnectionString
        }
      ]
    }
    managedEnvironmentId: managedEnvironmentId
  }
  dependsOn: [
    storageAccount
    hostingPlan
  ]
}
```

When deploying functions to Azure Arc, the value you set for the `kind` field of the function app resource depends on the type of deployment:

| Deployment type | `kind` field value |
| --- | --- |
| Code-only deployment | `functionapp,linux,kubernetes` |
| Container deployment | `functionapp,linux,kubernetes,container` |

You must also set the `customLocationId` as you did for the [hosting plan resource](https://learn.microsoft.com/en-us/azure/azure-functions/functions-infrastructure-as-code#create-the-hosting-plan).

The definition of a containerized function app, using a .NET 6 quickstart image, might look like this example:

*   [Bicep](https://learn.microsoft.com/en-us/azure/azure-functions/functions-infrastructure-as-code#tabpanel_24_bicep)
*   [ARM template](https://learn.microsoft.com/en-us/azure/azure-functions/functions-infrastructure-as-code#tabpanel_24_json)

```
resource functionApp 'Microsoft.Web/sites@2022-03-01' = {
  name: functionAppName
  kind: 'kubernetes,functionapp,linux,container'
  location: location
  extendedLocation: {
    name: customLocationId
  }
  properties: {
    serverFarmId: hostingPlanName
    siteConfig: {
      linuxFxVersion: 'DOCKER|mcr.microsoft.com/azure-functions/4-dotnet-isolated6.0-appservice-quickstart'
      appSettings: [
        {
          name: 'FUNCTIONS_EXTENSION_VERSION'
          value: '~4'
        }
        {
          name: 'AzureWebJobsStorage'
          value: 'DefaultEndpointsProtocol=https;AccountName=${storageAccountName};AccountKey=${storageAccount.listKeys().keys[0].value}'
        }
        {
          name: 'APPLICATIONINSIGHTS_CONNECTION_STRING'
          value: applicationInsightsName.properties.ConnectionString
        }
      ]
      alwaysOn: true
    }
  }
  dependsOn: [
    storageAccount
    hostingPlan
  ]
}
```

In a Flex Consumption plan, you configure your function app in Azure with two types of properties:

| Configuration | `Microsoft.Web/sites` property |
| --- | --- |
| Application configuration | `functionAppConfig` |
| Application settings | `siteConfig.appSettings` collection |

These application configurations are maintained in `functionAppConfig`:

| Behavior | Setting in `functionAppConfig` |
| --- | --- |
| [Always ready instances](https://learn.microsoft.com/en-us/azure/azure-functions/flex-consumption-plan#always-ready-instances) | `scaleAndConcurrency.alwaysReady` |
| [Deployment source](https://learn.microsoft.com/en-us/azure/azure-functions/functions-infrastructure-as-code#deployment-sources) | `deployment` |
| [Instance size](https://learn.microsoft.com/en-us/azure/azure-functions/flex-consumption-plan#instance-sizes) | `scaleAndConcurrency.instanceMemoryMB` |
| [HTTP trigger concurrency](https://learn.microsoft.com/en-us/azure/azure-functions/functions-concurrency#http-trigger-concurrency) | `scaleAndConcurrency.triggers.http.perInstanceConcurrency` |
| [Language runtime](https://learn.microsoft.com/en-us/azure/azure-functions/functions-app-settings#functions_worker_runtime) | `runtime.name` |
| [Language version](https://learn.microsoft.com/en-us/azure/azure-functions/supported-languages) | `runtime.version` |
| [Maximum instance count](https://learn.microsoft.com/en-us/azure/azure-functions/event-driven-scaling#flex-consumption-plan) | `scaleAndConcurrency.maximumInstanceCount` |
| [Site update strategy](https://learn.microsoft.com/en-us/azure/azure-functions/flex-consumption-site-updates) | `siteUpdateStrategy.type` |

The Flex Consumption plan also supports these application settings:

*   Connection string-based settings: 
    *   [`APPLICATIONINSIGHTS_CONNECTION_STRING`](https://learn.microsoft.com/en-us/azure/azure-functions/functions-app-settings#applicationinsights_connection_string)
    *   [`AzureWebJobsStorage`](https://learn.microsoft.com/en-us/azure/azure-functions/functions-app-settings#azurewebjobsstorage)

*   Managed identity-based settings: 
    *   [`APPLICATIONINSIGHTS_AUTHENTICATION_STRING`](https://learn.microsoft.com/en-us/azure/azure-functions/functions-app-settings#applicationinsights_authentication_string)
    *   [`AzureWebJobsStorage__accountName`](https://learn.microsoft.com/en-us/azure/azure-functions/functions-app-settings#azurewebjobsstorage__accountname)

Functions provides the following options for configuring your function app in Azure:

| Configuration | `Microsoft.Web/sites` property |
| --- | --- |
| Site settings | `siteConfig` |
| Application settings | `siteConfig.appSettings` collection |

These site settings are required on the `siteConfig` property:

*   [Windows](https://learn.microsoft.com/en-us/azure/azure-functions/functions-infrastructure-as-code#tabpanel_25_windows)
*   [Linux](https://learn.microsoft.com/en-us/azure/azure-functions/functions-infrastructure-as-code#tabpanel_25_linux)

*   [`alwaysOn`](https://learn.microsoft.com/en-us/azure/azure-functions/functions-app-settings#alwayson)
*   [`linuxFxVersion`](https://learn.microsoft.com/en-us/azure/azure-functions/functions-app-settings#linuxfxversion)
*   [`netFrameworkVersion`](https://learn.microsoft.com/en-us/azure/azure-functions/functions-app-settings#netframeworkversion)

*   [Windows](https://learn.microsoft.com/en-us/azure/azure-functions/functions-infrastructure-as-code#tabpanel_26_windows)
*   [Linux](https://learn.microsoft.com/en-us/azure/azure-functions/functions-infrastructure-as-code#tabpanel_26_linux)

*   [`linuxFxVersion`](https://learn.microsoft.com/en-us/azure/azure-functions/functions-app-settings#linuxfxversion)
*   [`netFrameworkVersion`](https://learn.microsoft.com/en-us/azure/azure-functions/functions-app-settings#netframeworkversion) (C#/PowerShell-only)

*   [`linuxFxVersion`](https://learn.microsoft.com/en-us/azure/azure-functions/functions-app-settings#linuxfxversion)

*   [`alwaysOn`](https://learn.microsoft.com/en-us/azure/azure-functions/functions-app-settings#alwayson)
*   [`linuxFxVersion`](https://learn.microsoft.com/en-us/azure/azure-functions/functions-app-settings#linuxfxversion)

These application settings are required (or recommended) for a specific operating system and hosting option:

*   [Windows](https://learn.microsoft.com/en-us/azure/azure-functions/functions-infrastructure-as-code#tabpanel_27_windows)
*   [Linux](https://learn.microsoft.com/en-us/azure/azure-functions/functions-infrastructure-as-code#tabpanel_27_linux)

*   [`APPLICATIONINSIGHTS_CONNECTION_STRING`](https://learn.microsoft.com/en-us/azure/azure-functions/functions-app-settings#applicationinsights_connection_string)
*   [`AzureWebJobsStorage`](https://learn.microsoft.com/en-us/azure/azure-functions/functions-app-settings#azurewebjobsstorage)
*   [`FUNCTIONS_EXTENSION_VERSION`](https://learn.microsoft.com/en-us/azure/azure-functions/functions-app-settings#functions_extension_version)
*   [`FUNCTIONS_WORKER_RUNTIME`](https://learn.microsoft.com/en-us/azure/azure-functions/functions-app-settings#functions_worker_runtime)
*   [`WEBSITE_CONTENTAZUREFILECONNECTIONSTRING`](https://learn.microsoft.com/en-us/azure/azure-functions/functions-app-settings#website_contentazurefileconnectionstring)
*   [`WEBSITE_CONTENTSHARE`](https://learn.microsoft.com/en-us/azure/azure-functions/functions-app-settings#website_contentshare)

Keep these considerations in mind when working with site and application settings using Bicep files or ARM templates:

*   The optional `alwaysReady` setting contains an array of one or more `{name,instanceCount}` objects, with one for each [per-function scale group](https://learn.microsoft.com/en-us/azure/azure-functions/flex-consumption-plan#per-function-scaling). These are the scale groups being used to make always-ready scale decisions. This example sets always-ready counts for both the `http` group and a single function named `helloworld`, which is of a nongrouped trigger type:

    *   [Bicep](https://learn.microsoft.com/en-us/azure/azure-functions/functions-infrastructure-as-code#tabpanel_30_bicep)
    *   [ARM template](https://learn.microsoft.com/en-us/azure/azure-functions/functions-infrastructure-as-code#tabpanel_30_json)

```
alwaysReady: [
    {
      name: 'http'
      instanceCount: 2
    }
    {
      name: 'function:helloworld'
      instanceCount: 1
    }
  ]
```

*   There are important considerations for when you should set `WEBSITE_CONTENTSHARE` in an automated deployment. For detailed guidance, see the [`WEBSITE_CONTENTSHARE`](https://learn.microsoft.com/en-us/azure/azure-functions/functions-app-settings#website_contentshare) reference.

*   For container deployments, also set [`WEBSITES_ENABLE_APP_SERVICE_STORAGE`](https://learn.microsoft.com/en-us/azure/app-service/reference-app-settings#custom-containers) to `false`, since your app content is provided in the container itself.

*   You should always define your application settings as a `siteConfig/appSettings` collection of the `Microsoft.Web/sites` resource being created, as is done in the examples in this article. This definition guarantees the settings your function app needs to run are available on initial startup.

*   When adding or updating application settings using templates, make sure that you include all existing settings with the update. You must do this because the underlying update REST API calls replace the entire `/config/appsettings` resource. If you remove the existing settings, your function app won't run. To programmatically update individual application settings, you can instead use the Azure CLI, Azure PowerShell, or the Azure portal to make these changes. For more information, see [Work with application settings](https://learn.microsoft.com/en-us/azure/azure-functions/functions-how-to-use-azure-function-app-settings#settings).

*   When possible, you should use managed identity-based connections to other Azure services, including the `AzureWebJobsStorage` connection. For more information, see [Configure an identity-based connection](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference#configure-an-identity-based-connection).

Functions lets you deploy different versions of your code to unique endpoints in your function app. This option makes it easier to develop, validate, and deploy functions updates without impacting functions running in production. Deployment slots is a feature of Azure App Service. The number of slots available [depends on your hosting plan](https://learn.microsoft.com/en-us/azure/azure-functions/functions-scale#service-limits). For more information, see [Azure Functions deployment slots](https://learn.microsoft.com/en-us/azure/azure-functions/functions-deployment-slots) functions.

A slot resource is defined in the same way as a function app resource (`Microsoft.Web/sites`), but instead you use the `Microsoft.Web/sites/slots` resource identifier. For an example deployment (in both Bicep and ARM templates) that creates both a production and a staging slot in a Premium plan, see [Azure Function App with a Deployment Slot](https://github.com/Azure-Samples/function-app-arm-templates/blob/main/function-app-deployment-slot).

To learn about how to swap slots by using templates, see [Automate with Resource Manager templates](https://learn.microsoft.com/en-us/azure/app-service/deploy-staging-slots#automate-with-resource-manager-templates).

Keep the following considerations in mind when working with slot deployments:

*   Don't explicitly set the `WEBSITE_CONTENTSHARE` setting in the deployment slot definition. This setting is generated for you when the app is created in the deployment slot.

*   When you swap slots, some application settings are considered "sticky," in that they stay with the slot and not with the code being swapped. You can define such a _slot setting_ by including `"slotSetting":true` in the specific application setting definition in your template. For more information, see [Manage settings](https://learn.microsoft.com/en-us/azure/azure-functions/functions-deployment-slots#manage-settings).

You can create your function app in a deployment where one or more of the resources have been secured by integrating with virtual networks. Virtual network integration for your function app is defined by a `Microsoft.Web/sites/networkConfig` resource. This integration depends on both the referenced function app and virtual network resources. Your function app might also depend on other private networking resources, such as private endpoints and routes. For more information, see [Azure Functions networking options](https://learn.microsoft.com/en-us/azure/azure-functions/functions-networking-options).

When creating a deployment that uses a secured storage account, you must both explicitly set the `WEBSITE_CONTENTSHARE` setting and create the file share resource named in this setting. Make sure you create a `Microsoft.Storage/storageAccounts/fileServices/shares` resource using the value of `WEBSITE_CONTENTSHARE`, as shown in this example ([ARM template](https://github.com/Azure-Samples/function-app-arm-templates/blob/main/function-app-private-endpoints-storage-private-endpoints/azuredeploy.json#L467)|[Bicep file](https://github.com/Azure-Samples/function-app-arm-templates/blob/main/function-app-private-endpoints-storage-private-endpoints/main.bicep#L351)). You'll also need to set the site property `vnetContentShareEnabled` to true.

Note

When these settings aren't part of a deployment that uses a secured storage account, you see this error during deployment validation: `Could not access storage account using provided connection string`.

These projects provide both Bicep and ARM template examples of how to deploy your function apps in a virtual network, including with network access restrictions:

| Restricted scenario | Description |
| --- | --- |
| [Create a function app with virtual network integration](https://github.com/Azure-Samples/function-app-arm-templates/tree/main/function-app-vnet-integration) | Your function app is created in a virtual network with full access to resources in that network. Inbound and outbound access to your function app isn't restricted. For more information, see [Virtual network integration](https://learn.microsoft.com/en-us/azure/azure-functions/functions-networking-options#virtual-network-integration). |
| [Create a function app that accesses a secured storage account](https://github.com/Azure-Samples/function-app-arm-templates/blob/main/function-app-storage-private-endpoints) | Your created function app uses a secured storage account, which Functions accesses by using private endpoints. For more information, see [Restrict your storage account to a virtual network](https://learn.microsoft.com/en-us/azure/azure-functions/configure-networking-how-to#restrict-your-storage-account-to-a-virtual-network). |
| [Create a function app and storage account that both use private endpoints](https://github.com/Azure-Samples/function-app-arm-templates/tree/main/function-app-private-endpoints-storage-private-endpoints) | Your created function app can only be accessed by using private endpoints, and it uses private endpoints to access storage resources. For more information, see [Private endpoints](https://learn.microsoft.com/en-us/azure/azure-functions/functions-networking-options#private-endpoints). |

You might also need to use these settings when your function app has network restrictions:

| Setting | Value | Description |
| --- | --- | --- |
| [`WEBSITE_CONTENTOVERVNET`](https://learn.microsoft.com/en-us/azure/azure-functions/functions-app-settings#website_contentovervnet) | `1` | Application setting that enables your function app to scale when the storage account is restricted to a virtual network. For more information, see [Restrict your storage account to a virtual network](https://learn.microsoft.com/en-us/azure/azure-functions/functions-networking-options#restrict-your-storage-account-to-a-virtual-network). |
| [`vnetrouteallenabled`](https://learn.microsoft.com/en-us/azure/azure-functions/functions-app-settings#vnetrouteallenabled) | `1` | Site setting that forces all traffic from the function app to use the virtual network. For more information, see [Regional virtual network integration](https://learn.microsoft.com/en-us/azure/azure-functions/functions-networking-options#regional-virtual-network-integration). This site setting supersedes the application setting [`WEBSITE_VNET_ROUTE_ALL`](https://learn.microsoft.com/en-us/azure/azure-functions/functions-app-settings#website_vnet_route_all). |

When you're restricting access to the storage account through the private endpoints, you aren't able to access the storage account through the portal or any device outside the virtual network. You can give access to your secured IP address or virtual network in the storage account by [Managing the default network access rule](https://learn.microsoft.com/en-us/azure/storage/common/storage-network-security-set-default-access).

Host-level [function access keys](https://learn.microsoft.com/en-us/azure/azure-functions/function-keys-how-to) are defined as Azure resources. This means that you can create and manage host keys in your ARM templates and Bicep files. A host key is defined as a resource of type `Microsoft.Web/sites/host/functionKeys`. This example creates a host-level access key named `my_custom_key` when the function app is created:

*   [Bicep](https://learn.microsoft.com/en-us/azure/azure-functions/functions-infrastructure-as-code#tabpanel_31_bicep)
*   [ARM template](https://learn.microsoft.com/en-us/azure/azure-functions/functions-infrastructure-as-code#tabpanel_31_json)

```
resource functionKey 'Microsoft.Web/sites/host/functionKeys@2022-09-01' = {
  name: '${parameters('name')}/default/my_custom_key'
  properties: {
    name: 'my_custom_key'
  }
  dependsOn: [
    resourceId('Microsoft.Web/Sites', parameters('name'))
  ]
}
```

In this example, the `name` parameter is the name of the new function app. You must include a `dependsOn` setting to guarantee that the key is created with the new function app. Finally, the `properties` object of the host key can also include a `value` property that can be used to set a specific key.

When you don't set the `value` property, Functions automatically generates a new key for you when the resource is created, which is recommended. To learn more about access keys, including security best practices for working with access keys, see [Work with access keys in Azure Functions](https://learn.microsoft.com/en-us/azure/azure-functions/function-keys-how-to).

Experts with Bicep or ARM templates can manually code their deployments using a simple text editor. For the rest of us, there are several ways to make the development process easier:

*   **Visual Studio Code**: There are extensions available to help you work with both [Bicep files](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-bicep) and [ARM templates](https://marketplace.visualstudio.com/items?itemName=msazurermtools.azurerm-vscode-tools). You can use these tools to help make sure that your code is correct, and they provide some [basic validation](https://learn.microsoft.com/en-us/azure/azure-functions/functions-infrastructure-as-code?tabs=vs-code#validate-your-template).

*   **Azure portal**: When you [create your function app and related resources in the portal](https://learn.microsoft.com/en-us/azure/azure-functions/functions-create-function-app-portal), the final **Review + create** screen has a **Download a template for automation** link.

![Image 1: Download template link from the Azure Functions creation process in the Azure portal.](https://learn.microsoft.com/en-us/azure/azure-functions/media/functions-infrastructure-as-code/portal-download-template.png)

This link shows you the ARM template generated based on the options you chose in portal. This template can seem a bit complex when you're creating a function app with many new resources. However, it can provide a good reference for how your ARM template might look.

When you manually create your deployment template file, it's important to validate your template before deployment. All deployment methods validate your template syntax and raise a `validation failed` error message as shown in the following JSON formatted example:

```
{"error":{"code":"InvalidTemplate","message":"Deployment template validation failed: 'The resource 'Microsoft.Web/sites/func-xyz' is not defined in the template. Please see https://aka.ms/arm-template for usage details.'.","additionalInfo":[{"type":"TemplateViolation","info":{"lineNumber":0,"linePosition":0,"path":""}}]}}
```

The following methods can be used to validate your template before deployment:

*   [Azure Pipelines](https://learn.microsoft.com/en-us/azure/azure-functions/functions-infrastructure-as-code#tabpanel_32_devops)
*   [Azure CLI](https://learn.microsoft.com/en-us/azure/azure-functions/functions-infrastructure-as-code#tabpanel_32_azure-cli)
*   [Visual Studio Code](https://learn.microsoft.com/en-us/azure/azure-functions/functions-infrastructure-as-code#tabpanel_32_vs-code)

The following [Azure resource group deployment v2 task](https://learn.microsoft.com/en-us/azure/devops/pipelines/tasks/deploy/azure-resource-group-deployment?view=azure-devops&preserve-view=true) with `deploymentMode: 'Validation'` instructs Azure Pipelines to validate the template.

```
- task: AzureResourceManagerTemplateDeployment@3
  inputs:
    deploymentScope: 'Resource Group'
    subscriptionId: # Required subscription ID
    action: 'Create Or Update Resource Group'
    resourceGroupName: # Required resource group name
    location: # Required when action == Create Or Update Resource Group
    templateLocation: 'Linked artifact'
    csmFile: # Required when  TemplateLocation == Linked Artifact
    csmParametersFile: # Optional
    deploymentMode: 'Validation'
```

You can also create a test resource group to find [preflight](https://learn.microsoft.com/en-us/azure/azure-resource-manager/troubleshooting/quickstart-troubleshoot-arm-deployment?tabs=azure-cli#fix-preflight-error) and [deployment](https://learn.microsoft.com/en-us/azure/azure-resource-manager/troubleshooting/quickstart-troubleshoot-arm-deployment?tabs=azure-cli#fix-deployment-error) errors.

You can use any of the following ways to deploy your Bicep file and template:

*   [Bicep](https://learn.microsoft.com/en-us/azure/azure-functions/functions-infrastructure-as-code#tabpanel_33_bicep)
*   [ARM template](https://learn.microsoft.com/en-us/azure/azure-functions/functions-infrastructure-as-code#tabpanel_33_json)

*   [Azure CLI](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/deploy-cli)
*   [PowerShell](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/deploy-powershell)

Note

This method doesn't support deploying Bicep files currently.

Replace `<url-encoded-path-to-azuredeploy-json>` with a [URL-encoded](https://www.bing.com/search?q=url+encode) version of the raw path of your `azuredeploy.json` file in GitHub.

Here's an example that uses markdown:

```
[![Deploy to Azure](https://azuredeploy.net/deploybutton.png)](https://portal.azure.com/#create/Microsoft.Template/uri/<url-encoded-path-to-azuredeploy-json>)
```

Here's an example that uses HTML:

```
<a href="https://portal.azure.com/#create/Microsoft.Template/uri/<url-encoded-path-to-azuredeploy-json>" target="_blank"><img src="https://azuredeploy.net/deploybutton.png"></a>
```

The following PowerShell commands create a resource group and deploy a Bicep file or ARM template that creates a function app with its required resources. To run locally, you must have [Azure PowerShell](https://learn.microsoft.com/en-us/powershell/azure/install-azure-powershell) installed. To sign in to Azure, you must first run [`Connect-AzAccount`](https://learn.microsoft.com/en-us/powershell/module/az.accounts/connect-azaccount).

*   [Bicep](https://learn.microsoft.com/en-us/azure/azure-functions/functions-infrastructure-as-code#tabpanel_34_bicep)
*   [ARM template](https://learn.microsoft.com/en-us/azure/azure-functions/functions-infrastructure-as-code#tabpanel_34_json)

```
# Register Resource Providers if they're not already registered
Register-AzResourceProvider -ProviderNamespace "microsoft.web"
Register-AzResourceProvider -ProviderNamespace "microsoft.storage"

# Create a resource group for the function app
New-AzResourceGroup -Name "MyResourceGroup" -Location 'West Europe'

# Deploy the template
New-AzResourceGroupDeployment -ResourceGroupName "MyResourceGroup" -TemplateFile main.bicep  -Verbose
```

To test out this deployment, you can use a [template like this one](https://github.com/Azure/azure-quickstart-templates/tree/master/quickstarts/microsoft.web/function-app-create-dynamic) that creates a function app on Windows in a Consumption plan.

Learn more about how to develop and configure Azure Functions.

*   [Azure Functions developer reference](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference)
*   [How to configure Azure function app settings](https://learn.microsoft.com/en-us/azure/azure-functions/functions-how-to-use-azure-function-app-settings)
*   [Create your first Azure function](https://learn.microsoft.com/en-us/azure/azure-functions/functions-get-started)
