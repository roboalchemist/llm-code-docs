# Source: https://docs.sonarsource.com/sonarqube-server/10.8/setup-and-upgrade/deploy-on-kubernetes/dce/installing-from-gcp.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/setup-and-update/deploy-on-kubernetes/dce/installing-from-gcp.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/server-installation/data-center-edition/on-kubernetes-or-openshift/installing-from-gcp.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/server-installation/data-center-edition/on-kubernetes-or-openshift/installing-from-gcp.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/setup-and-upgrade/deploy-on-kubernetes/dce/installing-from-gcp.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/server-installation/data-center-edition/on-kubernetes-or-openshift/installing-from-gcp.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/server-installation/data-center-edition/on-kubernetes-or-openshift/installing-from-gcp.md

# Source: https://docs.sonarsource.com/sonarqube-server/server-installation/data-center-edition/on-kubernetes-or-openshift/installing-from-gcp.md

# Installing from Google Cloud Platform

Data Center Edition can be deployed on Kubernetes through the Google Marketplace:

* Either with basic features only, by using its *Click to Deploy* feature.
* Or with advanced features by using its *Deploy via command line* feature.

### Basic installation

With the basic installation, you cannot benefit from various features such as autoscaling or deploying with Istio.

#### Prerequisites

Make sure that kubectl is configured in your environment and that your cluster has Google’s Application CustomResourceDefinition installed. That definition can be obtained from [this file](https://raw.githubusercontent.com/GoogleCloudPlatform/marketplace-k8s-app-tools/master/crd/app-crd.yaml).

#### Pre-installation steps <a href="#pre-installation" id="pre-installation"></a>

* Set the value of your Application authentication JWT Token. See [jwt-token](https://docs.sonarsource.com/sonarqube-server/server-installation/pre-installation/jwt-token "mention").
* If necessary, create the target namespace you want to install Data Center Edition into.

#### Installing using Click to Deploy <a href="#click-to-deploy" id="click-to-deploy"></a>

1. Go to the [Data Center Edition page](https://console.cloud.google.com/marketplace/product/sonarsource-public/sonarqube-data-center-edition) on the Google Cloud Platform.
2. Click **Get started** and follow the instructions.
3. In the **Deploy** page, fill in the fields in the **Click to Deploy on GKE** tab: see **Installation parameters** below.
4. At the bottom of the tab, click **Deploy**.

#### Installing manually <a href="#installing-manually" id="installing-manually"></a>

For manual installation or development purposes, SonarQube Server can be configured using the [mpdev CLI tool](https://github.com/GoogleCloudPlatform/marketplace-k8s-app-tools) provided by Google. See Installation parameters below for the supported parameters with key.

#### Deleting the installation <a href="#deleting-installation" id="deleting-installation"></a>

To delete the installation of SonarQube Server from your cluster:

1. Delete the created Application resource.
2. Delete the PersistentVolumeClaims related to the search nodes and database (if applicable).

#### Installation parameters <a href="#installation-parameters" id="installation-parameters"></a>

<table><thead><tr><th width="138">Name</th><th width="352">Description</th><th width="179">Key</th><th>Type</th></tr></thead><tbody><tr><td>Existing Kubernetes cluster</td><td>Kubernetes cluster in which the application will be deployed.</td><td><br></td><td><br></td></tr><tr><td>Namespace</td><td>Target namespace to install Data Center Edition into (The namespace must exist already, it will not be created automatically.).</td><td>namespace</td><td>string</td></tr><tr><td>App instance name</td><td>Name of the application in your Kubernetes cluster</td><td>name</td><td>string</td></tr><tr><td>Application authentication JWT Token</td><td>The HS256 key encoded with base64: see <strong>Pre-installation steps</strong> above.</td><td>ApplicationNode.jwtSecret</td><td>string</td></tr><tr><td>JDBC URL</td><td>The JDBC URL used to connect to the database.</td><td>jdbcOverwrite.jdbcUrl</td><td>string</td></tr><tr><td>JDBC Username</td><td>The username used to connect to the database.</td><td>jdbcOverwrite.jdbcUsername</td><td>string</td></tr><tr><td>JDBC Password</td><td>The password used to connect to the database.</td><td>jdbcOverwrite.jdbcPassword</td><td>string</td></tr><tr><td>Application nodes replicas</td><td>The number of replicas for the Application Nodes</td><td>ApplicationNodes.replicaCount</td><td>integer</td></tr><tr><td>Search nodes replicas</td><td>The number of replicas for the Search Nodes</td><td>searchNodes.replicaCount</td><td>integer</td></tr><tr><td>Enable initSysctl privileged initContainer to setup elasticearch kernel parameters</td><td>This should be disabled and set up by your cluster administrator. Refer to this <a href="https://github.com/SonarSource/helm-chart-sonarqube/blob/master/charts/sonarqube-dce/README.md#elasticsearch-prerequisites">documentation</a> for more details.</td><td>initSysctl.enabled</td><td>boolean</td></tr><tr><td>Enable initFs root initContainer to setup filesystem parameters</td><td>This is generally not required on a Google Kubernetes cluster. Refer to <a href="https://github.com/SonarSource/helm-chart-sonarqube/blob/master/charts/sonarqube-dce/README.md#production-use-case">this documentation</a> for more details.</td><td>initFs.enabled</td><td>boolean</td></tr><tr><td>GCP Marketplace application</td><td>This flag must be enabled in the context of the installation from GCP.</td><td>gcp_marketplace</td><td>boolean</td></tr></tbody></table>

### Advanced installation

Use the advanced installation if you want to benefit from various features such as autoscaling or deploying with Istio.

Proceed as follows:

1. Customize the Helm chart. See Customizing the Helm chart.
2. Go to the [Data Center Edition page](https://console.cloud.google.com/marketplace/product/sonarsource-public/sonarqube-data-center-edition) on the Google Cloud Platform.
3. In the **Deploy** page of your Google Cloud Platform, select the **Deploy via command line** tab.
4. Follow the instructions:
   1. Clone the[ repo](https://github.com/SonarSource/helm-chart-sonarqube).
   2. Use the command described in [installing-from-helm-repo](https://docs.sonarsource.com/sonarqube-server/server-installation/data-center-edition/on-kubernetes-or-openshift/installing-from-helm-repo "mention").

### Related pages <a href="#related-pages" id="related-pages"></a>

* [before-you-start](https://docs.sonarsource.com/sonarqube-server/server-installation/data-center-edition/on-kubernetes-or-openshift/before-you-start "mention")
* [customizing-helm-chart](https://docs.sonarsource.com/sonarqube-server/server-installation/data-center-edition/on-kubernetes-or-openshift/customizing-helm-chart "mention")
* [installing-from-helm-repo](https://docs.sonarsource.com/sonarqube-server/server-installation/data-center-edition/on-kubernetes-or-openshift/installing-from-helm-repo "mention")
* [set-up-monitoring](https://docs.sonarsource.com/sonarqube-server/server-installation/on-kubernetes-or-openshift/set-up-monitoring "mention")
* [setting-up-autoscaling](https://docs.sonarsource.com/sonarqube-server/server-installation/data-center-edition/on-kubernetes-or-openshift/setting-up-autoscaling "mention")
