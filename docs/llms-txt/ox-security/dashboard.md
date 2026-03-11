# Source: https://docs.ox.security/get-started/onboarding-to-ox/review-scan-results/dashboard.md

# Dashboard

The OX dashboard provides a system-wide snapshot of your security posture. It brings together issue status, application security coverage, asset inventory, and trends in a single view so you can quickly understand what requires attention.

OX focuses on protecting what really matters by reducing noise and highlighting real risk. The dashboard helps you:

* See the full impact of an issue across tools and environments through aggregation, by grouping related findings into a single issue.
* Focus remediation efforts where they matter most through prioritization, by ranking issues based on runtime context, exposure, and business impact.
* Improve visibility across your delivery pipeline and runtime environment, by showing security coverage from source control through deployment.
* Track progress over time, by monitoring severity and status trends as issues move through remediation.

This page describes the standard dashboard that opens by default when you log in. You can later replace this view with [a custom dashboard based on a report](https://docs.ox.security/get-started/onboarding-to-ox/review-scan-results/custom-dashboard-views) that better matches your daily workflow.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-79eec3f523b58901d952a9cf71cebec1ca665701%2Fnew_dashboard.png?alt=media" alt=""><figcaption></figcaption></figure>

## Issues status and prioritization

This section summarizes open issues by severity and shows how findings move through OX processing, from raw scanner output to actionable, prioritized issues.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-5f1ca23e5afdc4d657e9f15cfe12475f15acd9d5%2FIssues%20Status%20and%20Prioritization.png?alt=media" alt="" width="563"><figcaption></figcaption></figure>

<table><thead><tr><th width="179.83343505859375">Element</th><th>Description</th></tr></thead><tbody><tr><td><strong>Severity Summary</strong></td><td>Cards that show the number of open issues for each severity level (Apocalypse, Critical, High, Medium) and the current MTTR for each level.</td></tr><tr><td><strong>Original Alerts</strong></td><td>The total number of findings as reported by connected scanners and tools, before OX applies correlation or prioritization.</td></tr><tr><td><strong>OX Aggregation</strong></td><td>A consolidated view of related findings grouped into a single issue based on shared attributes such as asset, component, vulnerability type, and location.</td></tr><tr><td><strong>OX Prioritization</strong></td><td>A ranked view of aggregated issues based on severity, runtime context, exposure, and business impact.</td></tr></tbody></table>

## AppSec Data Fabric

This section shows coverage across the main stages of your software delivery and runtime environment. Each tile represents a domain and indicates whether posture and scan data are available.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-3eaa84c9f7afac15e2af72d4300da336670777e2%2FAppSec%20Data%20Fabric.png?alt=media" alt="" width="563"><figcaption></figcaption></figure>

| Domain               | What it shows                                                                                                                         | Why it matters                                                         |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| **Source Control**   | Posture and scan coverage for connected repositories, including code, secrets and PII, open source, SBOM, and Infrastructure as Code. | Confirms that development assets and dependencies are being monitored. |
| **CI/CD**            | Pipeline posture and scan status for connected CI/CD systems.                                                                         | Confirms that security checks run during build and deployment.         |
| **Registry**         | Container and artifact security coverage for connected registries.                                                                    | Confirms that images and artifacts are scanned before deployment.      |
| **Cloud Deployment** | Runtime and cloud context, including API security, artifact integrity, and cloud exposure.                                            | Shows risk in deployed and running workloads.                          |

## Assets

This section provides a count of key asset types managed by OX.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-e6e41caa5fb589ae2dee8168516111c66edaef60%2FAssets.png?alt=media" alt="" width="563"><figcaption></figcaption></figure>

| Asset type                          | Description                                                                          |
| ----------------------------------- | ------------------------------------------------------------------------------------ |
| **Applications**                    | Logical groupings of repositories, services, and workloads managed as a single unit. |
| **Pipeline protected repositories** | Repositories with CI/CD protection and scan enforcement enabled.                     |
| **Libraries**                       | Open source and third-party dependencies identified across repositories and images.  |
| **APIs**                            | Discovered or defined application programming interfaces.                            |
| **Artifacts**                       | Build outputs such as packages and images stored in registries.                      |
| **Cloud assets**                    | Cloud resources discovered across connected accounts.                                |
| **SaaS**                            | Connected software-as-a-service applications.                                        |

## Issue severity trend over time

This chart shows how the number of issues changes over time by severity.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-af17f423bc588e4ce32fa71e3bcf0eaca251ef19%2FIssue%20Severity%20Trend%20Over%20Time.png?alt=media" alt="" width="563"><figcaption></figcaption></figure>

| Aspect             | Description                                                       |
| ------------------ | ----------------------------------------------------------------- |
| **Time range**     | The period displayed on the horizontal axis.                      |
| **Severity bands** | Color-coded areas that represent issue counts per severity level. |
| **Data points**    | Snapshots of issue counts at each point in time.                  |

## Issue status trend over time

This chart shows how issue states change over time, such as open, resolved, or suppressed.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-5eaf18d3997c98745231fc315d3bdf807ae942d1%2FIssue%20Status%20Trend%20Over%20Time.png?alt=media" alt="" width="563"><figcaption></figcaption></figure>

| Aspect                | Description                                                      |
| --------------------- | ---------------------------------------------------------------- |
| **Time range**        | The period displayed on the horizontal axis.                     |
| **Status categories** | Issue states tracked over time.                                  |
| **Data points**       | Snapshots of issue counts for each status at each point in time. |

## Last scan indicator

The upper-right corner of the dashboard shows the time of the most recent scan.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-f122b33b88ea83cfb72b5048c0fec86656ac1f12%2FLast%20Scan%20Indicator.png?alt=media" alt="" width="318"><figcaption></figcaption></figure>

| Field         | Description                                                               |
| ------------- | ------------------------------------------------------------------------- |
| **Last scan** | The timestamp of the most recent completed scan across connected sources. |
