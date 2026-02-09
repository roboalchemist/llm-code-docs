# Source: https://docs.sonarsource.com/sonarqube-community-build/server-installation/system-properties/configuration-methods.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/server-installation/system-properties/configuration-methods.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/server-installation/system-properties/configuration-methods.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/server-installation/system-properties/configuration-methods.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/server-installation/system-properties/configuration-methods.md

# Source: https://docs.sonarsource.com/sonarqube-server/server-installation/system-properties/configuration-methods.md

# Configuration methods

SonarQube utilizes system properties during startup, which are not stored in the database. These properties can be configured through:

* `sonar.properties` configuration file\
  You can define system properties through sonar properties (`sonar.*`) stored in the `sonar.properties` file.
* Environment variables\
  You can define system properties through environment variables.
* Command line\
  You can define system properties in the command line used to start SonarQube.

The properties set through the command line have precedence over the environment variables which have precedence over the `sonar.properties` file.

See the list of sonar properties considered as system properties, along with the corresponding environment variables:

* [common-properties](https://docs.sonarsource.com/sonarqube-server/server-installation/system-properties/common-properties "mention")
* [dce-specific](https://docs.sonarsource.com/sonarqube-server/server-installation/system-properties/dce-specific "mention")

{% hint style="info" %}
Once you have set or changed system properties, you must restart SonarQube to apply the changes.
{% endhint %}

### In a ZIP installation <a href="#zip" id="zip"></a>

The preferred method to manage system properties in a ZIP installation is to edit the `sonar.properties` file which is stored in `<sonarqubeHome>/conf/sonar.properties` where `<sonarqubeHome>` is the location where the SonarQube Server distribution has been unzipped.

To encrypt sensitive system properties stored in `sonar.properties`, see [encrypting-settings](https://docs.sonarsource.com/sonarqube-server/instance-administration/security/encrypting-settings "mention").

{% hint style="info" %}
The `sonar.properties` file also accepts a restricted list of non-system properties. Currently, if you use a non-supported property, SonarQube will ignore it and no error or warning will be raised. As a principle, use only properties documented in the `sonar.properties` file or explicitly authorized in the SonarQube documentation.
{% endhint %}

### In a Docker installation <a href="#docker" id="docker"></a>

The preferred method to manage system properties in a Docker installation is to use the environment variables.

System properties can also be edited in the `sonar.properties` file which is stored in `<sonarqubeHome>/conf/sonar.properties` where `<sonarqubeHome>` is the installation directory of SonarQube Server within your container. This path is stored in the `SONARQUBE_HOME` environment variable.

### In a Kubernetes installation <a href="#kubernetes" id="kubernetes"></a>

In a Kubernetes installation, a few system properties are set through Helm chart parameters. For example, the Helm chart’s parameter `jdbcOverwrite.jdbcUrl` corresponds to the sonar property `sonar.jdbc.url`.

If you need to set additional system properties, you can set them in the Helm chart through:

* Sonar properties
* Environment variables

In addition, system properties stored in external Secrets or ConfigMaps can be injected into the Helm chart.

#### Defining sonar properties <a href="#defining-sonar-properties" id="defining-sonar-properties"></a>

In the SonarQube Helm chart (`values.yaml` file), use the `sonarProperties` parameter as illustrated below. This creates a custom `sonar.properties` file within the Kubernetes cluster.

```yaml
sonarProperties:
   sonar.log.level: DEBUG
   sonar.security.realm: LDAP
   ldap.url: ldaps://organization.com
```

To encrypt sensitive properties stored in the Helm chart, see [encrypting-helm-chart-sensitive-data](https://docs.sonarsource.com/sonarqube-server/server-installation/on-kubernetes-or-openshift/encrypting-helm-chart-sensitive-data "mention").

{% hint style="info" %}
Only system properties can be defined through `sonarProperties` in the Helm chart. Non-system properties will be ignored.
{% endhint %}

#### Using environment variables <a href="#using-environment-variables" id="using-environment-variables"></a>

In the Helm chart, you can define system properties through environment variables by using `env:`.

#### Injecting external Secrets or ConfigMaps <a href="#injecting-external-secrets-or-configmaps" id="injecting-external-secrets-or-configmaps"></a>

In environments where another tool, such as terraform or ansible, is used to provision infrastructure or passwords, configuration may be read, via environment variables, from existing Secrets and ConfigMaps.

To do so, proceed as follows:

1\. Create a `ConfigMap` (or `Secret`) containing key/value pairs, as expected by SonarQube.

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: external-sonarqube-opts
data:
  SONAR_JDBC_USERNAME: foo
  SONAR_JDBC_URL: jdbc:postgresql://db.example.com:5432/sonar
```

2\. Set the following in your `values.yaml` (using the key `extraConfig.secrets` to reference Secrets)

```yaml
extraConfig:
  configmaps:
    - external-sonarqube-opts
```

### Related pages <a href="#related-pages" id="related-pages"></a>

* [common-properties](https://docs.sonarsource.com/sonarqube-server/server-installation/system-properties/common-properties "mention")
* [dce-specific](https://docs.sonarsource.com/sonarqube-server/server-installation/system-properties/dce-specific "mention")
