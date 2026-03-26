# Source: https://docs.socket.dev/docs/socket-firewall-enterprise.md

# Socket Firewall Enterprise

Socket Firewall Enterprise is an HTTP/HTTPS proxy server that intercepts package manager requests and enforces security policies by blocking dangerous packages. It supports npm, PyPI, Maven, Go modules, RubyGems, Cargo, and NuGet registries.

It supports a number of ecosystems and package managers and can operate in a couple of modes:

* **CLI Wrapper Mode** - in this mode, Socket Firewall runs locally and is prefixed to package manager commands in your terminal. The experience is similar to Socket Firewall Free, differing in its additional configurability.
* **Proxy Service Mode** - in this mode, Socket Firewall runs as a persistent service and operates as a centrally-managed HTTPS proxy.

Learn how to deploy and configure Firewall in these modes by consulting the mode-specific documentation.

## Support Matrix

| Ecosystem             | Package Manager | Wrapper Mode                 | Service Mode - HTTP  | Service Mode - HTTPS |
| --------------------- | --------------- | ---------------------------- | -------------------- | -------------------- |
| JavaScript/TypeScript | npm             | :white\_check\_mark:         | :white\_check\_mark: | :white\_check\_mark: |
| JavaScript/TypeScript | yarn            | :white\_check\_mark:         | :white\_check\_mark: | :white\_check\_mark: |
| JavaScript/TypeScript | pnpm            | :white\_check\_mark:         | :white\_check\_mark: | :white\_check\_mark: |
| Python                | uv              | :white\_check\_mark:         | :white\_check\_mark: | :white\_check\_mark: |
| Python                | pip             | :white\_check\_mark:         | :white\_check\_mark: | :white\_check\_mark: |
| Python                | Poetry          | :x: (1)                      | :x: (1)              | :x: (1)              |
| Rust                  | Cargo           | :white\_check\_mark:         | :white\_check\_mark: | :x: (2)              |
| Go                    | Go Modules      | :large\_orange\_diamond: (3) | :white\_check\_mark: | :white\_check\_mark: |
| Java/Scala/Kotlin     | Maven           | :x: (4)                      | :white\_check\_mark: | :x: (5)              |
| Java/Scala/Kotlin     | Gradle          | :x: (4)                      | :white\_check\_mark: | :x: (5)              |
| Ruby                  | gem             | :white\_check\_mark:         | :white\_check\_mark: | :x: (6)              |
| Ruby                  | Bundler         | :white\_check\_mark:         | :white\_check\_mark: | :x: (6)              |
| .NET                  | NuGet           | :white\_check\_mark:         | :white\_check\_mark: | :white\_check\_mark: |

Footnodes:

1. Poetry has issues utilizing a proxy for package management requests. Poetry is not supported at this time.
2. Cargo has trouble interacting with a TLS-encrypted proxy. Traffic sent to and received by the remote registry will be encrypted, but initial per-request Socket Firewall config may be sent unencrypted. We recommend Cargo users to use the CLI wrapper or an on-prem HTTP service instance.
3. Wrapper mode is supported for Golang in Linux. However, due to how Golang interacts with system certificates and the keychain on MacOS, wrapper mode is not currently supported.
4. Unfortunately, Maven and Gradle require manual editing of configuration files in order to configure a proxy. For that reason, they are unsupported by `sfw` running in wrapper mode.
5. Maven and Gradle rely on a HTTP library that does not support TLS for HTTP proxy connections (the Socket Firewall URL). However, HTTPS to the destination is supported. It is recommended to configure this for on-prem, where per-request Socket Firewall configuration can be sent unencrypted in the initial CONNECT without security concerns.
6. gem and Bundler rely on a HTTP library that does not support TLS for HTTP proxy connections (the Socket Firewall URL). However, HTTPS to the destination is supported. It is recommended to that Ruby users should interact with Socket Firewall through the CLI wrapper or via an on-prem service instance.

<br />