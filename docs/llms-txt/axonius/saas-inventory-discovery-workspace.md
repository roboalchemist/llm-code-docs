# Source: https://docs.axonius.com/docs/saas-inventory-discovery-workspace.md

# SaaS Inventory Discovery Workspace

The **SaaS Inventory Discovery** workspace helps you gain full visibility into your organization's SaaS inventory. Use this workspace to identify managed versus unmanaged applications, onboard or block Shadow SaaS, and manage SaaS-to-SaaS extensions. The goal is to ensure comprehensive oversight of all SaaS assets, providing a centralized view to help you understand what applications are in use, who is using them, and the associated risks.

<Callout icon="📘" theme="info">
  Note

  See  **[Workspaces](/docs/workspaces)** to learn how to generally access, navigate, and use workspaces.
</Callout>

## &#x20;Products Required for this Workspace

To access and use this workspace, you must have access to **[Axonius SaaS Applications](/docs/saas-applications-overview)**.

## Adapters Required for this Workspace

To populate the SaaS Inventory workspace with data, connect adapters from each of the following categories. The Axonius adapters employ various methods to discover all existing SaaS applications within your organization, ensuring your SaaS inventory is comprehensive and up-to-date.

* **SSO providers** - Provide SSO Managed SaaS Applications. Includes basic activities, such as the last SSO access time. This is key for identifying your officially sanctioned and managed SaaS applications and understanding who has access to those. Common SSO provider adapters include: [Okta](https://docs.axonius.com/axonius-help-docs/docs/okta), [PingFederate](https://docs.axonius.com/axonius-help-docs/docs/pingfederate), [Google Workspace (G Suite)](https://docs.axonius.com/axonius-help-docs/docs/g-suite-by-google), and [Microsoft Entra ID (Azure AD)](https://docs.axonius.com/axonius-help-docs/docs/microsoft-azure-active-directory-ad).
* **Identity providers** - Provide managed and unmanaged extensions with permissions and user data. These adapters are essential for discovering user identities, group memberships, application permissions, and applications that users have authorized themselves (*user-consent applications*).  Common identity provider adapters include [Google Workspace (G Suite)](https://docs.axonius.com/axonius-help-docs/docs/g-suite-by-google) and [Microsoft Entra ID (Azure AD)](https://docs.axonius.com/axonius-help-docs/docs/microsoft-azure-active-directory-ad).
* **DNS tools** - Provide browsing activity to SaaS Applications. These adapters are crucial for uncovering *Shadow IT* by showing which SaaS application websites your users are accessing, even if those applications aren't in your SSO.  Common DNS provider adapters include:  [Zscaler Web Security](https://docs.axonius.com/axonius-help-docs/docs/zscaler-web-security), [Netskope](https://docs.axonius.com/axonius-help-docs/docs/netskope), [Cisco Meraki](https://docs.axonius.com/axonius-help-docs/docs/cisco-meraki), [Cisco Umbrella](https://docs.axonius.com/axonius-help-docs/docs/cisco-umbrella), and [Microsoft Cloud App Security](https://docs.axonius.com/axonius-help-docs/docs/ms-cloud-app-security).
* **Direct adapters (optional)** - These are API-based adapters that communicate directly with IT and security systems to pull asset data. Connecting adapters directly to Axonius provides detailed data on the SaaS Application itself, its users, groups and roles, and activity data, depending on the data exposed by the adapter’s public API. Common direct login adapters include: [Slack](https://docs.axonius.com/axonius-help-docs/docs/slack), [Salesforce](https://docs.axonius.com/axonius-help-docs/docs/salesforce), [Zoom](https://docs.axonius.com/axonius-help-docs/docs/zoom).
* **Endpoint Agents for Installed Software (optional)** - This category provides information about SaaS applications when an endpoint management tool or an agent finds a SaaS application. Installed software is crucial for discovering SaaS applications that are  installed on endpoints, enabling the identification of both managed and unmanaged (shadow IT) applications that users may be running locally. Common installed software adapters examples include: [Tanium Interact](https://docs.axonius.com/axonius-help-docs/docs/tanium-sq), [Ivanti Service Manager](https://docs.axonius.com/axonius-help-docs/docs/ivanti-service-manager), [ManageEngine Endpoint (Desktop) Central and Patch Manager Plus](https://docs.axonius.com/axonius-help-docs/docs/manageengine-desktop-central), [CrowdStrike Falcon](https://docs.axonius.com/axonius-help-docs/docs/crowdstrike-falcon), and [SentinelOne](https://docs.axonius.com/axonius-help-docs/docs/sentinelone).

## Workspace Assets and Modules

<Callout icon="📘" theme="info">
  Note

  Each workspace has its own use-case-focused navigation menu on the left. The assets and modules available from this menu depend upon your access configuration.
</Callout>

You can access the following assets directly from this workspace:

* **[SaaS Applications](https://docs.axonius.com/axonius-help-docs/docs/saas-applications)**
* **[Users](https://docs.axonius.com/axonius-help-docs/docs/users-page)**
* **[Application Extension](https://docs.axonius.com/axonius-help-docs/docs/application-extensions)**
* **[Application Extension Instances](/docs/application-extension-instances)**

The SaaS Inventory workspace displays a dashboard with charts and data visualizations that give you a quick overview of your SaaS environment. It provides immediate insights, allowing you to quickly spot trends and anomalies related to application management, risk, and user activity.

Click any chart in the workspace to open a separate page that provides further in-depth details and insights related to that chart.

## &#x20;Use Cases this Workspace Helps You Fulfill

The **SaaS Inventory Discovery** workspace is your essential starting point for controlling your entire cloud application portfolio. It helps security, IT, and risk teams transform chaos into controlled visibility through the following core use cases.

### Discovering all SaaS Applications to Achieve a Unified Inventory

**The Challenge:** When applications are adopted outside of standard procurement, IT and Security teams lose the ability to manage, secure, and account for the entire estate. This sprawl creates major blind spots that traditional tools cannot fix. Security and IT teams want to know how many SaaS Applications they have and how to discover them.

**Our Solution:** Axonius eliminates this complexity by automatically normalizing and unifying data from multiple sources (SSO providers, identity providers, DNS tools, or installed software on devices) to create one trusted, comprehensive inventory. You instantly achieve a single source of truth for every known and unmanaged application in your environment.

For example, the **All SaaS Applications** chart gives you the total, reconciled count of everything detected, while the **Number of SaaS Applications by Source** chart ensures you know which discovery method is working best, helping you close any coverage gaps and maintain continuous, full visibility.

### Identifying and Mitigating Shadow SaaS

**The Challenge:** Shadow IT and poorly governed applications introduce critical security risks, including data leakage and compliance violations. Security teams struggle to identify the highest-priority threats among hundreds of applications.

**Our Solution:** Axonius cuts through the noise by assigning a **risk score** and governance status to every application and integration, allowing you to prioritize enforcement actions instantly. You can clearly distinguish between **sanctioned, managed applications** (originating from your identity provider or SSO) and all **unsanctioned Shadow SaaS** (coming from user-consent extensions, installed software, or DNS activity). This critical classification immediately identifies security blind spots and compliance risks, such as dangerous **Shadow AI SaaS applications** that may expose corporate data.

The **High Risk Shadow SaaS** chart instantly lists applications that are both unmanaged and high-risk - your top priority list. Furthermore, the **Total Overly Permissive Unmanaged Integrations** chart highlights non-admin-controlled applications with dangerous permissions, like access to your users' email or files. This gives you the contextual data needed to block immediate data leakage threats or onboard the application for proper governance.

The workspace provides the necessary contextual data, such as associated users and [risk scores](/docs/application-risk-score), to prioritize and execute remediation steps, allowing you to efficiently mitigate risk by taking action to onboard the application for proper governance, block its further usage, or manage the unapproved asset.

<Image border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/SaaSApplications/Shadow_SaaS_High_Risk.png" />

### Discovering and Reviewing SaaS-to-SaaS Extensions

This workspace provides complete visibility into all SaaS-to-SaaS connections, including admin-managed extensions, user-initiated extensions, application add-ons and application keys. You can identify **shadow extensions** that are often created by non-administrators or user consent, and assess the risk by reviewing the specific access permissions they hold for your core SaaS applications.

This level of detail helps you identify which permissions are excessive and potentially risky, while also giving you full oversight of active or inactive integrations, the total count per application, and the number of integrations for each user.

This chart shows the SaaS application extension instances by type over time:

<Image border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/SaaSApplications/SaaS-to_SaaS_Extension_Instances.png" />

### Controlling User Access and Optimizing SaaS Licensing Spend

**The Challenge:** Managing user access, especially non-human access like API keys, is complex and often leads to expensive, unused licenses and unnecessary privilege creep.

**Our Solution:** Axonius provides granular control over both human and non-human identities connected to your SaaS estate. By correlating application access with actual user activity data, you can quickly optimize spend and enforce the principle of least privilege. The **Inactive Users** chart allows IT to reclaim expensive licenses from users who haven't logged into an affiliated application in 90 days, driving significant cost savings. Meanwhile, the **Admin Users** chart pinpoints every user with an elevated administrative role across all applications, ensuring you can audit privileged access regularly and reduce the attack surface.