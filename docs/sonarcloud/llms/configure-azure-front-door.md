# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/server-installation/data-center-edition/on-kubernetes-or-openshift/setting-up-disaster-recovery/configure-azure-front-door.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/server-installation/data-center-edition/on-kubernetes-or-openshift/setting-up-disaster-recovery/configure-azure-front-door.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/server-installation/data-center-edition/on-kubernetes-or-openshift/setting-up-disaster-recovery/configure-azure-front-door.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/server-installation/data-center-edition/on-kubernetes-or-openshift/setting-up-disaster-recovery/configure-azure-front-door.md

# Source: https://docs.sonarsource.com/sonarqube-server/server-installation/data-center-edition/on-kubernetes-or-openshift/setting-up-disaster-recovery/configure-azure-front-door.md

# Step 3: Configure the Azure Front Door

The setup instructions are based on a [architecture-example](https://docs.sonarsource.com/sonarqube-server/server-installation/data-center-edition/on-kubernetes-or-openshift/setting-up-disaster-recovery/architecture-example "mention").

### Step 1: Create an Azure Front Door <a href="#create-azure-front-door" id="create-azure-front-door"></a>

Create an Azure Front Door as follows (see also the [Azure documentation](https://learn.microsoft.com/en-us/azure/frontdoor/create-front-door-portal?tabs=quick)):

1\. In the Azure portal, create a new Azure Front Door by using the **Quick create** option. The **Create a Front Door** **profile** page opens.

2\. In **Project details**, select your subscription and resource group.

3\. In **Profile details**, enter your profile name

4\. In **Endpoint settings:**

* In **Endpoint name**, enter a name for your endpoint. This is the domain where users will access your SonarQube Server instance. Azure creates a \*.[azurefd.net](http://azurefd.net/) domain for your endpoint by default. You can modify this setting to use your own domain on the Front Door settings.
* In **Origin type**, select **Custom**.
* In **Origin host name**, enter the FQDN of your primary cluster Ingress. You’ll add the Replica origin once the Front Door is created along with the origin group.
* Leave **Caching** and **WAF policy** with the default settings.

<div align="left"><figure><img src="https://content.gitbook.com/content/LWhbesChsC4Yd1BbhHhS/blobs/bGSafiM7kGyhAFQuVmtp/sonarqube-dce-disaster-recovery-azure-front-door-endpoint-settings-.png" alt="Set the endpoint parameters by selecting Custom in Origin type and entering the FQDN of your primary cluster ingress in Origin host name"><figcaption></figcaption></figure></div>

5. Select the **Review + create** button.
6. Go back to the overview page and select the newly created Front Door.
7. Go to **Origin Groups** > **Origin group name**

<div align="left"><figure><img src="https://content.gitbook.com/content/LWhbesChsC4Yd1BbhHhS/blobs/Z2yIo5WoOsvsbpFFekZO/sonarqube-dce-disaster-recovery-azure-database-replication-origin-group.png" alt="The origin group is assigned by default the default-origin-group name"><figcaption></figcaption></figure></div>

8. Select your origin group from the list (the origin group is automatically created with default name `default-origin-group`). The **Update origin group** page opens.
9. Select **Add an origin**.

<div align="left"><figure><img src="https://content.gitbook.com/content/LWhbesChsC4Yd1BbhHhS/blobs/1xz46Lr5t7ZFWLrdMWBv/sonarqube-dce-disaster-recovery-azure-front-door-add-origin.png" alt="Select Add an origin to create the Replica origin"><figcaption></figcaption></figure></div>

10. Set the parameters of the new origin:
    * In **Name**, enter a name for the replica origin.
    * In **Origin type**, select **Custom**.
    * In **Host name**, enter the DNS name of your replica cluster Ingress.
    * Leave **Origin host header** blank.
    * In **Certificate subject name validation**, select **Enable the validation**.
    * Leave **HTTP port** and **HTTPS port** with the default values.
    * In **Priority**, enter **2**.
    * Leave **Weight** and **Status** with the default values.

<div align="left"><figure><img src="https://content.gitbook.com/content/LWhbesChsC4Yd1BbhHhS/blobs/WBjHDEJ1rBNEWEeTT1qk/sonarqube-dce-disaster-recovery-azure-front-door-origin-settings.png" alt="Set the priority of the replica origin to 2"><figcaption></figcaption></figure></div>

### Step 2: Configure an alert rule for the origin group <a href="#configure-alert-rule" id="configure-alert-rule"></a>

You can set up an alert for your origin group that triggers whenever your origin health goes under a specific threshold. The alert can optionally send an email to the SonarQube Server Administrator or start an automation runbook to perform additional actions, if required.

To configure an alert rule for the origin group:

1. Select your Front Door.
2. In **Monitoring**, select **Alerts**.
3. Select **Create Alert rule**.
4. In **Signal name**, select **Origin Health Percentage**.
5. In **Aggregation type**, select **Average**.
6. In **Threshold**, select **99%**.
7. In **Split by dimensions :**
   1. In **Dimension name**, select **Origin.**
   2. In **Operator**, select **=**.
   3. Select your primary SonarQube **Origin Group** as **Dimension values**.
8. In **When to evaluate**, select the values based on your requirements.
9. Select the **Next:Actions** button.
10. In **Select actions**, select **Use action groups**.
11. In **Action groups**, select **Select action groups** and then **Create action group**.
12. Select the correct subscription and resource group and give a name of your choice for the action group name and display name.
13. Select the **Next:Notifications** button.
14. Select a notification type. At a minimum, select **Email/SMS message/Push/Voice** to receive an email whenever the alert is triggered.
15. Optionally, select **Actions** and select an automation runbook with a script to power on the replica cluster. To create an automation runbook, see below.

### Creating an automation runbook <a href="#creating-automation-runbook" id="creating-automation-runbook"></a>

This section explains how to create an automation runbook triggered by an alert rule created for the Front Door origin containing your primary cluster. This runbook powers on the replica cluster in case of an outage of the primary cluster.

{% hint style="warning" %}
The following steps are listed in this guide as a reference only. Sonar recommends a manual power-on of the replica cluster in the event of a disaster, as this is a sensitive operation that could impact your RTO goals.
{% endhint %}

<details>

<summary>Step 1: Create an automation account</summary>

Proceed as follows (see also the [Azure documentation](https://learn.microsoft.com/en-us/azure/automation/quickstarts/create-azure-automation-account-portal)):

1. In your Azure portal, navigate to **Automation Accounts** and select **Create**.
2. Select your subscription and resource group.
3. In **Instance Details**, enter a name and select a region for your Automation Account.
4. Select the **Advanced** tab to select the managed identity option. This identity is needed for the Runbooks associated with this account to connect and run operations on your clusters. You can either use a System-assigned or a User-assigned identity.\
   If using an identity option, make sure you set the correct Azure role permissions to your SonarQube clusters.
5. Select the **Review + Create** button.

</details>

<details>

<summary>Step 2: Create a runbook</summary>

1. Go to your automation account.
2. In **Process Automation**, select **Runbooks** and **Create a runbook**.
3. Enter the runbook name.
4. In **Runbook type**, select **PowerShell**.
5. In **Runtime version**, select **7.2**.
6. Use the sample PowerShell script below to power on the replica cluster.

```powershell
# This script starts an Azure Kubernetes Service (AKS) cluster using the Azure PowerShell module.
#variables
param(
   [Parameter(Mandatory = $true)]
   [string]$PrimaryClusterName,
   [Parameter(Mandatory = $true)]
   [string]$ReplicaClusterName,
   [Parameter(Mandatory = $true)]
   [string]$SubscriptionId,
   [Parameter(Mandatory = $true)]
   [string]$ManagedIdentityClientId,
   [Parameter(Mandatory = $true)]
   [string]$ResourceGroupName
)
#connect to Azure using managed identity
Connect-AzAccount -Identity -AccountId $ManagedIdentityClientId

#check the status of the AKS Primary cluster
$primaryCluster = Get-AzAksCluster -ResourceGroupName $ResourceGroupName -Name $PrimaryClusterName -SubscriptionId $SubscriptionId
if ($primaryCluster.ProvisioningState -ne "Succeeded" -or $primaryCluster.PowerState.Code -ne "Running") {
   Start-AzAksCluster -ResourceGroupName $ResourceGroupName -Name $ReplicaClusterName -SubscriptionId $SubscriptionId
}
else {
   Write-Output "Primary AKS cluster is still running. No action taken."
}
```

</details>

### Related pages

* [architecture-example](https://docs.sonarsource.com/sonarqube-server/server-installation/data-center-edition/on-kubernetes-or-openshift/setting-up-disaster-recovery/architecture-example "mention")
* [deploy-databases](https://docs.sonarsource.com/sonarqube-server/server-installation/data-center-edition/on-kubernetes-or-openshift/setting-up-disaster-recovery/deploy-databases "mention")
* [set-up-clusters-on-aks](https://docs.sonarsource.com/sonarqube-server/server-installation/data-center-edition/on-kubernetes-or-openshift/setting-up-disaster-recovery/set-up-clusters-on-aks "mention")
* [test-failover-scenarios](https://docs.sonarsource.com/sonarqube-server/server-installation/data-center-edition/on-kubernetes-or-openshift/setting-up-disaster-recovery/test-failover-scenarios "mention")
