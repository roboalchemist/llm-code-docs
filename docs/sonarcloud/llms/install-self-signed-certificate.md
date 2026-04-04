# Source: https://docs.sonarsource.com/sonarqube-server/10.4/analyzing-source-code/scanner-environment/install-self-signed-certificate.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.5/analyzing-source-code/scanner-environment/install-self-signed-certificate.md

# Managing TLS certificates on client side

If your SonarQube server is [#securing-the-server-behind-a-proxy](https://docs.sonarsource.com/sonarqube-server/10.5/setup-and-upgrade/configure-and-operate-a-server/operating-the-server#securing-the-server-behind-a-proxy "mention") and a self-signed certificate then you must add the self-signed certificate to the trusted CA certificates of the SonarScanner.

In addition, if mutual TLS is used then you must define the access to the client certificate at the SonarScanner level.

### Managing the self-signed server certificate <a href="#self-signed-server-certificate" id="self-signed-server-certificate"></a>

#### Introduction to server authentication <a href="#introduction-to-server-authentication" id="introduction-to-server-authentication"></a>

During the TLS authentication of the server, the client requests the server certificate from the server and verifies that this certificate is signed by a CA it trusts by checking its truststore. In case a self-signed server certificate is used, it must be added to the truststore of the client. The figure below shows the certificates involved in the authentication of the SonarQube server by the SonarScanner.

![](https://3691828591-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Feu7dHWcqP9Cr3eUAzwWg%2Fuploads%2Fgit-blob-cf11bf472fb8a0da9bb30e39d32c0701ac8708f1%2F04e98d3c487a19d47fd905fb5a2c32af4f313093.png?alt=media)

#### Adding the self-signed server certificate to the trusted CA certificates <a href="#adding-the-selfsigned-server-certificate-to-the-trusted-ca-certificates" id="adding-the-selfsigned-server-certificate-to-the-trusted-ca-certificates"></a>

<details>

<summary>For SonarScanner for Maven, Gradle, or CLI</summary>

You can either use:

* The default JVM truststore (`\jre\lib\security\cacerts`).\
  To add the self-signed server certificate to the default truststore, use the JVM tool keytool. The instructions depend on your operating system and you will find many resources online, such as [this one](https://www.ibm.com/docs/en/tnpm/1.4.2?topic=security-import-certificate-jre-keystore) for Linux.

  See also: [troubleshooting](https://docs.sonarsource.com/sonarqube-server/10.5/setup-and-upgrade/install-the-server/troubleshooting "mention").
* A custom Java truststore by using the following properties:
  * `javax.net.ssl.trustStore`: path to the truststore file
  * `javax.net.ssl.trustStorePassword:` password to the truststore
  * `javax.net.ssl.trustStoreType`(optional, if the truststore file type is not JKS or PKCS12)

Define the properties by using the SONAR\_SCANNER\_OPTS environment variable.\
Example (on Windows, use forward slashes as path separators): `SONAR_SCANNER_OPTS="-Djavax.net.ssl.trustStore=/repositories/tls-mutual-nginx/cacerts -Djavax.net.ssl.trustStorePassword=changeit"`

</details>

<details>

<summary>For SonarScanner for .NET</summary>

Add the self-signed server certificate to the operating system truststore:

* On Linux and MacOS:
  1. Copy the self-signed server certificate to `/usr/local/share/ca-certificates`
  2. Run `sudo update-ca-certificates`
* On Windows: use [certutil](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/certutil).\
  Example: `certutil -addstore -f "ROOT" <path/to/certificate>`

In addition, since SonarScanner for .NET invokes SonarScanner CLI, you must add the self-signed certificate to the Java truststore as explained above.

</details>

<details>

<summary>If running the scanner with Docker</summary>

If you need to configure a self-signed certificate for the scanner to communicate with your SonarQube instance, you can use a volume under `/tmp/cacerts` to add it to the containers java trust store:

```css-79elbk
docker pull sonarsource/sonar-scanner-cli
docker run \
    --rm \
    -v ${YOUR_CERTS_DIR}/cacerts:/tmp/cacerts \
    -v ${YOUR_CACHE_DIR}:/opt/sonar-scanner/.sonar/cache \
    -v ${YOUR_REPO}:/usr/src \
    -e SONAR_HOST_URL="http://${SONARQUBE_URL}" \
    sonarsource/sonar-scanner-cli
```

Alternatively, you can create your own container that includes the modified `cacerts` file. Create a `Dockerfile` with the following contents:

```css-79elbk
FROM sonarsource/sonar-scanner-cli
COPY cacerts /usr/lib/jvm/default-jvm/jre/lib/security/cacerts
```

Then, assuming both the `cacerts` and `Dockerfile` are in the current directory, create the new image with a command such as:

```css-79elbk
docker build --tag our-custom/sonar-scanner-cli .
```

</details>

### Managing the client certificates <a href="#mutual-tls" id="mutual-tls"></a>

#### Introduction to client authentication <a href="#introduction-to-client-authentication" id="introduction-to-client-authentication"></a>

If mutual TLS is used then both the client and the server authenticate the other party. During the TLS authentication of the client, the client must provide its certificate with the corresponding CA certificate chain (intermediate and root CA certificates) to the server. The client manages its certificates in its own keystore. The figure below shows the certificates involved in the TLS authentication of the SonarScanner by the SonarQube Server.

![](https://3691828591-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Feu7dHWcqP9Cr3eUAzwWg%2Fuploads%2Fgit-blob-f36a72ea9dc0e52af7fbf29bdb5000b23635d04d%2F3374c9d5df12b5eb3aaf5f5aad133c8b8d56a2e7.png?alt=media)

#### Defining the access to the client certificates <a href="#defining-the-access-to-the-client-certificates" id="defining-the-access-to-the-client-certificates"></a>

<details>

<summary>For SonarScanner for Maven, Gradle, or CLI</summary>

Store the client certificate and CA certificate chain in a keystore file and define the access to this file through the following properties:

* `javax.net.ssl.keyStore`: path to the keystore file
* `javax.net.ssl.keyStorePassword`: password of the keystore file
* `javax.net.ssl.keyStoreType` (optional, if the keystore file type is not JKS or PKCS12)

</details>

<details>

<summary>For SonarScanner for .NET</summary>

1. Store the client certificate and CA certificate chain in a keystore file and define the access to this file through the following properties:
   * `sonar.clientcert.path` : path to the keystore file, must be set in the begin step.
   * `sonar.clientcert.password:` password of the keystore file, must be set in both the begin and end steps.
2. In addition, set the following options before the end step (for the SonarScanner CLI invocation):
   * `javax.net.ssl.keyStore`: same value as `sonar.clientcert.path`
   * `javax.net.ssl.keyStorePassword`: same value as `sonar.clientcert.password`

</details>
