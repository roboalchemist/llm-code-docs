# Source: https://docs.ox.security/scan-and-analyze-with-ox/scanning.md

# Scanning Methods

OX Security continuously monitors your development and runtime environments to identify and prioritize security issues across the software supply chain.

OX connects to your source control, CI/CD, artifact registries, cloud environments, and external testing tools to collect findings and context. Each scan enriches OX’s unified graph, so you see one consistent view of issues, owners, impact, and required actions.

OX supports multiple scan entry points. Repository and registry connectors keep your data in sync so new commits, pull requests, images, and packages are analyzed without manual effort. Pipeline jobs validate builds before they ship and can block based on your policy. The IDE extension analyzes local changes to help you fix issues before they reach the repo. You can also import results and SBOMs from third-party scanners, or trigger on-demand scans by API when you need a targeted check.

The OX scanning engine supports multiple scanning modes, enabling flexible and comprehensive coverage tailored to your workflow and infrastructure.

This section covers the available scanning methods in OX:

* [**Regular Scans**:](https://docs.ox.security/get-started/onboarding-to-ox/ox-connectors) Automatically triggered by default across all connected assets, these scans ensure ongoing security visibility.
* [**Selected Repositories Scans**:](https://docs.ox.security/scan-and-analyze-with-ox/scanning/scanning-selected-repositories) Target specific repositories to reduce scan scope and optimize performance when full coverage is not needed.
* [**Pipeline Scans**:](https://docs.ox.security/scan-and-analyze-with-ox/scanning/scanning-ci-cd-pipelines) Integrated directly into your CI/CD pipelines to detect vulnerabilities immediately after build, before images are deployed or pushed to registries.
* [**IDE Scans:**](https://docs.ox.security/scan-and-analyze-with-ox/scanning/ox-ide-extension) Run in your IDE with the OX IDE extension to analyze modified files as you code, flag issues inline, and suggest fixes including AI-based remediation for supported languages, preventing new issues before commit.
* [**Multi-branch Scans:**](https://docs.ox.security/scan-and-analyze-with-ox/scanning/multi-branch-support) Extend coverage beyond the default branch to scan multiple branches in parallel (for example, development, staging, production) and maintain visibility across release lines.
