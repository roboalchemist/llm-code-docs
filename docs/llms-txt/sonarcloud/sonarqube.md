# Source: https://docs.sonarsource.com/sonarqube-server/10.4/setup-and-upgrade/deploy-on-kubernetes/sonarqube.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.5/setup-and-upgrade/deploy-on-kubernetes/sonarqube.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.6/setup-and-upgrade/deploy-on-kubernetes/sonarqube.md

# Deploying SonarQube

This part of the Documentation is only valid for Community, Developer, and Enterprise Editions. For information on deploying the Data Center Edition of SonarQube on Kubernetes, see [cluster](https://docs.sonarsource.com/sonarqube-server/10.6/setup-and-upgrade/deploy-on-kubernetes/cluster "mention") documentation\*.\*

### Overview <a href="#overview" id="overview"></a>

You can find the SonarQube Helm chart on [GitHub](https://github.com/SonarSource/helm-chart-sonarqube/tree/master/charts/sonarqube).

Your feedback is welcome at [our community forum](https://community.sonarsource.com/).

### Kubernetes environment recommendations <a href="#kubernetes-environment-recommendations" id="kubernetes-environment-recommendations"></a>

When you want to operate SonarQube on Kubernetes, consider the following recommendations.

#### Prerequisites <a href="#prerequisites" id="prerequisites"></a>

**Supported versions**

The SonarQube helm chart should only be used with the latest version of SonarQube and a supported version of Kubernetes. There is a dedicated helm chart for the LTA([active-versions](https://docs.sonarsource.com/sonarqube-server/10.6/setup-and-upgrade/upgrade-the-server/active-versions "mention")) version of SonarQube that follows the same patch policy as the application, while also being compatible with the supported versions of Kubernetes.

#### Pod Security Standards <a href="#pod-security-standards" id="pod-security-standards"></a>

Here is the list of containers that are compatible with the [Pod Security levels](https://kubernetes.io/docs/concepts/security/pod-security-admission/#pod-security-levels):

* privileged:
  * `init-sysctl`
* baseline:
  * `init-fs`
* restricted:
  * SQ application containers
  * SQ init containers.
  * postgresql containers.

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

For more information, see the [production-use-case](https://github.com/SonarSource/helm-chart-sonarqube/blob/master/charts/sonarqube/README.md#production-use-case) or take a look at the `values.yaml` file.

#### Installation <a href="#installation" id="installation"></a>

Currently, only Helm 3 is supported.

To install the Helm Chart from our Helm Repository, you can use the following commands:

```css-79elbk
helm repo add sonarqube https://SonarSource.github.io/helm-chart-sonarqube
helm repo update
kubectl create namespace sonarqube
helm upgrade --install -n sonarqube sonarqube sonarqube/sonarqube
```

#### Persistency <a href="#persistency" id="persistency"></a>

SonarQube comes with a bundled Elasticsearch and, as Elasticsearch is stateful, so is SonarQube. There is an option to persist the Elasticsearch indexes in a Persistent Volume, but with regular killing operations by the Kubernetes Cluster, these indexes can be corrupted. By default, persistency is disabled in the Helm chart.

Enabling persistency decreases the startup time of the SonarQube Pod significantly, but you are risking corrupting your Elasticsearch index. You can enable persistency by adding the following to the `values.yaml`:

```css-79elbk
persistence:
  enabled: true
```

Leaving persistency disabled results in a longer startup time until SonarQube is fully available, but you won’t lose any data as SonarQube will persist all data in the database.

#### Self-signed certificate <a href="#selfsigned-certificate" id="selfsigned-certificate"></a>

When you’re working with your own CA or in an environment that uses self-signed certificates for your code repository platform, you can create a secret containing this certificate and add this certificate to the Java truststore inside the SonarQube deployment directly during the deployment.

To enable this behavior, add the following to your `value.yaml` file:

```css-79elbk
caCerts:
  secret: <secret name>
```

**Get Certificate via openssl**

If you already have a running installation of your code repository platform, you can extract the certificate with the following snippet using `openssl`

```css-79elbk
echo -n | openssl s_client -connect <server url>:443 | sed -ne '/-BEGIN CERTIFICATE-/,/-END CERTIFICATE-/p' > cert.pem
```

This certificate needs to be Base64 encoded in order to be added as secret data.

```css-79elbk
Create base64 string
cat cert.pem | base64 | tr -d "\n"
```

Note that you can also use `string-data` here if you don’t want to encode your certificate.

**Create secret**

The Base64 encoded certificate can be added to the secret’s data:

```css-79elbk
apiVersion: v1
kind: Secret
metadata:
  name: <secret name>
  namespace: <sonarqube namespace>
data:
  cert: <base64 string>
```

Then, create the secret in your Kubernetes cluster with the following command:

```css-79elbk
kubectl apply -f secret.yaml
```

#### Ingress creation <a href="#ingress-creation" id="ingress-creation"></a>

To make the SonarQube service accessible from outside of your cluster, you most likely need an ingress. Creating a new ingress is also covered by the Helm chart. See the following section for help with creating one.

**Ingress Class**

The SonarSource Helm chart has an optional dependency on the [NGINX-ingress helm chart](https://kubernetes.github.io/ingress-nginx). If you already have NGINX-ingress present in your cluster, you can use it.

If you want to install NGINX as well, add the following to your `values.yaml`.

```css-79elbk
nginx:
  enabled: true
```

We recommend using the ingress-class NGINX with a body size of at least 64MB (see also **Issue with downloading regulatory reports** in [troubleshooting](https://docs.sonarsource.com/sonarqube-server/10.6/setup-and-upgrade/troubleshooting "mention")). This can be achieved with the following changes to your values.yaml:

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
    nginx.ingress.kubernetes.io/proxy-body-size: "64m"
```

#### Monitoring <a href="#monitoring" id="monitoring"></a>

See [introduction](https://docs.sonarsource.com/sonarqube-server/10.6/setup-and-upgrade/deploy-on-kubernetes/set-up-monitoring/introduction "mention")

#### Customizing Helm chart values <a href="#customizing-helm-chart-values" id="customizing-helm-chart-values"></a>

You can customize the [Helm chart values](https://helm.sh/docs/chart_template_guide/values_files/) with various methods. One example is directly at the command line:

```css-79elbk
helm upgrade --install --set edition=enterprise sonarqube sonarqube/sonarqube
```

#### Other configuration options <a href="#other-configuration-options" id="other-configuration-options"></a>

While we only document the most pressing Helm chart customizations in this documentation, there are other possibilities for you to choose to [customize the chart before installing](https://helm.sh/docs/intro/using_helm/#customizing-the-chart-before-installing). Please see the Helm chart [README](https://github.com/SonarSource/helm-chart-sonarqube/tree/master/charts/sonarqube) file for more information on these.

### Known limitations <a href="#known-limitations" id="known-limitations"></a>

As SonarQube is intended to be run anywhere, there are some drawbacks that are currently known when operating in Kubernetes. This list is not comprehensive, but something to keep in mind and points for us to improve on.

#### Readiness and startup delays <a href="#readiness-and-startup-delays" id="readiness-and-startup-delays"></a>

When persistence is disabled, SonarQube startup takes significantly longer as the Elasticsearch indexes need to be rebuilt. As this delay depends on the amount of data in your SonarQube instance, the values for the startup/readiness and liveness probes need to be adjusted to your environment. We also recommend taking a look at the default limits for the SonarQube deployment as the amount of CPU available to SonarQube also impacts the startup time.

#### Problems with Azure Fileshare PVC <a href="#problems-with-azure-fileshare-pvc" id="problems-with-azure-fileshare-pvc"></a>

Currently, there is a known limitation when working on AKS that resonates around the use of Azure Fileshare. We recommend using another storage class for persistency on AKS.
