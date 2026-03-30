# Source: https://docs.roboflow.com/roboflow/roboflow-jp/depuroi/serverless-hosted-api-v2/python-sdk-tonisuru.md

# Python SDK と一緒に使用する

Pythonで作業している場合、Serverless APIとやり取りする最も便利な方法は、Inference Python SDKを使用することです。

を使用するには、 [Inference SDK](https://inference.roboflow.com/inference_helpers/inference_sdk/)、まずそれをインストールします:

```
pip install inference-sdk
```

Serverless Hosted APIにリクエストを行うには、次のコードを使用します:

<pre class="language-python"><code class="lang-python"><strong>from inference_sdk import InferenceHTTPClient
</strong>
CLIENT = InferenceHTTPClient(
    api_url="https://serverless.roboflow.com",
    api_key="API_KEY"
)

result = CLIENT.infer("image.jpg", model_id="model-id/1")
print(result)
</code></pre>

上記で、あなたの [model ID](https://docs.roboflow.com/developer/authentication/workspace-and-project-ids) と [API key](https://docs.roboflow.com/developer/authentication/find-your-roboflow-api-key)を指定してください。 このコードはモデルを実行し、結果を返します。

#### Roboflow Instant Model

Serverless APIはRoboflowの [Instant Model](https://docs.roboflow.com/roboflow/roboflow-jp/torningu/roboflow-instant)の実行もサポートしています。Instant Modelは他のモデルと同様に実行できますが、信頼度の閾値がInstant Modelでは敏感になることに注意してください。

{% hint style="info" %}
最適な信頼度は、モデルが学習した画像の数によって異なります。最適な信頼度の閾値は通常0.85から0.99の範囲です。
{% endhint %}

```python
configuration = InferenceConfiguration(
    confidence_threshold=0.95
)
CLIENT.configure(configuration)

result = CLIENT.infer("image.jpg", model_id="roboflow-instant-model-id/1")
```
