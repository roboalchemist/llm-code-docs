# Source: https://docs.sonarsource.com/sonarqube-community-build/server-installation/on-kubernetes-or-openshift/customizing-helm-chart.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/setup-and-upgrade/deploy-on-kubernetes/server/customizing-helm-chart.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/setup-and-upgrade/deploy-on-kubernetes/dce/customizing-helm-chart.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/setup-and-upgrade/deploy-on-kubernetes/server/customizing-helm-chart.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/setup-and-update/deploy-on-kubernetes/dce/customizing-helm-chart.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/setup-and-update/deploy-on-kubernetes/server/customizing-helm-chart.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/server-installation/data-center-edition/on-kubernetes-or-openshift/customizing-helm-chart.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/server-installation/on-kubernetes-or-openshift/customizing-helm-chart.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/server-installation/data-center-edition/on-kubernetes-or-openshift/customizing-helm-chart.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/server-installation/on-kubernetes-or-openshift/customizing-helm-chart.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/setup-and-upgrade/deploy-on-kubernetes/dce/customizing-helm-chart.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/setup-and-upgrade/deploy-on-kubernetes/server/customizing-helm-chart.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/server-installation/data-center-edition/on-kubernetes-or-openshift/customizing-helm-chart.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/server-installation/on-kubernetes-or-openshift/customizing-helm-chart.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/server-installation/data-center-edition/on-kubernetes-or-openshift/customizing-helm-chart.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/server-installation/on-kubernetes-or-openshift/customizing-helm-chart.md

# Source: https://docs.sonarsource.com/sonarqube-server/server-installation/data-center-edition/on-kubernetes-or-openshift/customizing-helm-chart.md

# Source: https://docs.sonarsource.com/sonarqube-server/server-installation/on-kubernetes-or-openshift/customizing-helm-chart.md

# Customizing Helm chart

While we only document the most pressing SonarQube Server Helm chart customizations in this documentation, there are other possibilities for you to choose to customize the chart before installing. Please see the [Helm chart README file](https://artifacthub.io/packages/helm/sonarqube/sonarqube) for more information on these. In particular, see the recommended production use case values.

You can customize the SonarQube Server Helm chart:

* By editing the default values in the `values.yaml` file.
* Or directly in the Helm chart installation command line, see [installing-helm-chart](https://docs.sonarsource.com/sonarqube-server/server-installation/on-kubernetes-or-openshift/installing-helm-chart "mention").

Parameters passed in the command line have precedence over parameters set in `values.yaml`.

{% hint style="info" %}
To set up SonarQube Server monitoring, see [set-up-monitoring](https://docs.sonarsource.com/sonarqube-server/server-installation/on-kubernetes-or-openshift/set-up-monitoring "mention").
{% endhint %}

### Enabling OpenShift <a href="#enabling-openshift" id="enabling-openshift"></a>

If you want to install SonarQube Server on OpenShift, you must enable OpenShift in the Helm chart. In that case:

* The Helm chart will auto-configure itself to comply with the default OpenShift [SCCs](https://docs.openshift.com/container-platform/3.11/admin_guide/manage_scc.html) (Security Context Constraints).
* Not using a default SCC in your OpenShift cluster may cause problems.

To enable OpenShift in the Helm chart:

1. Set `OpenShift.enabled` to `true`.
2. Set `OpenShift.createSCC` to `false`.
3. If you want to make your application publicly visible with Routes, you can set `route.enabled` to `true`. Please check the [configuration details](https://artifacthub.io/packages/helm/sonarqube/sonarqube#openshift) in the Helm chart documentation to customize the Route based on your needs.

### Ensuring a restricted security level <a href="#ensuring-restricted-level" id="ensuring-restricted-level"></a>

<details>

<summary>About the Pod security level</summary>

Below is the [Pod security level](https://kubernetes.io/docs/concepts/security/pod-security-admission/#pod-security-levels) applied by default to each container. To apply a security level, a default `SecurityContext` is set on the container through the SonarQube Server Helm chart.

| **Container**                           | **Pod security level** | **Note**                                                                                                                 |
| --------------------------------------- | ---------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| SonarQube Server application containers | restricted             | <p><br></p>                                                                                                              |
| SonarQube Server init containers        | restricted             | <p><br></p>                                                                                                              |
| init-sysctl                             | privileged             | <p>Utility software that requires root access.</p><p><br></p>                                                            |
| init-fs                                 | baseline               | Utility software that requires root access. To disable the container, set `initFs.enabled` in the Helm chart to `false`. |

The `SecurityContext` below is set as default on all restricted containers.

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

</details>

<details>

<summary>In a Kubernetes installation</summary>

To run the SonarQube Server Helm chart in a full restricted namespace, you must disable the `init-sysctl` and `init-fs` containers by setting in the Helm chart:

* `initSysctl.enabled` to `false`.
* `initFs.enabled` to `false`.

Since these containers are used to perform some settings at the host/kernel level, disabling them may require additional configuration steps. For more information, see [Elasticsearch prerequisites](https://artifacthub.io/packages/helm/sonarqube/sonarqube#elasticsearch-prerequisites) in the Helm chart documentation.

</details>

<details>

<summary>In an OpenShift installation</summary>

The configuration described in [#enabling-openshift](#enabling-openshift "mention") above forces the disabling of the `init-sysctl` and `init-fs` containers. These containers should not be required in the vast majority of cases for an Openshift installation. Therefore, an Openshift installation is compatible with restricted SCCv2 (Security Context Constraints).

</details>

### Setting access to your external database <a href="#access-to-database" id="access-to-database"></a>

You must configure the access to your database (except if you want to use SonarQube for test purposes and want to use the embedded database H2).

To do so:

1. Set `jdbcOverwrite.enabled` to `true`.
2. Set `jdbcOverwrite.jdbcUrl` to the database URL and `jdbcOverwrite.jdbcUsername` to the database username.
3. Store the database password in a Kubernetes secret and set `jdbcOverwrite.jdbcSecretName` to the secret’s name.
4. If you use an Oracle database:
   * Let the Helm chart download and inject the corresponding JDBC driver in SonarQube by setting `jdbcOverwrite.oracleJdbcDriver.url` to the URL of the Oracle JDBC driver to be downloaded.
   * In case the download requires it, set `jdbcOverwrite.oracleJdbcDriver.netrcCreds` to the name of the Kubernetes secret containing the `.netrc` file that stores the credentials.

For more information, see this [section](https://artifacthub.io/packages/helm/sonarqube/sonarqube#jdbc-overwrite) in the ArtifactHub page of the Helm Chart.

### Enabling persistency in Elasticsearch <a href="#enabling-es-persistency" id="enabling-es-persistency"></a>

SonarQube Server comes with a bundled Elasticsearch, and as Elasticsearch is stateful, so is SonarQube Server. There is an option to persist the Elasticsearch indexes in a Persistent Volume, but with regular stoppage operations by the Kubernetes Cluster, these indexes can be corrupted. By default, persistency is disabled in the Helm chart.

Enabling persistency decreases the startup time of the SonarQube Server Pod significantly, but you are risking corrupting your Elasticsearch index. You can enable persistency by adding the following to the `values.yaml`:

```css-79elbk
persistence:
  enabled: true
```

Leaving persistency disabled results in a longer startup time until SonarQube Server is fully available, but you won’t lose any data as SonarQube Server will persist all data in the database.

### Using custom certificates for your code repository <a href="#custom-certificates" id="custom-certificates"></a>

When you are working with your own Certificate Authority or in an environment that uses self-signed certificates for your code repository platform, you can create a secret containing this certificate and add this certificate to the Java truststore inside the SonarQube deployment.

To add a certificate to the Javatrustore inside the SonarQube deployment:

1. Ask the relevant team to provide you with a PEM format certificate or certificate chain. We will assume it to be called `cert.pem` on the following commands.
2. Generate the kubernetes secret, e.g. with this command:

```bash
kubectl create secret generic --from-file cert.pem <secretName> -n  <sonarqubeNamespace>
```

The generated secret should then appear in this format and the certificate should contain the full chain:

```
apiVersion: v1
data:
  sonar.crt: <base64 encoded certificate>
kind: Secret
metadata:
  name: <secretName>
  namespace: sq
type: Opaque
```

3\. In SonarQube’s `value.yaml` file, add:

```yaml
caCerts:
  enabled: true
  secret: <secretName>
```

### Creating an Ingress to make SonarQube Server service accessible from outside <a href="#ingress" id="ingress"></a>

To make the SonarQube Server service accessible from outside of your cluster, you most likely need an Ingress.

{% hint style="info" %}
The Sonar Helm chart has an optional dependency on the [NGINX Ingress Helm chart](https://kubernetes.github.io/ingress-nginx) which installs the NGINX Ingress controller (To install the NGINX Ingress Helm chart through SonarQube Server Helm chart, set `ingress-nginx.enabled` to `true` in SonarQube Server’s `values.yaml`.) You should use it only in a test environment. In a production environment, it’s highly recommended that you use your own Ingress controller since the controller is a critical part of the software chain.
{% endhint %}

To create an Ingress resource through the Helm chart:

* Add the following to your SonarQube Server’s `values.yaml`. In this configuration, we use the Ingress class NGINX with a body size of at least 64MB since this is what we recommend.

```yaml
ingress:
  enabled: true
  # Used to create an Ingress record.
  hosts:
    - name: <Your SonarQube Server's FQDN>
      # Different clouds or configurations might need /* as the default path
      path: /
      # For additional control over serviceName and servicePort
      # serviceName: someService
      # servicePort: somePort
  annotations: 
    nginx.ingress.kubernetes.io/proxy-body-size: "64m"
```

#### Deprecation of Ingress NGINX

Due to the retirement of the ingress-nginx controller in November 2025 (with best-effort support ceasing in March 2026), the dependency on this chart is now deprecated.

We advise migrating to the [Gateway API](https://gateway-api.sigs.k8s.io/guides/), which is the modern successor to Ingress. Should you need to continue using Ingress, consult the [Kubernetes documentation](https://kubernetes.io/docs/concepts/services-networking/ingress-controllers/) for a list of suitable alternative controllers. A replacement dependency will be provided in a future release.

### Related pages <a href="#related-pages" id="related-pages"></a>

* [installation-overview](https://docs.sonarsource.com/sonarqube-server/server-installation/on-kubernetes-or-openshift/installation-overview "mention")
* [before-you-start](https://docs.sonarsource.com/sonarqube-server/server-installation/on-kubernetes-or-openshift/before-you-start "mention")
* [installing-helm-chart](https://docs.sonarsource.com/sonarqube-server/server-installation/on-kubernetes-or-openshift/installing-helm-chart "mention")
* [set-up-monitoring](https://docs.sonarsource.com/sonarqube-server/server-installation/on-kubernetes-or-openshift/set-up-monitoring "mention")
* Installing Data Center Edition on Kubernetes: [on-kubernetes-or-openshift](https://docs.sonarsource.com/sonarqube-server/server-installation/data-center-edition/on-kubernetes-or-openshift "mention")
