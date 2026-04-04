Source: https://docs.slack.dev/tools/java-slack-sdk/ja-jp/guides/web-api-for-admins

# OrG 管理者向け API

Slack の [API メソッド](/reference/methods) のうち、一部のメソッド名は **`admin.`** から始まっています。ご存知かもしれませんが、これらの API は全ての開発者向けのものではありません。これらは [Enterprise Grid](/enterprise) の [OrG](https://slack.com/intl/ja-jp/help/articles/360004150931) 管理者が利用するための API 群です。

* * *

## OrG 管理者向け API の呼び出し {#org-管理者向け-api-の呼び出し}

OrG 管理者向け API の呼び出しは、それ用の scope が必定であること以外は他の API メソッドと何ら違いはありません。

```text
String orgAdminToken = System.getenv("SLACK_ORG_ADMIN_TOKEN");Slack slack = Slack.getInstance();// ユーザーセッションをサーバーサイドでリセットAdminUsersSessionResetResponse response = slack.methods(orgAdminToken).adminUsersSessionReset(r -> r  .userId(userId));// チャンネルを全ワークスペースでのマルチワークスペースチャンネルに変更AdminConversationsSetTeamsResponse orgChannelResp = slack.methods(orgAdminToken).adminConversationsSetTeams(r -> r  .teamId("T1234567")  .channelId("C12345567")  .orgChannel(true));// 承認済アプリの一覧を取得AdminAppsApprovedListResponse response = slack.methods(orgAdminToken).adminAppsApprovedList(r -> r  .limit(1000)  .teamId("T1234567"));// まだまだたくさんあります...!
```

網羅的な管理系 API の一覧は[こちら](/admins/)で確認することができます。また、この SDK の [Javadoc](https://oss.sonatype.org/service/local/repositories/releases/archive/com/slack/api/slack-api-client/1.48.0/slack-api-client-1.48.0-javadoc.jar/!/com/slack/api/methods/MethodsClient.html) にアクセスして、ページ内検索で **`admin`** で始まるものを探すのもよいでしょう。
