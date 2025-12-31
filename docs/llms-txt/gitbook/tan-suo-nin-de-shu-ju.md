# Source: https://gitbook.com/docs/documentation/zh/gitbook-agent/zi-dong-wen-dang-jian-yi/tan-suo-nin-de-shu-ju.md

# 探索您的数据

一旦 GitBook Agent 开始摄取对话，它会将您的数据分类为三类：

1. **对话**：代理已从您的连接器索引的原始数据。
2. **问题**：在对话中识别出的单个问题。
3. **主题**：在共同主题上彼此关联的问题组。

所有三者都被 GitBook Agent 用来确定可能需要在文档中进行的改动类型以便改进。下面，您可以找到有关每一项如何工作的更多信息。

{% hint style="info" %}
GitBook Agent 会对数据进行分类并自动为您的文档提出主动建议。您不需要对这些数据做任何操作——它们仅供查看。
{% endhint %}

### 对话

对话是从您的 [连接器](https://gitbook.com/docs/documentation/zh/gitbook-agent/zi-dong-wen-dang-jian-yi/lian-jie-shu-ju-yuan)发送到 GitBook Agent 的原始数据。代理会对其进行分析并分配影响评分，该评分会添加到对话最初被摄取时的元数据中。

然后对话被拆分为问题，这些问题是在对话中发现的具体改进点。一个对话可能包含多个问题。

您可以通过打开以下内容来查看对话： **组织设置** > **GitBook Agent** > **数据浏览器** 并选择 **对话** 选项卡。

### 问题

问题是已在对话中识别出的独立数据点。GitBook Agent 会为它们分配影响评分，并将该评分添加到数据被摄取时的元数据中。&#x20;

您可以通过打开以下内容来查看问题： **组织设置** > **GitBook Agent** > **数据浏览器** 并选择 **问题** 选项卡。

点击 **检查** <picture><source srcset="broken-reference" media="(prefers-color-scheme: dark)"><img src="https://2111890564-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FHBSHfffDzLSBh8vIMDpr%2Finspect.svg?alt=media&#x26;token=66d56df6-aa54-4bd5-985e-83ea0cfed841" alt=""></picture> 按钮以阅读问题摘要，以及 GitBook Agent 对其的分析。

### 主题

主题是彼此相关的问题组。通过将问题分组，GitBook Agent 可以为您的团队创建有用的、以上下文为驱动的变更请求。

代理会为每个主题分配影响评分，并显示用于形成该主题的问题和对话数量。随着新的对话和问题被处理，它们会自动更新。

点击 **检查** <picture><source srcset="broken-reference" media="(prefers-color-scheme: dark)"><img src="https://2111890564-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FHBSHfffDzLSBh8vIMDpr%2Finspect.svg?alt=media&#x26;token=66d56df6-aa54-4bd5-985e-83ea0cfed841" alt=""></picture> 任何主题以查看用于形成该主题的问题，以及 GitBook Agent 在处理这些问题并创建该主题时的思路日志。

该检查器界面还显示 GitBook Agent 基于该主题创建的任何变更请求——已准备好 [供您和您的团队审阅](https://gitbook.com/docs/documentation/zh/collaboration/change-requests/bian-geng-qing-qiu-jie-mian).

{% hint style="info" %}

## 停用主题

如果某个主题没有价值，您可以在其检查器界面中将该主题切换为关闭。停用后，该主题将不再用于为您的文档创建变更请求。
{% endhint %}
