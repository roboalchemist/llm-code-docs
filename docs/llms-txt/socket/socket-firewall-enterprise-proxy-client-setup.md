# Source: https://docs.socket.dev/docs/socket-firewall-enterprise-proxy-client-setup.md

# Enterprise Proxy Client Setup

This guide explains how to configure various package managers to work with Socket Firewall, an HTTP proxy that provides security scanning for package installations.

## Certificate Authority Setup

Socket Firewall uses a custom Certificate Authority (CA) to intercept HTTPS traffic. Before configuring package managers, you need to install and trust the CA certificate.

**Note:** If you're running Socket Firewall in service mode, you'll first need to generate the CA keypair and configure your service to use it. See [Generating Keys](socket-firewall-enterprise-generating-keys) for instructions on creating your CA keypair.

### Installing the CA Certificate

#### Linux (Ubuntu/Debian)

```bash
# Copy the CA certificate to the system certificate directory
sudo cp /path/to/socketFirewallCa.crt /usr/local/share/ca-certificates/socketFirewallCa.crt

# Update the system certificate store
sudo update-ca-certificates
```

#### Linux (RedHat/CentOS/Fedora)

```bash
# Copy the CA certificate to the system certificate directory
sudo cp /path/to/socketFirewallCa.crt /etc/pki/ca-trust/source/anchors/socketFirewallCa.crt

# Update the system certificate store
sudo update-ca-trust
```

#### macOS

##### Terminal Method

```bash
# Add the CA certificate to the system keychain
sudo security add-trusted-cert -d -r trustRoot -k /Library/Keychains/System.keychain /path/to/socketFirewallCa.crt

# Verify the certificate was added
security find-certificate -c "Socket Proxy CA" /Library/Keychains/System.keychain
```

##### GUI Method (Alternative)

1. Double-click the `socketFirewallCa.crt` file to open Keychain Access
2. Select "System" keychain when prompted
3. Enter your administrator password
4. Find the certificate in Keychain Access and double-click it
5. Expand "Trust" section and set "When using this certificate" to "Always Trust"
6. Close the dialog and enter your password again to save changes

For more details, see [Apple's documentation on certificate trust settings](https://support.apple.com/guide/keychain-access/change-the-trust-settings-of-a-certificate-kyca11871/mac).

#### Windows

##### PowerShell Method (Run as Administrator)

```powershell
# Import the CA certificate to the Trusted Root Certification Authorities store
Import-Certificate -FilePath "C:\path\to\socketFirewallCa.crt" -CertStoreLocation Cert:\LocalMachine\Root

# Verify the certificate was imported
Get-ChildItem -Path Cert:\LocalMachine\Root | Where-Object {$_.Subject -like "*Socket Proxy CA*"}
```

##### GUI Method (Alternative)

1. Right-click the `socketFirewallCa.crt` file and select "Install Certificate"
2. Choose "Local Machine" and click "Next"
3. Select "Place all certificates in the following store"
4. Click "Browse" and select "Trusted Root Certification Authorities"
5. Click "Next" then "Finish"
6. Click "Yes" when prompted about installing the certificate

For more details, see [Microsoft's documentation on managing certificates](https://learn.microsoft.com/en-us/windows-hardware/drivers/install/trusted-root-certification-authorities-certificate-store).

#### Java Applications (Maven, Gradle)

If Java is installed, add the CA certificate to the Java keystore:

```bash
keytool -import -trustcacerts -cacerts -noprompt \
    -storepass changeit \
    -alias socket-proxy-ca \
    -file /usr/local/share/ca-certificates/socketFirewallCa.crt
```

#### Verify CA is installed correctly

Run the following in the terminal to validate the Socket Firewall CA has been installed as a trusted root certificate:

```bash
openssl s_client -connect your-firewall-host:443 -prexit
```

Near the top of the output, you should see something like the following:

```
Certificate chain
 0 s:CN=your-firewall-host
   i:CN=Socket Security CA, O=Socket Security
   a:PKEY: RSA, 2048 (bit); sigalg: sha256WithRSAEncryption
   v:NotBefore: Aug 24 02:02:23 2025 GMT; NotAfter: Aug 24 02:02:23 2026 GMT
```

If you're not sure of the output, check it against the output from this command; they should look the same:

```bash
openssl s_client -connect your-firewall-host:443 -prexit -CAfile ./path/to/socketFirewallCa.crt
```

## Package Manager Configurations

### Node.js Package Managers

#### npm

**Environment Variables:**

```bash
npm config set proxy "https://your-firewall-host:https-port"
npm config set https-proxy "https://your-firewall-host:https-port"
export NODE_EXTRA_CA_CERTS="/path/to/socketFirewallCa.crt"
```

**Alternative for Node.js > 23:**

```bash
npm config set proxy "https://your-firewall-host:https-port"
npm config set https-proxy "https://your-firewall-host:https-port"
export NODE_OPTIONS="--use-system-ca"
```

**Note:** Firewall requires `npm` version 10 or higher. Previous versions of `npm` included an abstraction incompatible with how we intercept traffic.

#### Yarn

**Environment Variables:**

```bash
export YARN_HTTP_PROXY="https://your-firewall-host:https-port"
export YARN_HTTPS_PROXY="https://your-firewall-host:https-port"
export NODE_EXTRA_CA_CERTS="/path/to/socketFirewallCa.crt"
export YARN_HTTPS_CA_FILE_PATH="/path/to/socketFirewallCa.crt"
```

**Alternative for Node.js > 23:**

```bash
export YARN_HTTP_PROXY="https://your-firewall-host:https-port"
export YARN_HTTPS_PROXY="https://your-firewall-host:https-port"
export NODE_OPTIONS="--use-system-ca"
```

#### pnpm

**Environment Variables:**

```bash
export HTTP_PROXY="https://your-firewall-host:https-port"
export HTTPS_PROXY="https://your-firewall-host:https-port"
export NODE_EXTRA_CA_CERTS="/path/to/socketFirewallCa.crt"
```

**Alternative for Node.js > 23:**

```bash
export HTTP_PROXY="https://your-firewall-host:https-port"
export HTTPS_PROXY="https://your-firewall-host:https-port"
export NODE_OPTIONS="--use-system-ca"
```

### Python Package Managers

#### pip

**Environment Variables:**

```bash
export HTTP_PROXY="https://your-firewall-host:https-port"
export HTTPS_PROXY="https://your-firewall-host:https-port"
export PIP_CERT="/path/to/socketFirewallCa.crt"
```

#### Poetry

**Poetry is not currently supported by Socket Firewall**

#### uv

**Environment Variables:**

```bash
export HTTP_PROXY="https://your-firewall-host:https-port"
export HTTPS_PROXY="https://your-firewall-host:https-port"
export PIP_CERT="/path/to/socketFirewallCa.crt"
```

### Go

**Environment Variables:**

```bash
export HTTP_PROXY="https://your-firewall-host:https-port"
export HTTPS_PROXY="https://your-firewall-host:https-port"
```

### Rust (Cargo)

**Configuration File:** Create `.cargo/config.toml` in your project or home directory:

```toml
[http]
cainfo = "/path/to/socketFirewallCa.crt"
proxy = 'your-firewall-host:http-port'
proxy-cainfo = "/path/to/socketFirewallCa.crt"
multiplexing = false
```

**Known Issue:** Cargo currently has limited support for HTTPS proxies. Use the HTTP port of Socket Firewall instead.

### Ruby Package Managers

#### RubyGems (gem)

**Configuration File:** Create `~/.gemrc`:

```yaml
---
http_proxy: https://your-firewall-host:http-port
https_proxy: https://your-firewall-host:http-port
```

**Note:** RubyGems may not fully support HTTPS proxies. Use the HTTP port of Socket Firewall.

#### Bundler

**Configuration File:** Create `~/.gemrc`:

```yaml
---
http_proxy: https://your-firewall-host:http-port
https_proxy: https://your-firewall-host:http-port
```

**Note:** Bundler cannot establish proxy connections with HTTPS endpoints. Use the HTTP port of Socket Firewall.

### Java Package Managers

#### Maven

**Configuration File:** Edit `/usr/share/maven/conf/settings.xml` (or `~/.m2/settings.xml`):

```xml
<settings>
  <proxies>
    <proxy>
      <id>http-proxy</id>
      <active>true</active>
      <protocol>http</protocol>
      <host>your-firewall-host</host>
      <port>http-port</port>
    </proxy>
    <proxy>
      <id>https-proxy</id>
      <active>true</active>
      <protocol>https</protocol>
      <host>your-firewall-host</host>
      <port>http-port</port>
    </proxy>
  </proxies>
</settings>
```

**Known Issue:** Maven uses Apache HttpClient, which doesn't support HTTPS requests through HTTPS proxies. Use the HTTP port for both protocols.

#### Gradle

**Configuration File:** Create `~/.gradle/gradle.properties`:

```properties
systemProp.http.proxyHost=your-firewall-host
systemProp.http.proxyPort=http-port
systemProp.https.proxyHost=your-firewall-host
systemProp.https.proxyPort=http-port
```

**Known Issue:** Gradle uses Apache HttpClient, which doesn't support HTTPS requests through HTTPS proxies. Use the HTTP port for both protocols.

### .NET (NuGet)

**Environment Variables:**

```bash
export HTTP_PROXY="https://your-firewall-host:https-port"
export HTTPS_PROXY="https://your-firewall-host:https-port"
```

## Important Notes

### HTTPS Proxy Limitations

Several package managers have limitations with HTTPS proxies:

* **Cargo**: Limited HTTPS proxy support ([issue](https://github.com/rust-lang/cargo/issues/15376))
* **Maven/Gradle**: Apache HttpClient doesn't support HTTPS through HTTPS proxy ([issue](https://issues.apache.org/jira/projects/HTTPCLIENT/issues/HTTPCLIENT-2369))
* **RubyGems/Bundler**: Limited HTTPS proxy support

For these tools, use the HTTP port of Socket Firewall instead of the HTTPS port.

### Environment Variable Priority

Most package managers respect standard HTTP proxy environment variables:

* `HTTP_PROXY` / `http_proxy`
* `HTTPS_PROXY` / `https_proxy`

Some tools have their own specific environment variables (e.g., `YARN_HTTP_PROXY`, `PIP_CERT`).