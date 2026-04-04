# Source: https://docs.sonarsource.com/sonarqube-server/9.8/setup-and-upgrade/deploy-on-kubernetes/deploy-a-sonarqube-cluster-on-kubernetes.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.9/setup-and-upgrade/deploy-on-kubernetes/deploy-a-sonarqube-cluster-on-kubernetes.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.0/setup-and-upgrade/deploy-on-kubernetes/deploy-a-sonarqube-cluster-on-kubernetes.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.1/setup-and-upgrade/deploy-on-kubernetes/deploy-a-sonarqube-cluster-on-kubernetes.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.2/setup-and-upgrade/deploy-on-kubernetes/deploy-a-sonarqube-cluster-on-kubernetes.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.3/setup-and-upgrade/deploy-on-kubernetes/deploy-a-sonarqube-cluster-on-kubernetes.md

# Deploy a SonarQube cluster on Kubernetes

*This page applies to deploying SonarQube Data Center Edition on Kubernetes. For information on deploying Community, Developer, and Enterprise editions of SonarQube on Kubernetes,* see [deploy-sonarqube-on-kubernetes](https://docs.sonarsource.com/sonarqube-server/10.3/setup-and-upgrade/deploy-on-kubernetes/deploy-sonarqube-on-kubernetes "mention") documentation.

### Overview <a href="#overview" id="overview"></a>

You can find the SonarQube DCE Helm chart on [GitHub](https://github.com/SonarSource/helm-chart-sonarqube/tree/master/charts/sonarqube-dce).

Your feedback is welcome at [our community forum](https://community.sonarsource.com/).

### Kubernetes environment recommendations <a href="#kubernetes-environment-recommendations" id="kubernetes-environment-recommendations"></a>

When you want to operate SonarQube on Kubernetes, consider the following recommendations.

#### Supported versions <a href="#supported-versions" id="supported-versions"></a>

The SonarQube helm chart should only be used with the latest version of SonarQube and a supported version of Kubernetes. There is a dedicated helm chart for the LTS version of SonarQube that follows the same patch policy as the application, while also being compatible with the supported versions of Kubernetes.

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

#### Installation <a href="#installation" id="installation"></a>

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

The SonarSource Helm chart has an optional dependency to the [NGINX-ingress helm chart](https://kubernetes.github.io/ingress-nginx). If you already have NGINX-ingress present in your cluster, you can use it.

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

You can monitor your SonarQube cluster using SonarQube’s native integration with Prometheus. Through this integration, you can ensure your cluster is running properly and know if you need to take action to prevent future issues.

Prometheus monitors your SonarQube cluster by collecting metrics from the `/api/monitoring/metrics` endpoint. Results are returned in OpenMetrics text format. See Prometheus’ documentation on [Exposition formats](https://prometheus.io/docs/instrumenting/exposition_formats/) for more information on the OpenMetrics text format.

Monitoring through this endpoint requires authentication. You can access the endpoint following ways:

* **`Authorization:Bearer xxxx`** **header:** You can use a bearer token during database upgrade and when SonarQube is fully operational. Define the bearer token in the `sonar.properties` file using the `sonar.web.systemPasscode property`.
* **`X-Sonar-Passcode: xxxxx`** **header:** You can use `X-Sonar-passcode` during database upgrade and when SonarQube is fully operational. Define `X-Sonar-passcode` in the `sonar.properties` file using the `sonar.web.systemPasscode property`.
* **username:password and JWT token:** When SonarQube is fully operational, system admins logged in with local or delegated authentication can access the endpoint.

**JMX Exporter**

You can also expose the JMX metrics to Prometheus with the help of the Prometheus JMX exporter.

To use this option, set the following values in your `values.yaml` file:

```css-79elbk
prometheusExporter:
  enabled: true
  config:
    rules:
      - pattern: ".*"
```

This downloads the Prometheus JMX exporter agent and adds it to the startup options of SonarQube. With this default configuration, the JMX metrics will be exposed on /metrics for Prometheus to scrape.

The config scope here defines a configuration that is understandable by the Prometheus JMX exporter. For more information, please Prometheus’ documentation on the [JMX exporter](https://github.com/prometheus/jmx_exporter).

**PodMonitor**

You can collect metrics on application nodes using PodMonitor for Prometheus. Search node monitoring is not currently supported. To monitor applications nodes, define PodMonitor as follows:

```css-79elbk
apiVersion: monitoring.coreos.com/v1
kind: PodMonitor
metadata:
  name: sonarqube
  namespace: monitoring
spec:
  namespaceSelector:
    matchNames:
    - sonarqube-dce
  podMetricsEndpoints:
  - interval: 30s
    path: /
    scheme: http
    targetPort: monitoring-ce
  - interval: 30s
    path: /
    scheme: http
    targetPort: monitoring-web
  selector:
    matchLabels:
      app: sonarqube-dce
```

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

### Upgrade <a href="#upgrade" id="upgrade"></a>

See **Upgrading instructions > Upgrading from the Helm chart** in [upgrade-guide](https://docs.sonarsource.com/sonarqube-server/10.3/setup-and-upgrade/upgrade-the-server/upgrade-guide "mention").
