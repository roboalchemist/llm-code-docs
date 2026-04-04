# Source: https://gitbook.com/docs/documentation/ja-gitbook-documentation/creating-content/ai-kdinguashisutantoto-skillmd.md

# AI コーディングアシスタントと skill.md

GitBook は [skill.md](https://gitbook.com/docs/skill.md) ファイルを提供しており、AI コーディングアシスタントに GitBook ドキュメントを適切に編集する方法を教えます。ローカルで GitBook ドキュメントを編集する際の「プロジェクトルール」として使用してください。これは、 [Git Sync ](https://gitbook.com/docs/documentation/ja-gitbook-documentation/getting-started/git-sync)ワークフロー（ドキュメントをローカルで編集し、変更をコミットしてドキュメントサイトを更新する）に適しています。参照ファイルには GitBook のマークダウン拡張、カスタムブロック、設定ファイル、およびベストプラクティスが含まれます。

{% hint style="info" %}
GitBook はまた [GitBook Agent](https://gitbook.com/docs/documentation/ja-gitbook-documentation/gitbook-agent) を提供しており、エディタから直接 AI 支援のドキュメント作成が可能です。本ガイドは、Claude Code や Cursor のような外部のコーディングアシスタントを利用することを好むチーム向けです。
{% endhint %}

### skill.md ファイルの内容

* すべてのカスタムブロックの完全な構文リファレンス
* 設定ファイルの形式（`.gitbook.yaml`, `SUMMARY.md`, `.gitbook/vars.yaml`)
* フロントマターのオプションとレイアウト制御
* 変数と式の構文
* 適切なブロックタイプを選択するための意思決定表
* よくある落とし穴とベストプラクティス

このファイルを AI コーディングアシスタントに追加すると、GitBook ドキュメントの作成、編集、フォーマットに関する必要な情報が提供されます。つまり、アシスタントは GitBook の機能に対する確立されたフレームワークとベストプラクティスに従って動作します。

### URL で skill.md を使用する

ほとんどの AI コーディングアシスタントはプロジェクト固有の指示をサポートしています。スキルファイルの URL をプロジェクト設定で参照することで、アシスタントが GitBook の構文にどのように対応するかを認識できます。

### skill.md をローカルで使用する

スキルファイルをダウンロードしてリポジトリに含めることもできます。まず、skill.md をリポジトリのルートにダウンロードし、その後コーディングアシスタントのルールファイルで参照してください。 `"GitBook の構文とベストプラクティスについてはリポジトリルートの skill.md を参照してください"` .&#x20;

この方法はオフラインでも機能し、チーム固有の修正を可能にします。&#x20;

{% hint style="warning" %}
GitBook が新機能を追加する際には、最新版の skill.md ファイルでローカルリポジトリを更新することを忘れないでください。
{% endhint %}

### AI 生成コンテンツのテスト

AI アシスタントによって生成されたコンテンツは、技術的な正確性と適切なフォーマットの両面で常にレビューおよびテストすることが重要です。&#x20;

skill ファイルで学習した AI アシスタントと作業する際には、次の点を行うべきです：

* カスタムブロックが GitBook で正しくレンダリングされることを確認する
* すべての内部リンクが機能することを確認する
* フロントマターが有効な YAML であることを確認する
* 変数が正しいスコープを参照していることをテストする

{% hint style="warning" %}
**注：** AI アシスタントは時折誤った構文を生成したり、カスタムブロックの閉じ忘れをすることがあります。コミットする前に常に変更内容を確認してください。
{% endhint %}

### GitBook Agent

直接 GitBook で作業する方が良いですか？ [GitBook Agent](https://gitbook.com/docs/documentation/ja-gitbook-documentation/gitbook-agent/what-is-gitbook-agent) は Git Sync を使用しているかどうかに関係なく、GitBook エディタ内で AI 支援のワークフローを提供します。

Agent はドキュメントの完全なコンテキストを把握しており、GitBook のブロックや機能を最良の方法で使用する方法について既に学習しています。Agent はコンテンツの草案作成、更新の実施、さまざまなユースケース向けのドキュメント最適化を GitBook アプリ内から支援します。

<a href="../gitbook-agent" class="button primary">GitBook Agent を発見する</a>
