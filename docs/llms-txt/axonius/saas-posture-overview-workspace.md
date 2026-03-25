# Source: https://docs.axonius.com/docs/saas-posture-overview-workspace.md

# SaaS Posture Overview Workspace

Gain continuous oversight of your critical SaaS applications' security posture with the SaaS Posture Overview workspace. Identify misconfigurations, monitor drift, and ensure compliance with regulatory frameworks. The **SaaS Posture Overview** workspace enables you to identify and remediate application misconfigurations by tracking settings against security baselines (such as MFA, encryption, and password strength).

This workspace also enables you to monitor unauthorized configuration changes (drift) and audit compliance against regulatory frameworks. The workspace provides a centralized, risk-based view that allows you to continuously enforce best practices and protect sensitive data within your critical business applications.

<Callout icon="📘" theme="info">
  Note

  See  **[Workspaces](/docs/workspaces)** to learn how to generally access, navigate, and use workspaces.
</Callout>

## &#x20;Products Required for this Workspace

To access and use this workspace, you must have access to **[Axonius SaaS Applications](/docs/saas-applications-overview)**.

## Adapters Recommended for this Workspace

Axonius collects SaaS application settings from adapters such as [Microsoft Entra ID](/docs/microsoft-azure-active-directory-ad#/), [Google Workspace](/docs/g-suite-by-google#/), [Salesforce](/docs/salesforce), and many others. This is achieved by directly connecting to your critical SaaS platforms and providing deeper insights into their specific configurations and security settings.

## Workspace Assets and Modules

<Callout icon="📘" theme="info">
  Note

  Each workspace has its own use-case-focused navigation menu on the left. The assets and modules available from this menu depend upon your access configuration.
</Callout>

You can access the following assets directly from this workspace:

* **[Application Settings](/docs/application-settings#/)**
* **[SaaS Applications](https://docs.axonius.com/axonius-help-docs/docs/saas-applications)**
* **[Users](https://docs.axonius.com/axonius-help-docs/docs/users-page)**

<Callout icon="📘" theme="info">
  Note

  Click any chart in the workspace to open a separate page that provides further in-depth details and insights related to that chart.
</Callout>

## Use Cases this Workspace Helps You Fulfill

The SaaS Posture Overview workspace displays dashboards that give you a continuous, risk-based view of the security configuration of your managed SaaS applications. It provides immediate insights into configuration status, security gaps, and compliance health. Key data includes high-level metrics and security health scores to summarize the overall posture, as well as detailed, risk-prioritized views of failing security controls and configuration gaps for targeted remediation planning.

This workspace provides data and visualizations that help you address critical security use cases related to your SaaS applications.

### Finding and Remediating Application Misconfigurations

**The Challenge:** Security teams are overwhelmed by misconfiguration alerts across dozens of SaaS applications. It's difficult to know which issues pose the highest threat and where to focus immediate remediation efforts.

**Our Solution:** Axonius solves this by enabling you to continuously identify security configuration gaps by assessing application settings against established security baselines and best practices. You can specifically identify misconfigurations in crucial areas, such as Multi-factor authentication (MFA) enforcement, Robust password policies, Data encryption (both at rest and in transit), Secure session timeouts, and more. This depends on the connected adapters, their configurations, and the data they retrieve.

This workspace provides the data required to efficiently identify and remediate these configuration errors, directly improving the overall security posture of your managed SaaS applications. We automatically categorize misconfigurations by their assigned risk impact (High, Medium, Low), allowing your team to immediately focus on the most critical exposures.

The **High Impact Misconfigurations** chart instantly isolates the most severe security gaps that require urgent action, while the **Misconfigurations by Impact Score** chart visualizes the overall risk distribution to ensure high-impact items are consistently shrinking, driving continuous security improvement.

### Monitoring Configuration Drift and Tracking Posture Hygiene

**The Challenge:** Changes to security settings - whether unauthorized or accidental - introduce new risk and erode security posture over time. It's nearly impossible to manually monitor every critical configuration for deviation.

**Our Solution:** We provide trend-based intelligence that measures your security hygiene and demonstrates the effectiveness of your team's remediation work. This helps teams to immediately identify configuration drifts over time, which are unauthorized or accidental changes to established security settings.

The **Properly Configured Settings vs. Misconfigurations Over Time** chart clearly illustrates your security trend line, allowing you to see if your efforts are resulting in a measurable increase in compliant settings.

In addition, the **Total High or Medium Impact Misconfigurations Over Time** chart monitors how quickly your team is eliminating the most serious drift.

By flagging these deviations, the workspace ensures you can quickly address changes that could introduce new risks, security vulnerabilities, or non-compliance into your managed environment.

This chart demonstrates a breakdown of configured vs misconfigured SaaS applications over time:

<Image border={false} src="https://github.com/Axonius/ax-docs-pub/blob/main/img/SaaSApplications/SaaS_Configured_vs_Misconfigured.png?raw=true" />

### Map Configurations Against Key Compliance Frameworks

**The Challenge:** Maintaining compliance with stringent industry frameworks (such as HIPAA, SOC-2, or NIST) across a large, dynamic SaaS portfolio is a manual, intensive, and error-prone process. A single misconfiguration can lead to failed audits or regulatory fines.

**Our Solution:** This workspace helps you maintain continuous compliance by tracking your SaaS application configurations against key regulatory frameworks and industry standards (for example: **SOC2, ISO 27001, PCI DSS, HIPAA, GDPR**). Its function is to verify that application settings meet regulatory requirements, enabling you to efficiently prepare for compliance audits and easily demonstrate adherence to mandated security controls.

The **Misconfigurations by Compliance Framework** chart quickly identifies which frameworks are currently being violated. The **High-Impact Misconfigured Settings Impacting Key Compliance Frameworks** table provides an actionable list of the most critical settings that must be corrected to achieve or maintain regulatory adherence.

This chart shows SaaS application misconfigurations by compliance:

<Image align="center" border={false} width="600px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/SaaSApplications/Misconfigurations_by_Compliance.png" />