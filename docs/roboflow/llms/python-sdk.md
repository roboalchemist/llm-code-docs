# Source: https://docs.roboflow.com/roboflow/roboflow-ko/deploy/serverless-hosted-api-v2/python-sdk.md

# Python SDK와 함께 사용

Python으로 작업하는 경우 Serverless API와 상호작용하는 가장 편리한 방법은 Inference Python SDK를 사용하는 것입니다.

사용하려면 [Inference SDK](https://inference.roboflow.com/inference_helpers/inference_sdk/)먼저 설치하세요:

```
pip install inference-sdk
```

Serverless Hosted API에 요청을 하려면 다음 코드를 사용하세요:

<pre class="language-python"><code class="lang-python"><strong>from inference_sdk import InferenceHTTPClient
</strong>
CLIENT = InferenceHTTPClient(
    api_url="https://serverless.roboflow.com",
    api_key="API_KEY"
)

result = CLIENT.infer("image.jpg", model_id="model-id/1")
print(result)
</code></pre>

위에서 귀하의 [model ID](https://docs.roboflow.com/developer/authentication/workspace-and-project-ids) 및 [API key](https://docs.roboflow.com/developer/authentication/find-your-roboflow-api-key)을 지정하세요. 이 코드는 모델을 실행하고 결과를 반환합니다.

#### Roboflow Instant Model

Serverless API는 Roboflow [Instant Model](https://docs.roboflow.com/roboflow/roboflow-ko/train/roboflow-instant)의 실행도 지원합니다. Instant Model은 다른 모델과 동일하게 실행할 수 있지만, Instant Models에서는 신뢰도 임계값(confidence threshold)이 민감할 수 있음을 유의하세요.

{% hint style="info" %}
최적의 신뢰도는 모델이 학습한 이미지 수에 따라 다릅니다. 일반적으로 최적의 신뢰도 임계값은 0.85에서 0.99 범위입니다.
{% endhint %}

```python
configuration = InferenceConfiguration(
    confidence_threshold=0.95
)
CLIENT.configure(configuration)

result = CLIENT.infer("image.jpg", model_id="roboflow-instant-model-id/1")
```
