# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/server-installation/data-center-edition/on-kubernetes-or-openshift/setting-up-disaster-recovery/test-failover-scenarios.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/server-installation/data-center-edition/on-kubernetes-or-openshift/setting-up-disaster-recovery/test-failover-scenarios.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/server-installation/data-center-edition/on-kubernetes-or-openshift/setting-up-disaster-recovery/test-failover-scenarios.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/server-installation/data-center-edition/on-kubernetes-or-openshift/setting-up-disaster-recovery/test-failover-scenarios.md

# Source: https://docs.sonarsource.com/sonarqube-server/server-installation/data-center-edition/on-kubernetes-or-openshift/setting-up-disaster-recovery/test-failover-scenarios.md

# Step 4: Test failover scenarios

The disaster scenarios described below are based on a [architecture-example](https://docs.sonarsource.com/sonarqube-server/server-installation/data-center-edition/on-kubernetes-or-openshift/setting-up-disaster-recovery/architecture-example "mention").

### Regional failure of AKS <a href="#regional-failover-of-aks" id="regional-failover-of-aks"></a>

1. Stop the primary AKS cluster and go to Azure portal's **Home** > **Kubernetes services**.
2. Select the primary cluster and select **Stop**.
3. Wait until the cluster's **Power state** changes to **Stopped** and the **Cluster operation status** changes to **Succeeded**.

<div align="left"><figure><img src="https://content.gitbook.com/content/LWhbesChsC4Yd1BbhHhS/blobs/5mNVyZ5VV06YFutSukwf/sonarqube-dce-disaster-recovery-failover-scenario-aks-regional-failure.png" alt="Set Power state to Stopped and Cluster operation status to Succeeded"><figcaption></figcaption></figure></div>

4. Power on the Replica cluster and wait for the cluster's **Power state** to change to **Started** and **Cluster operation status** to **Succeeded**.
5. Once the cluster starts, perform a forced Elasticsearch reindexing. The [reindexing](https://docs.sonarsource.com/sonarqube-server/server-update-and-maintenance/maintenance/reindexing "mention") page has a special article about [#forcing-es-reindex](https://docs.sonarsource.com/sonarqube-server/server-update-and-maintenance/maintenance/reindexing#forcing-es-reindex "mention").
6. Using the Azure CLI, make sure the correct cluster credentials are set to your Helm and kubectl commands context with the command below.

```
az aks get-credentials --resource-group <YOUR_RESOURCE_GROUP> --name <YOUR_REPLICA_CLUSTER_NAME>
```

7. Run the following command to reduce the replica count of the search nodes from 3 to 0. The monitoring passcode is required for the helm upgrade operation.

```
helm upgrade sonarqube-dce sonarqube/sonarqube-dce  --set searchNodes.replicaCount=0,monitoringPasscode="mypassword" -n sonarqube-dce
```

8. If you are using any PVC with SonarQube deployment, delete the PVC, which should delete any PV, assuming the reclaim policy is Delete. Otherwise, manually delete/remove any PV. Typically, there is one PVC for each search node. Repeat this step for all the PVCs associated with the search nodes.

```
kubectl delete pvc 
sonarqube-dce-sonarqube-dce-sonarqube-dce-sonarqube-dce-search-0 -n sonarqube-dce
```

9. Run the following commands to bring the replica count back to 3 for the search nodes.

```
export JWT_SECRET=$(echo -n "your_secret" | openssl dgst -sha256 -hmac "your_key" -binary | base64)
helm upgrade sonarqube-dce sonarqube/sonarqube-dce  --set searchNodes.replicaCount=3,monitoringPasscode="mypassword",applicationNodes.jwtSecret=$JWT_SECRET -n sonarqube-dce
```

10. Login to your SonarQube Server instance using the Azure FrontDoor endpoint to confirm the failover was successful.

### Regional failure of Azure Database for PostgreSQL flexible server <a href="#regional-failure-of-azure-database" id="regional-failure-of-azure-database"></a>

1. On the Azure portal home page, go to **Azure Database for PostgreSQL flexible servers**.
2. Select the primary SonarQube database from the list.
3. On the database home page, go to **Settings** > **High availability.**
4. Select **Planned failover** or **Forced failover**. For less downtime, select **Planned failover**.

<div align="left"><figure><img src="https://content.gitbook.com/content/LWhbesChsC4Yd1BbhHhS/blobs/AHMwal1y9shgLE8oGKBj/sonarqube-dce-disaster-recovery-failover-scenario-azure-database-regional-failure.png" alt="Use either the Forced failover or Planned failover tab"><figcaption></figcaption></figure></div>

5. Once the failover is complete, open your SonarQube server instance and check the integrity of your data.

### Related pages

* [architecture-example](https://docs.sonarsource.com/sonarqube-server/server-installation/data-center-edition/on-kubernetes-or-openshift/setting-up-disaster-recovery/architecture-example "mention")
* [deploy-databases](https://docs.sonarsource.com/sonarqube-server/server-installation/data-center-edition/on-kubernetes-or-openshift/setting-up-disaster-recovery/deploy-databases "mention")
* [set-up-clusters-on-aks](https://docs.sonarsource.com/sonarqube-server/server-installation/data-center-edition/on-kubernetes-or-openshift/setting-up-disaster-recovery/set-up-clusters-on-aks "mention")
* [configure-azure-front-door](https://docs.sonarsource.com/sonarqube-server/server-installation/data-center-edition/on-kubernetes-or-openshift/setting-up-disaster-recovery/configure-azure-front-door "mention")
