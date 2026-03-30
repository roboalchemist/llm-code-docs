# Source: https://docs.roboflow.com/roboflow/roboflow-jp/depuroi/device-manager/wou/debaisuwosuru.md

# デバイス構成を更新する

### デプロイメントの設定

Deployment Manager の「Configuration」ページでは、デバイス上で実行されているサービスを管理できます。このガイドは主要な設定オプションの概要を提供します。

#### デバイス設定

デバイス名を変更したりタイムゾーンを更新したりできます。デバイス名は Deployment Manager のユーザーインターフェイス上の表示のためだけのもので、統合に影響を与えることはありません。タイムゾーンはログの表示や他のデバイスアクションのスケジューリングの調整に使用されます。デプロイの物理的な場所に合わせて設定することを強く推奨します。

<figure><img src="https://3740591140-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2FmQHwTiF9QV5aErJosQsq%2FScreenshot%202026-01-13%20at%2011.01.56%E2%80%AFAM.png?alt=media&#x26;token=1fcd7c77-2426-4767-aff1-f650e5aa7bbd" alt="" width="375"><figcaption></figcaption></figure>

#### 更新 / パフォーマンス設定

サービスごとのタブでサービスのバージョンを設定できます。バージョンは通常 Roboflow チームによって更新されます。&#x20;

<figure><img src="https://3740591140-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2FEP1uAKgx5XZukB7zcEfX%2FScreenshot%202026-01-13%20at%2011.02.25%E2%80%AFAM.png?alt=media&#x26;token=e2b59ba0-afda-4ebf-a83c-442aeffc05e4" alt=""><figcaption></figcaption></figure>

**バージョン表示の指標：**

* **緑色のチェックマーク** — 最新バージョンを実行しています
* **"Update available"** — より新しいバージョンが存在します

**自動更新** — このトグルを有効にすると（inference と manager サービスで利用可能）、設定したメンテナンスウィンドウ中に自動的に更新されます。

> **注意：** デバイスが設定と異なるバージョンを報告した場合、不一致の表示がされます。

**TensorRT を有効にする** — 推論を高速化するために TensorRT 最適化を有効にします。

***

#### 追加サービス

Roboflow では、ローカルイベントストア、デフォルトの HMI UI、テスト用の RTSP シミュレータなど、事前構成された追加サービスをデバイスに追加できます。これらはそれぞれ独自の設定オプションを持ち、各サービスを追加しようとすると必要に応じてプロンプトが表示されます。&#x20;

<figure><img src="https://3740591140-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2FX0g93AWHZ6brCnrNgYTF%2FScreenshot%202026-01-13%20at%2011.05.00%E2%80%AFAM.png?alt=media&#x26;token=1814c06b-3592-417c-be24-9863609d2748" alt="" width="563"><figcaption></figcaption></figure>
