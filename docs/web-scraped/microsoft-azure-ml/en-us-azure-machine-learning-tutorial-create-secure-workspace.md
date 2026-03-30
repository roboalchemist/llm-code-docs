# Source: https://learn.microsoft.com/en-us/azure/machine-learning/tutorial-create-secure-workspace?view=azureml-api-2

Title: Create a secure workspace with a managed virtual network - Azure Machine Learning

URL Source: https://learn.microsoft.com/en-us/azure/machine-learning/tutorial-create-secure-workspace?view=azureml-api-2

Markdown Content:
In this article, you learn how to create and connect to a secure Azure Machine Learning workspace. The steps in this article use an Azure Machine Learning managed virtual network to create a security boundary around resources used by Azure Machine Learning.

In this tutorial, you accomplish the following tasks:

*   Create an Azure Machine Learning workspace configured to use a managed virtual network.
*   Create an Azure Machine Learning compute cluster. You use a compute cluster when **training machine learning models in the cloud**.

After completing this tutorial, you have the following architecture:

*   An Azure Machine Learning workspace that uses a private endpoint to communicate through the managed network.
*   An Azure Storage Account that uses private endpoints to allow storage services such as blob and file to communicate through the managed network.
*   An Azure Container Registry that uses a private endpoint to communicate through the managed network.
*   An Azure Key Vault that uses a private endpoint to communicate through the managed network.
*   An Azure Machine Learning compute instance and compute cluster secured by the managed network.

*   An Azure subscription. If you don't have an Azure subscription, create a free account before you begin. Try the [free or paid version of Azure Machine Learning](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
*   Python 3.10 or later.

You can connect to the secured workspace in several ways. In this tutorial, use a **jump box**. A jump box is a virtual machine in an Azure Virtual Network. You can connect to it by using your web browser and Azure Bastion.

The following table lists several other ways that you might connect to the secure workspace:

| Method | Description |
| --- | --- |
| [Azure VPN gateway](https://learn.microsoft.com/en-us/azure/vpn-gateway/vpn-gateway-about-vpngateways) | Connects on-premises networks to an Azure Virtual Network over a private connection. A private endpoint for your workspace is created within that virtual network. Connection is made over the public internet. |
| [ExpressRoute](https://learn.microsoft.com/en-us/azure/expressroute/expressroute-introduction) | Connects on-premises networks into the cloud over a private connection. Connection is made using a connectivity provider. |

Important

When using a **VPN gateway** or **ExpressRoute**, plan how name resolution works between your on-premises resources and those in the cloud. For more information, see [Use a custom DNS server](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-custom-dns?view=azureml-api-2).

Use the following steps to create an Azure Virtual Machine to use as a jump box. From the VM desktop, you can use the browser on the VM to connect to resources inside the managed virtual network, such as Azure Machine Learning studio. Or you can install development tools on the VM.

Tip

The following steps create a Windows 11 enterprise VM. Depending on your requirements, you might want to select a different VM image. The Windows 11 (or 10) enterprise image is useful if you need to join the VM to your organization's domain.

1.   In the [Azure portal](https://portal.azure.com/), select the portal menu in the upper left corner. From the menu, select **+ Create a resource** and then enter **Virtual Machine**. Select the **Virtual Machine** entry, and then select **Create**.

2.   From the **Basics** tab, select the **subscription**, **resource group**, and **Region** to create the service in. Provide values for the following fields:

    *   **Virtual machine name**: A unique name for the VM.

    *   **Username**: The username you use to sign in to the VM.

    *   **Password**: The password for the username.

    *   **Security type**: Standard.

    *   **Image**: Windows 11 Enterprise.

Tip

If Windows 11 Enterprise isn't in the list for image selection, use _See all images_ _. Find the **Windows 11** entry from Microsoft, and use the **Select** drop-down to select the enterprise image. 

You can leave other fields at the default values.

![Image 1: Screenshot of the virtual machine basics configuration.](https://learn.microsoft.com/en-us/azure/machine-learning/media/tutorial-create-secure-workspace/create-virtual-machine-basic.png?view=azureml-api-2)

3.   Select **Networking**. Review the networking information and make sure that it's not using the 172.17.0.0/16 IP address range. If it is, select a different range such as 172.16.0.0/16. The 172.17.0.0/16 range can cause conflicts with Docker.

Note

The Azure Virtual Machine creates its own Azure Virtual Network for network isolation. This network is separate from the managed virtual network used by Azure Machine Learning. 
![Image 2: Screenshot of the networking tab for the virtual machine.](https://learn.microsoft.com/en-us/azure/machine-learning/media/tutorial-create-secure-workspace/virtual-machine-networking.png?view=azureml-api-2)

4.   Select **Review + create**. Verify that the information is correct, and then select **Create**.

By using Azure Bastion, you can connect to the VM desktop through your browser.

1.   In the Azure portal, select the VM you created earlier. From the **Connect** section of the page, select **Bastion** and then **Deploy Bastion**.

![Image 3: Screenshot of the deploy Bastion option.](https://learn.microsoft.com/en-us/azure/machine-learning/media/tutorial-create-secure-workspace/virtual-machine-deploy-bastion.png?view=azureml-api-2)

2.   After the portal deploys the Bastion service, it returns you to a connection dialog. Don't use this dialog yet.

1.   In the [Azure portal](https://portal.azure.com/), select the portal menu in the upper left corner. From the menu, select **+ Create a resource** and then enter **Azure Machine Learning**. Select the **Azure Machine Learning** entry, and then select **Create**.

2.   From the **Basics** tab, select the **subscription**, **resource group**, and **Region** to create the service in. Enter a unique name for the **Workspace name**. Leave the rest of the fields at the default values. The portal creates new instances of the required services for the workspace.

![Image 4: Screenshot of the workspace creation form.](https://learn.microsoft.com/en-us/azure/machine-learning/media/tutorial-create-secure-workspace/create-workspace.png?view=azureml-api-2)

3.   From the **Networking** tab, select **Private with Internet Outbound**.

Note

This tutorial uses internet outbound access to keep setup simple. If your organization requires stricter egress controls, use a managed virtual network configuration that allows only approved outbound traffic. 
![Image 5: Screenshot of the workspace network tab with internet outbound selected.](https://learn.microsoft.com/en-us/azure/machine-learning/media/tutorial-create-secure-workspace/private-internet-outbound.png?view=azureml-api-2)

4.   From the **Networking** tab, in the **Workspace inbound access** section, select **+ Add**.

![Image 6: Screenshot showing the add button for inbound access.](https://learn.microsoft.com/en-us/azure/machine-learning/media/tutorial-create-secure-workspace/workspace-inbound-access.png?view=azureml-api-2)

5.   From the **Create private endpoint** form, enter a unique value in the **Name** field. Select the **Virtual network** you created earlier with the VM, and select the default **Subnet**. Leave the rest of the fields at the default values. Select **OK** to save the endpoint.

![Image 7: Screenshot of the form to create a private endpoint.](https://learn.microsoft.com/en-us/azure/machine-learning/media/tutorial-create-secure-workspace/private-endpoint-workspace.png?view=azureml-api-2)

6.   Select **Review + create**. Verify that the information is correct, and then select **Create**.

7.   After the portal creates the workspace, select **Go to resource**.

1.   From the [Azure portal](https://portal.azure.com/), select the VM you created earlier.

2.   From the **Connect** section, select **Bastion**. Enter the username and password you configured for the VM, and then select **Connect**.

![Image 8: Screenshot of the Bastion connect form.](https://learn.microsoft.com/en-us/azure/machine-learning/media/tutorial-create-secure-workspace/virtual-machine-bastion-connect.png?view=azureml-api-2)

At this point, the workspace is created **but the managed virtual network isn't**. You configure the managed virtual network when you create the workspace. To create the managed virtual network, create a compute resource or manually provision the network.

Important

If you plan to run serverless Spark jobs, manually start managed virtual network provisioning before you submit Spark jobs.

Use the following steps to create a compute instance.

1.   From the **VM desktop**, use the browser to open the [Azure Machine Learning studio](https://ml.azure.com/) and select the workspace you created earlier.

2.   From studio, select **Compute**, **Compute instances**, and then **+ New**.

![Image 9: Screenshot of the new compute option in studio.](https://learn.microsoft.com/en-us/azure/machine-learning/media/tutorial-create-secure-workspace/create-new-compute-instance.png?view=azureml-api-2)

3.   From the **Configure required settings** dialog, enter a unique value as the **Compute name**. Leave the rest of the selections at the default value.

4.   Select **Create**. The compute instance takes a few minutes to create. The compute instance is created within the managed network.

Tip

It can take several minutes to create the first compute resource. This delay occurs because the managed virtual network is also being created. The managed virtual network isn't created until the first compute resource is created. Subsequent managed compute resources are created much faster. 

Because Azure Machine Learning studio partially runs in the web browser on the client, the client needs direct access to the default storage account for the workspace to perform data operations. To enable direct access, use the following steps:

1.   From the [Azure portal](https://portal.azure.com/), select the jump box VM you created earlier. From the **Overview** section, copy the **Public IP address**.

2.   From the [Azure portal](https://portal.azure.com/), select the workspace you created earlier. From the **Overview** section, select the link for the **Storage** entry.

3.   From the storage account, select **Networking**, and add the jump box's _public_ IP address to the **Firewall** section.

Tip

In a scenario where you use a VPN gateway or ExpressRoute instead of a jump box, you can add a private endpoint or service endpoint for the storage account to the Azure Virtual Network. By using a private endpoint or service endpoint, multiple clients connecting through the Azure Virtual Network can successfully perform storage operations through studio. 
At this point, you can use the studio to interactively work with notebooks on the compute instance and run training jobs. For a tutorial, see [Tutorial: Model development](https://learn.microsoft.com/en-us/azure/machine-learning/tutorial-cloud-workstation?view=azureml-api-2).

While it's running (started), the compute instance continues charging your subscription. To avoid excess cost, **stop** it when you don't use it.

From studio, select **Compute**, **Compute instances**, and then select the compute instance. Finally, select **Stop** from the top of the page.

![Image 10: Screenshot of stop button for compute instance](https://learn.microsoft.com/en-us/azure/machine-learning/media/tutorial-create-secure-workspace/compute-instance-stop.png?view=azureml-api-2)

If you plan to continue using the secured workspace and other resources, skip this section.

To delete all resources that you created in this tutorial, use the following steps:

1.   In the Azure portal, select **Resource groups**.

2.   From the list, select the resource group that you created in this tutorial.

3.   Select **Delete resource group**.

![Image 11: Screenshot of delete resource group button](https://learn.microsoft.com/en-us/azure/machine-learning/media/tutorial-create-secure-workspace/delete-resources.png?view=azureml-api-2)

4.   Enter the resource group name, and then select **Delete**.

Now that you have a secure workspace and can access studio, consider the following resources:

*   [Deploy a model to an online endpoint with network isolation](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-secure-online-endpoint?view=azureml-api-2)
*   [Secure your workspace with a managed virtual network](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-managed-network?view=azureml-api-2)
*   [Tutorial: Model development on a cloud workstation](https://learn.microsoft.com/en-us/azure/machine-learning/tutorial-cloud-workstation?view=azureml-api-2)
