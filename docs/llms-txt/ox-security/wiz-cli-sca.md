# Source: https://docs.ox.security/ox-integrations/3rd-party-integrations/open-source-security/wiz-cli-sca.md

# Wiz CLI SCA

{% hint style="info" %}
Wiz connects to OX across four categories. This article covers all four types:

* **Secret/PII Scan:** Wiz CLI Secrets
* **Open Source Security:** Wiz CLI SCA
* I**nfrastructure as Code Scan:** Wiz CLI IaC
* **Cloud Context:** Wiz Cloud
  {% endhint %}

Integrate Wiz with OX to centralize security findings alongside container, pipeline, cloud, and runtime signals already in OX.

OX scans Wiz on a schedule and on demand, enriches findings with OX context (application mapping, workflows, and compliance), and presents a unified queue for investigation and reporting.

After you connect, Wiz scan results appear on the Active Issues page (use the filter **Source tool > Wiz**).

## What OX adds

* **Context and correlation:** OX maps Wiz findings to applications, services, and teams to show impact and ownership.
* **Prioritization with severity factors:** OX may reprioritize scanner severities when exploitability and environment context reduce risk (for example, Critical → High). Severity factors explain why the priority changed.
* **Evidence at a glance:** When available, OX displays scanner evidence, file locations, and remediation guidance alongside OX analytics to speed triage.

## Connection methods

For general information about connection methods, see the article [Connection methods](https://docs.ox.security/get-started/onboarding-to-ox/source-control/connection-methods).

All connection methods use the same Wiz service account credentials: Client ID and Client Secret.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-43558fee0dc67e1f1553eab1fa1efe859b00a6a5%2Fwiz%204%20connectors.jpg?alt=media" alt=""><figcaption></figcaption></figure>

There are four methods to connect Wiz to OX:

* **Wiz CLI Secrets:** Scan for secrets and PII in your codebase through the Wiz CLI.
* **Wiz CLI SCA:** Scan open-source dependencies through the Wiz CLI.
* **Wiz CLI IaC:** Scan Infrastructure as Code configurations for security issues through the Wiz CLI.
* **Wiz Cloud (Cloud Context):** Scan cloud locations and identify critical risks in AWS, Azure, GCP, and Kubernetes. Requires API URL configuration.

For setup instructions, see the main article [Wiz](https://docs.ox.security/ox-integrations/3rd-party-integrations/cloud-context/wiz) in the Cloud Context folder.
