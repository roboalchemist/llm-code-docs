# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/server-installation/system-properties/dce-specific.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/server-installation/system-properties/dce-specific.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/server-installation/system-properties/dce-specific.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/server-installation/system-properties/dce-specific.md

# Source: https://docs.sonarsource.com/sonarqube-server/server-installation/system-properties/dce-specific.md

# List of DCE-specific properties

SonarQube utilizes system properties during startup, which are not stored in the database. This page lists the configurable system properties that are specific to the Data Center Edition.

### General <a href="#general" id="general"></a>

<details>

<summary>All nodes</summary>

<table><thead><tr><th width="195.2109375">System property (sonar property and ENVIRONMENT_VARIABLE)</th><th width="390.7578125">Description</th><th>Required</th></tr></thead><tbody><tr><td><code>sonar.cluster.enabled</code></td><td><p>Enables the cluster mode. Must be set to true in each node.</p><p><strong>Default value</strong>: false</p></td><td>yes</td></tr><tr><td><p><code>sonar.cluster.name</code></p><p><code>SONAR_CLUSTER_NAME</code></p></td><td><p>The name of the cluster. <strong>Required if multiple clusters are present on the same network.</strong> For example, this prevents mixing Production and Preproduction clusters.</p><p>Will be the name stored in the Hazelcast cluster and used as the name of the Elasticsearch cluster.</p><p><strong>Default value:</strong> sonarqube</p></td><td>Where appropriate</td></tr><tr><td><p><code>sonar.cluster.node.name</code></p><p><code>SONAR_CLUSTER_NODE_NAME</code></p></td><td><p>The name of the node that is used on Elasticsearch and stored in Hazelcast member attribute (NODE_NAME) for sonar-application.</p><p><strong>Default value:</strong> sonarqube-&#x3C;UUID></p></td><td>yes</td></tr><tr><td><p><code>sonar.cluster.node.type</code></p><p><code>SONAR_CLUSTER_NODE_TYPE</code></p></td><td><p>Type of node.</p><p><strong>Possible values:</strong></p><p>• application: node hosting the WebServer process.</p><p>• search: node hosting the Elasticsearch process.</p></td><td>yes</td></tr></tbody></table>

</details>

<details>

<summary>Application nodes only</summary>

<table><thead><tr><th width="215.875">System property (sonar property and ENVIRONMENT_VARIABLE)</th><th width="398.78515625">Description</th><th>Required</th></tr></thead><tbody><tr><td><p><code>sonar.cluster.hosts</code></p><p><code>SONAR_CLUSTER_HOSTS</code></p></td><td><p>Comma-delimited list of all application nodes in the cluster.</p><p><strong>List item format</strong> (the same format for all items):</p><p>• Either &#x3C;nodeIpAddress> (if all ports have the <code>sonar.cluster.node.port</code> default value)</p><p>• Or &#x3C;nodeIpAddress>:&#x3C;ApplicationPortNumber></p></td><td>yes</td></tr><tr><td><code>sonar.cluster.node.host</code></td><td>IP address of the current node used by Hazelcast to communicate with the node.</td><td>yes</td></tr><tr><td><p><code>sonar.cluster.node.port</code></p><p><code>SONAR_CLUSTER_NODE_PORT</code></p></td><td><p>Port of the current node used by Hazelcast to communicate with the node.</p><p><strong>Default value:</strong> 9003</p></td><td>yes</td></tr><tr><td><code>sonar.cluster.node.web.port</code></td><td><p>Port of the current node used by Hazelcast to communicate with the WebServer process on the current node. Port must be accessible to all other application nodes. </p><p>If not specified, a dynamic port will be chosen. In that case, all ports must be open among the nodes to ensure inter-node communication.</p></td><td>no</td></tr><tr><td><code>sonar.cluster.node.ce.port</code></td><td><p>Port of the current node used by Hazelcast to communicate with the Compute Engine process on the current node. Port must be accessible to all other application nodes. </p><p>If not specified, a dynamic port will be chosen. In that case, all ports must be open among the nodes to ensure inter-node communication. </p></td><td>no</td></tr><tr><td><p><code>sonar.cluster.search.hosts</code></p><p><code>SONAR_CLUSTER_SEARCH_HOSTS</code></p></td><td><p>Comma-delimited list of search nodes in the cluster. A search node is described through the IP address and port used for search requests.</p><p><strong>List item format</strong> (the same format for all items):</p><p>• Either &#x3C;nodeIpAddress> (if all ports have the <code>sonar.cluster.node.port default</code> value and this value has not been overridden in the current node’s configuration file)</p><p>• Or &#x3C;nodeIpAddress>:&#x3C;searchPortNumber></p><p><code>&#x3C;nodeIpAddress></code> can also be set to the service name of the search containers.</p></td><td>yes</td></tr><tr><td><p><code>sonar.auth.jwtBase64Hs256Secret</code></p><p><code>SONAR_AUTH_JWTBASE64HS256SECRET</code></p></td><td>Required for authentication with multiple web servers. It is used to keep user sessions opened when they are redirected from one web server to another by the load balancer. You must generate a secret for the application nodes (it will be the same for all application nodes).¹</td><td>yes</td></tr></tbody></table>

1\) See [#jwt-token](https://docs.sonarsource.com/sonarqube-server/data-center-edition/pre-installation#jwt-token "mention").

</details>

<details>

<summary>Search nodes only</summary>

<table><thead><tr><th width="214.28125">System property (sonar property and ENVIRONMENT_VARIABLE)</th><th width="404.59375">Description</th><th>Required</th></tr></thead><tbody><tr><td><code>sonar.cluster.node.search.host</code></td><td>Elasticsearch host of the current node used for HTTP communication between search and application nodes. IP must be accessible to all application nodes.</td><td>yes</td></tr><tr><td><code>sonar.cluster.node.search.port</code></td><td>Elasticsearch port of the current node used for HTTP communication between search and application nodes. Port must be accessible to all application nodes.</td><td>yes</td></tr><tr><td><p><code>sonar.cluster.es.hosts</code></p><p><code>SONAR_CLUSTER_ES_HOSTS</code></p></td><td><p>Comma-delimited list of nodes in the Elasticsearch cluster. A node is described through the IP address and port used for internal communication within the Elasticsearch cluster.</p><p><strong>List item format</strong> (the same format for all items):</p><p>• Either &#x3C;nodeIpAddress> (if all ports have the sonar.cluster.node.port default value and this value has not been overridden in the current node’s configuration file)</p><p>• Or &#x3C;nodeIpAddress>:&#x3C;esPortNumber></p></td><td>yes</td></tr><tr><td><code>sonar.cluster.node.es.host</code></td><td>IP address of the current search node used for internal communication within the Elasticsearch cluster. The IP address must be accessible to all other search nodes.</td><td>yes</td></tr><tr><td><code>sonar.cluster.node.es.port</code></td><td>Port of the current search node used for internal communication within the Elasticsearch cluster. The port must be accessible to all other search nodes</td><td>yes</td></tr><tr><td><code>sonar.search.initialStateTimeout</code></td><td><p>The timeout for the Elasticsearch nodes to elect a primary node. The default value will be fine in most cases, but in a situation where startup is failing because of a timeout, this may need to be adjusted.</p><p><strong>Value format</strong>: <code>&#x3C;integer>&#x3C;timeunit></code><br>where<code>&#x3C;timeunit></code> possible values are:</p><p>• ms: milliseconds</p><p>• s: seconds</p><p>• m: minutes</p><p>• h: hours</p><p>• d: days</p><p>• w: weeks</p></td><td>no</td></tr></tbody></table>

</details>

### Elasticsearch authentication <a href="#elasticsearch-authentication" id="elasticsearch-authentication"></a>

See also [elasticsearch-security-features](https://docs.sonarsource.com/sonarqube-server/server-installation/data-center-edition/network-security/elasticsearch-security-features "mention").

<details>

<summary>All nodes</summary>

<table><thead><tr><th width="254.20703125">System property (sonar property and ENVIRONMENT_VARIABLE)</th><th>Description</th></tr></thead><tbody><tr><td><p><code>sonar.cluster.search.password</code></p><p><code>SONAR_CLUSTER_SEARCH_PASSWORD</code></p></td><td>Password for Elasticsearch built-in user (elastic) which will be used on client side (for an application node) or set in Elasticsearch (for a search node). If provided, it enables authentication, and for a search node, the instance will require additional properties to be set. If this property is set, the same value must be used on all nodes of the cluster (application and search nodes).</td></tr></tbody></table>

</details>

<details>

<summary>Search nodes</summary>

<table><thead><tr><th width="313.79296875">System property (sonar property and ENVIRONMENT_VARIABLE)</th><th>Description</th></tr></thead><tbody><tr><td><p><code>sonar.cluster.es.ssl.keystore</code></p><p><code>SONAR_CLUSTER_ES_SSL_KEYSTORE</code></p></td><td><p>File path to a keystore in PKCS#12 format¹. The user running SonarQube must have READ permission to that file. Required if password provided.</p><p>Can be the same PKCS#12 container as the <code>SONAR_CLUSTER_ES_SSL_TRUSTSTORE</code>.</p></td></tr><tr><td><p><code>sonar.cluster.es.ssl.truststore</code></p><p><code>SONAR_CLUSTER_ES_SSL_TRUSTSTORE</code></p></td><td><p>File path to a truststore in PKCS#12 format¹. The user running SonarQube must have READ permission to that file. Required if password provided.</p><p>Can be the same PKCS#12 container as the <code>SONAR_CLUSTER_ES_SSL_KEYSTORE</code>.</p></td></tr><tr><td><p><code>sonar.cluster.es.ssl.keystorePassword</code></p><p><code>SONAR_CLUSTER_ES_SSL_KEYSTOREPASSWORD</code></p></td><td>Password to the keystore.</td></tr><tr><td><p><code>sonar.cluster.es.ssl.truststorePassword</code></p><p><code>SONAR_CLUSTER_ES_SSL_TRUSTSTOREPASSWORD</code></p></td><td>Password to the truststore.</td></tr></tbody></table>

1\) When creating the PKCS#12 container, make sure it is created with an algorithm that is readable by Java 17.

</details>

### TLS encryption <a href="#tls-encryption" id="tls-encryption"></a>

See also [#tls-encryption](https://docs.sonarsource.com/sonarqube-server/data-center-edition/network-security/elasticsearch-security-features#tls-encryption "mention").

<details>

<summary>All nodes</summary>

<table><thead><tr><th width="317.109375">System property (sonar property and ENVIRONMENT_VARIABLE)</th><th>Description</th></tr></thead><tbody><tr><td><p><code>sonar.cluster.es.http.ssl.keystore</code></p><p><code>SONAR_CLUSTER_ES_HTTP_SSL_KEYSTORE</code></p></td><td>File path to a keystore in PKCS#12 format¹. The user running SonarQube must have READ permission to that file. If provided, it enables TLS encryption.</td></tr><tr><td><p><code>sonar.cluster.es.http.ssl.keystorePassword</code></p><p><code>SONAR_CLUSTER_ES_HTTP_SSL_KEYSTOREPASSWORD</code></p></td><td>Password to the keystore.</td></tr></tbody></table>

1\) When creating the PKCS#12 container, make sure it is created with an algorithm that is readable by Java 17.

</details>

### Related pages <a href="#related-pages" id="related-pages"></a>

* [configuration-methods](https://docs.sonarsource.com/sonarqube-server/server-installation/system-properties/configuration-methods "mention")
* [common-properties](https://docs.sonarsource.com/sonarqube-server/server-installation/system-properties/common-properties "mention")
