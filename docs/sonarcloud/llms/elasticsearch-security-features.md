# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/server-installation/data-center-edition/network-security/elasticsearch-security-features.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/server-installation/data-center-edition/network-security/elasticsearch-security-features.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/server-installation/data-center-edition/network-security/elasticsearch-security-features.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/server-installation/data-center-edition/network-security/elasticsearch-security-features.md

# Source: https://docs.sonarsource.com/sonarqube-server/server-installation/data-center-edition/network-security/elasticsearch-security-features.md

# Elasticsearch security features

### Setting up Elasticsearch authentication <a href="#elasticsearch-authentication" id="elasticsearch-authentication"></a>

Elasticsearch authentication involves verifying the identity of users and systems before granting access to Elasticsearch. You can use TLS for Elasticsearch authentication.To do so, you need to configure both the search nodes (Elasticsearch nodes) and the application nodes (clients) to use TLS/SSL for communication and ensure they have valid certificates. This involves setting up a Certificate Authority (CA), generating a certificate and configuring Elasticsearch to use this certificate for authentication.

#### Step 1: Generate the CA and certificate <a href="#step-1-generate-the-ca-and-certificate" id="step-1-generate-the-ca-and-certificate"></a>

You must generate a Certificate Authority together with a certificate and private key. Generate only one certificate for all nodes.

You can use the elasticsearch-certutil tool to generate both the [Certificate Authority](https://www.elastic.co/guide/en/elasticsearch/reference/current/security-basic-setup.html#generate-certificates) and the [certificate](https://www.elastic.co/guide/en/elasticsearch/reference/current/security-basic-setup-https.html#encrypt-http-communication) (see [the Elastic documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/security-basic-setup-https.html)):

* Make sure you include all the search nodes’ hostnames. They will be then added as DNS names in the Subject Alternative Name. See the example below.
* Choose the password that will be assigned to `searchNodes.searchAuthentication.userPassword`. This is optional in a Kubernetes installation unless you are not using `searchAuthentication`. If you are using `searchAuthentication` and do not define a password in your helm chart, the system will fail.
* As a result of the certificate creation process, you should get a file called `http.p12`. Rename it to `elastic-stack-ca.p12`

{% hint style="warning" %}
When creating the PKCS#12 container, make sure it is created with an algorithm that is readable by Java 17.
{% endhint %}

<details>

<summary>DNS names list example</summary>

As an example, let’s assume that your cluster has three search nodes with the release’s name set to "sq", the chart’s name set to "sonarqube-dce", and the namespace set to "sonar". You will need to add the following DNS names in the SAN.

`sq-sonarqube-dce-search-0.sq-sonarqube-dce-search.sonar.svc.cluster.local`

`sq-sonarqube-dce-search-1.sq-sonarqube-dce-search.sonar.svc.cluster.local`

`sq-sonarqube-dce-search-2.sq-sonarqube-dce-search.sonar.svc.cluster.local`

`sq-sonarqube-dce-search`

Remember to add the service name in the list (in this case, sq-sonarqube-dce-search).

Note that you can retrieve the search nodes’ FQDN running hostname -f within one of the node.

</details>

#### Step 2: Configure the authentication in SonarQube <a href="#step-2-configure-the-authentication-in-sonarqube" id="step-2-configure-the-authentication-in-sonarqube"></a>

You must restart the cluster to apply the changes.

{% tabs %}
{% tab title="ZIP OR DOCKER INSTALLATION" %}

1. On each application node and on each search node, enable the authentication to the Elasticsearch cluster by setting the Elasticsearch password in the system property `sonar.cluster.search.password` or the corresponding environment variable `SONAR_CLUSTER_SEARCH_PASSWORD`. It must have the exact same value on all nodes.
2. On each search node, set the path to `elastic-stack-ca.p12` in the following system properties:
   * `sonar.cluster.es.ssl.keystore` / `SONAR_CLUSTER_ES_SSL_KEYSTORE`
   * `sonar.cluster.es.ssl.truststore` / `SONAR_CLUSTER_ES_SSL_TRUSTSTORE`
3. On each search node, set the keystore / truststore password in the following system properties:
   * `sonar.cluster.es.ssl.keystorePassword` / `SONAR_CLUSTER_ES_SSL_KEYSTOREPASSWORD`
   * `sonar.cluster.es.ssl.truststorePassword` / `SONAR_CLUSTER_ES_SSL_TRUSTSTOREPASSWORD`

For information about the system properties, see [#elasticsearch-authentication](https://docs.sonarsource.com/sonarqube-server/system-properties/dce-specific#elasticsearch-authentication "mention").
{% endtab %}

{% tab title="KUBERNETES INSTALLATION" %}
In the Helm chart:

1. Set `searchNodes.searchAuthentication.enabled` to `true`.
2. Create the secret that will contain the certificate and assign its name to the `searchNodes.searchAuthentication.keyStoreSecret` parameter.
3. If you chose a password in the certificate generation process, set the `keyStorePassword` or `keyStorePasswordSecret` values with that password value.
   {% endtab %}
   {% endtabs %}

### Setting up TLS encryption <a href="#tls-encryption" id="tls-encryption"></a>

TLS encryption is used to secure the HTTP traffic between clients (application nodes) and Elasticsearch (search nodes). If Elasticsearch authentication is enabled, you can set up TLS encryption.

You must restart the cluster to apply the changes.

{% tabs %}
{% tab title="ZIP OR DOCKER INSTALLATION" %}
On each application node and each search node, set the path to `elastic-stack-ca.p12` in the following system properties:

* `sonar.cluster.es.http.ssl.keystore` / `SONAR_CLUSTER_ES_HTTP_SSL_KEYSTORE`
* `sonar.cluster.es.http.ssl.keystorePassword` / `SONAR_CLUSTER_ES_HTTP_SSL_KEYSTOREPASSWORD`

For information about the properties, see [#tls-encryption](https://docs.sonarsource.com/sonarqube-server/system-properties/dce-specific#tls-encryption "mention").
{% endtab %}

{% tab title="KUBERNETES INSTALLATION" %}

* Set `nodeEncryption.enabled` to `true`.
  {% endtab %}
  {% endtabs %}

### Related pages <a href="#related-pages" id="related-pages"></a>

* [securing-behind-proxy](https://docs.sonarsource.com/sonarqube-server/server-installation/data-center-edition/network-security/securing-behind-proxy "mention")
* [network-rules](https://docs.sonarsource.com/sonarqube-server/server-installation/data-center-edition/network-security/network-rules "mention")
