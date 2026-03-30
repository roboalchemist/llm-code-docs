# Source: https://help.sonatype.com/en/sonatype-nexus-repository-3-87-0-release-notes.html

Title: Sonatype Nexus Repository 3.87.0 - 3.87.2 Release Notes

URL Source: https://help.sonatype.com/en/sonatype-nexus-repository-3-87-0-release-notes.html

Published Time: Wed, 11 Mar 2026 18:15:21 GMT

Markdown Content:
Sonatype Nexus Repository 3.87.0 - 3.87.2 Release Notes
===============

[Skip to main content](https://help.sonatype.com/en/sonatype-nexus-repository-3-87-0-release-notes.html#content-wrapper)

Toggle navigation

[![Image 1: Corporate logotype](https://help.sonatype.com/css/image/corporate-logo.png)](https://help.sonatype.com/index.html?lang=en)

[![Image 2: My Sonatype Platform Portal Link](https://help.sonatype.com/en/image/uuid-fa27c254-fe39-b491-1a9b-92871041e611.svg)](https://my.sonatype.com/)

Toggle navigation[![Image 3: Corporate logotype](https://help.sonatype.com/css/image/corporate-logo.png)](https://help.sonatype.com/index.html?lang=en)

* [Sonatype Platform Overview](https://help.sonatype.com/en/sonatype-product-overview.html)
  * [my.sonatype.com](https://help.sonatype.com/en/my-sonatype-com.html)
    * [Setting Up Organizations on my.sonatype.com](https://help.sonatype.com/en/using-my-sonatype-com.html)
    * [Configure Identity Provider (IdP)](https://help.sonatype.com/en/configure-identity-provider.html)

  * [Important Announcements](https://help.sonatype.com/en/important-announcements.html)
    * [Find and Fix React2Shell](https://help.sonatype.com/en/find-and-fix-react2shell.html)
      * [React2Shell Impact Report](https://help.sonatype.com/en/react2shell-impact-report.html)
      * [React2Shell Impact Filter in the Security Risk Breakdown Dashboard](https://help.sonatype.com/en/react2shell-impact-filter.html)

    * [Understanding the recent npm malware attacks](https://help.sonatype.com/en/understanding-the-phantomraven-malware-campaign.html)
    * [Understanding the Shai-Hulud npm Worm Attack](https://help.sonatype.com/en/understanding-the-shai-hulud-npm-worm-attack.html)
    * [Critical Cleanup Policy Bug Advisory](https://help.sonatype.com/en/critical-cleanup-policy-bug-advisory.html)
    * [Find and Fix Springshell](https://help.sonatype.com/en/find-and-fix-springshell.html)
    * [Find and Fix Log4j](https://help.sonatype.com/en/find-and-fix-log4j.html)
    * [Struts2 Frequently Asked Questions](https://help.sonatype.com/en/struts2-frequently-asked-questions.html)

  * [Sonatype Sunsetting Information](https://help.sonatype.com/en/sonatype-sunsetting-information.html)
    * [Sonatype Nexus Repository 3 Versions Status](https://help.sonatype.com/en/sonatype-nexus-repository-3-versions-status.html)
    * [Nexus Repository 3 Feature Status](https://help.sonatype.com/en/sonatype-nexus-repository-3-feature-status.html)
    * [Sonatype Nexus Repository 2 Sunsetting Information](https://help.sonatype.com/en/sonatype-nexus-repository-2-sunsetting-information.html)
    * [Sonatype Nexus Repository 2 Version Status](https://help.sonatype.com/en/sonatype-nexus-repository-2-version-status.html)
    * [Sonatype Auditor Sunsetting](https://help.sonatype.com/en/sonatype-auditor-sunsetting.html)
    * [Sonatype Repository Firewall Classic Sunsetting](https://help.sonatype.com/en/sonatype-repository-firewall-classic-sunsetting.html)
    * [Sonatype IQ Server Versions Status](https://help.sonatype.com/en/sonatype-iq-server-versions-status.html)
    * [Sonatype IQ Server Feature Status](https://help.sonatype.com/en/sonatype-iq-server-feature-status.html)
    * [Sonatype Integrations Version Status](https://help.sonatype.com/en/sonatype-integration-versions-status.html)

  * [Sonatype Platform Cloud-Native Reference Architectures](https://help.sonatype.com/en/sonatype-platform-reference-architectures.html)
    * [Sonatype Platform AWS Reference Architectures](https://help.sonatype.com/en/aws-reference-architectures.html)
      * [AWS Cloud-Native Single Instance IQ Reference Architecture](https://help.sonatype.com/en/sonatype-iq-reference-architecture-aws-cloud-native-single-instance.html)
      * [AWS Cloud-Native High Availability IQ Reference Architecture](https://help.sonatype.com/en/sonatype-iq-reference-architecture-aws-cloud-native-high-availability.html)
      * [AWS EKS Kubernetes High Availability IQ Reference Architecture](https://help.sonatype.com/en/sonatype-iq-reference-architecture-aws-eks-kubernetes-high-availability.html)

    * [Sonatype Platform Azure Reference Architectures](https://help.sonatype.com/en/azure-reference-architectures.html)
      * [Azure Cloud-Native Single Instance IQ Reference Architecture](https://help.sonatype.com/en/sonatype-iq-reference-architecture-azure-cloud-native-single-instance.html)
      * [Azure Cloud-Native High Availability IQ Reference Architecture](https://help.sonatype.com/en/sonatype-iq-reference-architecture-azure-cloud-native-high-availability.html)
      * [Azure Kubernetes Service High Availability IQ Reference Architecture](https://help.sonatype.com/en/sonatype-iq-reference-architecture-azure-kubernetes-service-high-availability.html)

    * [Sonatype Platform GCP Reference Architectures](https://help.sonatype.com/en/gcp-reference-architectures.html)
      * [GCP Cloud-Native Single Instance IQ Reference Architecture](https://help.sonatype.com/en/sonatype-iq-reference-architecture-gcp-cloud-native-single-instance.html)
      * [GCP Cloud-Native High Availability IQ Reference Architecture](https://help.sonatype.com/en/sonatype-iq-reference-architecture-gcp-cloud-native-high-availability.html)
      * [GCP GKE Kubernetes High Availability IQ Reference Architecture](https://help.sonatype.com/en/sonatype-iq-reference-architecture-gcp-gke-kubernetes-high-availability.html)

  * [Feature Parity with Sonatype Cloud](https://help.sonatype.com/en/feature-parity-with-sonatype-cloud.html)
  * [Java Runtime Compatibility Matrix](https://help.sonatype.com/en/java-compatibility-matrix.html)
  * [Sonatype on Responsible Disclosure](https://help.sonatype.com/en/responsible-disclosure.html)
  * [Sonatype Security Vulnerabilities](https://help.sonatype.com/en/sonatype-security-vulnerabilities.html)
  * [Product Preview Program](https://help.sonatype.com/en/product-preview-program.html)
  * [IPv6 Readiness Check](https://help.sonatype.com/en/ipv6-readiness-check.html)
  * [Reference: Glossary](https://help.sonatype.com/en/reference--glossary.html)

* [Sonatype Guide](https://help.sonatype.com/en/sonatype-guide.html)
  * [Getting Started with Sonatype Guide](https://help.sonatype.com/en/getting-started-with-sonatype-guide.html)
    * [Manage Guide User Tokens](https://help.sonatype.com/en/manage-guide-user-tokens.html)
    * [Accessing GUIDE-Sonatype Support](https://help.sonatype.com/en/sonatype-guide-support.html)

  * [Anonymous Access to Sonatype Guide](https://help.sonatype.com/en/anonymous-access-to-sonatype-guide.html)
  * [Research with Sonatype Guideinc](https://help.sonatype.com/en/research-with-sonatype-guide.html)
  * [Automate with Sonatype Guide](https://help.sonatype.com/en/automate-with-sonatype-guide.html)
  * [Integrate with Sonatype Guide](https://help.sonatype.com/en/integrate-with-sonatype-guide.html)
  * [OSS Index Migration to Sonatype Guide](https://help.sonatype.com/en/oss-index-migration-to-sonatype-guide.html)

* [Sonatype Nexus Repository](https://help.sonatype.com/en/sonatype-nexus-repository.html)
  * [Product Information](https://help.sonatype.com/en/product-information.html)
    * [Download](https://help.sonatype.com/en/download.html)
      * [Nexus Repository 3.70.x Downloads with OrientDB](https://help.sonatype.com/en/orientdb-downloads.html)
      * [Download Archives - Sonatype Nexus Repository 3](https://help.sonatype.com/en/download-archives---repository-manager-3.html)

    * [Release Notes](https://help.sonatype.com/en/release-notes.html)
      * [2026 Release Notes](https://help.sonatype.com/en/nexus-repository-2026-release-notes.html)
        * [Sonatype Nexus Repository 3.90.0 - 3.90.1 Release Notes](https://help.sonatype.com/en/sonatype-nexus-repository-3-90-0-release-notes.html)
        * [Sonatype Nexus Repository 3.89.0 Release Notes](https://help.sonatype.com/en/sonatype-nexus-repository-3-89-0-release-notes.html)
        * [Sonatype Nexus Repository 3.88.0 Release Notes](https://help.sonatype.com/en/sonatype-nexus-repository-3-88-0-release-notes.html)

      * [2025 Release Notes](https://help.sonatype.com/en/nexus-repository-2025-release-notes.html)
        * [Sonatype Nexus Repository 3.87.0 - 3.87.2 Release Notes](https://help.sonatype.com/en/sonatype-nexus-repository-3-87-0-release-notes.html)
        * [Sonatype Nexus Repository 3.86.0 - 3.86.2 Release Notes](https://help.sonatype.com/en/sonatype-nexus-repository-3-86-0-release-notes.html)
        * [Sonatype Nexus Repository 3.85.0 - 3.85.1 Release Notes](https://help.sonatype.com/en/sonatype-nexus-repository-3-85-0-release-notes.html)
        * [Sonatype Nexus Repository 3.84.0 - 3.84.2 Release Notes](https://help.sonatype.com/en/sonatype-nexus-repository-3-84-0-release-notes.html)
        * [Sonatype Nexus Repository 3.83.0 - 3.83.2 Release Notes](https://help.sonatype.com/en/sonatype-nexus-repository-3-83-0-release-notes.html)
        * [Sonatype Nexus Repository 3.82.0 - 3.82.1 Release Notes](https://help.sonatype.com/en/sonatype-nexus-repository-3-82-0-release-notes.html)
        * [Sonatype Nexus Repository 3.81.0 - 3.81.1 Release Notes](https://help.sonatype.com/en/sonatype-nexus-repository-3-81-0-release-notes.html)
        * [Sonatype Nexus Repository 3.80.0 Release Notes](https://help.sonatype.com/en/sonatype-nexus-repository-3-80-0-release-notes.html)
        * [Sonatype Nexus Repository 3.79.0 - 3.79.1 Release Notes](https://help.sonatype.com/en/sonatype-nexus-repository-3-79-0-release-notes.html)
        * [Sonatype Nexus Repository 3.78.0 - 3.78.3 Release Notes](https://help.sonatype.com/en/sonatype-nexus-repository-3-78-0-release-notes.html)
        * [Sonatype Nexus Repository 3.77.0 - 3.77.2 Release Notes](https://help.sonatype.com/en/sonatype-nexus-repository-3-77-0-release-notes.html)
        * [Sonatype Nexus Repository 3.76.0 - 3.76.1 Release Notes](https://help.sonatype.com/en/sonatype-nexus-repository-3-76-0-release-notes.html)

      * [2024 Release Notes](https://help.sonatype.com/en/2024-release-notes.html)
        * [Sonatype Nexus Repository 3.75.0 - 3.75.1 Release Notes](https://help.sonatype.com/en/sonatype-nexus-repository-3-75-0-release-notes.html)
        * [Sonatype Nexus Repository 3.74.0 Release Notes](https://help.sonatype.com/en/sonatype-nexus-repository-3-74-0-release-notes.html)
        * [Sonatype Nexus Repository 3.73.0 Release Notes](https://help.sonatype.com/en/sonatype-nexus-repository-3-73-0-release-notes.html)
        * [Sonatype Nexus Repository 3.72.0 Release Notes](https://help.sonatype.com/en/sonatype-nexus-repository-3-72-0-release-notes.html)
        * [Sonatype Nexus Repository 3.71.0 Release Notes](https://help.sonatype.com/en/sonatype-nexus-repository-3-71-0-release-notes.html)
        * [Sonatype Nexus Repository 3.70.0 - 3.70.4 Release Notes](https://help.sonatype.com/en/sonatype-nexus-repository-3-70-0-release-notes.html)
        * [Sonatype Nexus Repository 3.69.0 Release Notes](https://help.sonatype.com/en/sonatype-nexus-repository-3-69-0-release-notes.html)
        * [Sonatype Nexus Repository 3.68.0 - 3.68.1 Release Notes](https://help.sonatype.com/en/sonatype-nexus-repository-3-68-0-release-notes.html)
        * [Sonatype Nexus Repository 3.67.0 - 3.67.1 Release Notes](https://help.sonatype.com/en/sonatype-nexus-repository-3-67-0-release-notes.html)
        * [Sonatype Nexus Repository 3.66.0 Release Notes](https://help.sonatype.com/en/sonatype-nexus-repository-3-66-0-release-notes.html)
        * [Sonatype Nexus Repository 3.65.0 Release Notes](https://help.sonatype.com/en/sonatype-nexus-repository-3-65-0-release-notes.html)
        * [Sonatype Nexus Repository 3.64.0 Release Notes](https://help.sonatype.com/en/sonatype-nexus-repository-3-64-0-release-notes.html)

      * [2023 Release Notes](https://help.sonatype.com/en/2023-release-notes.html)
        * [Sonatype Nexus Repository 3.63.0 Release Notes](https://help.sonatype.com/en/sonatype-nexus-repository-3-63-0-release-notes.html)
        * [Sonatype Nexus Repository 3.62.0 Release Notes](https://help.sonatype.com/en/sonatype-nexus-repository-3-62-0-release-notes.html)
        * [Sonatype Nexus Repository 3.61.0 Release Notes](https://help.sonatype.com/en/sonatype-nexus-repository-3-61-0-release-notes.html)
        * [Sonatype Nexus Repository 3.60.0 Release Notes](https://help.sonatype.com/en/sonatype-nexus-repository-3-60-0-release-notes.html)
        * [Sonatype Nexus Repository 3.59.0 Release Notes](https://help.sonatype.com/en/sonatype-nexus-repository-3-59-0-release-notes.html)
        * [Sonatype Nexus Repository 3.58.0 - 3.58.1 Release Notes](https://help.sonatype.com/en/sonatype-nexus-repository-3-58-0---3-58-1-release-notes.html)
        * [Sonatype Nexus Repository 3.57.0 - 3.57.1 Release Notes](https://help.sonatype.com/en/sonatype-nexus-repository-3-57-0---3-57-1-release-notes.html)
        * [Sonatype Nexus Repository 3.56.0 Release Notes](https://help.sonatype.com/en/sonatype-nexus-repository-3-56-0-release-notes.html)
        * [Sonatype Nexus Repository 3.55.0 Release Notes](https://help.sonatype.com/en/sonatype-nexus-repository-3-55-0-release-notes.html)
        * [Sonatype Nexus Repository 3.54.0 - 3.54.1 Release Notes](https://help.sonatype.com/en/sonatype-nexus-repository-3-54-0---3-54-1-release-notes.html)
        * [Sonatype Nexus Repository 3.53.0 - 3.53.1 Release Notes](https://help.sonatype.com/en/sonatype-nexus-repository-3-53-0---3-53-1-release-notes.html)
        * [Sonatype Nexus Repository 3.52.0 Release Notes](https://help.sonatype.com/en/sonatype-nexus-repository-3-52-0-release-notes.html)
        * [Sonatype Nexus Repository 3.51.0 Release Notes](https://help.sonatype.com/en/sonatype-nexus-repository-3-51-0-release-notes.html)
        * [Sonatype Nexus Repository 3.50.0 Release Notes](https://help.sonatype.com/en/sonatype-nexus-repository-3-50-0-release-notes.html)
        * [Sonatype Nexus Repository 3.49.0 Release Notes](https://help.sonatype.com/en/sonatype-nexus-repository-3-49-0-release-notes.html)
        * [Sonatype Nexus Repository 3.48.0 Release Notes](https://help.sonatype.com/en/sonatype-nexus-repository-3-48-0-release-notes.html)
        * [Nexus Repository 3.47.0 - 3.47.1 Release Notes](https://help.sonatype.com/en/nexus-repository-3-47-0---3-47-1-release-notes.html)
        * [Nexus Repository 3.46.0 Release Notes](https://help.sonatype.com/en/nexus-repository-3-46-0-release-notes.html)

      * [2022 Release Notes](https://help.sonatype.com/en/2022-release-notes.html)
        * [Nexus Repository 3.45.0 - 3.45.1 Release Notes](https://help.sonatype.com/en/nexus-repository-3-45-0---3-45-1-release-notes.html)
        * [Nexus Repository 3.44.0 Release Notes](https://help.sonatype.com/en/nexus-repository-3-44-0-release-notes.html)
        * [Nexus Repository 3.43.0 Release Notes](https://help.sonatype.com/en/nexus-repository-3-43-0-release-notes.html)
        * [Nexus Repository 3.42.0 Release Notes](https://help.sonatype.com/en/nexus-repository-3-42-0-release-notes.html)
        * [Nexus Repository 3.41.0 - 3.41.1 Release Notes](https://help.sonatype.com/en/nexus-repository-3-41-0---3-41-1-release-notes.html)
        * [Nexus Repository 3.40.0 - 3.40.1 Release Notes](https://help.sonatype.com/en/nexus-repository-3-40-0---3-40-1-release-notes.html)
        * [Nexus Repository 3.39.0 Release Notes](https://help.sonatype.com/en/nexus-repository-3-39-0-release-notes.html)
        * [Nexus Repository 3.38.0 - 3.38.1 Release Notes](https://help.sonatype.com/en/nexus-repository-3-38-0---3-38-1-release-notes.html)

      * [2021 Release Notes](https://help.sonatype.com/en/2021-release-notes.html)
        * [Nexus Repository 3.37.0 - 3.37.3 Release Notes](https://help.sonatype.com/en/nexus-repository-3-37-0---3-37-3-release-notes.html)
        * [Nexus Repository 3.36.0 Release Notes](https://help.sonatype.com/en/nexus-repository-3-36-0-release-notes.html)
        * [Nexus Repository 3.35.0 Release Notes](https://help.sonatype.com/en/nexus-repository-3-35-0-release-notes.html)
        * [Nexus Repository 3.34.0 - 3.34.1 Release Notes](https://help.sonatype.com/en/nexus-repository-3-34-0---3-34-1-release-notes.html)
        * [Nexus Repository 3.33.0 - 3.33.1 Release Notes](https://help.sonatype.com/en/nexus-repository-3-33-0---3-33-1-release-notes.html)
        * [Nexus Repository 3.32.0 - 3.32.1 Release Notes](https://help.sonatype.com/en/nexus-repository-3-32-0---3-32-1-release-notes.html)
        * [Nexus Repository 3.31.0 - 3.31.1 Release Notes](https://help.sonatype.com/en/nexus-repository-3-31-0---3-31-1-release-notes.html)
        * [Nexus Repository 3.30.0 - 3.30.1 Release Notes](https://help.sonatype.com/en/nexus-repository-3-30-0---3-30-1-release-notes.html)
        * [Nexus Repository 3.29.0 - 3.29.2 Release Notes](https://help.sonatype.com/en/nexus-repository-3-29-0---3-29-2-release-notes.html)

    * [Sonatype Nexus Repository System Requirements](https://help.sonatype.com/en/sonatype-nexus-repository-system-requirements.html)
      * [Requirements for High Availability](https://help.sonatype.com/en/system-requirements-for-high-availability-deployments.html)
      * [Adjusting the File Handle Limits](https://help.sonatype.com/en/adjusting-file-handle-limits.html)
      * [Adjust the PostgreSQL Max Connections](https://help.sonatype.com/en/postgresql-max-connections.html)
      * [Nexus Repository Memory Overview](https://help.sonatype.com/en/nexus-repository-memory-overview.html)
      * [Installing the Trigram Module](https://help.sonatype.com/en/installing-the-trigram-module.html)
      * [Advanced Database Memory Tuning](https://help.sonatype.com/en/advanced-database-memory-tuning.html)

    * [Performance Data](https://help.sonatype.com/en/nexus-repository-performance-data.html)
      * [Nexus Repository Architecture Reference Spring Revalidation](https://help.sonatype.com/en/architecture-reference-spring-re-validation.html)
      * [Cleanup Performance Data](https://help.sonatype.com/en/cleanup-performance-data.html)
      * [Repository Size Calculation Performance Data](https://help.sonatype.com/en/repository-size-calculation-performance-data.html)
      * [Change Repository Blob Store Task Performance Testing](https://help.sonatype.com/en/change-repository-blob-store-task-performance-testing.html)
      * [Recalculate Blob Store Storage Task Performance Testing](https://help.sonatype.com/en/recalculate-blob-store-storage-performance-testing.html)

    * [Nexus Repository Professional Features](https://help.sonatype.com/en/nexus-repository-pro-features.html)
    * [Nexus Repository Feature Matrix](https://help.sonatype.com/en/nexus-repository-feature-matrix.html)
    * [Nexus Repository Telemetry](https://help.sonatype.com/en/nexus-repository-telemetry.html)

  * [Getting Started with Nexus Repository Cloud](https://help.sonatype.com/en/nexus-repository-cloud.html)
    * [Predictable S3 Bucket URLs for Nexus Repository Cloud](https://help.sonatype.com/en/predictable-s3-bucket-urls.html)

  * [Planning Your Implementation](https://help.sonatype.com/en/planning-your-implementation.html)
    * [Nexus Repository Reference Architectures](https://help.sonatype.com/en/sonatype-nexus-repository-reference-architectures.html)
      * [Nexus Repository Reference Architecture 1](https://help.sonatype.com/en/nexus-repository-reference-architecture-1.html)
      * [Nexus Repository Reference Architecture 2](https://help.sonatype.com/en/nexus-repository-reference-architecture-2.html)
      * [Nexus Repository Reference Architecture 3](https://help.sonatype.com/en/nexus-repository-reference-architecture-3.html)
      * [Nexus Repository Reference Architecture 4](https://help.sonatype.com/en/nexus-repository-reference-architecture-4.html)

    * [Deployment Pattern Library](https://help.sonatype.com/en/deployment-pattern-library.html)
      * [Backup/Same-Site Restore](https://help.sonatype.com/en/backup-same-site-restore.html)
      * [Disaster Recovery Site](https://help.sonatype.com/en/disaster-recovery-site.html)
      * [On-Prem Active/Passive Resiliency](https://help.sonatype.com/en/on-prem-active-passive-resiliency.html)
      * [Cloud Active/Passive Resiliency](https://help.sonatype.com/en/cloud-active-passive-resiliency.html)
      * [On-Prem Active/Active High Availability](https://help.sonatype.com/en/on-prem-active-active-high-availability.html)
      * [Cloud High Availability](https://help.sonatype.com/en/cloud-active-active-high-availability.html)
      * [Star Pattern](https://help.sonatype.com/en/star-pattern.html)
      * [Federated Repositories](https://help.sonatype.com/en/federated-repositories.html)
      * [Scaling with Proxies](https://help.sonatype.com/en/scaling-with-proxies.html)
      * [Scaling with Proxy Nodes](https://help.sonatype.com/en/scaling-with-proxy-nodes.html)
      * [Bi-Directional Proxying](https://help.sonatype.com/en/bi-directional-proxying.html)
      * [Cross-Region Disaster Recovery](https://help.sonatype.com/en/cross-region-disaster-recovery.html)
      * [Nexus Repository FIPS 140-3 Compliance](https://help.sonatype.com/en/nexus-repository-fips-140-3-compliance.html)
      * [Content Replication Pattern](https://help.sonatype.com/en/content-replication-pattern.html)
      * [Combination Active/Active High Availability + Disaster Recovery Site](https://help.sonatype.com/en/combination-active-active-high-availability---disaster-recovery-site.html)
      * [Combination Active/Active High Availability + Disaster Recovery Site + Federated Repositories](https://help.sonatype.com/en/combination-active-active-high-availability---disaster-recovery-site---federated-repositories.html)

    * [Resiliency](https://help.sonatype.com/en/resiliency-and-high-availability.html)
      * [Single-Node Cloud Resilient Deployment Using AWS](https://help.sonatype.com/en/single-node-cloud-resilient-deployment-example-using-aws.html)
      * [Single-Node Cloud Resilient Deployment Using Azure](https://help.sonatype.com/en/single-node-cloud-resilient-deployment-example-using-azure.html)
      * [Single-Node Cloud Resilient Deployment Example Using Google Cloud](https://help.sonatype.com/en/resilient-nexus-repository-deployment-to-google-cloud.html)
      * [Single Data Center On-Premises Resilient Deployment Example Using Kubernetes](https://help.sonatype.com/en/single-data-center-on-premises-deployment-example-using-kubernetes.html)

    * [High Availability Deployment](https://help.sonatype.com/en/high-availability-deployment.html)
      * [Nexus Repository vs. IQ Server High Availability](https://help.sonatype.com/en/sonatype-nexus-repository-high-availability-vs--sonatype-iq-server-high-availability.html)
      * [Manual High Availability Deployment](https://help.sonatype.com/en/option-1---manual-high-availability-deployment.html)
      * [On-Premises High Availability Using Kubernetes](https://help.sonatype.com/en/option-2---on-premises-high-availability-deployment-using-kubernetes.html)
      * [High Availability in Amazon Web Services](https://help.sonatype.com/en/option-3---high-availability-deployment-in-amazon-web-services--aws-.html)
      * [High Availability Deployment in Azure](https://help.sonatype.com/en/option-4---high-availability-deployment-in-azure.html)
      * [Deployment in Google Cloud](https://help.sonatype.com/en/deploy-nexus-repository-to-google-cloud.html)
      * [Post-Deployment Steps for HA](https://help.sonatype.com/en/post-deployment-steps-for-ha.html)
      * [Validating Your HA Deployment](https://help.sonatype.com/en/validating-your-ha-deployment.html)
      * [Migrate Nexus Repository Clustered Deployments to Use External Secrets Operator](https://help.sonatype.com/en/migrate-to-use-external-secrets-operator.html)

    * [Nexus Repository Database](https://help.sonatype.com/en/database-options.html)
    * [Storage Guide](https://help.sonatype.com/en/storage-guide.html)
      * [Storage Planning](https://help.sonatype.com/en/storage-planning.html)
      * [Using Replicated Blob Stores](https://help.sonatype.com/en/using-replicated-blob-stores.html)

    * [Run Behind a Reverse Proxy](https://help.sonatype.com/en/run-behind-a-reverse-proxy.html)
    * [Securing Nexus Repository](https://help.sonatype.com/en/securing-nexus-repository-manager.html)
    * [Keeping Disk Usage Low](https://help.sonatype.com/en/keeping-disk-usage-low.html)
    * [Backup and Restore](https://help.sonatype.com/en/backup-and-restore.html)
      * [Configure the Backup Task](https://help.sonatype.com/en/configure-and-run-the-backup-task.html)
      * [Prepare a Backup](https://help.sonatype.com/en/prepare-a-backup.html)
      * [Restore an H2 Database](https://help.sonatype.com/en/restore-an-h2-database.html)
      * [Backup and Restore in Amazon Web Services](https://help.sonatype.com/en/backup-and-restore-in-amazon-web-services.html)

    * [Usage-Based Consumption Guide for Self-Hosted Nexus Repository Deployments](https://help.sonatype.com/en/usage-based-consumption-guide-for-self-hosted.html)

  * [Install Self-Hosted Nexus Repository](https://help.sonatype.com/en/install-nexus-repository.html)
    * [Community Edition Onboarding](https://help.sonatype.com/en/ce-onboarding.html)
    * [Install Nexus Repository with a PostgreSQL Database](https://help.sonatype.com/en/install-nexus-repository-with-a-postgresql-database.html)
    * [Install Nexus Repository on OpenShift](https://help.sonatype.com/en/install-nexus-repository-on-openshift.html)
    * [Run as a Service](https://help.sonatype.com/en/run-as-a-service.html)
    * [Configuring SSL](https://help.sonatype.com/en/configuring-ssl.html)
    * [Configuring the Runtime Environment](https://help.sonatype.com/en/configuring-the-runtime-environment.html)
    * [Retry Limit Configuration](https://help.sonatype.com/en/retry-limit-configuration.html)
    * [Email Server Configuration](https://help.sonatype.com/en/email-server-configuration.html)
    * [Directories](https://help.sonatype.com/en/directories.html)

  * [Upgrade Nexus Repository](https://help.sonatype.com/en/upgrade-nexus-repository.html)
    * [Nexus Repository Upgrade Paths](https://help.sonatype.com/en/nexus-repository-upgrade-paths.html)
    * [Upgrading to Nexus Repository 3.71.0 and Beyond](https://help.sonatype.com/en/upgrading-to-nexus-repository-3-71-0-and-beyond.html)
    * [Upgrade from Nexus Repository 2](https://help.sonatype.com/en/upgrade-from-nexus-repository-2.html)
      * [Upgrade Wizard](https://help.sonatype.com/en/nexus-repository-3-upgrade-wizard.html)
      * [Changes during the Upgrade Process](https://help.sonatype.com/en/changes-during-the-upgrade-process.html)
      * [Upgrade Wizard Instructions](https://help.sonatype.com/en/upgrade-wizard-instructions.html)
      * [Upgrading Staging](https://help.sonatype.com/en/upgrading-staging.html)
      * [Feature Equivalency Matrix](https://help.sonatype.com/en/feature-equivalency-matrix.html)

    * [Migrating to a New Database](https://help.sonatype.com/en/migrating-to-a-new-database.html)
      * [Determining Current Database](https://help.sonatype.com/en/determining-current-database.html)
      * [Controlling Database Migrator Logging](https://help.sonatype.com/en/controlling-database-migrator-logging.html)
      * [Restoring a Database Backup After Migration](https://help.sonatype.com/en/restoring-a-backup.html)
      * [Reverting Back to OrientDB](https://help.sonatype.com/en/reverting-back-to-orientdb.html)

    * [Rolling Upgrades in High Availability](https://help.sonatype.com/en/nexus-repository-zero-downtime-upgrades.html)
    * [Upgrade Nexus Repository Java Version](https://help.sonatype.com/en/upgrade-nexus-repository-java-version.html)
    * [Upgrading Nexus Repository in a Kubernetes Environment](https://help.sonatype.com/en/upgrading-nexus-repository-in-an-ha-environment.html)
    * [Upgrading an H2 Database from 1.x to 2.x](https://help.sonatype.com/en/upgrade-h2.html)
    * [Migrating to a Resilient Deployment](https://help.sonatype.com/en/migrating-to-a-resilient-deployment.html)
    * [Migrating to an HA Deployment from a Legacy HA-C or a Resilient Deployment](https://help.sonatype.com/en/migrating-to-an-ha-deployment-from-a-legacy-ha-c-or-resilient-deployment.html)
    * [Moving from a High Availability Deployment to a Single Instance](https://help.sonatype.com/en/moving-from-a-high-availability-deployment-to-a-single-instance.html)
    * [Migrate to Nexus Repository from Artifactory](https://help.sonatype.com/en/migrating-to-nexus-repository-from-artifactory.html)
    * [Migrating to Shared Blob Storage](https://help.sonatype.com/en/migrating-to-shared-blob-storage.html)
    * [Instance Migrator](https://help.sonatype.com/en/instance-migrator.html)

  * [Nexus Repository Administration](https://help.sonatype.com/en/nexus-repository-administration.html)
    * [Access Control](https://help.sonatype.com/en/access-control.html)
      * [Privileges](https://help.sonatype.com/en/privileges.html)
      * [Roles](https://help.sonatype.com/en/roles.html)
      * [Users](https://help.sonatype.com/en/users.html)
      * [Default Role](https://help.sonatype.com/en/default-role.html)
      * [Content Selectors](https://help.sonatype.com/en/content-selectors.html)

    * [Authentication](https://help.sonatype.com/en/authentication.html)
      * [Realms](https://help.sonatype.com/en/realms.html)
      * [Anonymous Access](https://help.sonatype.com/en/anonymous-access.html)
      * [LDAP](https://help.sonatype.com/en/ldap.html)
      * [Local Authentication](https://help.sonatype.com/en/local-authentication.html)
      * [OpenID Connect](https://help.sonatype.com/en/openid-connect.html)
      * [SAML](https://help.sonatype.com/en/saml.html)
        * [Migrating User Tokens from LDAP to SAML](https://help.sonatype.com/en/migrating-from-ldap-to-saml.html)
        * [Migrating from Local Authentication to SAML](https://help.sonatype.com/en/migrating-from-local-authentication-to-saml.html)

      * [Authentication via Remote User Token](https://help.sonatype.com/en/authentication-via-remote-user-token.html)
      * [Reset the Admin Password](https://help.sonatype.com/en/reset-the-admin-password.html)
      * [Atlassian Crowd Support](https://help.sonatype.com/en/atlassian-crowd-support.html)
        * [Preparing Atlassian Crowd](https://help.sonatype.com/en/preparing-atlassian-crowd.html)
        * [Configure Crowd Integration](https://help.sonatype.com/en/configure-crowd-integration.html)

      * [User Tokens](https://help.sonatype.com/en/user-tokens.html)

    * [Blob Stores](https://help.sonatype.com/en/blob-stores.html)
      * [AWS Simple Storage Service (S3)](https://help.sonatype.com/en/aws-simple-storage-service--s3-.html)
      * [Azure Blob Store](https://help.sonatype.com/en/azure-blob-store.html)
      * [Google Cloud Blob Store](https://help.sonatype.com/en/google-cloud-blob-store.html)

    * [Capabilities](https://help.sonatype.com/en/capabilities.html)
      * [Auditing](https://help.sonatype.com/en/auditing.html)
      * [Base URL Capability](https://help.sonatype.com/en/base-url-capability.html)
      * [Branding Capability](https://help.sonatype.com/en/branding-capability.html)
      * [UI Settings Capability](https://help.sonatype.com/en/ui-settings-capability.html)

    * [Cleanup Policies](https://help.sonatype.com/en/cleanup-policies.html)
    * [Data Store](https://help.sonatype.com/en/data-store.html)
    * [HTTP Request and Proxy Settings](https://help.sonatype.com/en/http-request-and-proxy-settings.html)
    * [License Management](https://help.sonatype.com/en/license-management.html)
    * [Content Replication](https://help.sonatype.com/en/content-replication.html)
      * [Content Replication Use Cases](https://help.sonatype.com/en/content-replication-use-cases.html)

    * [Malware Risk](https://help.sonatype.com/en/malware-risk.html)
    * [Nodes](https://help.sonatype.com/en/nodes.html)
    * [Re-encryption in Nexus Repository](https://help.sonatype.com/en/re-encryption-in-nexus-repository.html)
    * [Repository Management](https://help.sonatype.com/en/repository-management.html)
      * [Repository Types](https://help.sonatype.com/en/repository-types.html)
      * [Creating Repositories](https://help.sonatype.com/en/creating-repositories.html)
      * [Configurable Repository Fields](https://help.sonatype.com/en/configurable-repository-fields.html)
      * [Repository Actions](https://help.sonatype.com/en/repository-actions.html)

    * [Repository Health Check](https://help.sonatype.com/en/repository-health-check.html)
    * [Routing Rules](https://help.sonatype.com/en/routing-rules.html)
    * [Staging](https://help.sonatype.com/en/staging.html)
      * [Staging Concepts](https://help.sonatype.com/en/staging-concepts.html)

    * [Support Features](https://help.sonatype.com/en/support-features.html)
      * [Status Checks](https://help.sonatype.com/en/status-checks.html)
      * [System Information](https://help.sonatype.com/en/system-information.html)
      * [Logging](https://help.sonatype.com/en/logging.html)
      * [Prometheus](https://help.sonatype.com/en/prometheus.html)
      * [Recovery Mode](https://help.sonatype.com/en/recovery-mode.html)

    * [Tagging](https://help.sonatype.com/en/tagging.html)
    * [Tasks](https://help.sonatype.com/en/tasks.html)
      * [Verify and Repair Data Consistency Tasks](https://help.sonatype.com/en/verify-and-repair-data-consistency-tasks.html)
      * [Change Repository Blob Store](https://help.sonatype.com/en/change-repository-blob-store.html)
      * [Maven SNAPSHOT Tasks](https://help.sonatype.com/en/maven-snapshot-tasks.html)
      * [Repository Export](https://help.sonatype.com/en/repository-export.html)
      * [Repository Import](https://help.sonatype.com/en/repository-import.html)

    * [Usage Metrics](https://help.sonatype.com/en/usage-metrics.html)
      * [Usage Center](https://help.sonatype.com/en/usage-center.html)
      * [How Components are Defined within Nexus Repository](https://help.sonatype.com/en/nexus-repository-component-definitions.html)
      * [Understanding Your Usage](https://help.sonatype.com/en/understanding-your-usage.html)

    * [Usage Metrics for Nexus Repository Manager 2 (NXRM2)](https://help.sonatype.com/en/usage-metrics-for-nexus-repository-manager-2--nxrm2-.html)

  * [Using Nexus Repository](https://help.sonatype.com/en/using-nexus-repository.html)
    * [Repository Manager Concepts](https://help.sonatype.com/en/repository-manager-concepts.html)
    * [User Interface Overview](https://help.sonatype.com/en/user-interface-overview.html)
    * [Working with Your User Profile](https://help.sonatype.com/en/working-with-your-user-profile.html)
    * [Browsing Repositories](https://help.sonatype.com/en/browsing-repositories.html)
    * [Component IQ](https://help.sonatype.com/en/component-iq.html)
    * [Searching for Components](https://help.sonatype.com/en/searching-for-components.html)
      * [SQL Search](https://help.sonatype.com/en/sql-search.html)
      * [Viewing Component Information](https://help.sonatype.com/en/viewing-component-information.html)
      * [Viewing Asset Information](https://help.sonatype.com/en/viewing-asset-information.html)

    * [Uploading Components](https://help.sonatype.com/en/uploading-components.html)
    * [Viewing Tags](https://help.sonatype.com/en/viewing-tags.html)

  * [Formats](https://help.sonatype.com/en/formats.html)
    * [APT Repositories](https://help.sonatype.com/en/apt-repositories.html)
    * [Bower Repositories](https://help.sonatype.com/en/bower-repositories.html)
    * [CocoaPods Repositories](https://help.sonatype.com/en/cocoapods-repositories.html)
    * [Composer Repositories](https://help.sonatype.com/en/composer-repositories.html)
    * [Conan Repositories](https://help.sonatype.com/en/conan-repositories.html)
    * [Conda Repositories](https://help.sonatype.com/en/conda-repositories.html)
    * [Docker Registry](https://help.sonatype.com/en/docker-registry.html)
      * [Docker Subdomain Connector](https://help.sonatype.com/en/docker-subdomain-connector.html)
      * [Docker Reverse Proxy Strategies](https://help.sonatype.com/en/docker-repository-reverse-proxy-strategies.html)
      * [Proxy Repository for Docker](https://help.sonatype.com/en/proxy-repository-for-docker.html)
      * [Hosted Repository for Docker](https://help.sonatype.com/en/hosted-repository-for-docker.html)
      * [Grouping Docker Repositories](https://help.sonatype.com/en/grouping-docker-repositories.html)
      * [Content Selectors and Docker](https://help.sonatype.com/en/content-selectors-and-docker.html)
      * [Docker Authentication](https://help.sonatype.com/en/docker-authentication.html)
      * [Searching](https://help.sonatype.com/en/searching.html)
      * [Pulling Images](https://help.sonatype.com/en/pulling-images.html)
      * [Pushing Images](https://help.sonatype.com/en/pushing-images.html)
      * [Pushing Images to a Group Repository](https://help.sonatype.com/en/pushing-images-to-a-group-repository.html)
      * [Foreign Layers](https://help.sonatype.com/en/foreign-layers.html)
      * [Docker Content Trust](https://help.sonatype.com/en/docker-content-trust.html)

    * [Git LFS Repositories](https://help.sonatype.com/en/git-lfs-repositories.html)
    * [Go Repositories](https://help.sonatype.com/en/go-repositories.html)
    * [Helm Repositories](https://help.sonatype.com/en/helm-repositories.html)
    * [Hugging Face Repositories](https://help.sonatype.com/en/hugging-face-repositories.html)
    * [Maven Repositories](https://help.sonatype.com/en/maven-repositories.html)
    * [npm Registry](https://help.sonatype.com/en/npm-registry.html)
      * [Configuring npm](https://help.sonatype.com/en/configuring-npm.html)
      * [npm Security](https://help.sonatype.com/en/npm-security.html)
      * [Publishing npm Packages](https://help.sonatype.com/en/publishing-npm-packages.html)
      * [Deprecating npm Packages](https://help.sonatype.com/en/deprecating-npm-packages.html)
      * [npm audit](https://help.sonatype.com/en/npm-audit.html)
      * [Download Cataloged Versions Only for Proxied Repositories](https://help.sonatype.com/en/download-cataloged-versions-only-for-proxied-repositories.html)
      * [Policy-Compliant Component Selection for npm](https://help.sonatype.com/en/policy-compliant-component-selection-for-npm.html)

    * [NuGet Repositories](https://help.sonatype.com/en/nuget-repositories.html)
    * [p2 Repositories](https://help.sonatype.com/en/p2-repositories.html)
    * [PyPI Repositories](https://help.sonatype.com/en/pypi-repositories.html)
    * [R Repositories](https://help.sonatype.com/en/r-repositories.html)
    * [Raw Repositories](https://help.sonatype.com/en/raw-repositories.html)
    * [RubyGems Repositories](https://help.sonatype.com/en/rubygems-repositories.html)
    * [Rust / Cargo Repositories](https://help.sonatype.com/en/rust-cargo.html)
    * [Swift Repositories](https://help.sonatype.com/en/swift-repositories.html)
      * [Create a Swift Repository](https://help.sonatype.com/en/create-a-swift-repository.html)
      * [Configure Swift with Nexus](https://help.sonatype.com/en/configure-spm-registry.html)
      * [Swift CLI Usage](https://help.sonatype.com/en/swift-cli-usage.html)

    * [Terraform Repositories](https://help.sonatype.com/en/terraform-repositories.html)
      * [Create a Terraform Repository](https://help.sonatype.com/en/create-a-terraform-repository.html)
      * [Configure Terraform with Nexus](https://help.sonatype.com/en/configure-registry.html)
      * [Terraform CLI Usage](https://help.sonatype.com/en/cli-usage-and-options.html)

    * [Yum Repositories](https://help.sonatype.com/en/yum-repositories.html)
      * [GPG signatures for Yum](https://help.sonatype.com/en/gpg-signatures-for-yum-proxy-group.html)
      * [Proxying RHEL Yum Repositories](https://help.sonatype.com/en/proxying-rhel-yum-repositories.html)

  * [Automation](https://help.sonatype.com/en/automation.html)
    * [Pagination](https://help.sonatype.com/en/pagination.html)
    * [Download artifacts using URI](https://help.sonatype.com/en/download-artifacts-using-uri.html)
    * [Webhooks](https://help.sonatype.com/en/webhooks.html)
      * [Enabling A Global Webhook Capability](https://help.sonatype.com/en/enabling-a-global-webhook-capability.html)
      * [Enabling A Repository Webhook Capability](https://help.sonatype.com/en/enabling-a-repository-webhook-capability.html)
      * [Working With HMAC Payloads](https://help.sonatype.com/en/working-with-hmac-payloads.html)
      * [Example Headers And Payloads](https://help.sonatype.com/en/example-headers-and-payloads.html)

    * [Bundle Development](https://help.sonatype.com/en/bundle-development.html)
      * [Support for a New Repository Format](https://help.sonatype.com/en/support-for-a-new-repository-format.html)

    * [Nexus Repository API Reference](https://help.sonatype.com/en/api-reference.html)
    * [Assets API](https://help.sonatype.com/en/assets-api.html)
    * [Blob Store API](https://help.sonatype.com/en/blob-store-api.html)
    * [Capabilities API](https://help.sonatype.com/en/capabilities-api.html)
    * [Configuration API](https://help.sonatype.com/en/configuration-api.html)
    * [Cleanup Policies API](https://help.sonatype.com/en/cleanup-policies-api.html)
    * [Components API](https://help.sonatype.com/en/components-api.html)
    * [Email API](https://help.sonatype.com/en/email-api.html)
    * [EULA REST API](https://help.sonatype.com/en/eula-rest-api.html)
    * [HTTP Configuration API](https://help.sonatype.com/en/http-configuration-api.html)
    * [Sonatype Repository Firewall API](https://help.sonatype.com/en/sonatype-repository-firewall-api.html)
    * [Licensing API](https://help.sonatype.com/en/licensing-api.html)
    * [Lifecycle API](https://help.sonatype.com/en/lifecycle-api.html)
    * [Log Management API](https://help.sonatype.com/en/log-management-api.html)
    * [Nodes API](https://help.sonatype.com/en/nodes-api.html)
    * [Read-Only API](https://help.sonatype.com/en/read-only-api.html)
    * [Repositories API](https://help.sonatype.com/en/repositories-api.html)
    * [Search API](https://help.sonatype.com/en/search-api.html)
    * [Security Management API](https://help.sonatype.com/en/security-management-api.html)
    * [Service Metrics Data API](https://help.sonatype.com/en/service-metrics-data-api.html)
    * [Script API](https://help.sonatype.com/en/script-api.html)
      * [Writing Scripts](https://help.sonatype.com/en/writing-scripts.html)
      * [Managing and Running Scripts](https://help.sonatype.com/en/managing-and-running-scripts.html)
      * [Examples](https://help.sonatype.com/en/examples.html)

    * [Status API](https://help.sonatype.com/en/status-api.html)
    * [Support API](https://help.sonatype.com/en/support-api.html)
    * [Tasks API](https://help.sonatype.com/en/tasks-api.html)
    * [User Tokens API](https://help.sonatype.com/en/user-tokens-api.html)

  * [Nexus Repository Best Practices](https://help.sonatype.com/en/nexus-repository-best-practices.html)
    * [Administration Best Practices](https://help.sonatype.com/en/administration-best-practices.html)
    * [Component Lifecycle Best Practices](https://help.sonatype.com/en/component-lifecycle-best-practices.html)
    * [Infrastructure-based Best Practices](https://help.sonatype.com/en/infrastructure-based-best-practices.html)
    * [Shadow Download Best Practices](https://help.sonatype.com/en/shadow-download-best-practices.html)

  * [Repository Manager 2](https://help.sonatype.com/en/repository-manager-2.html)

* [Sonatype IQ Server](https://help.sonatype.com/en/sonatype-iq-server.html)
  * [Sonatype IQ Server Release Notes](https://help.sonatype.com/en/iq-server-release-notes.html)
    * [2026 Release Notes](https://help.sonatype.com/en/sonatype-iq-server-2026-release-notes.html)
      * [Sonatype IQ Server 201 Release Notes](https://help.sonatype.com/en/sonatype-iq-server-201-release-notes.html)
      * [Sonatype IQ Server 200 Release Notes](https://help.sonatype.com/en/sonatype-iq-server-200-release-notes.html)

    * [2025 Release Notes](https://help.sonatype.com/en/sonatype-iq-server-2025-release-notes.html)
      * [Sonatype IQ Server 199 Release Notes](https://help.sonatype.com/en/sonatype-iq-server-199-release-notes.html)
      * [Sonatype IQ Server 198 Release Notes](https://help.sonatype.com/en/sonatype-iq-server-198-release-notes.html)
      * [Sonatype IQ Server 197 Release Notes](https://help.sonatype.com/en/sonatype-iq-server-197-release-notes.html)
      * [Sonatype IQ Server 196 Release Notes](https://help.sonatype.com/en/sonatype-iq-server-196-release-notes.html)
      * [Sonatype IQ Server 195 Release Notes](https://help.sonatype.com/en/sonatype-iq-server-195-release-notes.html)
      * [Sonatype IQ Server 194 Release Notes](https://help.sonatype.com/en/sonatype-iq-server-194-release-notes.html)
      * [Sonatype IQ Server 193 Release Notes](https://help.sonatype.com/en/sonatype-iq-server-193-release-notes.html)
      * [Sonatype IQ Server 192 Release Notes](https://help.sonatype.com/en/sonatype-iq-server-192-release-notes.html)
      * [Sonatype IQ Server 191 Release Notes](https://help.sonatype.com/en/sonatype-iq-server-191-release-notes.html)
      * [Sonatype IQ Server 190 Release Notes](https://help.sonatype.com/en/sonatype-iq-server-190-release-notes.html)
      * [Sonatype IQ Server 189 Release Notes](https://help.sonatype.com/en/sonatype-iq-server-189-release-notes.html)
      * [Sonatype IQ Server 188 Release Notes](https://help.sonatype.com/en/sonatype-iq-server-188-release-notes.html)
      * [Sonatype IQ Server 187 Release Notes](https://help.sonatype.com/en/sonatype-iq-server-187-release-notes.html)
      * [Sonatype IQ Server 186 Release Notes](https://help.sonatype.com/en/sonatype-iq-server-186-release-notes.html)

    * [2024 Release Notes](https://help.sonatype.com/en/iq-2024-release-notes.html)
    * [2023 Release Notes](https://help.sonatype.com/en/iq-2023-release-notes.html)
    * [2022 Release Notes](https://help.sonatype.com/en/iq-2022-release-notes.html)
    * [2021 Release Notes](https://help.sonatype.com/en/iq-2021-release-notes.html)
    * [2020 Release Notes](https://help.sonatype.com/en/iq-2020-release-notes.html)
    * [Track Resolved Issues](https://help.sonatype.com/en/track-resolved-issues.html)
    * [Release specific upgrade instructions](https://help.sonatype.com/en/release-specific-upgrade-instructions.html)

  * [Download and Compatibility](https://help.sonatype.com/en/download-and-compatibility.html)
    * [IQ Server Download Archives](https://help.sonatype.com/en/download-archives---iq-server---cli.html)

  * [IQ Server System Requirements](https://help.sonatype.com/en/system-requirements.html)
    * [Estimating Heap Sizes](https://help.sonatype.com/en/estimating-heap-sizes.html)

  * [Sonatype Cloud](https://help.sonatype.com/en/sonatype-cloud.html)
    * [Create the Sonatype Cloud Tenant](https://help.sonatype.com/en/create-the-sonatype-cloud-tenant.html)
    * [Authentication with Sonatype Cloud](https://help.sonatype.com/en/authentication-with-sonatype-cloud.html)
    * [User Management with Sonatype Cloud](https://help.sonatype.com/en/user-management-with-sonatype-cloud.html)
    * [Management Responsibilities for Sonatype Cloud](https://help.sonatype.com/en/responsibilities-for-sonatype-cloud.html)

  * [Legacy IQ Server Reference Architectures](https://help.sonatype.com/en/iq-server-reference-architecture.html)
    * [Small Size Deployments (Legacy)](https://help.sonatype.com/en/small-size-deployments.html)
    * [Medium Sized Deployments](https://help.sonatype.com/en/medium-sized-deployments.html)
    * [Large Sized Deployments (Legacy)](https://help.sonatype.com/en/large-sized-deployments.html)

  * [License and Features](https://help.sonatype.com/en/licensing-and-features.html)
    * [CPE Matching Experience in SBOM Manager vs. Lifecycle](https://help.sonatype.com/en/cpe-matching-experience-per-solution.html)

  * [Install self-hosted IQ Server](https://help.sonatype.com/en/install-self-hosted-iq-server.html)
    * [IQ Server Directory and Files](https://help.sonatype.com/en/iq-server-directory-and-files.html)
    * [Product License](https://help.sonatype.com/en/product-license.html)
    * [External Database Configuration](https://help.sonatype.com/en/external-database-configuration.html)
      * [Migrating IQ Server from H2 to PostgreSQL](https://help.sonatype.com/en/iq-migration-to-postgresql.html)

    * [Run IQ Server as a Service](https://help.sonatype.com/en/run-iq-server-as-a-service.html)
      * [Running as a Windows Service](https://help.sonatype.com/en/run-iq-server-as-a-windows-service.html)

    * [Switching from the IQ Server Standalone JAR to the Bundled JDK Assembly](https://help.sonatype.com/en/migrate-to-iq-with-bundled-jdk.html)
    * [IQ Server High Availability Installation](https://help.sonatype.com/en/iq-server-high-availability-installation.html)
      * [Installation on AWS](https://help.sonatype.com/en/installation-on-aws.html)
      * [Installation On-Premises](https://help.sonatype.com/en/installation-on-premises.html)
      * [Manual Self-Hosted High Availability IQ Server Deployment](https://help.sonatype.com/en/manual-self-hosted-iq-ha-deployment.html)
      * [Logging for HA](https://help.sonatype.com/en/logging-for-ha.html)
      * [Migrating to HA Setup](https://help.sonatype.com/en/migrating-to-ha-setup.html)
      * [Performance Benchmarks for High Availability](https://help.sonatype.com/en/performance-benchmarks-for-high-availability.html)

    * [Upgrade the IQ Server](https://help.sonatype.com/en/upgrading-the-iq-server.html)
    * [Backup the IQ Server](https://help.sonatype.com/en/backing-up-the-iq-server.html)
    * [Restore the IQ Server](https://help.sonatype.com/en/restoring-the-iq-server.html)
    * [Move the installation](https://help.sonatype.com/en/move-the-installation.html)

  * [Sonatype Solution Switcher](https://help.sonatype.com/en/sonatype-solution-switcher.html)
  * [Manage User Account](https://help.sonatype.com/en/manage-your-user-account.html)
  * [Add-on Packs](https://help.sonatype.com/en/add-on-packs.html)
    * [Advanced Legal Pack Quickstart](https://help.sonatype.com/en/advanced-legal-pack-quickstart.html)

  * [Sonatype Vulnerability Data](https://help.sonatype.com/en/sonatype-vulnerability-data.html)
    * [Working with Vulnerability Data](https://help.sonatype.com/en/working-with-vulnerability-data.html)
    * [Custom Vulnerability Attributes](https://help.sonatype.com/en/custom-vulnerability-attributes.html)

  * [Threats in AI/ML Models](https://help.sonatype.com/en/threats-in-ai-ml-models.html)
  * [Sonatype Malware Data](https://help.sonatype.com/en/sonatype-malware-data.html)
  * [Sonatype Data Handling Process](https://help.sonatype.com/en/sonatype-data-handling-process.html)
  * [Naming conventions for OSS licenses](https://help.sonatype.com/en/naming-conventions-for-oss-licenses.html)
  * [Package URLs (purl) and Component Identifiers](https://help.sonatype.com/en/package-url-and-component-identifiers.html)
  * [IQ API Reference](https://help.sonatype.com/en/iq-api-reference.html)

* [Sonatype Lifecycle](https://help.sonatype.com/en/sonatype-lifecycle.html)
  * [Product Information and Downloads](https://help.sonatype.com/en/lifecycle-product-information.html)
  * [Lifecycle Release Notes](https://help.sonatype.com/en/lifecycle-release-notes.html)
  * [Getting Started](https://help.sonatype.com/en/getting-started.html)
    * [Deployment Options](https://help.sonatype.com/en/deployment-options.html)
    * [Getting Started with Lifecycle SaaS](https://help.sonatype.com/en/getting-started-with-lifecycle-saas.html)
      * [Service Limits for Lifecycle SaaS](https://help.sonatype.com/en/service-limits-for-lifecycle-saas.html)

    * [Phase 1 - Installation and Configuration](https://help.sonatype.com/en/phase-1---installation-and-configuration.html)
    * [Phase 2 - Reviewing and Assessing Risk](https://help.sonatype.com/en/phase-2---reviewing-and-assessing-risk.html)
    * [Phase 3 - Removing Risk](https://help.sonatype.com/en/phase-3---removing-risk.html)

  * [Configuring](https://help.sonatype.com/en/configuring.html)
    * [Sonatype Lifecycle FIPS 140-3 Compliance](https://help.sonatype.com/en/sonatype-lifecycle-fips-compliance.html)
    * [Config YAML](https://help.sonatype.com/en/config-yaml.html)
      * [Configuring with Java System Properties](https://help.sonatype.com/en/configuring-with-java-system-properties.html)
      * [Configuring with Environment Variables](https://help.sonatype.com/en/configuring-with-environment-variables.html)

    * [Configuring Base URL](https://help.sonatype.com/en/configuring-base-url.html)
    * [Configuring Outbound Traffic](https://help.sonatype.com/en/configuring-outbound-traffic.html)
    * [Configuring Inbound Traffic](https://help.sonatype.com/en/configuring-inbound-traffic.html)
    * [Reverse Proxy Authentication](https://help.sonatype.com/en/reverse-proxy-authentication.html)
    * [Public Key Infrastructure (PKI) Authentication](https://help.sonatype.com/en/pki-authentication.html)
    * [Data Retention](https://help.sonatype.com/en/data-retention.html)
    * [Notification Configuration](https://help.sonatype.com/en/notification-configuration.html)
    * [Configuring System Notice](https://help.sonatype.com/en/configuring-system-notice.html)
    * [Logging Configuration](https://help.sonatype.com/en/logging-configuration.html)
      * [Audit Log](https://help.sonatype.com/en/audit-log.html)
      * [Policy Violation Log](https://help.sonatype.com/en/policy-violation-log.html)

    * [Sample Data Configuration](https://help.sonatype.com/en/sample-data-configuration.html)
    * [InnerSource Repository Configuration](https://help.sonatype.com/en/innersource-repository-configuration.html)
    * [Public Data Sources for CPE Vulnerabilities](https://help.sonatype.com/en/public-data-sources.html)
      * [CPE Matching Experience in SBOM Manager vs. Lifecycle](https://help.sonatype.com/en/cpe-matching-experience-per-solution-390065.html)

    * [Waived Component Upgrades](https://help.sonatype.com/en/waived-component-upgrades.html)
    * [Certificates and Secure Connections](https://help.sonatype.com/en/certificates-and-secure-connections.html)
    * [Operational Menu](https://help.sonatype.com/en/operational-menu.html)
    * [Advanced Legal Pack Extended Observed License Detections](https://help.sonatype.com/en/advanced-legal-pack-extended-observed-license-detections.html)

  * [Managing](https://help.sonatype.com/en/managing.html)
    * [Application Management](https://help.sonatype.com/en/application-management.html)
      * [Automatic Applications](https://help.sonatype.com/en/automatic-application.html)
      * [Automatic Source Control](https://help.sonatype.com/en/automatic-source-control.html)
      * [Manual Evaluation](https://help.sonatype.com/en/manual-evaluation.html)
      * [Continuous Monitoring](https://help.sonatype.com/en/continuous-monitoring.html)
        * [Continuous Monitoring Concepts](https://help.sonatype.com/en/continuous-monitoring-concepts.html)

    * [Organization Management](https://help.sonatype.com/en/organization-management.html)
      * [Manage Organizations](https://help.sonatype.com/en/manage-organizations.html)

    * [Policy Management](https://help.sonatype.com/en/policy-management.html)
      * [Policy Concepts](https://help.sonatype.com/en/policy-concepts.html)
        * [License Policy Governance](https://help.sonatype.com/en/license-policy-governance.html)

      * [Reference Policies](https://help.sonatype.com/en/reference-policies.html)
        * [Architecture Policies](https://help.sonatype.com/en/architecture-policies.html)
        * [Component Policies](https://help.sonatype.com/en/component-policies.html)
        * [Security Policies](https://help.sonatype.com/en/security-policies.html)
        * [License Policies](https://help.sonatype.com/en/license-policies.html)

      * [Configuring Policies](https://help.sonatype.com/en/configuring-policies.html)
      * [Application Categories](https://help.sonatype.com/en/application-categories.html)
      * [Component Labels](https://help.sonatype.com/en/component-labels.html)
      * [Continuous Monitoring](https://help.sonatype.com/en/continuous-monitoring-201455.html)
      * [Legacy Violations](https://help.sonatype.com/en/legacy-violations.html)
      * [License Threat Groups](https://help.sonatype.com/en/license-threat-groups.html)
      * [Policy Actions](https://help.sonatype.com/en/policy-actions.html)
      * [Policy Constraints](https://help.sonatype.com/en/policy-constraints.html)
      * [Policy Inheritance](https://help.sonatype.com/en/policy-inheritance.html)
      * [Policy Notifications](https://help.sonatype.com/en/policy-notifications.html)
      * [Policy Overrides](https://help.sonatype.com/en/policy-overrides.html)

    * [User Management](https://help.sonatype.com/en/user-management.html)
      * [LDAP Integration](https://help.sonatype.com/en/ldap-integration.html)
      * [Role Management](https://help.sonatype.com/en/role-management.html)
        * [Role-Based Access Control](https://help.sonatype.com/en/role-based-access-control.html)

      * [Resetting the Admin Account Password and Roles](https://help.sonatype.com/en/resetting-the-admin-account-password-and-roles.html)
      * [SAML Integration](https://help.sonatype.com/en/saml-integration.html)
      * [User Tokens](https://help.sonatype.com/en/iq-server-user-tokens.html)
      * [OIDC/OAuth2 Configuration](https://help.sonatype.com/en/oidc-oauth2-configuration.html)
      * [Atlassian Crowd Integration Configuration](https://help.sonatype.com/en/atlassian-crowd-integration-configuration.html)
      * [IQ Server Realms](https://help.sonatype.com/en/iq-server-realms.html)
      * [Authorization and Authentication Concepts](https://help.sonatype.com/en/authorization-and-authentication-concepts.html)

  * [Reporting](https://help.sonatype.com/en/reporting.html)
    * [Lifecycle Dashboard](https://help.sonatype.com/en/lifecycle-dashboard.html)
      * [Dashboard Filters](https://help.sonatype.com/en/dashboard-filters.html)
      * [Export Violation Data](https://help.sonatype.com/en/export-violation-data.html)
      * [Export Component Data](https://help.sonatype.com/en/export-component-data.html)
      * [Export Applications Data](https://help.sonatype.com/en/export-application-data.html)
      * [Exporting Waiver Data](https://help.sonatype.com/en/export-waiver-data.html)

    * [Waivers](https://help.sonatype.com/en/waivers.html)
      * [Waiver Management](https://help.sonatype.com/en/waiver-tasks.html)
      * [Automated Waivers](https://help.sonatype.com/en/automated-waivers.html)
      * [Examples of Waiver Scoping](https://help.sonatype.com/en/examples-of-waiver-scoping.html)
      * [Similar Waivers](https://help.sonatype.com/en/similar-waivers.html)
      * [Bulk Waivers](https://help.sonatype.com/en/bulk-waivers.html)
      * [Requested Waivers](https://help.sonatype.com/en/requested-waivers.html)
      * [Transitive Violation Waivers for InnerSource](https://help.sonatype.com/en/transitive-violation-waivers-for-innersource-components.html)

    * [Application Composition Report](https://help.sonatype.com/en/application-composition-report.html)
      * [Accessing the Report](https://help.sonatype.com/en/accessing-the-report.html)
      * [Reviewing a Report](https://help.sonatype.com/en/reviewing-a-report.html)
      * [Component Details Page](https://help.sonatype.com/en/component-details-page.html)
      * [Component Information Panel](https://help.sonatype.com/en/component-information-panel.html)
      * [Dependency Tree](https://help.sonatype.com/en/dependency-tree.html)
      * [Reviewing Security Vulnerabilities](https://help.sonatype.com/en/reviewing-security-vulnerabilities.html)
      * [Component License Information](https://help.sonatype.com/en/component-license-information.html)
      * [Component Identification](https://help.sonatype.com/en/component-identification.html)
        * [Claiming a Component](https://help.sonatype.com/en/claiming-a-component.html)
        * [Proprietary Component Configuration](https://help.sonatype.com/en/proprietary-component-configuration.html)

      * [Assigning Component Labels](https://help.sonatype.com/en/assigning-component-labels.html)
      * [Scan Reports](https://help.sonatype.com/en/scan-reports.html)
      * [View Latest Evaluations](https://help.sonatype.com/en/latest-evaluations.html)
      * [PDF Report](https://help.sonatype.com/en/pdf-report.html)
      * [Options Dropdown](https://help.sonatype.com/en/options-dropdown.html)
      * [InnerSource Insight](https://help.sonatype.com/en/innersource-insight.html)
      * [Re-evaluating a Report](https://help.sonatype.com/en/re-evaluating-a-report.html)

    * [Success Metrics](https://help.sonatype.com/en/legacy-success-metrics.html)
    * [Vulnerability Lookup](https://help.sonatype.com/en/vulnerability-lookup.html)
    * [Advanced Search](https://help.sonatype.com/en/advanced-search.html)
      * [Search Examples](https://help.sonatype.com/en/search-examples.html)

    * [Enterprise Reporting](https://help.sonatype.com/en/data-insights.html)
      * [AI Models Usage](https://help.sonatype.com/en/ai-models-usage.html)
      * [Component End-of-Life](https://help.sonatype.com/en/component-end-of-life.html)
      * [Machine Learning AI](https://help.sonatype.com/en/machine-learning-ai.html)
      * [Supply Chain Monitoring](https://help.sonatype.com/en/supply-chain-monitoring.html)
      * [Stack Divergence](https://help.sonatype.com/en/stack-divergence.html)
      * [Security Risk Trends](https://help.sonatype.com/en/security-risk-trends.html)
      * [Legal Risk Trends](https://help.sonatype.com/en/legal-risk-trends.html)
      * [Golden Fixes Dashboard](https://help.sonatype.com/en/golden-fixes-dashboard.html)
      * [Security Risk Breakdown](https://help.sonatype.com/en/security-risk-breakdown.html)
      * [Success Metrics Enterprise Dashboard](https://help.sonatype.com/en/success-metrics.html)
      * [Waivers Explorer](https://help.sonatype.com/en/waivers-explorer.html)
      * [HeroDevs End of Life Components](https://help.sonatype.com/en/herodevs-end-of-life-components.html)

  * [Automating](https://help.sonatype.com/en/automating.html)
    * [REST APIs](https://help.sonatype.com/en/rest-apis.html)
      * [Role Membership and Mapping APIs](https://help.sonatype.com/en/role-membership---mapping-apis.html)
      * [OIDC/OAuth2 Configuration](https://help.sonatype.com/en/oidc-oauth2-configuration-504596.html)
      * [IQ API Reference](https://help.sonatype.com/en/iq-api-reference-338492.html)
      * [Advanced Search REST API](https://help.sonatype.com/en/advanced-search-rest-api.html)
      * [Application Categories REST API](https://help.sonatype.com/en/application-categories-rest-api.html)
      * [Application REST API](https://help.sonatype.com/en/application-rest-api.html)
      * [Organizations REST API](https://help.sonatype.com/en/organizations-rest-api.html)
      * [Report REST APIs](https://help.sonatype.com/en/report-rest-api.html)
      * [Atlassian Crowd REST API](https://help.sonatype.com/en/atlassian-crowd-rest-api.html)
      * [Audit Log REST API](https://help.sonatype.com/en/audit-log-rest-api.html)
      * [Authorization Configuration REST API](https://help.sonatype.com/en/authorization-configuration-rest-api.html)
      * [Component Claim REST API](https://help.sonatype.com/en/component-claim-rest-api.html)
      * [Component Details REST API](https://help.sonatype.com/en/component-details-rest-api.html)
      * [Component Evaluation REST API](https://help.sonatype.com/en/component-evaluation-rest-api.html)
      * [Component Labels REST API](https://help.sonatype.com/en/component-labels-rest-api.html)
      * [Component Remediation REST API](https://help.sonatype.com/en/component-remediation-rest-api.html)
      * [Component Search REST API](https://help.sonatype.com/en/component-search-rest-api.html)
      * [Component Versions REST API](https://help.sonatype.com/en/component-versions-rest-api.html)
      * [Configuration REST API](https://help.sonatype.com/en/configuration-rest-api.html)
      * [CPE Matching REST API](https://help.sonatype.com/en/cpe-matching-rest-api.html)
      * [Cross-Stage Policy Violation REST API](https://help.sonatype.com/en/cross-stage-policy-violation-rest-api.html)
      * [Data Retention Policy REST API](https://help.sonatype.com/en/data-retention-policy-rest-api.html)
      * [Feature Configuration REST API](https://help.sonatype.com/en/feature-configuration-rest-api.html)
      * [Mail REST API](https://help.sonatype.com/en/mail-rest-api.html)
      * [HTTP Proxy Server Configuration REST API](https://help.sonatype.com/en/http-proxy-server-configuration-rest-api.html)
      * [JIRA Configuration REST API](https://help.sonatype.com/en/jira-configuration-rest-api.html)
      * [License Legal REST API](https://help.sonatype.com/en/license-legal-rest-api.html)
      * [License Overrides REST API](https://help.sonatype.com/en/license-override-rest-api.html)
      * [OIDC Configuration REST API](https://help.sonatype.com/en/oidc-configuration-rest-api.html)
      * [Product License REST API](https://help.sonatype.com/en/product-license-rest-api.html)
      * [Manifest Evaluation REST API](https://help.sonatype.com/en/manifest-evaluation-rest-api.html)
      * [Policy Violation REST API](https://help.sonatype.com/en/policy-violation-rest-api.html)
      * [Policy Waiver REST API](https://help.sonatype.com/en/policy-waiver-rest-api.html)
      * [Policy Waiver Request REST API](https://help.sonatype.com/en/policy-waiver-request-rest-api.html)
      * [Auto Policy Waiver REST API](https://help.sonatype.com/en/auto-policy-waiver-rest-api.html)
      * [Exclude Auto Policy Waiver REST API](https://help.sonatype.com/en/exclude-auto-policy-waiver-rest-api.html)
      * [Applicable Waivers REST API](https://help.sonatype.com/en/applicable-waivers-rest-api.html)
      * [Similar Waivers REST API](https://help.sonatype.com/en/similar-waivers-rest-api.html)
      * [Component Waivers REST API](https://help.sonatype.com/en/component-waivers-rest-api.html)
      * [Stale Waivers REST API](https://help.sonatype.com/en/stale-waivers-rest-api.html)
      * [Transitive Waivers REST API](https://help.sonatype.com/en/transitive-waivers-rest-api.html)
      * [Waiver Reason REST API](https://help.sonatype.com/en/waiver-reason-rest-api.html)
      * [Promote Scan REST API](https://help.sonatype.com/en/promote-scan-rest-api.html)
      * [Reverse Proxy Authentication Configuration REST API](https://help.sonatype.com/en/reverse-proxy-authentication-configuration-rest-api.html)
      * [Role REST API](https://help.sonatype.com/en/role-rest-api.html)
      * [Role Membership and Mapping APIs](https://help.sonatype.com/en/role-membership---mapping-apis-504598.html)
      * [SAML REST API](https://help.sonatype.com/en/saml-rest-api.html)
      * [Security Vulnerability Override API](https://help.sonatype.com/en/security-vulnerability-override-api.html)
      * [Source Control Configuration REST API](https://help.sonatype.com/en/source-control-configuration-rest-api.html)
      * [Source Control Evaluation REST API](https://help.sonatype.com/en/source-control-evaluation-rest-api.html)
      * [Source Control REST API](https://help.sonatype.com/en/source-control-rest-api.html)
      * [CycloneDX REST API](https://help.sonatype.com/en/cyclonedx-rest-api.html)
      * [SPDX REST API](https://help.sonatype.com/en/spdx-rest-api.html)
      * [Success Metrics Data REST API](https://help.sonatype.com/en/success-metrics-data-rest-api.html)
      * [Third-Party Analysis REST API](https://help.sonatype.com/en/third-party-scan-rest-api.html)
      * [User REST API](https://help.sonatype.com/en/user-rest-api.html)
      * [User Token REST API](https://help.sonatype.com/en/user-token-rest-api.html)
      * [User Token Expiration Configuration REST API](https://help.sonatype.com/en/user-token-expiration-configuration-rest-api.html)
      * [Vulnerability Details REST API](https://help.sonatype.com/en/vulnerability-details-rest-api.html)

    * [Lifecycle Webhooks](https://help.sonatype.com/en/lifecycle-webhooks.html)
      * [Lifecycle Webhooks Events Types](https://help.sonatype.com/en/lifecycle-webhooks-events-types.html)
      * [Webhooks Concepts: IQ Server and Slack Integration](https://help.sonatype.com/en/webhooks-concepts--iq-server-and-slack-integration.html)

    * [Experimental APIs](https://help.sonatype.com/en/experimental-apis.html)
      * [Repository Results REST API](https://help.sonatype.com/en/repository-results-rest-api.html)
      * [Vulnerability Custom Attributes REST API](https://help.sonatype.com/en/vulnerability-custom-attributes-rest-api.html)
      * [Vulnerability Group REST API](https://help.sonatype.com/en/vulnerability-group-rest-api.html)
      * [Vulnerability Analysis Details REST API](https://help.sonatype.com/en/vulnerability-analysis-details-rest-api.html)
      * [Call Flow Analysis REST API](https://help.sonatype.com/en/call-flow-analysis-rest-api.html)
      * [Signatures REST API](https://help.sonatype.com/en/signatures-rest-api.html)
      * [ALP Dashboard REST APIs](https://help.sonatype.com/en/alp-dashboard-rest-apis.html)
      * [Attributions REST API](https://help.sonatype.com/en/attributions-rest-api.html)
      * [Copyrights REST API](https://help.sonatype.com/en/copyrights-rest-api.html)
      * [Obligations REST API](https://help.sonatype.com/en/obligations-rest-api.html)
      * [Legal REST API](https://help.sonatype.com/en/legal-rest-api.html)
      * [Source Link REST API](https://help.sonatype.com/en/source-link-rest-api.html)

  * [Analysis](https://help.sonatype.com/en/analysis.html)
    * [C/C++ Application Analysis](https://help.sonatype.com/en/c-c---application-analysis.html)
    * [Clair Application Analysis](https://help.sonatype.com/en/clair-application-analysis.html)
    * [Conda Application Analysis](https://help.sonatype.com/en/conda-application-analysis.html)
    * [CycloneDX Application Analysis](https://help.sonatype.com/en/cyclonedx.html)
    * [Dart and Flutter Analysis](https://help.sonatype.com/en/dart-and-flutter-analysis.html)
    * [Docker Image Analysis](https://help.sonatype.com/en/docker-image-analysis.html)
    * [Go Application Analysis](https://help.sonatype.com/en/go-application-analysis.html)
    * [Java Application Analysis](https://help.sonatype.com/en/java-application-analysis.html)
    * [npm Application Analysis](https://help.sonatype.com/en/npm-application-analysis.html)
      * [Preparing to Run npm Application Analysis](https://help.sonatype.com/en/preparing-to-run-npm-application-analysis.html)
      * [Steps for Performing npm Application Analysis](https://help.sonatype.com/en/steps-for-performing-npm-application-analysis.html)

    * [NuGet Application Analysis](https://help.sonatype.com/en/nuget-application-analysis.html)
    * [Objective-C Application Analysis](https://help.sonatype.com/en/objective-c-application-analysis.html)
    * [PHP Application Analysis](https://help.sonatype.com/en/php-application-analysis.html)
    * [Python Application Analysis](https://help.sonatype.com/en/python-application-analysis.html)
    * [R (CRAN) Application Analysis](https://help.sonatype.com/en/r--cran--application-analysis.html)
    * [Ruby Application Analysis](https://help.sonatype.com/en/ruby-application-analysis.html)
    * [Rust Application Analysis](https://help.sonatype.com/en/rust-application-analysis.html)
    * [SPDX Application Analysis](https://help.sonatype.com/en/spdx-application-analysis.html)
    * [Swift Application Analysis](https://help.sonatype.com/en/swift-application-analysis.html)
    * [Yum Analysis](https://help.sonatype.com/en/yum-analysis.html)
    * [Hugging Face Model Analysis](https://help.sonatype.com/en/hugging-face-model-analysis.html)
    * [Threats in AI/ML Models](https://help.sonatype.com/en/threats-in-ai-ml-models-315000.html)

  * [Lifecycle Best Practices](https://help.sonatype.com/en/lifecycle-best-practices.html)
    * [Lifecycle Deployment Best Practices](https://help.sonatype.com/en/lifecycle-deployment-best-practices.html)
      * [Project Initiation (1st month)](https://help.sonatype.com/en/project-initiation--1st-month-.html)
      * [Project Pilot (first 2 months)](https://help.sonatype.com/en/project-pilot--first-2-months-.html)
      * [Project Commencement (1st year)](https://help.sonatype.com/en/project-commencement--1st-year-.html)

    * [Onboarding Applications Best Practices](https://help.sonatype.com/en/onboarding-applications-best-practices.html)
    * [Legacy Violations Best Practices](https://help.sonatype.com/en/legacy-violations-best-practices.html)
    * [Hierarchy and Inheritance Best Practices](https://help.sonatype.com/en/hierarchy-and-inheritance-best-practices.html)
    * [Waiver Best Practices](https://help.sonatype.com/en/waiver-best-practices.html)
      * [Example Waiver Workflows](https://help.sonatype.com/en/example-waiver-workflows.html)

    * [InnerSource Best Practices](https://help.sonatype.com/en/innersource-best-practices.html)
    * [Software Bill of Materials Best Practices](https://help.sonatype.com/en/software-bill-of-materials-best-practices.html)
      * [Guidelines for Using Lifecycle with SBOMs for Monitoring](https://help.sonatype.com/en/guidelines-for-using-lifecycle-with-sboms-for-monitoring.html)

    * [Policy Enforcement Best Practices](https://help.sonatype.com/en/policy-enforcement-best-practices.html)
    * [Reference Policy Best Practices](https://help.sonatype.com/en/reference-policy-best-practices.html)
    * [Continuous Monitoring Best Practices](https://help.sonatype.com/en/continuous-monitoring-best-practices.html)
    * [General Lifecycle Best Practices](https://help.sonatype.com/en/general-lifecycle-best-practices.html)
    * [Zero-Day Vulnerability Best Practices](https://help.sonatype.com/en/zero-day-vulnerability-best-practices.html)
    * [Source Control Integration Best Practices](https://help.sonatype.com/en/source-control-integration-best-practices.html)
    * [Backup and Restore Best Practices](https://help.sonatype.com/en/backup-and-restore-best-practices.html)
    * [Data Management and Storage Best Practices](https://help.sonatype.com/en/data-management-and-storage-best-practices.html)
    * [Creating a Lifecycle Remediation Plan](https://help.sonatype.com/en/creating-a-lifecycle-remediation-plan.html)
    * [Remediation Best Practices](https://help.sonatype.com/en/remediation-best-practices.html)

* [Sonatype Repository Firewall](https://help.sonatype.com/en/repository-firewall.html)
  * [Product Information and Downloads](https://help.sonatype.com/en/firewall-product-information.html)
  * [Repository Firewall Release Notes](https://help.sonatype.com/en/repository-firewall-release-notes.html)
  * [Repository Firewall Getting Started](https://help.sonatype.com/en/repository-firewall-getting-started.html)
    * [Nexus Repository 3 Pro Setup](https://help.sonatype.com/en/nexus-repository-3-pro-setup.html)
      * [Firewall Audit and Quarantine Capability](https://help.sonatype.com/en/firewall-audit-and-quarantine-capability.html)
      * [Firewall Results in Nexus Repository](https://help.sonatype.com/en/firewall-results-in-nexus-repository.html)

    * [JFrog Artifactory Setup](https://help.sonatype.com/en/jfrog-artifactory-setup.html)
      * [Getting the Firewall results page through the JFrog Artifactory API](https://help.sonatype.com/en/getting-the-firewall-results-page-through-the-jfrog-artifactory-api.html)
      * [Firewall for Artifactory Configuration](https://help.sonatype.com/en/jfrog-artifactory-plugin-configuration.html)
      * [JFrog Artifactory Plugin Configuration REST API](https://help.sonatype.com/en/jfrog-artifactory-plugin-configuration-rest-api.html)
      * [Upgrading Firewall for Artifactory plugin](https://help.sonatype.com/en/upgrading-firewall-for-artifactory-plugin.html)
      * [Uninstalling the Firewall for Artifactory Plugin](https://help.sonatype.com/en/uninstalling-the-firewall-for-artifactory-plugin.html)
      * [Firewall for Artifactory Release Notes](https://help.sonatype.com/en/repository-firewall-for-artifactory-plugin-release-notes.html)

  * [Firewall Navigation](https://help.sonatype.com/en/firewall-navigation.html)
    * [Firewall Dashboard](https://help.sonatype.com/en/firewall-dashboard.html)
    * [Quarantined Component View](https://help.sonatype.com/en/quarantined-component-view.html)
    * [Repository Results View](https://help.sonatype.com/en/repository-results-view.html)

  * [Firewall Quarantine](https://help.sonatype.com/en/firewall-quarantine.html)
    * [Automatic Quarantine Release](https://help.sonatype.com/en/automatic-quarantine-release.html)
    * [Custom Quarantine Messages](https://help.sonatype.com/en/custom-quarantine-messages.html)

  * [Enterprise Reporting](https://help.sonatype.com/en/enterprise-reporting.html)
    * [Firewall Malware Insights](https://help.sonatype.com/en/firewall-malware.html)

  * [Guide to Removing Malware](https://help.sonatype.com/en/guide-to-removing-malware.html)
  * [Firewall for Docker](https://help.sonatype.com/en/firewall-for-docker.html)
  * [Namespace Confusion Protection](https://help.sonatype.com/en/namespace-confusion-protection.html)
  * [Policy Compliant Component Selection](https://help.sonatype.com/en/policy-compliant-component-selection.html)
  * [Release Integrity](https://help.sonatype.com/en/release-integrity.html)
  * [Integrate Firewall with Zscaler](https://help.sonatype.com/en/zscaler.html)
  * [Repository Firewall Best Practices](https://help.sonatype.com/en/repository-firewall-best-practices.html)
  * [Firewall APIs](https://help.sonatype.com/en/firewall-apis.html)
    * [Container Waivers API](https://help.sonatype.com/en/container-waivers-api.html)
    * [Cascade Component Re-evaluation API](https://help.sonatype.com/en/cascade-component-re-evaluation-api.html)
    * [Repository Firewall Hashing](https://help.sonatype.com/en/repository-firewall-hashing.html)
    * [Repository Firewall Evaluation API](https://help.sonatype.com/en/firewall-evaluation-api.html)
    * [Quarantine REST API](https://help.sonatype.com/en/quarantine-rest-api.html)
    * [Repository Results REST API](https://help.sonatype.com/en/repository-results-rest-api-285699.html)
    * [Namespace Confusion API](https://help.sonatype.com/en/namespace-confusion-api.html)
    * [Malware Defense Evaluate API](https://help.sonatype.com/en/malware-defense-evaluate-api.html)

* [Sonatype SBOM Manager](https://help.sonatype.com/en/sonatype-sbom-manager.html)
  * [Product Information and Downloads](https://help.sonatype.com/en/sbom-manager-product-information.html)
  * [SBOM Manager Release Notes](https://help.sonatype.com/en/sbom-manager-release-notes.html)
  * [Getting Started](https://help.sonatype.com/en/sbom-getting-started.html)
  * [Software Bill of Materials (SBOM)](https://help.sonatype.com/en/software-bill-of-materials-sbom.html)
  * [Dashboard View](https://help.sonatype.com/en/sbom-dashboard-view.html)
  * [Organizations View](https://help.sonatype.com/en/sbom-organizations-view.html)
  * [Applications View](https://help.sonatype.com/en/sbom-applications.html)
  * [Advanced Search View](https://help.sonatype.com/en/sbom-search.html)
    * [Search Examples](https://help.sonatype.com/en/search-examples-215924.html)

  * [Legal View](https://help.sonatype.com/en/sbom-legal.html)
  * [SBOM Manager API](https://help.sonatype.com/en/sbom-manager-api.html)
  * [Importing SBOMs](https://help.sonatype.com/en/sbom-import.html)
  * [SBOM Bill of Material View](https://help.sonatype.com/en/sbom-bill-of-material-view.html)
  * [SBOM Component Details View](https://help.sonatype.com/en/sbom-component-details-view.html)
  * [SBOM Continuous Monitoring](https://help.sonatype.com/en/sbom-continuous-monitoring.html)
  * [SBOM VEX Workflow](https://help.sonatype.com/en/sbom-vex-workflow.html)

* [Sonatype Developer](https://help.sonatype.com/en/sonatype-developer.html)
  * [Product Information and Downloads](https://help.sonatype.com/en/developer-product-information.html)
  * [Sonatype Developer Release Notes](https://help.sonatype.com/en/sonatype-developer-release-notes.html)
  * [Developer Dashboard](https://help.sonatype.com/en/developer-dashboard.html)
  * [Golden Versions](https://help.sonatype.com/en/golden-versions-and-prs.html)
  * [Priorities View](https://help.sonatype.com/en/priorities-view.html)
    * [Prioritization Algorithm](https://help.sonatype.com/en/prioritization-algorithm.html)
    * [Create PRs from Priorities View](https://help.sonatype.com/en/create-prs-from-priorities-view.html)
    * [View Waivers from the Priorities View](https://help.sonatype.com/en/view-waivers-from-the-priorities-view.html)

  * [Reachability Analysis](https://help.sonatype.com/en/reachability-analysis.html)
  * [REST APIs](https://help.sonatype.com/en/rest-apis-307236.html)
    * [Priorities REST API](https://help.sonatype.com/en/priorities-rest-api.html)

* [Sonatype Integrations](https://help.sonatype.com/en/sonatype-integrations.html)
  * [Notable Integrations Changes](https://help.sonatype.com/en/notable-integrations-changes.html)
    * [2026 Notable Integrations Bug Fixes](https://help.sonatype.com/en/2026-notable-integrations-bug-fixes.html)
    * [2025 Notable Integrations Bug Fixes](https://help.sonatype.com/en/2025-notable-integrations-bug-fixes.html)
    * [2024 Notable Integrations Bug Fixes](https://help.sonatype.com/en/2024-notable-integrations-bug-fixes.html)

  * [Azure DevOps](https://help.sonatype.com/en/sonatype-for-azure-devops.html)
    * [Installation and Configuration - Sonatype for Azure DevOps](https://help.sonatype.com/en/installation-and-configuration---sonatype-for-azure-devops.html)
    * [Reachability Analysis with Sonatype for Azure DevOps](https://help.sonatype.com/en/reachability-analysis-with-sonatype-for-azure-devops.html)

  * [Bamboo Data Center](https://help.sonatype.com/en/sonatype-for-bamboo-data-center.html)
    * [Installation and Configuration - Sonatype for Bamboo Data Center](https://help.sonatype.com/en/installation-and-configuration---sonatype-for-bamboo-data-center.html)
    * [Reachability Analysis with Bamboo](https://help.sonatype.com/en/reachability-analysis-with-bamboo.html)

  * [Container Security](https://help.sonatype.com/en/sonatype-container-security.html)
  * [Eclipse](https://help.sonatype.com/en/iq-for-eclipse.html)
  * [Fortify SSC](https://help.sonatype.com/en/sonatype-fortify-ssc.html)
    * [Integration of IQ Webhook with Fortify SSC Sync Service](https://help.sonatype.com/en/integration-of-iq-webhook-with-fortify-ssc-sync-service.html)

  * [GitHub Actions](https://help.sonatype.com/en/sonatype-github-actions.html)
    * [Reachability Analysis with Sonatype for GitHub Actions](https://help.sonatype.com/en/reachability-analysis-with-sonatype-for-github-actions.html)

  * [GitLab CI](https://help.sonatype.com/en/sonatype-for-gitlab-ci.html)
    * [CI Components](https://help.sonatype.com/en/ci-components---sonatype-for-gitlab-ci.html)
    * [CI/CD Pipelines](https://help.sonatype.com/en/ci-cd-pipelines---sonatype-for-gitlab-ci.html)
    * [Reachability Analysis with Gitlab CI](https://help.sonatype.com/en/reachability-analysis-with-gitlab-ci.html)

  * [IDEA](https://help.sonatype.com/en/iq-for-idea.html)
  * [Jenkins - Lifecycle](https://help.sonatype.com/en/sonatype-platform-plugin-for-jenkins.html)
    * [Installation and Configuration - Sonatype Platform Plugin for Jenkins](https://help.sonatype.com/en/installation-and-configuration---sonatype-platform-plugin-for-jenkins.html)
    * [Reachability Analysis with Jenkins](https://help.sonatype.com/en/reachability-analysis-with-jenkins.html)

  * [Jenkins - Nexus Repository](https://help.sonatype.com/en/nexus-platform-plugin-for-jenkins.html)
  * [Jira Cloud](https://help.sonatype.com/en/sonatype-for-jira-cloud.html)
  * [Jira Data Center](https://help.sonatype.com/en/sonatype-for-jira-data-center.html)
  * [Maven - Lifecycle](https://help.sonatype.com/en/sonatype-clm-for-maven.html)
  * [Maven - Nexus Repository](https://help.sonatype.com/en/nexus-repository-maven-plugin.html)
  * [ServiceNow](https://help.sonatype.com/en/sonatype-for-servicenow.html)
  * [Visual Studio 2022](https://help.sonatype.com/en/sonatype-for-visual-studio-2022.html)
  * [VS Code](https://help.sonatype.com/en/sonatype-for-vs-code.html)
  * [Sonatype IQ CLI](https://help.sonatype.com/en/sonatype-iq-cli.html)
    * [Reachability Analysis with Sonatype CLI](https://help.sonatype.com/en/reachability-analysis-cli.html)
    * [Sonatype IQ CLI With Bundled JDK](https://help.sonatype.com/en/sonatype-iq-cli-with-bundled-jdk.html)
    * [Passing CLI parameters from a file](https://help.sonatype.com/en/passing-cli-parameters-from-a-file.html)
    * [Example Scan Result File](https://help.sonatype.com/en/example-scan-result-file.html)
    * [Using Automatic application creation with the CLI](https://help.sonatype.com/en/automatic-application-with-the-cli.html)
    * [Using the Sonatype CLI with a CI Server](https://help.sonatype.com/en/using-the-sonatype-cli-with-a-ci-server.html)
    * [CLI error messages](https://help.sonatype.com/en/cli-error-messages.html)

  * [Sonatype Container Deployment - Lifecycle](https://help.sonatype.com/en/container-deployments.html)
  * [Sonatype Container Deployment - Nexus Repository](https://help.sonatype.com/en/cloud-deployments.html)
  * [Sonatype for SCM](https://help.sonatype.com/en/sonatype-for-scm.html)
    * [Source Control Configuration](https://help.sonatype.com/en/source-control-configuration.html)
      * [SCM Features Technical Overview](https://help.sonatype.com/en/scm-features-technical-overview.html)
      * [GitHub SCM](https://help.sonatype.com/en/github-configuration.html)
      * [GitLab SCM](https://help.sonatype.com/en/gitlab-configuration.html)
      * [Bitbucket SCM](https://help.sonatype.com/en/bitbucket-configuration.html)
      * [Bitbucket Cloud SCM](https://help.sonatype.com/en/bitbucket-cloud-configuration.html)
      * [Azure DevOps SCM](https://help.sonatype.com/en/azure-devops-configuration.html)
      * [IQ Server Configuration](https://help.sonatype.com/en/iq-server-configuration.html)
      * [Sparse Checkout File Types](https://help.sonatype.com/en/sparse-checkout-file-types.html)

    * [Easy SCM Onboarding](https://help.sonatype.com/en/easy-scm-onboarding.html)
      * [Instant Risk Profile](https://help.sonatype.com/en/instant-risk-profile.html)
      * [Continuous Risk Profile](https://help.sonatype.com/en/continuous-risk-profile.html)

    * [Automated Source Control Feedback](https://help.sonatype.com/en/automated-source-control-feedback.html)
      * [Automated Commit Feedback](https://help.sonatype.com/en/automated-commit-feedback.html)
      * [Automated Pull Requests](https://help.sonatype.com/en/automated-pull-requests.html)
        * [Automated Pull Requests in Go](https://help.sonatype.com/en/automated-pull-requests-in-go.html)
        * [Automated Pull Requests in Maven](https://help.sonatype.com/en/automated-pull-requests-in-maven.html)
        * [Automated Pull Requests in npm](https://help.sonatype.com/en/automated-pull-requests-in-npm.html)
        * [Automated Pull Requests with Gradle](https://help.sonatype.com/en/automated-pull-requests-with-gradle.html)

      * [Automated PRs for InnerSource Components](https://help.sonatype.com/en/automated-prs-for-innersource.html)
      * [Pull Request Commenting](https://help.sonatype.com/en/pull-request-commenting.html)
      * [Golden PR for GitHub](https://help.sonatype.com/en/golden-pr-for-github.html)
      * [Golden PR for GitLab](https://help.sonatype.com/en/golden-pr-for-gitlab.html)
      * [Golden PR for Azure DevOps](https://help.sonatype.com/en/golden-pr-for-azure-devops.html)
      * [Golden PR for Bitbucket](https://help.sonatype.com/en/golden-pr-for-bitbucket.html)

    * [Policy Evaluation with Nexus IQ for SCM](https://help.sonatype.com/en/policy-evaluation-with-sonatype-for-scm.html)
    * [CI and CLI Integrations](https://help.sonatype.com/en/ci-and-cli-integrations.html)
    * [Bitbucket Code Insights](https://help.sonatype.com/en/bitbucket-code-insights.html)
    * [Policy Evaluation in Source Control Management](https://help.sonatype.com/en/policy-evaluation-in-source-control-management.html)

  * [Java Runtime Agent (Experimental)](https://help.sonatype.com/en/java-runtime-agent.html)
  * [Integrations Capability Matrix](https://help.sonatype.com/en/integrations-compatibility.html)

_print_

Toggle navigation

* [Prev](https://help.sonatype.com/en/nexus-repository-2025-release-notes.html)
* [Next](https://help.sonatype.com/en/sonatype-nexus-repository-3-86-0-release-notes.html)

* [Sonatype Help](https://help.sonatype.com/en/index-en.html)
* [Sonatype Nexus Repository](https://help.sonatype.com/en/sonatype-nexus-repository.html)
* [Product Information](https://help.sonatype.com/en/product-information.html)
* [Release Notes](https://help.sonatype.com/en/release-notes.html)
* [2025 Release Notes](https://help.sonatype.com/en/nexus-repository-2025-release-notes.html)
* Sonatype Nexus Repository 3.87.0 - 3.87.2 Release Notes

Sonatype Nexus Repository 3.87.0 - 3.87.2 Release Notes[](https://help.sonatype.com/en/sonatype-nexus-repository-3-87-0-release-notes.html)
===========================================================================================================================================

**_Execute Data Repair Plan_ Re-Enabled in 3.90.0**

In Sonatype Nexus Repository 3.90.0, the _Repair - Execute Data Repair Plan_ task is re-enabled by default. We previously disabled this task in 3.88.0 to prevent potential data loss while we addressed issues affecting the _Verify and Repair_ and _Data Repair Plan_ tasks.

You can now safely use the _Repair - Execute Data Repair Plan_ task to correct data inconsistencies between the database and blob store. Consider leveraging [Recovery Mode](https://help.sonatype.com/en/recovery-mode.html "Recovery Mode") to prevent any interfering background tasks.

**Known Issue in Sonatype Nexus Repository 3.87.0 - 3.87.2**

Sonatype is aware of an issue impacting Sonatype Nexus Repository 3.87.0 - 3.87.2 High Availability (HA) deployments that use group blob stores created using the REST API. After upgrading, the Blob Stores page can fail to load, and errors are logged during startup.

If you are using Nexus Repository in an HA configuration and have configured group blob stores via API, we recommend delaying your upgrade to 3.87.0 - 3.87.2 until a fix is available.

What's New and Noteworthy in 3.87.2?[](https://help.sonatype.com/en/sonatype-nexus-repository-3-87-0-release-notes.html)
------------------------------------------------------------------------------------------------------------------------

**Released January 15, 2026**

### _Repair - Execute Data Repair Plan_ Task Disabled[](https://help.sonatype.com/en/sonatype-nexus-repository-3-87-0-release-notes.html)

To prevent potential data loss caused by a known issue impacting Sonatype Nexus Repository 3.83.0 and later, this release disables the _Repair - Execute Data Repair Plan_ task by default.

Attempting to run this task will result in a failure and an error in the logs. The task remains visible in the UI, and any existing instances of this task will not be removed. However, execution is blocked by default.

While it is possible to manually re-enable this task by setting the`nexus.reconcile.task.enabled`property to`true`, it is important that you not do so until you are using a release that restores support.

We will announce when it is safe to re-enable this task in a future release note.

### Bug Fixes in 3.87.2[](https://help.sonatype.com/en/sonatype-nexus-repository-3-87-0-release-notes.html)

| Issue ID | Description |
| --- | --- |
| NEXUS-50152 | The blob attribute loading process no longer deletes properties files on transient I/O errors or unhandled exceptions. |

What's New and Noteworthy in 3.87.1?[](https://help.sonatype.com/en/sonatype-nexus-repository-3-87-0-release-notes.html)
------------------------------------------------------------------------------------------------------------------------

**Released December 8, 2025**

### Multiple Bug Fixes[](https://help.sonatype.com/en/sonatype-nexus-repository-3-87-0-release-notes.html)

This release contains multiple bug fixes impacting release 3.87.0:

| Issue ID | Description |
| --- | --- |
| NEXUS-49788 | Restored a missing Netty class dependency that was required for Azure client initialization. Sonatype Nexus Repository instances using Azure blob store now start as expected. |
| NEXUS-43821 | The Compact Blob Store task now gracefully handles 404 responses from Azure during deletion, allowing the task to continue when a blob is already missing instead of marking the task as failed. |

What’s New and Noteworthy in 3.87.0?[](https://help.sonatype.com/en/sonatype-nexus-repository-3-87-0-release-notes.html)
------------------------------------------------------------------------------------------------------------------------

**Released December 2, 2025**

### Java 21 Now Minimum Required Java Version[](https://help.sonatype.com/en/sonatype-nexus-repository-3-87-0-release-notes.html)

Java 21 is now the minimum required version for running Sonatype Nexus Repository. All official Docker images and installers have been updated to include Java 21 by default, ensuring compatibility with the latest platform improvements and long-term support standards.

**Change Impacting Non-AWS S3 Blob Stores**

Starting with Nexus Repository Manager 3.87.x, the AWS SDK used for S3 blob stores has been upgraded from **version 1.12.658** to **2.33.5** because the AWS SDK for Java 1.x reaches end of life on December 31, 2025.

This change impacts users of non-AWS S3–compliant blob stores. Customers using S3-compatible storage should review compatibility with AWS SDK for Java 2.x when upgrading.

For example, Dell S3-compatible storage is currently incompatible with the latest AWS SDK.

### Adjustments to Community Edition Usage Limits[](https://help.sonatype.com/en/sonatype-nexus-repository-3-87-0-release-notes.html)

To better align with our goals of supporting individual developers and small teams, Sonatype Nexus Repository Community Edition now supports up to 40,000 total components and 100,000 requests per day. These adjustments ensure consistent, reliable performance for intended use cases and help maintain Community Edition’s long-term sustainability.

When either threshold is exceeded, the addition of new components will pause until usage returns below both limits. This behavior helps safeguard performance and provides a clear signal that your development needs may benefit from the scalability and enterprise features offered in Sonatype Nexus Repository Pro.

Administrators can continue to monitor usage through the _Usage Center_. For details on interpreting usage and planning for growth, refer to the [Usage Center documentation](https://help.sonatype.com/en/usage-center.html "Usage Center").

### Repository Firewall Supports Release Integrity for NuGet[](https://help.sonatype.com/en/sonatype-nexus-repository-3-87-0-release-notes.html)

Repository Firewall now extends Release Integrity protection to NuGet components. This enhancement allows teams using NuGet to benefit from Sonatype’s analysis, which flags suspicious or malicious component behavior and automatically quarantines high-risk releases. By broadening ecosystem coverage, this update helps secure .NET development pipelines against emerging supply chain threats with minimal manual effort.

For full details, see the [Release Integrity help documentation](https://help.sonatype.com/en/release-integrity.html "Release Integrity").

### New Configuration API for Instance Configuration and Metadata Migration[](https://help.sonatype.com/en/sonatype-nexus-repository-3-87-0-release-notes.html)

A new Configuration API is now available to support configuration management and metadata migration between Nexus Repository instances. This API enables you to programmatically export and import repository configuration and retrieve or migrate asset metadata, making it easier to automate and streamline tasks such as environment setup, backup, and migration.

For details on available endpoints and usage examples, refer to the [Configuration API documentation](https://help.sonatype.com/en/configuration-api.html "Configuration API").

### Modernized Login Experience[](https://help.sonatype.com/en/sonatype-nexus-repository-3-87-0-release-notes.html)

This release introduces a redesigned login experience that delivers a consistent, modern interface that aligns with enterprise accessibility standards.

### OAuth2 Realm Now Enabled by Default with JWT[](https://help.sonatype.com/en/sonatype-nexus-repository-3-87-0-release-notes.html)

In Sonatype Nexus Repository Pro, the OAuth2 realm is now automatically enabled when `nexus.jwt.enabled` is set to `true`, either by default in high availability (HA) deployments or when manually configured in the `nexus.properties` file. This update ensures a smoother out-of-the-box experience for environments using token-based authentication and reduces the need for manual security realm configuration.

Bug Fixes in 3.87.0[](https://help.sonatype.com/en/sonatype-nexus-repository-3-87-0-release-notes.html)
-------------------------------------------------------------------------------------------------------

This release includes a wide range of stability, performance, and usability improvements across Sonatype Nexus Repository. For better scannability, we've broken our bug fix listings into categories:

### Repository and Format-Specific Fixes[](https://help.sonatype.com/en/sonatype-nexus-repository-3-87-0-release-notes.html)

| **Issue ID** | **Description** |
| --- | --- |
| NEXUS-49171 | APT repository metadata is now properly updated in both the source and target hosted repositories after performing a component move via the REST API. |
| NEXUS-48894 | Docker pull requests against repositories with Repository Firewall enabled no longer fail due to a missing base URL; the system now derives it from the inbound request instead of requiring manual configuration. |
| NEXUS-48777 | Docker login requests now succeed for users with access to at least one Docker repository, even when path-based routing is enabled. |
| NEXUS-48729 | Deleting an individual npm metadata asset from the _Browse_ page now correctly updates the UI without falsely indicating that the entire package directory has been removed. |
| NEXUS-48561 | The proprietary component synchronization process now excludes orphaned Maven components without assets, preventing unintended quarantining of valid open source components. |
| NEXUS-48463 | Routing rules now apply correctly to Huggingface proxy repositories. |
| NEXUS-48330 | Nexus Repository now correctly caches and reuses remote ETags for npm package root requests when PCCS is enabled. |
| NEXUS-48259 | Nexus Repository now consistently serves PyPI package metadata for proxy repositories protected by PCCS, regardless of whether the request URL includes a trailing slash. |
| NEXUS-48000 | APT hosted repositories now generate Filename fields in metadata without a leading slash. |
| NEXUS-47603 | Scoped npm packages in hosted repositories now appear with their full names (including the scope prefix) in search results. |
| NEXUS-47551 | Outbound requests for scoped npm packages now correctly encode slashes, ensuring compatibility with strict registries and restoring support for scoped package installs in environments that require encoded URLs. |
| NEXUS-47148 | Added validation for Composer package distribution types to prevent errors when processing certain upstream package metadata. |
| NEXUS-45796 | Tag association requests in Sonatype Nexus Repository no longer return 404 errors immediately after uploading a component. |
| NEXUS-42101 | Ensured that group-level maven-metadata.xml files are updated correctly when a version is deleted from a member repository. |
| NEXUS-36481 | Docker group repository searches now handle invalid responses from member proxy repositories more gracefully. |
| NEXUS-27439 | Anonymous access settings for Docker repositories in Sonatype Nexus Repository now correctly respect per-repository configurations, ensuring global anonymous permissions no longer override repository-level restrictions. |

### User Experience and Access Control[](https://help.sonatype.com/en/sonatype-nexus-repository-3-87-0-release-notes.html)

| Issue ID | Description |
| --- | --- |
| NEXUS-49753 | Repository permission checks now defer evaluation of content selectors using the path variable to the asset level, restoring search and tag operations that failed after upgrading to 3.86.0 - 3.86.2. |
| NEXUS-49653 | Authenticated users who navigate to the `/saml` endpoint are now automatically redirected to the application home page. |
| NEXUS-48888 | Search queries containing slashes (`/)` now correctly encode the character, preventing 404 errors. |
| NEXUS-48889 | Search queries using double quotes for exact matches now return correct results in High Availability (HA) Sonatype Nexus Repository deployments, aligning behavior with documented expectations. |
| NEXUS-48542 & NEXUS-48540 | New login experience properly handles deep links. Users who log in with a username and password are now correctly redirected to their intended destination after authentication. |
| NEXUS-48410 | The _Blob Stores_ UI now displays _Used Size_ instead of _Total Size_ to more accurately reflect current storage usage and reduce confusion for administrators. |
| NEXUS-47018 | Anonymous users with only `nx-search-read` and `nx-repository-view-*-*-browse` privileges can now successfully perform search operations as expected. |
| NEXUS-46707 | The licensing UI now displays a more accurate message when updating a license, clarifying that a restart is only required if installing a license for the first time. |
| NEXUS-44162 | The _Blob Store_ and _Repositories_ pages now display a "Calculating..." message while metrics are still being processed after a database migration. |
| NEXUS-43689 | Creating LDAP server connections via the Swagger UI now works as expected. |
| NEXUS-27044 | Enhanced LDAP logging to include full exception details and complete query information. |
| NEXUS-25658 | Users only need edit and read privileges for a specific repository to access the _Invalidate Cache_ button. |

### Blob Store and Storage Management[](https://help.sonatype.com/en/sonatype-nexus-repository-3-87-0-release-notes.html)

| Issue ID | Description |
| --- | --- |
| NEXUS-49200 | You can no longer accidentally create blob stores with invalid names via the API. |
| NEXUS-49091 | Cleanup policies now properly delete components when using the H2 database. |
| NEXUS-49031 | Corrupted or unreadable blob properties files are now automatically deleted across all supported blob stores, allowing recovery tasks to proceed and preventing component download failures. |
| NEXUS-48143 | Improved error handling in file and S3 blob stores now suppresses misleading warnings when simultaneous requests temporarily fail to update blob property files. |
| NEXUS-48087 | Repository deletions now complete successfully even when group cleanup operations encounter issues; affected groups are logged for review. |
| NEXUS-47545 | Failures during S3 blob store creation are now logged at the error level with full exception details, making it easier to diagnose issues without requiring debug-level logging. |

### Performance, High Availability, and Scalability[](https://help.sonatype.com/en/sonatype-nexus-repository-3-87-0-release-notes.html)

| Issue ID | Description |
| --- | --- |
| NEXUS-49043 | Improved performance of the _Users_ page by optimizing role mapping queries to prevent timeouts in environments with a large number of user roles. |
| NEXUS-49032 | Support zip generation no longer logs serialization errors or truncates logs when SAML is configured. |
| NEXUS-48160 | Task-specific log files are now preserved when deploying via Helm charts, improving troubleshooting by maintaining separate logs per task type while still supporting the combined _allTasks.log_ output for Kubernetes environments. |
| NEXUS-47926 | Improved the asset export task to gracefully handle missing blobs by skipping over them and logging warnings, allowing the export to complete successfully even if some blobs are unavailable. |
| NEXUS-47826 | Improved reliability of the rolling upgrade process by preventing timeouts during schema changes from leaving the system in a failed or partially upgraded state. |
| NEXUS-42345 | Added a global configuration option to control URL escaping behavior for proxy repositories. Details are included in the [Configuring the Runtime Environment help documentation](https://help.sonatype.com/en/configuring-the-runtime-environment.html "Configuring the Runtime Environment"). |
| NEXUS-40172 | The `nodeHeartbeatExport.json` file is now compressed as a ZIP archive, significantly reducing its size and making it easier to manage during support zip generation and HA troubleshooting. |
| NEXUS-21637 | Improved support zip generation to prevent duplicate file path errors. |

### Schema, API, and Configuration Improvements[](https://help.sonatype.com/en/sonatype-nexus-repository-3-87-0-release-notes.html)

| Issue ID | Description |
| --- | --- |
| NEXUS-49379 | Ensured the `default-features` value in Cargo manifests defaults to `true` and updated attribute names to align with Cargo documentation. |
| NEXUS-49154 | Refactored schema management to ensure all database changes are handled through Flyway migrations, preventing startup delays and outages caused by schema modifications under load. |
| NEXUS-49120 | Sonatype Nexus Repository no longer includes `commons-lang 2.x` as a dependency; all usage has been migrated to `commons-lang3`. |
| NEXUS-48505 | Corrected the Components API response to include the appropriate blob store name instead of returning `null`. |
| NEXUS-47905 | The archetype-catalog.xml file is now automatically updated after deploying new SNAPSHOT base versions of Maven archetypes, eliminating the need to manually delete the file to reflect recent changes. |
| NEXUS-36020 | REST API updates to Maven repositories now validate deployment policy values correctly. |
| NEXUS-25475 | Updated the REST API to accept `writePolicy` values regardless of letter casing, preventing repository misconfiguration and ensuring Docker pushes to group repositories work as expected. |

### Licensing and Audit[](https://help.sonatype.com/en/sonatype-nexus-repository-3-87-0-release-notes.html)

| Issue ID | Description |
| --- | --- |
| NEXUS-46449 | Tag association and disassociation with components are now recorded in the audit log. |

Coming Soon to Sonatype Nexus Repository[](https://help.sonatype.com/en/sonatype-nexus-repository-3-87-0-release-notes.html)
----------------------------------------------------------------------------------------------------------------------------

We’re excited to share that the following enhancements will be coming soon to Sonatype Nexus Repository:

### Nexus Repository Instance Migrator[](https://help.sonatype.com/en/sonatype-nexus-repository-3-87-0-release-notes.html)

Sonatype’s new Nexus Repository Instance Migrator supports both configuration and content migration through a powerful command-line interface. Designed to handle complex, large-scale migrations with reliability and flexibility, the Instance Migrator includes features like repository mapping, real-time asset polling, persistent state tracking, and detailed logging.

**Already using Nexus Repository Cloud?** The migrator is already available for customers with an active cloud tenant. Our team will work directly with you to guide the setup and migration process for your Cloud onboarding.

* [Sonatype Nexus Repository 3.87.0 - 3.87.2 Release Notes](https://help.sonatype.com/en/sonatype-nexus-repository-3-87-0-release-notes.html#sonatype-nexus-repository-3-87-0---3-87-2-release-notes)
* [What's New and Noteworthy in 3.87.2?](https://help.sonatype.com/en/sonatype-nexus-repository-3-87-0-release-notes.html#what-s-new-and-noteworthy-in-3-87-2-)
  * [Repair - Execute Data Repair Plan Task Disabled](https://help.sonatype.com/en/sonatype-nexus-repository-3-87-0-release-notes.html#repair---execute-data-repair-plan-task-disabled-504649)
  * [Bug Fixes in 3.87.2](https://help.sonatype.com/en/sonatype-nexus-repository-3-87-0-release-notes.html#bug-fixes-in-3-87-2)

* [What's New and Noteworthy in 3.87.1?](https://help.sonatype.com/en/sonatype-nexus-repository-3-87-0-release-notes.html#what-s-new-and-noteworthy-in-3-87-1-)
  * [Multiple Bug Fixes](https://help.sonatype.com/en/sonatype-nexus-repository-3-87-0-release-notes.html#multiple-bug-fixes-504649)

* [What’s New and Noteworthy in 3.87.0?](https://help.sonatype.com/en/sonatype-nexus-repository-3-87-0-release-notes.html#what-s-new-and-noteworthy-in-3-87-0-)
  * [Java 21 Now Minimum Required Java Version](https://help.sonatype.com/en/sonatype-nexus-repository-3-87-0-release-notes.html#java-21-now-minimum-required-java-version)
  * [Adjustments to Community Edition Usage Limits](https://help.sonatype.com/en/sonatype-nexus-repository-3-87-0-release-notes.html#adjustments-to-community-edition-usage-limits)
  * [Repository Firewall Supports Release Integrity for NuGet](https://help.sonatype.com/en/sonatype-nexus-repository-3-87-0-release-notes.html#repository-firewall-supports-release-integrity-for-nuget-504649)
  * [New Configuration API for Instance Configuration and Metadata Migration](https://help.sonatype.com/en/sonatype-nexus-repository-3-87-0-release-notes.html#new-configuration-api-for-instance-configuration-and-metadata-migration)
  * [Modernized Login Experience](https://help.sonatype.com/en/sonatype-nexus-repository-3-87-0-release-notes.html#modernized-login-experience)
  * [OAuth2 Realm Now Enabled by Default with JWT](https://help.sonatype.com/en/sonatype-nexus-repository-3-87-0-release-notes.html#oauth2-realm-now-enabled-by-default-with-jwt)

* [Bug Fixes in 3.87.0](https://help.sonatype.com/en/sonatype-nexus-repository-3-87-0-release-notes.html#bug-fixes-in-3-87-0)
  * [Repository and Format-Specific Fixes](https://help.sonatype.com/en/sonatype-nexus-repository-3-87-0-release-notes.html#repository-and-format-specific-fixes)
  * [User Experience and Access Control](https://help.sonatype.com/en/sonatype-nexus-repository-3-87-0-release-notes.html#user-experience-and-access-control)
  * [Blob Store and Storage Management](https://help.sonatype.com/en/sonatype-nexus-repository-3-87-0-release-notes.html#blob-store-and-storage-management)
  * [Performance, High Availability, and Scalability](https://help.sonatype.com/en/sonatype-nexus-repository-3-87-0-release-notes.html#performance--high-availability--and-scalability)
  * [Schema, API, and Configuration Improvements](https://help.sonatype.com/en/sonatype-nexus-repository-3-87-0-release-notes.html#schema--api--and-configuration-improvements)
  * [Licensing and Audit](https://help.sonatype.com/en/sonatype-nexus-repository-3-87-0-release-notes.html#licensing-and-audit)

* [Coming Soon to Sonatype Nexus Repository](https://help.sonatype.com/en/sonatype-nexus-repository-3-87-0-release-notes.html#coming-soon-to-sonatype-nexus-repository-504649)
  * [Nexus Repository Instance Migrator](https://help.sonatype.com/en/sonatype-nexus-repository-3-87-0-release-notes.html#nexus-repository-instance-migrator)

Search results
--------------

No results found

[Would you like to provide feedback? Just click here to suggest edits.](mailto:docs@sonatype.com?subject=Feedback%20for%20help%20topic%20%22Sonatype%20Nexus%20Repository%203.87.0%20-%203.87.2%20Release%20Notes%22&body=%0A%09%09%09%09%0A%09%09%09%09%0A%09%09%09%09_______________________%0A%09%09%09%09%0A%09%09%09Please%20add%20your%20feedback%20above%20for%20topic%20%22Sonatype%20Nexus%20Repository%203.87.0%20-%203.87.2%20Release%20Notes%22%20in%20the%20publication%20%22Sonatype%20Help%22.)

* [Prev](https://help.sonatype.com/en/nexus-repository-2025-release-notes.html)
* [Next](https://help.sonatype.com/en/sonatype-nexus-repository-3-86-0-release-notes.html)

 © 2026 Sonatype

Last modified: January 15, 2026

Publication date:

![Image 4](https://cdn.bizible.com/ipv?_biz_r=&_biz_h=-417244810&_biz_u=a64dd07f33714aacc9c9f2b6d36e9269&_biz_l=https%3A%2F%2Fhelp.sonatype.com%2Fen%2Fsonatype-nexus-repository-3-87-0-release-notes.html&_biz_t=1773252937382&_biz_i=Sonatype%20Nexus%20Repository%203.87.0%20-%203.87.2%20Release%20Notes&_biz_n=0&rnd=501189&cdn_o=a&_biz_z=1773252937383)![Image 5](https://cdn.bizibly.com/u?_biz_u=a64dd07f33714aacc9c9f2b6d36e9269&_biz_l=https%3A%2F%2Fhelp.sonatype.com%2Fen%2Fsonatype-nexus-repository-3-87-0-release-notes.html&_biz_t=1773252937384&_biz_i=Sonatype%20Nexus%20Repository%203.87.0%20-%203.87.2%20Release%20Notes&rnd=32479&cdn_o=a&_biz_z=1773252937384)
