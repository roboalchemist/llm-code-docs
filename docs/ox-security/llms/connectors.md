# Source: https://docs.ox.security/ox-integrations/connectors.md

# About Connectors

{% hint style="success" %}
**At a glance:** Integrate your infrastructure systems and (optionally) additional security tools with OX to get your full application security posture in our single, centralized platform – providing complete coverage, issue aggregation and prioritization, and automation.
{% endhint %}

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-84a3bbdf7caf446d7883f26f8c9437a746b1071d%2Fconnectors.png?alt=media" alt=""><figcaption></figcaption></figure>

## Overview

The **Connectors** page is the single location from which you can connect your infrastructure and security tools to OX.

OX supports 2 primary types of connectors:

* Development & production infrastructure
* Security tools

Additionally, you can connect tools such as ChatGPT, Jira, Slack, Logz.io, and Splunk to facilitate collaboration and remediation of issues.

You can find a full list of all supported connectors [here](https://docs.ox.security/supported-connectors-1).

### Development & production infrastructure

These are the systems that provide your supply chain infrastructure, including:

* Source control systems (such as GitHub, GitLab, and Bitbucket)
* CI/CD systems (such as Jenkins and Azure Pipelines)
* Registries (such as Docker Hub and JFrog)
* Cloud deployment infrastructure (such as AWS and Google Cloud Platform)

### Security tools

These are the security tools that scan and secure your software throughout the development lifecycle.

* OX provides complete coverage for each lifecycle stage with its combination of proprietary and open-source tools (such as Trivy, Bandit, DevSkim, Semgrep, GitLeaks, Checkov, and Prowler).
* We also provide you the flexibility to integrate other dedicated, security tools you are using (either commercial or open source) into the OX platform.
  * Examples of these tools include Snyk for SCA, Checkmarx for static code analysis, or Prisma for CSPM.

#### OX security tools

By default, OX security tools (proprietary and open source) are enabled to provide **full supply chain coverage out of the box** in the optimal configuration for your environment.

OX tools cover any stage you have not protected with dedicated tools. Additionally, all of these tools can work in parallel with any dedicated security tools you already have installed. In other words, you can keep the OX tools active even if you do add additional tools to cover specific categories.

Of course, you can elect to disable any of the OX tools according to your needs.

## Connecting your tools

To connect a tool, click its box on the **Connector** page. Each tool has its specific connection options and instructions. Usually, the connection can be made using one or more of the following methods:

* Identity provider
* Token
* Username & password
* Shared secret

Specific instructions for each connector can be found inside its box on the **Connectors** page. For certain connectors, additional details are available in the **Making connections** section of this help center.

### Connection status

An icon in a connector's box on the **Connectors** page indicates its status:

<table><thead><tr><th width="80" align="center"></th><th></th></tr></thead><tbody><tr><td align="center"><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-1bc61660ab2d3de94162ab7ac64b1c04337d7ace%2Fconnected.png?alt=media" alt="" data-size="line"></td><td>Tool is connected and active</td></tr><tr><td align="center"><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-45ef5f6b111c7df7fbb30ab8869dbb155b9e6604%2Fnot_connected_icon.png?alt=media" alt="" data-size="line"></td><td>Tool was discovered in your environment, but it is not yet connected</td></tr><tr><td align="center"><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-65925dba0daeedf07c233908c9ade27e31786c99%2Fbroken_connection.png?alt=media" alt="" data-size="line"></td><td>Tool was connected, but there are connection issues</td></tr></tbody></table>
