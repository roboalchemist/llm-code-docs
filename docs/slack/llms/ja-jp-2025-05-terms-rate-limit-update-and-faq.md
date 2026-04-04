Source: https://docs.slack.dev/ja-jp/2025-05-terms-rate-limit-update-and-faq

# 非 Marketplace アプリのレート制限の変更

_このページは、既存の社内用ユーザー構築アプリに対するレート制限を明確にするために更新されました。_

非 Marketplace アプリ向けの [`conversations.history`](/reference/methods/conversations.history) および [`conversations.replies`](/reference/methods/conversations.replies) Web API メソッドのレート制限を更新しています。このレート制限の削減は、Marketplace 外で商用配布されるアプリケーション（「非掲載」アプリとも呼ばれます）にのみ適用されます。これは、新しい非掲載アプリケーションと既存の非掲載 非 Marketplace アプリケーションの新しいインストールに即座に影響を与えます。新しいレート制限は、Marketplace 外で公開された非掲載配布アプリケーションの既存インストールには適用されません。新しいレート制限は、1 分あたり 1 リクエストを許可し、リクエストあたり最大 15 オブジェクトを返すように更新されます。

Slack は [Slack API サービス利用規約](https://slack.com/terms-of-service/api)を更新します。2025 年 5 月 29 日以降に作成されたアプリケーションには、更新された規約がただちに適用されます。2025 年 5 月 29 日より前に作成されたアプリには、2025 年 6 月 30 日に適用されます。

また、Slack は [`conversations.history`](/reference/methods/conversations.history) および [`conversations.replies`](/reference/methods/conversations.replies) API メソッドのレート制限を更新します。この変更は Marketplace アプリには影響しません。新しい非 Marketplace アプリケーション、および既存の非 Marketplace アプリケーションの新規インストールには、2025 年 5 月 29 日より、更新されたレート制限が即時適用されます。Marketplace 外で配布されたアプリの既存インストールには、新しいレート制限は適用されません。

[英語版](/changelog/2025/05/29/rate-limit-changes-for-non-marketplace-apps).

## 変更の詳細 {#what}

Slack Marketplace で承認されていない商用配布アプリの場合、[`conversations.history`](/reference/methods/conversations.history) および [`conversations.replies`](/reference/methods/conversations.replies) API メソッドの両方のレート制限が `Tier 3` から `Tier 1` に変更されます。

* [`conversations.history`](/reference/methods/conversations.history) - Slack Marketplace で承認されない限り、**2025 年 5 月 29 日**より後に作成された商用配布アプリ、および既存アプリの新規インストールでは、`conversations.history` API メソッドのレート制限が 1 分あたり 1 回のリクエストに制限されます。`limit` パラメーターの最大値と既定値は 15 オブジェクトに削減されています。

* [`conversations.replies`](/reference/methods/conversations.replies) - Slack Marketplace で承認されない限り、**2025 年 5 月 29 日**より後に作成された商用配布アプリ、および既存アプリの新規インストールでは、`conversations.replies` API メソッドのレート制限が 1 分あたり 1 回のリクエストに制限されます。`limit` パラメーターの最大値と既定値は 15 オブジェクトに削減されています。

社内用ユーザー構築アプリは、これらの変更による影響を受けません。カスタムアプリの場合、[`conversations.history`](/reference/methods/conversations.history) および [`conversations.replies`](/reference/methods/conversations.replies) API メソッドは、1 分あたり原則 50 回までのリクエストに制限されます。limit パラメーターの最大値と既定値は 1,000 オブジェクトです。

[不明な点への詳細な回答については、続きをお読みください](#faq)。もちろん、これらの変更に関して質問や懸念、提案があればお知らせください。よろしくお願いいたします。

## よくある質問 {#faq}

### API サービス利用規約はどのように変更されますか？ {#what-tos}

利用規約全文は[こちら](https://slack.com/terms-of-service/api)でご覧いただけます。変更点の概要は以下のとおりです。

**商用配布**: 更新後の規約では、Slack API を使用して作成されたアプリを商用配布する場合、[Slack Marketplace](https://slack.com/marketplace) のみが正式な配布経路として認められています。アプリが「非掲載」（Marketplace 以外で公開されている）であるか、製品に接続するテンプレート化されたカスタムアプリのユーザー向け手順を提供しているかは関係ありません。

**データの使用**: Slack API 経由でアクセスされるデータをサードパーティーアプリケーションで保存、使用、共有する方法に関する安全対策を強化します。

**API 固有の規約**: Discovery API や Data Access API などの特定の API を責任を持って使用する方法について、明確なガイダンスを提供します。

### Slack API はどのように変更されますか？ {#what-api}

ほとんどの開発者には、Slack API の変更による影響はありません。Slack では、[Slack App Marketplace](https://my.slack.com/marketplace) 外で配布されるアプリのみを対象に、2 つの特定の [Web API](/apis/web-api) メソッド（[`conversations.history`](/reference/methods/conversations.history) および [`conversations.replies`](/reference/methods/conversations.replies) メソッド）に対象を絞ってレート制限の変更を実施します。これらのメソッドはアプリがコメントやスレッドを読み取ることができるように設計されたものですが、未審査のアプリケーションがこれらを使用して機密性のある会話データを大量に抜き取る可能性もあります。ワークスペースデータのセキュリティを維持し、未審査のアプリケーションによる大量のデータ抜き取りを防ぐため、これらのメソッドに対して 1 分あたり 1 回のリクエスト、リクエスト 1 回あたり 15 件のメッセージというレート制限が新たに適用されます。Marketplace アプリのレート制限は変更されません。社内用ユーザー構築アプリについても変更はありません。

また、現在は一部のパートナーのみに提供されている、リアルタイム検索 API の新しいオフプラットフォーム機能も発表します。

### 変更を行う理由は？ {#why}

AI システムが強力になるにつれて、顧客データへのアクセス方法や使用方法に関連するリスクも増大します。Slack は、ポリシーの強化と明確化によって、不正なデータスクレイピングや不正使用を防止しながら、ユーザー企業の保護を強化し、イノベーションを支援します。

[Slack 開発者向けポリシー](/developer-policy)に記載されているように、Slack Marketplace は常に安全かつ高品質なアプリを提供することを意図した場所です。Slack は Marketplace への掲載に料金を請求しないため、開発者は [Marketplace のガイドライン](//slack-marketplace/slack-marketplace-app-guidelines-and-requirements)を満たし、アプリの審査を受ければ Marketplace を利用できます。Slack がアプリの認定や推奨を行うことはありませんが、Marketplace への掲載に先立ってアプリのセキュリティレビューを実施し、アプリの機能に照らしてリクエストされたスコープを分析します。このプロセスにより、ツールに対するユーザーの信頼が高まり、Slack エコシステムのセキュリティも確保できます。一方、非掲載アプリは開発やテストを意図したものであり、大規模な配布や商用配布に使用するものではありません。今回の API サービス利用規約の更新により、この点がさらに明確化されます。

これらのポリシーの変更に加えて、会話に関する 2 つのメソッドに対象を絞ったレート制限を実施することにより、顧客データに対するリスクが最も大きいと思われる、大量の顧客データの取得機能を持つ未審査のアプリケーションに対処します。

さらに Slack では、ユーザーと開発者の双方が、Slack の会話に蓄積された貴重なビジネスナレッジを安全に活用したいと強く望んでおられることを認識しています。そこで、リアルタイム検索 API にオフプラットフォームの新しい機能を追加し、Marketplace アプリケーションの可能性を広げ、期待が膨らむ新しい AI ユースケースの実現に貢献します。

### Marketplace アプリは影響を受けますか？ {#marketplace-impacts}

これらの規約の更新は Slack API を使用したすべての開発に適用されますが、[Slack Marketplace のガイドライン](/slack-marketplace/slack-marketplace-app-guidelines-and-requirements)に準拠する Marketplace アプリにはまったく影響しません。

### 非 Marketplace アプリは影響を受けますか？ {#non-marketplace-impacts}

これらの規約の変更は Slack API を使用したすべての開発に適用されますが、大多数の開発者にとって変更を意識することはしばらくないでしょう。

[`conversations.history`](/reference/methods/conversations.history) または [`conversations.replies`](/reference/methods/conversations.replies) Web API メソッドを呼び出さない場合、当面の間はレート制限の変更に気づく可能性は低いです。とはいえ、すべての商用配布アプリの適切な配布元は Marketplace のみです。そのため、アプリケーションを商用配布する場合は、[掲載プロセス](/slack-marketplace/distributing-your-app-in-the-slack-marketplace)を調べ、[Slack Marketplace のガイドライン](/slack-marketplace/slack-marketplace-app-guidelines-and-requirements)を確認して、アプリを Marketplace 掲載に適したものにする方法を理解する必要があります。

レート制限の変更や適用の影響を受ける開発者の皆さまには、アプリへの影響と今後の対応についてより詳細な情報が記載された通知をお届けします。特に注意すべき点として、本日より、商用配布されている 非 Marketplace アプリを新しくインストールした場合、[`conversations.history`](/reference/methods/conversations.history) および [`conversations.replies`](/reference/methods/conversations.replies) Web API メソッドには引き下げ後のレート制限が適用されます。ワークスペースデータのセキュリティを維持し、未審査のアプリケーションによる大量のデータ抜き取りを防ぐため、これらのメソッドに対して 1 分あたり 1 回のリクエスト、リクエスト 1 回あたり 15 件のメッセージというレート制限が新たに適用されます。社内用ユーザー構築アプリケーションは、これらの変更による影響を受けません。1 分あたり原則 50 回までのリクエスト、リクエスト 1 回あたり 1,000 件のメッセージというレート制限が引き続き適用されます。

### 社内用アプリは影響を受けますか？ {#internal}

いいえ、社内用ユーザー構築アプリは影響を受けません。現在の高いレート制限が保持されます。新しいレート制限は、Marketplace 外で商用配布されるアプリケーションのみに適用されます。

### リアルタイム検索 API とは何ですか？また、これらの変更後にチャンネルデータへアクセスする際、この API はどのように役立ちますか？ {#real-time-search-api}

ユーザー企業や開発者が Slack のデータを活用してアプリケーションの機能を強化したいと考えるのは当然のことです。しかし、インデックス作成やクエリのためにユーザーの会話データを一括ダウンロードすると、機密情報が漏洩したり、プライベートチャンネルのメンバーシップのような Slack のアクセス制御が損なわれたりするリスクが生じます。

リアルタイム検索 API は、こうしたニーズに応えるものであり、今回の変更後も Slack チャンネルのデータにこれまでより安全かつ快適にアクセスできるようにします。この API を使用すると、Slack データを保存せずにリアルタイムでクエリを実行できるため、ユーザー企業と開発者は、機密性の高い会話データを保存することなく、より的を絞ったアプローチで Slack 内にある豊富なナレッジを活用できます。現時点では、この API は一部のパートナーに限定ベータ版として提供されています。一般提供開始については、今後の発表にご期待ください。

### Marketplace の要件を満たすために、アプリをどのように更新すればよいですか？ {#meet-marketplace-requirements}

Marketplace に適したアプリケーションの種類の詳細と、ユースケースに合わせたメソッドとスコープの活用方法に関するガイダンスについては、[Marketplace のガイドライン](/slack-marketplace/slack-marketplace-app-guidelines-and-requirements)を参照してください。

リアルタイム検索 API の導入によってリアルタイムの検索とデータアクセスが容易になることで、これまで Marketplace では承認されなかったユースケースを実現できるようになる可能性もあります。

### レート制限エラーを回避するために、アプリをどのように更新すればよいですか？ {#avoid-errors}

レート制限エラーが増加している場合は、[レート制限条件への対応方法に関するガイド](/apis/web-api/rate-limits)を参照してください。ほとんどのアプリで、チャンネルのコンテンツ全体を読み取る必要はありません。レート制限エラーが発生する場合は、アプリで通常必要とされるコンテキスト情報に的を絞って取得するため、プラットフォームが提供するほかの方法（[Events API](/apis/events-api) や近日公開予定のリアルタイム検索 API など）の使用を検討してください。

### 何もしなかったらどうなりますか？ {#nothing}

ほとんどのアプリはこれらの変更の影響を受けません。すでに [`conversations.history`](/reference/methods/conversations.history) および [`conversations.replies`](/reference/methods/conversations.replies) Web API メソッドを使用しているアプリは引き続き機能しますが、Slack Marketplace で承認されていない場合は、新たにインストールするとレート制限エラーが増加する可能性があります。これらのレート制限はこれらのアプリの既存インストールには影響しません。あなたが作成し、商用配布した新しいアプリは、Slack Marketplace に提出されない限り、レート制限エラーが増加する可能性があります。

_こちらは、2025年 5 月 29日に公開された [Slack Developers Changelog の公式英語記事](/changelog/2025/05/29/rate-limit-changes-for-non-marketplace-apps)の日本語翻訳です。_
