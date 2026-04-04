# Source: https://docs.sonarsource.com/sonarqube-mcp-server/build-and-configure/configure.md

# Configure your SonarQube MCP server

No matter if you're looking for a configuration for single-users ([#stdio](#stdio "mention")), multi-user ([#http](#http "mention")), or secure multi-client ([#https](#https "mention")) configurations, the SonarQube MCP Server has you covered. On this page, you'll find container image examples for setup with SonarQube Cloud and SonarQube Server, including requirements for user tokens and handling of custom certificates and proxies.

If you're unable to use a container image to deploy your MCP server, please see the [build](https://docs.sonarsource.com/sonarqube-mcp-server/build-and-configure/build "mention") page for alternatives.

### Overview&#x20;

The SonarQube MCP Server uses [#stdio](#stdio "mention") when running a local configuration. This configuration is designed for single-user access however, it's possible to manage your MCP server using a [#transport-mode](#transport-mode "mention") configuration, designed for shared access across a network using [#http](#http "mention") or [#https](#https "mention") connection protocols.

### Transport mode

Once configured, your MCP server is hosted on a local network and can handle connections from multiple users; all of your team's developers can access the same MCP server and reduces the need for multiple unique configurations. For more information about how HTTP transport works, please see the [Model Context Protocol documentation on Transports](https://modelcontextprotocol.io/specification/2025-06-18/basic/transports).

The SonarQube MCP Server supports three transport modes:

1. [#stdio](#stdio "mention") is the default mode. This is the default mode, designed for single-user setups using command line tools or MCP clients.
2. [#http](#http "mention") is an unencrypted transport mode that can enable multiple client connections to a remote HTTP server. Each client provides its own user token. This transport mode is not recommended. Use [#stdio](#stdio "mention") for local development or [#https](#https "mention") for multi-user production deployments.
3. [#https](#https "mention") is also for multi-user production environments and uses a security protocol. This mode is the same as HTTP plus TLS encryption. The use of SSL certificates is required.

#### Stdio

Stdio is the default mode for local development and single-user set ups used by all MCP clients. The [#common-variables](https://docs.sonarsource.com/sonarqube-mcp-server/environment-variables#common-variables "mention") are required to initialize any transport mode you choose.

{% hint style="info" %}
Although the examples below use `docker`, any OCI-compatible container runtime works (for example, Podman, nerdctl, etc). Simply replace `docker` with commands specific to your preferred tool.
{% endhint %}

**Docker example**

{% tabs %}
{% tab title="SONARQUBE CLOUD" %}
Use this code sample when using the container image to configure your MCP HTTP server for integrating with SonarQube Cloud.

```bash
{
  "mcpServers": {
    "sonarqube": {
      "command": "docker",
      "args": ["run", "-i", "--rm", "-e", "SONARQUBE_TOKEN", "-e", "SONARQUBE_ORG", "mcp/sonarqube"],
      "env": {
        "SONARQUBE_TOKEN": "<YourSonarQubeUserToken>",
        "SONARQUBE_ORG": "<YourSonarQubeOrganization>"
      }
    }
  }
}
```

{% hint style="warning" %}
*User tokens* are required when setting up connected mode or an MCP Server between SonarQube (Server, Cloud) and SonarQube for IDE. Note that the binding will not function properly if *project tokens*, *global tokens*, or *scoped organization tokens* are used during the setup process.
{% endhint %}
{% endtab %}

{% tab title="SONARQUBE SERVER" %}
Use this code sample when using Docker to configure your MCP server for integrating with SonarQube Server or SonarQube Community Build.

```bash
{
  "mcpServers": {
    "sonarqube": {
      "command": "docker",
      "args": ["run", "-i", "--rm", "-e", "SONARQUBE_TOKEN", "-e", "SONARQUBE_URL", "mcp/sonarqube"],
      "env": {
        "SONARQUBE_TOKEN": "<YourSonarQubeUserToken>",
        "SONARQUBE_URL": "<YourSonarQubeURL>"
      }
    }
  }
}
```

{% hint style="warning" %}
*User tokens* are required when setting up connected mode or an MCP Server between SonarQube (Server, Cloud) and SonarQube for IDE. Note that the binding will not function properly if *project tokens*, *global tokens*, or *scoped organization tokens* are used during the setup process.
{% endhint %}
{% endtab %}
{% endtabs %}

#### HTTP

{% hint style="danger" %}
The HTTP [#transport-mode](#transport-mode "mention") is not recommended. Use [#stdio](#stdio "mention") for local development or [#https](#https "mention") for multi-user production deployments.
{% endhint %}

Enable HTTP transport for unencrypted multi-user scenarios where more than one client will connect to a shared server. The [#common-variables](https://docs.sonarsource.com/sonarqube-mcp-server/environment-variables#common-variables "mention") are required for initialization, in addition to the listed [#http-variables](https://docs.sonarsource.com/sonarqube-mcp-server/environment-variables#http-variables "mention") that clients will need to access the server.&#x20;

Once set up, each client must provide its own user token for access.

#### HTTPS

HTTPS configurations are very similar to [#http](#http "mention") but require SSL certificates.&#x20;

* For local development, use HTTP instead of HTTPS to avoid [#ssl-certificate](https://docs.sonarsource.com/sonarqube-mcp-server/environment-variables#ssl-certificate "mention") issues.&#x20;
* For production deployments with proper SSL certificates from a trusted CA, use HTTPS.

**Docker example**

{% tabs %}
{% tab title="SONARQUBE CLOUD" %}
Use this code sample when using the container image to configure your MCP HTTPS server for integrating with SonarQube Cloud. The server uses the `SONARQUBE_TOKEN`  one time, only for initialization.

{% hint style="info" %}
Although the examples below use `docker`, any OCI-compatible container runtime works (for example, Podman, nerdctl, etc). Simply replace `docker` with commands specific to your preferred tool.
{% endhint %}

```bash
# Start server (requires token for initialization)  
docker run -p 8443:8443 \
  -v $(pwd)/keystore.p12:/etc/ssl/mcp/keystore.p12:ro \
  -e SONARQUBE_TRANSPORT=https \
  -e SONARQUBE_HTTP_HOST=0.0.0.0 \
  -e SONARQUBE_HTTP_PORT=8443 \
  -e SONARQUBE_TOKEN="<YourSonarQubeUserToken>" \
  -e SONARQUBE_ORG="<YourSonarQubeOrganization>" \
  mcp/sonarqube
```

{% hint style="warning" %}
*User tokens* are required when setting up connected mode or an MCP Server between SonarQube (Server, Cloud) and SonarQube for IDE. Note that the binding will not function properly if *project tokens*, *global tokens*, or *scoped organization tokens* are used during the setup process.
{% endhint %}
{% endtab %}

{% tab title="SONARQUBE SERVER" %}
Use this code sample when using the container image to configure your MCP HTTP server for integrating with SonarQube Server or SonarQube Community Build. The server uses the `SONARQUBE_TOKEN`  one time, only for initialization.

{% hint style="info" %}
Although the examples below use `docker`, any OCI-compatible container runtime works (for example, Podman, nerdctl, etc). Simply replace `docker` with commands specific to your preferred tool.
{% endhint %}

```bash
# Start server (requires token for initialization)
docker run -p 8080:8080 \
  -e SONARQUBE_HTTP_ENABLED=true \
  -e SONARQUBE_HTTP_PORT=<YourHTTPPort> \
  -e SONARQUBE_TOKEN="<YourSonarQubeUserToken>" \
  -e SONARQUBE_URL="<YourSonarQubeURL>" \
  mcp/sonarqube
```

{% hint style="warning" %}
*User tokens* are required when setting up connected mode or an MCP Server between SonarQube (Server, Cloud) and SonarQube for IDE. Note that the binding will not function properly if *project tokens*, *global tokens*, or *scoped organization tokens* are used during the setup process.
{% endhint %}
{% endtab %}
{% endtabs %}

**Client configuration**

When connecting to the HTTP or HTTPS transport server, clients must include the `SONARQUBE_TOKEN` header in all requests. The server uses the `SONARQUBE_TOKEN`  only for initialization.

```json
{
  "mcpServers": {
    "sonarqube-https": {
      "url": "https://<YourSonarQubeMCPServer>:8443/mcp",
      "headers": {
        "SONARQUBE_TOKEN": "<YourSonarQubeUserToken>"
      }
    }
  }
}
```

{% hint style="warning" %}
*User tokens* are required when setting up connected mode or an MCP Server between SonarQube (Server, Cloud) and SonarQube for IDE. Note that the binding will not function properly if *project tokens*, *global tokens*, or *scoped organization tokens* are used during the setup process.
{% endhint %}

### Custom certificates

If your instance of SonarQube Server uses a self-signed certificate or a certificate from a private Certificate Authority (CA), you can add custom certificates to the container.

#### Supported certificate formats

The container supports the following certificate formats:

* `.crt` files (PEM or DER encoded)
* `.pem` files (PEM encoded)

{% hint style="info" %}
Although the examples below use `docker`, any OCI-compatible container runtime works (for example, Podman, nerdctl, etc). Simply replace `docker` with commands specific to your preferred tool.
{% endhint %}

<details>

<summary>Using a Volume Mount</summary>

Mount a directory containing your certificates when running the container:

```bash
docker run -i --rm \
  -v /path/to/your/certificates/:/usr/local/share/ca-certificates/:ro \
  -e SONARQUBE_TOKEN="<YourSonarQubeUserToken>" \
  -e SONARQUBE_URL="<YourSonarQubeURL>" \
  mcp/sonarqube
```

{% hint style="warning" %}
*User tokens* are required when setting up connected mode or an MCP Server between SonarQube (Server, Cloud) and SonarQube for IDE. Note that the binding will not function properly if *project tokens*, *global tokens*, or *scoped organization tokens* are used during the setup process.
{% endhint %}

</details>

<details>

<summary>Custom certificates</summary>

When using custom certificates, you can modify your MCP configuration to mount the certificates. Here an example when connecting to SonarQube Server or SonarQube Community Build:

```json
{
  "sonarqube": {
    "command": "docker",
    "args": [
      "run",
      "-i",
      "--rm",
      "-v",
      "/path/to/your/certificates/:/usr/local/share/ca-certificates/:ro",
      "-e",
      "SONARQUBE_TOKEN",
      "-e",
      "SONARQUBE_URL",
      "mcp/sonarqube"
    ],
    "env": {
      "SONARQUBE_TOKEN": "<YourSonarQubeUserToken>",
      "SONARQUBE_URL": "<YourSonarQubeURL>"
    }
  }
}
```

{% hint style="warning" %}
*User tokens* are required when setting up connected mode or an MCP Server between SonarQube (Server, Cloud) and SonarQube for IDE. Note that the binding will not function properly if *project tokens*, *global tokens*, or *scoped organization tokens* are used during the setup process.
{% endhint %}

</details>

### Proxy

The SonarQube MCP Server supports HTTP proxies through standard Java proxy system properties.

<details>

<summary><strong>Configure proxy settings</strong></summary>

You can configure proxy settings using Java system properties. These can be set as environment variables or passed as JVM arguments.

#### **Common proxy properties**

| Property             | Description                                  | Example                                |
| -------------------- | -------------------------------------------- | -------------------------------------- |
| `http.proxyHost`     | HTTP proxy hostname                          | `proxy.example.com`                    |
| `http.proxyPort`     | HTTP proxy port                              | `8080`                                 |
| `https.proxyHost`    | HTTPS proxy hostname                         | `proxy.example.com`                    |
| `https.proxyPort`    | HTTPS proxy port                             | `8443`                                 |
| `http.nonProxyHosts` | Hosts that bypass the proxy (pipe-separated) | `localhost\|127.0.0.1\|*.internal.com` |

#### **Proxy authentication**

If your proxy requires authentication, the SonarQube MCP Server uses Java's standard authentication mechanism. You can set up proxy credentials using Java system properties:

| Property              | Description          | Example        |
| --------------------- | -------------------- | -------------- |
| `http.proxyPassword`  | HTTP proxy password  | `yourpassword` |
| `http.proxyUser`      | HTTP proxy username  | `yourusername` |
| `https.proxyPassword` | HTTPS proxy password | `yourpassword` |
| `https.proxyUser`     | HTTPS proxy username | `yourusername` |

</details>
