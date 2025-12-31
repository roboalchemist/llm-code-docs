# Source: https://gitbook.com/docs/documentation/zh/gitbook-agent/zi-dong-wen-dang-jian-yi/lian-jie-shu-ju-yuan.md

# 连接数据源

GitBook Agent 可以从不同来源获取上下文，包括 Intercom、Slack、电子邮件等。连接一个来源允许 Agent 根据真实世界的上下文（例如电子邮件链、Slack 线程或已解决的 Intercom 会话）构建变更请求。

Agent 会扫描这些上下文，将相关数据分组为问题和主题，然后基于这些数据点生成建议的更改。

通过不同连接器提供的上下文将使您的团队工作更快、更可靠，减少重复记录在其他平台上可能已解决事项的工作。

### 连接一个来源

转到您组织的设置，然后进入 **GitBook Agent** 部分。在此处，您可以配置不同的连接器，以便成功连接所需的工具。

每个连接器的工作方式略有不同，可能包含不同的功能。请参阅下面您所用工具的部分，以查看如何配置和使用所需工具。

<details>

<summary>电子邮件</summary>

电子邮件连接器是一个多功能连接器，允许您向 GitBook Agent 提供上下文 **通过专用电子邮件地址**.

使用电子邮件连接器无需额外配置——开箱即可使用。

#### 将电子邮件线程添加到 GitBook Agent

1. 通过将电子邮件线程转发到 GitBook Agent 设置中提供的专用电子邮件地址，将任何电子邮件线程添加到 Agent。

#### 使用电子邮件连接器连接第三方应用

电子邮件连接器是向 GitBook 提供上下文的最通用方式。使用诸如 [Zapier](https://zapier.com/) 或 [Relay.app](https://relay.app/)，您可以连接成千上万的第三方应用。

在任一工具中，设置新的工作流/连接，并确保输出发送到 GitBook Agent 设置中提供的专用电子邮件地址。

</details>

<details>

<summary>Intercom</summary>

Intercom 连接器允许 GitBook Agent 从以下内容中提取上下文： **已解决或已关闭的会话**.&#x20;

每当您的支持团队关闭会话时，Intercom 连接器会将该会话的完整上下文发送给 GitBook Agent。Agent 将使用该上下文生成 [问题](https://gitbook.com/docs/documentation/zh/gitbook-agent/tan-suo-nin-de-shu-ju#issues) （以及最终的 [主题](https://gitbook.com/docs/documentation/zh/gitbook-agent/tan-suo-nin-de-shu-ju#topics)），然后用这些内容生成可操作的更改请求，供您的团队审阅。

#### 连接 Intercom

1. 在 GitBook Agent 的设置中，点击 Intercom 连接器并使用您的账号授权 Intercom。
2. 登录后，GitBook Agent 即可开始分析您已关闭的支持工单。

#### 将 Intercom 会话添加到 GitBook Agent

Intercom 连接器在后台工作——安装并配置后，它会在后台运行并自动将已解决或已关闭的会话添加到 GitBook Agent。

</details>

<details>

<summary>Slack</summary>

Slack 连接器允许 GitBook Agent 从以下内容中提取上下文： **被标记的线程**.

一旦在线程中调用 Slack 连接器，它将分析该线程的上下文，并将会话的完整上下文发送到您的 GitBook Agent。Agent 然后将使用这些上下文生成问题（以及最终的主题），再基于这些内容生成可操作的更改请求，供您的团队审阅。

#### 连接 Slack

1. 在 GitBook Agent 的设置中，点击 Slack 连接器并使用您的账号授权 Slack。
2. 将 Slack 机器人安装到您组织的 Slack 工作区。

#### 将 Slack 线程添加到 GitBook Agent

1. 在您想要采集的线程中调用 `@gitbook` 。
2. 可选地添加 Agent 可使用的额外上下文，例如：

```
@gitbook 使用此会话更好地记录我们的 API 参考。
```

</details>
