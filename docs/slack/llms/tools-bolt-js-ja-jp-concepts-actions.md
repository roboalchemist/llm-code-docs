Source: https://docs.slack.dev/tools/bolt-js/ja-jp/concepts/actions

# アクション

Bolt アプリは `action` メソッドを用いて、ボタンのクリック、メニューの選択、メッセージショートカットなどのユーザーのアクションをリッスンすることができます。

## アクションのリスニング {#アクションのリスニング}

アクションは文字列型の `action_id` または RegExp オブジェクトでフィルタリングできます。 `action_id` は、Slack プラットフォーム上のインタラクティブコンポーネントの一意の識別子として機能します。

すべての `action()` の例で `ack()` が使用されていることに注目してください。Slack からリクエストを受信したことを確認するために、アクションリスナー内で `ack()` 関数を呼び出す必要があります。これについては、「[リクエストの確認](/tools/bolt-js/concepts/acknowledge)」 セクションで説明しています。

info

Bolt 2.x からメッセージショートカット（以前はメッセージアクションと呼ばれていました）は `action()` ではなく `shortcut()` メソッドを使用するようになりました。この変更については [2.x マイグレーションガイド](/tools/bolt-js/migration/migration-v2)を参照してください。

`block_actions` ペイロードの詳細については、[こちら](/reference/interaction-payloads) をご覧ください。リスナー内からビューの完全なペイロードにアクセスするには、コールバック関数内で `body` 引数を参照します。

```text
// action_id が "approve_button" のインタラクティブコンポーネントがトリガーされる毎にミドルウェアが呼び出されるapp.action('approve_button', async ({ ack }) => {  await ack();  // アクションを反映してメッセージをアップデート});
```text

### 制約付きオブジェクトを使用したアクションのリスニング {#制約付きオブジェクトを使用したアクションのリスニング}

制約付きのオブジェクトを使って、 `callback_id` 、 `block_id` 、および `action_id` (またはそれらの組み合わせ) をリッスンすることができます。オブジェクト内の制約には、文字列型または RegExp オブジェクトを使用できます。

```text
// action_id が 'select_user' と一致し、block_id が 'assign_ticket' と一致する場合のみミドルウェアが呼び出されるapp.action({ action_id: 'select_user', block_id: 'assign_ticket' },  async ({ body, client, ack, logger }) => {    await ack();    try {      if (body.message) {        const result = await client.reactions.add({          name: 'white_check_mark',          timestamp: body.message.ts,          channel: body.channel.id        });        logger.info(result);      }    }    catch (error) {      logger.error(error);    }  });
```text

## アクションへの応答 {#アクションへの応答}

アクションへの応答には、主に 2 つのやり方があります。1 つ目の (最も一般的な) やり方は `say` 関数の利用です。 `say` 関数は、Slack 内のリクエストが発生した会話（チャンネルや DM）へメッセージを返します。

アクションに応答する 2 つ目の方法は `respond()` です。これはアクションに紐付けられている `response_url` を用いたメッセージの送信をシンプルに行うためのユーティリティです。

```text
// action_id が "approve_button" のインタラクティブコンポーネントがトリガーされる毎にミドルウェアが呼び出されるapp.action('approve_button', async ({ ack, say }) => {  // アクションリクエストの確認  await ack();  await say('Request approved 👍');});
```text

### respond() の使用 {#respond-の使用}

`respond()` は `response_url` を呼び出すためのユーティリティであるため、それを直接使うときと同様に動作します。新しいメッセージのペイロードと、オプショナルな引数である `response_type` (値は `in_channel` または `ephemeral` )、 `replace_original` 、 `delete_original` を含む JSON オブジェクトを渡すことができます。

```text
// "user_select" の action_id がトリガーされたアクションをリッスンapp.action('user_select', async ({ action, ack, respond }) => {  await ack();  if (action.type === 'users_select') {    await respond(`You selected <@${action.selected_user}>`);  }});
```text
