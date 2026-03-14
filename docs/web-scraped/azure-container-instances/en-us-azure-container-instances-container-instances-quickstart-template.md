# Source: https://learn.microsoft.com/en-us/azure/container-instances/container-instances-quickstart-template

Title: Quickstart - Create a container instance - Azure Resource Manager template - Azure Container Instances

URL Source: https://learn.microsoft.com/en-us/azure/container-instances/container-instances-quickstart-template

Markdown Content:
Use Azure Container Instances to run serverless Docker containers in Azure with simplicity and speed. Deploy an application to a container instance on-demand when you don't need a full container orchestration platform like Azure Kubernetes Service. In this quickstart, you use an Azure Resource Manager template (ARM template) to deploy an isolated Docker container and make its web application available with a public IP address.

An [Azure Resource Manager template](https://learn.microsoft.com/en-us/azure/azure-resource-manager/templates/overview) is a JavaScript Object Notation (JSON) file that defines the infrastructure and configuration for your project. The template uses declarative syntax. You describe your intended deployment without writing the sequence of programming commands to create the deployment.

If your environment meets the prerequisites and you're familiar with using ARM templates, select the **Deploy to Azure** button. The template opens in the Azure portal.

[![Image 1: Button to deploy the Resource Manager template to Azure.](https://learn.microsoft.com/en-us/azure/reusable-content/ce-skilling/azure/media/template-deployments/deploy-to-azure-button.svg)](https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.containerinstance%2Faci-linuxcontainer-public-ip%2Fazuredeploy.json)

If you don't have an Azure subscription, create a [free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn) account before you begin.

The template used in this quickstart is from [Azure Quickstart Templates](https://azure.microsoft.com/resources/templates/aci-linuxcontainer-public-ip/).

```
{
  "$schema": "https://schema.management.azure.com/schemas/2019-04-01/deploymentTemplate.json#",
  "languageVersion": "2.0",
  "contentVersion": "1.0.0.0",
  "metadata": {
    "_generator": {
      "name": "bicep",
      "version": "0.37.4.10188",
      "templateHash": "7099805986652764357"
    }
  },
  "parameters": {
    "name": {
      "type": "string",
      "defaultValue": "acilinuxpublicipcontainergroup",
      "metadata": {
        "description": "Name for the container group"
      }
    },
    "location": {
      "type": "string",
      "defaultValue": "[resourceGroup().location]",
      "metadata": {
        "description": "Location for all resources."
      }
    },
    "image": {
      "type": "string",
      "defaultValue": "mcr.microsoft.com/azuredocs/aci-helloworld",
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
      "defaultValue": 2,
      "metadata": {
        "description": "The amount of memory to allocate to the container in gigabytes."
      }
    },
    "restartPolicy": {
      "type": "string",
      "defaultValue": "Always",
      "allowedValues": [
        "Always",
        "Never",
        "OnFailure"
      ],
      "metadata": {
        "description": "The behavior of Azure runtime if container has stopped."
      }
    },
    "zone": {
      "type": "string",
      "nullable": true,
      "metadata": {
        "description": "The availability zone to deploy the container group into. If not specified, the container group is nonzonal and might be deployed into any zone."
      }
    }
  },
  "resources": {
    "containerGroup": {
      "type": "Microsoft.ContainerInstance/containerGroups",
      "apiVersion": "2023-05-01",
      "name": "[parameters('name')]",
      "location": "[parameters('location')]",
      "properties": {
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
      },
      "zones": "[if(not(equals(parameters('zone'), null())), createArray(parameters('zone')), null())]"
    }
  },
  "outputs": {
    "name": {
      "type": "string",
      "value": "[parameters('name')]"
    },
    "resourceGroupName": {
      "type": "string",
      "value": "[resourceGroup().name]"
    },
    "resourceId": {
      "type": "string",
      "value": "[resourceId('Microsoft.ContainerInstance/containerGroups', parameters('name'))]"
    },
    "containerIPv4Address": {
      "type": "string",
      "value": "[reference('containerGroup').ipAddress.ip]"
    },
    "location": {
      "type": "string",
      "value": "[parameters('location')]"
    }
  }
}
```

The following resource is defined in the template:

* **[Microsoft.ContainerInstance/containerGroups](https://learn.microsoft.com/en-us/azure/templates/microsoft.containerinstance/containergroups)**: create an Azure container group. This template defines a group consisting of a single container instance.

More Azure Container Instances template samples can be found in the [quickstart template gallery](https://azure.microsoft.com/resources/templates/?resourceType=Microsoft.Containerinstance&pageNumber=1&sort=Popular).

To [deploy the container group into a specific availability zone](https://learn.microsoft.com/en-us/azure/reliability/reliability-container-instances#availability-zone-support), set the value of the `zone` parameter to the logical availability zone you want to deploy to.

Important

Zonal deployments are only available in regions that support availability zones. To see if your region supports availability zones, see [Azure Regions List](https://learn.microsoft.com/en-us/azure/reliability/regions-list).

1. Select the following image to sign in to Azure and open a template. The template creates a registry and a replica in another location.

[![Image 2: Button to deploy the Resource Manager template to Azure.](https://learn.microsoft.com/en-us/azure/reusable-content/ce-skilling/azure/media/template-deployments/deploy-to-azure-button.svg)](https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.containerinstance%2Faci-linuxcontainer-public-ip%2Fazuredeploy.json)

1. Select or enter the following values.

    *   **Subscription**: select an Azure subscription.
    *   **Resource group**: select **Create new**, enter a unique name for the resource group, and then select **OK**.
    *   **Location**: select a location for the resource group. Example: **Central US**.
    *   **Name**: accept the generated name for the instance, or enter a name.
    *   **Image**: accept the default image name. This sample Linux image packages a small web app written in Node.js that serves a static HTML page.

Accept default values for the remaining properties.

Review the terms and conditions. If you agree, select **I agree to the terms and conditions stated above**.

![Image 3: Template properties](https://learn.microsoft.com/en-us/azure/container-instances/media/container-instances-quickstart-template/template-properties.png)

1. After the instance successfully creates, you get a notification:

![Image 4: Portal notification](https://learn.microsoft.com/en-us/azure/container-instances/media/container-instances-quickstart-template/deployment-notification.png)

The Azure portal is used to deploy the template. In addition to the Azure portal, you can use the Azure PowerShell, Azure CLI, and REST API. To learn other deployment methods, see [Deploy templates](https://learn.microsoft.com/en-us/azure/azure-resource-manager/templates/deploy-cli).

Use the Azure portal or a tool such as the [Azure CLI](https://learn.microsoft.com/en-us/azure/container-instances/container-instances-quickstart) to review the properties of the container instance.

1. In the portal, search for Container Instances, and select the container instance you created.

2. On the **Overview** page, note the **Status** of the instance and its **IP address**.

![Image 5: Instance overview](https://learn.microsoft.com/en-us/azure/container-instances/media/container-instances-quickstart-template/aci-overview.png)

1. Once its status is _Running_, navigate to the IP address in your browser.

![Image 6: App deployed using Azure Container Instances viewed in browser](https://learn.microsoft.com/en-us/azure/container-instances/media/container-instances-quickstart-template/view-application-running-in-an-azure-container-instance.png)

Viewing the logs for a container instance is helpful when troubleshooting issues with your container or the application it runs.

To view the container's logs, under **Settings**, select **Containers**>**Logs**. You should see the HTTP GET request generated when you viewed the application in your browser.

![Image 7: Container logs in the Azure portal](https://learn.microsoft.com/en-us/azure/container-instances/media/container-instances-quickstart-template/aci-logs.png)

When you're done with the container, on the **Overview** page for the container instance, select **Delete**. When prompted, confirm the deletion.

In this quickstart, you created an Azure container instance from a public Microsoft image. If you'd like to build a container image and deploy it from a private Azure container registry, continue to the Azure Container Instances tutorial.

For a step-by-step tutorial that guides you through the process of creating a template, see:
