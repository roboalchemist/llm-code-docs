# Source: https://docs.sonarsource.com/sonarqube-community-build/server-update-and-maintenance/maintenance/reindexing.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.1/instance-administration/reindexing.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.2/instance-administration/reindexing.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.3/instance-administration/reindexing.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.4/instance-administration/reindexing.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.5/instance-administration/reindexing.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.6/instance-administration/reindexing.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/server-upgrade-and-maintenance/maintenance/reindexing.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/server-upgrade-and-maintenance/maintenance/reindexing.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/server-update-and-maintenance/maintenance/reindexing.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/server-update-and-maintenance/maintenance/reindexing.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/server-update-and-maintenance/maintenance/reindexing.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/server-update-and-maintenance/maintenance/reindexing.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/server-update-and-maintenance/maintenance/reindexing.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/server-update-and-maintenance/maintenance/reindexing.md

# Source: https://docs.sonarsource.com/sonarqube-server/server-update-and-maintenance/maintenance/reindexing.md

# Reindexing

### Project, application, and portfolio availability <a href="#rebuild-of-elasticsearch-indexes" id="rebuild-of-elasticsearch-indexes"></a>

Most features are available during reindexing (for example, you can already analyze your projects), but some only become available when the process is complete:

* Project issues and security hotspots: Available, but some filters and the ability to add tags become available only when reindexing is complete.
* Security reports: Available when reindexing is complete.
* Applications and portfolios: Issues, security hotspots, and security reports become available once all their associated projects are reindexed.
* The global Issues page is unavailable until all projects are reindexed.

SonarQube Server uses analysis dates to determine which projects to prioritize during reindexing. Your projects with the most recent analysis dates are the first to become fully available in the UI.

Administrators can track the full reindexing progress:

* Within the banner displayed in SonarQube Server.
* In the [background-tasks](https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/background-tasks "mention").

{% hint style="info" %}
If a project fails to reindex, see **Reindexing a single project** below.
{% endhint %}

### Running analyses during reindexing <a href="#running-analyses-during-reindexing" id="running-analyses-during-reindexing"></a>

Reindexing starts once SonarQube Server is up and running. You can run analyses on your projects on the CI side while indexes are being rebuilt. The processing of analysis results takes priority over reindexing tasks, so your SonarQube Server instance is effectively operational.

Administrators can check the progress of these analyses in **Administration** > **Projects** > **Background tasks**.

### Quality gate timeout <a href="#quality-gate-timeout" id="quality-gate-timeout"></a>

When calculating the quality gate of a project that is actively being indexed, SonarQube Server will finish indexing to allow computation to complete before returning quality gate status. If the indexing does not finish by the Quality Gate timeout setting, then the Quality Gate will time out.

### Forcing an Elasticsearch reindex <a href="#forcing-es-reindex" id="forcing-es-reindex"></a>

You can trigger a full Elasticsearch reindex. During the reindex, SonarQube Server will detect out-of-sync indices and correct them.

{% hint style="warning" %}
Full Elasticsearch reindex can be quite lengthy depending on the size of your instance.
{% endhint %}

#### ZIP file deployment <a href="#zip-file-deployment" id="zip-file-deployment"></a>

<details>

<summary>In SonarQube Server (Developer Edition, Enterprise Edition)</summary>

1. Stop the server.
2. Remove the contents of the `<sonarqubeHome>/data/es8` directory where `<sonarqubeHome>` is the location where the SonarQube distribution has been unzipped.
3. Start the server.

</details>

<details>

<summary>In SonarQube Server Data Center Edition</summary>

1. Stop the cluster as follows: stop first the application nodes and then the search nodes.
2. On each search node, remove the contents of the `<sonarqubeHome>/data/es8` directory where `<sonarqubeHome>` is the location where the SonarQube distribution has been unzipped.
3. Start your cluster as follows: start first the search nodes and then the application nodes.

</details>

#### Docker deployment <a href="#docker-deployment" id="docker-deployment"></a>

<details>

<summary>In SonarQube Server (Developer Edition, Enterprise Edition)</summary>

1. Stop the server.
2. Remove the contents of the `<sonarqubeHome>/data/es8` directory where \<sonarqubeHome> is the installation directory of SonarQube within your container. This path is stored in the `SONARQUBE_HOME` environment variable.
3. Start the server.

</details>

<details>

<summary>In SonarQube Server Data Center Edition</summary>

1. Stop the cluster as follows: stop first the application nodes and then the search nodes.
2. On each search node, remove the contents of the `<sonarqubeHome>/data/es8` directory where `<sonarqubeHome>` is the installation directory of SonarQube within your container. This path is stored in the `SONARQUBE_HOME` environment variable.
3. Start your cluster as follows: start first the search nodes and then the application nodes.

</details>

#### Helm chart deployment <a href="#helm-chart-deployment" id="helm-chart-deployment"></a>

<details>

<summary>In SonarQube Server (Developer Edition, Enterprise Edition)</summary>

If `persistence.enabled=false`, an ES reindex is not necessary since no ES data will have persisted.

If `persistence.enabled=true`, proceed to perform ES reindex as follows:

1. Scale down the replica count from 1 to 0. For example, if you deployed via Helm:\
   `helm upgrade -n sonarqube sonarqube sonarqube/sonarqube --set replicaCount=0`
2. If you are using any PVC with SonarQube deployment, delete the PVC, which should delete any PV assuming the reclaim policy is *Delete*. Otherwise, manually delete/remove any PV. For example:\
   `kubectl delete pvc my-sonarqube-pvc -n sonarqube`
3. Scale up the replica count of the deployment from 0 to 1.
4. Verify that SonarQube starts up without issue.

</details>

<details>

<summary>In SonarQube Server Data Center Edition</summary>

If `searchNodes.persistence.enabled=false`, an ES reindex is not necessary since no ES data will have persisted.

If `searchNodes.persistence.enabled=true`, proceed to perform an ES reindex, proceed as follows:

1. Scale down the replica count of the search pods from 3 to 0. For example, if you deployed via Helm:\
   `helm upgrade -n sonarqube-dce sonarqube sonarqube/sonarqube-dce --set searchNodes.replicaCount=0`
2. If you are using any PVC with SonarQube deployment, delete the PVC, which should delete any PV assuming the reclaim policy is *Delete*. Otherwise, manually delete/remove any PV. For example:\
   `kubectl delete pvc my-sonarqube-pvc -n sonarqube-dce`
3. Scale up the replica count of the deployment from 0 to 3.
4. Verify that SonarQube starts up without issue.

</details>

### Reindexing a single project <a href="#reindexing-single-project" id="reindexing-single-project"></a>

You may have to reindex a project if it shows inconsistent data or fails to reindex after an instance version update or during a forced ElasticSearch reindex. To perform this procedure, you need the Administer System permission.

To reindex a single project:

* Use the SonarQube Server Web API [api/issues/reindex](https://next.sonarqube.com/sonarqube/web_api/api/issues?query=reindex).
