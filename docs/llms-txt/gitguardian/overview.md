# Source: https://docs.gitguardian.com/public-monitoring/perimeter/overview.md

# Source: https://docs.gitguardian.com/public-monitoring/explore/overview.md

# Source: https://docs.gitguardian.com/public-monitoring/detect-public-secret-incidents/overview.md

# Source: https://docs.gitguardian.com/platform/analytics/overview.md

# Source: https://docs.gitguardian.com/platform/agent/overview.md

# Source: https://docs.gitguardian.com/internal-monitoring/remediate/remediation-scenarios/overview.md

# Source: https://docs.gitguardian.com/internal-monitoring/prevent/overview.md

# Source: https://docs.gitguardian.com/internal-monitoring/integrate-sources/secrets-managers-integrations/overview.md

# Source: https://docs.gitguardian.com/internal-monitoring/integrate-sources/overview.md

# Source: https://docs.gitguardian.com/ggshield-docs/integrations/overview.md

# Overview

> Overview of all ggshield integration options including IDE extensions, CI/CD pipelines, git hooks, Docker image scanning, and other data sources.

GitGuardian specializes in detecting secrets within source code, yet we also plan to expand to monitoring other sources such as messaging systems, project management boards, wikis, etc.

### IDE plugins and extensions: real-time secret detection in your development environment

GitGuardian integrates with popular IDEs and code editors to provide real-time secret detection as you write code.

GitGuardian currently supports:
- [Antigravity](./ide-integrations/antigravity.md)
- [Cursor](./ide-integrations/cursor.md)
- [Visual Studio Code](./ide-integrations/vscode.md)
- [Windsurf](./ide-integrations/windsurf.md)

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/6RGoHXxwOLc?controls=0&loop=1" title="YouTube video player" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; fullscreen; encrypted-media; gyroscope; picture-in-picture; web-share; loop" allowFullScreen></iframe>

### CI/CD integrations: secrets detection in your CI/CD workflow.

GitGuardian integrates with the most common CI tools via our CLI application: [`ggshield`](../getting-started.md).

GitGuardian currently supports:
- [Azure pipelines](./cicd-integrations/azure-pipelines.md)
- [Bitbucket pipelines](./cicd-integrations/bitbucket-pipelines.md)
- [Circle CI](./cicd-integrations/circle-ci.md)
- [Drone CI](./cicd-integrations/drone-ci.md)
- [GitHub Actions](./cicd-integrations/github-actions.md)
- [GitLab pipelines](./cicd-integrations/gitlab-pipelines.md)
- [Jenkins CI](./cicd-integrations/jenkins-ci.md)
- [Travis CI](./cicd-integrations/travis-ci.md)

### Git hooks: prevent secrets from reaching your VCS.

GitGuardian's CLI application, [ggshield](../getting-started.md) enables you to integrate secrets detection in git workflow and shift left your security.

GitGuardian currently supports the following hooks:
- [pre-commit](./git-hooks/pre-commit.md)
- [pre-push](./git-hooks/pre-push.md)
- [pre-receive](./git-hooks/pre-receive.md)

### Docker

GitGuardian's CLI application, [ggshield](../getting-started.md) enables you to [scan Docker images](./docker/docker_image.md).

### Monitoring other sources

GitGuardian intends to progressively support more data sources for secrets scanning in the future. Since version
1.14.1, ggshield supports a new docset input format. Refer to the [corresponding documentation](./other-data-sources/other-data-sources.md) for more details.  

If GitGuardian does not yet support one of the sources you would like to monitor, you can build your own integration by leveraging our [public API for secrets detection](../../api-docs/introduction.md).

### Troubleshooting connectivity problems

In case you experience connectivity problems with your GitGuardian instance, please refer to this 
[section of GitGuardian internal monitoring documentation](../../internal-monitoring/integrate-sources/monitored-perimeter#troubleshooting-connectivity-problems).
