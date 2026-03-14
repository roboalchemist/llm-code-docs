# Source: https://docs.gitguardian.com/platform/getting-started/first-incident.md

# Investigate and remediate your first open incident

> Step-by-step guide to investigating and remediating your first secret incident in the GitGuardian dashboard.

## What is a secret incident? What are its implications?

Secret incidents are open issues that need your attention to be resolved. They are created by [our secrets detection engine](../../secrets-detection/home) that continuously scans your monitored repositories for hardcoded secrets and displays them in your GitGuardian dashboard.

Leaving a secret in plain text in source control represents a threat for the security of the resources that are protected by that secret. To learn more about why hardcoded secrets are a vulnerability that needs your Application or Product Security teams' attention, read the related paragraph in our [Core Concepts](../../secrets-detection/core-concepts/what-is-a-secret) section of Secrets Detection.

## What are the occurrences of an incident?

The **same secret can be seen multiple times** in your VCS. They are referred to as occurrences.
GitGuardian streamlines the remediation process by automatically **grouping multiple occurrences of the same secret into a single secret incident**.

Thus, an occurrence of a secret incident is uniquely identified by the combination of the following parameters:
 - the source (for instance: a GitHub repository or a GitLab project) impacted by the secret occurrence,
 - the commit in which we detected the secret occurrence,
 - the commit file containing the secret occurrence,
 - the line within the commit file where the secret occurred.

Alerts are sent only when a new incident is created or reopened because of a regression. A new occurrence attached to an already-existing open secret incident won't raise any alerts.

> GitGuardian sets a maximum limit of 1,000 occurrences for a single secret incident (this does not apply to the self-hosted platform).

## What are the critical steps to remediating a compromised secret?

The **most important step is to revoke the secret**.
Once a secret is exposed, it should be considered compromised and potentially exploited by attackers.
But to prevent operational disruption, always assess the impact of a revocation first. 

GitGuardian provides you with a lot of context and insights to [assess the impact of the exposure](../../internal-monitoring/remediate/investigate-incidents), but more importantly, [measure the impact of the revocation](/nhi-governance/discover-your-nhis#exploration-map), thanks to the identification of the workloads using these credentials.

### Recommended remediation workflow:

1. **Secure storage:** Store the secret properly in a secret manager or secure vault. 
2. **Update code:** Fix your application code to retrieve the secret from the secure storage location.
3. **Test and deploy:** Perform non-regression testing, deploy to production, and monitor that your application works as expected.
4. **Rotate and revoke:** Generate new credentials, update them in your secret manager, and revoke/deactivate the compromised secret to ensure no attacker can access the involved service.
5. **Check for unauthorized access:** Review logs to see if the secret was used maliciously, and proceed with mitigation process in case a breach is confirmed.  

This approach ensures your systems remain operational throughout the remediation process while implementing secure secret management practices.

### Detailed remediation guides:

Choose the guide that matches your situation:

- **For internal incidents** (secrets in your monitored repositories): [Remediation scenarios](../../internal-monitoring/remediate/remediation-scenarios/overview.md)
- **For public incidents** (secrets found on public GitHub): [Remediate public incidents](../../public-monitoring/remediate/remediate-incidents.md)
- **For public GitHub leaks** (comprehensive step-by-step guide): [Public GitHub leak remediation](../../secrets-detection/secrets-detection-engine/leaks_remediation.mdx)

## What if I don't have all the information I need?

### Getting more context:
- **Involve the developer** who committed the secret - they have the most knowledge about what the secret accesses
- **Check the detector documentation** - Each secret type has specific revocation instructions
- **Use the incident timeline** - Review all related commits and files
- **Follow the investigation process** - Use our [incident investigation guide](../../internal-monitoring/remediate/investigate-incidents.md) for thorough analysis

### Need help with the remediation process?
- **Contact your security team** if you don't have permission to revoke the secret
- **Use GitGuardian's sharing features** to collaborate with the right stakeholders
- **Check our [detector documentation](../../secrets-detection/secrets-detection-engine/detectors/supported_credentials.md)** for specific guidance on revoking different types of secrets

### Prevention for the future:

Now that you've handled your first incident, consider implementing these preventive measures to catch secrets before they enter your repositories:

- **Install [GitGuardian CLI (ggshield)](../../ggshield-docs/getting-started.md)** - Scan for secrets locally and in CI/CD pipelines before code is committed
- **Set up [pre-commit hooks](../../ggshield-docs/integrations/git-hooks/pre-commit.md)** - Automatically prevent secrets from being committed to your repositories
- **Adopt [secure secrets management practices](https://blog.gitguardian.com/secrets-api-management/)** - Use proper secret management solutions instead of hardcoding credentials.
