# Source: https://learn.microsoft.com/en-us/azure/container-instances/container-instances-quickstart

Title: Quickstart - Deploy Docker container to container instance - Azure CLI - Azure Container Instances

URL Source: https://learn.microsoft.com/en-us/azure/container-instances/container-instances-quickstart

Markdown Content:
Use Azure Container Instances to run serverless Docker containers in Azure with simplicity and speed. Deploy an application to a container instance on-demand when you don't need a full container orchestration platform like Azure Kubernetes Service.

In this quickstart, you use the Azure CLI to deploy an isolated Docker container and make its application available with a fully qualified domain name (FQDN). A few seconds after you execute a single deployment command, you can browse to the application running in the container:

![Image 1: View an app deployed to Azure Container Instances in browser](https://learn.microsoft.com/en-us/azure/container-instances/media/container-instances-quickstart/view-an-application-running-in-an-azure-container-instance.png)

If you don't have an Azure account, create a [free account](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn) before you begin.

* Use the Bash environment in [Azure Cloud Shell](https://learn.microsoft.com/en-us/azure/cloud-shell/overview). For more information, see [Get started with Azure Cloud Shell](https://learn.microsoft.com/en-us/azure/cloud-shell/quickstart).

[![Image 2](https://learn.microsoft.com/en-us/azure/reusable-content/azure-cli/media/hdi-launch-cloud-shell.png)](https://shell.azure.com/)

* If you prefer to run CLI reference commands locally, [install](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli) the Azure CLI. If you're running on Windows or macOS, consider running Azure CLI in a Docker container. For more information, see [How to run the Azure CLI in a Docker container](https://learn.microsoft.com/en-us/cli/azure/run-azure-cli-docker).

  * If you're using a local installation, sign in to the Azure CLI by using the [az login](https://learn.microsoft.com/en-us/cli/azure/reference-index#az-login) command. To finish the authentication process, follow the steps displayed in your terminal. For other sign-in options, see [Authenticate to Azure using Azure CLI](https://learn.microsoft.com/en-us/cli/azure/authenticate-azure-cli).

  * When you're prompted, install the Azure CLI extension on first use. For more information about extensions, see [Use and manage extensions with the Azure CLI](https://learn.microsoft.com/en-us/cli/azure/azure-cli-extensions-overview).

  * Run [az version](https://learn.microsoft.com/en-us/cli/azure/reference-index?#az-version) to find the version and dependent libraries that are installed. To upgrade to the latest version, run [az upgrade](https://learn.microsoft.com/en-us/cli/azure/reference-index?#az-upgrade).

* This quickstart requires version 2.0.55 or later of the Azure CLI. If using Azure Cloud Shell, the latest version is already installed.

Warning

Best practice: User’s credentials passed via command line interface (CLI) are stored as plain text in the backend. Storing credentials in plain text is a security risk; Microsoft advises customers to store user credentials in CLI environment variables to ensure they are encrypted/transformed when stored in the backend.

Azure container instances, like all Azure resources, must be deployed into a resource group. Resource groups allow you to organize and manage related Azure resources.

First, create a resource group named _myResourceGroup_ in the _eastus_ location with the [az group create](https://learn.microsoft.com/en-us/cli/azure/group#az_group_create) command:

```
az group create --name myResourceGroup --location eastus
```

Now that you have a resource group, you can run a container in Azure. To create a container instance with the Azure CLI, provide a resource group name, container instance name, and Docker container image to the [az container create](https://learn.microsoft.com/en-us/cli/azure/container#az_container_create) command. In this quickstart, you use the public `mcr.microsoft.com/azuredocs/aci-helloworld` image. This image packages a small web app written in Node.js that serves a static HTML page.

You can expose your containers to the internet by specifying one or more ports to open, a DNS name label, or both. In this quickstart, you deploy a container with a DNS name label so that the web app is publicly reachable.

Execute a command similar to the following to start a container instance. Set a `--dns-name-label` value that's unique within the Azure region where you create the instance. If you receive a "DNS name label not available" error message, try a different DNS name label.

```
az container create --resource-group myResourceGroup --name mycontainer --image mcr.microsoft.com/azuredocs/aci-helloworld --dns-name-label aci-demo --ports 80 --os-type linux --memory 1.5 --cpu 1
```

To [deploy the container into a specific availability zone](https://learn.microsoft.com/en-us/azure/reliability/reliability-container-instances#availability-zone-support), use the `--zone` argument and specify the logical zone number:

```
az container create --resource-group myResourceGroup --name mycontainer --image mcr.microsoft.com/azuredocs/aci-helloworld --dns-name-label aci-demo --ports 80 --os-type linux --memory 1.5 --cpu 1 --zone 1
```

Important

Zonal deployments are only available in regions that support availability zones. To see if your region supports availability zones, see [Azure Regions List](https://learn.microsoft.com/en-us/azure/reliability/regions-list).

Within a few seconds, you should get a response from the Azure CLI indicating the deployment completed. Check its status with the [az container show](https://learn.microsoft.com/en-us/cli/azure/container#az_container_show) command:

```
az container show --resource-group myResourceGroup --name mycontainer --query "{FQDN:ipAddress.fqdn,ProvisioningState:provisioningState}" --out table
```

When you run the command, the container's fully qualified domain name (FQDN) and its provisioning state are displayed.

```
FQDN                               ProvisioningState
---------------------------------  -------------------
aci-demo.eastus.azurecontainer.io  Succeeded
```

If the container's `ProvisioningState` is **Succeeded**, go to its FQDN in your browser. If you see a web page similar to the following, congratulations! You successfully deployed an application running in a Docker container to Azure.

![Image 3: View an app deployed to Azure Container Instances in browser](https://learn.microsoft.com/en-us/azure/container-instances/media/container-instances-quickstart/view-an-application-running-in-an-azure-container-instance.png)

If at first the application isn't displayed, you might need to wait a few seconds while DNS propagates, then try refreshing your browser.

When you need to troubleshoot a container or the application it runs (or just see its output), start by viewing the container instance's logs.

Pull the container instance logs with the [az container logs](https://learn.microsoft.com/en-us/cli/azure/container#az_container_logs) command:

```
az container logs --resource-group myResourceGroup --name mycontainer
```

The output displays the logs for the container, and should show the HTTP GET requests generated when you viewed the application in your browser.

```
listening on port 80
::ffff:10.240.255.55 - - [21/Mar/2019:17:43:53 +0000] "GET / HTTP/1.1" 304 - "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"
::ffff:10.240.255.55 - - [21/Mar/2019:17:44:36 +0000] "GET / HTTP/1.1" 304 - "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"
::ffff:10.240.255.55 - - [21/Mar/2019:17:44:36 +0000] "GET / HTTP/1.1" 304 - "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"
```

In addition to viewing the logs, you can attach your local standard out and standard error streams to that of the container.

First, execute the [az container attach](https://learn.microsoft.com/en-us/cli/azure/container#az_container_attach) command to attach your local console to the container's output streams:

```
az container attach --resource-group myResourceGroup --name mycontainer
```

Once attached, refresh your browser a few times to generate some more output. When you're done, detach your console with `Control+C`. You should see output similar to the following sample:

```
Container 'mycontainer' is in state 'Running'...
(count: 1) (last timestamp: 2019-03-21 17:27:20+00:00) pulling image "mcr.microsoft.com/azuredocs/aci-helloworld"
(count: 1) (last timestamp: 2019-03-21 17:27:24+00:00) Successfully pulled image "mcr.microsoft.com/azuredocs/aci-helloworld"
(count: 1) (last timestamp: 2019-03-21 17:27:27+00:00) Created container
(count: 1) (last timestamp: 2019-03-21 17:27:27+00:00) Started container

Start streaming logs:
listening on port 80

::ffff:10.240.255.55 - - [21/Mar/2019:17:43:53 +0000] "GET / HTTP/1.1" 304 - "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"
::ffff:10.240.255.55 - - [21/Mar/2019:17:44:36 +0000] "GET / HTTP/1.1" 304 - "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"
::ffff:10.240.255.55 - - [21/Mar/2019:17:44:36 +0000] "GET / HTTP/1.1" 304 - "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"
::ffff:10.240.255.55 - - [21/Mar/2019:17:47:01 +0000] "GET / HTTP/1.1" 304 - "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"
::ffff:10.240.255.56 - - [21/Mar/2019:17:47:12 +0000] "GET / HTTP/1.1" 304 - "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"
```

When you're done with the container, remove it using the [az container delete](https://learn.microsoft.com/en-us/cli/azure/container#az_container_delete) command:

```
az container delete --resource-group myResourceGroup --name mycontainer
```

To verify that the container deleted, execute the [az container list](https://learn.microsoft.com/en-us/cli/azure/container#az-container-list) command:

```
az container list --resource-group myResourceGroup --output table
```

The **mycontainer** container shouldn't appear in the command's output. If you have no other containers in the resource group, no output is displayed.

If you're done with the _myResourceGroup_ resource group and all the resources it contains, delete it with the [az group delete](https://learn.microsoft.com/en-us/cli/azure/group#az_group_delete) command:

```
az group delete --name myResourceGroup
```

In this quickstart, you created an Azure container instance by using a public Microsoft image. If you'd like to build a container image and deploy it from a private Azure container registry, continue to the Azure Container Instances tutorial.

To try out options for running containers in an orchestration system on Azure, see the [Azure Kubernetes Service (AKS)](https://learn.microsoft.com/en-us/azure/aks/intro-kubernetes) quickstarts.
