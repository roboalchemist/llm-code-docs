# Source: https://docs.roboflow.com/roboflow/roboflow-jp/datasets/adding-data/metadta.md

# 画像メタデータ

Metadataでは、Roboflowのワークスペース内の画像にカスタムのキーと値のペアを添付できます。Metadataを使用して、撮影条件、デバイス識別子、品質スコア、またはドメイン固有の属性など、画像に構造化された情報を保存し、その属性でデータを検索、フィルタ、整理できます。

## 概要

各画像は任意の数のメタデータエントリを保持できます。エントリは **キー** （例えばのような名前 `camera_id`）とペアになった **値** （文字列、数値、またはブール値）。

| 値の種類 | 例                                           |
| ---- | ------------------------------------------- |
| 文字列  | `location: "warehouse-3"`, `shift: "night"` |
| 数値   | `temperature: 72.5`, `quality_score: 95`    |
| ブール値 | `reviewed: true`, `is_night: false`         |

### ユースケース

* **キャプチャのコンテキスト** — カメラID、GPS座標、天候、照明条件を記録する
* **品質追跡** — 信頼度スコア、レビュー状況、アノテータIDを添付する
* **データのスライシング** — 任意の属性でデータセットをフィルタしてターゲットトレーニングセットを構築する
* **外部システムとの連携** — 画像を内部ツールに結びつける識別子を保存する

## メタデータの追加

メタデータは、Web UI、Python SDK、REST API、またはS3 Bucket Mirrorを介して自動的に画像に追加できます。

### Webアプリケーション

{% stepper %}
{% step %}

### 画像を開く

プロジェクト内の任意の画像を開きます。
{% endstep %}

{% step %}

### キーと値を入力

メタデータセクションで、 **キー** を最初の入力欄に、 **値** を2番目の入力欄に入力します。
{% endstep %}

{% step %}

### 追加

を押す **Enter** で保存するか、Addをクリックします
{% endstep %}
{% endstepper %}

値は自動的に型解析されます：

| 入力された値           | 保存される型                  |
| ---------------- | ----------------------- |
| `front`          | `"front"` （文字列）         |
| `95`             | `95` （数値）               |
| `3.14`           | `3.14` （数値）             |
| `true` / `false` | `true` / `false` （ブール値） |

<figure><img src="https://3740591140-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fh7L2L0c22TIzCxjxuiU1%2Fimage.png?alt=media&#x26;token=3f3eba92-e194-43b4-bd98-801a038836ff" alt=""><figcaption><p>Annotation Toolのメタデータエディタ</p></figcaption></figure>

### Python SDK

アップロード時に `metadata` 辞書を渡します：

```python
import roboflow

rf = roboflow.Roboflow(api_key="YOUR_API_KEY")
project = rf.workspace("your-workspace").project("your-project")

project.upload(
    image_path="image.jpg",
    metadata={
        "camera_id": "cam001",
        "location": "warehouse-3",
        "temperature": 72.5,
        "is_night": False
    }
)
```

### REST API

#### アップロード時にメタデータを追加

multipart form dataで `metadata` フィールド（JSON文字列化）を含めます。画像をアップロードする際に：

```bash
curl -X POST "https://api.roboflow.com/dataset/your-dataset/upload?api_key=YOUR_API_KEY" \
  -F "name=image.jpg" \
  -F "split=train" \
  -F "file=@image.jpg" \
  -F 'metadata={"camera_id":"cam001","temperature":72.5}'
```

### S3 Bucket Mirror

を使用する場合、 [Bucket Mirror](https://docs.roboflow.com/roboflow/roboflow-jp/datasets/adding-data/broken-reference) でS3バケットから画像を同期する際、各画像と同じベース名の `.json` ファイルを画像と並べて配置することでメタデータを添付できます：

```
my-bucket/
  images/
    photo_001.jpg
    photo_001.json      # photo_001.jpgのメタデータ
    photo_002.jpg
    photo_002.json      # photo_002.jpgのメタデータ
```

JSONファイルはキーと値のペアとしてメタデータを含みます：

```json
{
    "camera_id": "cam001",
    "location": "warehouse-3",
    "capture": { "temperature": 72.5, "humidity": 45 }
}
```

**ネストされたオブジェクトは自動的にフラット化されます** ドット表記を使用して。上の例は次を生成します：

| キー                    | 値               |
| --------------------- | --------------- |
| `camera_id`           | `"cam001"`      |
| `location`            | `"warehouse-3"` |
| `capture.temperature` | `72.5`          |
| `capture.humidity`    | `45`            |

#### メタデータファイルの制約

* 最大ファイルサイズ： **256 KB**
* 有効なJSONであること
* `null` および `undefined` の値はフィルタされます

#### 更新戦略

Bucket Mirrorは、同期されたメタデータがUIまたはAPIで手動設定したメタデータとどのように相互作用するかについて、異なる戦略をサポートします：

| 戦略                            | 動作                                          |
| ----------------------------- | ------------------------------------------- |
| **`mergeBucketWins`** （デフォルト） | 両方のソースをマージします。キーの競合がある場合はバケットの値が優先されます。     |
| **`mergeUserWins`**           | 両方のソースをマージします。キーの競合がある場合はユーザーが設定した値が優先されます。 |
| **`overwrite`**               | バケットのメタデータが既存のすべてのメタデータを完全に置き換えます。          |
| **`untilFirstChange`**        | ユーザーが手動でメタデータを編集するまでバケットから同期し、その後は更新を停止します。 |
| **`append`**                  | バケットから新しいキーのみを追加します。既存のキーは上書きしません。          |

## メタデータによる検索

メタデータはインデックス化され、 [Asset Library](https://docs.roboflow.com/roboflow/roboflow-jp/datasets/adding-data/broken-reference)で検索可能です。検索バーを使用してメタデータ値で画像をフィルタします：

```
metadata.camera_id:"cam001"
metadata.quality_score>80
metadata.reviewed:true
```

メタデータフィルタは他の検索フィルタと組み合わせることができます：

```
metadata.location:"warehouse-3" AND class:forklift
```

Asset Libraryは、ワークスペース内に存在するキーと値に基づいてメタデータキーと値のオートコンプリートも提供します。

## キー命名規則

メタデータキーは次のルールに従う必要があります：

| ルール       | 詳細                                               |
| --------- | ------------------------------------------------ |
| 許可される文字   | 文字（`a-z`, `A-Z`）、数字（`0-9`）、アンダースコア（`_`）、ドット（`.`) |
| 最初の文字     | 最初の文字は文字、数字、またはアンダースコアでなければなりません                 |
| 禁止されている文字 | スラッシュ（`/`）は許可されていません                             |

有効なキー： `camera_id`, `capture.temperature`, `_internal_ref`, `v2_score`

無効なキー： `camera/id` （を含む `/`), `.starts_with_dot` （ドットで始まる `.`), `has spaces` （スペースを含む）

## メタデータとタグの違い

メタデータと [タグ](https://docs.roboflow.com/roboflow/roboflow-jp/datasets/adding-data/broken-reference) は画像の整理に役立ちますが、目的が異なります：

|           | タグ                                   | メタデータ                                      |
| --------- | ------------------------------------ | ------------------------------------------ |
| **構造**    | 単純なラベル                               | キーと値のペア                                    |
| **値**     | 値はなく名前のみ                             | 文字列、数値、またはブール値                             |
| **最適な用途** | 分類、ワークフローステータス                       | 構造化属性、測定値                                  |
| **例**     | `reviewed`, `v2`, `needs-annotation` | `temperature: 72.5`, `camera_id: "cam001"` |

同じ画像で両方を使用できます。たとえば、画像にタグとして `reviewed` を付け、さらに `reviewer: "alice"` および `confidence: 0.95` をメタデータとして保存できます。
