# Source: https://docs.sonarsource.com/sonarqube-server/10.3/setup-and-upgrade/install-the-server/advanced-installation-features.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.4/setup-and-upgrade/install-the-server/advanced-installation-features.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.5/setup-and-upgrade/install-the-server/advanced-installation-features.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.6/setup-and-upgrade/install-the-server/advanced-installation-features.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/setup-and-upgrade/install-the-server/advanced-installation-features.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/setup-and-upgrade/install-the-server/advanced-installation-features.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/setup-and-update/install-the-server/advanced-installation-features.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/setup-and-upgrade/install-the-server/advanced-installation-features.md

# Advanced installation

This section explains how to:

* Change the web server connection parameters
* Modify the default configuration of the server installation

You can also:

* In case of a ZIP installation: run SonarQube Server as a service on Windows or Linux. See [#running-sonarqube-as-a-service-on-windows](https://docs.sonarsource.com/sonarqube-server/2025.1/operating-the-server#running-sonarqube-as-a-service-on-windows "mention").
* Run SonarQube Server behind a proxy. See [#securing-the-server-behind-a-proxy](https://docs.sonarsource.com/sonarqube-server/2025.1/operating-the-server#securing-the-server-behind-a-proxy "mention") [operating-the-server](https://docs.sonarsource.com/sonarqube-server/2025.1/setup-and-upgrade/operating-the-server "mention")
* Monitor and adjust Java process memory. See [#java-process-memory](https://docs.sonarsource.com/sonarqube-server/2025.1/server-update-and-maintenance/monitoring/instance#java-process-memory "mention").
* Install a plugin. See [install-a-plugin](https://docs.sonarsource.com/sonarqube-server/2025.1/setup-and-upgrade/plugins/install-a-plugin "mention").

### Changing the web server connection parameters <a href="#change-server-connection-parameters" id="change-server-connection-parameters"></a>

To set up the web server connection:

* For a server installation from the ZIP file: Verify and change if necessary the following properties in the SonarQube Server configuration file (`<sonarqubeHome>/conf/sonar.properties`).
* For a server installation from the Docker image: Verify and change if necessary the following environment variables.

<table><thead><tr><th width="158">Property (ZIP installation)</th><th width="182">Environment variable (Docker installation)</th><th>Description</th></tr></thead><tbody><tr><td>sonar.web.host</td><td>SONAR_WEB_HOST</td><td><p>For servers with more than one IP address, this property specifies which address will be used for listening on the specified ports.</p><p><strong>Default value</strong>: 0.0.0.0 (ports will be used on all IP addresses associated with the server)</p></td></tr><tr><td>sonar.web.port</td><td>SONAR_WEB_PORT</td><td><p>TCP port for incoming HTTP connections.</p><p><strong>Default value</strong>: 9000</p></td></tr><tr><td>sonar.web.context</td><td>SONAR_WEB_CONTEXT</td><td><p>Web context specifying the path at which to serve SonarQube Server. For example, with <code>sonar.web.port=9000</code> and <code>sonar.web.context=/sonarqube</code>, you will access the web interface at http://localhost:9000/sonarqube.</p><p><strong>Example</strong>: <code>/sonarqube</code> (must start with a forward slash)</p><p><strong>Default value</strong>: empty (root context)</p></td></tr></tbody></table>

### Modifying the default configuration of a server installation <a href="#modify-default-config" id="modify-default-config"></a>

To modify the default configuration:

* For a server installation from the ZIP file: Change the sonar properties in the SonarQube Server configuration file (`<sonarqubeHome>/conf/sonar.properties`).
* For a server installation from the Docker image: Change the sonar environment variables. See [environment-variables](https://docs.sonarsource.com/sonarqube-server/2025.1/setup-and-upgrade/environment-variables "mention").

### Self Signed Certificates of DevOps platforms <a href="#selfsigned-certificates" id="selfsigned-certificates"></a>

When running in an environment where the DevOps platform or other related tooling is secured by self-signed certificates, the CA needs to be added to the Java truststore of SonarQube Server.

In a zip installation, the systems truststore can be found in `$JAVA_HOME/lib/security/cacerts`. In order to add a new certificate to the truststore you can use the following command as an example:

```css-79elbk
keytool -importcert -file $PATH_TO_CERTIFICATE -alias $CERTIFICATE_NAME -keystore /$JAVA_HOME/lib/security/cacerts -storepass changeit -trustcacerts -noprompt
```

In our official Docker images, you can find the systems truststore in `<JAVA_HOME>/lib/security/cacerts`. In order to add new certificates here as well you can:

* Bind mount an existing truststore containing your certificates to `<JAVA_HOME>/lib/security/cacerts`.

<details>

<summary>Example</summary>

```css-79elbk
docker run -d --name sonarqube -v /path/to/your/cacerts.truststore:/opt/java/openjdk/lib/security/cacerts:ro -p 9000:9000 sonarqube 
```

</details>

* Import your CA certificate the same way as in the zip installation but inside the container.

If you deploy SonarQube Server on Kubernetes using the official Helm Chart, you can create a new secret containing your required certificates and reference this via:

```css-79elbk
caCerts:
  enabled: true
  image: adoptopenjdk/openjdk17:alpine
  secret: your-secret
```

### SonarQube Server DNS cache <a href="#dns-cache" id="dns-cache"></a>

When reporting Quality Gate status to DevOps platforms, SonarQube Server uses a DNS cache time to live policy of 30 seconds. If necessary, you can change this setting in your JVM:

```css-79elbk
echo "networkaddress.cache.ttl=5" >> "${JAVA_HOME}/conf/security/java.security" 
```

Please be aware that low values increase the risk of DNS spoofing attacks.
