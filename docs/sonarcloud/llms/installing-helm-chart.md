# Source: https://docs.sonarsource.com/sonarqube-community-build/server-installation/on-kubernetes-or-openshift/installing-helm-chart.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/setup-and-upgrade/deploy-on-kubernetes/server/installing-helm-chart.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/setup-and-upgrade/deploy-on-kubernetes/server/installing-helm-chart.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/setup-and-update/deploy-on-kubernetes/server/installing-helm-chart.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/server-installation/on-kubernetes-or-openshift/installing-helm-chart.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/server-installation/on-kubernetes-or-openshift/installing-helm-chart.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/setup-and-upgrade/deploy-on-kubernetes/server/installing-helm-chart.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/server-installation/on-kubernetes-or-openshift/installing-helm-chart.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/server-installation/on-kubernetes-or-openshift/installing-helm-chart.md

# Source: https://docs.sonarsource.com/sonarqube-server/server-installation/on-kubernetes-or-openshift/installing-helm-chart.md

# Installing Helm chart

Once you have customized the Helm chart, you can install it. You can also overwrite Helm chart parameters directly in the installation command (see OpenShift example below).

### General installation command <a href="#general-command" id="general-command"></a>

Use the following command to install the latest SonarQube Server Helm chart:

```sh
helm repo add sonarqube https://SonarSource.github.io/helm-chart-sonarqube
helm repo update
kubectl create namespace sonarqube
export MONITORING_PASSCODE="yourPasscode"
helm upgrade --install -n sonarqube sonarqube sonarqube/sonarqube --set edition=developer,monitoringPasscode=$MONITORING_PASSCODE
```

{% hint style="info" %}

* You must explicitly set the `edition` parameter to either `developer` or `enterprise`.
* The parameters after `--set` can also be defined in the `values.yaml` file. See [customizing-helm-chart](https://docs.sonarsource.com/sonarqube-server/server-installation/on-kubernetes-or-openshift/customizing-helm-chart "mention").
* If you want to deploy the SonarQube Server LTA version, you should install the LTA Helm chart, see the [Helm chart documentation](https://artifacthub.io/packages/helm/sonarqube/sonarqube).
* The monitoring Passcode is required for the helm upgrade operation. See [set-up-monitoring](https://docs.sonarsource.com/sonarqube-server/server-installation/on-kubernetes-or-openshift/set-up-monitoring "mention") for a better way to store the monitoring passcode used to authenticate to the Web API.
  {% endhint %}

### Example: installing on OpenShift <a href="#openshift-test" id="openshift-test"></a>

The following command enables OpenShift.

```
helm repo add sonarqube https://SonarSource.github.io/helm-chart-sonarqube
helm repo update
kubectl create namespace sonarqube
export MONITORING_PASSCODE="yourPasscode"
export EDITION="developer" # Choose your edition
export JDBC_URL="jdbc:postgresql://myPostgres/myDatabase"
export JDBC_USERNAME="jdbc-username"
export JDBC_PASSWORD_SECRET_NAME="jdbc-secret"
export JDBC_PASSWORD_SECRET_KEY="jdbc-password"
helm upgrade --install -n sonarqube sonarqube sonarqube/sonarqube \
  --set edition=$EDITION \
  --set OpenShift.enabled=true \
  --set monitoringPasscode=$MONITORING_PASSCODE \
  --set jdbcOverwrite.jdbcUrl=$JDBC_URL \
  --set jdbcOverwrite.jdbcUsername=$JDBC_USERNAME \
  --set jdbcOverwrite.jdbcSecretName=$JDBC_PASSWORD_SECRET_NAME \
  --set jdbcOverwrite.jdbcSecretPasswordKey=$JDBC_PASSWORD_SECRET_KEY
```

#### Setting up an external database for testing

The chart requires an external database. If you want to perform a quick test, install a [PostgreSQL chart](https://artifacthub.io/packages/helm/bitnami/postgresql) on your cluster. For more information and settings, refer to the[ chart documentation](https://artifacthub.io/packages/helm/sonarqube/sonarqube).

After installing the database, set the following values accordingly: `jdbcOverwrite.jdbcUrl`, `jdbcOverwrite.jdbcUsername`, `jdbcOverwrite.jdbcSecretName`, and `jdbcOverwrite.jdbcSecretPasswordKey`.

### Related pages <a href="#related-pages" id="related-pages"></a>

* [installation-overview](https://docs.sonarsource.com/sonarqube-server/server-installation/on-kubernetes-or-openshift/installation-overview "mention")
* [before-you-start](https://docs.sonarsource.com/sonarqube-server/server-installation/on-kubernetes-or-openshift/before-you-start "mention")
* [customizing-helm-chart](https://docs.sonarsource.com/sonarqube-server/server-installation/on-kubernetes-or-openshift/customizing-helm-chart "mention")
* [set-up-monitoring](https://docs.sonarsource.com/sonarqube-server/server-installation/on-kubernetes-or-openshift/set-up-monitoring "mention")
* Installing Data Center Edition on Kubernetes: [on-kubernetes-or-openshift](https://docs.sonarsource.com/sonarqube-server/server-installation/data-center-edition/on-kubernetes-or-openshift "mention")
