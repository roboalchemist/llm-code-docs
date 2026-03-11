# Source: https://docs.ox.security/get-started/onboarding-to-ox/ox-connectors.md

# OX Scanners

OX-provided scanning technologies appear in the platform as OX connectors and analyze your code, containers, cloud environment, and running applications.

Each scanner activates automatically once the required connection is established. When you connect your environment, OX ingests data, runs the appropriate scans, and displays results in the Dashboard, Applications, and Active Issues pages.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-2dfa741ebc02ef5b14ac843742e41e4cf84c7b18%2Fimage%20(1)%20(1)%20(1)%20(1)%20(1).png?alt=media" alt=""><figcaption></figcaption></figure>

OX Security includes the following scanners:

* [OX CI/CD Posture](#ox-ci-cd-posture)
* [OX Cloud Context](#ox-cloud-context)
* [OX Code Security](#ox-code-security)
* [OX Container Security](#ox-container-security)
* [OX Dynamic App Security](#ox-dynamic-app-security)
* [OX Git Posture](#ox-git-posture)
* [OX IaC Scan](#ox-iac-scan)
* [OX K8s Inspector (Beta)](#ox-k8s-inspector-beta)
* [OX Open Source Security](#ox-open-source-security)
* [OX SBOM Scan](#ox-sbom-scan)
* [OX Secret / PII Scan](#ox-secret-pii-scan)

### How OX Scanners Work

Each scanner requires a specific connection or configuration step. Once connected, OX begins scanning automatically and continues scanning on a regular schedule.

| Scanner                                                                 | What You Must Connect First                  | What the Scanner Does                                                                                                  | What Happens If Not Connected                      |
| ----------------------------------------------------------------------- | -------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------- |
| **Code Security** (SAST, IaC Scan, Secrets, SBOM, Open Source Security) | Source control (required)                    | Scans code for vulnerabilities, secrets, IaC misconfigurations, license risks, dependency issues, and generates SBOMs. | No code-level visibility.                          |
| **Container Security**                                                  | Container registry                           | Scans container images stored in registries for OS/package CVEs, misconfigurations, secrets, and insecure base images. | No image scanning or container posture visibility. |
| **Cloud Context**                                                       | Cloud account (AWS, GCP, Azure)              | Scans cloud resources and configuration, detects misconfigurations, and enriches issues with cloud context.            | No cloud posture or resource-level insights.       |
| **Dynamic App Security (DAST)**                                         | Defined target (URL/endpoint)                | Performs dynamic security testing on running applications.                                                             | No runtime application testing.                    |
| **Kubernetes Inspector / Runtime Sensor** (Early Availability)          | Kubernetes cluster + deployed runtime sensor | Provides runtime visibility into container workloads, image usage, and live execution context.                         | No runtime metadata or workload-level insights.    |

## Scanner Requirements and Recommended Order

OX scanners activate automatically once the required connection is in place. The steps below describe the recommended onboarding order and explain what each connection enables.

1. **Connect your source control.**\
   This is required for OX to operate.\
   Connecting source control activates all code-level scanners, including SAST, Secrets, IaC scanning, SBOM generation, and Open Source Security.\
   Without this step, no code scanning or dependency analysis can run.

   After completing this step, your initial onboarding is essentially complete.\
   **All other steps are optional** and depend on your environment, maturity, and security goals. You can configure them later at any time.
2. **Connect container registries** (optional).\
   This enables OX to scan Docker/container images stored in registries such as Amazon ECR, Google Artifact Registry, Azure Container Registry, Docker Hub, or GitHub Container Registry.\
   Connecting a registry allows OX to automatically discover images and scan them for OS/package CVEs, misconfigurations, secrets, and insecure base images.\
   Without this connection, OX cannot analyze your built containers.
3. **Connect cloud accounts** (optional).\
   Connecting AWS, GCP, or Azure accounts enables OX to scan cloud resources and configurations, detect misconfigurations, and enrich issues with cloud context.\
   Without a cloud connection, cloud posture and cloud-resource visibility are not available.
4. **Set up DAST targets** (optional).\
   To run Dynamic Application Security Testing, you must define one or more application targets (URLs or endpoints).\
   Once targets are configured, OX performs active testing of running applications.\
   Without defined targets, DAST scans will not run.
5. **Deploy the runtime sensor** (advanced / Early Availability).\
   Deploying the runtime sensor in your Kubernetes clusters enables runtime-level insights, including workload behavior, image usage, and live execution context.\
   Without the sensor, OX cannot collect runtime metadata or correlate issues with live workloads.

## Enable a connector

Most OX connectors are enabled by default. If the connector isn’t enabled.

**To enable the connector:**

1. Go to the **Connectors** page and locate the relevant connector. Here's an example.\
   ![](https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-85c793b53f741a0ba2c3e14e418d880558ee4b8c%2FConnector%20screen.png?alt=media)
2. Click the icon to open the connection screen.
3. Click the toggle to enable the connector or follow the on-screen instructions.

## Disable a connector

You can disable a connector in the production environment, but not in the demo environment. Once disconnected, issues and related data are no longer displayed in the UI.

**To disable the connector:**

1. Go to the **Connectors** page and locate the relevant connector.
2. Click the icon to open the connection screen.
3. Click the toggle to disable the connector or click **DELETE**.

To reconnect, click the toggle or reconnect following the on-screen instructions.

## OX CI/CD Posture

The connector analyzes Git and repositories posture to ensure best practices and standards are maintained for code health and organization.

The connector is ON by default.

## OX Cloud Context

The connector scans cloud environments and configurations to identify security risks, misconfigurations, runtime vulnerabilities, and non-compliance with security best practices.

The connector is ON by default.

AWS is the cloud provider.

For more on cloud-related artifacts, see the article [Cloud BOM](https://docs.ox.security/bom/cloud-bom).

## OX Code Security

The connector scans cloud environments and configurations to identify security risks, misconfigurations, runtime vulnerabilities, and non-compliance with security best practices.

The connector is ON by default.

For supported languages and frameworks, see the [Code Security](https://docs.ox.security/supported-languages-and-frameworks) section in the article [Supported Languages and Frameworks](https://docs.ox.security/supported-languages-and-frameworks).

## OX Container Security

The connector scans container images for vulnerabilities, secrets, misconfigurations, and security best practices to ensure a secure containerized environment.

The connector is ON by default.

## OX Dynamic App Security

The connector scans real-time testing of live applications to uncover vulnerabilities in their running environments. It simulates real attack scenarios to identify what truly matters, beyond static code analysis.

The connector is ON by default.

## OX Git Posture

The connector analyzes Git and repositories posture to ensure best practices and standards are maintained for code health and organization.

The connector is ON by default.

## OX IaC Scan

The connector scans source code to detect infrastructure-as-code configurations for security best practices and potential misconfigurations that could lead to vulnerabilities.

The connector is ON by default.

For supported languages and frameworks, see the[Infrastructure as Code Support](https://app.gitbook.com/s/DoksSYnSCvYSMGAaU9SQ/supported-languages-and-frameworks) section in the article[Supported Languages and Frameworks](https://app.gitbook.com/s/DoksSYnSCvYSMGAaU9SQ/supported-languages-and-frameworks).

## OX K8s Inspector (Beta)

The connector runs in your Kubernetes cluster and collects runtime metadata and configuration details. It securely sends this data to the OX platform, providing visibility into active workloads, identifying public images in use, and enriching vulnerability context.

The connector is OFF by default. To connect, see the article [OX K8s Inspector](https://docs.ox.security/making-connections/ox-inspector).

For supported languages and frameworks, see the [Infrastructure as Code Support](https://docs.ox.security/supported-languages-and-frameworks) section in the article [Supported Languages and Frameworks](https://docs.ox.security/supported-languages-and-frameworks).

## OX Open Source Security

The connector scans source code to detect vulnerable open-source components, libraries, and Docker files that could be exposed.

The connector is ON by default.

For supported languages and frameworks, see the section ​[Open Source Security & SBOM](https://docs.ox.security/get-started/supported-languages-and-frameworks#sca-and-sbom-support) in the article [Supported Languages and Frameworks](https://docs.ox.security/get-started/supported-languages-and-frameworks).

## OX SBOM Scan

The connector scans source code and containers to generate a detailed Software Bill Of Materials with all components, libraries, and tools used in the software, along with their versions and dependencies, for transparency and compliance.

The connector is ON by default.

For supported languages and frameworks, see the section ​[Open Source Security & SBOM](https://docs.ox.security/get-started/supported-languages-and-frameworks#sca-and-sbom-support) in the article [Supported Languages and Frameworks](https://docs.ox.security/get-started/supported-languages-and-frameworks).

You might also want to check these articles: [Malicious Dependencies](https://docs.ox.security/policies/malicious-dependencies) and [SBOM](https://docs.ox.security/bom/sbom).

## OX Secret / PII Scan

The connector scans source code to detect and alert on embedded secrets, such as passwords or API keys, and personally identifiable information (PII) that could be exposed.

The connector is ON by default.
