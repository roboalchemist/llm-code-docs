# Source: https://docs.gitguardian.com/nhi-governance/track-your-performance.md

# Track your performance

> NHI Governance analytics dashboard covering posture management trends, secret hygiene metrics, and secrets incident tracking.

Your dashboard provides data-driven insights into how well your organization is managing its NHIs. This section is divided into three main areas: Posture Management, Secret Hygiene, and Secrets Incidents.

### Posture Management

![Posture Management](/img/nhi-governance/posture-management-analytics.png)

- **Breached Policies Over Time**: The first graph displays the evolution of breached policies over time. By tracking these trends, you can evaluate the effectiveness of your remediation efforts and overall security measures.
- **Distribution of Breached Policies**: The second graph shows the distribution of breached policies across your environment, highlighting which risk types occur most frequently. Clicking on any specific breach category will take you to an inventory view filtered by that policy, enabling you to quickly identify and address areas that require attention.

### Secret Hygiene

![Secret Hygiene](/img/nhi-governance/secret-hygiene-analytics.png)

- **Vault Coverage**: Monitor what percentage of your secrets are stored in designated secret managers. This metric reflects how consistently your organization is adopting secure storage practices.
- **Integration Overview**: Get a snapshot of your NHI integrations. This overview lets you assess whether all relevant systems communicate properly with NHI Governance, ensuring comprehensive coverage.
- **Secrets Age Distribution**: Review the age of your active secrets. Older secretsâespecially those nearing or exceeding the recommended lifespan may require rotation to reduce the risk of exposure.

![Secrets Age](/img/nhi-governance/secrets-age-analytics.png)

### Secrets Incidents

![Compromised Secrets](/img/nhi-governance/compromised-secrets-analytics.png)

- **Public Incidents**: These secrets are detected by GitGuardian in publicly accessible GitHub repositories, making them potentially visible to anyone, including malicious actors. These incidents can occur through direct commits to public repositories or when private repositories are accidentally made public. You need to have Public Monitoring to access this data.
- **Private Incidents**: These secrets are discovered through GitGuardian's internal monitoring of private code repositories, CI/CD pipelines, and developer productivity tools.
