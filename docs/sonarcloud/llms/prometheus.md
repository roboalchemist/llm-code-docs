# Source: https://docs.sonarsource.com/sonarqube-community-build/server-installation/on-kubernetes-or-openshift/set-up-monitoring/prometheus.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.4/setup-and-upgrade/deploy-on-kubernetes/set-up-monitoring/prometheus.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.5/setup-and-upgrade/deploy-on-kubernetes/set-up-monitoring/prometheus.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.6/setup-and-upgrade/deploy-on-kubernetes/set-up-monitoring/prometheus.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/setup-and-upgrade/deploy-on-kubernetes/set-up-monitoring/prometheus.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/setup-and-upgrade/deploy-on-kubernetes/set-up-monitoring/prometheus.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/setup-and-update/deploy-on-kubernetes/set-up-monitoring/prometheus.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/server-installation/on-kubernetes-or-openshift/set-up-monitoring/prometheus.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/server-installation/on-kubernetes-or-openshift/set-up-monitoring/prometheus.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/setup-and-upgrade/deploy-on-kubernetes/set-up-monitoring/prometheus.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/server-installation/on-kubernetes-or-openshift/set-up-monitoring/prometheus.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/server-installation/on-kubernetes-or-openshift/set-up-monitoring/prometheus.md

# Source: https://docs.sonarsource.com/sonarqube-server/server-installation/on-kubernetes-or-openshift/set-up-monitoring/prometheus.md

# Setting up with Prometheus server

To set up the monitoring, follow the steps described below. We refer here to a setup using the Prometheus Operator which requires the PodMonitor to collect the metrics. The Prometheus Operator needs to be installed separately.

### Introduction <a href="#introduction" id="introduction"></a>

The deployment process is as follows:

1. When you install the SonarQube Server’s Helm chart in the Kubernetes cluster, the chart creates a PodMonitor resource (`podmonitor.yaml`), which configures the pulling of metrics from SonarQube Server.
2. The Prometheus operator deploys the Prometheus server and watches the PodMonitor to inject the relevant configuration to the Prometheus server.
3. The Prometheus server will pull the metrics from SonarQube Server according to the PodMonitor configuration. To pull the metrics from the Web API endpoint, it needs to authenticate to the Web API. The Helm chart sets up the PodMonitor to use the system passcode defined in the Helm chart for Bearer authentication scheme.

The figure below illustrates this process.

<figure><img src="broken-reference" alt="SonarQube deployment steps with Prometheus server"><figcaption></figcaption></figure>

### Step 1: Set up the Prometheus server authentication to the Web API’s monitoring endpoint <a href="#set-up-authentication-to-api-endpoint" id="set-up-authentication-to-api-endpoint"></a>

The PodMonitor needs to authenticate to the SonarQube Server’s Web API for getting metrics from the `/api/monitoring/metrics` endpoint. To setup this authentication, you must define the monitoring password in `values.yaml`: the Helm chart will store this value in the `SONAR_WEB_SYSTEMPASSCODE` environment variable on SonarQube Server.

To set the monitoring passcode in SonarQube Server, use one of the following methods (see also the [Helm chart documentation](https://artifacthub.io/packages/helm/sonarqube/sonarqube#sonarqube-specific)):

* Define the passcode in the `monitoringPasscode` property within the `values.yaml` file (default value is "define\_it").\
  For security reasons, this method is not recommended.
* Use a secret that contains the passcode that will be retrieved at runtime, and define the following properties in `values.yaml`:
  * `monitoringPasscodeSecretName`: name of the secret object.
  * `monitoringPasscodeSecretKey`: key identifying the passcode to be extracted from the secret object.

### Step 2: Enable the export of the JMX metrics <a href="#enable-jmx-metrics" id="enable-jmx-metrics"></a>

To expose the Prometheus JMX metrics, the JMX exporter must be enabled in the Helm chart configuration as follows:

* Add the following block in the `values.yaml` file of the SonarQube Server Helm chart:

```css-79elbk
prometheusExporter:
  enabled: true
  config:
    rules:
      - pattern: ".*"
```

### Step 3: Enable the PodMonitor <a href="#enable-podmonitor" id="enable-podmonitor"></a>

1. If not already done, install the Prometheus Operator in the Kubernetes cluster (it’s not installed through the Helm chart).
2. In the SonarQube Helm chart, enable the PodMonitor by setting `prometheusMonitoring.podMonitor.enabled` to `true`.
3. If necessary, adjust the PodMonitor created by default by the SonarQube Helm chart. Below is the default `podmonitor.yaml` file depending on the SonarQube Edition.\
   To adjust the PodMonitor:
   * Either edit the Helm chart.\
     For more information, see [Prometheus PodMonitor](https://artifacthub.io/packages/helm/sonarqube/sonarqube#monitoring-prometheus-podmonitor) in the Helm chart documentation.
   * Or edit the created `podmonitor.yaml` file directly.

<details>

<summary>Default PodMonitor: Developer and Enterprise Editions</summary>

```css-79elbk
apiVersion: monitoring.coreos.com/v1
kind: PodMonitor
metadata:
  name: sonarqube
  namespace: monitoring
spec:
  namespaceSelector:
    matchNames:
    - sonarqube
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
      app: sonarqube
```

</details>

<details>

<summary>Default PodMonitor: Data Center Edition</summary>

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

</details>

### Step 4: Set up the export of the metrics to an observability platform <a href="#set-up-metrics-export" id="set-up-metrics-export"></a>

See [prometheus-metrics](https://docs.sonarsource.com/sonarqube-server/server-installation/on-kubernetes-or-openshift/set-up-monitoring/prometheus-metrics "mention") for more information.

### Related pages <a href="#related-pages" id="related-pages"></a>

* [introduction](https://docs.sonarsource.com/sonarqube-server/server-installation/on-kubernetes-or-openshift/set-up-monitoring/introduction "mention") to Setting up monitoring
* [customizing-helm-chart](https://docs.sonarsource.com/sonarqube-server/server-installation/on-kubernetes-or-openshift/customizing-helm-chart "mention") (Developer and Enterprise Editions)
* [customizing-helm-chart](https://docs.sonarsource.com/sonarqube-server/server-installation/data-center-edition/on-kubernetes-or-openshift/customizing-helm-chart "mention") (Data Center Edition)
