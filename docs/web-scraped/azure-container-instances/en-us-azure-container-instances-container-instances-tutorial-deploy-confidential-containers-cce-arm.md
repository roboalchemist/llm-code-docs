# Source: https://learn.microsoft.com/en-us/azure/container-instances/container-instances-tutorial-deploy-confidential-containers-cce-arm

Title: Tutorial: Prepare a deployment for a confidential container on Azure Container Instances - Azure Container Instances

URL Source: https://learn.microsoft.com/en-us/azure/container-instances/container-instances-tutorial-deploy-confidential-containers-cce-arm

Markdown Content:
In Azure Container Instances, you can use confidential containers on the serverless platform to run container applications in a hardware-based and attested trusted execution environment (TEE). This capability can help protect data in use and provides in-memory encryption via Secure Nested Paging.

In this tutorial, you learn how to:

* Create an Azure Resource Manager template (ARM template) for a confidential container group.
* Generate a confidential computing enforcement (CCE) policy.
* Deploy the confidential container group to Azure.

To complete this tutorial, you must satisfy the following requirements:

* **Azure CLI**: You must have Azure CLI version 2.44.1 or later installed on your local computer. To find your version, run `az --version`. If you need to install or upgrade, see [Install the Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli).

* **Azure CLI confcom extension**: You must have Azure CLI confcom extension version 0.30+ installed to generate confidential computing enforcement policies.

```
az extension add -n confcom
```

* **Docker**: You need Docker installed locally. Docker provides packages that configure the Docker environment on [macOS](https://docs.docker.com/docker-for-mac/), [Windows](https://docs.docker.com/docker-for-windows/), and [Linux](https://docs.docker.com/engine/installation/#supported-platforms).

This tutorial assumes a basic understanding of core Docker concepts like containers, container images, and basic `docker` commands. For a primer on Docker and container basics, see the [Docker overview](https://docs.docker.com/engine/docker-overview/).

Important

Because Azure Cloud Shell doesn't include the Docker daemon, you must install both the Azure CLI and Docker Engine on your _local computer_ to complete this tutorial. You can't use Azure Cloud Shell for this tutorial.

In this tutorial, you deploy a Hello World application that generates a hardware attestation report. You start by creating an ARM template with a container group resource to define the properties of this application. You then use this ARM template with the Azure CLI confcom tooling to generate a CCE policy for attestation.

This tutorial uses [this ARM template](https://raw.githubusercontent.com/microsoft/confidential-container-demos/main/hello-world/ACI/arm-template.json) as an example. To view the source code for this application, see [Azure Confidential Container Instances Hello World](https://github.com/microsoft/confidential-container-demos/tree/main/hello-world/ACI).

The example template adds two properties to the Container Instances resource definition to make the container group confidential:

* `sku`: Enables you to select between confidential and standard container group deployments. If you don't add this property to the resource, the container group is a standard deployment.
* `confidentialComputeProperties`: Enables you to pass in a custom CCE policy for attestation of your container group. If you don't add this object to the resource, the software components that run within the container group won't validate.

Note

The `ccePolicy` parameter under `confidentialComputeProperties` is blank. You'll fill it in when you generate the policy later in the tutorial.

Use your preferred text editor to save this ARM template on your local machine as _template.json_.

```
{
    "$schema": "https://schema.management.azure.com/schemas/2019-04-01/deploymentTemplate.json#",
    "contentVersion": "1.0.0.0",
    "parameters": {
      "name": {
        "type": "string",
        "defaultValue": "helloworld",
        "metadata": {
          "description": "Name for the container group"
        }
      },
      "location": {
        "type": "string",
        "defaultValue": "North Europe",
        "metadata": {
          "description": "Location for all resources."
        }
      },
      "image": {
        "type": "string",
        "defaultValue": "mcr.microsoft.com/acc/samples/aci/helloworld:2.8",
        "metadata": {
          "description": "Container image to deploy. Should be of the form repoName/imagename:tag for images stored in public Docker Hub, or a fully qualified URI for other registries. Images from private registries require additional registry credentials."
        }
      },
      "port": {
        "type": "int",
        "defaultValue": 80,
        "metadata": {
          "description": "Port to open on the container and the public IP address."
        }
      },
      "cpuCores": {
        "type": "int",
        "defaultValue": 1,
        "metadata": {
          "description": "The number of CPU cores to allocate to the container."
        }
      },
      "memoryInGb": {
        "type": "int",
        "defaultValue": 1,
        "metadata": {
          "description": "The amount of memory to allocate to the container in gigabytes."
        }
      },
      "restartPolicy": {
        "type": "string",
        "defaultValue": "Never",
        "allowedValues": [
          "Always",
          "Never",
          "OnFailure"
        ],
        "metadata": {
          "description": "The behavior of Azure runtime if container has stopped."
        }
      }
    },
    "resources": [
      {
        "type": "Microsoft.ContainerInstance/containerGroups",
        "apiVersion": "2023-05-01",
        "name": "[parameters('name')]",
        "location": "[parameters('location')]",
        "properties": {
          "confidentialComputeProperties": {
            "ccePolicy": ""
          },
          "containers": [
            {
              "name": "[parameters('name')]",
              "properties": {
                "image": "[parameters('image')]",
                "ports": [
                  {
                    "port": "[parameters('port')]",
                    "protocol": "TCP"
                  }
                ],
                "resources": {
                  "requests": {
                    "cpu": "[parameters('cpuCores')]",
                    "memoryInGB": "[parameters('memoryInGb')]"
                  }
                }
              }
            }
          ],
          "sku": "Confidential",
          "osType": "Linux",
          "restartPolicy": "[parameters('restartPolicy')]",
          "ipAddress": {
            "type": "Public",
            "ports": [
              {
                "port": "[parameters('port')]",
                "protocol": "TCP"
              }
            ]
          }
        }
      }
    ],
    "outputs": {
      "containerIPv4Address": {
        "type": "string",
        "value": "[reference(resourceId('Microsoft.ContainerInstance/containerGroups', parameters('name'))).ipAddress.ip]"
      }
    }
  }
```

With the ARM template that you crafted and the Azure CLI confcom extension, you can generate a custom CCE policy. The CCE policy is used for attestation. The tool takes the ARM template as an input to generate the policy. The policy enforces the specific container images, environment variables, mounts, and commands, which can then be validated when the container group starts up. For more information on the Azure CLI confcom extension, see the [documentation on GitHub](https://github.com/Azure/azure-cli-extensions/blob/main/src/confcom/azext_confcom/README.md).

1. To generate the CCE policy, run the following command by using the ARM template as input:

```
az confcom acipolicygen -a .\template.json
```

When this command finishes, a Base64 string generated as output will automatically appear in the `ccePolicy` property of the ARM template.

In the following steps, you use the Azure portal to deploy the template. You can also use Azure PowerShell, the Azure CLI, or the REST API. To learn about other deployment methods, see [Deploy templates](https://learn.microsoft.com/en-us/azure/azure-resource-manager/templates/deploy-cli).

1. Select the **Deploy to Azure** button to sign in to Azure and begin a Container Instances deployment.

[![Image 1: Button to deploy the Resource Manager template to Azure.](https://learn.microsoft.com/en-us/azure/reusable-content/ce-skilling/azure/media/template-deployments/deploy-to-azure-button.svg)](https://ms.portal.azure.com/#create/Microsoft.Template)

1. Select **Build your own template in the editor**.

![Image 2: Screenshot of the button for building your own template in the editor.](https://learn.microsoft.com/en-us/azure/container-instances/media/container-instances-confidential-containers-tutorials/confidential-containers-cce-build-template.png)

The template JSON that appears is mostly blank.

1. Select **Load file** and upload _template.json_, which you modified by adding the CCE policy in the previous steps.

![Image 3: Screenshot of the button for loading a file.](https://learn.microsoft.com/en-us/azure/container-instances/media/container-instances-confidential-containers-tutorials/confidential-containers-cce-load-file.png)

1. Select **Save**.

2. Select or enter the following values:

    *   **Subscription**: Select an Azure subscription.
    *   **Resource group**: Select **Create new**, enter a unique name for the resource group, and then select **OK**.
    *   **Name**: Accept the generated name for the instance, or enter a name.
    *   **Location**: Select a location for the resource group. Choose a region where [confidential containers are supported](https://learn.microsoft.com/en-us/azure/container-instances/container-instances-region-availability#linux-container-groups). Example: **North Europe**.
    *   **Image**: Accept the default image name. This sample Linux image displays a hardware attestation.

Accept default values for the remaining properties, and then select **Review + create**.

![Image 4: Screenshot of details for a custom ARM template deployment.](https://learn.microsoft.com/en-us/azure/container-instances/media/container-instances-confidential-containers-tutorials/confidential-containers-cce-custom-arm-deployment.png)

1. Review the terms and conditions. If you agree, select **I agree to the terms and conditions stated above**.

2. Wait until the **Deployment succeeded** notification appears. It confirms that you successfully created the instance.

![Image 5: Screenshot of a portal notification for successful deployment.](https://learn.microsoft.com/en-us/azure/container-instances/media/container-instances-confidential-containers-tutorials/confidential-containers-cce-deployment-succeed.png)

In the following steps, you use the Azure portal to review the properties of the container instance. You can also use a tool such as the [Azure CLI](https://learn.microsoft.com/en-us/azure/container-instances/container-instances-quickstart).

1. In the portal, search for **Container Instances**, and then select the container instance that you created.

2. On the **Overview** page, note the status of the instance and its IP address.

![Image 6: Screenshot of the overview page for a container group instance.](https://learn.microsoft.com/en-us/azure/container-instances/media/container-instances-confidential-containers-tutorials/confidential-containers-cce-portal.png)

1. When the status of the instance is **Running**, go to the IP address in your browser.

![Image 7: Screenshot of a browser view of an app deployed via Azure Container Instances.](https://learn.microsoft.com/en-us/azure/container-instances/media/container-instances-confidential-containers-tutorials/confidential-containers-aci-hello-world.png)

The presence of the attestation report below the Azure Container Instances logo confirms that the container is running on hardware that supports a TEE.

If you deploy to hardware that doesn't support a TEE (for example, by choosing a region where Confidential Container Instances isn't available), no attestation report appears.

Now that you deployed a confidential container group on Container Instances, you can learn more about how policies are enforced:

* [Confidential containers on Azure Container Instances](https://learn.microsoft.com/en-us/azure/container-instances/container-instances-confidential-overview)
* [Azure CLI confcom extension examples](https://github.com/Azure/azure-cli-extensions/blob/main/src/confcom/azext_confcom/README.md)
* [Confidential Hello World application](https://github.com/microsoft/confidential-container-demos/tree/main/hello-world/ACI)
