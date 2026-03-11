# Source: https://learn.microsoft.com/en-us/azure/azure-functions/how-to-create-function-azure-cli

Title: Create a function in Azure from the command line

URL Source: https://learn.microsoft.com/en-us/azure/azure-functions/how-to-create-function-azure-cli

Published Time: Thu, 22 Jan 2026 23:07:05 GMT

Markdown Content:
In this article, you use local command-line tools to create a function that responds to HTTP requests. After verifying your code locally, you deploy it to a serverless Flex Consumption hosting plan in Azure Functions.

Completing this quickstart incurs a small cost of a few USD cents or less in your Azure account.

Make sure to select your preferred development language at the top of the article.

*   An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).

*   [.NET 8.0 SDK](https://dotnet.microsoft.com/download)

*   [Azurite storage emulator](https://learn.microsoft.com/en-us/azure/storage/common/storage-install-azurite?tabs=npm#install-azurite)

*   [Java 17 Developer Kit](https://learn.microsoft.com/en-us/azure/developer/java/fundamentals/java-support-on-azure)
    *   If you use another [supported version of Java](https://learn.microsoft.com/en-us/azure/azure-functions/supported-languages?pivots=programming-language-java#languages-by-runtime-version), you must update the project's pom.xml file.
    *   The `JAVA_HOME` environment variable must be set to the install location of the correct version of the Java Development Kit (JDK).

*   [Apache Maven 3.8.x](https://maven.apache.org/)

*   [Node.js 20](https://nodejs.org/)

*   [PowerShell 7.2](https://learn.microsoft.com/en-us/powershell/scripting/install/installing-powershell-core-on-windows)

*   [.NET 6.0 SDK](https://dotnet.microsoft.com/download)

*   [Python 3.11](https://www.python.org/)

*   [Azurite storage emulator](https://learn.microsoft.com/en-us/azure/storage/common/storage-use-azurite)

*   [Go](https://learn.microsoft.com/en-us/azure/azure-functions/how-to-create-function-azure-cli#tabpanel_1_go)
*   [Rust](https://learn.microsoft.com/en-us/azure/azure-functions/how-to-create-function-azure-cli#tabpanel_1_rust)

*   [Go](https://go.dev/doc/install), latest version recommended. Use the `go version` command to check your version.

*   [Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli)

*   The [`jq` command line JSON processor](https://jqlang.org/download/), used to parse JSON output, and is also available in Azure Cloud Shell.

The recommended way to install Core Tools depends on the operating system of your local development computer.

*   [Windows](https://learn.microsoft.com/en-us/azure/azure-functions/how-to-create-function-azure-cli#tabpanel_1_windows)
*   [macOS](https://learn.microsoft.com/en-us/azure/azure-functions/how-to-create-function-azure-cli#tabpanel_1_macos)
*   [Linux](https://learn.microsoft.com/en-us/azure/azure-functions/how-to-create-function-azure-cli#tabpanel_1_linux)

The following steps use [APT](https://wiki.debian.org/Apt) to install Core Tools on your Ubuntu/Debian Linux distribution. For other Linux distributions, see the [Core Tools readme](https://github.com/Azure/azure-functions-core-tools/blob/v4.x/README.md#linux).

1.   Install the Microsoft package repository GPG key, to validate package integrity:

```
curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > microsoft.gpg
sudo mv microsoft.gpg /etc/apt/trusted.gpg.d/microsoft.gpg
```
2.   Set up the APT source list before doing an APT update.

##### Ubuntu

```
sudo sh -c 'echo "deb [arch=amd64] https://packages.microsoft.com/repos/microsoft-ubuntu-$(lsb_release -cs 2>/dev/null)-prod $(lsb_release -cs 2>/dev/null) main" > /etc/apt/sources.list.d/dotnetdev.list'
```

##### Debian

```
sudo sh -c 'echo "deb [arch=amd64] https://packages.microsoft.com/debian/$(lsb_release -rs 2>/dev/null | cut -d'.' -f 1)/prod $(lsb_release -cs 2>/dev/null) main" > /etc/apt/sources.list.d/dotnetdev.list'
```
3.   Check the `/etc/apt/sources.list.d/dotnetdev.list` file for one of the appropriate Linux version strings in the following table:

| Linux distribution | Version |
| --- | --- |
| Debian 12 | `bookworm` |
| Debian 11 | `bullseye` |
| Debian 10 | `buster` |
| Debian 9 | `stretch` |
| Ubuntu 24.04 | `noble` |
| Ubuntu 22.04 | `jammy` |
| Ubuntu 20.04 | `focal` |
| Ubuntu 19.04 | `disco` |
| Ubuntu 18.10 | `cosmic` |
| Ubuntu 18.04 | `bionic` |
| Ubuntu 17.04 | `zesty` |
| Ubuntu 16.04/Linux Mint 18 | `xenial` | 
4.   Start the APT source update:

```
sudo apt-get update
```
5.   Install the Core Tools package:

```
sudo apt-get install azure-functions-core-tools-4
```

In a suitable folder, run the following commands to create and activate a virtual environment named `.venv`. Make sure to use one of the [Python versions](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-python#supported-python-versions) supported by Azure Functions.

*   [bash](https://learn.microsoft.com/en-us/azure/azure-functions/how-to-create-function-azure-cli#tabpanel_1_bash)
*   [PowerShell](https://learn.microsoft.com/en-us/azure/azure-functions/how-to-create-function-azure-cli#tabpanel_1_powershell)
*   [Cmd](https://learn.microsoft.com/en-us/azure/azure-functions/how-to-create-function-azure-cli#tabpanel_1_cmd)

```
python -m venv .venv
```

```
source .venv/bin/activate
```

If Python didn't install the venv package on your Linux distribution, run the following command:

```
sudo apt-get install python3-venv
```

You run all subsequent commands in this activated virtual environment.

In Azure Functions, your code project is an app that contains one or more individual functions that each respond to a specific trigger. All functions in a project share the same configurations and are deployed as a unit to Azure. In this section, you create a code project that contains a single function.

1.   In a terminal or command prompt, run this [`func init`](https://learn.microsoft.com/en-us/azure/azure-functions/functions-core-tools-reference#func-init) command to create a function app project in the current folder:

```
func init --worker-runtime dotnet-isolated
```

1.   In a terminal or command prompt, run this [`func init`](https://learn.microsoft.com/en-us/azure/azure-functions/functions-core-tools-reference#func-init) command to create a function app project in the current folder:

```
func init --worker-runtime node --language javascript
```

1.   In a terminal or command prompt, run this [`func init`](https://learn.microsoft.com/en-us/azure/azure-functions/functions-core-tools-reference#func-init) command to create a function app project in the current folder:

```
func init --worker-runtime powershell
```

1.   In a terminal or command prompt, run this [`func init`](https://learn.microsoft.com/en-us/azure/azure-functions/functions-core-tools-reference#func-init) command to create a function app project in the current folder:

```
func init --worker-runtime python
```

1.   In a terminal or command prompt, run this [`func init`](https://learn.microsoft.com/en-us/azure/azure-functions/functions-core-tools-reference#func-init) command to create a function app project in the current folder:

```
func init --worker-runtime node --language typescript
```

1.   In a terminal or command prompt, run this [`func init`](https://learn.microsoft.com/en-us/azure/azure-functions/functions-core-tools-reference#func-init) command to create a function app project in the current folder:

```
func init --worker-runtime custom
```

1.   In an empty folder, run this `mvn` command to generate the code project from an Azure Functions [Maven archetype](https://maven.apache.org/guides/introduction/introduction-to-archetypes.html):

    *   [Bash](https://learn.microsoft.com/en-us/azure/azure-functions/how-to-create-function-azure-cli#tabpanel_2_bash)
    *   [PowerShell](https://learn.microsoft.com/en-us/azure/azure-functions/how-to-create-function-azure-cli#tabpanel_2_powershell)
    *   [Cmd](https://learn.microsoft.com/en-us/azure/azure-functions/how-to-create-function-azure-cli#tabpanel_2_cmd)

```
mvn archetype:generate -DarchetypeGroupId=com.microsoft.azure -DarchetypeArtifactId=azure-functions-archetype -DjavaVersion=17
```

Important

    *   Use `-DjavaVersion=11` if you want your functions to run on Java 11. To learn more, see [Java versions](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-java#java-versions).
    *   Set the `JAVA_HOME` environment variable to the install location of the correct version of the JDK to complete this article.

2.   Maven asks you for values needed to finish generating the project on deployment.

 Provide the following values when prompted:

| Prompt | Value | Description |
| --- | --- | --- |
| **groupId** | `com.fabrikam` | A value that uniquely identifies your project across all projects, following the [package naming rules](https://docs.oracle.com/javase/specs/jls/se6/html/packages.html#7.7) for Java. |
| **artifactId** | `fabrikam-functions` | A value that is the name of the jar, without a version number. |
| **version** | `1.0-SNAPSHOT` | Choose the default value. |
| **package** | `com.fabrikam` | A value that is the Java package for the generated function code. Use the default. | 
3.   Type `Y` or press Enter to confirm.

Maven creates the project files in a new folder with a name of _artifactId_, which in this example is `fabrikam-functions`.

4.   Navigate into the project folder:

```
cd fabrikam-functions
```

You can review the template-generated code for your new HTTP trigger function in _Function.java_ in the _\src\main\java\com\fabrikam_ project directory.

1.   Use this [`func new`](https://learn.microsoft.com/en-us/azure/azure-functions/functions-core-tools-reference#func-new) command to add a function to your project:

```
func new --name HttpExample --template "HTTP trigger" --authlevel "function"
```

A new code file is added to your project. In this case, the `--name` argument is the unique name of your function (`HttpExample`) and the `--template` argument specifies an HTTP trigger.

The project root folder contains various files for the project, including configurations files named [local.settings.json](https://learn.microsoft.com/en-us/azure/azure-functions/functions-develop-local#local-settings-file) and [host.json](https://learn.microsoft.com/en-us/azure/azure-functions/functions-host-json). Because _local.settings.json_ can contain secrets downloaded from Azure, the file is excluded from source control by default in the _.gitignore_ file.

The _function.json_ file in the _HttpExample_ folder declares an HTTP trigger function. You complete the function by adding a handler and compiling it into an executable.

*   [Go](https://learn.microsoft.com/en-us/azure/azure-functions/how-to-create-function-azure-cli#tabpanel_1_go)
*   [Rust](https://learn.microsoft.com/en-us/azure/azure-functions/how-to-create-function-azure-cli#tabpanel_1_rust)

1.   Press Ctrl + N (Cmd + N on macOS) to create a new file. Save it as _handler.go_ in the function app root (in the same folder as _host.json_).

2.   In _handler.go_, add the following code and save the file. This is your Go custom handler.

```
package main

import (
    "fmt"
    "log"
    "net/http"
    "os"
)

func helloHandler(w http.ResponseWriter, r *http.Request) {
    message := "This HTTP triggered function executed successfully. Pass a name in the query string for a personalized response.\n"
    name := r.URL.Query().Get("name")
    if name != "" {
        message = fmt.Sprintf("Hello, %s. This HTTP triggered function executed successfully.\n", name)
    }
    fmt.Fprint(w, message)
}

func main() {
    listenAddr := ":8080"
    if val, ok := os.LookupEnv("FUNCTIONS_CUSTOMHANDLER_PORT"); ok {
        listenAddr = ":" + val
    }
    http.HandleFunc("/api/HttpExample", helloHandler)
    log.Printf("About to listen on %s. Go to https://127.0.0.1%s/", listenAddr, listenAddr)
    log.Fatal(http.ListenAndServe(listenAddr, nil))
}
```
3.   Press Ctrl + Shift + ` or select _New Terminal_ from the _Terminal_ menu to open a new integrated terminal in VS Code.

4.   Compile your custom handler using the following command. An executable file named `handler` (`handler.exe` on Windows) is output in the function app root folder.

```
go build handler.go
```

The function host needs to be configured to run your custom handler binary when it starts.

1.   Open _host.json_.

2.   In the `customHandler.description` section, set the value of `defaultExecutablePath` to `handler` (on Windows, set it to `handler.exe`).

3.   In the `customHandler` section, add a property named `enableForwardingHttpRequest` and set its value to `true`. For functions consisting of only an HTTP trigger, this setting simplifies programming by allow you to work with a typical HTTP request instead of the custom handler [request payload](https://learn.microsoft.com/en-us/azure/azure-functions/functions-custom-handlers#request-payload).

4.   Confirm the `customHandler` section looks like this example. Save the file.

```
"customHandler": {
  "description": {
    "defaultExecutablePath": "handler",
    "workingDirectory": "",
    "arguments": []
  },
  "enableForwardingHttpRequest": true
}
```

The function app is configured to start your custom handler executable.

Verify your new function by running the project locally and calling the function endpoint.

1.   Use this command to start the local Azure Functions runtime host in the root of the project folder:

```
func start
``` ```
npm install
npm start
``` ```
mvn clean package  
mvn azure-functions:run
``` 
Toward the end of the output, the following lines appear:

 ...

 Now listening on: http://0.0.0.0:7071
 Application started. Press Ctrl+C to shut down.

 Http Functions:

         HttpExample: [GET,POST] http://localhost:7071/api/HttpExample
 ...

 
2.   Copy the URL of your `HttpExample` function from this output to a browser and browse to the function URL. You should receive a success response with a "hello world" message.

Note

Because access key authorization isn't enforced when running locally, the function URL returned doesn't include the access key value and you don't need it to call your function. 
3.   When you're done, use **Ctrl**+**C** and choose `y` to stop the functions host.

Before you can deploy your function code to Azure, you need to create these resources:

*   A [resource group](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/overview), which is a logical container for related resources.
*   A default [Storage account](https://learn.microsoft.com/en-us/azure/storage/common/storage-account-create), which is used by the Functions host to maintain state and other information about your functions.
*   A [user-assigned managed identity](https://learn.microsoft.com/en-us/azure/active-directory/managed-identities-azure-resources/overview), which the Functions host uses to connect to the default storage account.
*   A function app, which provides the environment for executing your function code. A function app maps to your local function project and lets you group functions as a logical unit for easier management, deployment, and sharing of resources.

Use the Azure CLI commands in these steps to create the required resources.

1.   If you haven't done so already, sign in to Azure:

```
az login
```

The [`az login`](https://learn.microsoft.com/en-us/cli/azure/reference-index#az-login) command signs you into your Azure account. Skip this step when running in Azure Cloud Shell.

2.   If you haven't already done so, use this [`az extension add`](https://learn.microsoft.com/en-us/cli/azure/extension#az-extension-add) command to install the Application Insights extension:

```
az extension add --name application-insights
```
3.   Use this [az group create](https://learn.microsoft.com/en-us/cli/azure/group#az-group-create) command to create a resource group named `AzureFunctionsQuickstart-rg` in your chosen region:

```
az group create --name "AzureFunctionsQuickstart-rg" --location "<REGION>"
```

In this example, replace `<REGION>` with a region near you that supports the Flex Consumption plan. Use the [az functionapp list-flexconsumption-locations](https://learn.microsoft.com/en-us/cli/azure/functionapp#az-functionapp-list-flexconsumption-locations) command to view the list of currently supported regions.

4.   Use this [az storage account create](https://learn.microsoft.com/en-us/cli/azure/storage/account#az-storage-account-create) command to create a general-purpose storage account in your resource group and region:

```
az storage account create --name <STORAGE_NAME> --location "<REGION>" --resource-group "AzureFunctionsQuickstart-rg" \
--sku "Standard_LRS" --allow-blob-public-access false --allow-shared-key-access false
```

In this example, replace `<STORAGE_NAME>` with a name that is appropriate to you and unique in Azure Storage. Names must contain three to 24 characters numbers and lowercase letters only. `Standard_LRS` specifies a general-purpose account, which is [supported by Functions](https://learn.microsoft.com/en-us/azure/azure-functions/storage-considerations#storage-account-requirements). This new account can only be accessed by using Microsoft Entra-authenticated identities that have been granted permissions to specific resources.

5.   Use this script to create a user-assigned managed identity, parse the returned JSON properties of the object using `jq`, and grant `Storage Blob Data Owner` permissions in the default storage account:

```
output=$(az identity create --name "func-host-storage-user" --resource-group "AzureFunctionsQuickstart-rg" --location <REGION> \
--query "{userId:id, principalId: principalId, clientId: clientId}" -o json)

userId=$(echo $output | jq -r '.userId')
principalId=$(echo $output | jq -r '.principalId')
clientId=$(echo $output | jq -r '.clientId')

storageId=$(az storage account show --resource-group "AzureFunctionsQuickstart-rg" --name <STORAGE_NAME> --query 'id' -o tsv)
az role assignment create --assignee-object-id $principalId --assignee-principal-type ServicePrincipal \
--role "Storage Blob Data Owner" --scope $storageId
```

If you don't have the `jq` utility in your local Bash shell, it's available in Azure Cloud Shell. In this example, replace `<STORAGE_NAME>` and `<REGION>` with your default storage account name and region, respectively.

The [az identity create](https://learn.microsoft.com/en-us/cli/azure/identity#az-identity-create) command creates an identity named `func-host-storage-user`. The returned `principalId` is used to assign permissions to this new identity in the default storage account by using the [`az role assignment create`](https://learn.microsoft.com/en-us/cli/azure/role/assignment#az-role-assignment-create) command. The [`az storage account show`](https://learn.microsoft.com/en-us/cli/azure/storage/account#az-storage-account-show) command is used to obtain the storage account ID.

6.   Use this [az functionapp create](https://learn.microsoft.com/en-us/cli/azure/functionapp#az-functionapp-create) command to create the function app in Azure:

```
az functionapp create --resource-group "AzureFunctionsQuickstart-rg" --name <APP_NAME> --flexconsumption-location <REGION> \
--runtime dotnet-isolated --runtime-version <LANGUAGE_VERSION> --storage-account <STORAGE_NAME> \
--deployment-storage-auth-type UserAssignedIdentity --deployment-storage-auth-value "func-host-storage-user"
``` ```
az functionapp create --resource-group "AzureFunctionsQuickstart-rg" --name <APP_NAME> --flexconsumption-location <REGION> \
--runtime java --runtime-version <LANGUAGE_VERSION> --storage-account <STORAGE_NAME> \
--deployment-storage-auth-type UserAssignedIdentity --deployment-storage-auth-value "func-host-storage-user"
``` ```
az functionapp create --resource-group "AzureFunctionsQuickstart-rg" --name <APP_NAME> --flexconsumption-location <REGION> \
--runtime node --runtime-version <LANGUAGE_VERSION> --storage-account <STORAGE_NAME> \
--deployment-storage-auth-type UserAssignedIdentity --deployment-storage-auth-value "func-host-storage-user"
``` ```
az functionapp create --resource-group "AzureFunctionsQuickstart-rg" --name <APP_NAME> --flexconsumption-location <REGION> \
--runtime python --runtime-version <LANGUAGE_VERSION> --storage-account <STORAGE_NAME> \
--deployment-storage-auth-type UserAssignedIdentity --deployment-storage-auth-value "func-host-storage-user"
``` ```
az functionapp create --resource-group "AzureFunctionsQuickstart-rg" --name <APP_NAME> --flexconsumption-location <REGION> \
--runtime python --runtime-version <LANGUAGE_VERSION> --storage-account <STORAGE_NAME> \
--deployment-storage-auth-type UserAssignedIdentity --deployment-storage-auth-value "func-host-storage-user"
``` ```
az functionapp create --resource-group "AzureFunctionsQuickstart-rg" --name <APP_NAME> --flexconsumption-location <REGION> \
--runtime other --storage-account <STORAGE_NAME> \
--deployment-storage-auth-type UserAssignedIdentity --deployment-storage-auth-value "func-host-storage-user"
``` 
In this example, replace these placeholders with the appropriate values:

    *   `<APP_NAME>`: a globally unique name appropriate to you. The `<APP_NAME>` is also the default DNS domain for the function app.
    *   `<STORAGE_NAME>`: the name of the account you used in the previous step.
    *   `<REGION>`: your current region.
    *   `<LANGUAGE_VERSION>`: use the same [supported language stack version](https://learn.microsoft.com/en-us/azure/azure-functions/supported-languages) you verified locally, when applicable.

This command creates a function app running in your specified language runtime on Linux in the [Flex Consumption Plan](https://learn.microsoft.com/en-us/azure/azure-functions/flex-consumption-plan), which is free for the amount of usage you incur here. The command also creates an associated Azure Application Insights instance in the same resource group, with which you can use to monitor your function app executions and view logs. For more information, see [Monitor Azure Functions](https://learn.microsoft.com/en-us/azure/azure-functions/functions-monitoring). The instance incurs no costs until you activate it.

7.   Use this script to add your user-assigned managed identity to the [Monitoring Metrics Publisher](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles/monitor#monitoring-metrics-publisher) role in your Application Insights instance:

```
appInsights=$(az monitor app-insights component show --resource-group "AzureFunctionsQuickstart-rg" \
    --app <APP_NAME> --query "id" --output tsv)
principalId=$(az identity show --name "func-host-storage-user" --resource-group "AzureFunctionsQuickstart-rg" \
    --query principalId -o tsv)
az role assignment create --role "Monitoring Metrics Publisher" --assignee $principalId --scope $appInsights
```

In this example, replace `<APP_NAME>` with the name of your function app. The [az role assignment create](https://learn.microsoft.com/en-us/cli/azure/role/assignment#az-role-assignment-create) command adds your user to the role. The resource ID of your Application Insights instance and the principal ID of your user are obtained by using the [az monitor app-insights component show](https://learn.microsoft.com/en-us/cli/azure/monitor/app-insights/component#az-monitor-app-insights-component-show) and [`az identity show`](https://learn.microsoft.com/en-us/cli/azure/identity#az-identity-show) commands, respectively.

To enable the Functions host to connect to the default storage account by using shared secrets, replace the `AzureWebJobsStorage` connection string setting with several settings that are prefixed with `AzureWebJobsStorage__`. These settings define a complex setting that your app uses to connect to storage and Application Insights with a user-assigned managed identity.

1.   Use this script to get the client ID of the user-assigned managed identity and uses it to define managed identity connections to both storage and Application Insights:

```
clientId=$(az identity show --name func-host-storage-user \
    --resource-group AzureFunctionsQuickstart-rg --query 'clientId' -o tsv)
az functionapp config appsettings set --name <APP_NAME> --resource-group "AzureFunctionsQuickstart-rg" \
    --settings AzureWebJobsStorage__accountName=<STORAGE_NAME> \
    AzureWebJobsStorage__credential=managedidentity AzureWebJobsStorage__clientId=$clientId \
    APPLICATIONINSIGHTS_AUTHENTICATION_STRING="ClientId=$clientId;Authorization=AAD"
```

In this script, replace `<APP_NAME>` and `<STORAGE_NAME>` with the names of your function app and storage account, respectively.

2.   Run the [az functionapp config appsettings delete](https://learn.microsoft.com/en-us/cli/azure/functionapp/config/appsettings#az-functionapp-config-appsettings-delete) command to remove the existing `AzureWebJobsStorage` connection string setting, which contains a shared secret key:

```
az functionapp config appsettings delete --name <APP_NAME> --resource-group "AzureFunctionsQuickstart-rg" --setting-names AzureWebJobsStorage
```

In this example, replace `<APP_NAME>` with the names of your function app.

At this point, the Functions host can connect to the storage account securely by using managed identities instead of shared secrets. You can now deploy your project code to the Azure resources.

After you've successfully created your function app in Azure, you're now ready to deploy your local functions project by using the [`func azure functionapp publish`](https://learn.microsoft.com/en-us/azure/azure-functions/functions-run-local#project-file-deployment) command.

1.   In your root project folder, run this [`func azure functionapp publish`](https://learn.microsoft.com/en-us/azure/azure-functions/functions-core-tools-reference#func-azure-functionapp-publish) command:

```
func azure functionapp publish <APP_NAME>
```

In this example, replace `<APP_NAME>` with the name of your app. A successful deployment shows results similar to the following output (truncated for simplicity):

 ...

 Getting site publishing info...
 Creating archive for current directory...
 Performing remote build for functions project.

 ...

 Deployment successful.
 Remote build succeeded!
 Syncing triggers...
 Functions in msdocs-azurefunctions-qs:
     HttpExample - [httpTrigger]
         Invoke url: https://msdocs-azurefunctions-qs.azurewebsites.net/api/httpexample
 
2.   In your local terminal or command prompt, run this command to get the URL endpoint value, including the access key:

```
func azure functionapp list-functions <APP_NAME> --show-keys
```

In this example, again replace `<APP_NAME>` with the name of your app.

3.   Copy the returned endpoint URL and key, which you use to invoke the function endpoint.

After you successfully create your function app in Azure, update the pom.xml file so that Maven can deploy to your new app. Otherwise, Maven creates a new set of Azure resources during deployment.

1.   In Azure Cloud Shell, use this [`az functionapp show`](https://learn.microsoft.com/en-us/cli/azure/functionapp#az-functionapp-show) command to get the deployment container URL and ID of the new user-assigned managed identity:

```
az functionapp show --name <APP_NAME> --resource-group AzureFunctionsQuickstart-rg  \
    --query "{userAssignedIdentityResourceId: properties.functionAppConfig.deployment.storage.authentication.userAssignedIdentityResourceId, \
    containerUrl: properties.functionAppConfig.deployment.storage.value}"
```

In this example, replace `<APP_NAME>` with the names of your function app.

2.   In the project root directory, open the pom.xml file in a text editor, locate the `properties` element, and update these specific property values:

| Property name | Value |
| --- | --- |
| `java.version` | Use the same [supported language stack version](https://learn.microsoft.com/en-us/azure/azure-functions/supported-languages) you verified locally, such as `17`. |
| `azure.functions.maven.plugin.version` | `1.37.1` |
| `azure.functions.java.library.version` | `3.1.0` |
| `functionAppName` | The name of your function app in Azure. | 
3.   Find the `configuration` section of the `azure-functions-maven-plugin` and replace it with this XML fragment:

```
<configuration>
    <appName>${functionAppName}</appName>
    <resourceGroup>AzureFunctionsQuickstart-rg</resourceGroup>
    <pricingTier>Flex Consumption</pricingTier>
    <region>....</region>
    <runtime>
        <os>linux</os>
        <javaVersion>${java.version}</javaVersion>
    </runtime>
    <deploymentStorageAccount>...</deploymentStorageAccount>
    <deploymentStorageResourceGroup>AzureFunctionsQuickstart-rg</deploymentStorageResourceGroup>
    <deploymentStorageContainer>...</deploymentStorageContainer>
    <storageAuthenticationMethod>UserAssignedIdentity</storageAuthenticationMethod>
    <userAssignedIdentityResourceId>...</userAssignedIdentityResourceId>
    <appSettings>
        <property>
            <name>FUNCTIONS_EXTENSION_VERSION</name>
            <value>~4</value>
        </property>
    </appSettings>
</configuration>
```
4.   In the new `configuration` element, make these specific replacements of the ellipses (`...`) values:

| Configuration | Value |
| --- | --- |
| `region` | The region code of your existing function app, such as `eastus`. |
| `deploymentStorageAccount` | The name of your storage account. |
| `deploymentStorageContainer` | The name of the deployment share, which comes after the `\` in the `containerUrl` value you obtained. |
| `userAssignedIdentityResourceId` | The fully qualified resource ID of your managed identity, which you obtained. | 
5.   Save your changes to the _pom.xml_ file.

You can now use Maven to deploy your code project to your existing app.

1.   From the command prompt, run this command:

```
mvn clean package azure-functions:deploy
```
2.   After your deployment succeeds, run this Core Tools command to get the URL endpoint value, including the access key:

```
func azure functionapp list-functions <APP_NAME> --show-keys
```

In this example, again replace `<APP_NAME>` with the name of your app.

3.   Copy the returned endpoint URL and key, which you use to invoke the function endpoint.

Because your function uses an HTTP trigger and supports GET requests, you invoke it by making an HTTP request to its URL using the function-level access key. It's easiest to execute a GET request in a browser.

Paste the URL and access key you copied into a browser address bar.

The endpoint URL should look something like this example:

`https://contoso-app.azurewebsites.net/api/httpexample?code=aabbccdd...`

In this case, you must also provide an access key in the query string when making a GET request to the endpoint URL. Using an access key is recommended to limit access from random clients. When making a POST request using an HTTP client, you should instead provide the access key in the `x-functions-key` header.

When you navigate to this URL, the browser should display similar output as when you ran the function locally.

If you continue to the [next step](https://learn.microsoft.com/en-us/azure/azure-functions/how-to-create-function-azure-cli#next-steps) and add an Azure Storage queue output binding, keep all your resources in place as you'll build on what you've already done.

Otherwise, use the following command to delete the resource group and all its contained resources to avoid incurring further costs.

*   [Azure CLI](https://learn.microsoft.com/en-us/azure/azure-functions/how-to-create-function-azure-cli#tabpanel_1_azure-cli)
*   [Azure PowerShell](https://learn.microsoft.com/en-us/azure/azure-functions/how-to-create-function-azure-cli#tabpanel_1_azure-powershell)

```
az group delete --name AzureFunctionsQuickstart-rg
```
