# Source: https://docs.roboflow.com/roboflow/roboflow-jp/depuroi/device-manager/wou/deployment-manager-wodepuroisuru.md

# Deployment Manager を再デプロイする

場合によっては、既存のデバイスに Deployment Manager を再デプロイしたいことがあります。これは、既存のデバイスが破損したり、回復不能なハードウェア障害が発生した場合に最も一般的です。&#x20;

手動で作業を行う代わりに、デバイスを再デプロイするだけで、Roboflow の構成を一度の手順で完全に復元できます。&#x20;

:warning: 最初のデバイスがまだ稼働中の間に、2 台目のデバイスに manager を再デプロイしないようにしてください。

新しいデバイスに再デプロイするには、そのデバイスの Deployment Manager ダッシュボードにアクセスしてください。次に、右上のオプションメニューを開き「Redeploy Device」をクリックします。

<figure><img src="https://3740591140-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fzfc395Dg7MilGGZApAY8%2FScreenshot%202026-01-08%20at%2011.16.35%E2%80%AFAM.png?alt=media&#x26;token=ebbfe3ab-2316-4ab8-a741-4ddfccb588b1" alt="" width="164"><figcaption></figcaption></figure>

次に「Generate Redeploy Command」をクリックしてインストールスクリプトを取得します。

<figure><img src="https://3740591140-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2FPrfqy0McmWUokdCMy8xo%2FScreenshot%202026-01-08%20at%2011.23.04%E2%80%AFAM.png?alt=media&#x26;token=d68dbabd-9d96-47bf-995c-ce409ea20255" alt="" width="375"><figcaption></figcaption></figure>

インストールスクリプトをコピーし、権限のある端末でデバイス上から実行してください。&#x20;

<figure><img src="https://3740591140-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2FMMEAsk7iDvN9rnPZxXvN%2FScreenshot%202026-01-08%20at%2011.25.29%E2%80%AFAM.png?alt=media&#x26;token=ce900b81-2fb8-442e-98d1-12a240990bd7" alt="" width="375"><figcaption></figcaption></figure>

:warning: インストールスクリプトは 10 分間のみ有効で、その後有効期限が切れることに注意してください。有効期限後は、インストールスクリプトを再生成する必要があります。
