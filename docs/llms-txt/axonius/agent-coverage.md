# Source: https://docs.axonius.com/docs/agent-coverage.md

# Agent Coverage & Health

**Manage & Optimize Assets**

<HTMLBlock>
  {`
  <iframe src="https://fast.wistia.net/embed/iframe/667gwtjjy8?web_component=true&amp;seo=false&amp;videoFoam=false" frameborder="0" allowfullscreen="true" allow="autoplay; fullscreen" title="Security Tool Coverage Video" style="display:flex;margin-right:auto;width:640px;height:360px;" width="640" height="360" allowtransparency="true" scrolling="no" class="wistia_embed" name="wistia_embed" dataalign="left" datadisplay="flex"></iframe>
  `}
</HTMLBlock>

## **Introduction**

Agent Coverage is one of the cornerstones of Axonius. It is a simple use case that lasts indefinitely and is extremely quick to implement.

**Audience:** SOC, Desktop and Server teams, & Security Tool owners

**Difficulty:** Beginner

**Execution Time:** 1 week per tool, ongoing refinement

**Duration of Use Case:** Perpetual

**Value:** Time saved & license cost reduction

**What is this use case?**

The primary objective of Agent Coverage is ensuring every asset is observed and protected by your security tool suite. This use case forms the foundation for multiple others, enabling you to understand the overall coverage of each security tool and an important facet of the risk related to each endpoint.

**Use Case in Action:**

We’ll use Crowdstrike coverage to demonstrate this use case today, however, this use case applies to a multitude of agent tools, including:

* Endpoint Protection (EPP)
* Endpoint Detection and Response (EDR)
* Extended Detection and Response (XDR)
* Security Information and Event Management (SIEM)
* Endpoint Management

**Why is it Relevant?**

* Compliance with Standards: Essential for meeting regulations like ISO/IEC 27001, PCI DSS, GDPR, HIPAA, and more.
* Protecting your attack surface: Ensuring assets are hardened from attack through your security tool suite.

## Scope

**How do I build this use case?**

The starting point for Agent Coverage is always queries, with a focus on three core areas: Scoping Queries, Metric Queries, and Combination/Presentation Queries. Each of the below queries is essential in identifying a device's context and providing insight into the tools appropriate for that context. It will also underpin the visualization and automation components for this use case.

1. **Scoping Queries**

   1. Establish what assets are in-scope or out-of-scope:

      1. In-Scope Examples: OS Type, Business Units, High Priority Assets
      2. Out-of-Scope Examples: Personal Devices, Cluster Servers, Recently Imaged (no agents installed), Single-Adapter and no MAC and Hostname, Approved Exceptions, Unsupported OS, and No Agent Installed![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-F8TFIRV6.png)

**Metric Queries (Crowdstrike)**

1. Examples: Tool Footprint, Agent Version, Recently scanned or not (Vulnerability Scanners)![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-TH3DXDHM.png)

**Combine Scoping and Metric Queries**

1. In-scope devices missing Crowdstrike
2. In-scope devices with out-of-date agents ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-NDK6PL42.png)

## Visibility

**How do I visually explain this use case?**

Reporting on agent coverage is often expected as a singular number: What percentage of my devices are covered (or not covered)? However, visually explaining the use case requires several facets to ensure executives and analysts alike understand the trajectory of each agent’s coverage.

**Recommended Visualizations**

When starting this use case, we recommend several key visualizations that attempt to answer key questions by leadership/executives.

**Coverage Measurement** – How many of my devices are missing this tool?

<Image align="center" border={false} width="456px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-WLTPSJGD.png" height="auto" />

**Coverage Trend**– Is my coverage improving or declining?

<Image align="center" border={false} width="803px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-CBRNV7Z8.png" height="auto" />

**Agent Health**– Are all of my agents healthy and up-to-date?

## Actionability

**How do I automate this use case?**

Automation is a key component for the Agent Coverage use case, allowing us to immediately take action to resolve the issues we identify. We can break this down into several categories of automation, in increasing order of complexity.

**Reporting**

Automatically deliver timely, detailed, and accurate reports to stakeholders through emails, PDF reports, and CSV exports.

Examples Include:

* Send Email
* Send CSV to S3
* Send CSV to Azure Storage
* Microsoft Teams – Send Message
* Slack – Send Message
* Reports (Send Dashboard)

**Ticketing**

Automatically create work tickets for responsible parties directly in your ticketing system of choice, creating seamless workflows without relying on inbox spelunking.

Examples Include:

* ServiceNow – Create Incident
* Jira Service Management – Create Ticket
* Fresh Service – Create Ticket
* Cherwell – Create Incident
* Opsgenie – Create Alert
* Zendesk – Create Ticket
* Manage Engine ServiceDesk Plus – Create Request

**Remediation**

Automatically remediate assets out of compliance (i.e., assets with a broken/out-of-date agent or with no connection to the tool/agent console)

Examples Include:

* Axonius Deploy Files and Run Shell Commands (Windows or Linux)
* Absolute - Run Script
* Automox - Install Update or Run Worklet
* BigFix - Create Fixlet Action
* Chef - Run Command
* ConnectWise Automate - Deploy Patches
* CrowdStrike Falcon - Run Script, Add Tagging Group, Isolate Asset
* Kenna - Add tags to Assets
* MECM - Add Assets to Collection
* Microsoft Entra ID - Change Group or Role Assignment
* Microsoft AD - Change Groups or LDAP Attributes
* Qualys - Execute Script, add IPs to scan, or Tag Assets
* Quest KACE - Run Script
* Red Hat Ansible Tower - Run Command
* SentinelOne - Run Scan or Remote Script, Isolate Asset
* Tanium - Create Action or Software Deployment
* Tenable.io - Add IP Addresses to Scan, Tag Assets

**Reach out to your Sales Engineer or TAM for the latest Agent Coverage Dashboards!**