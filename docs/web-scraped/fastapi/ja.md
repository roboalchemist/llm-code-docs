# Source: https://fastapi.tiangolo.com/ja/

Title: FastAPI

URL Source: https://fastapi.tiangolo.com/ja/

Markdown Content:
🌐 AI と人間による翻訳
この翻訳は、人間のガイドに基づいて AI によって作成されました。🤝

原文の意図を取り違えていたり、不自然な表現になっている可能性があります。🤖

[AI LLM をより適切に誘導するのを手伝う](https://fastapi.tiangolo.com/ja/contributing/#translations) ことで、この翻訳を改善できます。

[英語版](https://fastapi.tiangolo.com/)

[![Image 1: FastAPI](https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png)](https://fastapi.tiangolo.com/ja)

_FastAPI フレームワーク、高パフォーマンス、学びやすい、素早くコーディングできる、本番運用に対応_

[![Image 2: Test](https://github.com/fastapi/fastapi/actions/workflows/test.yml/badge.svg?event=push&branch=master)](https://github.com/fastapi/fastapi/actions?query=workflow%3ATest+event%3Apush+branch%3Amaster)[![Image 3: Coverage](https://coverage-badge.samuelcolvin.workers.dev/fastapi/fastapi.svg)](https://coverage-badge.samuelcolvin.workers.dev/redirect/fastapi/fastapi)[![Image 4: Package version](https://img.shields.io/pypi/v/fastapi?color=%2334D058&label=pypi%20package)](https://pypi.org/project/fastapi)[![Image 5: Supported Python versions](https://img.shields.io/pypi/pyversions/fastapi.svg?color=%2334D058)](https://pypi.org/project/fastapi)

* * *

**ドキュメント**: [https://fastapi.tiangolo.com](https://fastapi.tiangolo.com/ja)

**ソースコード**: [https://github.com/fastapi/fastapi](https://github.com/fastapi/fastapi)

* * *

FastAPI は、Python の標準である型ヒントに基づいて Python で API を構築するための、モダンで、高速（高パフォーマンス）な Web フレームワークです。

主な特徴:

*   **高速**: **NodeJS** や **Go** 並みのとても高いパフォーマンス（Starlette と Pydantic のおかげです）。 [利用可能な最も高速な Python フレームワークの一つです](https://fastapi.tiangolo.com/ja/#performance)。
*   **高速なコーディング**: 開発速度を約 200%〜300% 向上させます。*
*   **少ないバグ**: 開発者起因のヒューマンエラーを約 40% 削減します。*
*   **直感的**: 素晴らしいエディタサポート。補完 があらゆる場所で使えます。デバッグ時間を削減します。
*   **簡単**: 簡単に利用・習得できるようにデザインされています。ドキュメントを読む時間を削減します。
*   **短い**: コードの重複を最小限にします。各パラメータ宣言から複数の機能を得られます。バグも減ります。
*   **堅牢性**: 自動対話型ドキュメントにより、本番環境向けのコードが得られます。
*   **Standards-based**: API のオープンスタンダードに基づいており（そして完全に互換性があります）、[OpenAPI](https://github.com/OAI/OpenAPI-Specification)（以前は Swagger として知られていました）や [JSON Schema](https://json-schema.org/) をサポートします。

* 本番アプリケーションを構築している社内開発チームのテストに基づく見積もりです。

[![Image 6](https://fastapi.tiangolo.com/img/sponsors/fastapicloud.png)](https://fastapicloud.com/ "FastAPI Cloud. By the same team behind FastAPI. You code. We Cloud.")

### Gold and Silver Sponsors[¶](https://fastapi.tiangolo.com/ja/#gold-and-silver-sponsors)

[![Image 7](https://fastapi.tiangolo.com/img/sponsors/blockbee.png)](https://blockbee.io/?ref=fastapi "BlockBee Cryptocurrency Payment Gateway")[![Image 8](https://fastapi.tiangolo.com/img/sponsors/scalar.svg)](https://github.com/scalar/scalar/?utm_source=fastapi&utm_medium=website&utm_campaign=main-badge "Scalar: Beautiful Open-Source API References from Swagger/OpenAPI files")[![Image 9](https://fastapi.tiangolo.com/img/sponsors/propelauth.png)](https://www.propelauth.com/?utm_source=fastapi&utm_campaign=1223&utm_medium=mainbadge "Auth, user management and more for your B2B product")[![Image 10](https://fastapi.tiangolo.com/img/sponsors/zuplo.png)](https://zuplo.link/fastapi-gh "Zuplo: Deploy, Secure, Document, and Monetize your FastAPI")[![Image 11](https://fastapi.tiangolo.com/img/sponsors/liblab.png)](https://liblab.com/?utm_source=fastapi "liblab - Generate SDKs from FastAPI")[![Image 12](https://fastapi.tiangolo.com/img/sponsors/render.svg)](https://docs.render.com/deploy-fastapi?utm_source=deploydoc&utm_medium=referral&utm_campaign=fastapi "Deploy & scale any full-stack web app on Render. Focus on building apps, not infra.")[![Image 13](https://fastapi.tiangolo.com/img/sponsors/coderabbit.png)](https://www.coderabbit.ai/?utm_source=fastapi&utm_medium=badge&utm_campaign=fastapi "Cut Code Review Time & Bugs in Half with CodeRabbit")[![Image 14](https://fastapi.tiangolo.com/img/sponsors/subtotal.svg)](https://subtotal.com/?utm_source=fastapi&utm_medium=sponsorship&utm_campaign=open-source "The Gold Standard in Retail Account Linking")[![Image 15](https://fastapi.tiangolo.com/img/sponsors/railway.png)](https://docs.railway.com/guides/fastapi?utm_medium=integration&utm_source=docs&utm_campaign=fastapi "Deploy enterprise applications at startup speed")[![Image 16](https://fastapi.tiangolo.com/img/sponsors/serpapi.png)](https://serpapi.com/?utm_source=fastapi_website "SerpApi: Web Search API")[![Image 17](https://fastapi.tiangolo.com/img/sponsors/greptile.png)](https://www.greptile.com/?utm_source=fastapi&utm_medium=sponsorship&utm_campaign=fastapi_sponsor_page "Greptile: The AI Code Reviewer")[![Image 18](https://fastapi.tiangolo.com/img/sponsors/databento.svg)](https://databento.com/?utm_source=fastapi&utm_medium=sponsor&utm_content=display "Pay as you go for market data")[![Image 19](https://fastapi.tiangolo.com/img/sponsors/speakeasy.png)](https://speakeasy.com/editor?utm_source=fastapi+repo&utm_medium=github+sponsorship "SDKs for your API | Speakeasy")[![Image 20](https://fastapi.tiangolo.com/img/sponsors/svix.svg)](https://www.svix.com/ "Svix - Webhooks as a service")[![Image 21](https://fastapi.tiangolo.com/img/sponsors/stainless.png)](https://www.stainlessapi.com/?utm_source=fastapi&utm_medium=referral "Stainless | Generate best-in-class SDKs")[![Image 22](https://fastapi.tiangolo.com/img/sponsors/permit.png)](https://www.permit.io/blog/implement-authorization-in-fastapi?utm_source=github&utm_medium=referral&utm_campaign=fastapi "Fine-Grained Authorization for FastAPI")[![Image 23](https://fastapi.tiangolo.com/img/sponsors/interviewpal.png)](https://www.interviewpal.com/?utm_source=fastapi&utm_medium=open-source&utm_campaign=dev-hiring "InterviewPal - AI Interview Coach for Engineers and Devs")[![Image 24](https://fastapi.tiangolo.com/img/sponsors/dribia.png)](https://dribia.com/en/ "Dribia - Data Science within your reach")

[その他のスポンサー](https://fastapi.tiangolo.com/ja/fastapi-people/#sponsors)

評価[¶](https://fastapi.tiangolo.com/ja/#opinions)
------------------------------------------------

"_[...] 最近 **FastAPI** を使っています。 [...] 実際に私のチームの全ての **Microsoft の機械学習サービス** で使用する予定です。 そのうちのいくつかのコアな **Windows** 製品と **Office** 製品に統合されつつあります。_"

Kabir Khan - **Microsoft**[(ref)](https://github.com/fastapi/fastapi/pull/26)

* * *

"_FastAPIライブラリを採用し、クエリで **予測値** を取得できる **REST** サーバを構築しました。 [for Ludwig]_"

Piero Molino, Yaroslav Dudin, and Sai Sumanth Miryala - **Uber**[(ref)](https://eng.uber.com/ludwig-v0-2/)

* * *

"_**Netflix** は、**危機管理**オーケストレーションフレームワーク、**Dispatch** のオープンソースリリースを発表できることをうれしく思います。 [built with **FastAPI**]_"

Kevin Glisson, Marc Vilanova, Forest Monsen - **Netflix**[(ref)](https://netflixtechblog.com/introducing-dispatch-da4b8a2a8072)

* * *

"_私は **FastAPI** にワクワクしています。 めちゃくちゃ楽しいです！_"

* * *

"_正直、あなたが作ったものは超堅実で洗練されているように見えます。いろんな意味で、それは私が **Hug** にそうなってほしかったものです。誰かがそれを作るのを見るのは本当に刺激的です。_"

Timothy Crosley - **[Hug](https://github.com/hugapi/hug) creator**[(ref)](https://news.ycombinator.com/item?id=19455465)

* * *

"_REST API を構築するための **モダンなフレームワーク** を学びたい方は、**FastAPI** [...] をチェックしてみてください。 [...] 高速で、使用・習得が簡単です [...]_"

"_私たちの **API** は **FastAPI** に切り替えました [...] きっと気に入ると思います [...]_"

* * *

"_本番運用の Python API を構築したい方には、**FastAPI** を強くおすすめします。**美しく設計**されており、**使いやすく**、**高いスケーラビリティ**があります。私たちの API ファースト開発戦略の **主要コンポーネント** となり、Virtual TAC Engineer などの多くの自動化やサービスを推進しています。_"

Deon Pillsbury - **Cisco**[(ref)](https://www.linkedin.com/posts/deonpillsbury_cisco-cx-python-activity-6963242628536487936-trAp/)

* * *

FastAPI ミニドキュメンタリー[¶](https://fastapi.tiangolo.com/ja/#fastapi-mini-documentary)
--------------------------------------------------------------------------------

2025 年末に公開された [FastAPI ミニドキュメンタリー](https://www.youtube.com/watch?v=mpR8ngthqiE)があります。オンラインで視聴できます:

[![Image 25: FastAPI Mini Documentary](https://fastapi.tiangolo.com/img/fastapi-documentary.jpg)](https://www.youtube.com/watch?v=mpR8ngthqiE)

**Typer**、CLI 版 FastAPI[¶](https://fastapi.tiangolo.com/ja/#typer-the-fastapi-of-clis)
--------------------------------------------------------------------------------------

[![Image 26](https://typer.tiangolo.com/img/logo-margin/logo-margin-vector.svg)](https://typer.tiangolo.com/)

Web API の代わりにターミナルで使用する CLI アプリを構築する場合は、[**Typer**](https://typer.tiangolo.com/) を確認してください。

**Typer** は FastAPI の弟分です。そして、**CLI 版 FastAPI** を意図しています。 ⌨️ 🚀

必要条件[¶](https://fastapi.tiangolo.com/ja/#requirements)
------------------------------------------------------

FastAPI は巨人の肩の上に立っています。

*   Web の部分は [Starlette](https://www.starlette.dev/)
*   データの部分は [Pydantic](https://docs.pydantic.dev/)

インストール[¶](https://fastapi.tiangolo.com/ja/#installation)
--------------------------------------------------------

[virtual environment](https://fastapi.tiangolo.com/ja/virtual-environments/) を作成して有効化し、それから FastAPI をインストールします。

**注**: すべてのターミナルで動作するように、`"fastapi[standard]"` は必ずクォートで囲んでください。

アプリケーション例[¶](https://fastapi.tiangolo.com/ja/#example)
------------------------------------------------------

### 作成[¶](https://fastapi.tiangolo.com/ja/#create-it)

`main.py` ファイルを作成し、以下のコードを入力します。

```
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}
```

または `async def` を使います...
コードで `async` / `await` を使用する場合は、`async def` を使います。

```
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}
```

**注**:

わからない場合は、[ドキュメントの `async` と `await` の _"In a hurry?"_ セクション](https://fastapi.tiangolo.com/ja/async/#in-a-hurry)を確認してください。

### 実行[¶](https://fastapi.tiangolo.com/ja/#run-it)

以下のコマンドでサーバーを起動します。

`fastapi dev main.py` コマンドについて
`fastapi dev` コマンドは `main.py` ファイルを読み取り、その中の **FastAPI** アプリを検出し、[Uvicorn](https://www.uvicorn.dev/) を使用してサーバーを起動します。

デフォルトでは、`fastapi dev` はローカル開発向けに自動リロードを有効にして起動します。

詳しくは [FastAPI CLI docs](https://fastapi.tiangolo.com/ja/fastapi-cli/) を参照してください。

### 動作確認[¶](https://fastapi.tiangolo.com/ja/#check-it)

ブラウザで [http://127.0.0.1:8000/items/5?q=somequery](http://127.0.0.1:8000/items/5?q=somequery) を開きます。

以下の JSON のレスポンスが確認できます。

```
{"item_id": 5, "q": "somequery"}
```

すでに以下の API が作成されています。

*   _パス_`/` と `/items/{item_id}` で HTTP リクエストを受け取ります。
*   両方の _パス_ は `GET`_操作_（HTTP _メソッド_ としても知られています）を取ります。
*   _パス_`/items/{item_id}` は `int` であるべき _パスパラメータ_`item_id` を持ちます。
*   _パス_`/items/{item_id}` はオプションの `str`_クエリパラメータ_`q` を持ちます。

### 自動対話型 API ドキュメント[¶](https://fastapi.tiangolo.com/ja/#interactive-api-docs)

次に、[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) にアクセスします。

自動対話型 API ドキュメントが表示されます（[Swagger UI](https://github.com/swagger-api/swagger-ui) が提供しています）。

![Image 27: Swagger UI](https://fastapi.tiangolo.com/img/index/index-01-swagger-ui-simple.png)

### 代替 API ドキュメント[¶](https://fastapi.tiangolo.com/ja/#alternative-api-docs)

次に、[http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc) にアクセスします。

代替の自動ドキュメントが表示されます（[ReDoc](https://github.com/Rebilly/ReDoc) が提供しています）。

![Image 28: ReDoc](https://fastapi.tiangolo.com/img/index/index-02-redoc-simple.png)

アップグレード例[¶](https://fastapi.tiangolo.com/ja/#example-upgrade)
-------------------------------------------------------------

次に、`PUT` リクエストからボディを受け取るために `main.py` ファイルを修正しましょう。

Pydantic によって、標準的な Python の型を使ってボディを宣言します。

```
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: bool | None = None

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}
```

`fastapi dev` サーバーは自動でリロードされるはずです。

### 自動対話型 API ドキュメントのアップグレード[¶](https://fastapi.tiangolo.com/ja/#interactive-api-docs-upgrade)

次に、[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) にアクセスします。

*   自動対話型 API ドキュメントは新しいボディも含めて自動でアップデートされます。

![Image 29: Swagger UI](https://fastapi.tiangolo.com/img/index/index-03-swagger-02.png)

*   「Try it out」ボタンをクリックします。パラメータを入力して API と直接やりとりできます。

![Image 30: Swagger UI interaction](https://fastapi.tiangolo.com/img/index/index-04-swagger-03.png)

*   次に、「Execute」ボタンをクリックします。ユーザーインターフェースは API と通信し、パラメータを送信し、結果を取得して画面に表示します。

![Image 31: Swagger UI interaction](https://fastapi.tiangolo.com/img/index/index-05-swagger-04.png)

### 代替 API ドキュメントのアップグレード[¶](https://fastapi.tiangolo.com/ja/#alternative-api-docs-upgrade)

次に、[http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc) にアクセスします。

*   代替のドキュメントにも新しいクエリパラメータやボディが反映されます。

![Image 32: ReDoc](https://fastapi.tiangolo.com/img/index/index-06-redoc-02.png)

### まとめ[¶](https://fastapi.tiangolo.com/ja/#recap)

要約すると、関数のパラメータとして、パラメータやボディなどの型を **一度だけ** 宣言します。

標準的な最新の Python の型を使います。

新しい構文や特定のライブラリのメソッドやクラスなどを覚える必要はありません。

単なる標準的な **Python** です。

例えば、`int` の場合:

```
item_id: int
```

または、より複雑な `Item` モデルの場合:

```
item: Item
```

...そして、この一度の宣言で、以下のようになります。

*   以下を含むエディタサポート:
    *   補完。
    *   型チェック。

*   データの検証:
    *   データが無効な場合に自動で明確なエラーを返します。
    *   深い入れ子になった JSON オブジェクトでも検証が可能です。

*   入力データの 変換: ネットワークから Python のデータや型へ。以下から読み取ります:
    *   JSON。
    *   パスパラメータ。
    *   クエリパラメータ。
    *   Cookie。
    *   ヘッダー。
    *   フォーム。
    *   ファイル。

*   出力データの 変換: Python のデータや型からネットワークデータへ（JSON として）変換します:
    *   Python の型（`str`、`int`、`float`、`bool`、`list` など）の変換。
    *   `datetime` オブジェクト。
    *   `UUID` オブジェクト。
    *   データベースモデル。
    *   ...などなど。

*   2 つの代替ユーザーインターフェースを含む自動対話型 API ドキュメント:
    *   Swagger UI。
    *   ReDoc。

* * *

前のコード例に戻ると、**FastAPI** は次のように動作します。

*   `GET` および `PUT` リクエストのパスに `item_id` があることを検証します。
*   `GET` および `PUT` リクエストに対して `item_id` が `int` 型であることを検証します。
    *   そうでない場合、クライアントは有用で明確なエラーを受け取ります。

*   `GET` リクエストに対して、`q` という名前のオプションのクエリパラメータ（`http://127.0.0.1:8000/items/foo?q=somequery` のような）が存在するかどうかを調べます。
    *   `q` パラメータは `= None` で宣言されているため、オプションです。
    *   `None` がなければ必須になります（`PUT` の場合のボディと同様です）。

*   `PUT` リクエストを `/items/{item_id}` に送信する場合、ボディを JSON として読み込みます:
    *   必須の属性 `name` があり、`str` であるべきことを確認します。
    *   必須の属性 `price` があり、`float` でなければならないことを確認します。
    *   オプションの属性 `is_offer` があり、存在する場合は `bool` であるべきことを確認します。
    *   これらはすべて、深くネストされた JSON オブジェクトに対しても動作します。

*   JSON への/からの変換を自動的に行います。
*   OpenAPI ですべてを文書化し、以下で利用できます:
    *   対話型ドキュメントシステム。
    *   多くの言語に対応した自動クライアントコード生成システム。

*   2 つの対話型ドキュメント Web インターフェースを直接提供します。

* * *

まだ表面的な部分に触れただけですが、仕組みはすでにイメージできているはずです。

以下の行を変更してみてください。

```
return {"item_name": item.name, "item_id": item_id}
```

...以下の:

```
... "item_name": item.name ...
```

...を:

```
... "item_price": item.price ...
```

...に変更し、エディタが属性を自動補完し、その型を知ることを確認してください。

![Image 33: editor support](https://fastapi.tiangolo.com/img/vscode-completion.png)

より多くの機能を含む、より完全な例については、[Tutorial - User Guide](https://fastapi.tiangolo.com/ja/tutorial/) を参照してください。

**ネタバレ注意**: tutorial - user guide には以下が含まれます。

*   **ヘッダー**、**Cookie**、**フォームフィールド**、**ファイル**など、他のさまざまな場所からの **パラメータ** 宣言。
*   `maximum_length` や `regex` のような **検証制約** を設定する方法。
*   非常に強力で使いやすい **依存性注入** システム。
*   **JWT トークン**を用いた **OAuth2** や **HTTP Basic** 認証のサポートを含む、セキュリティと認証。
*   **深くネストされた JSON モデル**を宣言するための、より高度な（しかし同様に簡単な）手法（Pydantic のおかげです）。
*   [Strawberry](https://strawberry.rocks/) および他のライブラリによる **GraphQL** 統合。
*   以下のようなたくさんのおまけ機能（Starlette のおかげです）:
    *   **WebSockets**
    *   HTTPX と `pytest` に基づく極めて簡単なテスト
    *   **CORS**
    *   **Cookie Sessions**
    *   ...などなど。

### アプリをデプロイ（任意）[¶](https://fastapi.tiangolo.com/ja/#deploy-your-app-optional)

必要に応じて FastAPI アプリを [FastAPI Cloud](https://fastapicloud.com/) にデプロイできます。まだの場合はウェイティングリストに参加してください。 🚀

すでに **FastAPI Cloud** アカウント（ウェイティングリストから招待されました 😉）がある場合は、1 コマンドでアプリケーションをデプロイできます。

デプロイ前に、ログインしていることを確認してください。

次に、アプリをデプロイします。

これで完了です！その URL でアプリにアクセスできます。 ✨

#### FastAPI Cloud について[¶](https://fastapi.tiangolo.com/ja/#about-fastapi-cloud)

**[FastAPI Cloud](https://fastapicloud.com/)** は **FastAPI** の作者と同じチームによって作られています。

最小限の労力で API を **構築**、**デプロイ**、**アクセス** するためのプロセスを効率化します。

FastAPI でアプリを構築するのと同じ **開発者体験** を、クラウドへの **デプロイ** にももたらします。 🎉

FastAPI Cloud は _FastAPI and friends_ オープンソースプロジェクトの主要スポンサーであり、資金提供元です。 ✨

#### 他のクラウドプロバイダにデプロイ[¶](https://fastapi.tiangolo.com/ja/#deploy-to-other-cloud-providers)

FastAPI はオープンソースであり、標準に基づいています。選択した任意のクラウドプロバイダに FastAPI アプリをデプロイできます。

各クラウドプロバイダのガイドに従って、FastAPI アプリをデプロイしてください。 🤓

パフォーマンス[¶](https://fastapi.tiangolo.com/ja/#performance)
--------------------------------------------------------

独立した TechEmpower のベンチマークでは、Uvicorn で動作する **FastAPI** アプリケーションが、[利用可能な最も高速な Python フレームワークの一つ](https://www.techempower.com/benchmarks/#section=test&runid=7464e520-0dc2-473d-bd34-dbdfd7e85911&hw=ph&test=query&l=zijzen-7)であり、Starlette と Uvicorn（FastAPI で内部的に使用されています）にのみ下回っていると示されています。（*）

詳細は [Benchmarks](https://fastapi.tiangolo.com/ja/benchmarks/) セクションをご覧ください。

依存関係[¶](https://fastapi.tiangolo.com/ja/#dependencies)
------------------------------------------------------

FastAPI は Pydantic と Starlette に依存しています。

### `standard` 依存関係[¶](https://fastapi.tiangolo.com/ja/#standard-dependencies)

FastAPI を `pip install "fastapi[standard]"` でインストールすると、`standard` グループのオプション依存関係が含まれます。

Pydantic によって使用されるもの:

*   [`email-validator`](https://github.com/JoshData/python-email-validator) - メール検証のため。

Starlette によって使用されるもの:

*   [`httpx`](https://www.python-httpx.org/) - `TestClient` を使用したい場合に必要です。
*   [`jinja2`](https://jinja.palletsprojects.com/) - デフォルトのテンプレート設定を使用したい場合に必要です。
*   [`python-multipart`](https://github.com/Kludex/python-multipart) - `request.form()` とともに、フォームの 「parsing」 をサポートしたい場合に必要です。

FastAPI によって使用されるもの:

*   [`uvicorn`](https://www.uvicorn.dev/) - アプリケーションをロードして提供するサーバーのため。これには `uvicorn[standard]` も含まれ、高性能なサービングに必要な依存関係（例: `uvloop`）が含まれます。
*   `fastapi-cli[standard]` - `fastapi` コマンドを提供します。
    *   これには `fastapi-cloud-cli` が含まれ、FastAPI アプリケーションを [FastAPI Cloud](https://fastapicloud.com/) にデプロイできます。

### `standard` 依存関係なし[¶](https://fastapi.tiangolo.com/ja/#without-standard-dependencies)

`standard` のオプション依存関係を含めたくない場合は、`pip install "fastapi[standard]"` の代わりに `pip install fastapi` でインストールできます。

### `fastapi-cloud-cli` なし[¶](https://fastapi.tiangolo.com/ja/#without-fastapi-cloud-cli)

標準の依存関係を含めつつ `fastapi-cloud-cli` を除外して FastAPI をインストールしたい場合は、`pip install "fastapi[standard-no-fastapi-cloud-cli]"` でインストールできます。

### 追加のオプション依存関係[¶](https://fastapi.tiangolo.com/ja/#additional-optional-dependencies)

追加でインストールしたい依存関係があります。

追加のオプション Pydantic 依存関係:

*   [`pydantic-settings`](https://docs.pydantic.dev/latest/usage/pydantic_settings/) - 設定管理のため。
*   [`pydantic-extra-types`](https://docs.pydantic.dev/latest/usage/types/extra_types/extra_types/) - Pydantic で使用する追加の型のため。

追加のオプション FastAPI 依存関係:

*   [`orjson`](https://github.com/ijl/orjson) - `ORJSONResponse` を使用したい場合に必要です。
*   [`ujson`](https://github.com/esnme/ultrajson) - `UJSONResponse` を使用したい場合に必要です。

ライセンス[¶](https://fastapi.tiangolo.com/ja/#license)
--------------------------------------------------

このプロジェクトは MIT ライセンスの条項の下でライセンスされています。
