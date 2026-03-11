# Source: https://learn.microsoft.com/en-us/azure/container-instances/container-instances-volume-azure-files

Title: Mount Azure Files volume to container group - Azure Container Instances

URL Source: https://learn.microsoft.com/en-us/azure/container-instances/container-instances-volume-azure-files

Markdown Content:
By default, Azure Container Instances are stateless. If the container is restarted, crashes, or stops, all of its state is lost. To persist state beyond the lifetime of the container, you must mount a volume from an external store. As shown in this article, Azure Container Instances can mount an Azure file share created with [Azure Files](https://learn.microsoft.com/en-us/azure/storage/files/storage-files-introduction). Azure Files offers fully managed file shares hosted in Azure Storage that are accessible via the industry standard Server Message Block (SMB) protocol. Using an Azure file share with Azure Container Instances provides file-sharing features similar to using an Azure file share with Azure virtual machines.

* Azure Storage doesn't support SMB mounting of file share using managed identity
* You can only mount Azure Files shares to Linux containers. Review more about the differences in feature support for Linux and Windows container groups in the [overview](https://learn.microsoft.com/en-us/azure/container-instances/container-instances-overview#linux-and-windows-containers).
* Azure file share volume mount requires the Linux container run as _root_.
* Azure File share volume mounts are limited to CIFS support.

Note

Mounting an Azure Files share to a container instance is similar to a Docker [bind mount](https://docs.docker.com/storage/bind-mounts/). If you mount a share into a container directory in which files or directories exist, the mount obscures files or directories, making them inaccessible while the container runs.

Important

If the outbound connection to the internet is blocked in the delegated subnet, you must add a [service endpoint](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-network-service-endpoints-overview) to Azure Strorage on your delegated subnet.

Before using an Azure file share with Azure Container Instances, you must create it. Run the following script to create a storage account to host the file share, and the share itself. The storage account name must be globally unique, so the script adds a random value to the base string.

```
# Change these four parameters as needed
ACI_PERS_RESOURCE_GROUP=myResourceGroup
ACI_PERS_STORAGE_ACCOUNT_NAME=mystorageaccount$RANDOM
ACI_PERS_LOCATION=eastus
ACI_PERS_SHARE_NAME=acishare

# Create the storage account with the parameters
az storage account create \
    --resource-group $ACI_PERS_RESOURCE_GROUP \
    --name $ACI_PERS_STORAGE_ACCOUNT_NAME \
    --location $ACI_PERS_LOCATION \
    --sku Standard_LRS

# Create the file share
az storage share create \
  --name $ACI_PERS_SHARE_NAME \
  --account-name $ACI_PERS_STORAGE_ACCOUNT_NAME
```

To mount an Azure file share as a volume in Azure Container Instances, you need three values: the storage account name, the share name, and the storage access key.

* **Storage account name** - If you used the preceding script, the storage account name was stored in the `$ACI_PERS_STORAGE_ACCOUNT_NAME` variable. To see the account name, type:

```
echo $ACI_PERS_STORAGE_ACCOUNT_NAME
```

* **Share name** - This value is already known (defined as `acishare` in the preceding script)

* **Storage account key** - This value can be found using the following command:

```
STORAGE_KEY=$(az storage account keys list --resource-group $ACI_PERS_RESOURCE_GROUP --account-name $ACI_PERS_STORAGE_ACCOUNT_NAME --query "[0].value" --output tsv)
echo $STORAGE_KEY
```

To mount an Azure file share as a volume in a container by using the Azure CLI, specify the share and volume mount point when you create the container with [az container create](https://learn.microsoft.com/en-us/cli/azure/container#az_container_create). If you followed the previous steps, you can mount the share you created earlier by using the following command to create a container:

```
az container create \
    --resource-group $ACI_PERS_RESOURCE_GROUP \
    --name hellofiles \
    --image mcr.microsoft.com/azuredocs/aci-hellofiles \
    --dns-name-label aci-demo \
    --ports 80 \
    --azure-file-volume-account-name $ACI_PERS_STORAGE_ACCOUNT_NAME \
    --azure-file-volume-account-key $STORAGE_KEY \
    --azure-file-volume-share-name $ACI_PERS_SHARE_NAME \
    --azure-file-volume-mount-path /aci/logs/
```

The `--dns-name-label` value must be unique within the Azure region where you create the container instance. Update the value in the preceding command if you receive a **DNS name label** error message when you execute the command.

Once the container starts up, you can use the web app deployed via the Microsoft aci-hellofiles image to create small text files in the Azure file share at the mount path you specified. Obtain the web app's fully qualified domain name (FQDN) with the [az container show](https://learn.microsoft.com/en-us/cli/azure/container#az_container_show) command:

```
az container show --resource-group $ACI_PERS_RESOURCE_GROUP \
  --name hellofiles --query ipAddress.fqdn --output tsv
```

After saving text using the app, you can use the [Azure portal](https://portal.azure.com/) or a tool like the [Microsoft Azure Storage Explorer](https://storageexplorer.com/) to retrieve and inspect the file or files written to the file share.

You can also deploy a container group and mount a volume in a container with the Azure CLI and a [YAML template](https://learn.microsoft.com/en-us/azure/container-instances/container-instances-multi-container-yaml). Deploying by YAML template is a preferred method when deploying container groups consisting of multiple containers.

The following YAML template defines a container group with one container created with the `aci-hellofiles` image. The container mounts the Azure file share _acishare_ created previously as a volume. Where indicated, enter the name and storage key for the storage account that hosts the file share.

As in the CLI example, the `dnsNameLabel` value must be unique within the Azure region where you create the container instance. Update the value in the YAML file if needed.

```
apiVersion: '2019-12-01'
location: eastus
name: file-share-demo
properties:
  containers:
  - name: hellofiles
    properties:
      environmentVariables: []
      image: mcr.microsoft.com/azuredocs/aci-hellofiles
      ports:
      - port: 80
      resources:
        requests:
          cpu: 1.0
          memoryInGB: 1.5
      volumeMounts:
      - mountPath: /aci/logs/
        name: filesharevolume
  osType: Linux
  restartPolicy: Always
  ipAddress:
    type: Public
    ports:
      - port: 80
    dnsNameLabel: aci-demo
  volumes:
  - name: filesharevolume
    azureFile:
      sharename: acishare
      storageAccountName: <Storage account name>
      storageAccountKey: <Storage account key>
tags: {}
type: Microsoft.ContainerInstance/containerGroups
```

To deploy with the YAML template, save the preceding YAML to a file named `deploy-aci.yaml`, then execute the [az container create](https://learn.microsoft.com/en-us/cli/azure/container#az_container_create) command with the `--file` parameter:

```
# Deploy with YAML template
az container create --resource-group myResourceGroup --file deploy-aci.yaml
```

In addition to CLI and YAML deployment, you can deploy a container group and mount a volume in a container using an Azure [Resource Manager template](https://learn.microsoft.com/en-us/azure/templates/microsoft.containerinstance/containergroups).

First, populate the `volumes` array in the container group `properties` section of the template.

Then, for each container in which you'd like to mount the volume, populate the `volumeMounts` array in the `properties` section of the container definition.

The following Resource Manager template defines a container group with one container created with the `aci-hellofiles` image. The container mounts the Azure file share _acishare_ created previously as a volume. Where indicated, enter the name and storage key for the storage account that hosts the file share.

As in the previous examples, the `dnsNameLabel` value must be unique within the Azure region where you create the container instance. Update the value in the template if needed.

```
{
  "$schema": "https://schema.management.azure.com/schemas/2015-01-01/deploymentTemplate.json#",
  "contentVersion": "1.0.0.0",
  "variables": {
    "container1name": "hellofiles",
    "container1image": "mcr.microsoft.com/azuredocs/aci-hellofiles"
  },
  "resources": [
    {
      "name": "file-share-demo",
      "type": "Microsoft.ContainerInstance/containerGroups",
      "apiVersion": "2019-12-01",
      "location": "[resourceGroup().location]",
      "properties": {
        "containers": [
          {
            "name": "[variables('container1name')]",
            "properties": {
              "image": "[variables('container1image')]",
              "resources": {
                "requests": {
                  "cpu": 1,
                  "memoryInGb": 1.5
                }
              },
              "ports": [
                {
                  "port": 80
                }
              ],
              "volumeMounts": [
                {
                  "name": "filesharevolume",
                  "mountPath": "/aci/logs"
                }
              ]
            }
          }
        ],
        "osType": "Linux",
        "ipAddress": {
          "type": "Public",
          "ports": [
            {
              "protocol": "tcp",
              "port": "80"
            }
          ],
          "dnsNameLabel": "aci-demo"
        },
        "volumes": [
          {
            "name": "filesharevolume",
            "azureFile": {
                "shareName": "acishare",
                "storageAccountName": "<Storage account name>",
                "storageAccountKey": "<Storage account key>"
            }
          }
        ]
      }
    }
  ]
}
```

To deploy with the Resource Manager template, save the preceding JSON to a file named `deploy-aci.json`, then execute the [az deployment group create](https://learn.microsoft.com/en-us/cli/azure/deployment/group#az_deployment_group_create) command with the `--template-file` parameter:

```
# Deploy with Resource Manager template
az deployment group create --resource-group myResourceGroup --template-file deploy-aci.json
```

To mount multiple volumes in a container instance, you must deploy using an [Azure Resource Manager template](https://learn.microsoft.com/en-us/azure/templates/microsoft.containerinstance/containergroups), a YAML file, or another programmatic method. To use a template or YAML file, provide the share details and define the volumes by populating the `volumes` array in the `properties` section of the file.

For example, if you created two Azure Files shares named _share1_ and _share2_ in storage account _myStorageAccount_, the `volumes` array in a Resource Manager template would appear similar to the following example:

```
"volumes": [{
  "name": "myvolume1",
  "azureFile": {
    "shareName": "share1",
    "storageAccountName": "myStorageAccount",
    "storageAccountKey": "<storage-account-key>"
  }
},
{
  "name": "myvolume2",
  "azureFile": {
    "shareName": "share2",
    "storageAccountName": "myStorageAccount",
    "storageAccountKey": "<storage-account-key>"
  }
}]
```

Next, for each container in the container group in which you'd like to mount the volumes, populate the `volumeMounts` array in the `properties` section of the container definition. For example, this mounts the two volumes, _myvolume1_ and _myvolume2_, previously defined:

```
"volumeMounts": [{
  "name": "myvolume1",
  "mountPath": "/mnt/share1/"
},
{
  "name": "myvolume2",
  "mountPath": "/mnt/share2/"
}]
```

Learn how to mount other volume types in Azure Container Instances:

* [Mount an emptyDir volume in Azure Container Instances](https://learn.microsoft.com/en-us/azure/container-instances/container-instances-volume-emptydir)
* [Mount a gitRepo volume in Azure Container Instances](https://learn.microsoft.com/en-us/azure/container-instances/container-instances-volume-gitrepo)
* [Mount a secret volume in Azure Container Instances](https://learn.microsoft.com/en-us/azure/container-instances/container-instances-volume-secret)
