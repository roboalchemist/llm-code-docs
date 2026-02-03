# Source: https://docs.sonarsource.com/sonarqube-server/10.8/setup-and-upgrade/deploy-on-kubernetes/dce/installing-from-helm-repo.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/setup-and-update/deploy-on-kubernetes/dce/installing-from-helm-repo.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/server-installation/data-center-edition/on-kubernetes-or-openshift/installing-from-helm-repo.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/server-installation/data-center-edition/on-kubernetes-or-openshift/installing-from-helm-repo.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/setup-and-upgrade/deploy-on-kubernetes/dce/installing-from-helm-repo.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/server-installation/data-center-edition/on-kubernetes-or-openshift/installing-from-helm-repo.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/server-installation/data-center-edition/on-kubernetes-or-openshift/installing-from-helm-repo.md

# Source: https://docs.sonarsource.com/sonarqube-server/server-installation/data-center-edition/on-kubernetes-or-openshift/installing-from-helm-repo.md

# Installing the DCE Helm chart

Once you have customized the Helm chart, you can install it via the command line from the Helm repository.

{% hint style="info" %}
You can also overwrite Helm chart parameters directly in the installation command.
{% endhint %}

### General installation command

Use the following command to install the latest SonarQube Server Helm chart:

```
helm repo add sonarqube https://SonarSource.github.io/helm-chart-sonarqube
helm repo update
kubectl create namespace sonarqube-dce
export JWT_SECRET=$(echo -n "your_secret" | openssl dgst -sha256 -hmac "your_key" -binary | base64)
export MONITORING_PASSCODE="yourPasscode"
export JDBC_URL="jdbc:postgresql://myPostgres/myDatabase"
export JDBC_USERNAME="sonar"
export JDBC_PASSWORD_SECRET_NAME="jdbc-secret"
export JDBC_PASSWORD_SECRET_KEY="jdbc-password"
helm upgrade --install -n sonarqube-dce sonarqube sonarqube/sonarqube-dce --set applicationNodes.jwtSecret=$JWT_SECRET,monitoringPasscode=$MONITORING_PASSCODE,jdbcOverwrite.jdbcUrl=$JDBC_URL,jdbcOverwrite.jdbcUsername=$JDBC_USERNAME,jdbcOverwrite.jdbcSecretName=$JDBC_PASSWORD_SECRET_NAME,jdbcOverwrite.jdbcSecretPasswordKey=$JDBC_PASSWORD_SECRET_KEY
```

* You must set the applicationNodes.jwtSecret value with a HS256 key encoded with base64.
* The chart requires an external database. If you want to perform a quick testing, you might want to follow the steps outlined [here](https://github.com/SonarSource/helm-chart-sonarqube/tree/master/charts/sonarqube-dce#setting-up-an-external-database-for-quick-testing). You will be required to set the following values accordingly: `jdbcOverwrite.jdbcUrl`, `jdbcOverwrite.jdbcUsername`, `jdbcOverwrite.jdbcSecretName`, and `jdbcOverwrite.jdbcSecretPasswordKey`.
* The parameters after --set can also be defined in the values.yaml file. See [customizing-helm-chart](https://docs.sonarsource.com/sonarqube-server/server-installation/data-center-edition/on-kubernetes-or-openshift/customizing-helm-chart "mention") for more information.
* If you want to deploy the SonarQube Server LTA version, you should install the LTA Helm chart, see the [Helm chart documentation](https://artifacthub.io/packages/helm/sonarqube/sonarqube-dce).
* The monitoring Passcode is required for the helm upgrade operation. See [set-up-monitoring](https://docs.sonarsource.com/sonarqube-server/server-installation/on-kubernetes-or-openshift/set-up-monitoring "mention") for a better way to store the monitoring passcode used to authenticate to the Web API.

### Example: installing on OpenShift

The following command enables OpenShift.

```
helm repo add sonarqube https://SonarSource.github.io/helm-chart-sonarqube
helm repo update
kubectl create namespace sonarqube-dce 
export JWT_SECRET=$(echo -n "your_secret" | openssl dgst -sha256 -hmac "your_key" -binary | base64) 
export MONITORING_PASSCODE="yourPasscode"
export JDBC_URL="jdbc:postgresql://myPostgres/myDatabase"
export JDBC_USERNAME="sonar"
export JDBC_PASSWORD_SECRET_NAME="jdbc-secret"
export JDBC_PASSWORD_SECRET_KEY="jdbc-password"
helm upgrade --install -n sonarqube-dce sonarqube sonarqube/sonarqube-dce \
  --set applicationNodes.jwtSecret=$JWT_SECRET \
  --set OpenShift.enabled=true \
  --set applicationNodes.jwtSecret=$JWT_SECRET \
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

* [before-you-start](https://docs.sonarsource.com/sonarqube-server/server-installation/data-center-edition/on-kubernetes-or-openshift/before-you-start "mention")
* [customizing-helm-chart](https://docs.sonarsource.com/sonarqube-server/server-installation/data-center-edition/on-kubernetes-or-openshift/customizing-helm-chart "mention")
* [installing-from-gcp](https://docs.sonarsource.com/sonarqube-server/server-installation/data-center-edition/on-kubernetes-or-openshift/installing-from-gcp "mention")
* [set-up-monitoring](https://docs.sonarsource.com/sonarqube-server/server-installation/on-kubernetes-or-openshift/set-up-monitoring "mention")
* [setting-up-autoscaling](https://docs.sonarsource.com/sonarqube-server/server-installation/data-center-edition/on-kubernetes-or-openshift/setting-up-autoscaling "mention")
