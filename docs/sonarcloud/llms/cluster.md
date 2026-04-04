# Source: https://docs.sonarsource.com/sonarqube-server/10.4/setup-and-upgrade/deploy-on-kubernetes/cluster.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.5/setup-and-upgrade/deploy-on-kubernetes/cluster.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.6/setup-and-upgrade/deploy-on-kubernetes/cluster.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/setup-and-upgrade/deploy-on-kubernetes/cluster.md

# Deploying SonarQube cluster

This page applies to deploying SonarQube Data Center Edition on Kubernetes. For information on deploying Community, Developer, and Enterprise editions of SonarQube on Kubernetes, see [introduction](https://docs.sonarsource.com/sonarqube-server/10.7/setup-and-upgrade/deploy-on-kubernetes/server/introduction "mention") documentation.

### Overview <a href="#overview" id="overview"></a>

You can find the SonarQube DCE Helm chart on [GitHub](https://github.com/SonarSource/helm-chart-sonarqube/tree/master/charts/sonarqube-dce).

Your feedback is welcome at [our community forum](https://community.sonarsource.com/).

### Kubernetes environment recommendations <a href="#kubernetes-environment-recommendations" id="kubernetes-environment-recommendations"></a>

When you want to operate SonarQube on Kubernetes, consider the following recommendations.

#### Supported versions <a href="#supported-versions" id="supported-versions"></a>

The SonarQube helm chart should only be used with the latest version of SonarQube and a supported version of Kubernetes. There is a dedicated helm chart for the LTA ([active-versions](https://docs.sonarsource.com/sonarqube-server/10.7/server-upgrade-and-maintenance/upgrade/upgrade-the-server/active-versions "mention")) version of SonarQube that follows the same patch policy as the application, while also being compatible with the supported versions of Kubernetes.

#### Pod Security Standards <a href="#pod-security-standards" id="pod-security-standards"></a>

Here is the list of containers that are compatible with the [Pod Security levels](https://kubernetes.io/docs/concepts/security/pod-security-admission/#pod-security-levels):

* privileged:
  * `init-sysctl`
* baseline:
  * `init-fs`
* restricted:
  * SQ application containers
  * SQ init containers.
  * PostgreSQL containers.

This is achieved by setting this `SecurityContext` as default on most containers:

```css-79elbk
allowPrivilegeEscalation: false
runAsNonRoot: true
runAsUser: 1000
runAsGroup: 1000
seccompProfile:
  type: RuntimeDefault
capabilities:
  drop: ["ALL"]
```

Based on that, one can run the SQ helm chart in a full restricted namespace, by deactivating the `initSysctl.enabled` and `initFs.enabled` parameters, which require root access.

For more information, see the [production-use-case](https://github.com/SonarSource/helm-chart-sonarqube/tree/master/charts/sonarqube-dce#production-use-case) or take a look at the `values.yaml` file.

### Helm chart specifics <a href="#helm-chart-specifics" id="helm-chart-specifics"></a>

We try to provide a good default with the Helm chart, but there are some points to consider while working with SonarQube on Kubernetes. Please read the following sections carefully to make the correct decisions for your environment.

#### Persistency <a href="#persistency" id="persistency"></a>

SonarQube comes with a bundled Elasticsearch and, as Elasticsearch is stateful, so is SonarQube. For Data Center Edition (DCE) clusters, it makes sense to persist the Elasticsearch data because the cluster will survive the loss of any single search node without index corruption. By default, persistency is *enabled* for the DCE, and managed with the Helm chart.

Enabling persistency decreases the project reload time so that accessing project data is much faster. Although there is no need to change the default value in DCE, you can manage persistency with the following parameter in the `values.yaml`:

```css-79elbk
persistence:
  enabled: true
```

Disabling persistency would result in a longer startup time until SonarQube is fully available which can be a very large factor considering the downtime for the index rebuild on DCE clusters.

#### Ingress Creation <a href="#ingress-creation" id="ingress-creation"></a>

To make the SonarQube service accessible from outside of your cluster, you most likely need an ingress. Creating a new ingress is also covered by the Helm chart. See the following section for help with creating one.

**Ingress Class**

The Sonar Helm chart has an optional dependency to the [NGINX-ingress helm chart](https://kubernetes.github.io/ingress-nginx). If you already have NGINX-ingress present in your cluster, you can use it.

If you want to install NGINX as well, add the following to your `values.yaml`.

```css-79elbk
nginx:
  enabled: true
```

We recommend using the `ingress-class` NGINX with a body size of at least 8MB. This can be achieved with the following changes to your `values.yaml`:

```css-79elbk
ingress:
  enabled: true
  # Used to create an Ingress record.
  hosts:
    - name: <Your Sonarqube FQDN>
      # Different clouds or configurations might need /* as the default path
      path: /
      # For additional control over serviceName and servicePort
      # serviceName: someService
      # servicePort: somePort
  annotations: 
    kubernetes.io/ingress.class: nginx
    nginx.ingress.kubernetes.io/proxy-body-size: "8m"
```

#### Monitoring <a href="#monitoring" id="monitoring"></a>

See [introduction](https://docs.sonarsource.com/sonarqube-server/10.7/setup-and-upgrade/deploy-on-kubernetes/set-up-monitoring/introduction "mention")

#### Log Format <a href="#log-format" id="log-format"></a>

SonarQube prints all logs in plain-text to stdout/stderr. It can print logs as JSON-String if the variable `logging.jsonOutput` is set to `true`. This will enable log collection tools like [Loki](https://grafana.com/oss/loki/) to do post processing on the information that are provided by the application.

**LogQL Example**

With JSON Logging enabled, you can define a LogQL Query like this to filter only logs with the severity "ERROR" and display the Name of the Pod as well as the Message:

```css-79elbk
{namespace="sonarqube-dce", app="sonarqube-dce"}| json | severity="ERROR" | line_format "{{.nodename}} {{.message}}"
```

#### ES Cluster Authentication <a href="#es-cluster-authentication" id="es-cluster-authentication"></a>

Since SonarQube 8.9, you can enable basic security for the Search Cluster in SonarQube. To benefit from this additional layer of security on Kubernetes as well, you need to provide a PKCS#11 Container with the required certificates to our Helm chart. The required secret can be created like this:

```css-79elbk
kubectl create secret generic <NAME OF THE SECRET> --from-file=/PATH/TO/YOUR/PKCS12.container=elastic-stack-ca.p12 -n <NAMESPACE>
```

#### Other Configuration Options <a href="#other-configuration-options" id="other-configuration-options"></a>

This documentation only contains the most important Helm chart customizations. See the [Customize the chart before installing](https://helm.sh/docs/intro/using_helm/#customizing-the-chart-before-installing) documentation and the Helm chart [README](https://github.com/SonarSource/helm-chart-sonarqube/tree/master/charts/sonarqube-dce) for more possibilities on customizing the Helm chart.

### Known limitations <a href="#known-limitations" id="known-limitations"></a>

#### Problems with Azure Fileshare PVC <a href="#problems-with-azure-fileshare-pvc" id="problems-with-azure-fileshare-pvc"></a>

Currently, there is a known limitation when working on AKS that resonates around the use of Azure Fileshare. We recommend using another storage class for persistency on AKS.

### Installing from the Helm repository <a href="#install-from-helm-repo" id="install-from-helm-repo"></a>

Currently only Helm 3 is supported.

To install the Helm chart from Helm repository, you can use the following commands:

```css-79elbk
helm repo add sonarqube https://SonarSource.github.io/helm-chart-sonarqube
helm repo update
kubectl create namespace sonarqube-dce
export JWT_SECRET=$(echo -n "your_secret" | openssl dgst -sha256 -hmac "your_key" -binary | base64)
helm upgrade --install -n sonarqube-dce sonarqube-dce --set ApplicationNodes.jwtSecret=$JWT_SECRET sonarqube/sonarqube-dce
```

The `helm upgrade --install -n sonarqube-dce sonarqube-dce --set` line allows you to customize the [Helm chart values](https://helm.sh/docs/chart_template_guide/values_files/).

The `echo`command allows you to set the value of your Application authentication JWT token. This value must be an HS256 key encoded with base64.

### Installing from the Google Cloud Platform <a href="#install-from-gcp" id="install-from-gcp"></a>

SonarQube DCE can be deployed on Kubernetes through the Google Marketplace, using its "Click to Deploy" feature with the following current limitations:

* SonarQube DCE can’t be deployed into "Autopilot" clusters.
* SonarQube DCE is not compatible with Istio.

#### Prerequisites <a href="#prerequisites" id="prerequisites"></a>

Make sure that you have kubectl configured in your environment and that your cluster has Google’s Application CustomResourceDefinition installed. That definition can be obtained from [this file](https://raw.githubusercontent.com/GoogleCloudPlatform/marketplace-k8s-app-tools/master/crd/app-crd.yaml).

#### Pre-installation steps <a href="#preinstallation-steps" id="preinstallation-steps"></a>

* Set the value of your Application authentication JWT Token. This value is an HS256 key encoded with base64. To do so, you may use the `echo` command below:

```css-79elbk
echo -n "your_secret" | openssl dgst -sha256 -hmac "your_key" -binary | base64 
```

* If necessary, create the target namespace you want to install SonarQube DCE into.

#### Installing using Click to Deploy <a href="#installing-using-click-to-deploy" id="installing-using-click-to-deploy"></a>

1. Go to the [SonarQube DCE page](https://console.cloud.google.com/marketplace/product/sonarsource-public/sonarqube-data-center-edition) on the Google Cloud Platform.
2. Click **Get started** and follow the instructions.
3. In the **Deploy** page, fill in the fields in the **Click to Deploy on GKE** tab: see **Installation parameters** below.
4. At the bottom of the tab, click **Deploy**.

#### Installing manually <a href="#installing-manually" id="installing-manually"></a>

For manual installation or development purposes, SonarQube can be configured using the [mpdev CLI tool](https://github.com/GoogleCloudPlatform/marketplace-k8s-app-tools) provided by Google. See Installation parameters below for the supported parameters with key.

#### Deleting the installation <a href="#deleting-the-installation" id="deleting-the-installation"></a>

To delete the installation of SonarQube from your cluster:

1. Delete the created Application resource.
2. Delete the PersistentVolumeClaims related to the search nodes and database (if applicable).

#### Installation parameters <a href="#installation-parameters" id="installation-parameters"></a>

| **Name**                                                                           | **Description**                                                                                                                                                                                                                               | **Key**                       | **Type**    |
| ---------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------- | ----------- |
| Existing Kubernetes cluster                                                        | Kubernetes cluster in which the application will be deployed.                                                                                                                                                                                 | <p><br></p>                   | <p><br></p> |
| Namespace                                                                          | Target namespace to install SonarQube DCE into (The namespace must exist already, it will not be created automatically.).                                                                                                                     | namespace                     | string      |
| App instance name                                                                  | Name of the application in your Kubernetes cluster                                                                                                                                                                                            | name                          | string      |
| Application authentication JWT Token                                               | The HS256 key encoded with base64: see **Pre-installation steps** above.                                                                                                                                                                      | ApplicationNode.jwtSecret     | string      |
| Connection to a database - Recommended                                             | If enabled, SonarQube will be connected to your PostgreSQL database. The connection parameters **JDBC URL**, **username**, and **password** will be used. Make sure that the **Embedded database** option is disabled.                        | jdbcOverwrite.enable          | boolean     |
| JDBC URL                                                                           | The JDBC URL used to connect to the database.                                                                                                                                                                                                 | jdbcOverwrite.jdbcUrl         | string      |
| JDB Username                                                                       | The username used to connect to the database.                                                                                                                                                                                                 | jdbcOverwrite.jdbcUsername    | string      |
| JDBC Password                                                                      | The password used to connect to the database.                                                                                                                                                                                                 | jdbcOverwrite.jdbcPassword    | string      |
| Application nodes replicas                                                         | The number of replicas for the Application Nodes                                                                                                                                                                                              | ApplicationNodes.replicaCount | integer     |
| Search nodes replicas                                                              | The number of replicas for the Search Nodes                                                                                                                                                                                                   | searchNodes.replicaCount      | integer     |
| Enable initSysctl privileged initContainer to setup elasticearch kernel parameters | This should be disabled and set up by your cluster administrator. Refer to this [documentation](https://github.com/SonarSource/helm-chart-sonarqube/blob/master/charts/sonarqube-dce/README.md#elasticsearch-prerequisites) for more details. | initSysctl.enabled            | boolean     |
| Enable initFs root initContainer to setup filesystem parameters                    | This is generally not required on a Google Kubernetes cluster. Refer to [this documentation](https://github.com/SonarSource/helm-chart-sonarqube/blob/master/charts/sonarqube-dce/README.md#production-use-case) for more details.            | initFs.enabled                | boolean     |
| GCP Marketplace application                                                        | This flag must be enabled in the context of the installation from GCP.                                                                                                                                                                        | gcp\_marketplace              | boolean     |
| Embedded database - For testing purposes only                                      | Not recommended for production: a test PostgreSQL database will be installed.                                                                                                                                                                 | postgresql.enabled            | boolean     |
