# Source: https://docs.firehydrant.com/docs/acronyms-and-glossary.md

# Acronyms and Glossary

This page covers acronyms and terms not covered on the [main website's glossary](https://firehydrant.com/glossary/). This page goes into more technical details and will link to additional resources and reading when necessary.

## Definitions

### Contributing Factors

**One of many potential issues that contributed to causing an incident.** This is FireHydrant's recommended terminology and method for tracking what others may call "root causes."

Generally, systems are so complex that rarely, if ever, can a significant issue be boiled down to a single item gone wrong (ergo, "root cause"). For a more detailed essay, read John Allspaw's blog post ([#2 below](#additional-reading)) in Additional Reading.

### DORA Metrics

The DORA (DevOps Research Assessments) team was a Google research group that did a 7-year program analyzing tech companies and what separated high from low performers. Their research resulted in the 4 "DORA metrics" that the industry has adopted to gauge a company's performance/DevOps maturity:

* **Deployment Frequency (DF)**: How often an organization pushes new features/changes. More is better.
* **Lead Time for Changes (LT)**: How long it takes to make changes and deploy them. Shorter is better.
* **Mean Time To Recovery (MTTR)**: How long it takes to recover from an outage. Shorter is better.
* **Change Failure Rate (CFR)**: How often new changes & deployments break things. Less is better.

You may recognize **MTTR**, a common metric SRE teams use to gauge reliability and a metric we also offer in [our Analytics](https://docs.firehydrant.com/docs/analytics-basics).

### Service Ownership

**The principle or idea that "if you build it, you own it."** Service Ownership refers to development or engineering teams owning their parts of the system throughout the entire lifecycle, including responding to incidents involving said services.

The idea runs somewhat contrary to a **NOC**, where a single team steps in for all issues and incidents regardless of whether they were involved in developing and deploying impacted services.

## Acronyms

These are acronyms either commonly used in the industry or encountered by individual FireHydrant employees during calls or conferences. We've added these here to share the knowledge.

| Acronym | Definition                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| CMDB    | **Configuration Management Database**. A central repository or database storing information about your IT environment and infrastructure. Often used by larger enterprises that need deep auditing and logging of all settings and changes in their systems.                                                                                                                                                                                                                  |
| DRI     | **Directly Responsible Individual**. Term coined by Apple to refer to someone who ultimately owns a project or outcome. Has been rarely used to refer to Service Owners or Incident Commanders.                                                                                                                                                                                                                                                                               |
| IM      | **Incident Management**. Sometimes used interchangeably with **IR**. FireHydrant considers Response and Management different things, where Response is reactive and Management is proactive.                                                                                                                                                                                                                                                                                  |
| IMOC    | **Incident Manager On-Call.** Individual who owns an incident and often leads and coordinates the response team through handling an incident. Often used interchangeably with **Incident Commander**.                                                                                                                                                                                                                                                                         |
| IR      | **Incident Response**. Sometimes used interchangeably with **IM**. FireHydrant considers Response and Management different things, where Response is reactive and Management is proactive.                                                                                                                                                                                                                                                                                    |
| KEDB    | **Known Error Database**. A place to track problems found, including root causes of incidents. It could be sophisticated, like an actual issue tracker, or rudimentary, like a spreadsheet or text document. Often used by IT teams.                                                                                                                                                                                                                                          |
| NOC     | **Network Operations Center**. Usually a specialized team or location for monitoring network and infrastructure performance. NOC teams function as an umbrella layer of defense, responding to all incidents when detected. This is a more traditional form of incident management and runs contrary to **Service Ownership**, where engineering teams will react independently to incidents involving their services.                                                        |
| PIR     | **Post-Incident Review**. Used interchangeably with **Postmortems**, **Retrospectives**, and sometimes **RCAs**. See the [Retrospectives page](https://firehydrant.com/glossary/retrospective/).                                                                                                                                                                                                                                                                              |
| RCA     | **Root Cause Analysis**. The process of identifying and analyzing what caused the incident. Sometimes used to refer to the incident review process overall (e.g., like a **Retrospective**).                                                                                                                                                                                                                                                                                  |
| RFO     | **Reason For Outage**. Another acronym equivalent to **root cause**.                                                                                                                                                                                                                                                                                                                                                                                                          |
| SEV     | **Severity**. A shortening of the word "Severity", which is how many organizations measure "how bad" an incident is. Typically measured on a single-digit scale (e.g., SEV1, SEV2, SEV3, etc.) but can vary by organization. Sometimes, people colloquially refer to incidents as "SEVs".                                                                                                                                                                                     |
| SLA     | **Service Level Agreement**. Contract/agreement between a company and its clients about service delivery expectations. Typically, it includes uptime, availability, performance, and more. Suppose the company fails to deliver according to the contract (e.g., uptime falls below 99.9%). In that case, the company breaches the SLA, and there may be consequences such as refunds of credits to clients or even legal ramifications. See [#3](#additional-reading) below. |
| SLI     | **Service Level Indicator**. SLIs are the actual, measured values of some metric in your infrastructure. You can think of **SLOs** as the "ideal" level and **SLIs** as the "actual" level. If an SLI does not meet an SLO, there may be a breach of SLA. See [#3](#additional-reading) below.                                                                                                                                                                                |
| SLO     | **Service Level Objective**. The specified goal or "ideal" level of some metric in your infrastructure. For example, you may define a 500ms response time on a particular query. If the SLI, or the measured response time at a particular moment, exceeds 500ms, then the SLO is not met. See [#3](#additional-reading) below.                                                                                                                                               |
| SME     | **Subject Matter Expert**. Sometimes used to refer to key individuals who know a lot about, or own, specific services and functions in a system. Used more often than **DRI**.                                                                                                                                                                                                                                                                                                |
| SOP     | **Standard Operating Procedure**. Refers to any codified process. Sometimes used to refer to incident management/response processes.                                                                                                                                                                                                                                                                                                                                          |
| SRE     | **Site Reliability Engineering**. A discipline and term coined by Google, who found that they needed an entirely new team/practice for managing their huge infrastructure at scale. See [#1 below](#additional-reading).                                                                                                                                                                                                                                                      |

## Additional Reading

1. [What is SRE? (Google)](https://sre.google/)
2. [Each necessary, but only jointly sufficient (John Allspaw)](https://www.kitchensoap.com/2012/02/10/each-necessary-but-only-jointly-sufficient/)
3. [Service Level Objectives (Google)](https://sre.google/sre-book/service-level-objectives/)