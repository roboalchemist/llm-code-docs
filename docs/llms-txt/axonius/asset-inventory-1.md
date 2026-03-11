# Source: https://docs.axonius.com/docs/asset-inventory-1.md

# Asset Inventory

## Introduction

**Audience:** SOC, Desktop and Server teams,  CMDB owners, IT/Help Desk & Security Tool owners

**Difficulty:** Beginner

**Execution Time:** 2 weeks to build initial dashboards and connect data sources, ongoing refinement as new data is identified.

**Duration of Use Case:** Perpetual

**Value:** Time saved, Cost reduction in identifying assets, Unparalleled visibility

**What is this use case?**

Asset Inventory involves the identification and stratification of all assets within any given environment. This use case directly ties to the concept of needing to see an asset before you can secure it.

**Use Case in Action:**

Asset Inventory is broken down into 2 distinct workflows: Identification of Asset Scope (and the adapters that support visibility of this scope) and Stratification of Asset Data (for the reporting of pertinent data points to relevant stakeholders). This use case generally includes the following focus areas:

* Business Metadata - Location, Business Unit/Company attribution, Device Ownership, Device Criticality
* Software Metadata - Operating System Family, End-of-life/End-of-Service devices, Firmware/Version Tracking
* Hardware Metadata - Device Model tracking, Device Manufacturer Breakdown

**Why is it Relevant?**

* Compliance with Standards: Essential for meeting regulations like ISO/IEC 27001, PCI DSS, GDPR, HIPAA, and more.
* Protecting your attack surface: Attack surface management starts with identifying what devices exist on your network
* Procurement Complexity: Identifying devices, their warranties, and their EOL/EOS dates is often a highly manual, cumbersome process. With Axonius, this becomes significantly easier, automating the discovery process for devices by leveraging existing, trusted sources of data.

### Scope

**How do I build this use case?**

**Adapter Selection**

Asset Inventory starts with an examination of your adapters and the scope of the inventory. Establish a baseline scope of devices (for example, endpoints, servers, and network infrastructure) and then establish which security consoles would have visibility on those devices.

In the process of establishing a scope, you will identify adapters that have been connected or not connected. The first true step is ensuring that the appropriate consoles are connected via adapters to your Axonius instance. This may require new adapters to be built or custom data to be ingested via flat files (such as CSV, JSON, or Excel files).

To ensure completeness, each source should:

* Accurately identify each asset (based on identifying attributes such as hostname/serial number, etc., for devices, or email/username for users)
* Capture accurate information that supports your end-goal (i.e., enriching OS information, Business Metadata, or Device Lifecycle Data, etc.)
* Provide a temporal metric that enables effective understanding of the recency of the data (such as last check-in time, last scan time, etc.)

**For example:**

Considering a Server, we may want to ascertain the following:

* Operating System Information - OS Type, Patching Status, EOL/EOS
* Ownership/Life Cycle - Status, Business Unit
* Software metadata - Installed Software/Vulnerabilities
* Hardware metadata - Uptime, CPU, RAM, HDD Size/Availability

Using the above information, it is possible to identify appropriate sources to give that information, which then makes up the adapter list required for a comprehensive inventory.

**Foundation Queries:**

Once adapters are connected, the next step is to establish the basis for reporting and analysis through foundation queries. In this stage, we establish a set of queries that will be the foundation not only for this use case but also for each subsequent piece of analysis in the system.

Examples of foundation queries:

1. **Scoping Queries**

   1. Establish what assets are in-scope or out-of-scope:

      1. In-Scope Device Examples: OS Type, Business Units, High Priority Assets
      2. Out-of-Scope Examples: Personal Devices, Cluster Servers, Recently Imaged (no agents installed), Single-Adapter and no MAC and Hostname, Approved Exceptions, Unsupported OS, and No Agent Installed

<Image align="center" border={false} width="624px" src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXctL9UF9lmWlZIBxEiIpQ94KGb72_EZ_0OO2YHA_iPEq4O1yDBKlCDSsoM3RUoujSmR0TPFXItYJdhArf-Os_TLbhR-NNXsOFWSVYajmRIibcJTE22jK3WQwowi8B77yUE5AkqOWg?key=rlLYpD5mVqjTRYNUoVM9swGO" height="275px" />

2. Capturing Metadata

   1. Next, we identify pieces of information that are either missing or captured inconsistently. In order to assist with capturing this data, business rules-based enhancements and CSV enrichments may be used to add in additional contextual information that is not otherwise captured in existing adapters.

<Image align="center" border={false} width="624px" src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXedJUsX3a7rpkwFDM1W_hzA63Ek00EBHlnASZL3h4P9Rt5ATMKSD-zx5ZBrWznDFCc0ZXutdhS_3QpyAV67ZMnsBJTm7CNNIli1ep4BPxWR2nxIjpAmHZzzMLqMLJ5A-g_e2eKqgQ?key=rlLYpD5mVqjTRYNUoVM9swGO" height="307px" />

2. Additionally, secondary sets of information from reference data sources can be added as an invaluable component for the asset inventory, adding in perspectives such as EOL/EOS dates, Association of Golden vs. Non-standard Images for Virtual Machines based on their OS/Build/AMI.

<Image align="center" border={false} width="624px" src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXcQCYp5cZdiKYhP8vT8McZH2NUS4iLw5oCrurGuqYzgJNem3nIhe7JAnpvn2W9yE-1Wbm_CB_Jqeb61iSdG24QCLUWtdIbyhbDebRA4RTJtt26b85kfRbaJfjZ6NU153mf1Eu1S5A?key=rlLYpD5mVqjTRYNUoVM9swGO" height="307px" />

## Visibility

How do I visually explain this use case?

Reporting on an asset inventory is highly subjective and dependent on the questions you wish to ask of your inventory. Be it something simple like: how many servers do I have? Or something complex, such as: how many critical servers do I have on the Windows 2008 Server operating system? Based on the questions you wish to answer, your initial visualisations will vary rapidly.

In the interest of examples, however, we have provided a few recommendations below:

**Recommended Visualizations**

When starting this use case, we recommend several key visualizations that attempt to answer key questions by leadership/executives.

**For Desktops:**

<Image align="center" border={false} width="624px" src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXfLxWGHGj-IoFcj9QwBp38q3XDXjobZvXaB-qEhA53zWPwiw1Vgbn2mY8Zh2PSAK7fARbXGcgJ1ushgkLa3FpFj7mAG0GKhAqzZ42YvVp5KTv4uU-Xx-esXe2ILqy2LhZfC1XFB?key=rlLYpD5mVqjTRYNUoVM9swGO" height="280px" />

|                       |                                                                                                                                                                                                                                                                                                            |
| --------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Data Point            | Typical Questions this solves                                                                                                                                                                                                                                                                              |
| Department(Not Shown) | How many desktops belong to my vital business functions?What are the devices that belong to my executive/leadership teams?How many devices do I need to account for in department X to be functional after a disaster?                                                                                     |
| Activity(Last Seen)   | What is my current Attack Surface of active Devices?How many Inactive Devices are there?Do I expect that many Inactive Devices?                                                                                                                                                                            |
| Manufacturer          | There is a known issue with manufacturer X. How many of those devices exist in my environment?I am gauging swapping vendors, how many devices do I have from that vendor?                                                                                                                                  |
| Location / Subnet     | I have a breach in Subnet X. How many devices are affected?How many devices do I have in my DMZ?How many devices exist at a location that I need DR for? (Business Continuity Management)I am planning on shutting down Office X and moving to a different space. How many desktops do I need to plan for? |
| Build/OS Distribution | How many Windows desktops do I have?How many desktops have an Operating system that will go end of life or end of support this year?How many desktops are not on my approved build of Windows?                                                                                                             |

**For Cloud Assets:**

<Image align="center" border={false} width="624px" src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXcsE4PthdjKnbIFPPQ4876A-o6l7ITixEfaXM1eCB66MB4e4bQiigdlz4PtSFeprHJt1wv6v31Wwa2ph6yVO0-c2phfTwJ3PIgQOFF3sq-pOBcAsaPsmJ6rTnCt5dfQwcC7_H5wuw?key=rlLYpD5mVqjTRYNUoVM9swGO" height="236px" />

|                           |                                                                                                                                                                   |
| ------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Data Point                | Typical Questions this solves                                                                                                                                     |
| Region/Availability Zones | In what regions do I have virtual machines?What redundancy do I have across regions and Availability Zones?                                                       |
| Asset Type                | What does my current cloud workloads look like (Serverless, vs. VM based vs. Autoscaled)                                                                          |
| Instance Sizing           | What is the current breakdown of cloud infrastructure above a certain tier?What are my biggest cloud VMs currently running                                        |
| Deployed Images           | Are all my virtual machines leveraging my golden images?Are any of my virtual machines leveraging publicly available images?                                      |
| Reservation Type          | Are all of my Virtual Machines leveraging the most cost-effective cloud reservation type?What is the prevalence of Short-Term/Spot instances in my AWS instances? |

## Actionability

**How do I automate this use case?**

Automation provides invaluable enhancements to Asset Inventory, allowing for the incorporation of business rules into enriching metadata, supplementing adapter information using CSV enrichments, and finally building out key reports for use by stakeholders from analysts to the C-suite.

**Enhancement of Data**

Leveraging the Custom Data, Tagging, and CSV Enrichment enforcements, users may be able to extend the scope of data already captured in Axonius. This may help incorporate additional data (or error-prone data) such as:

* Device Ownership
* Compatibility with Security Tooling
* Business Criticality
* Infrastructure Supporting Critical Assets

**Reporting**

Automatically deliver timely, detailed, and accurate reports to stakeholders through emails, PDF reports, and CSV exports.

**Examples Include:**

* Send Email
* Send CSV to S3
* Send CSV to Azure Storage
* Microsoft Teams – Send Message
* Slack – Send Message
* Reports (Send Dashboard)

**Ticketing**

Automatically create work tickets for responsible parties directly in your ticketing system of choice, creating seamless workflows without relying on inbox spelunking.

**Examples Include:**

* ServiceNow – Create Incident
* Jira Service Management – Create Ticket
* Fresh Service – Create Ticket
* Cherwell – Create Incident
* Opsgenie – Create Alert
* Zendesk – Create Ticket
* Manage Engine ServiceDesk Plus – Create Request

**Remediation**

Automatically remediate assets out of compliance (i.e., assets with a broken/out-of-date agent or with no connection to the tool/agent console)

**Examples Include:**

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

##