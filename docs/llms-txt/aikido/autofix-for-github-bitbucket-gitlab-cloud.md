# Source: https://help.aikido.dev/aikido-autofix/configure/autofix-for-github-bitbucket-gitlab-cloud.md

# AutoFix for GitHub, Bitbucket and GitLab Cloud

Aikido AutoFix is a tool you can use to have Aikido fix vulnerabilities in 3rd party dependencies in your projects. It will do this by creating pull requests that remove the vulnerability via package updates or by other means. In some cases an Aikido Autofix can remove a whole class of vulnerabilities instead of just 1 issue.

### Supported Languages <a href="#supported-languages" id="supported-languages"></a>

Support for the auto-fixer at this time is limited to **Javascript** (Yarn, npm, pnpm)**, Java** (pom.xml)**, Go, PHP** (composer)**, Python, .NET** and **Ruby** repositories which are hosted on Github, Bitbucket, GitLab, [GitLab Self-Managed](https://aikido.outverse.com/doc/enable-aikido-autofix-for-gitlab-self-managed/docfdOyiUltZ) or [Azure DevOps](https://help.aikido.dev/aikido-autofix/configure/autofix-for-azure-devops).

### Setting Up Autofix <a href="#setting-up-autofix" id="setting-up-autofix"></a>

**Step 1. Enable Autofix on the** [**Autofix Settings**](https://app.aikido.dev/settings/integrations/autofix) **page or go to** [**Autofix Page**](https://app.aikido.dev/issues/fix) **and click on Enable Autofix.**

![Prompt to enable write access for Aikido to auto-patch vulnerabilities in version control.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-01e5b42c9e2e166681b752c59a8c4945626703ba%2Fautofix-for-github-bitbucket-gitlab-cloud_d1149bda-5055-45e6-afaf-a7b728bc33ef.png?alt=media)

**Step 2.** After installing the Aikido Autofix application, you can instruct Aikido to create these pull requests. This can either be done via the action menu in the **sub-issues table** in the sidebar or manage in bulk on the [Autofix page.](https://app.aikido.dev/issues/fix)\
​

![Issue management menu with options to fix, create task, snooze, ignore, or adjust severity.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-f400b5dbacd46b512b9ed5ab4a1a38113b9c4366%2Fautofix-for-github-bitbucket-gitlab-cloud_95ee20a4-3001-44f5-b66c-2e2c6beb9deb.png?alt=media)

We'll always explain beforehand what Aikido Autofix will be doing. In some cases, there are multiple ways we can fix an issue. In such a case you will be able to select the option you prefer.

![Dependency upgrade prompt for resolving a security issue with an auto pull request.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-a002bed96c2c1eb82d6dfb10a8944ba1591ca326%2Fautofix-for-github-bitbucket-gitlab-cloud_9ea84323-a443-43e6-af11-f2731479e179.png?alt=media)

When a fix is prepared, we'll present you with a modal with the commands we are running to install the requested fix. This way you'll be able to reproduce the creation of the pull request locally if needed. The modal can be closed while the process is still running.

![Overriding and updating vulnerable npm dependency in package.json.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-973b76e558cd80052e07a9866c89ddd1abdfdab6%2Fautofix-for-github-bitbucket-gitlab-cloud_d3828ae3-cb1d-4332-9ee6-47a44c74e150.png?alt=media)
