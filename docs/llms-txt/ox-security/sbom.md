# Source: https://docs.ox.security/inventory-with-ox-bom/sbom.md

# SBOM

The Software Bill of Materials (SBOM) provides a unified inventory of open-source and third-party libraries across your applications. It helps security and engineering teams understand what dependencies are in use, where they are used, and the risk and license posture for each version.

SBOM collects data from connected sources, including source control, CI/CD pipelines, container images, and imported files. It automatically discovers packages, resolves versions, and categorizes them by application and source. This automated discovery improves visibility into supply-chain risk, as follows:

* **Dependency discovery:** SBOM identifies and catalogs libraries by ecosystem (npm, PyPI, Maven, Go, and others), version, and application.
* **Vulnerability visibility:** Shows known CVEs for each library and version so you can prioritize remediation.
* **License compliance:** Surfaces detected licenses and highlights items that may violate your organization’s policy.
* **Usage context:** Indicates whether a library is actually used in code or artifacts, helping you focus on what matters.
* **Health signals:** Provides indicators such as maintenance activity, update availability, popularity, and release dates to guide upgrade decisions.
* **Drill-down details:** For each library, SBOM displays metadata, policy results, related artifacts, and maintainers so you can assess risk and plan next steps.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-3809cb3d9fd5428a94adba09cd66d7afe6f65d8f%2FSBOM%20(2).png?alt=media" alt=""><figcaption></figcaption></figure>

## SBOM table columns

| Column                                                                                      | Explanation                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Library                                                                                     | Package name with version in the format `name@version`. Select to open the details drawer.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| License                                                                                     | Detected license for the selected version, for example Apache-2.0, MIT, BSD-3-Clause, or N/A if unknown.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| CVE                                                                                         | Vulnerability status for the selected version. A check mark means no known CVEs. A number shows the CVE count.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Benign                                                                                      | Libraries your organization flags as benign. A check mark means benign.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Used                                                                                        | Whether the library is used in code or artifacts. A check mark means OX finds usage.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Updated                                                                                     | Whether a newer version exists. A check mark means you are on the latest version.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Maintained                                                                                  | Upstream project activity signal. A check mark means the project is maintained.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Popular                                                                                     | Community popularity signal. Higher values indicate broader adoption.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [Runtime Status](https://docs.ox.security/secure-runtime/ox-runtime-sensor) (EA capability) | <p>Shows whether a third-party library is actually loaded in memory during runtime. This helps identify which dependencies are active in the running application and which ones exist in the SBOM but are not used.</p><ul><li><strong>Loaded</strong><br>The library is loaded in memory during runtime and affects the running application.</li><li><strong>Not Loaded</strong><br>The library appears in the SBOM but is not loaded in memory during runtime and may not influence application behavior.</li></ul><p>Runtime Status is an Early Access capability and is visible only when the OX Runtime Sensor is connected.</p> |
| Source                                                                                      | Where OX detected the library, for example repository or registry. Icons link to the source when available.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| App name                                                                                    | The application that includes the library. Select to open the app in OX.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |

## Library details tabs

Select a library to open the details drawer. Use the tabs to inspect specific information.

| Tab           | What you see                                                                    |
| ------------- | ------------------------------------------------------------------------------- |
| General info  | Core metadata about the selected library and where OX found it.                 |
| Policy status | Results of license, maintenance, update, malware, popularity, and usage checks. |
| Artifacts     | Images and other artifacts that include the library, with tags and registries.  |
| Maintainers   | Known maintainers for the library with activity signals when available.         |

## General info fields

| Field           | Description                                                                                                           |
| --------------- | --------------------------------------------------------------------------------------------------------------------- |
| Package name    | Canonical package identifier, for example `@apollo/protobufjs`.                                                       |
| Library version | Version detected in your environment.                                                                                 |
| Latest version  | Newest version available in the registry, if known.                                                                   |
| Application     | App where OX found the library. The link opens the app page.                                                          |
| Library name    | Name reported by the package source.                                                                                  |
| SHA             | Content hash that identifies the exact resolved build.                                                                |
| Release date    | Upstream release date of the detected version, when available.                                                        |
| Manager         | Package ecosystem, for example npm, pip, Maven, Go. The link opens the package page when available.                   |
| Stars           | Community stars for the upstream repository when available.                                                           |
| Open issues     | Count of open issues in the upstream repository when available.                                                       |
| Language        | Primary implementation language when known.                                                                           |
| Forks           | Count of repository forks when available.                                                                             |
| Source          | Where OX resolved the library, for example Registry or Repository. The link opens the source location when available. |
| Maintainers     | Number of maintainers detected for the package in the source registry.                                                |
| Copyright       | Copyright statement reported by the project.                                                                          |
| License         | License assigned to the detected version. The link opens the license reference when available.                        |

## Policy status checks

Each card shows the current evaluation for the selected library.

| Check             | Fields shown                                | What it means                                                                                   |
| ----------------- | ------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| License check     | License                                     | Whether the library’s license aligns with your organization’s policy.                           |
| Maintenance check | Maintainers, Open issues                    | Signals on upstream health. Low maintainer count or many open issues can indicate risk.         |
| Update check      | Latest version, Release date, Version I use | Whether a newer version exists and when it was released. Helps prioritize upgrades.             |
| Malware check     | Malicious type                              | Indicators of known malicious behavior. “None” means no known malicious indicators.             |
| Popularity check  | Stars, Forks                                | Community adoption signals that can guide trust and upgrade decisions.                          |
| Usage check       | Usage                                       | Whether OX detects the library in use. Used libraries require higher priority than unused ones. |

## Artifacts tab fields

| Field      | Description                                              |
| ---------- | -------------------------------------------------------- |
| Artifact   | Name of the image or artifact that contains the library. |
| Tag        | Tag of the artifact, for example `1.2.3` or `latest`.    |
| Registry   | Registry where the artifact is stored.                   |
| OS image   | Base operating system of the artifact when known.        |
| Base image | Parent image the artifact is built from.                 |
| Source     | Connector or scan source that reported the artifact.     |

## Maintainers tab fields

| Field      | Description                                                               |
| ---------- | ------------------------------------------------------------------------- |
| Maintainer | Maintainer name or handle as reported by the registry or repository.      |
| Contact    | Contact information when available, for example URL or email.             |
| Signals    | Activity indicators such as stars, forks, and open issues when available. |
