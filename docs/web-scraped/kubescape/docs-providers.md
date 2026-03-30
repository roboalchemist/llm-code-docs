# Source: https://kubescape.io/docs/providers/

Title: Connecting to providers - Kubescape

URL Source: https://kubescape.io/docs/providers/

Markdown Content:
Connecting to providers - Kubescape
===============
- [x] - [x] 

[Skip to content](https://kubescape.io/docs/providers/#connecting-to-providers)

[![Image 1: logo](https://kubescape.io/assets/kubescape-lockup.svg)](https://kubescape.io/ "Kubescape")

 Kubescape 

 Connecting to providers 

Type to start searching

[GitHub * v4.0.2 * 11.2k * 900](https://github.com/kubescape/kubescape "Go to repository")

*   [Home](https://kubescape.io/)
*   [Docs](https://kubescape.io/docs/)
*   [Project](https://kubescape.io/project/about/)
*   [Blog](https://kubescape.io/blog/)
*   [GitHub](https://github.com/kubescape/kubescape)

[![Image 2: logo](https://kubescape.io/assets/kubescape-lockup.svg)](https://kubescape.io/ "Kubescape") Kubescape  

[GitHub * v4.0.2 * 11.2k * 900](https://github.com/kubescape/kubescape "Go to repository")

*   [Home](https://kubescape.io/)
*   - [x]  Docs   Docs  
    *   [Documentation overview](https://kubescape.io/docs/)
    *   [Getting Started](https://kubescape.io/docs/getting-started/)
    *   [Installing the client](https://kubescape.io/docs/install-cli/)
    *   [Installing in your cluster](https://kubescape.io/docs/install-operator/)
    *   [Scanning your environment](https://kubescape.io/docs/scanning/)
    *   [Accepting risk](https://kubescape.io/docs/accepting-risk/)
    *   - [x]  Connecting to providers  [Connecting to providers](https://kubescape.io/docs/providers/) Table of contents  
        *   [Compatible providers](https://kubescape.io/docs/providers/#compatible-providers)
        *   [Configuring a provider](https://kubescape.io/docs/providers/#configuring-a-provider)
            *   [In the Kubescape client](https://kubescape.io/docs/providers/#in-the-kubescape-client)
            *   [In the Kubescape Operator](https://kubescape.io/docs/providers/#in-the-kubescape-operator)

    *   [MCP Server](https://kubescape.io/docs/mcp-server/)
    *   - [x]  Kubescape Operator   Kubescape Operator  
        *   [Overview](https://kubescape.io/docs/operator/)
        *   [Vulnerability scanning](https://kubescape.io/docs/operator/vulnerabilities/)
        *   [Relevancy](https://kubescape.io/docs/operator/relevancy/)
        *   [Runtime Threat Detection](https://kubescape.io/docs/operator/runtime-threat-detection/)
        *   [Generate Network Policies](https://kubescape.io/docs/operator/network-policy-generation/)
        *   [Scheduled scans](https://kubescape.io/docs/operator/scheduled-scans/)
        *   [Continuous scanning](https://kubescape.io/docs/operator/continuous-scanning/)
        *   [Prometheus Integrations](https://kubescape.io/docs/operator/prometheus-integration/)
        *   [UI with Headlamp](https://kubescape.io/docs/operator/ui-with-headlamp/)
        *   [Automatic upgrades](https://kubescape.io/docs/operator/automatic-release-upgrades/)
        *   [VEX document generation (experimental)](https://kubescape.io/docs/operator/generating-vex/)
        *   [Telemetry](https://kubescape.io/docs/operator/telemetry/)
        *   [Node Agents per Node Pool](https://kubescape.io/docs/operator/multiple-node-agent-per-node-pool/)

    *   - [x]  Integrations   Integrations  
        *   [Overview](https://kubescape.io/docs/integrations/)
        *   [GitHub](https://kubescape.io/docs/integrations/github/)
        *   [Lens](https://kubescape.io/docs/integrations/lens/)
        *   [VS Code](https://kubescape.io/docs/integrations/vscode/)

    *   - [x]  Frameworks and Controls   Frameworks and Controls  
        *   [Overview](https://kubescape.io/docs/frameworks-and-controls/)
        *   [Frameworks](https://kubescape.io/docs/frameworks-and-controls/frameworks/)
        *   [Control library](https://kubescape.io/docs/controls/)
        *   [Configuring controls](https://kubescape.io/docs/frameworks-and-controls/configuring-controls/)

    *   - [x]  Guides   Guides  
        *   [Configure checks on a GitHub repository](https://kubescape.io/docs/guides/kubescape-gha/)
        *   [Harden a cluster](https://kubescape.io/docs/guides/kubescape-cli/)
        *   [Deploying on OpenShift](https://kubescape.io/docs/guides/deploying-on-openshift/)
        *   [Kubescape for teenagers](https://kubescape.io/docs/guides/kubescape-for-teenagers/kubescape-for-teenagers/)

*   - [x]  Project   Project  
    *   [About the Kubescape project](https://kubescape.io/project/about/)
    *   [License](https://kubescape.io/project/license/)
    *   [Releases](https://github.com/kubescape/helm-charts/releases)
    *   [Community](https://kubescape.io/project/community/)
    *   [Contributing](https://github.com/kubescape/kubescape/blob/master/CONTRIBUTING.md)

*   - [x]  Blog   Blog  
    *   [Kubescape Blog](https://kubescape.io/blog/)
    *   - [x]  Archive   Archive  
        *   [May 2025](https://kubescape.io/blog/archive/2025/05/)
        *   [April 2025](https://kubescape.io/blog/archive/2025/04/)
        *   [March 2025](https://kubescape.io/blog/archive/2025/03/)
        *   [February 2025](https://kubescape.io/blog/archive/2025/02/)
        *   [August 2024](https://kubescape.io/blog/archive/2024/08/)
        *   [July 2024](https://kubescape.io/blog/archive/2024/07/)
        *   [December 2023](https://kubescape.io/blog/archive/2023/12/)
        *   [November 2023](https://kubescape.io/blog/archive/2023/11/)
        *   [October 2023](https://kubescape.io/blog/archive/2023/10/)
        *   [September 2023](https://kubescape.io/blog/archive/2023/09/)

    *   - [x]  Categories   Categories  
        *   [Announcements](https://kubescape.io/blog/category/announcements/)
        *   [Project](https://kubescape.io/blog/category/project/)
        *   [Study](https://kubescape.io/blog/category/study/)

*   [GitHub](https://github.com/kubescape/kubescape)

 Table of contents  
*   [Compatible providers](https://kubescape.io/docs/providers/#compatible-providers)
*   [Configuring a provider](https://kubescape.io/docs/providers/#configuring-a-provider)
    *   [In the Kubescape client](https://kubescape.io/docs/providers/#in-the-kubescape-client)
    *   [In the Kubescape Operator](https://kubescape.io/docs/providers/#in-the-kubescape-operator)

Connecting to providers
=======================

A provider is a service which sends and receives data from Kubescape. To configure a provider with Kubescape, you must provide its server URL and your account ID on that service.

With a configured provider, you can download artifacts (custom frameworks, controls, attack tracks and configurations), and upload scan results.

Compatible providers
--------------------

*   [ARMO Platform](https://cloud.armosec.io/account/sign-up?utm_source=kubescapeio) is an enterprise solution based on Kubescape. It’s a multi-cloud and multi-cluster Kubernetes and CI/CD security platform behind a single pane of glass. ARMO Platform includes Kubernetes hardening and compliance assistance, misconfiguration scanning and remediation, prioritized container image vulnerability reporting, an RBAC investigator and more. Using ARMO Platform, you will save valuable time and make spot-on hardening decisions with contextual insights, based on the data from your scans and environment.

_To add your own provider here, [send a pull request](https://github.com/kubescape/kubescape.io/)._

Configuring a provider
----------------------

### In the Kubescape client

You can save configuration data for providers with `kubescape config`:

```
kubescape config set server <server URL>
kubescape config set accountID <accountID>
```

You can override this configuration with `--account <accountID>` and `--server <server>` on the command line.

### In the Kubescape Operator

When installing the operator, specify your account and server as Helm values using `--set account=<accountID>` and `--set server=<server URL>`.

[Previous Accepting risk](https://kubescape.io/docs/accepting-risk/)[Next MCP Server](https://kubescape.io/docs/mcp-server/)

 Copyright &copy; 2021 - 2026 [The Kubescape Authors](https://kubescape.devstats.cncf.io/d/66/developer-activity-counts-by-companies?orgId=1)

 Made with [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) and hosted by [Netlify](https://netlify.com/)

[](https://twitter.com/@kubescape "twitter.com")[](https://github.com/kubescape/kubescape "github.com")
