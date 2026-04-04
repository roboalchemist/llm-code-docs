# Source: https://docs.sonarsource.com/sonarqube-for-eclipse/connect-your-ide/advanced-configuration.md

# Source: https://docs.sonarsource.com/sonarqube-for-visual-studio/connect-your-ide/advanced-configuration.md

# Source: https://docs.sonarsource.com/sonarqube-for-intellij/connect-your-ide/advanced-configuration.md

# Source: https://docs.sonarsource.com/sonarqube-for-vs-code/connect-your-ide/advanced-configuration.md

# Advanced configuration

### HTTP configuration <a href="#http-configuration" id="http-configuration"></a>

To operate, SonarQube for VS Code needs to perform HTTP requests, especially in [Connected mode](https://app.gitbook.com/s/NvI4wotPmITyM0mnsmtp/connect-your-ide/connected-mode "mention"). While SonarQube for VS Code will work out-of-the-box in most situations, some network infrastructure may require a custom configuration.

### Passing SonarQube for IDE properties <a href="#passing-sonarlint-properties" id="passing-sonarlint-properties"></a>

In SonarQube for VS Code, open the SonarLint extension settings, and add your properties to the **Settings** > **Extensions** > **Sonarlint** > **Ls: Vmargs** JVM arguments.

<div align="left"><figure><img src="https://3457378997-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F6LPRABg3ubAJhpfR5K0Y%2Fuploads%2Fgit-blob-6edb839843055bc43204ada4ec3b670c121c29f9%2Ff4a39225e1c1e3d6c904e89a5fb4553a69c327d6.png?alt=media" alt="You&#x27;ll need to edit the SonarLint Extension setting, LS: Vmargs, to add advanced HTTP properties." width="375"><figcaption></figcaption></figure></div>

### Proxy configuration

To use connected mode with a SonarQube instance running behind a proxy, pass your settings using the JVM arguments as referenced above in [#passing-sonarlint-properties](#passing-sonarlint-properties "mention").

For example, you might add these arguments:

```
{ "sonarlint.ls.vmargs": "-Dhttps.proxyHost=<YourProxy.company.tld> -Dhttps.proxyPort=8080 -Dhttps.nonProxyHosts=localhost|127.0.0.1|<YourIntranet.company.tld>" }
```

### Manage your configuration <a href="#manage-your-configuration" id="manage-your-configuration"></a>

#### HTTP Client timeouts <a href="#http-client-timeouts" id="http-client-timeouts"></a>

SonarQube for IDE supports various timeouts. Below you will find the properties added to control them:

`sonarlint.http.connectTimeout`

* Determines the timeout, in minutes, until a new connection is fully established.
* **Default**: 1 min

`sonarlint.http.socketTimeout`

* Determines the default socket timeout value, in minutes, for I/O operations.
* **Default**: infinite

`sonarlint.http.connectionRequestTimeout`

* The connection lease request timeout, in minutes, is used when requesting a connection from the connection manager.
* **Default**: 1 min

`sonarlint.http.responseTimeout`

* Determines the timeout, in minutes, until the arrival of a response from the opposite endpoint.
* **Default**: 10 min

#### Server SSL certificates <a href="#server-ssl-certificates" id="server-ssl-certificates"></a>

SonarQube for IDE manages its own TrustStore in addition to the OS and Java TrustStores. When encountering an untrusted certificate, SonarQube for IDE will ask the user if the certificate should be trusted. If the answer is yes, the certificate will be added to the TrustStore.

SonarQube for IDE depends on you to provide server certificates when required by your environment. Here’s a generalization of a few basic steps you can use to help make that easier. Note that these instructions are for *server SSL certificates*. If you're dealing with a *client SSL certificate*, you'll need to create and configure a "key store" instead.

<details>

<summary>Install a server SSL certificate</summary>

**To install a server SSL certificate**

**Step 1:** Import your certificate into SonarQube for IDE. Here is a common command to import your certificate (`<Your_Certificate>.cer`) into a TrustStore (`C:/<Your_Path_To_Your_Truststore>`):

```bash
keytool -import -keystore C:/<Your_Path_To_Your_Truststore> -storepass password -noprompt -alias sonarqube-ssl -file <Your_Certificate>.cer
```

* Replace `C:/<Your_Path_To_Your_Truststore>` with your desired path and `password` with your chosen TrustStore password.

**Step 2:** Now that you’ve created the file, tell VS Code where to find it by adding these lines to your JVM arguments. See the [#passing-sonarlint-properties](#passing-sonarlint-properties "mention") instructions for more details.

```bash
-Dsonarlint.ssl.trustStorePath=C:/<Your_Path_To_Your_Truststore>

-Dsonarlint.ssl.trustStorePassword=<Your_Password>

-Dsonarlint.ssl.trustStoreType=PKCS12
```

* Check that your path and password match what you used for your TrustStore.

**Step 3:** Restart your IDE.

</details>

**TrustStore**

**sonarlint.ssl.trustStorePath**

* Path to the keystore used by SonarLint to store custom trusted server certificates
* **default**: `~/.sonarlint/ssl/truststore.p12`

**sonarlint.ssl.trustStorePassword**

* Password of the truststore.
* **default**: `sonarlint`

**sonarlint.ssl.trustStoreType**

* The format of the keystore file is found in the [Oracle documentation](https://docs.oracle.com/en/java/javase/17/docs/specs/security/standard-names.html#keystore-types).
* **default**: `PKCS12`

#### Client SSL certificates <a href="#client-ssl-certificates" id="client-ssl-certificates"></a>

Some servers or proxies may also require SonarQube for IDE to authenticate using client-side SSL certificates. This is a rare use case, and at for the moment, there is no UI to configure client-side SSL certificates. To properly authenticate client-side SSL certificates, you must manually create a keystore at the default location, or use the following properties:

**KeyStore**

**sonarlint.ssl.keyStorePath**

* Path to the keystore used by SonarQube for IDE to store client certificates.
* **default**: `~/.sonarlint/ssl/keystore.p12`

**sonarlint.ssl.keyStorePassword**

* Password of the keystore.
* **default**: `sonarlint`

**sonarlint.ssl.keyStoreType**

* The format of the keystore file is found in the [Oracle documentation](https://docs.oracle.com/en/java/javase/17/docs/specs/security/standard-names.html#keystore-types).
* **default**: `PKCS12`
