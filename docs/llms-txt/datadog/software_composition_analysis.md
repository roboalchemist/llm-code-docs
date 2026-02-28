# Source: https://docs.datadoghq.com/security/code_security/software_composition_analysis.md

---
title: Software Composition Analysis
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > Code Security > Software Composition Analysis
---

# Software Composition Analysis

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Overview{% #overview %}

Software Composition Analysis (SCA) detects open source libraries in both your repositories and running services, providing end-to-end visibility of library vulnerabilities and license management from development to production.

Using Software Composition Analysis provides organizations with the following benefits:

- Identification of emerging and known vulnerabilities affecting open source libraries
- Risk-based prioritization and remediation based on runtime detection of vulnerabilities
- Identification of malicious packages, end-of-life libraries, and library riskiness based on OpenSSF standards

Datadog SCA uses a curated proprietary database. The database is sourced from Open Source Vulnerabilities (OSV), National Vulnerability Database (NVD), GitHub advisories, and other language ecosystem advisories, as well as Datadog's own Security Research team's findings. There is a maximum of 2 hours between when a new vulnerability is published and when it appears in Datadog, with emerging vulnerabilities typically appearing in Datadog within minutes.

## SCA language support{% #sca-language-support %}

Software Composition Analysis (SCA) supports the following languages:

- [python](#set-up-sca)
- [javascript](#set-up-sca)
- [java](#set-up-sca)
- [c sharp](#set-up-sca)
- [go](#set-up-sca)
- [ruby](#set-up-sca)
- [php](#set-up-sca)
- [php](#set-up-sca)
- [go](#set-up-sca)
-
-
-

For steps on setting up SCA for your language, see [Set up SCA](https://docs.datadoghq.com/security/code_security/software_composition_analysis/#set-up-sca).

## Set up SCA{% #set-up-sca %}

SCA supports both static and runtime dependency detection:

- For **static detection**, you can scan your repositories from your CI/CD pipelines or directly from Datadog's infrastructure. See [static setup](https://docs.datadoghq.com/security/code_security/software_composition_analysis/setup_static/) to get started.
- For **runtime detection**, you can enable SCA on services instrumented with Datadog APM. See [runtime setup](https://docs.datadoghq.com/security/code_security/software_composition_analysis/setup_runtime/) to get started.

## Search and filter results{% #search-and-filter-results %}

### Vulnerabilities explorer{% #vulnerabilities-explorer %}

The [Vulnerabilities](https://app.datadoghq.com/security/appsec/vm/library) explorer provides a vulnerability-centric view of library vulnerabilities detected by SCA, alongside vulnerabilities detected by other Code Security capabilities (SAST and IAST). All vulnerabilities in the explorer are either detected on the default branch at the last commit of a scanned repository, or are affecting a running service.

### Datadog severity score{% #datadog-severity-score %}

Each vulnerability begins with a base CVSS score. To assist in prioritizing remediation, Datadog modifies the base CVSS score into the Datadog Severity Score by incorporating runtime context and exploitability signals. These factors help distinguish theoretical risk from vulnerabilities that are more likely to be exploited in real-world environments. The table below describes how each factor influences the final score.

| Risk factor                     | How it is evaluated                                                  | Impact on the score                                    |
| ------------------------------- | -------------------------------------------------------------------- | ------------------------------------------------------ |
| Base CVSS score                 | Published CVSS score for the vulnerability.                          | Starting point for the severity score.                 |
| Reachability                    | Whether the vulnerable code path is actually executed.               | Increased when the vulnerable code is invoked.         |
| Production runtime context      | Whether the affected service is running in a production environment. | Decreased if the service is not running in production. |
| Under attack                    | Evidence of active attack activity targeting the service.            | Decreased if there is no observed attack activity.     |
| Exploit availability            | Availability of public exploits for the vulnerability.               | Decreased if no exploit is available.                  |
| Exploitation probability (EPSS) | Likelihood of real-world exploitation based on EPSS data.            | Decreased when the probability of exploitation is low. |

### Repositories explorer{% #repositories-explorer %}

The [Repositories](https://app.datadoghq.com/ci/code-analysis) explorer provides a repository-centric view of all scan results across Static Code Analysis (SAST) and Software Composition Analysis (SCA). Click on a repository to analyze **Library Vulnerabilities** and **Library Catalog** results from SCA scoped to your chosen branch and commit.

- The **Library Vulnerabilities** tab contains the vulnerable library versions found by Datadog SCA
- The **Library Catalog** tab contains all of the libraries (vulnerable or not) found by Datadog SCA.

Recommended steps for remediating detected vulnerabilities can be found in the side panel for each vulnerability in SCA. Steps are provided for upgrading the library to the safest (non-vulnerable) version, as well as the closest version.

To filter your results, use the facets to the left of the list or the search bar at the top. Results can be filtered by service or team facets. For more information about how results are linked to Datadog services and teams, see [Getting Started with Code Security](https://docs.datadoghq.com/getting_started/code_security/).

Every row represents a unique library and version combination. Each combination is associated with the specific commit and branch that is selected in the filters at the top of the page (by default, the latest commit on the default branch of the repository you selected).

Click on a library with a vulnerability to open a side panel that contains information about remediation steps.

### Library inventory{% #library-inventory %}

The [Library Inventory](https://app.datadoghq.com/security/appsec/inventory/libraries) provides visibility into the third-party libraries detected across your codebase. Datadog collects this information from:

- **Static SCA**, which identifies all libraries referenced in your repositories, and
- **Runtime SCA**, which detects libraries that are actually loaded and used by your services at runtime.

Use the Library Inventory to understand which dependencies you rely on, where they are used, and whether they contain known vulnerabilities or license risks.

To learn more about how the inventory is generated, how Static and Runtime data differ, and how to interpret the library details (usage, vulnerabilities, licenses, versions, and OpenSSF score), see [Library Inventory](https://docs.datadoghq.com/security/code_security/software_composition_analysis/library_inventory).

### Library vulnerability context in APM{% #library-vulnerability-context-in-apm %}

SCA enriches the information Application Performance Monitoring (APM) is already collecting by flagging libraries that match with current vulnerability advisories. Potentially vulnerable services are highlighted directly in the **Security** view embedded in the [APM Software Catalog](https://app.datadoghq.com/services?lens=Security).

- Whether it is reaching end of life
- Whether it is a malicious package
- The health of this library version based on its OpenSSF scorecard breakdown
- Software supply chain & Software Bill of Materials (SBOM) management

### Vulnerability lifecycle{% #vulnerability-lifecycle %}

Vulnerabilities detected in libraries by SCA **at runtime** are closed by Datadog after a certain period, depending on the service's usage of the vulnerable library.

- **Hot Libraries:** Libraries from services that are alive for more than 2 hours.

  - **When vulnerabilities are auto-closed by Datadog:** After 1 hour, if they are not detected again and the service is running on all environments where the vulnerability was detected.

- **Lazy Libraries:** Libraries that are loaded more than 1 hour after the service has started.

  - **When vulnerabilities are auto-closed by Datadog:** After 5 days, if they have not been detected again during this period.

- **Cold Libraries:** Libraries from services that are alive for less than 2 hours (such as jobs).

  - **When vulnerabilities are auto-closed by Datadog:** After 5 days, if they have not been detected again during this period.

## Further Reading{% #further-reading %}

- [Detect and block exposed credentials with Datadog Secret Scanning](https://www.datadoghq.com/blog/code-security-secret-scanning)
