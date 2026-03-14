# Source: https://docs.gitguardian.com/honeytoken/deploy-honeytokens/troubleshoot-sources-deployment-jobs.md

# Troubleshoot sources for Deployment jobs

> Troubleshoot source selection issues in honeytoken deployment jobs, including eligibility criteria and VCS-specific requirements.

# Troubleshoot sources for Deployment jobs

Refer to this document if you cannot find or select your sources in the Honeytoken Deployment jobs.

## Understand eligibility criteria for source selection

### Monitored repositories and projects

In order to be used in deployment jobs, your source needs to be [monitored](../../internal-monitoring/integrate-sources/monitored-perimeter#source-status) by GitGuardian. Sources excluded from the monitored perimeter can, therefore, not be selected in deployment jobs.

### Active repositories and projects

If your repository or project is archived and thus read-only, it cannot be used by deployment jobs. Therefore, only active sources are available for selection.

### Non-public repositories and projects

Honeytokens should **not** be deployed on purpose in public locations. They would be immediately triggered for ânormalâ reasons as a result of being in the public space without it indicating a security incident. This is why we do not make them available when creating deployment jobs.

If, for any reason, you wish to deploy a honeytoken in a public location, you will need to do it manually.

## Troubleshooting for each VCS integration

### GitLab sources

Unless your GitLab project is public, it should be available for selection in Deployment jobs. If itâs not the case:

- Check [here](https://dashboard.gitguardian.com/settings/integrations/gitlab) that the project is successfully integrated and monitored by GitGuardian.

If you have checked the above and still encounter an issue, reach out to our [support team](mailto:support@gitguardian.com).

### GitHub.com sources

GitHub.com sources (non-public and monitored) can be targeted for Honeytoken Deployment jobs, on the condition that a GitHub app with write access is enabled for these sources.

Refer to our [GitHub integration guide](../../internal-monitoring/integrate-sources/vcs-integrations/github) for instructions on granting GitGuardian write access to your GitHub repositories.

### GitHub Enterprise Server sources

GitHub Enterprise Server sources (non-public) can be targeted for honeytokens Deployment jobs, on the condition that a GitHub app with write access is enabled for these sources.

Refer to our [GitHub Enterprise Server integration guide](../../internal-monitoring/integrate-sources/vcs-integrations/github-enterprise) for instructions on granting GitGuardian write access to your GitHub Enterprise Server repositories.

### Azure DevOps sources

Unfortunately, Azure DevOps integration is not supported for Honeytoken Deployment jobs at the moment.

Check our [roadmap](https://roadmap.gitguardian.com/tabs/1-under-consideration) and upvote for this feature if youâre interested.

In the meantime, you can check [our other solutions](../deploy-honeytokens/deployment-methods) to deploy honeytokens.

### Bitbucket sources

Unfortunately, Bitbucket integration is not supported for Honeytoken Deployment jobs at the moment.

Check our [roadmap](https://roadmap.gitguardian.com/tabs/1-under-consideration) and upvote this feature if youâre interested.

In the meantime, you can check [our other solutions](../deploy-honeytokens/deployment-methods) to deploy honeytokens.
