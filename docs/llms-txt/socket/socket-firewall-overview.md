# Source: https://docs.socket.dev/docs/socket-firewall-overview.md

# Socket Firewall Overview

Socket Firewall is a suite of security tools that protects your development environment from malicious packages in real time. By intercepting package manager requests and enforcing security policies, Socket Firewall blocks dangerous dependencies before they reach your systems.

## What Socket Firewall Does

Socket Firewall acts as an intelligent proxy between your package managers and package registries. When you install dependencies, Socket Firewall:

* **Intercepts network requests** from package managers before packages are downloaded
* **Checks packages against Socket's security intelligence** to identify known and potential malware
* **Blocks malicious packages** at any dependency depth, including transitive dependencies
* **Socket Firewall Enterprise additionally:**
  * **Enforces your organization's security policies** automatically across all installations
  * **Provides visibility** into what packages are being installed across your organization

This approach provides protection at the point of installation, preventing malicious code from ever reaching your filesystem, build systems, or production environments.

## Why Use Socket Firewall

**Real-time Protection**: Unlike scanning tools that analyze code after installation, Socket Firewall prevents malicious packages from being downloaded in the first place. This eliminates the window of vulnerability between installation and detection.

**Comprehensive Coverage**: Socket Firewall protects against threats in transitive dependencies, not just the packages you explicitly install. Since the majority of your dependency tree consists of indirect dependencies, this comprehensive approach is critical for real security.

**Zero-Day Defense**: Socket Firewall leverages Socket's AI-powered detection and human review process to identify emerging threats, providing protection against newly published malware before traditional signature-based tools can respond.

**Organizational Control**: Enforce consistent security policies across all developers, CI/CD pipelines, and build environments without requiring individual configuration or compliance monitoring.

**Minimal Disruption**: Socket Firewall integrates seamlessly into existing workflows, requiring minimal changes to how developers work while providing maximum protection.

## Architecture

Socket Firewall operates as an HTTP/HTTPS proxy server that sits between package managers and package registries. When a package manager attempts to download a package, the request flows through Socket Firewall, which:

1. Extracts package metadata (name, version, registry) from the request
2. Queries Socket's security API to check the package against your organization's security policy
3. Either allows the request to proceed to the registry or blocks it with an informative error message
4. Returns the package to the package manager (if allowed) or prevents installation (if blocked)

This architecture provides several advantages:

* **Language-agnostic**: Works with any package manager that supports HTTP proxies
* **No code changes required**: Existing projects work without modification
* **Centralized policy enforcement**: Security rules are enforced at the network level
* **Transparent operation**: Package managers function normally, with security applied automatically

## Socket Firewall Variants

Socket offers two variants of Socket Firewall to meet different needs.

### Socket Firewall Free

Socket Firewall Free is a zero-configuration tool designed for individual developers and small teams. It provides essential protection against known malware with no setup required.

**Key Characteristics:**

* **No API key required** - works immediately after installation
* **Zero configuration** - no setup files or environment variables needed
* **Wrapper mode only** - run as a command prefix (e.g., `sfw npm install`)
* **Core ecosystem support** - JavaScript/TypeScript (npm, yarn, pnpm), Python (pip, uv), and Rust (cargo)
* **Known malware blocking** - blocks confirmed malicious packages, warns on AI-detected threats
* **Public registries only** - does not support private or custom registries
* **Free for all users** - no paid plan required

**Ideal For:**

* Individual developers protecting their local machines
* Open source projects
* Teams getting started with supply chain security
* CI/CD pipelines requiring basic malware protection

### Socket Firewall Enterprise

Socket Firewall Enterprise is a fully configurable security solution designed for organizations that need comprehensive protection, custom policies, and broad ecosystem support.

**Key Characteristics:**

* **Requires API key** - integrates with your Socket organization and security policies
* **Flexible deployment modes**:
  * **Wrapper mode** - run as a command prefix, similar to the free version
  * **Service mode** - run as a persistent proxy server for centralized deployment
* **Comprehensive ecosystem support** - JavaScript/TypeScript, Python, Go, Java (Maven, Gradle), Ruby (gem, Bundler), Rust (cargo), and .NET (NuGet)
* **Configurable security policies** - customize how AI-detected malware, unscanned packages, packages with CVEs, and other threats are handled
* **Private registry support** - works with custom and private package registries
* **Allow-list capabilities** - override blocking decisions for specific packages when needed
* **Dashboard integration** - view installation activity and security events in your Socket dashboard
* **Organizational telemetry controls** - configure what usage data is collected
* **Chained proxy support** - integrate with existing corporate proxy infrastructure

**Ideal For:**

* Enterprise organizations with security and compliance requirements
* Teams using private package registries
* Organizations needing custom security policies
* Centralized deployment in Docker, Kubernetes, or on-premise environments
* CI/CD pipelines requiring comprehensive ecosystem coverage