Source: https://docs.slack.dev/tools/java-slack-sdk/ja-jp/reference

# リファレンス

## モジュール一覧 {#-モジュール一覧}

以下のテーブルは、この Java SDK で現在提供されているモジュールの一覧を示しています。これらのモジュールは、たとえその一部のモジュール自体には変更がなく、依存ライブラリ側の変更しかなかったとしても、すべてのモジュールが必ず同じタイミングでリリースされます。そのため、いかなるタイミングでも、必ず同一の最新バージョンが存在します。

全てのリリースは Maven Central リポジトリで公開されています。最新のバージョンは `1.48.0` です。

## Bolt とその標準拡張モジュール {#bolt-とその標準拡張モジュール}

groupId:artifactId

説明

[`com.slack.api:bolt`](https://search.maven.org/search?q=g:com.slack.api%20AND%20a:bolt) [📖](https://oss.sonatype.org/service/local/repositories/releases/archive/com/slack/api/bolt/1.48.0/bolt-1.48.0-javadoc.jar/!/index.html#package)

Bolt は全ての Slack プラットフォームの公開機能を利用して Slack アプリを開発するためのフレームワークで、特定の環境やフレームワークに依存しない抽象化されたレイヤーを提供します。

[`com.slack.api:bolt-socket-mode`](https://search.maven.org/search?q=g:com.slack.api%20AND%20a:bolt-socket-mode) [📖](https://oss.sonatype.org/service/local/repositories/releases/archive/com/slack/api/bolt-socket-mode/1.48.0/bolt-socket-mode-1.48.0-javadoc.jar/!/index.html#package)

ソケットモード環境で Bolt アプリを動作させるためのアダプターを提供するモジュールです。

[`com.slack.api:bolt-jakarta-socket-mode`](https://search.maven.org/search?q=g:com.slack.api%20AND%20a:bolt-jakarta-socket-mode) [📖](https://oss.sonatype.org/service/local/repositories/releases/archive/com/slack/api/bolt-jakarta-socket-mode/1.48.0/bolt-jakarta-socket-mode-1.48.0-javadoc.jar/!/index.html#package)

ソケットモード環境で Bolt アプリを動作させるためのアダプターを提供するモジュールです。

[`com.slack.api:bolt-servlet`](https://search.maven.org/search?q=g:com.slack.api%20AND%20a:bolt-servlet) [📖](https://oss.sonatype.org/service/local/repositories/releases/archive/com/slack/api/bolt-servlet/1.48.0/bolt-servlet-1.48.0-javadoc.jar/!/index.html#package)

Java EE Servlet 環境で Bolt アプリを動作させるためのアダプターを提供するモジュールです。

[`com.slack.api:bolt-jetty`](https://search.maven.org/search?q=g:com.slack.api%20AND%20a:bolt-jetty) [📖](https://oss.sonatype.org/service/local/repositories/releases/archive/com/slack/api/bolt-jetty/1.48.0/bolt-jetty-1.48.0-javadoc.jar/!/index.html#package)

Bolt で実装された Slack アプリを [Java EE 互換 Jetty HTTP サーバー (9.x)](https://www.eclipse.org/jetty/)で動作させるモジュールです。

[`com.slack.api:bolt-jakarta-servlet`](https://search.maven.org/search?q=g:com.slack.api%20AND%20a:bolt-jakarta-servlet) [📖](https://oss.sonatype.org/service/local/repositories/releases/archive/com/slack/api/bolt-jakarta-servlet/1.48.0/bolt-jakarta-servlet-1.48.0-javadoc.jar/!/index.html#package)

Jakarta EE Servlet 環境で Bolt アプリを動作させるためのアダプターを提供するモジュールです。

[`com.slack.api:bolt-jakarta-jetty`](https://search.maven.org/search?q=g:com.slack.api%20AND%20a:bolt-jakarta-jetty) [📖](https://oss.sonatype.org/service/local/repositories/releases/archive/com/slack/api/bolt-jakarta-jetty/1.48.0/bolt-jakarta-jetty-1.48.0-javadoc.jar/!/index.html#package)

Bolt で実装された Slack アプリを [Jakarta EE 互換 Jetty HTTP サーバー](https://www.eclipse.org/jetty/)で動作させるモジュールです。

[`com.slack.api:bolt-aws-lambda`](https://search.maven.org/search?q=g:com.slack.api%20AND%20a:bolt-aws-lambda) [📖](https://oss.sonatype.org/service/local/repositories/releases/archive/com/slack/api/bolt-aws-lambda/1.48.0/bolt-aws-lambda-1.48.0-javadoc.jar/!/index.html#package)

Bolt で実装された Slack アプリを AWS [API Gateway](https://aws.amazon.com/api-gateway/) + [Lambda](https://aws.amazon.com/lambda/) で動作させるためのモジュールです。

[`com.slack.api:bolt-google-cloud-functions`](https://search.maven.org/search?q=g:com.slack.api%20AND%20a:bolt-google-cloud-functions) [📖](https://oss.sonatype.org/service/local/repositories/releases/archive/com/slack/api/bolt-google-cloud-functions/1.48.0/bolt-google-cloud-functions-1.48.0-javadoc.jar/!/index.html#package)

Bolt で実装された Slack アプリを [Google Cloud Functions](https://cloud.google.com/functions) で動作させるためのモジュールです。

[`com.slack.api:bolt-micronaut`](https://search.maven.org/search?q=g:com.slack.api%20AND%20a:bolt-micronaut) [📖](https://oss.sonatype.org/service/local/repositories/releases/archive/com/slack/api/bolt-micronaut/1.48.0/bolt-micronaut-1.48.0-javadoc.jar/!/index.html#package)

[Micronaut](https://micronaut.io/) で Bolt アプリを動作させるためのアダプターを提供するモジュールです。

[`com.slack.api:bolt-helidon`](https://search.maven.org/search?q=g:com.slack.api%20AND%20a:bolt-helidon) [📖](https://oss.sonatype.org/service/local/repositories/releases/archive/com/slack/api/bolt-helidon/1.48.0/bolt-helidon-1.48.0-javadoc.jar/!/index.html#package)

[Helidon SE](https://helidon.io/docs/latest/) で Bolt アプリを動作させるためのアダプターを提供するモジュールです。

[`com.slack.api:bolt-http4k`](https://search.maven.org/search?q=g:com.slack.api%20AND%20a:bolt-http4k) [📖](https://oss.sonatype.org/service/local/repositories/releases/archive/com/slack/api/bolt-http4k/1.48.0/bolt-http4k-1.48.0-javadoc.jar/!/index.html#package)

[http4k](https://http4k.org/) で Bolt アプリを動作させるためのアダプターを提供するモジュールです。

[`com.slack.api:bolt-ktor`](https://search.maven.org/search?q=g:com.slack.api%20AND%20a:bolt-ktor) [📖](https://oss.sonatype.org/service/local/repositories/releases/archive/com/slack/api/bolt-ktor/1.48.0/bolt-ktor-1.48.0-javadoc.jar/!/index.html#package)

[Ktor](https://ktor.io/) で Bolt アプリを動作させるためのアダプターを提供するモジュールです。

## 基盤モジュール {#基盤モジュール}

groupId:artifactId

Description

[`com.slack.api:slack-api-model`](https://search.maven.org/search?q=g:com.slack.api%20AND%20a:slack-api-model) [📖](https://oss.sonatype.org/service/local/repositories/releases/archive/com/slack/api/slack-api-model/1.48.0/slack-api-model-1.48.0-javadoc.jar/!/index.html#package)

チャンネル、メッセージ、ユーザー、Block Kit のブロックとそれによって構成されるサーフェスエリアなど [Slack の核となるような重要なオブジェクト（英語）](/reference/objects)を表現するクラス群を提供します。

[`com.slack.api:slack-api-model-kotlin-extension`](https://search.maven.org/search?q=g:com.slack.api%20AND%20a:slack-api-model-kotlin-extension) [📖](https://oss.sonatype.org/service/local/repositories/releases/archive/com/slack/api/slack-api-model-kotlin-extension/1.48.0/slack-api-model-kotlin-extension-1.48.0-javadoc.jar/!/index.html#package)

Block Kit のデータ構造を Kotlin ネイティブな DSL を使って構築できるビルダーのモジュールを提供します。

[`com.slack.api:slack-api-client`](https://search.maven.org/search?q=g:com.slack.api%20AND%20a:slack-api-client) [📖](https://oss.sonatype.org/service/local/repositories/releases/archive/com/slack/api/slack-api-client/1.48.0/slack-api-client-1.48.0-javadoc.jar/!/index.html#package)

様々な Slack API クライアントを提供します。サポートされているのは、API メソッド、ソケットモード、RTM API、SCIM API、Audit Logs API、ステータス API です。

[`com.slack.api:slack-api-client-kotlin-extension`](https://search.maven.org/search?q=g:com.slack.api%20AND%20a:slack-api-client-kotlin-extension) [📖](https://oss.sonatype.org/service/local/repositories/releases/archive/com/slack/api/slack-api-client-kotlin-extension/1.48.0/slack-api-client-kotlin-extension-1.48.0-javadoc.jar/!/index.html#package)

Slack API クライアントのリクエストビルダーのメソッドを拡張することで、Block Kit のデータ構造を構築するための Kotlin ネイティブな DSL を直接利用できるようにするモジュールを提供します。

[`com.slack.api:slack-jakarta-socket-mode-client`](https://search.maven.org/search?q=g:com.slack.api%20AND%20a:slack-jakarta-socket-mode-client) [📖](https://oss.sonatype.org/service/local/repositories/releases/archive/com/slack/api/slack-jakarta-socket-mode-client/1.48.0/slack-jakarta-socket-mode-client-1.48.0-javadoc.jar/!/index.html)

Jakarta EE 互換のソケットモードクライアントを提供します。

[`com.slack.api:slack-app-backend`](https://search.maven.org/search?q=g:com.slack.api%20AND%20a:slack-app-backend) [📖](https://oss.sonatype.org/service/local/repositories/releases/archive/com/slack/api/slack-app-backend/1.48.0/slack-app-backend-1.48.0-javadoc.jar/!/index.html#package)

Slack アプリサーバーサイドで必要となる共通モジュールやペイロードなどのデータ構造を提供します。サポートされているのは、イベント API、インタラクティブコンポーネント、スラッシュコマンド、アクション、そして OAuth フローです。これらの機能はよりプリミティブなレイヤーとして Bolt から利用されています。
