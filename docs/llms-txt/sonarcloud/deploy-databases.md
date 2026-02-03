# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/server-installation/data-center-edition/on-kubernetes-or-openshift/setting-up-disaster-recovery/deploy-databases.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/server-installation/data-center-edition/on-kubernetes-or-openshift/setting-up-disaster-recovery/deploy-databases.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/server-installation/data-center-edition/on-kubernetes-or-openshift/setting-up-disaster-recovery/deploy-databases.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/server-installation/data-center-edition/on-kubernetes-or-openshift/setting-up-disaster-recovery/deploy-databases.md

# Source: https://docs.sonarsource.com/sonarqube-server/server-installation/data-center-edition/on-kubernetes-or-openshift/setting-up-disaster-recovery/deploy-databases.md

# Step 1: Deploy the primary and replica databases

The setup instructions are based on a [architecture-example](https://docs.sonarsource.com/sonarqube-server/server-installation/data-center-edition/on-kubernetes-or-openshift/setting-up-disaster-recovery/architecture-example "mention").

Deploy the primary and replica PostgreSQL databases on Azure as follows:

1. On the Azure Database for PostgreSQL flexible server creation page of your primary database, select your subscription and resource group.
2. In **Server details** > **Compute + storage**, select **Configure server**. A new pane opens.

<div align="left"><figure><img src="https://content.gitbook.com/content/LWhbesChsC4Yd1BbhHhS/blobs/F1ubh0opIGyxMsgnEwFe/sonarqube-dce-disaster-recovery-configure-azure-database.png" alt="In the Server details of your primary Azure database, select Configure server"><figcaption></figcaption></figure></div>

3. In **Backups**, enable the **Geo-redundancy**.

<div align="left"><figure><img src="https://content.gitbook.com/content/LWhbesChsC4Yd1BbhHhS/blobs/VwSFgZnvuORLxGqH4mwy/sonarqube-dce-disaster-recovery-azure%20database-enable-geo-redundancy.png" alt="Enable the geo-redundancy by selecting the Recover from regional outage or disaster option"><figcaption></figcaption></figure></div>

4. Once the primary database has been deployed, create the replica database. To do so, go to the primary database resource page > **Settings >** **Replication >** **Create replica**. Ensure that you select a different **Availability zone** than for the primary database.

<div align="left"><figure><img src="https://content.gitbook.com/content/LWhbesChsC4Yd1BbhHhS/blobs/IV5adoYmgosTkSr0dpBu/sonarqube-dce-disaster-recovery-azure-replica-database-availability-zone.png" alt="Create the replica database and set a different Availability zone that for the primary database"><figcaption></figcaption></figure></div>

5. Create virtual endpoints: go to **Database Settings** > **Replication** > **Virtual endpoints**.

<figure><img src="https://content.gitbook.com/content/LWhbesChsC4Yd1BbhHhS/blobs/vnLsiwK3nTYkZmtCK067/sonarqube-dce-disaster-recovery-azure-front-door-endpoints-command.png" alt="Creating virtual endpoints"><figcaption></figcaption></figure>

The following pane is displayed.

<div align="left"><figure><img src="https://content.gitbook.com/content/LWhbesChsC4Yd1BbhHhS/blobs/nr1K0e1BQvYOvNyVL16M/sonarqube-dce-disaster-recovery-azure-front-door-create-virtual-endpoints.png" alt="Information displayed in a pane"><figcaption></figcaption></figure></div>

### Related pages <a href="#related-pages" id="related-pages"></a>

* [architecture-example](https://docs.sonarsource.com/sonarqube-server/server-installation/data-center-edition/on-kubernetes-or-openshift/setting-up-disaster-recovery/architecture-example "mention")
* [set-up-clusters-on-aks](https://docs.sonarsource.com/sonarqube-server/server-installation/data-center-edition/on-kubernetes-or-openshift/setting-up-disaster-recovery/set-up-clusters-on-aks "mention")
* [configure-azure-front-door](https://docs.sonarsource.com/sonarqube-server/server-installation/data-center-edition/on-kubernetes-or-openshift/setting-up-disaster-recovery/configure-azure-front-door "mention")
* [test-failover-scenarios](https://docs.sonarsource.com/sonarqube-server/server-installation/data-center-edition/on-kubernetes-or-openshift/setting-up-disaster-recovery/test-failover-scenarios "mention")
