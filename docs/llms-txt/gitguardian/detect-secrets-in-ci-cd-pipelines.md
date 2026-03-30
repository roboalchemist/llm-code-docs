# Source: https://docs.gitguardian.com/internal-monitoring/prevent/detect-secrets-in-ci-cd-pipelines.md

# Detect secrets in CI pipelines

> Integrate ggshield into CI/CD pipelines to detect hardcoded secrets and raise developer awareness around credential leaks.

## Overview

For vulnerabilities that are only exploitable during runtime like buffer overflows, SQL injections, or cross-site scripting, application security testing in the CI pipelines often translates into considerably shorter fix times. In the case of hardcoded credentials, the situation is different. No gains are to be expected in terms of remediation when comparing incidents that surface here against those that are found through the VCS integration (as a matter of fact, incidents detected during CI scans are also raised in the GitGuardian dashboard, since the remote branches live in the centralized repository).

You should regard secrets that enter centralized remote repositories as compromised, no matter how they found their way inside. The remediation process needs to get triggered in full in such a case; you should revoke and rotate the credentials before re-running security checks again.

### Advantages

Automating security testing in the CI pipelines is a great strategy to quickly raise the awareness of both developer and DevOps engineering teams around the problem of hardcoded secrets.

### Integrate ggshield in CI workflows

1. [Create a service account](../../api-docs/service-accounts.md) for the GitGuardian API
2. Set up CI/CD Integrations with ggshield
   1. [Jenkins CI](../../ggshield-docs/integrations/cicd-integrations/jenkins-ci.md)
   2. [GitHub Actions](../../ggshield-docs/integrations/cicd-integrations/github-actions.md)
   3. [GitLab CI/CD](../../ggshield-docs/integrations/cicd-integrations/gitlab-pipelines.md)
   4. [Azure pipelines](../../ggshield-docs/integrations/cicd-integrations/azure-pipelines.md)
   5. [Bitbucket pipelines](../../ggshield-docs/integrations/cicd-integrations/bitbucket-pipelines.md)
   6. [Circle CI](../../ggshield-docs/integrations/cicd-integrations/circle-ci.md)
   7. [Drone CI](../../ggshield-docs/integrations/cicd-integrations/drone-ci.md)
   8. [Travis CI](../../ggshield-docs/integrations/cicd-integrations/travis-ci.md)
   9. [Scan Docker images](../../ggshield-docs/integrations/docker/docker_image.md) after the build job
