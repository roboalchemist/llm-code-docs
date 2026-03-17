# Source: https://docs.roboflow.com/roboflow/roboflow-jp/depuroi/device-manager/settoappu/mentenansuwindouwosuru.md

# メンテナンスウィンドウを設定する

デバイスの更新と構成変更が適用される日時をスケジュールできます。メンテナンスウィンドウは自動更新のための特定の時間帯を定義することで中断を制御し、重要な時間帯でも本番デバイスをスムーズに稼働させるのに役立ちます。

デフォルトでは、デバイスにはメンテナンスウィンドウが設定されておらず、すべての更新は即時に適用されます。

#### メンテナンスウィンドウを設定する

メンテナンスウィンドウを設定するには、Deployment Manager の特定のデバイスのダッシュボードに移動します。右上のオプションメニューに移動して「Maintenance Windows」をクリックしてください。

<figure><img src="https://3740591140-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2FULOXHZyuL5GEDGAnTkgf%2FScreenshot%202026-01-08%20at%2012.19.52%E2%80%AFPM.png?alt=media&#x26;token=a6ae3546-dc3b-4b0c-aa81-3761daa075a7" alt="" width="151"><figcaption></figcaption></figure>

その後、運用ニーズに応じて各デバイスのメンテナンスウィンドウを定義できます。更新を安全に適用できる特定の曜日と時間を選択してください。

主なオプション：

* **Timezone** — 正確なスケジュールのためにデバイスのローカルタイムゾーンを設定する
* **Per-day scheduling** — 曜日ごとに異なるウィンドウを構成する
* **Same time for all days** — 複数の日にわたって単一のスケジュールを使用する
* **Apply updates immediately** — 必要に応じてメンテナンスウィンドウをバイパスする&#x20;

<figure><img src="https://3740591140-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2FdXAgj1s498azMKSp2S8G%2FScreenshot%202026-01-08%20at%2012.21.00%E2%80%AFPM.png?alt=media&#x26;token=24ddac74-2aa0-451a-9d4c-6766c956668e" alt="" width="375"><figcaption></figcaption></figure>

#### Updates Outside of Mainenance Windows

メンテナンスウィンドウが設定されていても、クラウドの Roboflow Deployment Manager にアクセス権を持つユーザーは、必要に応じてメンテナンスウィンドウを上書きして更新を即時に適用することを選択できます。
