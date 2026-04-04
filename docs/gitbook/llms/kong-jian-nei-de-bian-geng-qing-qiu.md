# Source: https://gitbook.com/docs/documentation/zh/collaboration/change-requests/kong-jian-nei-de-bian-geng-qing-qiu.md

# 空间内的变更请求

当你在一个 [空间](https://gitbook.com/docs/documentation/zh/getting-started/concepts#space)时，你可以通过打开新的变更请求来进行更改，或浏览现有的变更请求以查看其他人在做什么。

### 创建变更请求

在禁用实时编辑的空间内，点击 **编辑** 按钮位于 [空间标题](https://gitbook.com/docs/documentation/zh/zi-yuan/gitbook-ui#space-header) 以开始新的变更请求。

这将打开一个新的变更请求，你可以根据需要编辑或删除内容。你的更改会自动保存，其他人也可以加入你的变更请求以实时协作。

创建变更请求时，你可以添加标题和描述，以提供有关你所做更改的更多上下文。

一旦你对更改满意，可以使用标题栏中的按钮来 [**请求审阅**](#request-a-review-on-a-change-request) 你的变更请求，或 [**合并**](#merging-a-change-request) 将其直接合并到主分支中。

#### 使用 GitBook Agent 创建变更请求

[GitBook 代理](https://gitbook.com/docs/documentation/zh/gitbook-agent/shen-me-shi-gitbook-agent) 是一个可以 [根据你提供的任何指示规划并实施变更请求](https://gitbook.com/docs/documentation/zh/gitbook-agent/write-and-edit-with-ai#implement-a-change-request-with-gitbook-agent) 的 AI 团队成员。

要使用 GitBook Agent 打开新的变更请求，请点击位于右上角“编辑”按钮旁的 GitBook Agent 图标，并让 GitBook 根据你想要的更改来实施操作。

你可以要求它做的一些事情包括：

* 添加使用示例
* 改善页面 SEO
* 提升清晰度
* 检查一致性
* 修正错别字和拼写错误
* 关联相关内容
* 更多+

前往 [使用 GitBook Agent 编写](https://gitbook.com/docs/documentation/zh/gitbook-agent/write-and-edit-with-ai) 以了解更多。

### 预览变更请求

你可以通过点击 **预览** 选项在 [空间标题](https://gitbook.com/docs/documentation/zh/zi-yuan/gitbook-ui#space-header)中预览你在变更请求中所做的更改。这将切换到包含建议更改的已发布文档预览，让你可以在完整的已发布文档上下文中查看更改。

在 **预览** 按钮下方是你站点预览的 URL。点击它，站点预览将在新标签页中完整打开。&#x20;

当你在新标签页打开预览 URL 时，你还会看到 [预览工具栏](https://gitbook.com/docs/documentation/zh/zi-yuan/gitbook-ui/toolbar-on-published-sites-and-site-previews) 位于浏览器窗口底部。该工具栏可以让你快速跳回 GitBook 以查看、编辑或评论变更请求，或打开站点的实时版本。

{% hint style="info" %}
你只能预览已添加到 [已发布文档站点](https://gitbook.com/docs/documentation/zh/publishing-documentation/publish-a-docs-site).
{% endhint %}

{% hint style="warning" %}
的空间的变更请求。如果你的内容是通过共享链接或需要身份验证的访问发布的，则不会显示预览功能。
{% endhint %}

### 在变更请求上请求审查

当你想在将更改合并到主分支之前请团队成员检查你的内容时，请对你的变更请求请求审查。

在空间标题栏中选择 **概览** 选项卡以打开你的变更请求概览——包括以差异视图显示的所有更改。

在这里你可以为变更请求添加描述以为审阅者提供一些上下文，并标记你希望检查你工作的特定人员。

当你点击 **请求审阅**时，变更请求的状态将更改为 **审核中**，任何你在审查请求中标记的人都会收到通知。

如果你的更改不需要审查、你拥有适当的 [权限](https://gitbook.com/docs/documentation/zh/zhang-hu-guan-li/member-management/roles)，并且你没有任何阻止的 [合并规则](https://gitbook.com/docs/documentation/zh/collaboration/merge-rules)，你可以直接将更改合并到主版本中。

{% hint style="info" %}
[将 GitBook Agent 添加为审阅者](https://gitbook.com/docs/documentation/zh/gitbook-agent/yu-gitbook-agent-yi-qi-shen-yue-bian-geng-qing-qiu) 到你的变更请求中，它可以检查你的内容以发现拼写、语法和风格指南错误，建议改进等。&#x20;
{% endhint %}

{% hint style="warning" %}
如果你在审查请求中没有标记任何人，所有具有审阅者权限的人都会收到你的请求通知。如果空间中没有审阅者，则会通知高于审阅者的下一个角色。
{% endhint %}

#### 差异视图 <a href="#diff-mode" id="diff-mode"></a>

当你打开空间标题中的 **更改** 选项卡时，差异视图将出现。差异视图会突出显示在变更请求中被编辑的每个页面和块。它会在目录中标记任何被编辑的页面，并在页面上显示已添加、编辑或删除的具体块。

使用差异视图时有两种选项：

1. **显示所有页面** — 这是差异视图的默认模式，它将在目录中同时显示已修改和未修改的页面。对于在整个空间的上下文中查看哪些页面已被编辑非常有用。
2. **仅显示已更改的页面** — 此模式将在目录中仅显示已修改的页面，帮助你专注于已更改的内容。在包含许多页面和子页面的较大空间中特别有用。

你可以切换到 **更改** 选项卡以检查任何变更请求中的差异视图。

### 合并变更请求

合并变更请求将把该变更请求的更改添加到内容的主分支，创建一个更新的版本并在空间的 [版本历史](https://gitbook.com/docs/documentation/zh/creating-content/version-control#see-the-activity-of-a-specific-draft).

中产生一条新记录。 [权限](https://gitbook.com/docs/documentation/zh/zhang-hu-guan-li/member-management/permissions-and-inheritance)如果你没有正确的 [合并规则](https://gitbook.com/docs/documentation/zh/collaboration/merge-rules).

### ，或你的变更请求未通过你所属组织或空间的

，你可能无法合并变更请求。

解决合并冲突

有时，当你想合并变更请求时，你可能会发现主内容与要合并的内容之间存在冲突。最简单的形式，冲突是无法自动合并的一段内容。 **如果发生这种情况，你会看到冲突警告，以及在继续合并之前需要解决的冲突列表。** 或 **在解决合并冲突时你有两个选项——** **选择要合并的版本**.

#### 手动

编辑内容

选择要合并的版本

#### 你可以通过选择要合并的版本来解决合并冲突——要么是你正在合并的内容，要么是之前存在的内容。这使你可以在两个更改之间做出选择——要么保留你最近的更改，要么保留原始内容。

如果你遇到可以通过这种方式解决的合并冲突，你可以选择要保留的版本，另一个版本将被删除。

### 手动编辑

如果你不想在版本之间做选择，可以通过手动编辑冲突来解决合并冲突。你可以删除不需要的块，甚至完全重写它们。一旦你对更改感到满意，就可以继续下一个冲突，直到全部解决。

归档变更请求 **操作菜单** <picture><source srcset="broken-reference" media="(prefers-color-scheme: dark)"><img src="https://2111890564-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FPnnI41SqLSaKBNwT98fW%2Factions-horizontal.svg?alt=media&#x26;token=99754200-a354-4ffe-931e-aa6322ea7395" alt="The Actions menu icon in GitBook"></picture> 如果你决定不合并变更请求并希望将其从队列中移除，可以将其归档。 **要归档变更请求，首先打开它。然后点击变更请求标题旁的**并选择 **归档** 。你可以稍后通过打开 **变更请求** 菜单并选择
