# Source: https://learn.microsoft.com/en-us/azure/container-instances/container-instances-vnet

Title: Deploy container group to Azure virtual network - Azure Container Instances

URL Source: https://learn.microsoft.com/en-us/azure/container-instances/container-instances-vnet

Markdown Content:
[Azure Virtual Network](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-networks-overview) provides secure, private networking for your Azure and on-premises resources. By deploying container groups into an Azure virtual network, your containers can communicate securely with other resources in the virtual network.

This article shows how to use the [az container create](https://learn.microsoft.com/en-us/cli/azure/container#az_container_create) command in the Azure CLI to deploy container groups to either a new virtual network or an existing virtual network.

Important

* Subnets must be delegated before using a virtual network
* Before deploying container groups in virtual networks, we suggest checking the limitation first. For networking scenarios and limitations, see [Virtual network scenarios and resources for Azure Container Instances](https://learn.microsoft.com/en-us/azure/container-instances/container-instances-virtual-network-concepts).
* Container group deployment to a virtual network is generally available for Linux and Windows containers, in most regions where Azure Container Instances is available. For details, see [available-regions](https://azure.microsoft.com/explore/global-infrastructure/products-by-region/?products=container-instances).

Important

[Network profiles](https://learn.microsoft.com/en-us/azure/container-instances/container-instances-virtual-network-concepts#network-profile) have been retired as of the `2021-07-01` API version. If you're using this or a more recent version, ignore any steps and actions related to network profiles.

Examples in this article are formatted for the Bash shell. If you prefer another shell such as PowerShell or Command Prompt, adjust the line continuation characters accordingly.

The automated deployment pathway uses the following environment variables and resource names throughout this guide. Users proceeding through the guide manually can use their own variables and names as preferred.

You need a resource group to manage all the resources used in the following examples. To create a resource group, use [az group create](https://learn.microsoft.com/en-us/cli/azure/group#az-group-create):

```
export RANDOM_ID="$(openssl rand -hex 3)"
export MY_RESOURCE_GROUP_NAME="myACIResourceGroup$RANDOM_ID"

az group create --name $MY_RESOURCE_GROUP_NAME --location eastus
```

A successful operation should produce output similar to the following JSON:

Results:

```
{
  "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx/resourceGroups/myACIResourceGroup123abc",
  "location": "abcdef",
  "managedBy": null,
  "name": "myACIResourceGroup123",
  "properties": {
    "provisioningState": "Succeeded"
  },
  "tags": null,
  "type": "Microsoft.Resources/resourceGroups"
}
```

Note

If you are using subnet IP range /29 to have only 3 IP addresses. we recommend always to go one range above (never below). For example, use subnet IP range /28 so you can have at least 1 or more IP buffer per container group. By doing this, you can avoid containers in stuck, not able to start, restart or even not able to stop states.

To deploy to a new virtual network and have Azure create the network resources for you automatically, specify the following when you execute [az container create](https://learn.microsoft.com/en-us/cli/azure/container#az_container_create):

* Virtual network name
* Virtual network address prefix in CIDR format
* Subnet name
* Subnet address prefix in CIDR format

The virtual network and subnet address prefixes specify the address spaces for the virtual network and subnet, respectively. These values are represented in Classless Inter-Domain Routing (CIDR) notation, for example `10.0.0.0/16`. For more information about working with subnets, see [Add, change, or delete a virtual network subnet](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-network-manage-subnet).

Once you deploy your first container group with this method, you can deploy to the same subnet by specifying the virtual network and subnet names, or the network profile that Azure automatically creates for you. Because Azure delegates the subnet to Azure Container Instances, you can deploy _only_ container groups to the subnet.

The following [az container create](https://learn.microsoft.com/en-us/cli/azure/container#az_container_create) command specifies settings for a new virtual network and subnet. Provide the name of a resource group that was created in a region where container group deployments in a virtual network are [available](https://learn.microsoft.com/en-us/azure/container-instances/container-instances-region-availability). This command deploys the public Microsoft aci-helloworld container that runs a small Node.js webserver serving a static web page. In the next section, you'll deploy a second container group to the same subnet, and test communication between the two container instances.

```
export MY_APP_CONTAINER_NAME="appcontainer"
export MY_VNET_NAME="aci-vnet"
export MY_SUBNET_NAME="aci-subnet"

az container create \
  --name $MY_APP_CONTAINER_NAME \
  --resource-group $MY_RESOURCE_GROUP_NAME \
  --image mcr.microsoft.com/azuredocs/aci-helloworld \
  --vnet $MY_VNET_NAME \
  --vnet-address-prefix 10.0.0.0/16 \
  --subnet $MY_SUBNET_NAME \
  --subnet-address-prefix 10.0.0.0/24
```

A successful operation should produce output similar to the following JSON:

Results:

```
{
  "confidentialComputeProperties": null,
  "containers": [
    {
      "command": null,
      "environmentVariables": [],
      "image": "mcr.microsoft.com/azuredocs/aci-helloworld",
      "instanceView": {
        "currentState": {
          "detailStatus": "",
          "exitCode": null,
          "finishTime": null,
          "startTime": "0000-00-00T00:00:00.000000+00:00",
          "state": "Running"
        },
        "events": [
          {
            "count": 1,
            "firstTimestamp": "0000-00-00T00:00:00+00:00",
            "lastTimestamp": "0000-00-00T00:00:00+00:00",
            "message": "Successfully pulled image \"mcr.microsoft.com/azuredocs/aci-helloworld@sha256:0000000000000000000000000000000000000000000000000000000000000000\"",
            "name": "Pulled",
            "type": "Normal"
          },
          {
            "count": 1,
            "firstTimestamp": "0000-00-00T00:00:00+00:00",
            "lastTimestamp": "0000-00-00T00:00:00+00:00",
            "message": "pulling image \"mcr.microsoft.com/azuredocs/aci-helloworld@sha256:0000000000000000000000000000000000000000000000000000000000000000\"",
            "name": "Pulling",
            "type": "Normal"
          },
          {
            "count": 1,
            "firstTimestamp": "0000-00-00T00:00:00+00:00",
            "lastTimestamp": "0000-00-00T00:00:00+00:00",
            "message": "Started container",
            "name": "Started",
            "type": "Normal"
          }
        ],
        "previousState": null,
        "restartCount": 0
      },
      "livenessProbe": null,
      "name": "appcontainer",
      "ports": [
        {
          "port": 80,
          "protocol": "TCP"
        }
      ],
      "readinessProbe": null,
      "resources": {
        "limits": null,
        "requests": {
          "cpu": 1.0,
          "gpu": null,
          "memoryInGb": 1.5
        }
      },
      "securityContext": null,
      "volumeMounts": null
    }
  ],
  "diagnostics": null,
  "dnsConfig": null,
  "encryptionProperties": null,
  "extensions": null,
  "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx/resourceGroups/myACIResourceGroup123/providers/Microsoft.ContainerInstance/containerGroups/appcontainer",
  "identity": null,
  "imageRegistryCredentials": null,
  "initContainers": [],
  "instanceView": {
    "events": [],
    "state": "Running"
  },
  "ipAddress": {
    "autoGeneratedDomainNameLabelScope": null,
    "dnsNameLabel": null,
    "fqdn": null,
    "ip": "10.0.0.4",
    "ports": [
      {
        "port": 80,
        "protocol": "TCP"
      }
    ],
    "type": "Private"
  },
  "location": "eastus",
  "name": "appcontainer",
  "osType": "Linux",
  "priority": null,
  "provisioningState": "Succeeded",
  "resourceGroup": "myACIResourceGroup123abc",
  "restartPolicy": "Always",
  "sku": "Standard",
  "subnetIds": [
    {
      "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx/resourceGroups/myACIResourceGroup123/providers/Microsoft.Network/virtualNetworks/aci-vnet/subnets/aci-subnet",
      "name": null,
      "resourceGroup": "myACIResourceGroup123abc"
    }
  ],
  "tags": {},
  "type": "Microsoft.ContainerInstance/containerGroups",
  "volumes": null,
  "zones": null
}
```

When you deploy to a new virtual network by using this method, the deployment can take a few minutes while the network resources are created. After the initial deployment, further container group deployments to the same subnet complete more quickly.

To deploy a container group to an existing virtual network:

1. Create a subnet within your existing virtual network, use an existing subnet in which a container group is already deployed, or use an existing subnet emptied of _all_ other resources and configuration. The subnet that you use for container groups can contain only container groups. Before you deploy a container group to a subnet, you must explicitly delegate the subnet before provisioning. Once delegated, the subnet can be used only for container groups. If you attempt to deploy resources other than container groups to a delegated subnet, the operation fails.
2. Deploy a container group with [az container create](https://learn.microsoft.com/en-us/cli/azure/container#az_container_create) and specify one of the following:
    *Virtual network name and subnet name
    *   Virtual network resource ID and subnet resource ID, which allows using a virtual network from a different resource group

You can also deploy a container group to an existing virtual network by using a YAML file, a [Resource Manager template](https://github.com/Azure/azure-quickstart-templates/tree/master/quickstarts/microsoft.containerinstance/aci-vnet), or another programmatic method such as with the Python SDK.

For example, when using a YAML file, you can deploy to a virtual network with a subnet delegated to Azure Container Instances. Specify the following properties:

* `ipAddress`: The private IP address settings for the container group.
  * `ports`: The ports to open, if any.
  * `protocol`: The protocol (TCP or UDP) for the opened port.

* `subnetIds`: The resource IDs of the subnets to be deployed to
  * `id`: The resource ID of the subnet
  * `name`: The name of the subnet

This YAML creates a container group in your virtual network. Enter your container group name in the name fields and your subnet ID in the subnet ID field. We use _appcontaineryaml_ for the name. If you need to find your subnet ID and no longer have access to previous outputs, you can use the [az container show](https://learn.microsoft.com/en-us/cli/azure/container#az_container_show) command to view it. Look for the `id` field under `subnetIds`.

```
apiVersion: '2021-07-01'
location: eastus
name: appcontaineryaml
properties:
  containers:
  - name: appcontaineryaml
    properties:
      image: mcr.microsoft.com/azuredocs/aci-helloworld
      ports:
      - port: 80
        protocol: TCP
      resources:
        requests:
          cpu: 1.0
          memoryInGB: 1.5
  ipAddress:
    type: Private
    ports:
    - protocol: tcp
      port: '80'
  osType: Linux
  restartPolicy: Always
  subnetIds:
    - id: <subnet_id>
      name: default
tags: null
type: Microsoft.ContainerInstance/containerGroups
```

The following Bash command is for the automated deployment pathway.

```
export MY_YAML_APP_CONTAINER_NAME="appcontaineryaml"
export MY_SUBNET_ID="/subscriptions/$(az account show --query id --output tsv)/resourceGroups/$MY_RESOURCE_GROUP_NAME/providers/Microsoft.Network/virtualNetworks/$MY_VNET_NAME/subnets/$MY_SUBNET_NAME"
```

```
echo -e "apiVersion: '2021-07-01'\nlocation: eastus\nname: $MY_YAML_APP_CONTAINER_NAME\nproperties:\n  containers:\n  - name: $MY_YAML_APP_CONTAINER_NAME\n    properties:\n      image: mcr.microsoft.com/azuredocs/aci-helloworld\n      ports:\n      - port: 80\n        protocol: TCP\n      resources:\n        requests:\n          cpu: 1.0\n          memoryInGB: 1.5\n  ipAddress:\n    type: Private\n    ports:\n    - protocol: tcp\n      port: '80'\n  osType: Linux\n  restartPolicy: Always\n  subnetIds:\n    - id: $MY_SUBNET_ID\n      name: default\ntags: null\ntype: Microsoft.ContainerInstance/containerGroups" > container-instances-vnet.yaml
```

Deploy the container group with the [az container create](https://learn.microsoft.com/en-us/cli/azure/container#az_container_create) command, specifying the YAML file name for the `--file` parameter:

```
az container create --resource-group $MY_RESOURCE_GROUP_NAME \
  --file container-instances-vnet.yaml
```

The following Bash command is for the automated deployment pathway.

```
rm container-instances-vnet.yaml
```

Once the deployment completes, run the [az container show](https://learn.microsoft.com/en-us/cli/azure/container#az_container_show) command to display its status:

```
az container list --resource-group $MY_RESOURCE_GROUP_NAME --output table
```

The output should resemble the sample below:

Results:

```
Name              ResourceGroup             Status     Image                                       IP:ports        Network    CPU/Memory       OsType    Location
----------------  ------------------------  ---------  ------------------------------------------  --------------  ---------  ---------------  --------  ----------
appcontainer      myACIResourceGroup123abc  Succeeded  mcr.microsoft.com/azuredocs/aci-helloworld  10.0.0.4:80,80  Private    1.0 core/1.5 gb  Linux     abcdef
appcontaineryaml  myACIResourceGroup123abc  Succeeded  mcr.microsoft.com/azuredocs/aci-helloworld  10.0.0.5:80,80  Private    1.0 core/1.5 gb  Linux     abcdef
```

The following example deploys a third container group to the same subnet created previously. Using an Alpine Linux image, it verifies communication between itself and the first container instance.

Note

Due to rate limiting in effect for pulling public Docker images like the Alpine Linux one used here, you may receive an error in the form:

(RegistryErrorResponse) An error response is received from the docker registry 'index.docker.io'. Please retry later. Code: RegistryErrorResponse Message: An error response is received from the docker registry 'index.docker.io'. Please retry later.

The following Bash command is for the automated deployment pathway.

```
echo -e "Due to rate limiting in effect for pulling public Docker images like the Alpine Linux one used here, you may receive an error in the form:\n\n(RegistryErrorResponse) An error response is received from the docker registry 'index.docker.io'. Please retry later.\nCode: RegistryErrorResponse\nMessage: An error response is received from the docker registry 'index.docker.io'. Please retry later.\n\nIf this occurs, the automated deployment will exit. You can try again or go to the end of the guide to see instructions for cleaning up your resources."
```

First, get the IP address of the first container group you deployed, the _appcontainer_:

```
az container show --resource-group $MY_RESOURCE_GROUP_NAME \
  --name $MY_APP_CONTAINER_NAME \
  --query ipAddress.ip --output tsv
```

The output displays the IP address of the container group in the private subnet. For example:

Results:

```
10.0.0.4
```

Now, set `CONTAINER_GROUP_IP` to the IP you retrieved with the `az container show` command, and execute the following `az container create` command. This second container, _commchecker_, runs an Alpine Linux-based image and executes `wget` against the first container group's private subnet IP address.

```
export MY_COMM_CHECKER_NAME="commchecker"

az container create \
  --resource-group $MY_RESOURCE_GROUP_NAME \
  --name $MY_COMM_CHECKER_NAME \
  --image alpine:3.4 \
  --command-line "wget 10.0.0.4" \
  --restart-policy never \
  --vnet $MY_VNET_NAME \
  --subnet $MY_SUBNET_NAME
```

After this second container deployment completes, pull its logs so you can see the output of the `wget` command it executed:

```
az container logs --resource-group $MY_RESOURCE_GROUP_NAME --name $MY_COMM_CHECKER_NAME
```

If the second container communicated successfully with the first, output is similar to:

```
Connecting to 10.0.0.4 (10.0.0.4:80)
index.html           100% |*******************************|  1663   0:00:00 ETA
```

The log output should show that `wget` was able to connect and download the index file from the first container using its private IP address on the local subnet. Network traffic between the two container groups remained within the virtual network.

If you don't plan to continue using these resources, you can delete them to avoid Azure charges. You can clean up all the resources you used in this guide by deleting the resource group with the [az group delete](https://learn.microsoft.com/en-us/cli/azure/group#az-group-delete) command. Once deleted, **these resources are unrecoverable**.

* To deploy a new virtual network, subnet, network profile, and container group using a Resource Manager template, see [Create an Azure container group with virtual network](https://github.com/Azure/azure-quickstart-templates/tree/master/quickstarts/microsoft.containerinstance/aci-vnet).

* To deploy Azure Container Instances that can pull images from an Azure Container Registry through a private endpoint, see [Deploy to Azure Container Instances from Azure Container Registry using a managed identity](https://learn.microsoft.com/en-us/azure/container-instances/using-azure-container-registry-mi).
