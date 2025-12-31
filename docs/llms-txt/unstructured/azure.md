# Source: https://docs.unstructured.io/open-source/ingestion/source-connectors/azure.md

# Source: https://docs.unstructured.io/open-source/ingestion/destination-connectors/azure.md

# Source: https://docs.unstructured.io/api-reference/legacy-api/azure.md

# Source: https://docs.unstructured.io/open-source/ingestion/source-connectors/azure.md

# Source: https://docs.unstructured.io/open-source/ingestion/destination-connectors/azure.md

# Source: https://docs.unstructured.io/api-reference/legacy-api/azure.md

# Source: https://docs.unstructured.io/open-source/ingestion/source-connectors/azure.md

# Source: https://docs.unstructured.io/open-source/ingestion/destination-connectors/azure.md

# Source: https://docs.unstructured.io/api-reference/legacy-api/azure.md

# Unstructured API on Azure

<Warning>
  The Unstructured API on Azure is deprecated. It is no longer supported and is not being actively updated.
  Unstructured is now available on the Azure Marketplace as a private offering. To explore supported options
  for running Unstructured within your virtual private cloud (VPC), email Unstructured Sales at
  [sales@unstructured.io](mailto:sales@unstructured.io).

  This page is not being actively updated. It might contain out-of-date information. This page is provided for legacy reference purposes only.
</Warning>

Follow these steps to deploy the Unstructured API service into your Azure account.

<Warning>
  This article describes how to create several interrelated resources in your Azure account.
  Your Azure account will be charged on an ongoing basis for these resources, even if you are not actively using them.<br /><br />
  Manually shutting down the associated Azure virtual machine when you are not using it can help reduce—but not fully eliminate—these ongoing charges.<br /><br />
  To stop accruing all related ongoing charges, you must delete all of the associated Azure resources.
</Warning>

<Steps>
  <Step title=" Log in to the Azure Portal">
    Go to [https://portal.azure.com](https://portal.azure.com/).
  </Step>

  <Step title="Access the Azure Marketplace">
    Go to the [Unstructured Data Preprocessing - Customer Hosted API](https://azuremarketplace.microsoft.com/en-us/marketplace/apps/unstructured1691024866136.customer_api_v1?tab=Overview/) offering in the Azure Marketplace.

        <img src="https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/Azure_Step2.png?fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=0a3e2db8d53ba51c958e4dc949c20cde" alt="Azure Marketplace" data-og-width="2670" width="2670" data-og-height="1296" height="1296" data-path="img/api/Azure_Step2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/Azure_Step2.png?w=280&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=6f7efa9ae6767b75f68218b5ef1dd630 280w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/Azure_Step2.png?w=560&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=92be6010eba9a5abb39e2f0e1b7dabb3 560w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/Azure_Step2.png?w=840&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=c5f8c0739566729b61e5b4dffef94bfd 840w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/Azure_Step2.png?w=1100&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=5f21c0952314e92224c85a642cd7c7a8 1100w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/Azure_Step2.png?w=1650&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=c77ba9877dac4f4862b4cfbd9cefabab 1650w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/Azure_Step2.png?w=2500&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=1ff31f700973c0fef520e8a143b94afe 2500w" />
  </Step>

  <Step title="Start the deployment process">
    1. Click **Get It Now** and fill out the form.
    2. Read the terms and click **Continue**.
    3. Click **Create**.

        <img src="https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/Azure_Step3.png?fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=d489b4c86ae06d70addcf1ade2439ba9" alt="Deployment Process" data-og-width="2086" width="2086" data-og-height="1562" height="1562" data-path="img/api/Azure_Step3.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/Azure_Step3.png?w=280&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=6afb5a0dbb4972113d8137ed5f04a235 280w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/Azure_Step3.png?w=560&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=ef15d7b5b7d2945759ce5df7a390a0f8 560w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/Azure_Step3.png?w=840&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=a2f9cc48988aae622c7c530e01ad0505 840w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/Azure_Step3.png?w=1100&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=eaae11ec129c0c660f7959319373cded 1100w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/Azure_Step3.png?w=1650&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=e7398c4fc3d4ee8f08f09053e648805d 1650w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/Azure_Step3.png?w=2500&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=be7b308bf5bdcbabe592747ff6e9e8ea 2500w" />
  </Step>

  <Step title=" Configure the deployment options">
    1. On the **Create a virtual machine** page, click the **Basics** tab.

    2. In the **Project details** section, select an existing **Subscription**, and select an **Resource group** from the dropdown menus, or create a new resource group by clicking **Create new**.

       <img src="https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/Azure_Step4a.png?fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=5943b437891c592174aa209b92ac5840" alt="project details" data-og-width="1562" width="1562" data-og-height="816" height="816" data-path="img/api/Azure_Step4a.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/Azure_Step4a.png?w=280&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=5ee661e0af2e74732ecb4a15f56d3bce 280w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/Azure_Step4a.png?w=560&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=584704082e7ca54b307091fad318537e 560w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/Azure_Step4a.png?w=840&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=ea2c8dd370abfb5c9774a3c773b3fef8 840w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/Azure_Step4a.png?w=1100&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=2245c81dc4bd6c6f567daee3fb984bef 1100w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/Azure_Step4a.png?w=1650&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=f09b2124260373d8fabe20ed3fda58dc 1650w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/Azure_Step4a.png?w=2500&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=0a535c05663df89a279b09323427f580 2500w" />

    3. In the **Instance details** section, enter a name in the **Virtual machine name** field. Note this name, as you will need it later steps.

    4. Select a **Region** from the dropdown menu.

    5. For **Image**, select **Unstructured Customer Hosted API Hourly - x64 Gen2** (*default*).

    6. For **Size**, select a VM size from the dropdown menu, or leave the default VM size selection. To learn more, see [Azure VM comparisons](https://azure.microsoft.com/en-us/pricing/details/virtual-machines/linux/).

       <img src="https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/Azure_Step4b.png?fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=4ed604cb032b6bfe3cd3c0d41a547221" alt="instance details" data-og-width="1562" width="1562" data-og-height="1088" height="1088" data-path="img/api/Azure_Step4b.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/Azure_Step4b.png?w=280&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=d0bbe497563bd738597647efba43bb5b 280w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/Azure_Step4b.png?w=560&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=65e1dbaaf3c7f2c28c7d87d5cc71bf56 560w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/Azure_Step4b.png?w=840&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=99405467dd8c0c8eadeee00396eccc91 840w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/Azure_Step4b.png?w=1100&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=6cf9db66b928d3174d3ff1abe575431b 1100w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/Azure_Step4b.png?w=1650&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=be5827cfe4daadb904e6b27243319d85 1650w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/Azure_Step4b.png?w=2500&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=885fa48808543212624710cc54df3daf 2500w" />

    7. In the **Administrator account** section, for **Authentication type**, select **SSH public key** or **Password**.

    8. Enter the credential settings, depending on the authentication type.

       <img src="https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/Azure_Step4c.png?fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=d76f2bdbce10adcd7fd94c2e971ace8b" alt="administrator account" data-og-width="1562" width="1562" data-og-height="604" height="604" data-path="img/api/Azure_Step4c.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/Azure_Step4c.png?w=280&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=2871192d25075ea4e3479a652eb1f140 280w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/Azure_Step4c.png?w=560&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=5f6d30999cde5a64039a4b7dbf81ce1b 560w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/Azure_Step4c.png?w=840&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=8fcb9a18f9ed804c30fed47585245905 840w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/Azure_Step4c.png?w=1100&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=0ce6e4402a2fc7502919a23c9e31f417 1100w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/Azure_Step4c.png?w=1650&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=e1580b551d20425d32545c87730f88e2 1650w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/Azure_Step4c.png?w=2500&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=bd783d79ce8a37a72366075fd5ec9451 2500w" />

    <Note>Do not click **Review + create** yet. You must still set up the load balancer.</Note>
  </Step>

  <Step title="Set up the load balancer">
    1. Click the **Networking** tab.

    2. In the **Networking interface** section, fill out the following fields:

       * **Virtual network**: Click **Create new**, or select an existing virtual network from the dropdown menu. To learn more, see [Quickstart: Use the Azure portal to create a virtual network](https://learn.microsoft.com/en-us/azure/virtual-network/quick-create-portal).
       * **Subnet**: Click **Manage subnet configuration**, or select a new or existing subnet from the dropdown menu. To learn more, see [Add, change, or delete a virtual network subnet](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-network-manage-subnet?tabs=azure-portal).
       * **Configure network security group**: Click **Create new**, or select an existing security group from the dropdown menu. To learn more, see [Create, change, or delete a network security group](https://learn.microsoft.com/en-us/azure/virtual-network/manage-network-security-group?tabs=network-security-group-portal).

    3. In the **Load balancing** section, fill out the following fields:

       * **Load balancing options**: Select **Azure load balancer**.
       * **Select a load balancer**: Click **Create a load balancer** and fill out the following fields in the pop-up window, or select an existing load balancer from the dropdown menu and note this name as you will need it in later steps:

         * Enter a **Load balancer name**. Note this name, as you will need it in later steps.
         * For **Type**, select **Public** or **Internal**.
         * For **Protocol**, select **TCP** or **UDP**.
         * Set both **Port** and **Backend port** to **80**.

       <img src="https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/Azure_Step5.png?fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=7e843686ab229bfd84d905a8f41d4195" alt="load balancer" data-og-width="3042" width="3042" data-og-height="1884" height="1884" data-path="img/api/Azure_Step5.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/Azure_Step5.png?w=280&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=8be78fe7320fd044bd4c9208d5172ffb 280w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/Azure_Step5.png?w=560&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=8300291aeb7945cb8f5a87daaa102170 560w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/Azure_Step5.png?w=840&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=3e925f0e53476ad26e4cba0b107e1bc3 840w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/Azure_Step5.png?w=1100&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=0bb7d0e0097077fb6543438a5428fc39 1100w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/Azure_Step5.png?w=1650&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=b73c81bc599d002965cb9c1a4e55a89e 1650w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/Azure_Step5.png?w=2500&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=615b6419b759380c3658b5580b908cbc 2500w" />

    4. Click **Create**.
  </Step>

  <Step title="Finalize and deploy">
    1. Click **Review + create**.
    2. Wait for validation.
    3. Click **Create**.

       <img src="https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/Azure_Step6.png?fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=6c24eb1cf3cb32ad7340ffe936c487a6" alt="deployment" data-og-width="3042" width="3042" data-og-height="1360" height="1360" data-path="img/api/Azure_Step6.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/Azure_Step6.png?w=280&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=60fd1a912cdedb678eb3bf9f0797fd48 280w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/Azure_Step6.png?w=560&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=3f1ca1d5f45959eff0449c15aac6b4ea 560w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/Azure_Step6.png?w=840&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=e1f1e55d7bfc02ec8fcf5fca9b440ed6 840w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/Azure_Step6.png?w=1100&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=a8496d0b651e5c3d107b0b030eb79570 1100w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/Azure_Step6.png?w=1650&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=b4ea2d4a4ec3ead4b534f0bd7999a7d7 1650w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/Azure_Step6.png?w=2500&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=5fb85b5b9f2593cee7c559f8568cfd29 2500w" />
  </Step>

  <Step title="Post-deployment: additional load balancer configuration">
    1. Go to your load balancer: in the Azure portal's **Search resources, services and docs** box, enter and then select **Load balancers**.
    2. Search for and open the new load balancer that you created earlier, or the existing load balancer that you chose earlier.
    3. Make any necessary settings updates to your new or existing load balancer, based on the recommended configurations in the [Load balancer network settings](#load-balancer-network-settings) section, later on this page.
  </Step>

  <Step title="Post-deployment: get the deployed endpoint URL">
    1. Go to your virtual machine: in the Azure portal's **Search resources, services and docs** box, enter and then select **Virtual machines**.

    2. Search for and open the new virtual machine that you created earlier, using the name that you entered earlier.

    3. On the **Overview** tab, under **Properties**, note the **Public IP address** for the **Load balancer**.

       <img src="https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/Azure_Step7.png?fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=d01980746fd32ef48d0a7ac9bc360ae9" alt="retrieve public ip" data-og-width="3042" width="3042" data-og-height="1894" height="1894" data-path="img/api/Azure_Step7.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/Azure_Step7.png?w=280&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=1be2cd3b01cd086484e311588bf1e7fe 280w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/Azure_Step7.png?w=560&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=49dc20f0ae42f96449e64a662861f449 560w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/Azure_Step7.png?w=840&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=5dc1916895b911d8993026db72a1be56 840w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/Azure_Step7.png?w=1100&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=364ed4678cc489c24b643a4e76f6c026 1100w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/Azure_Step7.png?w=1650&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=606ddbda10ff1262dba4539460f2eaa2 1650w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/Azure_Step7.png?w=2500&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=ed63b518db3c4e90947b7b573809940a 2500w" />

    4. The deployed endpoint URL is **http\://\<load-balancer-public-IP-address>/general/v0/general**. Note this endpoint URL, as you will need it later to call the Unstructured API.
  </Step>

  <Step title="Post-deployment: set API environment variables">
    Note the API environment variables in the [API environment variables](#api-environment-variables) section, later on this page. If you need to set any of these in the Docker container on the virtual machine, do the following:

    1. If the virtual machine is not already running from earlier, click the **Start** icon.

    2. After the virtual machine starts, click the **Connect** icon, and then click **Connect** from the drop-down list.

    3. Follow the on-screen directions for one of the available options to connect to the virtual machine and display a connected terminal.

    4. Stop the running container in the virtual machine, so that you can restart it later with the environment variables set: In the connected terminal, run the following command: `sudo docker container ls`.

    5. Note the `CONTAINER ID` value for the running container.

    6. Run the following command, replacing `<CONTAINER ID>` with the `CONTAINER ID` value:

       ```bash  theme={null}
       sudo docker container rm --force <CONTAINER ID>
       ```

    7. Now run the container again, setting the environment variables at the same time: Run the following command: `sudo docker image ls`.

    8. Note the `REPOSITORY` and `TAG` value for the Docker image.

    9. Run the following command, replacing `<REPOSITORY>` and `<TAG>` with the `REPOSITORY` and `TAG` values for the Docker image, and replacing
       `<VAR1>=<value1>`, `<VAR2>=<value2>` and so on with the environment variable name and value pairs:

       ```bash  theme={null}
       sudo docker run -d --restart unless-stopped \
       -p 80:5000 \
       -e <VAR1>=<value1> -e <VAR2>=<value2> -e <VAR3>=<value3> \
       <REPOSITORY>:<TAG>
       ```

    10. Verify that the environment variables were set correctly: Run the following command:

        ```bash  theme={null}
        sudo docker container ls
        ```

    11. Note the `CONTAINER ID` value for the running container.

    12. Run the following command, replacing `<CONTAINER ID>` with the `CONTAINER ID` value:

    ```bash  theme={null}
    sudo docker exec <CONTAINER ID> bash -c 'printenv'
    ```

    14. The environment variables should be in the list that appears.

    <Note>To help manage your overall costs, you should click the **Stop** icon whenever you are not using this virtual machine to call the Unstructured API.</Note>
  </Step>

  <Step title="Call the Unstructured API">
    You can now use the running virtual machine to call the Unstructured API. For example, run one of the following, setting the following environment variables to make your code more portable:

    * Set `UNSTRUCTURED_API_URL` to `http://`, followed by your load balancer's public IP address, followed by `/general/v0/general`.
    * Set `LOCAL_FILE_INPUT_DIR` to the path on your local machine to the files for the Unstructured API to process. If you do not have any input files available, you can download any of the ones from the [example-docs](https://github.com/Unstructured-IO/unstructured-ingest/tree/main/example-docs) folder in GitHub.
    * Set `LOCAL_FILE_OUTPUT_DIR` to the path on your local machine for Unstructured API to send the processed output in JSON format.
  </Step>
</Steps>

<AccordionGroup>
  <Accordion title="Ingest CLI">
    You must first [install the Unstructured Ingest CLI](/open-source/ingestion/overview#unstructured-ingest-cli).

    Because you are calling a private API and therefore do not need an Unstructured API key, you can omit the command-line option `--api-key` Or, for better code portability, it is recommended that you first set the environment variable `UNSTRUCTURED_API_KEY` to an empty string and then include the command-line option `--api-key`.

    ```bash CLI theme={null}
    unstructured-ingest \
      local \
        --input-path $LOCAL_FILE_INPUT_DIR \
        --output-dir $LOCAL_FILE_OUTPUT_DIR \
        --partition-by-api \
        --api-key $UNSTRUCTURED_API_KEY \
        --partition-endpoint $UNSTRUCTURED_API_URL \
        --strategy hi_res \
        --additional-partition-args="{\"split_pdf_page\":\"true\", \"split_pdf_allow_failed\":\"true\", \"split_pdf_concurrency_level\": 15}"
    ```
  </Accordion>

  <Accordion title="Ingest Python library">
    You must first [install the Unstructured Ingest Python library](/open-source/ingestion/python-ingest).

    Because you are calling a private API and therefore do not need an Unstructured API key, you can omit the parameter `api_key`. Or, for better code portability, it is recommended that you first set the environment variable `UNSTRUCTURED_API_KEY` to an empty string and then include the parameter `api_key`.

    ```python Python Ingest theme={null}
    import os

    from unstructured_ingest.pipeline.pipeline import Pipeline
    from unstructured_ingest.interfaces import ProcessorConfig
    from unstructured_ingest.processes.connectors.local import (
        LocalIndexerConfig,
        LocalDownloaderConfig,
        LocalConnectionConfig,
        LocalUploaderConfig
    )
    from unstructured_ingest.processes.partitioner import PartitionerConfig

    if __name__ == "__main__":
        Pipeline.from_configs(
            context=ProcessorConfig(),
            indexer_config=LocalIndexerConfig(input_path=os.getenv("LOCAL_FILE_INPUT_DIR")),
            downloader_config=LocalDownloaderConfig(),
            source_connection_config=LocalConnectionConfig(),
            partitioner_config=PartitionerConfig(
                partition_by_api=True,
                api_key=os.getenv("UNSTRUCTURED_API_KEY"),
                partition_endpoint=os.getenv("UNSTRUCTURED_API_URL"),
                strategy="hi_res",
                additional_partition_args={
                    "split_pdf_page": True,
                    "split_pdf_allow_failed": True,
                    "split_pdf_concurrency_level": 15
                }
            ),
            uploader_config=LocalUploaderConfig(output_dir=os.getenv("LOCAL_FILE_OUTPUT_DIR"))
        ).run()
    ```
  </Accordion>
</AccordionGroup>

<Note>To help manage your overall costs, you should stop running the associated virtual machine whenever you are not using it to call the Unstructured API.</Note>

## Load balancer network settings

Unstructured recommends the following load balancer settings, which you should set on your deployment's load balancer soon after you finalize and deploy it.

On the load balancer's **Overview** tab in the Azure portal:

* **SKU**: **Standard**

On the load balancer's **Settings** tab in the Azure portal:

* **Frontend IP configuration**: Private IP

* **Backend pools**: VMSS

* **Health probes**:

  * **Protocol**: **HTTP**, or **HTTPS** (this requires setting up a reverse proxy on the VMSS set to do TLS termination)
  * **Port**: `80` or `443` (this can be any port that the backend VMs are listening on)
  * **Path**: `/healthcheck`
  * **Interval (seconds)**: `5`

* **Load balancing rules**:

  * **Protocol**: **TCP**
  * **Port**: `443` for HTTPS, or `80` for HTTP
  * **Backend port**: `443` for HTTPS, or `80` for HTTP
  * **Idle timeout (minutes)**: `60`
  * **Enable TCP Reset** box: Checked

* **Inbound NAT rules**:

  * **Frontend Port**: `443` for HTTPS, or `80` for HTTP
  * **Backend port**: `443` for HTTPS, or `80` for HTTP
  * **Protocol**: **TCP**
  * **Enable TCP Reset** box: Checked
  * **Idle timeout (minutes)**: `60`

## API environment variables

Unstructured supports the following environment variables, which you can set in the Docker image on the virtual machine, as needed:

* `ALLOW_ORIGINS`: CORS-allowed origins.
* `UNSTRUCTURED_ALLOWED_MIMETYPE`: The list of allowed MIME types, if you want to limit the file types that can be processed.
* `UNSTRUCTURED_API_KEY`: The default Unstructured API key to use.
* `UNSTRUCTURED_MEMORY_FREE_MINIMUM_MB`: The minimum amount of free memory in MB to allow for processing a file. If this memory is too low, the server will return a `503` error.
* `UNSTRUCTURED_PDF_HI_RES_MAX_PAGES`: The maximum number of pages in a PDF file that the Unstructured API will not reject, if the `hi_res` strategy is used. The default is `300`.
* `UNSTRUCTURED_REDIRECT_ROOT_URL`: If this is set, redirect a `GET` request to the Unstructured API to use this URL instead.
