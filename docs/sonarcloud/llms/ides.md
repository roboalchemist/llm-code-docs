# Source: https://docs.sonarsource.com/sonarqube-for-vs-code/ai-capabilities/ides.md

# Source: https://docs.sonarsource.com/sonarqube-for-vs-code/getting-started/ides.md

# Supported IDEs

SonarQube for VS Code integrates with multiple IDEs built on the VS Code architecture and is designed to be easily installed and fully functional within these environments. This broad compatibility ensures that you can leverage SonarQube's code analysis tools while using your favorite IDE.

As a result, you can expect a consistent experience, with SonarQube's features like on-the-fly issue detection, quick fixes, rule customization, and connected mode working as intended, regardless of the specific VS Code-based IDE you’re using.

In addition, SonarQube's compatibility with VS Code forks extends to your integrated AI tools. SonarQube for VS Code is built to coexist with these AI features, so you can benefit from both intelligent code assistance and robust static analysis without conflicts.

### Installing a compatible IDE

| Supported IDE                                                                                             | Profile migration is available                                                                                                             |
| --------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| [VS Code](https://code.visualstudio.com/docs/setup/setup-overview)                                        | None required                                                                                                                              |
| [Cursor](https://docs.cursor.com/guides/migration/vscode)                                                 | ✅ Check our [#installation](https://docs.sonarsource.com/sonarqube-for-vs-code/ai-capabilities/ides/cursor#installation "mention") guide   |
| GitPod                                                                                                    | [Install your extension](https://www.gitpod.io/docs/classic/user/references/ides-and-editors/vscode-extensions#installing-an-extension)    |
| [Kiro](https://kiro.dev/docs/guides/migrating-from-vscode/)                                               | ✅ Check out our [#installation](https://docs.sonarsource.com/sonarqube-for-vs-code/ai-capabilities/ides/kiro#installation "mention") guide |
| [Trae](https://docs.trae.ai/ide/manage-extensions)                                                        | [Manage your extension](https://docs.trae.ai/ide/manage-extensions)                                                                        |
| [VSCodium](https://github.com/VSCodium/vscodium/blob/master/docs/migration.md)                            | ✅                                                                                                                                          |
| [Windsurf](https://docs.windsurf.com/windsurf/getting-started#forgot-to-import-vs-code-configurations%3F) | ✅ Check our [#installation](https://docs.sonarsource.com/sonarqube-for-vs-code/ai-capabilities/ides/windsurf#installation "mention") guide |

{% hint style="info" %}
Note that although your supported IDE has migrated your extension, your SonarQube token is in secure storage and will not be migrated; you will be prompted to reauthenticate your connection.
{% endhint %}

When using Visual Studio Code and GitHub Codespaces, SonarQube for VS Code is available directly from the [VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=SonarSource.sonarlint-vscode).

### IDE-specific features

SonarQube features and workflows may differ for each supported IDE. Please see these dedicated pages as for more information as it becomes available:

{% columns %}
{% column %}
{% content-ref url="../ai-capabilities/ides/cursor" %}
[cursor](https://docs.sonarsource.com/sonarqube-for-vs-code/ai-capabilities/ides/cursor)
{% endcontent-ref %}

{% content-ref url="../ai-capabilities/ides/kiro" %}
[kiro](https://docs.sonarsource.com/sonarqube-for-vs-code/ai-capabilities/ides/kiro)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
{% content-ref url="../ai-capabilities/ides/windsurf" %}
[windsurf](https://docs.sonarsource.com/sonarqube-for-vs-code/ai-capabilities/ides/windsurf)
{% endcontent-ref %}
{% endcolumn %}
{% endcolumns %}
