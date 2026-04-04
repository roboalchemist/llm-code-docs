# Source: https://docs.socket.dev/docs/scans.md

# Scans

## Introduction

The \*\*Scans section in Socket provides a centralized view of all scans run within your organization across GitHub, API, and CLI sources. Each scan captures the state of your repositories and surfaces alerts related to supply chain risks, vulnerabilities, license violations, and more.

***

#### 1. Accessing Scans

* Navigate to the **Scans** section from the left sidebar of the Socket dashboard.
* The main **Scans** page lists all completed scans across repositories.

<Image align="center" src="https://files.readme.io/1f2968c4827dcbf6c4f64ad43ebf866bd537f3b60188747589b9e084e3a2b28f-Screenshot_2025-07-14_at_10.09.35_PM.png" />

***

#### 2. Scan List Details

Each row in the scan list includes:

* **Ran At**: Timestamp of when the scan was performed.
* **Repository**: Repository name associated with the scan.
* **Branch**: The branch that was scanned.
* **Pull Request**: If applicable, PR identifier linked to the scan.
* **Commit**: The commit that triggered the scan.

***

#### 3. Scan Details

Clicking on a scan entry opens the detailed view. Tabs include:

* **Alerts**: Shows categorized alerts.
* **Dependencies**: Lists packages analyzed.
* **Files**: Displays scanned files and metadata.

Example:\
![](https://files.readme.io/85bc6a96cb5f87b766e3a133053894aec743dac772dce7ba20eb8d77ebee45a9-Screenshot_2025-07-14_at_10.10.08_PM.png)

***

#### 4. Understanding Alerts

* Alerts are categorized based on severity, with the following levels: Critical, High, Medium, and Low.
* Alert Priority: Socket’s internal signal about how relevant this alert is to the org (based on reachability, triage, etc).
* Alert Type: e.g. Known Malware, Critical CVE, Supply Chain Risk, etc.
* Scope: e.g. Direct vs Transitive dependency.

Example of Alerts:\
![](https://files.readme.io/ba13e5d12712d14d75753aa4d8df060bd89428a0e8b7459497c224844cdb537a-Screenshot_2025-07-15_at_2.32.12_AM.png)

<Image align="center" src="https://files.readme.io/6777f364098efed4f2bfa72fe6ebfecf2de0f1983656e00021322f9be4f82bcb-Screenshot_2025-07-15_at_2.57.17_AM.png" />

***

#### 5. Dependency Analysis

The **Dependencies** tab provides a comprehensive list of all dependencies associated with the scan, highlighting potential issues such as:

* Scope: Direct vs transitive.
* Version detected.
* Associated alert counts and types.

Example:\
![](https://files.readme.io/77795a38ad3d76e0981fc8cd8cd15b89bcb79b5f8e4afe59877838faf23343a1-Screenshot_2025-07-15_at_2.33.41_AM.png)

<Image align="center" src="https://files.readme.io/ac626fb8b65edab8b98da260a9a178d8a9b82833817d18efac514a3cf5fcb95b-Screenshot_2025-07-15_at_2.33.52_AM.png" />

***

#### 6. Files

The **Files** tab provides a list of files used within the repository. You can select individual files to view the contents.

Example:

<Image align="center" src="https://files.readme.io/ccf131ee8d5e1ffe59bbdad626d1cd5065dc64a054028dac67a4d51a206ea868-Screenshot_2025-07-15_at_2.34.55_AM.png" />

***

#### 7. Artifact Details

Each artifact in the scan is detailed with information such as:

* **Ecosystem**: The environment (e.g., npm, PyPI) the artifact belongs to.
* **Artifact Name**: The specific name and version of the artifact.
* **Category**: The type of risk associated (e.g., Supply chain risk).
* **Scores**: Various metrics such as supply chain security, quality, maintenance, vulnerabilities, and license compliance.

Example:\
![](https://files.readme.io/354d18fbe115fc3303b9fe564d65025ea284bd16aefeba6d826d201158dc61da-Screenshot_2025-07-15_at_4.11.46_AM.png)

***

By utilizing the Scans feature in Socket, you can maintain a secure and efficient development workflow, ensuring all dependencies and components are continuously monitored and evaluated for potential risks.