# Source: https://docs.ox.security/ox-integrations/3rd-party-integrations/cloud-context.md

# Cloud Context

Cloud context platforms collect runtime, posture, and exposure data from your cloud and infrastructure environments. This data describes what is actually deployed, reachable, and running in production.

OX connects to third-party cloud security and infrastructure tools to import this data, enrich it with OX context, and present it alongside findings from SAST, SCA, DAST, and pipeline scanning.

OX does not scan your cloud environment directly through these integrations. Each connector reads data through the vendor’s API, then maps cloud assets, workloads, and posture signals to your applications, repositories, and workflows in OX so you can triage, prioritize, and report consistently.

### Where You Will See Cloud Context Data in OX

* **Active Issues**: Filter by Source tool to focus on findings enriched by a specific cloud provider.
* **Issue details**: Tabs include cloud asset data, exposure indicators, runtime context, and OX correlations such as application and repository mapping.
* **Assets and Applications**: Imported cloud assets and workloads appear in asset views, application context, and dashboards.
* **Risk prioritization**: Findings are ranked using combined development, pipeline, and runtime signals.

### Supported Connectors

The following cloud context connectors are supported:

* OX Cloud Context
* Kong
* Microsoft Defender for Cloud
* Oligo
* Orca Security
* PAN: Prisma Cloud (CSPM)
* Sentinel One
* Upwind
* Qualys
* Solace
* Sysdig
* Tenable
* Tenable Cloud Security
* Wiz

When a cloud context connector is active, OX continuously imports cloud posture, workload, and exposure data and links it to existing security findings across your environment.

### How Data from Cloud Context Connectors Is Used by OX

Each connected platform can provide different types of cloud context, depending on the vendor and the permissions you configure. This may include:

* Cloud asset identifiers, such as virtual machines, containers, clusters, and services
* Exposure and reachability indicators, such as internet-facing or network-accessible assets
* Runtime signals, such as active workloads and observed processes
* Posture and configuration data, such as misconfigurations and policy violations
* Provider-specific metadata used to improve asset and application mapping

This information helps OX determine which issues affect running systems and which findings represent theoretical risk only.

### Choosing a Cloud Context Provider

Different cloud context platforms specialize in different types of visibility. Your choice should reflect what kind of signal you want to bring into OX.

* **Posture-focused platforms**\
  These platforms emphasize configuration and compliance across cloud accounts, subscriptions, and services. Use them if your priority is identifying misconfigurations, policy violations, and cloud governance gaps.
* **Runtime-focused platforms**\
  These platforms monitor running workloads, processes, and behaviors in real time. Use them if you need visibility into what is actively executing in your environment and how workloads behave at runtime.
* **Exposure and attack surface platforms**\
  These platforms focus on identifying internet-facing, reachable, or externally exposed assets. Use them if your priority is understanding which systems are accessible from outside your environment.

If you already use a cloud security platform, start with that provider to extend its visibility into OX. You can also connect more than one provider to combine posture, runtime, and exposure signals in a single risk view.

***
