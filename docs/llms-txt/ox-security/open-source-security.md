# Source: https://docs.ox.security/ox-integrations/3rd-party-integrations/open-source-security.md

# Open Source Security

Open Source Security connectors connect OX to software composition analysis (SCA) tools that identify vulnerabilities, license risks, and outdated dependencies in open source libraries and third-party components

OX imports data from these tools through APIs, enriches it with OX context (application mapping, ownership, workflows, and compliance), and presents it alongside findings from other scanners and tools in a unified view.

## What OX adds

* **Context and correlation:** OX maps findings to applications, services, and teams to show impact and ownership.
* **Prioritization with severity factors:** OX may reprioritize scanner severities when exploitability and environment context reduce risk (for example, Critical → High). Severity factors explain why the priority changed.
* **Evidence at a glance:** When available, OX displays scanner evidence, file locations, and remediation guidance alongside OX analytics to speed triage.

## **Where data appears in OX**

* **Active Issues:** Filter by **Source tool** to focus on findings from a specific connector.
* **Issue details:** Tabs show scanner evidence, asset data, and OX correlations such as application and repository mapping.
* **Assets and applications:** Imported assets appear in asset views, application context, and dashboards.
* **Risk prioritization:** Findings are ranked using combined development, pipeline, and runtime signals.

## Supported connectors

* Black Duck
* Checkmarx SCA
* Coverity on Polaris
* Fortify on Demand
* Fossa
* GitHub Dependabot
* GitLab Dependency Scanning
* HCL AppScan
* OX Open Source Security
* Semgrep Enterprise
* Snyk
* Sonatype Nexus IQ CLI
* Sonatype Veracode
* WhiteSource
* Wiz CLI SCA: OX supports multiple Wiz connectors. For setup instructions, see the article [Wiz](https://docs.ox.security/ox-integrations/3rd-party-integrations/cloud-context/wiz)in the Cloud Context folder.
