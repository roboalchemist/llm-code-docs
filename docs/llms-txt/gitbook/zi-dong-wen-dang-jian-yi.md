# Source: https://gitbook.com/docs/documentation/zh/gitbook-agent/zi-dong-wen-dang-jian-yi.md

# 自动文档建议

{% hint style="info" %}

#### 此功能目前处于早期访问阶段

前往 **组织设置 → GitBook Agent** 以请求访问。
{% endhint %}

GitBook Agent 可以 [连接到相同的信号](https://gitbook.com/docs/documentation/zh/gitbook-agent/zi-dong-wen-dang-jian-yi/lian-jie-shu-ju-yuan) 你的团队用来了解产品和用户需求的：支持对话、Slack 线程、GitHub issue 等。

有了这些上下文，Agent 可以主动识别空白、提出更新并自动生成文档更改。&#x20;

GitBook Agent 基于你组织的内容进行训练，这意味着它了解你团队的写作风格、结构和语气。你还可以 [添加自定义指令](#add-custom-instructions) 供 Agent 遵循 — 更多说明见下文。

{% stepper %}
{% step %}

### 连接一个来源

要允许 GitBook Agent 建议自动文档改进，你首先需要 [连接一个来源](https://gitbook.com/docs/documentation/zh/gitbook-agent/zi-dong-wen-dang-jian-yi/lian-jie-shu-ju-yuan).&#x20;

连接一个或多个来源后，Agent 将在后台开始收集并分析你的数据。
{% endstep %}

{% step %}

### 探索 GitBook Agent 如何分析你的数据

连接来源后，GitBook Agent 会将该上下文信息分类为对话、问题和主题。

它将这些信息结合起来，建议对文档的自动改进，并以变更请求的形式打开。

要查看 GitBook Agent 分析的数据，请进入你组织的设置，然后打开 [**数据浏览器** 选项卡](https://gitbook.com/docs/documentation/zh/gitbook-agent/zi-dong-wen-dang-jian-yi/tan-suo-nin-de-shu-ju) 在 **GitBook Agent** 部分。
{% endstep %}

{% step %}

### 查看 GitBook Agent 提出的变更请求

随着更多数据的流入，GitBook Agent 将获得足够的上下文来开始提出建议——通过在相关空间打开新的 [变更请求](https://gitbook.com/docs/documentation/zh/collaboration/change-requests) 。

你可以像处理其他变更请求一样编辑由 GitBook Agent 打开的变更请求——团队中的任何人只要拥有相应的 [权限](https://gitbook.com/docs/documentation/zh/zhang-hu-guan-li/member-management/permissions-and-inheritance).&#x20;

你也可以 [向 GitBook Agent 请求审查](https://gitbook.com/docs/documentation/zh/gitbook-agent/yu-gitbook-agent-yi-qi-shen-yue-bian-geng-qing-qiu) 以让它分析它所建议的更改。
{% endstep %}

{% step %}

### 与 GitBook Agent 协作处理更改

GitBook Agent 也可以充当写作伙伴，允许你在变更请求中计划、撰写、重写或更新任何内容。

在 [变更请求界面](https://gitbook.com/docs/documentation/zh/collaboration/change-requests/bian-geng-qing-qiu-jie-mian), 打开 GitBook Agent 将允许你直接与其聊天，以在你正在处理的变更请求的上下文中进行更改。&#x20;

你还可以添加 [评论](https://gitbook.com/docs/documentation/zh/collaboration/comments) 到特定块，并标记 @gitbook 以请求 GitBook Agent 进行更改。
{% endstep %}
{% endstepper %}

### 为 GitBook Agent 添加或移除可修改的已发布站点

默认情况下，GitBook Agent 将能够在你任何已发布的文档站点中创建变更请求。在 GitBook Agent 的设置界面，你可以选择希望 Agent 提出建议更改的站点。

### 为 GitBook Agent 添加自定义指令

要 [为 GitBook Agent 添加自定义指令](https://gitbook.com/docs/documentation/zh/shen-me-shi-gitbook-agent#add-a-style-guide-and-custom-instructions) 以供其遵循，请打开你组织的设置并在侧栏中选择 **GitBook Agent** 页面。

在此处你可以编写自定义指令，Agent 在为你的文档站点准备、分析和生成变更请求时将始终使用这些指令。
