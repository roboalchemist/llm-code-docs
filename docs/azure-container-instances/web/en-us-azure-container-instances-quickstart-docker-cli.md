# Source: https://learn.microsoft.com/en-us/azure/container-instances/quickstart-docker-cli

Title: Quickstart - Deploy Docker container to container instance - Docker CLI - Azure Container Instances

URL Source: https://learn.microsoft.com/en-us/azure/container-instances/quickstart-docker-cli

Markdown Content:
Use Azure Container Instances to run serverless Docker containers in Azure with simplicity and speed. Deploy to a container instance on-demand when you develop cloud-native apps and you want to switch seamlessly from local development to cloud deployment.

In this quickstart, you use native Docker CLI commands to deploy a Docker container and make its application available in Azure Container Instances. The [integration between Docker and Azure](https://docs.docker.com/engine/context/aci-integration/) enables this capability. A few seconds after you execute a `docker run` command, you can browse to the application running in the container:

![Image 1: App deployed using Azure Container Instances viewed in browser](https://learn.microsoft.com/en-us/previous-versions/azure/container-instances/media/quickstart-docker-cli/view-application-running-in-an-azure-container-instance.png)

If you don't have an Azure subscription, create a [free account](https://azure.microsoft.com/free/) before you begin.

For this quickstart, you need Docker Desktop version 2.3.0.5 or later, available for [Windows](https://desktop.docker.com/win/edge/Docker%20Desktop%20Installer.exe) or [macOS](https://desktop.docker.com/mac/edge/Docker.dmg). Or install the [Docker ACI Integration CLI for Linux](https://docs.docker.com/engine/context/aci-integration/#install-the-docker-aci-integration-cli-on-linux).

Important

Not all features of Azure Container Instances are supported. Provide feedback about the Docker-Azure integration by creating an issue in the [aci-integration-beta](https://github.com/docker/aci-integration-beta) GitHub repository.

To use Docker commands to run containers in Azure Container Instances, first log into Azure:

```
docker login azure --tenant-id "[tenant ID]"
```

To find your tenant ID, browse to the Microsoft Entra ID properties.

When prompted, enter or select your Azure credentials.

Create an ACI context by running `docker context create aci`. This context associates Docker with an Azure subscription and resource group so you can create and manage container instances. For example, to create a context called _myacicontext_:

```
docker context create aci myacicontext
```

When prompted, select your Azure subscription ID, then select an existing resource group or **create a new resource group**. If you choose a new resource group, it has a system-generated name on creation. Azure container instances, like all Azure resources, must be deployed into a resource group. Resource groups allow you to organize and manage related Azure resources.

Run `docker context ls` to confirm that you added the ACI context to your Docker contexts:

```
docker context ls
```

After creating a Docker context, you can create a container in Azure. In this quickstart, you use the public `mcr.microsoft.com/azuredocs/aci-helloworld` image. This image packages a small web app written in Node.js that serves a static HTML page.

First, change to the ACI context. All subsequent Docker commands run in this context.

```
docker context use myacicontext
```

Run the following `docker run` command to create the Azure container instance with port 80 exposed to the internet:

```
docker run -p 80:80 mcr.microsoft.com/azuredocs/aci-helloworld
```

Sample output for a successful deployment:

```
[+] Running 2/2
 ⠿ hungry-kirch            Created                                                                               5.1s
 ⠿ single--container--aci  Done                                                                                 11.3s
hungry-kirch
```

Run `docker ps` to get details about the running container, including the public IP address:

```
docker ps
```

Sample output shows a public IP address, in this case _52.230.225.232_:

```
CONTAINER ID        IMAGE                                        COMMAND             STATUS              PORTS
hungry-kirch        mcr.microsoft.com/azuredocs/aci-helloworld                       Running             52.230.225.232:80->80/tcp
```

Now go to the IP address in your browser. If you see a web page similar to the following, congratulations! You successfully deployed an application running in a Docker container to Azure.

![Image 2: App deployed using Azure Container Instances viewed in browser](https://learn.microsoft.com/en-us/previous-versions/azure/container-instances/media/quickstart-docker-cli/view-application-running-in-an-azure-container-instance.png)

When you need to troubleshoot a container or the application it runs (or just see its output), start by viewing the container instance's logs.

For example, run the `docker logs` command to see the logs of the _hungry-kirch_ container in the ACI context:

```
docker logs hungry-kirch
```

The output displays the logs for the container, and should show the HTTP GET requests generated when you viewed the application in your browser.

```
listening on port 80
::ffff:10.240.255.55 - - [07/Jul/2020:17:43:53 +0000] "GET / HTTP/1.1" 304 - "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"
::ffff:10.240.255.55 - - [07/Jul/2020:17:44:36 +0000] "GET / HTTP/1.1" 304 - "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"
::ffff:10.240.255.55 - - [07/Jul/2020:17:44:36 +0000] "GET / HTTP/1.1" 304 - "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"
```

When you're done with the container, run `docker rm` to remove it. This command stops and deletes the Azure container instance.

```
docker rm hungry-kirch
```

In this quickstart, you created an Azure container instance from a public image by using integration between Docker and Azure. Learn more about integration scenarios in the [Docker documentation](https://docs.docker.com/engine/context/aci-integration/).

You can also use the [Docker extension for Visual Studio Code](https://aka.ms/VSCodeDocker) for an integrated experience to develop, run, and manage containers, images, and contexts.

To use Azure tools to create and manage container instances, see other quickstarts using the [Azure CLI](https://learn.microsoft.com/en-us/previous-versions/azure/container-instances/container-instances-quickstart), [Azure PowerShell](https://learn.microsoft.com/en-us/previous-versions/azure/container-instances/container-instances-quickstart-powershell), [Azure portal](https://learn.microsoft.com/en-us/previous-versions/azure/container-instances/container-instances-quickstart-portal), and [Azure Resource Manager template](https://learn.microsoft.com/en-us/previous-versions/azure/container-instances/container-instances-quickstart-template).

If you'd like to use Docker Compose to define and run a multi-container application locally and then switch to Azure Container Instances, continue to the tutorial.
