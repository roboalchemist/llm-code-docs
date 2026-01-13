# Extensions

Source: https://semgrep.dev/docs/extensions/overview

- [](/docs/)- [Scan](/docs/getting-started/quickstart)- Set up and deploy scans- Extensions**On this pageExtensions
Several third-party tools include Semgrep extensions.

## Official IDE extensions[​](#official-ide-extensions)
NameMarketplace linkDocumentationMicrosoft Visual Studio Code[** `semgrep-vscode`](https://marketplace.visualstudio.com/items?itemName=semgrep.semgrep)[Semgrep VS Code extension](/docs/extensions/semgrep-vs-code)IntelliJ Ultimate Ideaand many other IntelliJ products[** `semgrep-intellij`](https://plugins.jetbrains.com/plugin/22622-semgrep)[Semgrep IntelliJ extension](/docs/extensions/semgrep-intellij)Emacs[** `lsp-mode`](https://github.com/emacs-lsp/lsp-mode)See repository README
## Use of Language Server Protocol (LSP)[​](#use-of-language-server-protocol-lsp)
All of the official IDE extensions use the [Language Server Protocol](https://microsoft.github.io/language-server-protocol/) to communicate with Semgrep. This allows the team to focus on one codebase that can be shared across most modern editor platforms.

## `pre-commit`[​](#pre-commit)
Prevent secrets or security issues from entering your Git source control history by running Semgrep as a [** pre-commit](https://pre-commit.com/) hook. See [`pre-commit` documentation](/docs/extensions/pre-commit) for details.

## Semgrep as an engine[​](#semgrep-as-an-engine)
Many other tools have capabilities powered by Semgrep.
Add yours [with a pull request](https://github.com/semgrep/semgrep-docs)!

- [DefectDojo](https://github.com/DefectDojo/django-DefectDojo/pull/2781)
- [Dracon](https://github.com/thought-machine/dracon)
- [GitLab SAST](https://docs.gitlab.com/ee/user/application_security/sast/#multi-project-support)
- [GuardDog](https://github.com/datadog/guarddog)
- [litbsast](https://github.com/ajinabraham/libsast)
- [mobsfscan](https://github.com/MobSF/mobsfscan)
- [nodejsscan](https://github.com/ajinabraham/nodejsscan)
- [SecObserve](https://github.com/SecObserve/SecObserve)
Not finding what you need in this doc? Ask questions in our [Community Slack group](https://go.semgrep.dev/slack), or see [Support](/docs/support/) for other ways to get help.

[Edit this page](https://github.com/semgrep/semgrep-docs/edit/main/docs/extensions/overview.md)Last updated on Nov 10, 2025**