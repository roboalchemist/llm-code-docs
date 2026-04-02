Source: https://docs.slack.dev/tools/bolt-js/ja-jp/deployments/heroku

# Heroku へのデプロイ

このガイドでは、Bolt for JavaScriptと[Heroku プラットフォーム](https://heroku.com/)を使ってSlack アプリを用意して、デプロイするまでの手順を説明します。全体の流れとしては、Bolt Slack アプリをダウンロードし、Heroku 用の準備を済ませ、デプロイする流れになります。

この手順を全て終わらせたら、あなたはきっと️⚡️[getting-started-with-heroku](https://github.com/slackapi/bolt-js/tree/main/examples/deploy-heroku)のサンプルアプリを動作させたり、それに変更を加えたり、自分のアプリを作ったりすることができるようになるでしょう。

* * *

## Bolt Slack アプリを入手する {#get-a-bolt-slack-app}

Bolt アプリを作るのが初めてという場合は、まず[Bolt 入門ガイド](/tools/bolt-js/getting-started)に沿って進めてみましょう。または、以下のテンプレートアプリをクローンしてもよいでしょう。

```text
git clone https://github.com/slackapi/bolt-js-getting-started-app.git
```text

ダウンロードしたBolt アプリのディレクトリに移動します。

```text
cd bolt-js-getting-started-app/
```text

次に、このアプリをHeroku で動かすための準備をします。

* * *

## アプリをHeroku で動かすための準備する {#prepare-the-app-for-heroku}

Heroku は、作ったアプリをホストできる柔軟性の高いプラットフォームで、少し設定が必要です。このセクションでは、Bolt アプリに変更を加え、Heroku に対応させます。

### 1. Git リポジトリを使用する {#1-git-リポジトリを使用する}

Heroku にアプリをデプロイするには、まずGit リポジトリが必要です。まだGit を使ったことがない場合は、[Git をインストール](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)し、[Git リポジトリを作成](https://git-scm.com/book/en/v2/Git-Basics-Getting-a-Git-Repository)します

tip

前のセクションで`git clone`を使用した場合、Git リポジトリはすでに存在しますので、この手順はスキップできます

### 2. Procfile を追加する {#2-procfile-を追加する}

Heroku アプリでは、必ず`Procfile`という専用のファイルが必要です。このファイルを使ってHeroku にアプリの起動方法を伝えます。Bolt Slack アプリは、公開されたWeb アドレスを持つWeb サーバーとして起動します。

アプリのルートディレクトリに、拡張子なしの`Procfile`という名前のファイルを作成し、次の内容を貼りつけます。内容はどのようにアプリを動かすかによって変わります。

デフォルトでは Bolt アプリは公開された Web アドレスを持つ Web サーバーとして起動するので、以下のように指定します：

```text
web: node app.js
```text

ソケットモードを使ったアプリをデプロイするときは、ポートをリッスンしない worker として起動します：

```text
worker: node app.js
```text

ファイルを保存したら、ローカルのGit リポジトリにコミットします。

```text
git add Procfilegit commit -m "Add Procfile"
```text

tip

既存のBolt アプリを使ってこのガイドに沿って進めている場合は、[Preparing a Codebase for Heroku Deployment](https://devcenter.heroku.com/articles/preparing-a-codebase-for-heroku-deployment#4-listen-on-the-correct-port)のガイドを参考に、適切なポートをリッスンするようにしてください。

* * *

## Heroku ツールをセットアップする {#set-up-the-heroku-tools}

ローカルマシンでHeroku ツールのセットアップを行います。このツールは、Heroku プラットフォームを使用するアプリの管理、デプロイ、デバッグを行う場合に便利です。

### 1. Heroku CLI をインストールする {#1-heroku-cli-をインストールする}

Heroku ツールは、コマンドラインインターフェイス（CLI）の形で提供されています。さっそく[macOS、Windows、Linux 用のHeroku CLI](https://devcenter.heroku.com/articles/getting-started-with-nodejs#set-up)をインストールしましょう。macOS では次のコマンドを実行します。

```text
brew install heroku/brew/heroku
```text

インストールが完了したら、Heroku CLI を試してみましょう。どのようなコマンドが使えるかを一覧表示してみます。

```text
heroku help
```text

tip

`heroku`コマンドが見つからない場合は、パスを更新するため新しいターミナルセッションまたはターミナルタブを開いてください。

### 2. Heroku CLI にログインする {#2-heroku-cli-にログインする}

Heroku CLI では、ローカルマシンからHeroku アカウントに接続します。[無料のHeroku アカウントを新規登録](https://heroku.com)して、次のコマンドでHeroku CLI にログインします。

```text
heroku login
```text

tip

ファイアウォールを使っている場合、Heroku CLI で使用される[プロキシ環境変数](https://devcenter.heroku.com/articles/using-the-cli#using-an-http-proxy)の設定が必要なことがあります。

### 3. Heroku CLI へのログインが成功したか確認する {#3-heroku-cli-へのログインが成功したか確認する}

ログインできたかどうか確認しましょう。次のコマンドを実行すると、Heroku CLI に現在接続されているアカウント名が表示されます。

```text
heroku auth:whoami
```text

これでHeroku ツールのセットアップが完了しました。それではHeroku アプリの作成の本編に進みましょう。

* * *

## Heroku アプリを作成する {#create-an-app-on-heroku}

先ほどインストールしたツールを使って、[Heroku アプリを作成](https://devcenter.heroku.com/articles/creating-apps)します。アプリを作成するときは、ユニークな名前を自分で指定するか、ランダムな名前を生成することができます。

tip

[Heroku アプリはあとから名前を変更することもできます](https://devcenter.heroku.com/articles/renaming-apps)が、リモートのGit アドレスとパブリックのWeb アドレスも変更になります。

### 1. Heroku アプリを作成する {#1-heroku-アプリを作成する}

ユニークな名前を指定してHeroku アプリを作成します。

```text
heroku create my-unique-bolt-app-name
```text

または、ランダムな名前を楽しむならこちらで。

```text
heroku create# Creating sharp-rain-871... done, stack is heroku-18# https://sharp-rain-871.herokuapp.com/ | https://git.heroku.com/sharp-rain-871.git
```text

Heroku アプリが作成されると、いくつかの情報が表示されます。これらの情報は次のセクションで使用します。この例では、次のようになります。

* アプリ名: `sharp-rain-871`
* Web アドレス: `https://sharp-rain-871.herokuapp.com/`
* 空のリモートGit リポジトリ: `https://git.heroku.com/sharp-rain-871.git`

### 2. Heroku のリモートGit リポジトリを確認する {#2-heroku-のリモートgit-リポジトリを確認する}

Heroku CLI は、自動的に`heroku`という名前のリモートGit リポジトリをローカルに追加します。リモートGit リポジトリを一覧して、`heroku`が存在することを確認しましょう。

```text
git remote -v# heroku https://git.heroku.com/sharp-rain-871.git (fetch)# heroku https://git.heroku.com/sharp-rain-871.git (push)
```text

### 3. アプリをデプロイする {#3-アプリをデプロイする}

Slack アプリの認証情報をHeroku アプリに設定します。

```text
heroku config:set SLACK_SIGNING_SECRET=<your-signing-secret>heroku config:set SLACK_BOT_TOKEN=xoxb-<your-bot-token>
```text

tip

認証情報の入手場所がわからない場合、Bolt 入門ガイドで[署名シークレットとトークンのエクスポート](/tools/bolt-js/getting-started)について参照してください。

ローカルでのアプリの準備と、Heroku アプリの作成が完了しました。次のステップは、デプロイです。

* * *

## アプリをデプロイする {#deploy-the-app}

アプリをデプロイするため、ローカルのコードをHeroku にプッシュします。その後Slack アプリの設定を更新し、Heroku アプリに"hello" と声をかけてみましょう。 ✨

### 1. Heroku にアプリをデプロイする {#1-heroku-にアプリをデプロイする}

Heroku へのアプリのデプロイには、通常`git push`コマンドを使用します。これにより、ローカルリポジトリのコードがリモートの`heroku`リポジトリにプッシュされます。

次のコマンドでアプリをデプロイしましょう。

```text
git push heroku main
```text

Heroku でデプロイされるのは、[master またはmain ブランチ](https://devcenter.heroku.com/articles/git-branches)のコードです。それ以外のブランチにプッシュした場合、デプロイ処理はトリガーされません

tip

Heroku deploys code that's pushed to the [master or main branches](https://devcenter.heroku.com/articles/git-branches). Pushing to other branches will not trigger a deployment.

最後に、Heroku CLI を使ってWeb サーバーインスタンスを起動します。

```text
heroku ps:scale web=1
```text

### 2. Slack アプリの設定を更新する {#2-slack-アプリの設定を更新する}

次に、Heroku のWeb アドレスをリクエストURL に指定し、Slack からのイベントやアクションがこのURL に送信されるようにします。

次のコマンドを使ってHeroku のWeb アドレスを取得します。

```text
heroku info# ...# Web URL: https://sharp-rain-871.herokuapp.com/
```text

この例では、`https://sharp-rain-871.herokuapp.com/`がWeb アドレスとなります。

[Slack アプリのページ](https://api.slack.com/apps)を開き、アプリ名を選択します。次に、リクエストURLを自分で確認したWeb アドレスに変更します。設定する場所は2 か所あります。

tip

リクエストURL の末尾は`/slack/events`です。例えば`https://sharp-rain-871.herokuapp.com/slack/events`のようになります。

つ目の場所は、サイドパネルの「**Interactivity & Shortcuts**」です。これを選択し、リクエスト**URLを**更新します。

![Interactivity &amp; Shortcuts page](/assets/images/interactivity-and-shortcuts-page-9fd2aea5b54022019f3ae9f78b4207d2.png "Interactivity &amp; Shortcuts")

2 つ目の場所は、サイドパネルの「**Event Subscriptions**」です。これを選択し、リクエスト**URLを**更新します。

![Event Subscriptions page](/assets/images/event-subscriptions-page-af6db31acb1d6b357dcb77cdd4d7d326.png "Event Subscriptions")

tip

無料プランで使用するHeroku アプリは、非アクティブな状態が続くとスリープします。💤 認証が失敗した場合、すぐに再試行してみてください。

### 3. Slack アプリをテストする {#3-slack-アプリをテストする}

アプリのデプロイが完了し、Slack の設定変更も行いました。アプリを試してみましょう。

アプリが参加しているSlack チャンネルを開き、半角の小文字で"hello" と書き込みます。[Bolt 入門ガイド](/tools/bolt-js/getting-started)のとおり、アプリから応答があるはずです。応答がない場合、リクエスト**URLを**確認し、もう一度試してください。

* * *

## 変更をデプロイする {#deploy-an-update}

Slack アプリを構築するなかで、変更を加えてデプロイする必要があります。一般的な流れでは、変更を加え、コミットし、Heroku にプッシュするという順番です。

この流れをつかむため、アプリが"goodbye" というメッセージに応答するように変更を加えてみましょう。次のコードを`app.js` に追加します（[GitHub のソースコードはこちら](https://github.com/slackapi/bolt-js/blob/main/examples/deploy-heroku/app.js)）。

```text
// "goodbye" が含まれるメッセージの着信をリッスンapp.message('goodbye', async ({ message, say }) => {  // say() で、イベントがトリガーされたチャンネルにメッセージを送信する  await say(`See ya later, <@${message.user}> :wave:`);});
```text

変更内容をローカルのGit リポジトリにコミットします。

```text
git commit -am "ユーザーに'goodbye' を返す"
```text

変更内容をリモートのherokuリポジトリにプッシュし、デプロイします。

```text
git push heroku main
```text

デプロイ処理が完了したら、アプリが参加しているSlack チャンネルを開き、半角の小文字で"goodbye" と書き込みます。Slack アプリから、さよならの挨拶が返ってくるはずです。

* * *

## 次のステップ {#next-steps}

これではじめて️⚡Bolt for JavaScript アプリをHerokuへデプロイすることに成功しました。🚀

基本的なアプリのデプロイができましたので、次はアプリのカスタマイズやモニタリングを行う方法を調べてみましょう。おすすめのステップをいくつか紹介します。

* [How Heroku Works](https://devcenter.heroku.com/articles/how-heroku-works)を読んでHeroku の動作の理解を深めたり、[Heroku アプリを無料で使う場合の制限](https://devcenter.heroku.com/articles/free-dyno-hours)をチェックしたりする。
* Bolt の基本的な概念を参考にしてアプリを拡張したり、[Heroku Add-ons](https://elements.heroku.com/addons)をアプリに取り入れたりする
* Bolt の応用コンセプトでログの表示について学習し、[Heroku でのログメッセージの確認方法](https://devcenter.heroku.com/articles/getting-started-with-nodejs#view-logs)を把握する。
* [Heroku アプリのスケール方法](https://devcenter.heroku.com/articles/getting-started-with-nodejs#scale-the-app)に従って、アクセスの増加に対処する。
