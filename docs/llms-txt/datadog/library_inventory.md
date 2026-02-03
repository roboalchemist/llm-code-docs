# Source: https://docs.datadoghq.com/security/code_security/software_composition_analysis/library_inventory.md

---
title: Library Inventory
description: >-
  The Library Inventory provides a unified view of all third-party libraries
  detected across your codebase and services.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Software Composition Analysis >
  Library Inventory
---

# Library Inventory

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

The [Library Inventory](https://app.datadoghq.com/security/code-security/inventory/libraries) provides a unified view of all third-party libraries detected across your codebase and services. It helps you understand which components you depend on, which versions are in use, and where vulnerabilities or license risks might exist. The inventory is built from two complementary data sources:

- **Static Software Composition Analysis (Static SCA)**, which scans your repositories to identify every library referenced in your source code.
- **Runtime Software Composition Analysis (Runtime SCA)**, which detects libraries that are actually loaded and used at runtime by your services. This combined visibility helps you distinguish between theoretical dependencies and real risk exposure.

## Static view{% #static-view %}

The **Static** view lists all libraries referenced in your repositories as detected by **Static SCA**.

Static SCA analyzes dependency files and source code to identify all declared third-party libraries, regardless of whether they are used at runtime. Use this view to:

- See your complete dependency footprint
- Identify libraries present in specific repositories
- Track dependency versions and upgrade needs
- Explore vulnerabilities and license metadata for all referenced libraries

Static data updates on every repository scan.

## Runtime view{% #runtime-view %}

The **Runtime** view lists only the libraries actively used by your services in production or other monitored environments, as detected by **Runtime SCA**.

Runtime SCA observes loaded dependencies through the Datadog tracing library, enabling you to:

- Prioritize vulnerabilities in libraries that are actually executed
- Reduce noise by filtering out unused dependencies
- Understand real exposure to vulnerable components
- Map vulnerable libraries to the services and environments using them

This view updates continuously as your services run.

## Library details{% #library-details %}

Clicking any library in the inventory opens the library detail panel, which provides an in-depth view of its metadata, vulnerabilities, and usage.

The panel includes the following sections.

### Overview{% #overview %}

Displays key information about the selected library and version, including:

- **Security status** (count of Critical, High, Medium, Low vulnerabilities)
- **License type**
- **Version status** (older version, actively maintained, deprecated, etc.)
- **Popularity** and download statistics when available

This section provides a snapshot of the security and maintenance posture of the dependency.

{% image
   source="https://datadog-docs.imgix.net/images/security/code_security/overview.b88d57ed59a885a2ba932ba36f8ba530.png?auto=format"
   alt="a snapshot of the security and maintenance posture of the dependency" /%}

### Repositories{% #repositories %}

Shows all repositories where this library is referenced, as detected by **Static SCA**.

For each repository, you can see:

- The file and path where the dependency was declared
- Whether the dependency is direct or transitive
- The first detection timestamp
- The latest scanned commit

Use this view to understand how widely the library is used across your codebase.

{% image
   source="https://datadog-docs.imgix.net/images/security/code_security/repositories.3ebbc224d27619f6dfa8c13924a5d832.png?auto=format"
   alt="a snapshot of the security and maintenance posture of the dependency" /%}

### Services{% #services %}

Shows all services that load this library at runtime, as detected by **Runtime SCA**.

For each service, you can view:

- The environments where it is running (for example, env:dev, env:prod)
- The team responsible (when available)
- The first time the library was detected in that service

If no services appear, the library is referenced statically but not used at runtime.

{% image
   source="https://datadog-docs.imgix.net/images/security/code_security/services.234f8d278999ca26a0434504d7383815.png?auto=format"
   alt="services that load this library at runtime" /%}

### Security{% #security %}

Lists all known vulnerabilities affecting this library version, including:

- Severity (Critical, High, Medium, Low)
- CVE or advisory ID (for example, GHSA identifiers)
- A short description of each vulnerability
- Links to the full vulnerability details

This section consolidates all vulnerabilities detected by Datadog from upstream security advisories.

{% image
   source="https://datadog-docs.imgix.net/images/security/code_security/security.b2e3423889a9bfd38512b1cc6712ee9b.png?auto=format"
   alt="all known vulnerabilities affecting this library version" /%}

### Licenses{% #licenses %}

The license table in this section is based on the **Choose a License Appendix**: [https://choosealicense.com/appendix/](https://choosealicense.com/appendix/)

It summarizes the license's:

- **Permissions****Conditions**
- **Limitations**

Additionally, Datadog identifies **license risks**, including:

- **Network copyleft**: code must be released when offered as a network service
- **Strong copyleft**: derivative work must be open-sourced under the same license
- **Non-standard copyleft**: copyleft terms differ from common OSI-approved patterns
- **Non-commercial**: use is restricted to non-commercial contexts
- **Non-standard / Non-free**: license does not meet standard open-source definitions

Each risk contains a short explanation and links to more detailed license information.

{% image
   source="https://datadog-docs.imgix.net/images/security/code_security/licenses.dcd58528e41a2bc30126e15fd918009a.png?auto=format"
   alt="license summary" /%}

### Versions{% #versions %}

Lists all known versions of the library, along with:

- Release dates
- Vulnerability counts for each version
- Whether the version is used in your repositories or services

This helps you evaluate remediation options and identify safer upgrade paths.

{% image
   source="https://datadog-docs.imgix.net/images/security/code_security/versions_of_this_library.fca43e41a71a95b1b6aeb638f9541713.png?auto=format"
   alt="all known versions of the library" /%}

### OpenSSF score{% #openssf-score %}

Displays the **OpenSSF Scorecard** results for the upstream project. Each check provides insight into the project's security maturity, such as:

- Maintenance activity
- Use of security policies
- Safe workflow practices
- Dependency pinning
- Binary artifact usage

The score ranges from **0 to 10**, where 10 indicates best practices.

{% image
   source="https://datadog-docs.imgix.net/images/security/code_security/openSSF_Score_1.f1e3e4948c3d6359518fa355065cd356.png?auto=format"
   alt="OpenSSF Scorecard results for the upstream project" /%}

## Next steps{% #next-steps %}

To get started with Library Inventory:

1. Enable **Static SCA** to detect libraries in your repositories. See [static setup](https://docs.datadoghq.com/security/code_security/software_composition_analysis/setup_static/) to get started.
1. Enable **Runtime SCA** to identify libraries actually used during execution. See [runtime setup](https://docs.datadoghq.com/security/code_security/software_composition_analysis/setup_runtime/) to get started.
1. Use both views together to understand both your full dependency footprint and your real runtime exposure.
