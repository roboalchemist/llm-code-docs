# Source: https://docs.socket.dev/docs/socket-firewall-enterprise-configuration.md

# Enterprise Configuration

Socket Firewall Enterprise can be configured through environment variables or configuration files. Configuration applies to both [CLI Wrapper Mode](socket-firewall-enterprise-wrapper-mode)  and [Proxy Service Mode](socket-firewall-enterprise-proxy-service-setup) .

## Configuration Files

By default, the proxy loads configuration from `.sfw.config` in your home directory and `/run/secrets/dot-env-secrets` (designed for use with Docker).

If the `SFW_CONFIG_RELATIVE_PATHS` environment variable is set, Socket Firewall will load configuration from multiple sources in order:

1. `.sfw.config` (current directory)
2. `.sfw.config` (parent directories)
3. `.sfw.config` (home directory)
4. `/run/secrets/dot-env-secrets`

Configuration files use dotenv format:

```shell
SOCKET_API_KEY=sktsec_your_api_key_here_api
SFW_HOSTNAME=your.proxy.hostname
```

## Configuration Options

<Table align={["left","left","left","left"]}>
  <thead>
    <tr>
      <th>
        Variable
      </th>

      <th>
        Valid Modes
      </th>

      <th>
        Is Required
      </th>

      <th>
        Details
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        `SOCKET_API_KEY`
      </td>

      <td>
        ✅ Proxy Mode\
        ✅ Wrapper Mode
      </td>

      <td>
        Yes
      </td>

      <td>
        Socket API token with required scopes: `packages`, `entitlements:list`.

        Get your API key from [socket.dev](https://socket.dev).
      </td>
    </tr>

    <tr>
      <td>
        `SFW_CONFIG_RELATIVE_PATHS`
      </td>

      <td>
        ✅ Proxy Mode\
        ✅ Wrapper Mode
      </td>

      <td>
        No
      </td>

      <td>
        Determines whether Firewall config will be loaded from paths relative to the current working directory. This is particularly useful if you're running in CLI wrapper mode and want to use different configurations for different local projects.
      </td>
    </tr>

    <tr>
      <td>
        `SFW_HOSTNAME`
      </td>

      <td>
        ✅ Proxy Mode\
        ❌ Wrapper Mode
      </td>

      <td>
        Yes (service mode)
      </td>

      <td>
        The hostname which will be used to address the proxy server.
      </td>
    </tr>

    <tr>
      <td>
        `SFW_CA_CERT_PATH`
      </td>

      <td>
        ✅ Proxy Mode\
        ❌ Wrapper Mode
      </td>

      <td>
        Yes (service mode)
      </td>

      <td>
        Path to a PEM-encoded CA certificate file. See Generating Keys for instructions.
      </td>
    </tr>

    <tr>
      <td>
        `SFW_CA_KEY_PATH`
      </td>

      <td>
        ✅ Proxy Mode\
        ❌ Wrapper Mode
      </td>

      <td>
        Yes (service mode)
      </td>

      <td>
        Path to a PEM-encoded CA key file. See Generating Keys for instructions.
      </td>
    </tr>

    <tr>
      <td>
        `SFW_HTTP_PORT`
      </td>

      <td>
        ✅ Proxy Mode\
        ✅ Wrapper Mode
      </td>

      <td>
        No
      </td>

      <td>
        Port on which to listen for HTTP CONNECT requests. Defaults to `80`.
      </td>
    </tr>

    <tr>
      <td>
        `SFW_HTTPS_PORT`
      </td>

      <td>
        ✅ Proxy Mode\
        ✅ Wrapper Mode
      </td>

      <td>
        No
      </td>

      <td>
        Port on which to listen for HTTPS CONNECT requests. Defaults to `443`.
      </td>
    </tr>

    <tr>
      <td>
        `SFW_ALLOW_BAD_DESTINATION_CERT`
      </td>

      <td>
        ✅ Proxy Mode\
        ✅ Wrapper Mode
      </td>

      <td>
        No
      </td>

      <td>
        ill ignore SSL errors when connecting to destination hosts. Must be set to the string `true` for the option to take effect.
      </td>
    </tr>

    <tr>
      <td>
        `SFW_CUSTOM_REGISTRIES`
      </td>

      <td>
        ✅ Proxy Mode\
        ✅ Wrapper Mode
      </td>

      <td>
        No
      </td>

      <td>
        A comma-delimited set of custom registry entries. See Custom Registries documentation below for details.

        **Example:**\
        `export SFW_CUSTOM_REGISTRIES='npm:packages.example.com/npm-mirror,pypi:packages.example.com/pypi-mirror'`
      </td>
    </tr>

    <tr>
      <td>
        `SFW_UNKNOWN_HOST_ACTION`
      </td>

      <td>
        ✅ Proxy Mode\
        ✅ Wrapper Mode
      </td>

      <td>
        No
      </td>

      <td>
        Action to take when encountering unknown hosts. Valid values: `block`, `warn`, or `ignore`. Defaults to `block`.
      </td>
    </tr>

    <tr>
      <td>
        `SFW_JSON_REPORT_PATH`
      </td>

      <td>
        ✅ Proxy Mode\
        ✅ Wrapper Mode
      </td>

      <td>
        No
      </td>

      <td>
        Path to write a JSON report of blocked packages.
      </td>
    </tr>

    <tr>
      <td>
        `SFW_DEBUG`
      </td>

      <td>
        ✅ Proxy Mode\
        ✅ Wrapper Mode
      </td>

      <td>
        No
      </td>

      <td>
        Enable debug logging. Must be set to the string `true` to enable.
      </td>
    </tr>

    <tr>
      <td>
        `SFW_TELEMETRY_DISABLED`
      </td>

      <td>
        ✅ Proxy Mode\
        ✅ Wrapper Mode
      </td>

      <td>
        No
      </td>

      <td>
        Disables telemetry reporting to Socket. Must be set to the string `true` to disable.
      </td>
    </tr>

    <tr>
      <td>
        `SFW_TELEMETRY_ENDPOINT`
      </td>

      <td>
        ✅ Proxy Mode\
        ✅ Wrapper Mode
      </td>

      <td>
        No
      </td>

      <td>
        Custom URL endpoint for telemetry data. Must be a valid URL. Defaults to `https://api.socket.dev/v0/telemetry`.
      </td>
    </tr>

    <tr>
      <td>
        `SFW_REPORT_MESSAGE`
      </td>

      <td>
        ✅ Proxy Mode
        ✅ Wrapper Mode
      </td>

      <td>
        No
      </td>

      <td>
        Custom message to display in the report when packages are blocked. Useful for linking to internal documentation (Wiki, Confluence) or providing organization-specific guidance. The message is displayed exactly as provided in the "Need help?" section of the report.

        Example:
        export SFW\_REPORT\_MESSAGE="For internal guidance, see [https://wiki.example.com/security/sfw](https://wiki.example.com/security/sfw)"
      </td>
    </tr>
  </tbody>
</Table>

## Custom Registries

Socket Firewall can filter traffic for custom registries. Each entry must take the form `kind:fqdn` or `kind:fqdn/url-prefix`.

### Valid Registry Kinds

* `npm` - npm registry
* `pypi` - Python Package Index
* `maven` - Maven repository
* `golang` - Go modules proxy
* `gem` - RubyGems registry
* `cargo` - Rust crates registry
* `nuget` - NuGet package registry
* `block` - All traffic to the specified host will be blocked
* `wrap` - All traffic to the specified host will be blindly forwarded without inspecting requests

### FQDN Matching

The FQDN value should match the exact hostname that your package manager is configured to use.

### URL Prefix (Optional)

An optional URL prefix is allowed. Some private registry services support multiple types of package manager, determined by the first part of the path. For example, you might have an `.npmrc` file that looks something like this:

```
; The trailing slash is required
registry=https://packages.example.com/npm-mirror/

; Auth token scoped to the exact host + path prefix
always-auth=true
//packages.example.com/npm-mirror/:_authToken=${NPM_TOKEN}

; You've installed the Socket Firewall CA locally, so you can trust the proxied TLS connection
strict-ssl=true
```

If this were your npm configuration, the corresponding custom registry config would look like this:

```
export SFW_CUSTOM_REGISTRIES='npm:packages.example.com/npm-mirror'
```

When configured in this way, Socket Firewall will intercept traffic to `packages.example.com` in the same way it does for standard public registries.

### Multiple Custom Registries

Multiple prefixed registry entries are allowed. For example, the following configuration is valid:

```
export SFW_CUSTOM_REGISTRIES='npm:packages.example.com/npm-mirror,pypi:packages.example.com/pypi-mirror'
```