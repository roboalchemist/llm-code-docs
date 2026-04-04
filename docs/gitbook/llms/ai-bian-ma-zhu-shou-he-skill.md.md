# Source: https://gitbook.com/docs/documentation/zh/creating-content/ai-bian-ma-zhu-shou-he-skill.md.md

# AI 编码助手和 skill.md

GitBook 提供了一个 [skill.md](https://gitbook.com/docs/skill.md) 文件，教会 AI 编码助手如何正确编辑 GitBook 文档。在本地编辑 GitBook 文档时，将其作为“项目规则”使用。此做法非常适合 [Git 同步 ](https://gitbook.com/docs/documentation/zh/getting-started/git-sync)工作流，你可以在本地编辑文档并提交更改以更新文档站点。该参考文件涵盖了 GitBook 的 Markdown 扩展、自定义区块、配置文件和最佳实践。

{% hint style="info" %}
GitBook 还提供了 [GitBook Agent](https://gitbook.com/docs/documentation/zh/gitbook-dai-li-agent) 可在编辑器中直接进行 AI 辅助文档编写。本指南适用于更喜欢使用外部编码助手（如 Claude Code 或 Cursor）的团队。
{% endhint %}

### skill.md 文件包含的内容

* 所有自定义区块的完整语法参考
* 配置文件格式（`.gitbook.yaml`, `SUMMARY.md`, `.gitbook/vars.yaml`)
* Frontmatter 选项和布局控制
* 变量与表达式语法
* 用于选择正确区块类型的决策表
* 常见陷阱与最佳实践

将此文件添加到你的 AI 编码助手中可提供有关为 GitBook 文档创建、编辑和格式化内容所需的信息。这意味着助手会遵循已建立的框架和 GitBook 功能的最佳实践。

### 通过 URL 使用 skill.md

大多数 AI 编码助手支持特定于项目的说明。你可以在项目配置中引用 skill 文件的 URL，以便助手知道如何处理 GitBook 语法。

### 在本地使用 skill.md

你也可以下载 skill 文件并将其包含在你的仓库中。首先，将 skill.md 下载到仓库根目录，然后在你的编码助手的规则文件中引用它： `"在仓库根目录读取 skill.md 以获取 GitBook 语法和最佳实践"` .&#x20;

此方法可离线工作，并允许进行团队特定的修改。&#x20;

{% hint style="warning" %}
请记得在 GitBook 添加新功能时，用最新的 skill.md 更新你的本地仓库。
{% endhint %}

### 测试 AI 生成的内容

始终审查并测试 AI 助手生成的内容非常重要——既要检查技术准确性，也要检查格式是否正确。&#x20;

在使用以 skill 文件为训练依据的 AI 助手时，你应当：

* 验证任何自定义区块在 GitBook 中是否正确渲染
* 检查所有内部链接是否可用
* 确认 frontmatter 是有效的 YAML
* 测试变量是否引用了正确的作用域

{% hint style="warning" %}
**注意：** AI 助手有时可能生成不正确的语法或忘记关闭自定义区块。提交前务必审查更改。
{% endhint %}

### GitBook Agent

更倾向于直接在 GitBook 中工作？ [GitBook Agent](https://gitbook.com/docs/documentation/zh/gitbook-dai-li-agent/what-is-gitbook-agent) 在 GitBook 编辑器中为你提供了 AI 辅助的工作流——无论你是否使用 Git 同步。

Agent 拥有文档的完整上下文，并且已经接受了如何以最佳方式使用 GitBook 的区块和功能的训练。Agent 帮助你起草内容、进行更新，并在 GitBook 应用内为不同用例优化文档。

<a href="../gitbook-dai-li-agent" class="button primary">了解 GitBook Agent</a>
